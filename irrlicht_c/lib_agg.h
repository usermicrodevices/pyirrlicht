// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#include "agg_scanline_p.h"
//#include "agg_renderer_scanline.h"
//#include "agg_pixfmt_rgba.h"
//#include "agg_rasterizer_scanline_aa.h"

#include "agg_basics.h"
#include "agg_rendering_buffer.h"
#include "agg_rasterizer_scanline_aa.h"
#include "agg_renderer_scanline.h"
//#include "agg_pixfmt_rgb.h"
#include "agg_pixfmt_rgba.h"

#include "agg_svg_parser.h"

using namespace agg;
using namespace svg;

//#include "..\..\agg-2.5\src\agg_curves.cpp"
//#include "..\..\agg-2.5\src\agg_trans_affine.cpp"
//#include "..\..\agg-2.5\src\agg_vcgen_contour.cpp"
//#include "..\..\agg-2.5\src\agg_vcgen_stroke.cpp"
//#include "..\..\agg-2.5\examples\svg_viewer\agg_svg_parser.cpp"
//#include "..\..\agg-2.5\examples\svg_viewer\agg_svg_path_renderer.cpp"
//#include "..\..\agg-2.5\examples\svg_viewer\agg_svg_path_tokenizer.cpp"

//typedef agg::pixfmt_bgra32 agg_pixel_type;
typedef row_accessor<irr::u32> rendering_buffer_u32;
typedef pixfmt_alpha_blend_rgba<blender_bgra32, rendering_buffer_u32, pixel32_type> agg_pixel_type;
//typedef pixfmt_alpha_blend_rgba<blender_argb32, rendering_buffer_u32, pixel32_type> agg_pixel_type;

class svg_viewer
{
public:
	svg_viewer()
	{
		alpha_value = 0;
		m_min_x = 0.0;
		m_min_y = 0.0;
		m_max_x = 0.0;
		m_max_y = 0.0;
		stride_value = 1;
		color_format = ECF_A8R8G8B8;
		file_name = "tiger.svg";
		agg::svg::parser p(m_path);
		p.parse(file_name);
		m_path.arrange_orientations();
		m_path.bounding_rect(&m_min_x, &m_min_y, &m_max_x, &m_max_y);
		texture = 0;
	}
	void set_video_driver(IVideoDriver* drv){driver = drv;}
	void scale(double scale_value = 1.0)
	{
		m_max_x *= scale_value;
		m_max_y *= scale_value;
		const dimension2d<u32>& image_size = dimension2d<u32>((irr::u32)m_max_x, (irr::u32)m_max_y);
		IImage* image = driver->createImage(color_format, image_size);
		rendering_buffer_u32 rbuf((irr::u32*)image->lock(), image_size.Width, image_size.Height, image_size.Width*stride_value);
		agg_pixel_type pixf(rbuf);
		agg::renderer_base<agg_pixel_type> renb(pixf);
		agg::renderer_scanline_aa_solid<agg::renderer_base<agg_pixel_type>> ren(renb);
		renb.clear(agg::rgba8(255, 255, 255, alpha_value));
		agg::rasterizer_scanline_aa<> ras;
		agg::scanline_p8 sl;
		agg::trans_affine mtx;
		mtx *= agg::trans_affine_scaling(scale_value);
		agg::render_scanlines(ras, sl, ren);
		m_path.render(ras, sl, ren, mtx, renb.clip_box(), 1.0);
		image->unlock();
		driver->removeTexture(texture);
		texture = driver->addTexture(file_name, image);
		image->drop();
		if (image)
			delete image;
	}
	ITexture* get_texture(){return texture;}
	~svg_viewer()
	{
		//m_path = NULL;
	}
private:
	const char* file_name;
	agg::svg::path_renderer m_path;
	u32 alpha_value;
	double m_min_x;
	double m_min_y;
	double m_max_x;
	double m_max_y;
	video::ECOLOR_FORMAT color_format;
	int stride_value;
	IVideoDriver* driver;
	ITexture* texture;
};

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API svg_viewer* svg_viewer_ctor(){return new svg_viewer();}
IRRLICHT_C_API void svg_viewer_set_video_driver(svg_viewer* pointer, IVideoDriver* drv){pointer->set_video_driver(drv);}
IRRLICHT_C_API void svg_viewer_scale(svg_viewer* pointer, double scale_value = 1.0){pointer->scale(scale_value);}
IRRLICHT_C_API ITexture* svg_viewer_get_texture(svg_viewer* pointer){return pointer->get_texture();}

IRRLICHT_C_API ITexture* tool_texture_from_svg(IVideoDriver* driver, char* file_name = "tiger.svg", video::ECOLOR_FORMAT color_format = ECF_A8R8G8B8, char* texture_name = "texture_01", u32 alpha_value = 0)
{
	double scale_value = 1.0;
	double rotate_value = 180.0;
	double expand_value = 0.0;
	double m_min_x = 0.0;
	double m_min_y = 0.0;
	double m_max_x = 0.0;
	double m_max_y = 0.0;
	double m_x = 0.0;
	double m_y = 0.0;

	agg::svg::path_renderer m_path;
	agg::svg::parser p(m_path);
	p.parse(file_name);
	m_path.arrange_orientations();
	m_path.bounding_rect(&m_min_x, &m_min_y, &m_max_x, &m_max_y);

	const dimension2d<u32> image_size = dimension2d<u32>((irr::u32)m_max_x, (irr::u32)m_max_y);
	IImage* image = driver->createImage(color_format, image_size);

	agg::rendering_buffer rbuf;
	rbuf.attach((unsigned char*)image->lock(), image_size.Width, image_size.Height, -(int)(image_size.Width*4));

	// Pixel format and basic primitives renderer
	agg::pixfmt_bgra32 pixf(rbuf);
	agg::renderer_base<agg::pixfmt_bgra32> renb(pixf);

	renb.clear(agg::rgba8(255, 255, 255, alpha_value));

	// Scanline renderer for solid filling.
	agg::renderer_scanline_aa_solid<agg::renderer_base<agg::pixfmt_bgra32> > ren(renb);

	// Rasterizer & scanline
	agg::rasterizer_scanline_aa<> ras;
	agg::scanline_p8 sl;
	agg::trans_affine mtx;
	mtx *= agg::trans_affine_translation((m_min_x + m_max_x) * -0.5, (m_min_y + m_max_y) * -0.5);
	mtx *= agg::trans_affine_scaling(scale_value);
	mtx *= agg::trans_affine_rotation(agg::deg2rad(rotate_value));
	mtx *= agg::trans_affine_translation((m_min_x + m_max_x) * 0.5 + m_x, (m_min_y + m_max_y) * 0.5 + m_y + 30);

	// Rendering
	agg::render_scanlines(ras, sl, ren);

	m_path.expand(expand_value);
	//start_timer();
	m_path.render(ras, sl, ren, mtx, renb.clip_box(), 1.0);

	image->unlock();
	return driver->addTexture(texture_name, image);
}

IRRLICHT_C_API ITexture* tool_texture_from_test_vectors(IVideoDriver* driver, video::ECOLOR_FORMAT image_format = ECF_R8G8B8, const dimension2d<u32>& image_size = dimension2d<u32>(640, 480), char* texture_name = "texture_01", u32 alpha_value = 128)
{
	IImage* image = driver->createImage(image_format, image_size);
	int alpha = 0;
	bool blend = false;
	video::ECOLOR_FORMAT color_format = image->getColorFormat();
	if (color_format == ECF_A1R5G5B5 || color_format == ECF_A8R8G8B8 || color_format == ECF_A16B16G16R16F || color_format == ECF_A32B32G32R32F)
	{
		alpha = alpha_value;
		blend = true;
	}

	//void* buf = image->lock();

	agg::rendering_buffer rbuf;
	rbuf.attach((unsigned char*)image->lock(), image_size.Width, image_size.Height, -(int)(image_size.Width*4));

	// Pixel format and basic primitives renderer
	agg::pixfmt_bgra32 pixf(rbuf);
	agg::renderer_base<agg::pixfmt_bgra32> renb(pixf);

	renb.clear(agg::rgba8(255, 255, 255, 255));

	// Scanline renderer for solid filling.
	agg::renderer_scanline_aa_solid<agg::renderer_base<agg::pixfmt_bgra32> > ren(renb);

	// Rasterizer & scanline
	agg::rasterizer_scanline_aa<> ras;
	agg::scanline_p8 sl;

	// Polygon (triangle)
	ras.move_to_d(20.7, 34.15);
	ras.line_to_d(398.23, 123.43);
	ras.line_to_d(165.45, 401.87);

	// Setting the attrribute (color) & Rendering
	ren.color(agg::rgba8(80, 90, 60));
	agg::render_scanlines(ras, sl, ren);

	image->unlock();
	return driver->addTexture(texture_name, image);
}

IRRLICHT_C_API agg::svg::path_renderer* agg_svg_path(fschar_t* file_name = "tiger.svg")
{
	//agg::svg::path_renderer& m_path = *(new path_renderer());
	//agg::svg::parser p(m_path);
	//p.parse(file_name);
	//return &m_path;
	agg::svg::path_renderer* m_path = new path_renderer();
	agg::svg::parser p(*m_path);
	p.parse(file_name);
	return m_path;
}

IRRLICHT_C_API IImage* agg_svg_IImage(agg::svg::path_renderer* m_path, IVideoDriver* driver, double scale_value = 1.0, double rotate_value = 0.0, double expand_value = 0.0, video::ECOLOR_FORMAT color_format = ECF_A8R8G8B8, u32 alpha_value = 0, int stride_value = 1)
{
	double m_min_x = 0.0;
	double m_min_y = 0.0;
	double m_max_x = 0.0;
	double m_max_y = 0.0;

	//m_path->arrange_orientations();
	m_path->bounding_rect(&m_min_x, &m_min_y, &m_max_x, &m_max_y);
	m_max_x *= scale_value;
	m_max_y *= scale_value;

	const dimension2d<u32>& image_size = dimension2d<u32>((irr::u32)m_max_x, (irr::u32)m_max_y);
	IImage* image = driver->createImage(color_format, image_size);

	typedef row_accessor<irr::u32> rendering_buffer_u32;
	rendering_buffer_u32 rbuf((irr::u32*)image->lock(), image_size.Width, image_size.Height, image_size.Width*stride_value);
	//row_accessor<agg::int8u> rbuf((agg::int8u*)image->lock(), image_size.Width, image_size.Height, image_size.Width*stride_value);

	agg_pixel_type pixf(rbuf);
	agg::renderer_base<agg_pixel_type> renb(pixf);
	agg::renderer_scanline_aa_solid<agg::renderer_base<agg_pixel_type>> ren(renb);
	renb.clear(agg::rgba8(255, 255, 255, alpha_value));

	// Rasterizer & scanline
	agg::rasterizer_scanline_aa<> ras;
	agg::scanline_p8 sl;
	agg::trans_affine mtx;
	mtx *= agg::trans_affine_scaling(scale_value);
	mtx *= agg::trans_affine_rotation(agg::deg2rad(rotate_value));

	// Rendering
	agg::render_scanlines(ras, sl, ren);

	m_path->expand(expand_value);
	m_path->render(ras, sl, ren, mtx, renb.clip_box(), 1.0);

	image->unlock();
	return image;
}

IRRLICHT_C_API ITexture* agg_svg_ITexture(agg::svg::path_renderer* m_path, IVideoDriver* driver, fschar_t* texture_name = "", double scale_value = 1.0, double rotate_value = 0.0, double expand_value = 0.0, video::ECOLOR_FORMAT color_format = ECF_A8R8G8B8, u32 alpha_value = 0, int stride_value = 1)
{
	double m_min_x = 0.0;
	double m_min_y = 0.0;
	double m_max_x = 0.0;
	double m_max_y = 0.0;
	//m_path->arrange_orientations();
	m_path->bounding_rect(&m_min_x, &m_min_y, &m_max_x, &m_max_y);
	m_max_x *= scale_value;
	m_max_y *= scale_value;
	const dimension2d<u32>& image_size = dimension2d<u32>((irr::u32)m_max_x, (irr::u32)m_max_y);
	IImage* image = driver->createImage(color_format, image_size);
	rendering_buffer_u32 rbuf((irr::u32*)image->lock(), image_size.Width, image_size.Height, image_size.Width*stride_value);
	//row_accessor<agg::int8u> rbuf((irr::u32*)image->lock(), image_size.Width, image_size.Height, image_size.Width*stride_value);
	agg_pixel_type pixf(rbuf);
	agg::renderer_base<agg_pixel_type> renb(pixf);
	agg::renderer_scanline_aa_solid<agg::renderer_base<agg_pixel_type>> ren(renb);
	renb.clear(agg::rgba8(255, 255, 255, alpha_value));
	agg::rasterizer_scanline_aa<> ras;
	agg::scanline_p8 sl;
	agg::trans_affine mtx;
	mtx *= agg::trans_affine_scaling(scale_value);
	mtx *= agg::trans_affine_rotation(agg::deg2rad(rotate_value));
	agg::render_scanlines(ras, sl, ren);
	m_path->expand(expand_value);
	m_path->render(ras, sl, ren, mtx, renb.clip_box(), 1.0);
	image->unlock();
	ITexture* texture = driver->addTexture(texture_name, image);
	image->drop();
	if (image)
		delete image;
	return texture;
}

class agg_svg_loader : public irr::video::IImageLoader
//class agg_svg_loader : virtual public IReferenceCounted
{
public:
	agg_svg_loader(IVideoDriver* driver)
	{
		video_driver = driver;
	}
	~agg_svg_loader()
	{
		video_driver = 0;
	}
	virtual bool isALoadableFileExtension(const io::path& filename) const
	{
		//if(filename == "svg")
			//return true;
		//else
			//return false;
		return core::hasFileExtension ( filename, "svg" );
	}
	virtual bool isALoadableFileFormat(irr::io::IReadFile* file) const
	{
		//return true;
		return (false);
	}
	virtual irr::video::IImage* loadImage(irr::io::IReadFile* file) const
	{
		agg::svg::path_renderer m_path;
		agg::svg::parser p(m_path);
		p.parse(file->getFileName().c_str());
		double m_min_x = 0.0;
		double m_min_y = 0.0;
		double m_max_x = 0.0;
		double m_max_y = 0.0;
		m_path.bounding_rect(&m_min_x, &m_min_y, &m_max_x, &m_max_y);
		const dimension2d<u32>& image_size = dimension2d<u32>((irr::u32)m_max_x, (irr::u32)m_max_y);
		IImage* image = video_driver->createImage(ECF_A8R8G8B8, image_size);
		typedef row_accessor<irr::u32> rendering_buffer_u32;
		rendering_buffer_u32 rbuf((irr::u32*)image->lock(), image_size.Width, image_size.Height, image_size.Width);
		agg_pixel_type pixf(rbuf);
		agg::renderer_base<agg_pixel_type> renb(pixf);
		agg::renderer_scanline_aa_solid<agg::renderer_base<agg_pixel_type>> ren(renb);
		renb.clear(agg::rgba8(255, 255, 255, 0));
		agg::rasterizer_scanline_aa<> ras;
		agg::scanline_p8 sl;
		agg::trans_affine mtx;
		agg::render_scanlines(ras, sl, ren);
		m_path.render(ras, sl, ren, mtx, renb.clip_box(), 1.0);
		image->unlock();
		return image;
	}
	protected:
		IVideoDriver* video_driver;
};

//IRRLICHT_C_API IImageLoader* agg_svg_loader_ctor(IVideoDriver* driver)
IRRLICHT_C_API agg_svg_loader* agg_svg_loader_ctor(IVideoDriver* driver)
{
	//return (IImageLoader*)new agg_svg_loader(driver);
	return new agg_svg_loader(driver);
}

#ifdef __cplusplus
}
#endif

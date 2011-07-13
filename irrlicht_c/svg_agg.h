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
#include "agg_pixfmt_rgba.h"

#include "agg_svg_parser.h"

using namespace agg;
using namespace svg;

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API ITexture* tool_texture_from_svg(IVideoDriver* driver, char* file_name = "tiger.svg", video::ECOLOR_FORMAT image_format = ECF_R8G8B8, char* texture_name = "texture_01", u32 alpha_value = 128)
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
	IImage* image = driver->createImage(image_format, image_size);
	int alpha = 0;
	bool blend = false;
	video::ECOLOR_FORMAT color_format = image->getColorFormat();
	if (color_format == ECF_A1R5G5B5 || color_format == ECF_A8R8G8B8 || color_format == ECF_A16B16G16R16F || color_format == ECF_A32B32G32R32F)
	{
		alpha = alpha_value;
		blend = true;
	}

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

#ifdef __cplusplus
}
#endif

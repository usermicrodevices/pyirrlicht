// author Nalin
// http://irrlicht.sourceforge.net/phpBB2/profile.php?mode=viewprofile&u=8214

#ifndef __C_GUI_TTFONT_H_INCLUDED__
#define __C_GUI_TTFONT_H_INCLUDED__

#include <irrlicht.h>
#include "irrUString.h"
#include <ft2build.h>
#include FT_FREETYPE_H

//#if !defined(_IRR_COMPILE_WITH_CGUITTFONT_)

//=================from CGUITTFont.cpp=================
struct SGUITTFace : public virtual irr::IReferenceCounted
{
	~SGUITTFace()
	{
		FT_Done_Face(face);
		delete[] face_buffer;
	}

	FT_Face face;
	FT_Byte* face_buffer;
	FT_Long face_buffer_size;
};
FT_Library c_library;
bool c_libraryLoaded = false;
//==================================================


namespace irr
{
namespace gui
{
	// Assists us in deleting Glyphs.
	class CGUITTAssistDelete
	{
		public:
			template <class T, typename TAlloc>
			static void Delete(core::array<T, TAlloc>& a)
			{
				TAlloc allocator;
				allocator.deallocate(a.pointer());
			}
	};

	//! Holds a sheet of glyphs.
	class CGUITTGlyphPage
	{
		public:
			CGUITTGlyphPage(video::IVideoDriver* Driver, const io::path& texture_name) : image(0), texture(0), available_slots(0), used_slots(0), dirty(false), driver(Driver), name(texture_name) {}
			~CGUITTGlyphPage()
			{
				if (image)
					image->drop();
				if (texture)
				{
					if (driver)
						driver->removeTexture(texture);
					else texture->drop();
				}
			}

			//! Updates the texture if dirty.
			void updateTexture()
			{
				static u32 test = 0;
				dirty = false;

				// Save our texture creation flags and disable mipmaps.
				bool flg16 = driver->getTextureCreationFlag(video::ETCF_ALWAYS_16_BIT);
				bool flg32 = driver->getTextureCreationFlag(video::ETCF_ALWAYS_32_BIT);
				bool flgmip = driver->getTextureCreationFlag(video::ETCF_CREATE_MIP_MAPS);
				driver->setTextureCreationFlag(video::ETCF_CREATE_MIP_MAPS, false);

				// Set the texture color format.
				switch (image->getColorFormat())
				{
					case video::ECF_A1R5G5B5:
						// We want to create a 16-bit texture.
						driver->setTextureCreationFlag(video::ETCF_ALWAYS_16_BIT, true);
						driver->setTextureCreationFlag(video::ETCF_ALWAYS_32_BIT, false);
						break;

					case video::ECF_A8R8G8B8:
					default:
						// We want to create a 32-bit texture.
						driver->setTextureCreationFlag(video::ETCF_ALWAYS_16_BIT, false);
						driver->setTextureCreationFlag(video::ETCF_ALWAYS_32_BIT, true);
						break;
				}

				// Add the texture.
				if (texture)
				{
					driver->setMaterial(video::SMaterial());
					driver->removeTexture(texture);
				}
				texture = driver->addTexture(name, image);

				// Restore our texture creation flags.
				driver->setTextureCreationFlag(video::ETCF_CREATE_MIP_MAPS, flgmip);
				driver->setTextureCreationFlag(video::ETCF_ALWAYS_32_BIT, flg32);
				driver->setTextureCreationFlag(video::ETCF_ALWAYS_16_BIT, flg16);
			}

			video::IImage* image;
			video::ITexture* texture;
			u32 available_slots;
			u32 used_slots;
			bool dirty;

			core::array<core::vector2di> render_positions;
			core::array<core::recti> render_source_rects;

		private:
			video::IVideoDriver* driver;
			io::path name;
	};

	//! Structure representing a single TrueType glyph.
	struct SGUITTGlyph
	{
		//! Loads the glyph.
		void load(u32 character, FT_Face face, video::IVideoDriver* driver, u32 size, core::dimension2du max_texture_size, core::array<CGUITTGlyphPage*>* Glyph_Pages, bool fontHinting, bool autoHinting, bool useMonochrome);

		//! Unloads the glyph.
		void unload();

		//! If true, the glyph has been loaded.
		bool isLoaded;

		//! The page the glyph is on.
		u32 glyph_page;

		//! The source rectangle for the glyph.
		core::recti source_rect;

		//! The offset of glyph when drawn.
		core::vector2di offset;

		// Glyph advance information.
		FT_Vector advance;
	};

	//! Class representing a font.
	class CGUITTFont : public IGUIFont
	{
		public:
			//! Creates a new TrueType font and returns a pointer to it.  The pointer must be drop()'ed when finished.
			//! \param env The IGUIEnvironment the font loads out of.
			//! \param filename The filename of the font.
			//! \param size The size of the font glyphs in pixels.  Since this is the size of the individual glyphs, the true height of the font may change depending on the characters used.
			//! \return Returns a pointer to a CGUITTFont.  Will return 0 if the font failed to load.
//===============change to not static for dll build=======================
			static CGUITTFont* createTTFont(IGUIEnvironment *env, const io::path& filename, const u32 size);
//=============================================================

			//! Destructor
			virtual ~CGUITTFont();

			//! Sets the amount of glyphs to batch load.
			//! When a new glyph is loaded, the class also loads extra glyphs which surround the target glyph.
			//! For example, if batch_size is set to 50 and you try to load glyph 100, the class will load glyphs 75-125.
			//! \param batch_size The amount of glyphs to batch load.  Defaults to 100.
			void setBatchLoadSize(u32 batch_size)
			{
				batch_load_size = batch_size;
			}

			//! Sets the maximum texture size for a page of glyphs.
			//! By default, it creates a texture large enough for at least 400 glyphs.
			//! \param texture_size The maximum size of the texture.
			void setMaxPageTextureSize(const core::dimension2du& texture_size)
			{
				max_page_texture_size = texture_size;
			}

			//! Tells the font to allow transparency when rendering.
			//! Default: true.
			//! \param flag If true, the font draws using transparency.
			void setTransparency(const bool flag)
			{
				use_transparency = flag;
			}

			//! Tells the font to use monochrome rendering.
			//! Default: false.
			//! \param flag If true, the font draws using a monochrome image.  If false, the font uses a grayscale image.
			void setMonochrome(const bool flag);

			//! Enables or disables font hinting.
			//! Default: Hinting and auto-hinting true.
			//! \param enable If false, font hinting is turned off.  If true, font hinting is turned on.
			//! \param enable_auto_hinting If true, FreeType uses its own auto-hinting algorithm.  If false, it tries to use the algorithm specified by the font.
			void setFontHinting(const bool enable, const bool enable_auto_hinting = true);

			//! Draws some text and clips it to the specified rectangle if wanted.
			virtual void draw(const core::stringw& text, const core::rect<s32>& position,
				video::SColor color, bool hcenter=false, bool vcenter=false,
				const core::rect<s32>* clip=0);

			//! Returns the dimension of a text string.
			virtual core::dimension2d<u32> getDimension(const wchar_t* text) const;
			virtual core::dimension2d<u32> getDimension(const core::ustring& text) const;

			//! Calculates the index of the character in the text which is on a specific position.
			virtual s32 getCharacterFromPos(const wchar_t* text, s32 pixel_x) const;
			virtual s32 getCharacterFromPos(const core::ustring& text, s32 pixel_x) const;

			//! Sets global kerning width for the font.
			virtual void setKerningWidth(s32 kerning);

			//! Sets global kerning height for the font.
			virtual void setKerningHeight(s32 kerning);

			//! Gets kerning values (distance between letters) for the font. If no parameters are provided,
			virtual s32 getKerningWidth(const wchar_t* thisLetter=0, const wchar_t* previousLetter=0) const;
			virtual s32 getKerningWidth(const uchar32_t thisLetter=0, const uchar32_t previousLetter=0) const;

			//! Returns the distance between letters
			virtual s32 getKerningHeight() const;

			//! Define which characters should not be drawn by the font.
			virtual void setInvisibleCharacters(const wchar_t *s);
			virtual void setInvisibleCharacters(const core::ustring& s);

			void forceGlyphUpdate()
			{
				for (u32 i = 0; i != Glyph_Pages.size(); ++i)
					Glyph_Pages[i]->updateTexture();
			}

		private:
			CGUITTFont(IGUIEnvironment *env);
			bool load(const io::path& filename, const u32 size);
			void reset_images();
			void update_glyph_pages() const;

			u32 getWidthFromCharacter(wchar_t c) const;
			u32 getWidthFromCharacter(uchar32_t c) const;
			u32 getHeightFromCharacter(wchar_t c) const;
			u32 getHeightFromCharacter(uchar32_t c) const;
			u32 getGlyphByChar(wchar_t c) const;
			u32 getGlyphByChar(uchar32_t c) const;
			core::vector2di getKerning(const wchar_t thisLetter, const wchar_t previousLetter) const;
			core::vector2di getKerning(const uchar32_t thisLetter, const uchar32_t previousLetter) const;

			gui::IGUIEnvironment* Environment;
			video::IVideoDriver* Driver;
			io::path filename;
			FT_Face tt_face;
			FT_Size_Metrics font_metrics;

			bool use_monochrome;
			bool use_transparency;
			bool use_hinting;
			bool use_auto_hinting;
			u32 size;
			u32 batch_load_size;
			core::dimension2du max_page_texture_size;
			mutable core::array<CGUITTGlyphPage*> Glyph_Pages;
			mutable core::array<SGUITTGlyph> Glyphs;

			s32 GlobalKerningWidth;
			s32 GlobalKerningHeight;
			core::ustring Invisible;

//==================from CGUITTFont.cpp==================
			core::map<io::path, SGUITTFace*> c_faces;
//====================================================
	};

//==================from CGUITTFont.cpp==================
void SGUITTGlyph::load(u32 character, FT_Face face, video::IVideoDriver* driver, u32 size, core::dimension2du max_texture_size, core::array<CGUITTGlyphPage*>* Glyph_Pages, bool fontHinting, bool autoHinting, bool useMonochrome)
{
	if (isLoaded) return;

	// Set the size of the glyph.
	FT_Set_Pixel_Sizes(face, 0, size);

	// Set up our loading flags.
	FT_Int32 loadFlags = FT_LOAD_DEFAULT | FT_LOAD_RENDER;
	if (!fontHinting) loadFlags |= FT_LOAD_NO_HINTING;
	if (!autoHinting) loadFlags |= FT_LOAD_NO_AUTOHINT;
	if (useMonochrome) loadFlags |= FT_LOAD_MONOCHROME | FT_LOAD_TARGET_MONO | FT_RENDER_MODE_MONO;
	else loadFlags |= FT_LOAD_TARGET_NORMAL;

	// Attempt to load the glyph.
	if (FT_Load_Glyph(face, character, loadFlags) != FT_Err_Ok)
		// TODO: error message?
		return;

	FT_GlyphSlot glyph = face->glyph;
	advance = glyph->advance;

	// Load the image.
	FT_Bitmap bits = glyph->bitmap;

	// Bitmap offset information.
	offset = core::vector2di(glyph->bitmap_left, glyph->bitmap_top);

	// Determine what our texture size should be.
	// Add 1 because textures are inclusive-exclusive.
	core::dimension2du d(bits.width + 1, bits.rows + 1);
	core::dimension2du texture_size;
	//core::dimension2du texture_size(bits.width + 1, bits.rows + 1);

	// Create and load our image now.
	video::IImage* image = 0;
	switch (bits.pixel_mode)
	{
		case FT_PIXEL_MODE_MONO:
		{
			// Create a blank image and fill it with transparent pixels.
			texture_size = d.getOptimalSize(true, true);
			image = driver->createImage(video::ECF_A1R5G5B5, texture_size);
			image->fill(video::SColor(0, 255, 255, 255));

			// Load the monochrome data in.
			const u32 image_pitch = image->getPitch() / sizeof(u16);
			u16* image_data = (u16*)image->lock();
			u8* glyph_data = glyph->bitmap.buffer;
			for (s32 y = 0; y < bits.rows; ++y)
			{
				u16* row = image_data;
				for (s32 x = 0; x < bits.width; ++x)
				{
					// Monochrome bitmaps store 8 pixels per byte.  The left-most pixel is the bit 0x80.
					// So, we go through the data each bit at a time.
					if ((glyph_data[y * bits.pitch + (x / 8)] & (0x80 >> (x % 8))) != 0)
						*row = 0xFFFF;
					++row;
				}
				image_data += image_pitch;
			}
			image->unlock();
			break;
		}

		case FT_PIXEL_MODE_GRAY:
		{
			// Create our blank image.
			texture_size = d.getOptimalSize(!driver->queryFeature(video::EVDF_TEXTURE_NPOT), !driver->queryFeature(video::EVDF_TEXTURE_NSQUARE), true, 0);
			image = driver->createImage(video::ECF_A8R8G8B8, texture_size);
			image->fill(video::SColor(0, 255, 255, 255));

			// Load the grayscale data in.
			const float gray_count = static_cast<float>(bits.num_grays);
			const u32 image_pitch = image->getPitch() / sizeof(u32);
			u32* image_data = (u32*)image->lock();
			u8* glyph_data = glyph->bitmap.buffer;
			for (s32 y = 0; y < bits.rows; ++y)
			{
				u8* row = glyph_data;
				for (s32 x = 0; x < bits.width; ++x)
					image_data[y * image_pitch + x] |= static_cast<u32>(255.0f * (static_cast<float>(*row++) / gray_count)) << 24;
					//data[y * image_pitch + x] |= ((u32)(*bitsdata++) << 24);
				glyph_data += bits.pitch;
			}
			image->unlock();
			break;
		}

		default:
			// TODO: error message?
			return;
	}

	// Check to see if we have a free page.
	CGUITTGlyphPage* page = 0;
	bool make_new_page = false;
	if (Glyph_Pages->empty()) make_new_page = true;
	else
	{
		page = (*Glyph_Pages)[Glyph_Pages->size() - 1];
		if (page->available_slots == 0)
		{
			make_new_page = true;
			page = 0;
		}
	}

	// If we need to make a new page, do that now.
	if (make_new_page)
	{
		// Name of our page.
		io::path name("TTFontGlyphPage_");
		name += face->family_name;
		name += ".";
		name += face->style_name;
		name += ".";
		name += size;
		name += "_";
		name += Glyph_Pages->size();

		// Create the new page.
		page = new CGUITTGlyphPage(driver, name);

		// Determine our maximum texture size.
		// If we keep getting 0, set it to 2048x2048, as that number is pretty safe.
		if (max_texture_size.Width == 0 || max_texture_size.Height == 0)
			max_texture_size = driver->getMaxTextureSize();
		if (max_texture_size.Width == 0 || max_texture_size.Height == 0)
			max_texture_size = core::dimension2du(2048, 2048);

		// We want to try to put at least 400 glyphs on one texture.
		core::dimension2du page_texture_size;
		if (size <= 20) page_texture_size = core::dimension2du(512, 512);
		else if (size <= 51) page_texture_size = core::dimension2du(1024, 1024);
		else if (size <= 102) page_texture_size = core::dimension2du(2048, 2048);
		else if (size <= 204) page_texture_size = core::dimension2du(4096, 4096);
		else page_texture_size = core::dimension2du(8192, 8192);
		if (page_texture_size.Width > max_texture_size.Width || page_texture_size.Height > max_texture_size.Height)
			page_texture_size = max_texture_size;

		// Create the image for our page.
		switch (bits.pixel_mode)
		{
			case FT_PIXEL_MODE_MONO:
				page->image = driver->createImage(video::ECF_A1R5G5B5, page_texture_size);
				page->image->fill(video::SColor(0, 255, 255, 255));
				//page->image->fill(video::SColor(255, 0, 255, 0));
				break;

			case FT_PIXEL_MODE_GRAY:
			default:
				page->image = driver->createImage(video::ECF_A8R8G8B8, page_texture_size);
				page->image->fill(video::SColor(0, 255, 255, 255));
				//page->image->fill(video::SColor(255, 0, 255, 0));
				break;
		}

		// Determine the number of glyph slots on the page and add it to the list of pages.
		page->available_slots = (page_texture_size.Width / size) * (page_texture_size.Height / size);
		Glyph_Pages->push_back(page);
	}

	// Add the glyph to the page.
	core::vector2di page_position((page->used_slots % (page->image->getDimension().Width / size)) * size, (page->used_slots / (page->image->getDimension().Width / size)) * size);
	source_rect.UpperLeftCorner = page_position;
	source_rect.LowerRightCorner = core::vector2di(page_position.X + bits.width, page_position.Y + bits.rows);
	image->copyTo(page->image, page_position);
	image->drop();
	page->dirty = true;
	++page->used_slots;
	--page->available_slots;

	// Set our glyph as loaded.
	glyph_page = Glyph_Pages->size() - 1;
	isLoaded = true;
}

void SGUITTGlyph::unload()
{
	isLoaded = false;
}

//////////////////////

CGUITTFont* CGUITTFont::createTTFont(IGUIEnvironment *env, const io::path& filename, const u32 size)
{
	if (!c_libraryLoaded)
	{
		if (FT_Init_FreeType(&c_library))
			return 0;
		c_libraryLoaded = true;
	}

	CGUITTFont* font = new CGUITTFont(env);
	bool ret = font->load(filename, size);
	if (!ret)
	{
		font->drop();
		return 0;
	}

	return font;
}

//! constructor
CGUITTFont::CGUITTFont(IGUIEnvironment *env)
: Environment(env), Driver(0),
use_monochrome(false), use_transparency(true), use_hinting(true), use_auto_hinting(true),
batch_load_size(100),
GlobalKerningWidth(0), GlobalKerningHeight(0)
{
	#ifdef _DEBUG
	setDebugName("CGUITTFont");
	#endif

	if (Environment)
	{
		// don't grab environment, to avoid circular references
		Driver = Environment->getVideoDriver();
	}

	if (Driver)
		Driver->grab();

	setInvisibleCharacters(L" ");

	// Glyphs isn't reference counted, so don't try to delete when we free the array.
	Glyphs.set_free_when_destroyed(false);
}

bool CGUITTFont::load(const io::path& filename, const u32 size)
{
	// Some sanity checks.
	if (Environment == 0 || Driver == 0) return false;
	if (size == 0) return false;
	if (filename.size() == 0) return false;

	this->size = size;
	io::IFileSystem* filesystem = Environment->getFileSystem();
	//io::path f(filename);
	//filesystem->flattenFilename(f);
	this->filename = filename;

	// Grab the face.
	SGUITTFace* face = 0;
	core::map<io::path, SGUITTFace*>::Node* node = c_faces.find(filename);
	if (node == 0)
	{
		face = new SGUITTFace();
		c_faces.set(filename, face);

		if (filesystem)
		{
			// Read in the file data.
			io::IReadFile* file = filesystem->createAndOpenFile(filename);
			face->face_buffer = new FT_Byte[file->getSize()];
			file->read(face->face_buffer, file->getSize());
			face->face_buffer_size = file->getSize();
			file->drop();

			// Create the face.
			if (FT_New_Memory_Face(c_library, face->face_buffer, face->face_buffer_size,  0, &face->face))
			{
				delete face;
				c_faces.remove(filename);
				return false;
			}
		}
		else
		{
			core::ustring converter(filename);
			if (FT_New_Face(c_library, reinterpret_cast<const char*>(converter.toUTF8_s().c_str()), 0, &face->face))
			{
				delete face;
				c_faces.remove(filename);
				return false;
			}
		}
	}
	else
	{
		// Using another instance of this face.
		face = node->getValue();
		face->grab();
	}

	// Store our face.
	tt_face = face->face;

	// Store font metrics.
	FT_Set_Pixel_Sizes(tt_face, size, 0);
	font_metrics = tt_face->size->metrics;

	// Allocate our glyphs.
	Glyphs.reallocate(tt_face->num_glyphs);
	Glyphs.set_used(tt_face->num_glyphs);
	for (FT_Long i = 0; i < tt_face->num_glyphs; ++i)
	{
		Glyphs[i].isLoaded = false;
	}

	// Cache the first 127 ascii characters.
	u32 old_size = batch_load_size;
	batch_load_size = 127;
	getGlyphByChar((uchar32_t)0);
	batch_load_size = old_size;

	return true;
}

CGUITTFont::~CGUITTFont()
{
	// Delete the glyphs and glyph pages.
	reset_images();
	CGUITTAssistDelete::Delete(Glyphs);
	//Glyphs.clear();

	// We aren't using this face anymore.
	core::map<io::path, SGUITTFace*>::Node* n = c_faces.find(filename);
	if (n)
	{
		SGUITTFace* f = n->getValue();

		// Drop our face.  If this was the last face, the destructor will clean up.
		if (f->drop())
			c_faces.remove(filename);

		// If there are no more faces referenced by FreeType, clean up.
		if (c_faces.size() == 0)
		{
			FT_Done_FreeType(c_library);
			c_libraryLoaded = false;
		}
	}

	// Drop our driver now.
	if (Driver)
		Driver->drop();
}

void CGUITTFont::reset_images()
{
	// Delete the glyphs.
	for (u32 i = 0; i != Glyphs.size(); ++i)
		Glyphs[i].unload();

	// Unload the glyph pages from video memory.
	for (u32 i = 0; i != Glyph_Pages.size(); ++i)
		delete Glyph_Pages[i];
	Glyph_Pages.clear();
}

void CGUITTFont::update_glyph_pages() const
{
	for (u32 i = 0; i != Glyph_Pages.size(); ++i)
	{
		if (Glyph_Pages[i]->dirty)
			Glyph_Pages[i]->updateTexture();
	}
}

void CGUITTFont::setMonochrome(const bool flag)
{
	use_monochrome = flag;

	reset_images();
}

void CGUITTFont::setFontHinting(const bool enable, const bool enable_auto_hinting)
{
	use_hinting = enable;
	use_auto_hinting = enable_auto_hinting;

	reset_images();
}

void CGUITTFont::draw(const core::stringw& text, const core::rect<s32>& position, video::SColor color, bool hcenter, bool vcenter, const core::rect<s32>* clip)
{
	if (!Driver)
		return;

	// Clear the glyph pages of their render information.
	for (u32 i = 0; i < Glyph_Pages.size(); ++i)
	{
		Glyph_Pages[i]->render_positions.clear();
		Glyph_Pages[i]->render_source_rects.clear();
	}

	// Set up some variables.
	core::dimension2d<s32> textDimension;
	core::position2d<s32> offset = position.UpperLeftCorner;
	video::SColor colors[4];
	for (u32 i = 0; i < 4; i++)
		colors[i] = color;

	// Determine offset positions.
	if (hcenter || vcenter)
	{
		textDimension = getDimension(text.c_str());

		if (hcenter)
			offset.X = ((position.getWidth() - textDimension.Width) >> 1) + offset.X;

		if (vcenter)
			offset.Y = ((position.getHeight() - textDimension.Height) >> 1) + offset.Y;
	}

	// Convert to a unicode string.
	core::ustring utext(text);
	u32 utext_size = utext.size();

	// Set up our render map.
	core::map<u32, CGUITTGlyphPage*> Render_Map;

	// Start parsing characters.
	u32 n;
	uchar32_t previousChar = 0;
	core::ustring::const_iterator iter(utext);
	while (!iter.atEnd())
	{
		uchar32_t currentChar = *iter;
		n = getGlyphByChar(currentChar);
		bool visible = (Invisible.findFirst(currentChar) == -1);
		if (n > 0 && visible)
		{
			bool lineBreak=false;
			if (currentChar == L'\r') // Mac or Windows breaks
			{
				lineBreak = true;
				if (*(iter + 1) == (uchar32_t)'\n')	// Windows line breaks.
					currentChar = *(++iter);
			}
			else if (currentChar == (uchar32_t)'\n') // Unix breaks
			{
				lineBreak = true;
			}

			if (lineBreak)
			{
				previousChar = 0;
				offset.Y += font_metrics.ascender / 64;
				offset.X = position.UpperLeftCorner.X;

				if (hcenter)
					offset.X += (position.getWidth() - textDimension.Width) >> 1;
				++iter;
				continue;
			}

			// Calculate the glyph offset.
			s32 offx = Glyphs[n-1].offset.X;
			s32 offy = (font_metrics.ascender / 64) - Glyphs[n-1].offset.Y;

			// Apply kerning.
			core::vector2di k = getKerning(currentChar, previousChar);
			offset.X += k.X;
			offset.Y += k.Y;

			// Determine rendering information.
			SGUITTGlyph& glyph = Glyphs[n-1];
			CGUITTGlyphPage* const page = Glyph_Pages[glyph.glyph_page];
			page->render_positions.push_back(core::position2di(offset.X + offx, offset.Y + offy));
			page->render_source_rects.push_back(glyph.source_rect);
			Render_Map.set(glyph.glyph_page, page);
		}
		offset.X += getWidthFromCharacter(currentChar);

		previousChar = currentChar;
		++iter;
	}

	// Draw now.
	update_glyph_pages();
	core::map<u32, CGUITTGlyphPage*>::Iterator j = Render_Map.getIterator();
	while (!j.atEnd())
	{
		core::map<u32, CGUITTGlyphPage*>::Node* n = j.getNode();
		j++;
		if (n == 0) continue;

		CGUITTGlyphPage* page = n->getValue();

		if (!use_transparency) color.color |= 0xff000000;
		Driver->draw2DImageBatch(page->texture, page->render_positions, page->render_source_rects, clip, color, true);
	}
}

core::dimension2d<u32> CGUITTFont::getDimension(const wchar_t* text) const
{
	return getDimension(core::ustring(text));
}

core::dimension2d<u32> CGUITTFont::getDimension(const core::ustring& text) const
{
	// Get the maximum font height.  Unfortunately, we have to do this hack as
	// Irrlicht will draw things wrong.  In FreeType, the font size is the
	// maximum size for a single glyph, but that glyph may hang "under" the
	// draw line, increasing the total font height to beyond the set size.
	// Irrlicht does not understand this concept when drawing fonts.  Also, I
	// add +1 to give it a 1 pixel blank border.  This makes things like
	// tooltips look nicer.
	s32 test1 = getHeightFromCharacter((uchar32_t)'g') + 1;
	s32 test2 = getHeightFromCharacter((uchar32_t)'j') + 1;
	s32 test3 = getHeightFromCharacter((uchar32_t)'_') + 1;
	s32 max_font_height = core::max_(test1, core::max_(test2, test3));

	core::dimension2d<u32> text_dimension(0, max_font_height);
	core::dimension2d<u32> line(0, max_font_height);

	uchar32_t previousChar = 0;
	core::ustring::const_iterator iter = text.begin();
	for (; !iter.atEnd(); ++iter)
	{
		uchar32_t p = *iter;
		bool lineBreak = false;
		if (p == '\r')	// Mac or Windows line breaks.
		{
			lineBreak = true;
			if (*(iter + 1) == '\n')
			{
				++iter;
				p = *iter;
			}
		}
		else if (p == '\n')	// Unix line breaks.
		{
			lineBreak = true;
		}

		// Kerning.
		core::vector2di k = getKerning(p, previousChar);
		line.Width += k.X;
		previousChar = p;

		// Check for linebreak.
		if (lineBreak)
		{
			previousChar = 0;
			text_dimension.Height += line.Height;
			if (text_dimension.Width < line.Width)
				text_dimension.Width = line.Width;
			line.Width = 0;
			line.Height = max_font_height;
			continue;
		}
		line.Width += getWidthFromCharacter(p);
	}
	if (text_dimension.Width < line.Width)
		text_dimension.Width = line.Width;

	return text_dimension;
}

inline u32 CGUITTFont::getWidthFromCharacter(wchar_t c) const
{
	return getWidthFromCharacter((uchar32_t)c);
}

inline u32 CGUITTFont::getWidthFromCharacter(uchar32_t c) const
{
	// Set the size of the face.
	// This is because we cache faces and the face may have been set to a different size.
	//FT_Set_Pixel_Sizes(tt_face, 0, size);

	u32 n = getGlyphByChar(c);
	if (n > 0)
	{
		int w = Glyphs[n-1].advance.x / 64;
		return w;
	}
	if (c >= 0x2000)
		return (font_metrics.ascender / 64);
	else return (font_metrics.ascender / 64) / 2;
}

inline u32 CGUITTFont::getHeightFromCharacter(wchar_t c) const
{
	return getHeightFromCharacter((uchar32_t)c);
}

inline u32 CGUITTFont::getHeightFromCharacter(uchar32_t c) const
{
	// Set the size of the face.
	// This is because we cache faces and the face may have been set to a different size.
	//FT_Set_Pixel_Sizes(tt_face, 0, size);

	u32 n = getGlyphByChar(c);
	if (n > 0)
	{
		// Grab the true height of the character, taking into account underhanging glyphs.
		s32 height = (font_metrics.ascender / 64) - Glyphs[n-1].offset.Y + Glyphs[n-1].source_rect.getHeight();
		return height;
	}
	if (c >= 0x2000)
		return (font_metrics.ascender / 64);
	else return (font_metrics.ascender / 64) / 2;
}

u32 CGUITTFont::getGlyphByChar(wchar_t c) const
{
	return getGlyphByChar((uchar32_t)c);
}

u32 CGUITTFont::getGlyphByChar(uchar32_t c) const
{
	// Get the glyph.
	u32 glyph = FT_Get_Char_Index(tt_face, c);

	// Check for a valid glyph.  If it is invalid, attempt to use the replacement character.
	if (glyph == 0)
		glyph = FT_Get_Char_Index(tt_face, core::unicode::UTF_REPLACEMENT_CHARACTER);

	// If our glyph is already loaded, don't bother doing any batch loading code.
	if (glyph != 0 && Glyphs[glyph - 1].isLoaded)
		return glyph;

	// Determine our batch loading positions.
	u32 half_size = (batch_load_size / 2);
	u32 start_pos = 0;
	if (c > half_size) start_pos = c - half_size;
	u32 end_pos = start_pos + batch_load_size;

	// Load all our characters.
	do
	{
		// Get the character we are going to load.
		u32 load_glyph = FT_Get_Char_Index(tt_face, start_pos);

		// If the glyph hasn't been loaded yet, do it now.
		if (load_glyph != 0 && !Glyphs[load_glyph - 1].isLoaded)
			Glyphs[load_glyph - 1].load(load_glyph, tt_face, Driver, size, max_page_texture_size, &Glyph_Pages, use_hinting, use_auto_hinting, use_monochrome);
	}
	while (++start_pos < end_pos);

	// Update any glyph pages that were modified.
	//update_glyph_pages();
	
	// Return our original character.
	return glyph;
}

s32 CGUITTFont::getCharacterFromPos(const wchar_t* text, s32 pixel_x) const
{
	return getCharacterFromPos(core::ustring(text), pixel_x);
}

s32 CGUITTFont::getCharacterFromPos(const core::ustring& text, s32 pixel_x) const
{
	s32 x = 0;
	s32 idx = 0;

	u32 character = 0;
	uchar32_t previousChar = 0;
	core::ustring::const_iterator iter = text.begin();
	while (!iter.atEnd())
	{
		uchar32_t c = *iter;
		x += getWidthFromCharacter(c);

		// Kerning.
		core::vector2di k = getKerning(c, previousChar);
		x += k.X;

		if (x >= pixel_x)
			return character;

		previousChar = c;
		++iter;
		++character;
	}

	return -1;
}

void CGUITTFont::setKerningWidth(s32 kerning)
{
	GlobalKerningWidth = kerning;
}

void CGUITTFont::setKerningHeight(s32 kerning)
{
	GlobalKerningHeight = kerning;
}

s32 CGUITTFont::getKerningWidth(const wchar_t* thisLetter, const wchar_t* previousLetter) const
{
	if (tt_face == 0)
		return GlobalKerningWidth;
	if (thisLetter == 0 || previousLetter == 0)
		return 0;

	return getKerningWidth((uchar32_t)*thisLetter, (uchar32_t)*previousLetter);
}

s32 CGUITTFont::getKerningWidth(const uchar32_t thisLetter, const uchar32_t previousLetter) const
{
	// Return only the kerning width.
	return getKerning(thisLetter, previousLetter).X;
}

s32 CGUITTFont::getKerningHeight() const
{
	// FreeType 2 currently doesn't return any height kerning information.
	return GlobalKerningHeight;
}

core::vector2di CGUITTFont::getKerning(const wchar_t thisLetter, const wchar_t previousLetter) const
{
	return getKerning((uchar32_t)thisLetter, (uchar32_t)previousLetter);
}

core::vector2di CGUITTFont::getKerning(const uchar32_t thisLetter, const uchar32_t previousLetter) const
{
	if (tt_face == 0 || thisLetter == 0 || previousLetter == 0)
		return core::vector2di();

	// Set the size of the face.
	// This is because we cache faces and the face may have been set to a different size.
	FT_Set_Pixel_Sizes(tt_face, 0, size);

	core::vector2di ret(GlobalKerningWidth, GlobalKerningHeight);

	// If we don't have kerning, no point in continuing.
	if (!FT_HAS_KERNING(tt_face))
		return ret;

	// Get the kerning information.
	FT_Vector v;
	FT_Get_Kerning(tt_face, getGlyphByChar(previousLetter), getGlyphByChar(thisLetter), FT_KERNING_DEFAULT, &v);

	// If we have a scalable font, the return value will be in font points.
	if (FT_IS_SCALABLE(tt_face))
	{
		// Font points, so divide by 64.
		ret.X += (v.x / 64);
		ret.Y += (v.y / 64);
	}
	else
	{
		// Pixel units.
		ret.X += v.x;
		ret.Y += v.y;
	}
	return ret;
}

void CGUITTFont::setInvisibleCharacters(const wchar_t *s)
{
	core::ustring us(s);
	Invisible = us;
}

void CGUITTFont::setInvisibleCharacters(const core::ustring& s)
{
	Invisible = s;
}
//====================================================

} // end namespace gui
} // end namespace irr

//#endif // end of _IRR_COMPILE_WITH_CGUITTFONT_
#endif

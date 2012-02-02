// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#include "IGUITTFont.h"

#ifdef __cplusplus
extern "C" {
#endif

//================= CGUITTFont
IRRLICHT_C_API CGUITTFont* CGUITTFont_ctor(IGUIEnvironment *env, const fschar_t* filename, u32 size){return CGUITTFont::createTTFont(env, io::path(filename), size);}
IRRLICHT_C_API CGUITTFont* CGUITTFont_as_IGUIFont(IGUIFont *font){return (CGUITTFont*)font;}
IRRLICHT_C_API CGUITTFont* CGUITTFont_createTTFont(IGUIEnvironment *env, const fschar_t* filename, const u32 size){return CGUITTFont::createTTFont(env, io::path(filename), size);}
IRRLICHT_C_API void CGUITTFont_setBatchLoadSize(CGUITTFont* pointer, u32 batch_size){pointer->setBatchLoadSize(batch_size);}
IRRLICHT_C_API void CGUITTFont_setMaxPageTextureSize(CGUITTFont* pointer, const core::dimension2du* texture_size){pointer->setMaxPageTextureSize(*texture_size);}
IRRLICHT_C_API void CGUITTFont_setTransparency(CGUITTFont* pointer, const bool flag){pointer->setTransparency(flag);}
IRRLICHT_C_API void CGUITTFont_setMonochrome(CGUITTFont* pointer, const bool flag){pointer->setMonochrome(flag);}
IRRLICHT_C_API void CGUITTFont_setFontHinting(CGUITTFont* pointer, const bool enable, const bool enable_auto_hinting = true){pointer->setFontHinting(enable, enable_auto_hinting);}

IRRLICHT_C_API void CGUITTFont_draw(CGUITTFont* pointer, const wchar_t* text, const core::rect<s32>* position, const video::SColor* color, bool hcenter=false, bool vcenter=false, const core::rect<s32>* clip=0){pointer->draw(core::stringw(text), *position, *color, hcenter, vcenter, clip);}

IRRLICHT_C_API const core::dimension2d<u32>* CGUITTFont_getDimension1(CGUITTFont* pointer, const wchar_t* text){return new core::dimension2d<u32>(pointer->getDimension(text));}
//IRRLICHT_C_API const core::dimension2d<u32>* CGUITTFont_getDimension2(CGUITTFont* pointer, const core::ustring* text){return new core::dimension2d<u32>(pointer->getDimension(*text));}
IRRLICHT_C_API const core::dimension2d<u32>* CGUITTFont_getDimension2(CGUITTFont* pointer, const uchar16_t* text){return new core::dimension2d<u32>(pointer->getDimension(core::ustring(text)));}

IRRLICHT_C_API s32 CGUITTFont_getCharacterFromPos1(CGUITTFont* pointer, const wchar_t* text, s32 pixel_x){return pointer->getCharacterFromPos(text, pixel_x);}
//IRRLICHT_C_API s32 CGUITTFont_getCharacterFromPos2(CGUITTFont* pointer, const core::ustring* text, s32 pixel_x){return pointer->getCharacterFromPos(*text, pixel_x);}
IRRLICHT_C_API s32 CGUITTFont_getCharacterFromPos2(CGUITTFont* pointer, const uchar16_t* text, s32 pixel_x){return pointer->getCharacterFromPos(core::ustring(text), pixel_x);}

IRRLICHT_C_API void CGUITTFont_setKerningWidth(CGUITTFont* pointer, s32 kerning){pointer->setKerningWidth(kerning);}
IRRLICHT_C_API void CGUITTFont_setKerningHeight(CGUITTFont* pointer, s32 kerning){pointer->setKerningHeight(kerning);}
IRRLICHT_C_API s32 CGUITTFont_getKerningWidth1(CGUITTFont* pointer, const wchar_t* thisLetter=0, const wchar_t* previousLetter=0){return pointer->getKerningWidth(thisLetter, previousLetter);}
IRRLICHT_C_API s32 CGUITTFont_getKerningWidth2(CGUITTFont* pointer, const uchar32_t thisLetter=0, const uchar32_t previousLetter=0){return pointer->getKerningWidth(thisLetter, previousLetter);}
IRRLICHT_C_API s32 CGUITTFont_getKerningHeight(CGUITTFont* pointer){return pointer->getKerningHeight();}

IRRLICHT_C_API void CGUITTFont_setInvisibleCharacters1(CGUITTFont* pointer, const wchar_t* s){pointer->setInvisibleCharacters(s);}
//IRRLICHT_C_API void CGUITTFont_setInvisibleCharacters2(CGUITTFont* pointer, const core::ustring& s){pointer->setInvisibleCharacters(s);}
IRRLICHT_C_API void CGUITTFont_setInvisibleCharacters2(CGUITTFont* pointer, const uchar16_t* s){pointer->setInvisibleCharacters(core::ustring(s));}

IRRLICHT_C_API void CGUITTFont_forceGlyphUpdate(CGUITTFont* pointer){pointer->forceGlyphUpdate();}

#ifdef __cplusplus
}
#endif

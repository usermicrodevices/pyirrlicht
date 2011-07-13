// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIFont
//IRRLICHT_C_API void IGUIFont_draw(IGUIFont* pointer, const core::stringw* text, const core::rect<s32>* position, video::SColor* color, bool hcenter=false, bool vcenter=false, const core::rect<s32>* clip=0)
IRRLICHT_C_API void IGUIFont_draw(IGUIFont* pointer, wchar_t* text, const core::rect<s32>* position, video::SColor* color, bool hcenter=false, bool vcenter=false, const core::rect<s32>* clip=0)
{pointer->draw(text, *position, *color, hcenter, vcenter, clip);}
IRRLICHT_C_API core::dimension2d<u32>* IGUIFont_getDimension(IGUIFont* pointer, const wchar_t* text)
{return &pointer->getDimension(text);}
IRRLICHT_C_API s32 IGUIFont_getCharacterFromPos(IGUIFont* pointer, const wchar_t* text, s32 pixel_x)
{return pointer->getCharacterFromPos(text, pixel_x);}
IRRLICHT_C_API EGUI_FONT_TYPE IGUIFont_getType(IGUIFont* pointer)
{return pointer->getType();}
IRRLICHT_C_API void IGUIFont_setKerningWidth(IGUIFont* pointer, s32 kerning)
{pointer->setKerningWidth(kerning);}
IRRLICHT_C_API void IGUIFont_setKerningHeight(IGUIFont* pointer, s32 kerning)
{pointer->setKerningHeight(kerning);}
IRRLICHT_C_API s32 IGUIFont_getKerningWidth(IGUIFont* pointer, const wchar_t* thisLetter=0, const wchar_t* previousLetter=0)
{return pointer->getKerningWidth(thisLetter, previousLetter);}
IRRLICHT_C_API s32 IGUIFont_getKerningHeight(IGUIFont* pointer)
{return pointer->getKerningHeight();}
IRRLICHT_C_API void IGUIFont_setInvisibleCharacters(IGUIFont* pointer, const wchar_t *s)
{pointer->setInvisibleCharacters(s);}

#ifdef __cplusplus
}
#endif

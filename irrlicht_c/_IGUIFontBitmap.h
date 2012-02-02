// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIFontBitmap
IRRLICHT_C_API EGUI_FONT_TYPE IGUIFontBitmap_getType(IGUIFontBitmap* pointer)
{return pointer->getType();}
IRRLICHT_C_API IGUISpriteBank* IGUIFontBitmap_getSpriteBank(IGUIFontBitmap* pointer)
{return pointer->getSpriteBank();}
IRRLICHT_C_API u32 IGUIFontBitmap_getSpriteNoFromChar(IGUIFontBitmap* pointer, const wchar_t *c)
{return pointer->getSpriteNoFromChar(c);}
IRRLICHT_C_API s32 IGUIFontBitmap_getKerningWidth(IGUIFontBitmap* pointer, const wchar_t* thisLetter=0, const wchar_t* previousLetter=0)
{return pointer->getKerningWidth(thisLetter, previousLetter);}

#ifdef __cplusplus
}
#endif

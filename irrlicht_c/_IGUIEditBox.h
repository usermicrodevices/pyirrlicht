// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IGUIEditBox* IGUIEditBox_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIEditBox*)new IGUIElement(EGUIET_EDIT_BOX, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIEditBox_setOverrideFont(IGUIEditBox* pointer, IGUIFont* font=0)
{pointer->setOverrideFont(font);}
IRRLICHT_C_API void IGUIEditBox_setOverrideColor(IGUIEditBox* pointer, video::SColor* color)
{pointer->setOverrideColor(*color);}
IRRLICHT_C_API void IGUIEditBox_enableOverrideColor(IGUIEditBox* pointer, bool enable)
{pointer->enableOverrideColor(enable);}
IRRLICHT_C_API void IGUIEditBox_setDrawBorder(IGUIEditBox* pointer, bool border)
{pointer->setDrawBorder(border);}
IRRLICHT_C_API void IGUIEditBox_setTextAlignment(IGUIEditBox* pointer, EGUI_ALIGNMENT horizontal, EGUI_ALIGNMENT vertical)
{pointer->setTextAlignment(horizontal, vertical);}
IRRLICHT_C_API void IGUIEditBox_setWordWrap(IGUIEditBox* pointer, bool enable)
{pointer->setWordWrap(enable);}
IRRLICHT_C_API bool IGUIEditBox_isWordWrapEnabled(IGUIEditBox* pointer)
{return pointer->isWordWrapEnabled();}
IRRLICHT_C_API void IGUIEditBox_setMultiLine(IGUIEditBox* pointer, bool enable)
{pointer->setMultiLine(enable);}
IRRLICHT_C_API bool IGUIEditBox_isMultiLineEnabled(IGUIEditBox* pointer)
{return pointer->isMultiLineEnabled();}
IRRLICHT_C_API void IGUIEditBox_setAutoScroll(IGUIEditBox* pointer, bool enable)
{pointer->setAutoScroll(enable);}
IRRLICHT_C_API bool IGUIEditBox_isAutoScrollEnabled(IGUIEditBox* pointer)
{return pointer->isAutoScrollEnabled();}
IRRLICHT_C_API void IGUIEditBox_setPasswordBox(IGUIEditBox* pointer, bool passwordBox, wchar_t passwordChar = L'*')
{pointer->setPasswordBox(passwordBox, passwordChar);}
IRRLICHT_C_API bool IGUIEditBox_isPasswordBox(IGUIEditBox* pointer)
{return pointer->isPasswordBox();}
IRRLICHT_C_API core::dimension2du* IGUIEditBox_getTextDimension(IGUIEditBox* pointer)
{return &pointer->getTextDimension();}
IRRLICHT_C_API void IGUIEditBox_setMax(IGUIEditBox* pointer, u32 max)
{pointer->setMax(max);}
IRRLICHT_C_API u32 IGUIEditBox_getMax(IGUIEditBox* pointer)
{return pointer->getMax();}

#ifdef __cplusplus
}
#endif

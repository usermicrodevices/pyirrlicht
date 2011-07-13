// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIColorSelectDialog
IRRLICHT_C_API IGUIColorSelectDialog* IGUIColorSelectDialog_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIColorSelectDialog*)new IGUIElement(EGUIET_COLOR_SELECT_DIALOG, environment, parent, id, *rectangle);}

#ifdef __cplusplus
}
#endif

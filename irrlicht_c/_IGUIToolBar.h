// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIToolBar
IRRLICHT_C_API IGUIToolBar* IGUIToolBar_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIToolBar*)new IGUIElement(EGUIET_TOOL_BAR, environment, parent, id, *rectangle);}
IRRLICHT_C_API IGUIButton* IGUIToolBar_addButton(IGUIToolBar* pointer, s32 id=-1, const wchar_t* text=0,const wchar_t* tooltiptext=0, video::ITexture* img=0, video::ITexture* pressedimg=0, bool isPushButton=false, bool useAlphaChannel=false)
{return pointer->addButton(id, text, tooltiptext, img, pressedimg, isPushButton, useAlphaChannel);}

#ifdef __cplusplus
}
#endif

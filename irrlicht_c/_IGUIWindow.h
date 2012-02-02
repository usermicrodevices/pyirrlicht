// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class IGUIWindow : public IGUIElement

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IGUIWindow* IGUIWindow_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIWindow*)new IGUIElement(EGUIET_WINDOW, environment, parent, id, *rectangle);}
IRRLICHT_C_API IGUIButton* IGUIWindow_getCloseButton(IGUIWindow* pointer){return pointer->getCloseButton();}
IRRLICHT_C_API IGUIButton* IGUIWindow_getMinimizeButton(IGUIWindow* pointer){return pointer->getMinimizeButton();}
IRRLICHT_C_API IGUIButton* IGUIWindow_getMaximizeButton(IGUIWindow* pointer){return pointer->getMaximizeButton();}
IRRLICHT_C_API bool IGUIWindow_isDraggable(IGUIWindow* pointer){return pointer->isDraggable();}
IRRLICHT_C_API void IGUIWindow_setDraggable(IGUIWindow* pointer, bool draggable){pointer->setDraggable(draggable);}
IRRLICHT_C_API void IGUIWindow_setDrawBackground(IGUIWindow* pointer, bool draw){pointer->setDrawBackground(draw);}
IRRLICHT_C_API bool IGUIWindow_getDrawBackground(IGUIWindow* pointer){return pointer->getDrawBackground();}
IRRLICHT_C_API void IGUIWindow_setDrawTitlebar(IGUIWindow* pointer, bool draw){pointer->setDrawTitlebar(draw);}
IRRLICHT_C_API bool IGUIWindow_getDrawTitlebar(IGUIWindow* pointer){return pointer->getDrawTitlebar();}
IRRLICHT_C_API core::rect<s32>* IGUIWindow_getClientRect(IGUIWindow* pointer){return &pointer->getClientRect();}

#ifdef __cplusplus
}
#endif

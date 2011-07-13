// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUITab
IRRLICHT_C_API IGUITab* IGUITab_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUITab*)new IGUIElement(EGUIET_TAB, environment, parent, id, *rectangle);}
IRRLICHT_C_API s32 IGUITab_getNumber(IGUITab* pointer)
{return pointer->getNumber();}
IRRLICHT_C_API void IGUITab_setDrawBackground(IGUITab* pointer, bool draw=true)
{pointer->setDrawBackground(draw);}
IRRLICHT_C_API void IGUITab_setBackgroundColor(IGUITab* pointer, video::SColor* c)
{pointer->setBackgroundColor(*c);}
IRRLICHT_C_API bool IGUITab_isDrawingBackground(IGUITab* pointer)
{return pointer->isDrawingBackground();}
IRRLICHT_C_API SColor* IGUITab_getBackgroundColor(IGUITab* pointer)
{return &pointer->getBackgroundColor();}
IRRLICHT_C_API void IGUITab_setTextColor(IGUITab* pointer, video::SColor* c)
{pointer->setTextColor(*c);}
IRRLICHT_C_API SColor* IGUITab_getTextColor(IGUITab* pointer)
{return &pointer->getTextColor();}

//================= IGUITabControl
IRRLICHT_C_API IGUITabControl* IGUITabControl_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32> rectangle)
{return (IGUITabControl*)new IGUIElement(EGUIET_TAB_CONTROL, environment, parent, id, rectangle);}
IRRLICHT_C_API IGUITab* IGUITabControl_addTab(IGUITabControl* pointer, const wchar_t* caption, s32 id=-1)
{return pointer->addTab(caption, id);}
IRRLICHT_C_API s32 IGUITabControl_getTabCount(IGUITabControl* pointer)
{return pointer->getTabCount();}
IRRLICHT_C_API IGUITab* IGUITabControl_getTab(IGUITabControl* pointer, s32 idx)
{return pointer->getTab(idx);}
IRRLICHT_C_API bool IGUITabControl_setActiveTab1(IGUITabControl* pointer, s32 idx)
{return pointer->setActiveTab(idx);}
IRRLICHT_C_API bool IGUITabControl_setActiveTab2(IGUITabControl* pointer, IGUIElement *tab)
{return pointer->setActiveTab(tab);}
IRRLICHT_C_API s32 IGUITabControl_getActiveTab(IGUITabControl* pointer)
{return pointer->getActiveTab();}
IRRLICHT_C_API void IGUITabControl_setTabHeight(IGUITabControl* pointer, s32 height)
{pointer->setTabHeight(height);}
IRRLICHT_C_API s32 IGUITabControl_getTabHeight(IGUITabControl* pointer)
{return pointer->getTabHeight();}
IRRLICHT_C_API void IGUITabControl_setTabMaxWidth(IGUITabControl* pointer, s32 width)
{pointer->setTabMaxWidth(width);}
IRRLICHT_C_API s32 IGUITabControl_getTabMaxWidth(IGUITabControl* pointer)
{return pointer->getTabMaxWidth();}
IRRLICHT_C_API void IGUITabControl_setTabVerticalAlignment(IGUITabControl* pointer, gui::EGUI_ALIGNMENT alignment)
{pointer->setTabVerticalAlignment(alignment);}
IRRLICHT_C_API gui::EGUI_ALIGNMENT IGUITabControl_getTabVerticalAlignment(IGUITabControl* pointer)
{return pointer->getTabVerticalAlignment();}
IRRLICHT_C_API void IGUITabControl_setTabExtraWidth(IGUITabControl* pointer, s32 extraWidth)
{pointer->setTabExtraWidth(extraWidth);}
IRRLICHT_C_API s32 IGUITabControl_getTabExtraWidth(IGUITabControl* pointer)
{return pointer->getTabExtraWidth();}

#ifdef __cplusplus
}
#endif

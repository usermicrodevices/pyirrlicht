// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIContextMenu
IRRLICHT_C_API IGUIContextMenu* IGUIContextMenu_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIContextMenu*)new IGUIElement(EGUIET_CONTEXT_MENU, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIContextMenu_setCloseHandling(IGUIContextMenu* pointer, ECONTEXT_MENU_CLOSE onClose)
{pointer->setCloseHandling(onClose);}
IRRLICHT_C_API ECONTEXT_MENU_CLOSE IGUIContextMenu_getCloseHandling(IGUIContextMenu* pointer)
{return pointer->getCloseHandling();}
IRRLICHT_C_API u32 IGUIContextMenu_getItemCount(IGUIContextMenu* pointer)
{return pointer->getItemCount();}
IRRLICHT_C_API u32 IGUIContextMenu_addItem(IGUIContextMenu* pointer, const wchar_t* text, s32 commandId=-1, bool enabled=true, bool hasSubMenu=false, bool checked=false, bool autoChecking=false)
{return pointer->addItem(text, commandId, enabled, hasSubMenu, checked, autoChecking);}
IRRLICHT_C_API u32 IGUIContextMenu_insertItem(IGUIContextMenu* pointer, u32 idx, const wchar_t* text, s32 commandId=-1, bool enabled=true, bool hasSubMenu=false, bool checked=false, bool autoChecking=false)
{return pointer->insertItem(idx, text, commandId, enabled, hasSubMenu, checked, autoChecking);}
IRRLICHT_C_API s32 IGUIContextMenu_findItemWithCommandId(IGUIContextMenu* pointer, s32 commandId, u32 idxStartSearch=0)
{return pointer->findItemWithCommandId(commandId, idxStartSearch);}
IRRLICHT_C_API void IGUIContextMenu_addSeparator(IGUIContextMenu* pointer)
{pointer->addSeparator();}
IRRLICHT_C_API const wchar_t* IGUIContextMenu_getItemText(IGUIContextMenu* pointer, u32 idx)
{return pointer->getItemText(idx);}
IRRLICHT_C_API void IGUIContextMenu_setItemText(IGUIContextMenu* pointer, u32 idx, const wchar_t* text)
{pointer->setItemText(idx, text);}
IRRLICHT_C_API bool IGUIContextMenu_isItemEnabled(IGUIContextMenu* pointer, u32 idx)
{return pointer->isItemEnabled(idx);}
IRRLICHT_C_API void IGUIContextMenu_setItemEnabled(IGUIContextMenu* pointer, u32 idx, bool enabled)
{pointer->setItemEnabled(idx, enabled);}
IRRLICHT_C_API void IGUIContextMenu_setItemChecked(IGUIContextMenu* pointer, u32 idx, bool enabled)
{pointer->setItemChecked(idx, enabled);}
IRRLICHT_C_API bool IGUIContextMenu_isItemChecked(IGUIContextMenu* pointer, u32 idx)
{return pointer->isItemChecked(idx);}
IRRLICHT_C_API void IGUIContextMenu_removeItem(IGUIContextMenu* pointer, u32 idx)
{pointer->removeItem(idx);}
IRRLICHT_C_API void IGUIContextMenu_removeAllItems(IGUIContextMenu* pointer)
{pointer->removeAllItems();}
IRRLICHT_C_API s32 IGUIContextMenu_getSelectedItem(IGUIContextMenu* pointer)
{return pointer->getSelectedItem();}
IRRLICHT_C_API s32 IGUIContextMenu_getItemCommandId(IGUIContextMenu* pointer, u32 idx)
{return pointer->getItemCommandId(idx);}
IRRLICHT_C_API void IGUIContextMenu_setItemCommandId(IGUIContextMenu* pointer, u32 idx, s32 id)
{pointer->setItemCommandId(idx, id);}
IRRLICHT_C_API IGUIContextMenu* IGUIContextMenu_getSubMenu(IGUIContextMenu* pointer, u32 idx)
{return pointer->getSubMenu(idx);}
IRRLICHT_C_API void IGUIContextMenu_setItemAutoChecking(IGUIContextMenu* pointer, u32 idx, bool autoChecking)
{pointer->setItemAutoChecking(idx, autoChecking);}
IRRLICHT_C_API bool IGUIContextMenu_getItemAutoChecking(IGUIContextMenu* pointer, u32 idx)
{return pointer->getItemAutoChecking(idx);}
IRRLICHT_C_API void IGUIContextMenu_setEventParent(IGUIContextMenu* pointer, IGUIElement *parent)
{pointer->setEventParent(parent);}

#ifdef __cplusplus
}
#endif

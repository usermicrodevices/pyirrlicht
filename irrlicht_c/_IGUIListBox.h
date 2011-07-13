// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIListBox
IRRLICHT_C_API IGUIListBox* IGUIListBox_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIListBox*)new IGUIElement(EGUIET_LIST_BOX, environment, parent, id, *rectangle);}

IRRLICHT_C_API u32 IGUIListBox_getItemCount(IGUIListBox* pointer)
{return pointer->getItemCount();}

IRRLICHT_C_API const wchar_t* IGUIListBox_getListItem(IGUIListBox* pointer, u32 id)
{return pointer->getListItem(id);}

IRRLICHT_C_API u32 IGUIListBox_addItem1(IGUIListBox* pointer, const wchar_t* text)
{return pointer->addItem(text);}

IRRLICHT_C_API u32 IGUIListBox_addItem2(IGUIListBox* pointer, const wchar_t* text, s32 icon)
{return pointer->addItem(text, icon);}

IRRLICHT_C_API void IGUIListBox_removeItem(IGUIListBox* pointer, u32 index)
{pointer->removeItem(index);}

IRRLICHT_C_API s32 IGUIListBox_getIcon(IGUIListBox* pointer, u32 index)
{return pointer->getIcon(index);}

IRRLICHT_C_API void IGUIListBox_setSpriteBank(IGUIListBox* pointer, IGUISpriteBank* bank)
{pointer->setSpriteBank(bank);}

IRRLICHT_C_API void IGUIListBox_clear(IGUIListBox* pointer)
{pointer->clear();}

IRRLICHT_C_API s32 IGUIListBox_getSelected(IGUIListBox* pointer)
{return pointer->getSelected();}

IRRLICHT_C_API void IGUIListBox_setSelected1(IGUIListBox* pointer, s32 index)
{pointer->setSelected(index);}

IRRLICHT_C_API void IGUIListBox_setSelected2(IGUIListBox* pointer, const wchar_t* item)
{pointer->setSelected(item);}

IRRLICHT_C_API void IGUIListBox_setAutoScrollEnabled(IGUIListBox* pointer, bool scroll)
{pointer->setAutoScrollEnabled(scroll);}

IRRLICHT_C_API bool IGUIListBox_isAutoScrollEnabled(IGUIListBox* pointer)
{return pointer->isAutoScrollEnabled();}

IRRLICHT_C_API void IGUIListBox_setItemOverrideColor1(IGUIListBox* pointer, u32 index, const video::SColor& color = SColor(128,128,128,128))
{pointer->setItemOverrideColor(index, color);}

IRRLICHT_C_API void IGUIListBox_setItemOverrideColor2(IGUIListBox* pointer, u32 index, EGUI_LISTBOX_COLOR colorType, const video::SColor& color = SColor(128,128,128,128))
{pointer->setItemOverrideColor(index, colorType, color);}

IRRLICHT_C_API void IGUIListBox_clearItemOverrideColor1(IGUIListBox* pointer, u32 index)
{pointer->clearItemOverrideColor(index);}

IRRLICHT_C_API void IGUIListBox_clearItemOverrideColor2(IGUIListBox* pointer, u32 index, EGUI_LISTBOX_COLOR colorType)
{pointer->clearItemOverrideColor(index, colorType);}

IRRLICHT_C_API bool IGUIListBox_hasItemOverrideColor(IGUIListBox* pointer, u32 index, EGUI_LISTBOX_COLOR colorType)
{return pointer->hasItemOverrideColor(index, colorType);}

IRRLICHT_C_API video::SColor* IGUIListBox_getItemOverrideColor(IGUIListBox* pointer, u32 index, EGUI_LISTBOX_COLOR colorType)
{return &pointer->getItemOverrideColor(index, colorType);}

IRRLICHT_C_API video::SColor* IGUIListBox_getItemDefaultColor(IGUIListBox* pointer, EGUI_LISTBOX_COLOR colorType)
{return &pointer->getItemDefaultColor(colorType);}

IRRLICHT_C_API void IGUIListBox_setItem(IGUIListBox* pointer, u32 index, const wchar_t* text, s32 icon)
{pointer->setItem(index, text, icon);}

IRRLICHT_C_API s32 IGUIListBox_insertItem(IGUIListBox* pointer, u32 index, const wchar_t* text, s32 icon)
{return pointer->insertItem(index, text, icon);}

IRRLICHT_C_API void IGUIListBox_swapItems(IGUIListBox* pointer, u32 index1, u32 index2)
{pointer->swapItems(index1, index2);}

IRRLICHT_C_API void IGUIListBox_setItemHeight(IGUIListBox* pointer, s32 height)
{pointer->setItemHeight(height);}

IRRLICHT_C_API void IGUIListBox_setDrawBackground(IGUIListBox* pointer, bool draw)
{pointer->setDrawBackground(draw);}

#ifdef __cplusplus
}
#endif

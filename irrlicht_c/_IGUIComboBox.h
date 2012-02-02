// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIComboBox
IRRLICHT_C_API IGUIComboBox* IGUIComboBox_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIComboBox*)new IGUIElement(EGUIET_COMBO_BOX, environment, parent, id, *rectangle);}

IRRLICHT_C_API u32 IGUIComboBox_getItemCount(IGUIComboBox* pointer)
{return pointer->getItemCount();}
IRRLICHT_C_API const wchar_t* IGUIComboBox_getItem(IGUIComboBox* pointer, u32 idx)
{return pointer->getItem(idx);}
IRRLICHT_C_API u32 IGUIComboBox_getItemData(IGUIComboBox* pointer, u32 idx)
{return pointer->getItemData(idx);}
IRRLICHT_C_API s32 IGUIComboBox_getIndexForItemData(IGUIComboBox* pointer, u32 data)
{return pointer->getIndexForItemData(data);}
IRRLICHT_C_API u32 IGUIComboBox_addItem(IGUIComboBox* pointer, const wchar_t* text, u32 data = 0)
{return pointer->addItem(text, data);}
IRRLICHT_C_API void IGUIComboBox_removeItem(IGUIComboBox* pointer, u32 idx)
{pointer->removeItem(idx);}
IRRLICHT_C_API void IGUIComboBox_clear(IGUIComboBox* pointer)
{pointer->clear();}
IRRLICHT_C_API s32 IGUIComboBox_getSelected(IGUIComboBox* pointer)
{return pointer->getSelected();}
IRRLICHT_C_API void IGUIComboBox_setSelected(IGUIComboBox* pointer, s32 idx)
{pointer->setSelected(idx);}
IRRLICHT_C_API void IGUIComboBox_setTextAlignment(IGUIComboBox* pointer, EGUI_ALIGNMENT horizontal, EGUI_ALIGNMENT vertical)
{pointer->setTextAlignment(horizontal, vertical);}

#ifdef __cplusplus
}
#endif

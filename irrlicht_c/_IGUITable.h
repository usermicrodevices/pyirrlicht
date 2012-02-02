// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUITable
IRRLICHT_C_API IGUITable* IGUITable_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUITable*)new IGUIElement(EGUIET_TABLE, environment, parent, id, *rectangle);}

IRRLICHT_C_API void IGUITable_addColumn(IGUITable* pointer, const wchar_t* caption, s32 columnIndex=-1)
{pointer->addColumn(caption, columnIndex);}

IRRLICHT_C_API void IGUITable_removeColumn(IGUITable* pointer, u32 columnIndex)
{pointer->removeColumn(columnIndex);}

IRRLICHT_C_API s32 IGUITable_getColumnCount(IGUITable* pointer)
{return pointer->getColumnCount();}

IRRLICHT_C_API bool IGUITable_setActiveColumn(IGUITable* pointer, s32 idx, bool doOrder=false)
{return pointer->setActiveColumn(idx, doOrder);}

IRRLICHT_C_API s32 IGUITable_getActiveColumn(IGUITable* pointer)
{return pointer->getActiveColumn();}

IRRLICHT_C_API EGUI_ORDERING_MODE IGUITable_getActiveColumnOrdering(IGUITable* pointer)
{return pointer->getActiveColumnOrdering();}

IRRLICHT_C_API void IGUITable_setColumnWidth(IGUITable* pointer, u32 columnIndex, u32 width)
{pointer->setColumnWidth(columnIndex, width);}

IRRLICHT_C_API void IGUITable_setResizableColumns(IGUITable* pointer, bool resizable)
{pointer->setResizableColumns(resizable);}

IRRLICHT_C_API bool IGUITable_hasResizableColumns(IGUITable* pointer)
{return pointer->hasResizableColumns();}

IRRLICHT_C_API void IGUITable_setColumnOrdering(IGUITable* pointer, u32 columnIndex, EGUI_COLUMN_ORDERING mode)
{pointer->setColumnOrdering(columnIndex, mode);}

IRRLICHT_C_API s32 IGUITable_getSelected(IGUITable* pointer)
{return pointer->getSelected();}

IRRLICHT_C_API void IGUITable_setSelected(IGUITable* pointer, s32 index)
{pointer->setSelected(index);}

IRRLICHT_C_API s32 IGUITable_getRowCount(IGUITable* pointer)
{return pointer->getRowCount();}

IRRLICHT_C_API u32 IGUITable_addRow(IGUITable* pointer, u32 rowIndex)
{return pointer->addRow(rowIndex);}

IRRLICHT_C_API void IGUITable_removeRow(IGUITable* pointer, u32 rowIndex)
{pointer->removeRow(rowIndex);}

IRRLICHT_C_API void IGUITable_clearRows(IGUITable* pointer)
{pointer->clearRows();}

IRRLICHT_C_API void IGUITable_swapRows(IGUITable* pointer, u32 rowIndexA, u32 rowIndexB)
{pointer->swapRows(rowIndexA, rowIndexB);}

IRRLICHT_C_API void IGUITable_orderRows(IGUITable* pointer, s32 columnIndex=-1, EGUI_ORDERING_MODE mode=EGOM_NONE)
{pointer->orderRows(columnIndex, mode);}

IRRLICHT_C_API void IGUITable_setCellText1(IGUITable* pointer, u32 rowIndex, u32 columnIndex, const wchar_t* text)
{pointer->setCellText(rowIndex, columnIndex, core::stringw(text));}

IRRLICHT_C_API void IGUITable_setCellText2(IGUITable* pointer, u32 rowIndex, u32 columnIndex, const wchar_t* text, const video::SColor& color = SColor(128,128,128,128))
{pointer->setCellText(rowIndex, columnIndex, core::stringw(text), color);}

IRRLICHT_C_API void IGUITable_setCellData(IGUITable* pointer, u32 rowIndex, u32 columnIndex, void* data)
{pointer->setCellData(rowIndex, columnIndex, data);}

IRRLICHT_C_API void IGUITable_setCellColor(IGUITable* pointer, u32 rowIndex, u32 columnIndex, const video::SColor& color = SColor(128,128,128,128))
{pointer->setCellColor(rowIndex, columnIndex, color);}

IRRLICHT_C_API const wchar_t* IGUITable_getCellText(IGUITable* pointer, u32 rowIndex, u32 columnIndex)
{return pointer->getCellText(rowIndex, columnIndex);}

IRRLICHT_C_API void* IGUITable_getCellData(IGUITable* pointer, u32 rowIndex, u32 columnIndex)
{return pointer->getCellData(rowIndex, columnIndex);}

IRRLICHT_C_API void IGUITable_clear(IGUITable* pointer)
{pointer->clear();}

IRRLICHT_C_API void IGUITable_setDrawFlags(IGUITable* pointer, s32 flags)
{pointer->setDrawFlags(flags);}

IRRLICHT_C_API s32 IGUITable_getDrawFlags(IGUITable* pointer)
{return pointer->getDrawFlags();}

#ifdef __cplusplus
}
#endif

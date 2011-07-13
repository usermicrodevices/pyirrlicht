// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUITreeViewNode
IRRLICHT_C_API IGUITreeView* IGUITreeViewNode_getOwner(IGUITreeViewNode* pointer)
{return pointer->getOwner();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getParent(IGUITreeViewNode* pointer)
{return pointer->getParent();}

IRRLICHT_C_API const wchar_t* IGUITreeViewNode_getText(IGUITreeViewNode* pointer)
{return pointer->getText();}

IRRLICHT_C_API void IGUITreeViewNode_setText(IGUITreeViewNode* pointer, const wchar_t* text)
{pointer->setText(text);}

IRRLICHT_C_API const wchar_t* IGUITreeViewNode_getIcon(IGUITreeViewNode* pointer)
{return pointer->getIcon();}

IRRLICHT_C_API void IGUITreeViewNode_setIcon(IGUITreeViewNode* pointer, const wchar_t* icon)
{pointer->setIcon(icon);}

IRRLICHT_C_API u32 IGUITreeViewNode_getImageIndex(IGUITreeViewNode* pointer)
{return pointer->getImageIndex();}

IRRLICHT_C_API void IGUITreeViewNode_setImageIndex(IGUITreeViewNode* pointer, u32 imageIndex)
{pointer->setImageIndex(imageIndex);}

IRRLICHT_C_API u32 IGUITreeViewNode_getSelectedImageIndex(IGUITreeViewNode* pointer)
{return pointer->getSelectedImageIndex();}

IRRLICHT_C_API void IGUITreeViewNode_setSelectedImageIndex(IGUITreeViewNode* pointer, u32 imageIndex)
{pointer->setSelectedImageIndex(imageIndex);}

IRRLICHT_C_API void* IGUITreeViewNode_getData(IGUITreeViewNode* pointer)
{return pointer->getData();}

IRRLICHT_C_API void IGUITreeViewNode_setData(IGUITreeViewNode* pointer, void* data)
{pointer->setData(data);}

IRRLICHT_C_API IReferenceCounted* IGUITreeViewNode_getData2(IGUITreeViewNode* pointer)
{return pointer->getData2();}

IRRLICHT_C_API void IGUITreeViewNode_setData2(IGUITreeViewNode* pointer, IReferenceCounted* data)
{pointer->setData2(data);}

IRRLICHT_C_API u32 IGUITreeViewNode_getChildCount(IGUITreeViewNode* pointer)		
{return pointer->getChildCount();}

IRRLICHT_C_API void IGUITreeViewNode_clearChilds(IGUITreeViewNode* pointer)
{pointer->clearChilds();}

IRRLICHT_C_API bool IGUITreeViewNode_hasChilds(IGUITreeViewNode* pointer)
{return pointer->hasChilds();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_addChildBack(IGUITreeViewNode* pointer, const wchar_t* text, const wchar_t* icon = 0, s32 imageIndex=-1, s32 selectedImageIndex=-1, void* data=0, IReferenceCounted* data2=0)
{return pointer->addChildBack(text, icon, imageIndex, selectedImageIndex, data, data2);}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_addChildFront(IGUITreeViewNode* pointer, const wchar_t* text, const wchar_t* icon = 0, s32 imageIndex=-1, s32 selectedImageIndex=-1, void* data=0, IReferenceCounted* data2=0 )
{return pointer->addChildFront(text, icon, imageIndex, selectedImageIndex, data, data2);}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_insertChildAfter(IGUITreeViewNode* pointer, IGUITreeViewNode* other, const wchar_t* text, const wchar_t* icon = 0, s32 imageIndex=-1, s32 selectedImageIndex=-1, void* data=0, IReferenceCounted* data2=0)
{return pointer->insertChildAfter(other, text, icon, imageIndex, selectedImageIndex, data, data2);}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_insertChildBefore(IGUITreeViewNode* pointer, IGUITreeViewNode* other, const wchar_t* text, const wchar_t* icon = 0, s32 imageIndex=-1, s32 selectedImageIndex=-1, void* data=0, IReferenceCounted* data2=0)
{return pointer->insertChildBefore(other, text, icon, imageIndex, selectedImageIndex, data, data2);}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getFirstChild(IGUITreeViewNode* pointer)
{return pointer->getFirstChild();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getLastChild(IGUITreeViewNode* pointer)
{return pointer->getLastChild();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getPrevSibling(IGUITreeViewNode* pointer)
{return pointer->getPrevSibling();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getNextSibling(IGUITreeViewNode* pointer)
{return pointer->getNextSibling();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeViewNode_getNextVisible(IGUITreeViewNode* pointer)
{return pointer->getNextVisible();}

IRRLICHT_C_API bool IGUITreeViewNode_deleteChild(IGUITreeViewNode* pointer, IGUITreeViewNode* child)
{return pointer->deleteChild(child);}

IRRLICHT_C_API bool IGUITreeViewNode_moveChildUp(IGUITreeViewNode* pointer, IGUITreeViewNode* child)
{return pointer->moveChildUp(child);}

IRRLICHT_C_API bool IGUITreeViewNode_moveChildDown(IGUITreeViewNode* pointer, IGUITreeViewNode* child)
{return pointer->moveChildDown(child);}

IRRLICHT_C_API bool IGUITreeViewNode_getExpanded(IGUITreeViewNode* pointer)
{return pointer->getExpanded();}

IRRLICHT_C_API void IGUITreeViewNode_setExpanded(IGUITreeViewNode* pointer, bool expanded)
{pointer->setExpanded(expanded);}

IRRLICHT_C_API bool IGUITreeViewNode_getSelected(IGUITreeViewNode* pointer)
{return pointer->getSelected();}

IRRLICHT_C_API void IGUITreeViewNode_setSelected(IGUITreeViewNode* pointer, bool selected)
{pointer->setSelected(selected);}

IRRLICHT_C_API bool IGUITreeViewNode_isRoot(IGUITreeViewNode* pointer)
{return pointer->isRoot();}

IRRLICHT_C_API s32 IGUITreeViewNode_getLevel(IGUITreeViewNode* pointer)
{return pointer->getLevel();}

IRRLICHT_C_API bool IGUITreeViewNode_isVisible(IGUITreeViewNode* pointer)
{return pointer->isVisible();}

//================= IGUITreeView
IRRLICHT_C_API IGUITreeView* IGUITreeView_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUITreeView*)new IGUIElement(EGUIET_TREE_VIEW, environment, parent, id, *rectangle);}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeView_getRoot(IGUITreeView* pointer)
{return pointer->getRoot();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeView_getSelected(IGUITreeView* pointer)
{return pointer->getSelected();}

IRRLICHT_C_API bool IGUITreeView_getLinesVisible(IGUITreeView* pointer)
{return pointer->getLinesVisible();}

IRRLICHT_C_API void IGUITreeView_setLinesVisible(IGUITreeView* pointer, bool visible)
{pointer->setLinesVisible(visible);}

IRRLICHT_C_API void IGUITreeView_setIconFont(IGUITreeView* pointer, IGUIFont* font)
{pointer->setIconFont(font);}

IRRLICHT_C_API void IGUITreeView_setImageList(IGUITreeView* pointer, IGUIImageList* imageList)
{pointer->setImageList(imageList);}

IRRLICHT_C_API IGUIImageList* IGUITreeView_getImageList(IGUITreeView* pointer)
{return pointer->getImageList();}

IRRLICHT_C_API void IGUITreeView_setImageLeftOfIcon(IGUITreeView* pointer, bool bLeftOf)
{pointer->setImageLeftOfIcon(bLeftOf);}

IRRLICHT_C_API bool IGUITreeView_getImageLeftOfIcon(IGUITreeView* pointer)
{return pointer->getImageLeftOfIcon();}

IRRLICHT_C_API IGUITreeViewNode* IGUITreeView_getLastEventNode(IGUITreeView* pointer)
{return pointer->getLastEventNode();}

#ifdef __cplusplus
}
#endif

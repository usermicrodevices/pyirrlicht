// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= list<IGUIElement>::Iterator
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_ctor(){return new list<IGUIElement>::Iterator();}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_next(list<IGUIElement>::Iterator* pointer){return &pointer->operator++();}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_prev(list<IGUIElement>::Iterator* pointer){return &pointer->operator--();}
IRRLICHT_C_API bool listIGUIElementIterator_operator_eq(list<IGUIElement>::Iterator* pointer, const list<IGUIElement>::Iterator& other){return pointer->operator==(other);}
IRRLICHT_C_API bool listIGUIElementIterator_operator_ne(list<IGUIElement>::Iterator* pointer, const list<IGUIElement>::Iterator& other){return pointer->operator!=(other);}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_add_set(list<IGUIElement>::Iterator* pointer, s32 num){return &pointer->operator+=(num);}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_add(list<IGUIElement>::Iterator* pointer, s32 num){return &pointer->operator+(num);}
//IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_sub_set(list<IGUIElement>::Iterator* pointer, s32 num){return &pointer->operator-=(num);}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElementIterator_operator_sub(list<IGUIElement>::Iterator* pointer, s32 num){return &pointer->operator-(num);}

//================= listIGUIElement
IRRLICHT_C_API list<IGUIElement>* listIGUIElement_ctor1(){return new list<IGUIElement>();}
IRRLICHT_C_API list<IGUIElement>* listIGUIElement_ctor2(const list<IGUIElement>& other){return new list<IGUIElement>(other);}
//IRRLICHT_C_API void listIGUIElement_Destructor(list<IGUIElement>* pointer){delete pointer;}
IRRLICHT_C_API void listIGUIElement_operator_set(list<IGUIElement>* pointer, const list<IGUIElement>& other){pointer->operator=(other);}
IRRLICHT_C_API u32 listIGUIElement_size(list<IGUIElement>* pointer){return pointer->size();}
IRRLICHT_C_API u32 listIGUIElement_getSize(list<IGUIElement>* pointer){return pointer->getSize();}
IRRLICHT_C_API void listIGUIElement_clear(list<IGUIElement>* pointer){pointer->clear();}
IRRLICHT_C_API bool listIGUIElement_empty(list<IGUIElement>* pointer){return pointer->empty();}
IRRLICHT_C_API void listIGUIElement_push_back(list<IGUIElement>* pointer, const IGUIElement& element){pointer->push_back(element);}
IRRLICHT_C_API void listIGUIElement_push_front(list<IGUIElement>* pointer, const IGUIElement& element){pointer->push_front(element);}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElement_begin(list<IGUIElement>* pointer){return &pointer->begin();}
//IRRLICHT_C_API list<IGUIElement>::ConstIterator* listIGUIElement_begin_const(list<IGUIElement>* pointer){return &pointer->begin();}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElement_end(list<IGUIElement>* pointer){return &pointer->end();}
//IRRLICHT_C_API list<IGUIElement>::ConstIterator* listIGUIElement_end_const(list<IGUIElement>* pointer){return &pointer->end();}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElement_getLast(list<IGUIElement>* pointer){return &pointer->getLast();}
//IRRLICHT_C_API list<IGUIElement>::ConstIterator* listIGUIElement_getLast_const(list<IGUIElement>* pointer){return &pointer->getLast();}
IRRLICHT_C_API void listIGUIElement_insert_after(list<IGUIElement>* pointer, const list<IGUIElement>::Iterator& it, const IGUIElement& element){pointer->insert_after(it, element);}
IRRLICHT_C_API void listIGUIElement_insert_before(list<IGUIElement>* pointer, const list<IGUIElement>::Iterator& it, const IGUIElement& element){pointer->insert_before(it, element);}
IRRLICHT_C_API list<IGUIElement>::Iterator* listIGUIElement_erase(list<IGUIElement>* pointer, list<IGUIElement>::Iterator& it){return &pointer->erase(it);}
IRRLICHT_C_API void listIGUIElement_swap(list<IGUIElement>* pointer, list<IGUIElement>* other){pointer->swap(*other);}

//================= IGUIElement
IRRLICHT_C_API IGUIElement* IGUIElement_ctor(EGUI_ELEMENT_TYPE type, IGUIEnvironment* environment, IGUIElement* parent, s32 id, const core::rect<s32>& rectangle){return new IGUIElement(type, environment, parent, id, rectangle);}
//IRRLICHT_C_API void IGUIElement_Destructor(IGUIElement* pointer){delete pointer;}
IRRLICHT_C_API IGUIElement* IGUIElement_getParent(IGUIElement* pointer){return pointer->getParent();}
IRRLICHT_C_API core::rect<s32>* IGUIElement_getRelativePosition(IGUIElement* pointer){return &pointer->getRelativePosition();}
IRRLICHT_C_API void IGUIElement_setRelativePosition1(IGUIElement* pointer, const core::rect<s32>& r){pointer->setRelativePosition(r);}
IRRLICHT_C_API void IGUIElement_setRelativePosition2(IGUIElement* pointer, const core::position2di & position){pointer->setRelativePosition(position);}
IRRLICHT_C_API void IGUIElement_setRelativePositionProportional(IGUIElement* pointer, const core::rect<f32>& r){pointer->setRelativePositionProportional(r);}
IRRLICHT_C_API core::rect<s32>* IGUIElement_getAbsolutePosition(IGUIElement* pointer){return &pointer->getAbsolutePosition();}
IRRLICHT_C_API core::rect<s32>* IGUIElement_getAbsoluteClippingRect(IGUIElement* pointer){return &pointer->getAbsoluteClippingRect();}
IRRLICHT_C_API void IGUIElement_setNotClipped(IGUIElement* pointer, bool noClip){pointer->setNotClipped(noClip);}
IRRLICHT_C_API bool IGUIElement_isNotClipped(IGUIElement* pointer){return pointer->isNotClipped();}
IRRLICHT_C_API void IGUIElement_setMaxSize(IGUIElement* pointer, core::dimension2du* size){pointer->setMaxSize(*size);}
IRRLICHT_C_API void IGUIElement_setMinSize(IGUIElement* pointer, core::dimension2du* size){pointer->setMinSize(*size);}
IRRLICHT_C_API void IGUIElement_setAlignment(IGUIElement* pointer, EGUI_ALIGNMENT left, EGUI_ALIGNMENT right, EGUI_ALIGNMENT top, EGUI_ALIGNMENT bottom){pointer->setAlignment(left, right, top, bottom);}
IRRLICHT_C_API void IGUIElement_updateAbsolutePosition(IGUIElement* pointer){pointer->updateAbsolutePosition();}
IRRLICHT_C_API IGUIElement* IGUIElement_getElementFromPoint(IGUIElement* pointer, const core::position2d<s32>& point){return pointer->getElementFromPoint(point);}
IRRLICHT_C_API bool IGUIElement_isPointInside(IGUIElement* pointer, const core::position2d<s32>& point){return pointer->isPointInside(point);}
IRRLICHT_C_API void IGUIElement_addChild(IGUIElement* pointer, IGUIElement* child){pointer->addChild(child);}
IRRLICHT_C_API void IGUIElement_removeChild(IGUIElement* pointer, IGUIElement* child){pointer->removeChild(child);}
IRRLICHT_C_API void IGUIElement_remove(IGUIElement* pointer){pointer->remove();}
IRRLICHT_C_API void IGUIElement_draw(IGUIElement* pointer){pointer->draw();}
IRRLICHT_C_API void IGUIElement_OnPostRender(IGUIElement* pointer, u32 timeMs){pointer->OnPostRender(timeMs);}
IRRLICHT_C_API void IGUIElement_move(IGUIElement* pointer, core::position2d<s32>* absoluteMovement){pointer->move(*absoluteMovement);}
IRRLICHT_C_API bool IGUIElement_isVisible(IGUIElement* pointer){return pointer->isVisible();}
IRRLICHT_C_API void IGUIElement_setVisible(IGUIElement* pointer, bool visible){pointer->setVisible(visible);}
IRRLICHT_C_API bool IGUIElement_isSubElement(IGUIElement* pointer){return pointer->isSubElement();}
IRRLICHT_C_API void IGUIElement_setSubElement(IGUIElement* pointer, bool subElement){pointer->setSubElement(subElement);}
IRRLICHT_C_API void IGUIElement_setTabStop(IGUIElement* pointer, bool enable){pointer->setTabStop(enable);}
IRRLICHT_C_API bool IGUIElement_isTabStop(IGUIElement* pointer){return pointer->isTabStop();}
IRRLICHT_C_API void IGUIElement_setTabOrder(IGUIElement* pointer, s32 index){pointer->setTabOrder(index);}
IRRLICHT_C_API s32 IGUIElement_getTabOrder(IGUIElement* pointer){return pointer->getTabOrder();}
IRRLICHT_C_API void IGUIElement_setTabGroup(IGUIElement* pointer, bool isGroup){pointer->setTabGroup(isGroup);}
IRRLICHT_C_API bool IGUIElement_isTabGroup(IGUIElement* pointer){return pointer->isTabGroup();}
IRRLICHT_C_API IGUIElement* IGUIElement_getTabGroup(IGUIElement* pointer){return pointer->getTabGroup();}
IRRLICHT_C_API bool IGUIElement_isEnabled(IGUIElement* pointer){return pointer->isEnabled();}
IRRLICHT_C_API void IGUIElement_setEnabled(IGUIElement* pointer, bool enabled){pointer->setEnabled(enabled);}
IRRLICHT_C_API void IGUIElement_setText(IGUIElement* pointer, const wchar_t* text){pointer->setText(text);}
IRRLICHT_C_API const wchar_t* IGUIElement_getText(IGUIElement* pointer){return pointer->getText();}
IRRLICHT_C_API void IGUIElement_setToolTipText(IGUIElement* pointer, const wchar_t* text){pointer->setToolTipText(text);}

IRRLICHT_C_API const wchar_t* IGUIElement_getToolTipText(IGUIElement* pointer){return pointer->getToolTipText().c_str();}

IRRLICHT_C_API s32 IGUIElement_getID(IGUIElement* pointer){return pointer->getID();}
IRRLICHT_C_API void IGUIElement_setID(IGUIElement* pointer, s32 id){pointer->setID(id);}
//IRRLICHT_C_API bool IGUIElement_OnEvent(IGUIElement* pointer, const SEvent& event){return pointer->OnEvent(event);}
IRRLICHT_C_API bool IGUIElement_bringToFront(IGUIElement* pointer, IGUIElement* element){return pointer->bringToFront(element);}

IRRLICHT_C_API const core::list<IGUIElement*>* IGUIElement_getChildren(IGUIElement* pointer){return &pointer->getChildren();}

IRRLICHT_C_API IGUIElement* IGUIElement_getElementFromId(IGUIElement* pointer, s32 id, bool searchchildren=false){return pointer->getElementFromId(id, searchchildren);}
IRRLICHT_C_API bool IGUIElement_isMyChild(IGUIElement* pointer, IGUIElement* child){return pointer->isMyChild(child);}
IRRLICHT_C_API bool IGUIElement_getNextElement(IGUIElement* pointer, s32 startOrder, bool reverse, bool group, IGUIElement*& first, IGUIElement*& closest, bool includeInvisible=false){return pointer->getNextElement(startOrder, reverse, group, first, closest, includeInvisible);}
IRRLICHT_C_API EGUI_ELEMENT_TYPE IGUIElement_getType(IGUIElement* pointer){return pointer->getType();}
IRRLICHT_C_API bool IGUIElement_hasType(IGUIElement* pointer, EGUI_ELEMENT_TYPE type){return pointer->hasType(type);}
IRRLICHT_C_API const c8* IGUIElement_getTypeName(IGUIElement* pointer){return pointer->getTypeName();}
IRRLICHT_C_API void IGUIElement_serializeAttributes(IGUIElement* pointer, io::IAttributes* out, io::SAttributeReadWriteOptions* options=0){pointer->serializeAttributes(out, options);}
IRRLICHT_C_API void IGUIElement_deserializeAttributes(IGUIElement* pointer, io::IAttributes* in, io::SAttributeReadWriteOptions* options=0){pointer->deserializeAttributes(in, options);}

//extended methods for compatibility with swig project
IRRLICHT_C_API IGUIButton* IGUIElement_as_IGUIButton(IGUIElement* pointer){return (IGUIButton*)pointer;};
IRRLICHT_C_API IGUICheckBox* IGUIElement_as_IGUICheckBox(IGUIElement* pointer){return (IGUICheckBox*)pointer;};
IRRLICHT_C_API IGUIColorSelectDialog* IGUIElement_as_IGUIColorSelectDialog(IGUIElement* pointer){return (IGUIColorSelectDialog*)pointer;};
IRRLICHT_C_API IGUIComboBox* IGUIElement_as_IGUIComboBox(IGUIElement* pointer){return (IGUIComboBox*)pointer;};
IRRLICHT_C_API IGUIContextMenu* IGUIElement_as_IGUIContextMenu(IGUIElement* pointer){return (IGUIContextMenu*)pointer;};
IRRLICHT_C_API IGUIEditBox* IGUIElement_as_IGUIEditBox(IGUIElement* pointer){return (IGUIEditBox*)pointer;};
IRRLICHT_C_API IGUIFileOpenDialog* IGUIElement_as_IGUIFileOpenDialog(IGUIElement* pointer){return (IGUIFileOpenDialog*)pointer;};
IRRLICHT_C_API IGUIFontBitmap* IGUIElement_as_IGUIFontBitmap(IGUIElement* pointer){return (IGUIFontBitmap*)pointer;};
IRRLICHT_C_API IGUIImage* IGUIElement_as_IGUIImage(IGUIElement* pointer){return (IGUIImage*)pointer;};
IRRLICHT_C_API IGUIListBox* IGUIElement_as_IGUIListBox(IGUIElement* pointer){return (IGUIListBox*)pointer;};
IRRLICHT_C_API IGUIMeshViewer* IGUIElement_as_IGUIMeshViewer(IGUIElement* pointer){return (IGUIMeshViewer*)pointer;};
IRRLICHT_C_API IGUIScrollBar* IGUIElement_as_IGUIScrollBar(IGUIElement* pointer){return (IGUIScrollBar*)pointer;};
IRRLICHT_C_API IGUISpinBox* IGUIElement_as_IGUISpinBox(IGUIElement* pointer){return (IGUISpinBox*)pointer;};
IRRLICHT_C_API IGUIStaticText* IGUIElement_as_IGUIStaticText(IGUIElement* pointer){return (IGUIStaticText*)pointer;};
IRRLICHT_C_API IGUITab* IGUIElement_as_IGUITab(IGUIElement* pointer){return (IGUITab*)pointer;};
IRRLICHT_C_API IGUITabControl* IGUIElement_as_IGUITabControl(IGUIElement* pointer){return (IGUITabControl*)pointer;};
IRRLICHT_C_API IGUITable* IGUIElement_as_IGUITable(IGUIElement* pointer){return (IGUITable*)pointer;};
IRRLICHT_C_API IGUIToolBar* IGUIElement_as_IGUIToolBar(IGUIElement* pointer){return (IGUIToolBar*)pointer;};
IRRLICHT_C_API IGUITreeView* IGUIElement_as_IGUITreeView(IGUIElement* pointer){return (IGUITreeView*)pointer;};
IRRLICHT_C_API IGUIWindow* IGUIElement_as_IGUIWindow(IGUIElement* pointer){return (IGUIWindow*)pointer;};

#ifdef __cplusplus
}
#endif

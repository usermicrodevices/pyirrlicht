// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIEnvironment
IRRLICHT_C_API void IGUIEnvironment_drawAll(IGUIEnvironment* pointer)
{pointer->drawAll();}
IRRLICHT_C_API bool IGUIEnvironment_setFocus(IGUIEnvironment* pointer, IGUIElement* element)
{return pointer->setFocus(element);}
IRRLICHT_C_API IGUIElement* IGUIEnvironment_getFocus(IGUIEnvironment* pointer)
{return pointer->getFocus();}
IRRLICHT_C_API bool IGUIEnvironment_removeFocus(IGUIEnvironment* pointer, IGUIElement* element)
{return pointer->removeFocus(element);}
IRRLICHT_C_API bool IGUIEnvironment_hasFocus(IGUIEnvironment* pointer, IGUIElement* element)
{return pointer->hasFocus(element);}
IRRLICHT_C_API video::IVideoDriver* IGUIEnvironment_getVideoDriver(IGUIEnvironment* pointer)
{return pointer->getVideoDriver();}
IRRLICHT_C_API io::IFileSystem* IGUIEnvironment_getFileSystem(IGUIEnvironment* pointer)
{return pointer->getFileSystem();}
IRRLICHT_C_API IOSOperator* IGUIEnvironment_getOSOperator(IGUIEnvironment* pointer)
{return pointer->getOSOperator();}
IRRLICHT_C_API void IGUIEnvironment_clear(IGUIEnvironment* pointer)
{pointer->clear();}
IRRLICHT_C_API bool IGUIEnvironment_postEventFromUser(IGUIEnvironment* pointer, const SEvent& event)
{return pointer->postEventFromUser(event);}
IRRLICHT_C_API void IGUIEnvironment_setUserEventReceiver(IGUIEnvironment* pointer, IEventReceiver* evr)
{pointer->setUserEventReceiver(evr);}
IRRLICHT_C_API IGUISkin* IGUIEnvironment_getSkin(IGUIEnvironment* pointer)
{return pointer->getSkin();}
IRRLICHT_C_API void IGUIEnvironment_setSkin(IGUIEnvironment* pointer, IGUISkin* skin)
{pointer->setSkin(skin);}
IRRLICHT_C_API IGUISkin* IGUIEnvironment_createSkin(IGUIEnvironment* pointer, EGUI_SKIN_TYPE type)
{return pointer->createSkin(type);}
IRRLICHT_C_API IGUIImageList* IGUIEnvironment_createImageList(IGUIEnvironment* pointer, video::ITexture* texture, core::dimension2d<s32>* imageSize, bool useAlphaChannel)
{return pointer->createImageList(texture, *imageSize, useAlphaChannel);}
IRRLICHT_C_API IGUIFont* IGUIEnvironment_getFont(IGUIEnvironment* pointer, const char* filename)
{return pointer->getFont(filename);}
IRRLICHT_C_API IGUIFont* IGUIEnvironment_getBuiltInFont(IGUIEnvironment* pointer)
{return pointer->getBuiltInFont();}
IRRLICHT_C_API IGUISpriteBank* IGUIEnvironment_getSpriteBank(IGUIEnvironment* pointer, const char* filename)
{return pointer->getSpriteBank(filename);}
IRRLICHT_C_API IGUISpriteBank* IGUIEnvironment_addEmptySpriteBank(IGUIEnvironment* pointer, const char* name)
{return pointer->addEmptySpriteBank(name);}
IRRLICHT_C_API IGUIElement* IGUIEnvironment_getRootGUIElement(IGUIEnvironment* pointer)
{return pointer->getRootGUIElement();}
IRRLICHT_C_API IGUIButton* IGUIEnvironment_addButton(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, const wchar_t* text=0, const wchar_t* tooltiptext = 0)
{return pointer->addButton(rectangle, parent, id, text, tooltiptext);}
IRRLICHT_C_API IGUIWindow* IGUIEnvironment_addWindow(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, bool modal = false, const wchar_t* text=0, IGUIElement* parent=0, s32 id=-1)
{return pointer->addWindow(rectangle, modal, text, parent, id);}
IRRLICHT_C_API IGUIElement* IGUIEnvironment_addModalScreen(IGUIEnvironment* pointer, IGUIElement* parent)
{return pointer->addModalScreen(parent);}
IRRLICHT_C_API IGUIWindow* IGUIEnvironment_addMessageBox(IGUIEnvironment* pointer, const wchar_t* caption, const wchar_t* text=0, bool modal = true, s32 flags = EMBF_OK, IGUIElement* parent=0, s32 id=-1)
{return pointer->addMessageBox(caption, text, modal, flags, parent, id);}
IRRLICHT_C_API IGUIScrollBar* IGUIEnvironment_addScrollBar(IGUIEnvironment* pointer, bool horizontal, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1)
{return pointer->addScrollBar(horizontal, rectangle, parent, id);}
IRRLICHT_C_API IGUIImage* IGUIEnvironment_addImage(IGUIEnvironment* pointer, video::ITexture* image, core::position2d<s32> *pos, bool useAlphaChannel=true, IGUIElement* parent=0, s32 id=-1, const wchar_t* text=0)
{return pointer->addImage(image, *pos, useAlphaChannel, parent, id, text);}
IRRLICHT_C_API IGUIImage* IGUIEnvironment_addImage2(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, const wchar_t* text=0)
{return pointer->addImage(rectangle, parent, id, text);}
IRRLICHT_C_API IGUICheckBox* IGUIEnvironment_addCheckBox(IGUIEnvironment* pointer, bool checked, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, const wchar_t* text=0)
{return pointer->addCheckBox(checked, rectangle, parent, id, text);}
IRRLICHT_C_API IGUIListBox* IGUIEnvironment_addListBox(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, bool drawBackground=false)
{return pointer->addListBox(rectangle, parent, id, drawBackground);}
IRRLICHT_C_API IGUITreeView* IGUIEnvironment_addTreeView(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, bool drawBackground=false, bool scrollBarVertical = true, bool scrollBarHorizontal = false)
{return pointer->addTreeView(rectangle, parent, id, drawBackground, scrollBarVertical, scrollBarHorizontal);}
IRRLICHT_C_API IGUIMeshViewer* IGUIEnvironment_addMeshViewer(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, const wchar_t* text=0)
{return pointer->addMeshViewer(rectangle, parent, id, text);}
IRRLICHT_C_API IGUIFileOpenDialog* IGUIEnvironment_addFileOpenDialog(IGUIEnvironment* pointer, const wchar_t* title = 0, bool modal=true, IGUIElement* parent=0, s32 id=-1)
{return pointer->addFileOpenDialog(title, modal, parent, id);}
IRRLICHT_C_API IGUIColorSelectDialog* IGUIEnvironment_addColorSelectDialog(IGUIEnvironment* pointer, const wchar_t* title = 0, bool modal=true, IGUIElement* parent=0, s32 id=-1)
{return pointer->addColorSelectDialog(title, modal, parent, id);}
IRRLICHT_C_API IGUIStaticText* IGUIEnvironment_addStaticText(IGUIEnvironment* pointer, const wchar_t* text, const core::rect<s32>& rectangle, bool border=false, bool wordWrap=true, IGUIElement* parent=0, s32 id=-1, bool fillBackground = false)
{return pointer->addStaticText(text, rectangle, border, wordWrap, parent, id, fillBackground);}
IRRLICHT_C_API IGUIEditBox* IGUIEnvironment_addEditBox(IGUIEnvironment* pointer, const wchar_t* text, const core::rect<s32>& rectangle, bool border=true, IGUIElement* parent=0, s32 id=-1)
{return pointer->addEditBox(text, rectangle, border, parent, id);}
IRRLICHT_C_API IGUISpinBox* IGUIEnvironment_addSpinBox(IGUIEnvironment* pointer, const wchar_t* text, const core::rect<s32>& rectangle, bool border=true, IGUIElement* parent=0, s32 id=-1)
{return pointer->addSpinBox(text, rectangle, border, parent, id);}
IRRLICHT_C_API IGUIInOutFader* IGUIEnvironment_addInOutFader(IGUIEnvironment* pointer, const core::rect<s32>* rectangle=0, IGUIElement* parent=0, s32 id=-1)
{return pointer->addInOutFader(rectangle, parent, id);}
IRRLICHT_C_API IGUITabControl* IGUIEnvironment_addTabControl(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, bool fillbackground=false, bool border=true, s32 id=-1)
{return pointer->addTabControl(rectangle, parent, fillbackground, border, id);}
IRRLICHT_C_API IGUITab* IGUIEnvironment_addTab(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1)
{return pointer->addTab(rectangle, parent, id);}
IRRLICHT_C_API IGUIContextMenu* IGUIEnvironment_addContextMenu(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1)
{return pointer->addContextMenu(rectangle, parent, id);}
IRRLICHT_C_API IGUIContextMenu* IGUIEnvironment_addMenu(IGUIEnvironment* pointer, IGUIElement* parent=0, s32 id=-1)
{return pointer->addMenu(parent, id);}
IRRLICHT_C_API IGUIToolBar* IGUIEnvironment_addToolBar(IGUIEnvironment* pointer, IGUIElement* parent=0, s32 id=-1)
{return pointer->addToolBar(parent, id);}
IRRLICHT_C_API IGUIComboBox* IGUIEnvironment_addComboBox(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1)
{return pointer->addComboBox(rectangle, parent, id);}
IRRLICHT_C_API IGUITable* IGUIEnvironment_addTable(IGUIEnvironment* pointer, const core::rect<s32>& rectangle, IGUIElement* parent=0, s32 id=-1, bool drawBackground=false)
{return pointer->addTable(rectangle, parent, id, drawBackground);}
IRRLICHT_C_API IGUIElementFactory* IGUIEnvironment_getDefaultGUIElementFactory(IGUIEnvironment* pointer)
{return pointer->getDefaultGUIElementFactory();}
IRRLICHT_C_API void IGUIEnvironment_registerGUIElementFactory(IGUIEnvironment* pointer, IGUIElementFactory* factoryToAdd)
{pointer->registerGUIElementFactory(factoryToAdd);}
IRRLICHT_C_API u32 IGUIEnvironment_getRegisteredGUIElementFactoryCount(IGUIEnvironment* pointer)
{return pointer->getRegisteredGUIElementFactoryCount();}
IRRLICHT_C_API IGUIElementFactory* IGUIEnvironment_getGUIElementFactory(IGUIEnvironment* pointer, u32 index)
{return pointer->getGUIElementFactory(index);}
IRRLICHT_C_API IGUIElement* IGUIEnvironment_addGUIElement(IGUIEnvironment* pointer, const c8* elementName, IGUIElement* parent=0)
{return pointer->addGUIElement(elementName, parent);}
IRRLICHT_C_API bool IGUIEnvironment_saveGUI(IGUIEnvironment* pointer, const char* filename, IGUIElement* start=0)
{return pointer->saveGUI(filename, start);}
IRRLICHT_C_API bool IGUIEnvironment_saveGUI2(IGUIEnvironment* pointer, io::IWriteFile* file, IGUIElement* start=0)
{return pointer->saveGUI(file, start);}
IRRLICHT_C_API bool IGUIEnvironment_loadGUI(IGUIEnvironment* pointer, const char* filename, IGUIElement* parent=0)
{return pointer->loadGUI(filename, parent);}
IRRLICHT_C_API bool IGUIEnvironment_loadGUI2(IGUIEnvironment* pointer, io::IReadFile* file, IGUIElement* parent=0)
{return pointer->loadGUI(file, parent);}
IRRLICHT_C_API void IGUIEnvironment_serializeAttributes(IGUIEnvironment* pointer, io::IAttributes* out, io::SAttributeReadWriteOptions* options=0)
{pointer->serializeAttributes(out, options);}
IRRLICHT_C_API void IGUIEnvironment_deserializeAttributes(IGUIEnvironment* pointer, io::IAttributes* in, io::SAttributeReadWriteOptions* options=0)
{pointer->deserializeAttributes(in, options);}
IRRLICHT_C_API void IGUIEnvironment_writeGUIElement(IGUIEnvironment* pointer, io::IXMLWriter* writer, IGUIElement* node)
{pointer->writeGUIElement(writer, node);}
IRRLICHT_C_API void IGUIEnvironment_readGUIElement(IGUIEnvironment* pointer, io::IXMLReader* reader, IGUIElement* node)
{pointer->readGUIElement(reader, node);}
#if defined(_IRR_COMPILE_WITH_CGUITTFONT_)
IRRLICHT_C_API IGUIFont* IGUIEnvironment_getTTFont(IGUIEnvironment* pointer, const io::path& filename, u32 fontsize, bool antialias = true, bool transparency = true)
{return pointer->getFont(filename, fontsize, antialias, transparency);}
#endif

#ifdef __cplusplus
}
#endif

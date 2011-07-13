// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IGUISkin* IGUISkin_ctor(){return new IGUISkin();}
IRRLICHT_C_API video::SColor* IGUISkin_getColor(IGUISkin* pointer, EGUI_DEFAULT_COLOR color)
{return new video::SColor(pointer->getColor(color));}
IRRLICHT_C_API void IGUISkin_setColor(IGUISkin* pointer, EGUI_DEFAULT_COLOR which, const SColor& newColor = SColor(0,0,0,0))
{pointer->setColor(which, newColor);}
IRRLICHT_C_API s32 IGUISkin_getSize(IGUISkin* pointer, EGUI_DEFAULT_SIZE size){return pointer->getSize(size);}
IRRLICHT_C_API const wchar_t* IGUISkin_getDefaultText(IGUISkin* pointer, EGUI_DEFAULT_TEXT text){return pointer->getDefaultText(text);}
IRRLICHT_C_API void IGUISkin_setDefaultText(IGUISkin* pointer, EGUI_DEFAULT_TEXT which, const wchar_t* newText){pointer->setDefaultText(which, newText);}
IRRLICHT_C_API void IGUISkin_setSize(IGUISkin* pointer, EGUI_DEFAULT_SIZE which, s32 size){pointer->setSize(which, size);}
IRRLICHT_C_API IGUIFont* IGUISkin_getFont(IGUISkin* pointer, EGUI_DEFAULT_FONT which = EGDF_DEFAULT){return pointer->getFont(which);}
IRRLICHT_C_API void IGUISkin_setFont(IGUISkin* pointer, IGUIFont* font, EGUI_DEFAULT_FONT which = EGDF_DEFAULT){pointer->setFont(font, which);}
IRRLICHT_C_API IGUISpriteBank* IGUISkin_getSpriteBank(IGUISkin* pointer){return pointer->getSpriteBank();}
IRRLICHT_C_API void IGUISkin_setSpriteBank(IGUISkin* pointer, IGUISpriteBank* bank){pointer->setSpriteBank(bank);}
IRRLICHT_C_API u32 IGUISkin_getIcon(IGUISkin* pointer, EGUI_DEFAULT_ICON icon){return pointer->getIcon(icon);}
IRRLICHT_C_API void IGUISkin_setIcon(IGUISkin* pointer, EGUI_DEFAULT_ICON icon, u32 index){pointer->setIcon(icon, index);}
IRRLICHT_C_API void IGUISkin_draw3DButtonPaneStandard(IGUISkin* pointer, IGUIElement* element, const core::rect<s32>& rect, const core::rect<s32>* clip = 0){pointer->draw3DButtonPaneStandard(element, rect, clip);}
IRRLICHT_C_API void IGUISkin_draw3DButtonPanePressed(IGUISkin* pointer, IGUIElement* element, const core::rect<s32>& rect, const core::rect<s32>* clip = 0){pointer->draw3DButtonPanePressed(element, rect, clip);}
IRRLICHT_C_API void IGUISkin_draw3DSunkenPane(IGUISkin* pointer, IGUIElement* element, video::SColor* bgcolor, bool flat, bool fillBackGround, const core::rect<s32>& rect, const core::rect<s32>* clip = 0){pointer->draw3DSunkenPane(element, *bgcolor, flat, fillBackGround, rect, clip);}
IRRLICHT_C_API core::rect<s32>* IGUISkin_draw3DWindowBackground(IGUISkin* pointer, IGUIElement* element, bool drawTitleBar, video::SColor* titleBarColor, const core::rect<s32>& rect, const core::rect<s32>* clip = 0, core::rect<s32>* checkClientArea = 0){return &pointer->draw3DWindowBackground(element, drawTitleBar, *titleBarColor, rect, clip, checkClientArea);}
IRRLICHT_C_API void IGUISkin_draw3DMenuPane(IGUISkin* pointer, IGUIElement* element, const core::rect<s32>& rect, const core::rect<s32>* clip = 0){pointer->draw3DMenuPane(element, rect, clip);}
IRRLICHT_C_API void IGUISkin_draw3DToolBar(IGUISkin* pointer, IGUIElement* element, const core::rect<s32>& rect, const core::rect<s32>* clip = 0){pointer->draw3DToolBar(element, rect, clip);}
IRRLICHT_C_API void IGUISkin_draw3DTabButton(IGUISkin* pointer, IGUIElement* element, bool active, const core::rect<s32>& rect, const core::rect<s32>* clip = 0, gui::EGUI_ALIGNMENT alignment = EGUIA_UPPERLEFT){pointer->draw3DTabButton(element, active, rect, clip, alignment);}
IRRLICHT_C_API void IGUISkin_draw3DTabBody(IGUISkin* pointer, IGUIElement* element, bool border, bool background, const core::rect<s32>& rect, const core::rect<s32>* clip = 0, s32 tabHeight = -1, gui::EGUI_ALIGNMENT alignment = EGUIA_UPPERLEFT){pointer->draw3DTabBody(element, border, background, rect, clip, tabHeight, alignment);}
IRRLICHT_C_API void IGUISkin_drawIcon(IGUISkin* pointer, IGUIElement* element, EGUI_DEFAULT_ICON icon, const core::position2di& position, u32 starttime = 0, u32 currenttime = 0, bool loop = false, const core::rect<s32>* clip=0){pointer->drawIcon(element, icon, position, starttime, currenttime, loop, clip);}
IRRLICHT_C_API void IGUISkin_draw2DRectangle(IGUISkin* pointer, IGUIElement* element, const video::SColor &color, const core::rect<s32>& pos, const core::rect<s32>* clip = 0){pointer->draw2DRectangle(element, color, pos, clip);}
IRRLICHT_C_API EGUI_SKIN_TYPE IGUISkin_getType(IGUISkin* pointer){return pointer->getType();}

#ifdef __cplusplus
}
#endif

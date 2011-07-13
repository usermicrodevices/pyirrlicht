// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IGUIStaticText* IGUIStaticText_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIStaticText*)new IGUIElement(EGUIET_STATIC_TEXT, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIStaticText_setOverrideFont(IGUIStaticText* pointer, IGUIFont* font=0){pointer->setOverrideFont(font);}
IRRLICHT_C_API IGUIFont* IGUIStaticText_getOverrideFont(IGUIStaticText* pointer){return pointer->getOverrideFont();}
IRRLICHT_C_API void IGUIStaticText_setOverrideColor(IGUIStaticText* pointer, video::SColor* color){pointer->setOverrideColor(*color);}
IRRLICHT_C_API video::SColor const& IGUIStaticText_getOverrideColor(IGUIStaticText* pointer){return pointer->getOverrideColor();}
IRRLICHT_C_API void IGUIStaticText_enableOverrideColor(IGUIStaticText* pointer, bool enable){pointer->enableOverrideColor(enable);}
IRRLICHT_C_API bool IGUIStaticText_isOverrideColorEnabled(IGUIStaticText* pointer){return pointer->isOverrideColorEnabled();}
IRRLICHT_C_API void IGUIStaticText_setBackgroundColor(IGUIStaticText* pointer, video::SColor* color){pointer->setBackgroundColor(*color);}
IRRLICHT_C_API void IGUIStaticText_setDrawBackground(IGUIStaticText* pointer, bool draw){pointer->setDrawBackground(draw);}
IRRLICHT_C_API void IGUIStaticText_setDrawBorder(IGUIStaticText* pointer, bool draw){pointer->setDrawBorder(draw);}
IRRLICHT_C_API void IGUIStaticText_setTextAlignment(IGUIStaticText* pointer, EGUI_ALIGNMENT horizontal, EGUI_ALIGNMENT vertical){pointer->setTextAlignment(horizontal, vertical);}
IRRLICHT_C_API void IGUIStaticText_setWordWrap(IGUIStaticText* pointer, bool enable){pointer->setWordWrap(enable);}
IRRLICHT_C_API bool IGUIStaticText_isWordWrapEnabled(IGUIStaticText* pointer){return pointer->isWordWrapEnabled();}
IRRLICHT_C_API s32 IGUIStaticText_getTextHeight(IGUIStaticText* pointer){return pointer->getTextHeight();}
IRRLICHT_C_API s32 IGUIStaticText_getTextWidth(IGUIStaticText* pointer){return pointer->getTextWidth();}

#ifdef __cplusplus
}
#endif

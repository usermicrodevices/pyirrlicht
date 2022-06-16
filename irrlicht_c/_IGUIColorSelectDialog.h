// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIColorSelectDialog
IRRLICHT_C_API IGUIColorSelectDialog* IGUIColorSelectDialog_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle){return (IGUIColorSelectDialog*)new IGUIElement(EGUIET_COLOR_SELECT_DIALOG, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIColorSelectDialog_delete(IGUIColorSelectDialog* pointer){if(pointer)delete pointer;}

#ifdef __cplusplus
}
#endif

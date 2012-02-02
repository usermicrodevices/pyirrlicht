// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUICheckBox
IRRLICHT_C_API IGUICheckBox* IGUICheckBox_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUICheckBox*)new IGUIElement(EGUIET_CHECK_BOX, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUICheckBox_setChecked(IGUICheckBox* pointer, bool checked)
{pointer->setChecked(checked);}
IRRLICHT_C_API bool IGUICheckBox_isChecked(IGUICheckBox* pointer)
{return pointer->isChecked();}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUISpinBox
IRRLICHT_C_API IGUISpinBox* IGUISpinBox_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUISpinBox*)new IGUIElement(EGUIET_SPIN_BOX, environment, parent, id, *rectangle);}
IRRLICHT_C_API IGUIEditBox* IGUISpinBox_getEditBox(IGUISpinBox* pointer)
{return pointer->getEditBox();}
IRRLICHT_C_API void IGUISpinBox_setValue(IGUISpinBox* pointer, f32 val)
{pointer->setValue(val);}
IRRLICHT_C_API f32 IGUISpinBox_getValue(IGUISpinBox* pointer)
{return pointer->getValue();}
IRRLICHT_C_API void IGUISpinBox_setRange(IGUISpinBox* pointer, f32 min, f32 max)
{pointer->setRange(min, max);}
IRRLICHT_C_API f32 IGUISpinBox_getMin(IGUISpinBox* pointer)
{return pointer->getMin();}
IRRLICHT_C_API f32 IGUISpinBox_getMax(IGUISpinBox* pointer)
{return pointer->getMax();}
IRRLICHT_C_API void IGUISpinBox_setStepSize(IGUISpinBox* pointer, f32 step=1.f)
{pointer->setStepSize(step);}
IRRLICHT_C_API void IGUISpinBox_setDecimalPlaces(IGUISpinBox* pointer, s32 places)
{pointer->setDecimalPlaces(places);}
IRRLICHT_C_API f32 IGUISpinBox_getStepSize(IGUISpinBox* pointer)
{return pointer->getStepSize();}

#ifdef __cplusplus
}
#endif

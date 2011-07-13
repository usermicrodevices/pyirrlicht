// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ICursorControl
IRRLICHT_C_API void ICursorControl_setVisible(ICursorControl* pointer, bool visible)
{pointer->setVisible(visible);}
IRRLICHT_C_API bool ICursorControl_isVisible(ICursorControl* pointer)
{return pointer->isVisible();}
IRRLICHT_C_API void ICursorControl_setPositionF(ICursorControl* pointer, const position2d<f32> &pos)
{pointer->setPosition(pos);}
IRRLICHT_C_API void ICursorControl_setPositionF2(ICursorControl* pointer, f32 x, f32 y)
{pointer->setPosition(x, y);}
IRRLICHT_C_API void ICursorControl_setPositionI(ICursorControl* pointer, const position2d<s32> &pos)
{pointer->setPosition(pos);}
IRRLICHT_C_API void ICursorControl_setPositionI2(ICursorControl* pointer, s32 x, s32 y)
{pointer->setPosition(x, y);}
IRRLICHT_C_API const position2d<s32>& ICursorControl_getPosition(ICursorControl* pointer)
{return (const position2d<s32>&)pointer->getPosition();}
IRRLICHT_C_API const position2d<f32>& ICursorControl_getRelativePosition(ICursorControl* pointer)
{return (const position2d<f32>&)pointer->getRelativePosition();}
IRRLICHT_C_API void ICursorControl_setReferenceRect(ICursorControl* pointer, core::rect<s32>* rect=0)
{pointer->setReferenceRect(rect);}

#ifdef __cplusplus
}
#endif

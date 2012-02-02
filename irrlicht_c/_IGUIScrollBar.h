// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IGUIScrollBar* IGUIScrollBar_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIScrollBar*)new IGUIElement(EGUIET_SCROLL_BAR, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIScrollBar_setMax(IGUIScrollBar* pointer, s32 max)
{pointer->setMax(max);}
IRRLICHT_C_API s32 IGUIScrollBar_getMax(IGUIScrollBar* pointer)
{return pointer->getMax();}
IRRLICHT_C_API void IGUIScrollBar_setMin(IGUIScrollBar* pointer, s32 max)
{pointer->setMin(max);}
IRRLICHT_C_API s32 IGUIScrollBar_getMin(IGUIScrollBar* pointer)
{return pointer->getMin();}
IRRLICHT_C_API s32 IGUIScrollBar_getSmallStep(IGUIScrollBar* pointer)
{return pointer->getSmallStep();}
IRRLICHT_C_API void IGUIScrollBar_setSmallStep(IGUIScrollBar* pointer, s32 step)
{pointer->setSmallStep(step);}
IRRLICHT_C_API s32 IGUIScrollBar_getLargeStep(IGUIScrollBar* pointer)
{return pointer->getLargeStep();}
IRRLICHT_C_API void IGUIScrollBar_setLargeStep(IGUIScrollBar* pointer, s32 step)
{pointer->setLargeStep(step);}
IRRLICHT_C_API s32 IGUIScrollBar_getPos(IGUIScrollBar* pointer)
{return pointer->getPos();}
IRRLICHT_C_API void IGUIScrollBar_setPos(IGUIScrollBar* pointer, s32 pos)
{pointer->setPos(pos);}

#ifdef __cplusplus
}
#endif

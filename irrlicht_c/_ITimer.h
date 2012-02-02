// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ITimer
//IRRLICHT_C_API void ITimer_Destructor(ITimer* pointer){delete pointer;}
IRRLICHT_C_API u32 ITimer_getRealTime(ITimer* pointer)
{return pointer->getRealTime();}
IRRLICHT_C_API u32 ITimer_getTime(ITimer* pointer)
{return pointer->getTime();}
IRRLICHT_C_API void ITimer_setTime(ITimer* pointer, u32 time)
{pointer->setTime(time);}
IRRLICHT_C_API void ITimer_stop(ITimer* pointer)
{pointer->stop();}
IRRLICHT_C_API void ITimer_start(ITimer* pointer)
{pointer->start();}
IRRLICHT_C_API void ITimer_setSpeed(ITimer* pointer, f32 speed = 1.0f)
{pointer->setSpeed(speed);}
IRRLICHT_C_API f32 ITimer_getSpeed(ITimer* pointer)
{return pointer->getSpeed();}
IRRLICHT_C_API bool ITimer_isStopped(ITimer* pointer)
{return pointer->isStopped();}
IRRLICHT_C_API void ITimer_tick(ITimer* pointer)
{pointer->tick();}

#ifdef __cplusplus
}
#endif

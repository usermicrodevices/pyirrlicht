// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IAnimatedMeshMD2
IRRLICHT_C_API void IAnimatedMeshMD2_getFrameLoop1(IAnimatedMeshMD2* pointer, EMD2_ANIMATION_TYPE l, s32& outBegin, s32& outEnd, s32& outFPS)
{pointer->getFrameLoop(l, outBegin, outEnd, outFPS);}
IRRLICHT_C_API bool IAnimatedMeshMD2_getFrameLoop2(IAnimatedMeshMD2* pointer, const c8* name, s32& outBegin, s32& outEnd, s32& outFPS)
{return pointer->getFrameLoop(name, outBegin, outEnd, outFPS);}
IRRLICHT_C_API s32 IAnimatedMeshMD2_getAnimationCount(IAnimatedMeshMD2* pointer)
{return pointer->getAnimationCount();}
IRRLICHT_C_API const c8* IAnimatedMeshMD2_getAnimationName(IAnimatedMeshMD2* pointer, s32 nr)
{return pointer->getAnimationName(nr);}

#ifdef __cplusplus
}
#endif

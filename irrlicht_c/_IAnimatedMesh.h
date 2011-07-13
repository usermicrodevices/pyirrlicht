// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IAnimatedMesh
IRRLICHT_C_API u32 IAnimatedMesh_getFrameCount(IAnimatedMesh* pointer)
{return pointer->getFrameCount();}
IRRLICHT_C_API IMesh* IAnimatedMesh_getMesh(IAnimatedMesh* pointer, s32 frame, s32 detailLevel=255, s32 startFrameLoop=-1, s32 endFrameLoop=-1)
{return pointer->getMesh(frame, detailLevel, startFrameLoop, endFrameLoop);}
IRRLICHT_C_API E_ANIMATED_MESH_TYPE IAnimatedMesh_getMeshType(IAnimatedMesh* pointer)
{return pointer->getMeshType();}

#ifdef __cplusplus
}
#endif

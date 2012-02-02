// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ITriangleSelector
//IRRLICHT_C_API void ITriangleSelector_Destructor(ITriangleSelector* pointer){delete pointer;}
IRRLICHT_C_API s32 ITriangleSelector_getTriangleCount(ITriangleSelector* pointer){return pointer->getTriangleCount();}
IRRLICHT_C_API void ITriangleSelector_getTriangles(ITriangleSelector* pointer, core::triangle3df* triangles, s32 arraySize, s32& outTriangleCount, const core::matrix4* transform=0){pointer->getTriangles(triangles, arraySize, outTriangleCount, transform);}
IRRLICHT_C_API void ITriangleSelector_getTriangles2(ITriangleSelector* pointer, core::triangle3df* triangles, s32 arraySize, s32& outTriangleCount, const core::aabbox3d<f32>& box, const core::matrix4* transform=0){pointer->getTriangles(triangles, arraySize, outTriangleCount, box, transform);}
IRRLICHT_C_API void ITriangleSelector_getTriangles3(ITriangleSelector* pointer, core::triangle3df* triangles, s32 arraySize, s32& outTriangleCount, const core::line3d<f32>& line, const core::matrix4* transform=0){pointer->getTriangles(triangles, arraySize, outTriangleCount, line, transform);}
IRRLICHT_C_API const ISceneNode* ITriangleSelector_getSceneNodeForTriangle(ITriangleSelector* pointer, u32 triangleIndex){return pointer->getSceneNodeForTriangle(triangleIndex);}

#ifdef __cplusplus
}
#endif

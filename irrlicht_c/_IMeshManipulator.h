// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IMeshManipulator : public IReferenceCounted
IRRLICHT_C_API void IMeshManipulator_flipSurfaces(IMeshManipulator* pointer, IMesh* mesh)
{pointer->flipSurfaces(mesh);}

IRRLICHT_C_API void IMeshManipulator_setVertexColorAlpha(IMeshManipulator* pointer, IMesh* mesh, s32 alpha)
{pointer->setVertexColorAlpha(mesh, alpha);}

IRRLICHT_C_API void IMeshManipulator_setVertexColors(IMeshManipulator* pointer, IMesh* mesh, video::SColor* color)
{pointer->setVertexColors(mesh, *color);}

IRRLICHT_C_API void IMeshManipulator_recalculateNormals1(IMeshManipulator* pointer, IMesh* mesh, bool smooth = false, bool angleWeighted = false)
{pointer->recalculateNormals(mesh, smooth, angleWeighted);}

IRRLICHT_C_API void IMeshManipulator_recalculateNormals2(IMeshManipulator* pointer, IMeshBuffer* buffer, bool smooth = false, bool angleWeighted = false)
{pointer->recalculateNormals(buffer, smooth, angleWeighted);}

IRRLICHT_C_API void IMeshManipulator_recalculateTangents(IMeshManipulator* pointer, IMesh* mesh, bool recalculateNormals = false, bool smooth = false, bool angleWeighted = false)
{pointer->recalculateTangents(mesh, recalculateNormals, smooth, angleWeighted);}

IRRLICHT_C_API void IMeshManipulator_scale1(IMeshManipulator* pointer, IMesh* mesh, const core::vector3df* factor)
{pointer->scale(mesh, *factor);}

IRRLICHT_C_API void IMeshManipulator_scale2(IMeshManipulator* pointer, IMeshBuffer* buffer, const core::vector3df* factor)
{pointer->scale(buffer, *factor);}

IRRLICHT_C_API void IMeshManipulator_scaleMesh(IMeshManipulator* pointer, IMesh* mesh, const core::vector3df* factor)
{pointer->scaleMesh(mesh, *factor);}

IRRLICHT_C_API void IMeshManipulator_scaleTCoords1(IMeshManipulator* pointer, scene::IMesh* mesh, const core::vector2df* factor, u32 level = 1)
{pointer->scaleTCoords(mesh, *factor, level);}

IRRLICHT_C_API void IMeshManipulator_scaleTCoords2(IMeshManipulator* pointer, scene::IMeshBuffer* buffer, const core::vector2df* factor, u32 level = 1)
{pointer->scaleTCoords(buffer, *factor, level);}

IRRLICHT_C_API void IMeshManipulator_transform1(IMeshManipulator* pointer, IMesh* mesh, const core::matrix4* m)
{pointer->transform(mesh, *m);}

IRRLICHT_C_API void IMeshManipulator_transform2(IMeshManipulator* pointer, IMeshBuffer* buffer, const core::matrix4* m)
{pointer->transform(buffer, *m);}

IRRLICHT_C_API void IMeshManipulator_transformMesh(IMeshManipulator* pointer, IMesh* mesh, const core::matrix4* m)
{pointer->transformMesh(mesh, *m);}

IRRLICHT_C_API SMesh* IMeshManipulator_createMeshCopy(IMeshManipulator* pointer, IMesh* mesh)
{return pointer->createMeshCopy(mesh);}

IRRLICHT_C_API void IMeshManipulator_makePlanarTextureMapping1(IMeshManipulator* pointer, IMesh* mesh, f32 resolution = 0.001f)
{pointer->makePlanarTextureMapping(mesh, resolution);}

IRRLICHT_C_API void IMeshManipulator_makePlanarTextureMapping2(IMeshManipulator* pointer, scene::IMeshBuffer* meshbuffer, f32 resolution = 0.001f)
{pointer->makePlanarTextureMapping(meshbuffer, resolution);}

IRRLICHT_C_API void IMeshManipulator_makePlanarTextureMapping3(IMeshManipulator* pointer, scene::IMeshBuffer* buffer, f32 resolutionS, f32 resolutionT, u8 axis, const core::vector3df* offset)
{pointer->makePlanarTextureMapping(buffer, resolutionS, resolutionT, axis, *offset);}

IRRLICHT_C_API IMesh* IMeshManipulator_createMeshWithTangents(IMeshManipulator* pointer, IMesh* mesh, bool recalculateNormals = false, bool smooth = false, bool angleWeighted = false, bool recalculateTangents = true)
{return pointer->createMeshWithTangents(mesh, recalculateNormals, smooth, angleWeighted, recalculateTangents);}

IRRLICHT_C_API IMesh* IMeshManipulator_createMeshWith2TCoords(IMeshManipulator* pointer, IMesh* mesh)
{return pointer->createMeshWith2TCoords(mesh);}

IRRLICHT_C_API IMesh* IMeshManipulator_createMeshWith1TCoords(IMeshManipulator* pointer, IMesh* mesh)
{return pointer->createMeshWith1TCoords(mesh);}

IRRLICHT_C_API IMesh* IMeshManipulator_createMeshUniquePrimitives(IMeshManipulator* pointer, IMesh* mesh)
{return pointer->createMeshUniquePrimitives(mesh);}

IRRLICHT_C_API IMesh* IMeshManipulator_createMeshWelded(IMeshManipulator* pointer, IMesh* mesh, f32 tolerance = core::ROUNDING_ERROR_f32)
{return pointer->createMeshWelded(mesh, tolerance);}

IRRLICHT_C_API s32 IMeshManipulator_getPolyCount1(IMeshManipulator* pointer, IMesh* mesh)
{return pointer->getPolyCount(mesh);}

IRRLICHT_C_API s32 IMeshManipulator_getPolyCount2(IMeshManipulator* pointer, IAnimatedMesh* mesh)
{return pointer->getPolyCount(mesh);}

IRRLICHT_C_API IAnimatedMesh* IMeshManipulator_createAnimatedMesh(IMeshManipulator* pointer, IMesh* mesh, scene::E_ANIMATED_MESH_TYPE type = scene::EAMT_UNKNOWN)
{return pointer->createAnimatedMesh(mesh, type);}

//IRRLICHT_C_API const bool IMeshManipulator_apply1(IMeshManipulator* pointer, const IVertexManipulator* func, IMeshBuffer* buffer, bool boundingBoxUpdate = false)
//{return pointer->apply(*func, buffer, boundingBoxUpdate);}
//
//IRRLICHT_C_API const bool IMeshManipulator_apply2(IMeshManipulator* pointer, const void* func, IMesh* mesh, bool boundingBoxUpdate = false)
//{return pointer->apply(func, mesh, boundingBoxUpdate);}

#ifdef __cplusplus
}
#endif

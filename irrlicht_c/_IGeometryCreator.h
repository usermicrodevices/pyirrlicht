// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IGeometryCreator* IGeometryCreator_ctor(){return new IGeometryCreator();}

IRRLICHT_C_API IMesh* IGeometryCreator_createCubeMesh(IGeometryCreator* pointer, const core::vector3df& size=core::vector3df(5.f,5.f,5.f))
{return pointer->createCubeMesh(size);}

IRRLICHT_C_API IMesh* IGeometryCreator_createHillPlaneMesh(IGeometryCreator* pointer, const core::dimension2d<f32>& tileSize, const core::dimension2d<u32>& tileCount, video::SMaterial* material, f32 hillHeight, const core::dimension2d<f32>& countHills, const core::dimension2d<f32>& textureRepeatCount)
{return pointer->createHillPlaneMesh(tileSize, tileCount, material, hillHeight, countHills, textureRepeatCount);}

IRRLICHT_C_API IMesh* IGeometryCreator_createPlaneMesh(IGeometryCreator* pointer, const core::dimension2d<f32>& tileSize, const core::dimension2d<u32>& tileCount, video::SMaterial* material, const core::dimension2d<f32>& textureRepeatCount)
{return pointer->createPlaneMesh(tileSize, tileCount, material, textureRepeatCount);}

IRRLICHT_C_API IMesh* IGeometryCreator_createTerrainMesh(IGeometryCreator* pointer, video::IImage* texture, video::IImage* heightmap, const core::dimension2d<f32>& stretchSize, f32 maxHeight, video::IVideoDriver* driver, const core::dimension2d<u32>& defaultVertexBlockSize, bool debugBorders = false)
{return pointer->createTerrainMesh(texture, heightmap, stretchSize, maxHeight, driver, defaultVertexBlockSize, debugBorders);}

IRRLICHT_C_API IMesh* IGeometryCreator_createArrowMesh(IGeometryCreator* pointer, const u32 tesselationCylinder = 4, const u32 tesselationCone = 8, const f32 height = 1.f, const f32 cylinderHeight = 0.6f, const f32 widthCylinder = 0.05f, const f32 widthCone = 0.3f, const video::SColor& colorCylinder = 0xFFFFFFFF, const video::SColor& colorCone = 0xFFFFFFFF)
{return pointer->createArrowMesh(tesselationCylinder, tesselationCone, height, cylinderHeight, widthCylinder, widthCone, colorCylinder, colorCone);}

IRRLICHT_C_API IMesh* IGeometryCreator_createSphereMesh(IGeometryCreator* pointer, f32 radius = 5.f, u32 polyCountX = 16, u32 polyCountY = 16)
{return pointer->createSphereMesh(radius, polyCountX, polyCountY);}

IRRLICHT_C_API IMesh* IGeometryCreator_createCylinderMesh(IGeometryCreator* pointer, f32 radius, f32 length, u32 tesselation, const video::SColor& color = video::SColor(0xffffffff), bool closeTop = true, f32 oblique = 0.f)
{return pointer->createCylinderMesh(radius, length, tesselation, color, closeTop, oblique);}

IRRLICHT_C_API IMesh* IGeometryCreator_createConeMesh(IGeometryCreator* pointer, f32 radius, f32 length, u32 tesselation, const video::SColor& colorTop = video::SColor(0xffffffff), const video::SColor& colorBottom = video::SColor(0xffffffff), f32 oblique = 0.f)
{return pointer->createConeMesh(radius, length, tesselation, colorTop, colorBottom, oblique);}

IRRLICHT_C_API IMesh* IGeometryCreator_createVolumeLightMesh(IGeometryCreator* pointer, const u32 subdivideU = 32, const u32 subdivideV = 32, const video::SColor& footColor = 0xffffffff, const video::SColor& tailColor = 0xffffffff, const f32 lpDistance = 8.f, const core::vector3df& lightDim = core::vector3df(1.f,1.2f,1.f))
{return pointer->createVolumeLightMesh(subdivideU, subdivideV, footColor, tailColor, lpDistance, lightDim);}

#ifdef __cplusplus
}
#endif

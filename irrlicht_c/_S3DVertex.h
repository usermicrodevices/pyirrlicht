// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API u32 tool_getVertexPitchFromType(E_VERTEX_TYPE vertexType){return getVertexPitchFromType(vertexType);}

//struct S3DVertex
IRRLICHT_C_API S3DVertex* S3DVertex_ctor1(int length = 1)
{S3DVertex* pointer; pointer = new S3DVertex[length]; return pointer;}
IRRLICHT_C_API S3DVertex* S3DVertex_ctor2(f32 x, f32 y, f32 z, f32 nx, f32 ny, f32 nz, SColor* c, f32 tu, f32 tv)
{return new S3DVertex(x, y, z, nx, ny, nz, *c, tu, tv);}
IRRLICHT_C_API S3DVertex* S3DVertex_ctor3(const core::vector3df& pos, const core::vector3df& normal, SColor* color, const core::vector2d<f32>& tcoords)
{return new S3DVertex(pos, normal, *color, tcoords);}
IRRLICHT_C_API S3DVertex* S3DVertex_get_item(S3DVertex* pointer, int index)
{return &pointer[index];}
IRRLICHT_C_API void S3DVertex_set_item(S3DVertex* pointer, S3DVertex* value, int index)
{pointer[index] = *value;}
IRRLICHT_C_API core::vector3df* S3DVertex_get_Pos(S3DVertex* pointer, int index)
{return &pointer[index].Pos;}
IRRLICHT_C_API void S3DVertex_set_Pos(S3DVertex* pointer, core::vector3df* value, int index)
{pointer[index].Pos = *value;}
IRRLICHT_C_API core::vector3df* S3DVertex_get_Normal(S3DVertex* pointer, int index)
{return &pointer[index].Normal;}
IRRLICHT_C_API void S3DVertex_set_Normal(S3DVertex* pointer, core::vector3df* value, int index)
{pointer[index].Normal = *value;}
IRRLICHT_C_API SColor* S3DVertex_get_Color(S3DVertex* pointer, int index)
{return &pointer[index].Color;}
IRRLICHT_C_API void S3DVertex_set_Color(S3DVertex* pointer, SColor* value, int index)
{pointer[index].Color = *value;}
IRRLICHT_C_API core::vector2d<f32>* S3DVertex_get_TCoords(S3DVertex* pointer, int index)
{return &pointer[index].TCoords;}
IRRLICHT_C_API void S3DVertex_set_TCoords(S3DVertex* pointer, core::vector2d<f32>* value, int index)
{pointer[index].TCoords = *value;}
IRRLICHT_C_API bool S3DVertex_eq(S3DVertex* pointer, const S3DVertex* other, int index){return pointer[index].operator==(*other);}
IRRLICHT_C_API bool S3DVertex_ne(S3DVertex* pointer, const S3DVertex* other, int index){return pointer[index].operator!=(*other);}
IRRLICHT_C_API bool S3DVertex_less(S3DVertex* pointer, const S3DVertex* other, int index){return pointer[index].operator<(*other);}
IRRLICHT_C_API E_VERTEX_TYPE S3DVertex_getType(S3DVertex* pointer, int index){return pointer[index].getType();}
#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR > 7)
IRRLICHT_C_API const S3DVertex S3DVertex_getInterpolated(S3DVertex* pointer, const S3DVertex* other, f32 d, int index){return pointer[index].getInterpolated(*other, d);}
#endif

//struct S3DVertex2TCoords : public S3DVertex
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor1(int length = 1)
{S3DVertex2TCoords* pointer; pointer = new S3DVertex2TCoords[length]; return pointer;}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor2(f32 x, f32 y, f32 z, SColor* c, f32 tu, f32 tv, f32 tu2, f32 tv2)
{return new S3DVertex2TCoords(x, y, z, *c, tu, tv, tu2, tv2);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor3(const core::vector3df* pos, SColor* color, const core::vector2d<f32>* tcoords, const core::vector2d<f32>* tcoords2)
{return new S3DVertex2TCoords(*pos, *color, *tcoords, *tcoords2);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor4(const core::vector3df* pos, const core::vector3df* normal, SColor* color, const core::vector2d<f32>* tcoords, const core::vector2d<f32>* tcoords2)
{return new S3DVertex2TCoords(*pos, *normal, *color, *tcoords, *tcoords2);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor5(f32 x, f32 y, f32 z, f32 nx, f32 ny, f32 nz, SColor* c, f32 tu, f32 tv, f32 tu2, f32 tv2)
{return new S3DVertex2TCoords(x, y, z, nx, ny, nz, *c, tu, tv, tu2, tv2);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor6(f32 x, f32 y, f32 z, f32 nx, f32 ny, f32 nz, SColor* c, f32 tu, f32 tv)
{return new S3DVertex2TCoords(x, y, z, nx, ny, nz, *c, tu, tv);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor7(const core::vector3df* pos, const core::vector3df* normal, SColor* color, const core::vector2d<f32>* tcoords)
{return new S3DVertex2TCoords(*pos, *normal, *color, *tcoords);}
IRRLICHT_C_API S3DVertex2TCoords* S3DVertex2TCoords_ctor8(S3DVertex* other)
{return new S3DVertex2TCoords(*other);}
IRRLICHT_C_API core::vector2d<f32>* S3DVertex2TCoords_get_TCoords2(S3DVertex2TCoords* pointer, int index)
{return &pointer[index].TCoords2;}
IRRLICHT_C_API void S3DVertex2TCoords_set_TCoords2(S3DVertex2TCoords* pointer, core::vector2d<f32>* value, int index)
{pointer[index].TCoords2 = *value;}
//IRRLICHT_C_API bool S3DVertex2TCoords_eq(S3DVertex2TCoords* pointer, const S3DVertex2TCoords* other, int index){return pointer[index].operator==(*other);}
//IRRLICHT_C_API bool S3DVertex2TCoords_ne(S3DVertex2TCoords* pointer, const S3DVertex2TCoords* other, int index){return pointer[index].operator!=(*other);}
//IRRLICHT_C_API bool S3DVertex2TCoords_less(S3DVertex2TCoords* pointer, const S3DVertex2TCoords* other, int index){return pointer[index].operator<(*other);}

//struct S3DVertexTangents : public S3DVertex
IRRLICHT_C_API S3DVertexTangents* S3DVertexTangents_ctor1(int length = 1)
{S3DVertexTangents* pointer; pointer = new S3DVertexTangents[length]; return pointer;}
IRRLICHT_C_API S3DVertexTangents* S3DVertexTangents_ctor2(f32 x, f32 y, f32 z, f32 nx=0.0f, f32 ny=0.0f, f32 nz=0.0f, const SColor& c = SColor(255, 255, 255, 255), f32 tu=0.0f, f32 tv=0.0f, f32 tanx=0.0f, f32 tany=0.0f, f32 tanz=0.0f, f32 bx=0.0f, f32 by=0.0f, f32 bz=0.0f)
{return new S3DVertexTangents(x, y, z, nx, ny, nz, c, tu, tv, tanx, tany, tanz, bx, by, bz);}
IRRLICHT_C_API S3DVertexTangents* S3DVertexTangents_ctor3(const core::vector3df* pos, SColor* c, const core::vector2df* tcoords)
{return new S3DVertexTangents(*pos, *c, *tcoords);}
IRRLICHT_C_API S3DVertexTangents* S3DVertexTangents_ctor4(const core::vector3df* pos, const core::vector3df* normal, SColor* c, const core::vector2df* tcoords, const core::vector3df& tangent=core::vector3df(), const core::vector3df& binormal=core::vector3df())
{return new S3DVertexTangents(*pos, *normal, *c, *tcoords, tangent, binormal);}
IRRLICHT_C_API core::vector3d<f32>* S3DVertexTangents_get_Tangent(S3DVertexTangents* pointer, int index)
{return &pointer[index].Tangent;}
IRRLICHT_C_API void S3DVertexTangents_set_Tangent(S3DVertexTangents* pointer, core::vector3d<f32>* value, int index)
{pointer[index].Tangent = *value;}
IRRLICHT_C_API core::vector3d<f32>* S3DVertexTangents_get_Binormal(S3DVertexTangents* pointer, int index)
{return &pointer[index].Binormal;}
IRRLICHT_C_API void S3DVertexTangents_set_Binormal(S3DVertexTangents* pointer, core::vector3d<f32>* value, int index)
{pointer[index].Binormal = *value;}

#ifdef __cplusplus
}
#endif

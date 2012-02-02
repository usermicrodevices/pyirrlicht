// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= S3DVertex
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
IRRLICHT_C_API bool S3DVertex_eq(S3DVertex* pointer, const S3DVertex& other, int index){return pointer[index].operator==(other);}
IRRLICHT_C_API bool S3DVertex_ne(S3DVertex* pointer, const S3DVertex& other, int index){return pointer[index].operator!=(other);}
IRRLICHT_C_API bool S3DVertex_less(S3DVertex* pointer, const S3DVertex& other, int index){return pointer[index].operator<(other);}
IRRLICHT_C_API E_VERTEX_TYPE S3DVertex_getType(S3DVertex* pointer, int index){return pointer[index].getType();}

#ifdef __cplusplus
}
#endif

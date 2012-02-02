// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IQ3LevelMesh
IRRLICHT_C_API const quake3::IShader* IQ3LevelMesh_getShader1(IQ3LevelMesh* pointer, const c8* filename, bool fileNameIsValid = true)
{return pointer->getShader(filename, fileNameIsValid);}
IRRLICHT_C_API const quake3::IShader* IQ3LevelMesh_getShader2(IQ3LevelMesh* pointer, u32 index)
{return pointer->getShader(index);}
IRRLICHT_C_API quake3::tQ3EntityList* IQ3LevelMesh_getEntityList(IQ3LevelMesh* pointer)
{return &pointer->getEntityList();}

#ifdef __cplusplus
}
#endif

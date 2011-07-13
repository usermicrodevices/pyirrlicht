// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API u32 _MATERIAL_MAX_TEXTURES = MATERIAL_MAX_TEXTURES;

//================= SMaterial
IRRLICHT_C_API SMaterial* SMaterial_ctor1(){return new SMaterial();}
IRRLICHT_C_API SMaterial* SMaterial_ctor2(SMaterial* other){return new SMaterial(*other);}
IRRLICHT_C_API SMaterial* SMaterial_set(SMaterial* pointer, SMaterial* other){return &pointer->operator=(*other);}
//IRRLICHT_C_API void SMaterial_Destructor(SMaterial* pointer){delete pointer;}
IRRLICHT_C_API SMaterialLayer* SMaterial_get_TextureLayer(SMaterial* pointer, s32 index = 0){return &pointer->TextureLayer[index];}
IRRLICHT_C_API E_MATERIAL_TYPE SMaterial_get_MaterialType(SMaterial* pointer){return pointer->MaterialType;}
IRRLICHT_C_API SColor* SMaterial_get_AmbientColor(SMaterial* pointer){return &pointer->AmbientColor;}
IRRLICHT_C_API SColor* SMaterial_get_DiffuseColor(SMaterial* pointer){return &pointer->DiffuseColor;}
IRRLICHT_C_API SColor* SMaterial_get_EmissiveColor(SMaterial* pointer){return &pointer->EmissiveColor;}
IRRLICHT_C_API SColor* SMaterial_get_SpecularColor(SMaterial* pointer){return &pointer->SpecularColor;}
IRRLICHT_C_API f32 SMaterial_get_Shininess(SMaterial* pointer){return pointer->Shininess;}
IRRLICHT_C_API f32 SMaterial_get_MaterialTypeParam(SMaterial* pointer){return pointer->MaterialTypeParam;}
IRRLICHT_C_API f32 SMaterial_get_MaterialTypeParam2(SMaterial* pointer){return pointer->MaterialTypeParam2;}
IRRLICHT_C_API f32 SMaterial_get_Thickness(SMaterial* pointer){return pointer->Thickness;}
IRRLICHT_C_API u8 SMaterial_get_ZBuffer(SMaterial* pointer){return pointer->ZBuffer;}
IRRLICHT_C_API u8 SMaterial_get_AntiAliasing(SMaterial* pointer){return pointer->AntiAliasing;}
IRRLICHT_C_API u8 SMaterial_get_ColorMask(SMaterial* pointer){return pointer->ColorMask;}
IRRLICHT_C_API u8 SMaterial_get_ColorMaterial(SMaterial* pointer){return pointer->ColorMaterial;}
IRRLICHT_C_API bool SMaterial_get_Wireframe(SMaterial* pointer){return pointer->Wireframe;}
IRRLICHT_C_API bool SMaterial_get_PointCloud(SMaterial* pointer){return pointer->PointCloud;}
IRRLICHT_C_API bool SMaterial_get_GouraudShading(SMaterial* pointer){return pointer->GouraudShading;}
IRRLICHT_C_API bool SMaterial_get_Lighting(SMaterial* pointer){return pointer->Lighting;}
IRRLICHT_C_API bool SMaterial_get_ZWriteEnable(SMaterial* pointer){return pointer->ZWriteEnable;}
IRRLICHT_C_API bool SMaterial_get_BackfaceCulling(SMaterial* pointer){return pointer->BackfaceCulling;}
IRRLICHT_C_API bool SMaterial_get_FrontfaceCulling(SMaterial* pointer){return pointer->FrontfaceCulling;}
IRRLICHT_C_API bool SMaterial_get_FogEnable(SMaterial* pointer){return pointer->FogEnable;}
IRRLICHT_C_API bool SMaterial_get_NormalizeNormals(SMaterial* pointer){return pointer->NormalizeNormals;}
IRRLICHT_C_API void SMaterial_set_TextureLayer(SMaterial* pointer, SMaterialLayer *texture_layer[]){for (u32 i=0; i<MATERIAL_MAX_TEXTURES; ++i) pointer->TextureLayer[i] = *texture_layer[i];}
IRRLICHT_C_API void SMaterial_set_MaterialType(SMaterial* pointer, E_MATERIAL_TYPE value){pointer->MaterialType = value;}
IRRLICHT_C_API void SMaterial_set_AmbientColor(SMaterial* pointer, const SColor& value){pointer->AmbientColor = value;}
IRRLICHT_C_API void SMaterial_set_DiffuseColor(SMaterial* pointer, const SColor& value){pointer->DiffuseColor = value;}
IRRLICHT_C_API void SMaterial_set_EmissiveColor(SMaterial* pointer, const SColor& value){pointer->EmissiveColor = value;}
IRRLICHT_C_API void SMaterial_set_SpecularColor(SMaterial* pointer, const SColor& value){pointer->SpecularColor = value;}
IRRLICHT_C_API void SMaterial_set_Shininess(SMaterial* pointer, f32 value){pointer->Shininess = value;}
IRRLICHT_C_API void SMaterial_set_MaterialTypeParam(SMaterial* pointer, f32 value){pointer->MaterialTypeParam = value;}
IRRLICHT_C_API void SMaterial_set_MaterialTypeParam2(SMaterial* pointer, f32 value){pointer->MaterialTypeParam2 = value;}
IRRLICHT_C_API void SMaterial_set_Thickness(SMaterial* pointer, f32 value){pointer->Thickness = value;}
IRRLICHT_C_API void SMaterial_set_ZBuffer(SMaterial* pointer, u8 value){pointer->ZBuffer = value;}
IRRLICHT_C_API void SMaterial_set_AntiAliasing(SMaterial* pointer, u8 value){pointer->AntiAliasing = value;}
IRRLICHT_C_API void SMaterial_set_ColorMask(SMaterial* pointer, u8 value){pointer->ColorMask = value;}
IRRLICHT_C_API void SMaterial_set_ColorMaterial(SMaterial* pointer, u8 value){pointer->ColorMaterial = value;}
IRRLICHT_C_API void SMaterial_set_Wireframe(SMaterial* pointer, bool value){pointer->Wireframe = value;}
IRRLICHT_C_API void SMaterial_set_PointCloud(SMaterial* pointer, bool value){pointer->PointCloud = value;}
IRRLICHT_C_API void SMaterial_set_GouraudShading(SMaterial* pointer, bool value){pointer->GouraudShading = value;}
IRRLICHT_C_API void SMaterial_set_Lighting(SMaterial* pointer, bool value){pointer->Lighting = value;}
IRRLICHT_C_API void SMaterial_set_ZWriteEnable(SMaterial* pointer, bool value){pointer->ZWriteEnable = value;}
IRRLICHT_C_API void SMaterial_set_BackfaceCulling(SMaterial* pointer, bool value){pointer->BackfaceCulling = value;}
IRRLICHT_C_API void SMaterial_set_FrontfaceCulling(SMaterial* pointer, bool value){pointer->FrontfaceCulling = value;}
IRRLICHT_C_API void SMaterial_set_FogEnable(SMaterial* pointer, bool value){pointer->FogEnable = value;}
IRRLICHT_C_API void SMaterial_set_NormalizeNormals(SMaterial* pointer, bool value){pointer->NormalizeNormals = value;}
IRRLICHT_C_API matrix4* SMaterial_getTextureMatrix(SMaterial* pointer, u32 i){return &pointer->getTextureMatrix(i);}
IRRLICHT_C_API void SMaterial_setTextureMatrix(SMaterial* pointer, u32 i, const matrix4& mat){pointer->setTextureMatrix(i, mat);}
IRRLICHT_C_API ITexture* SMaterial_getTexture(SMaterial* pointer, u32 i){return pointer->getTexture(i);}
IRRLICHT_C_API void SMaterial_setTexture(SMaterial* pointer, u32 i, ITexture* tex){pointer->setTexture(i, tex);}
IRRLICHT_C_API void SMaterial_setFlag(SMaterial* pointer, E_MATERIAL_FLAG flag, bool value){pointer->setFlag(flag, value);}
IRRLICHT_C_API bool SMaterial_getFlag(SMaterial* pointer, E_MATERIAL_FLAG flag){return pointer->getFlag(flag);}
IRRLICHT_C_API bool SMaterial_operator_noteq(SMaterial* pointer, const SMaterial& b){return pointer->operator!=(b);}
IRRLICHT_C_API bool SMaterial_operator_eq(SMaterial* pointer, const SMaterial& b){return pointer->operator==(b);}
IRRLICHT_C_API bool SMaterial_isTransparent(SMaterial* pointer){return pointer->isTransparent();}

#ifdef __cplusplus
}
#endif

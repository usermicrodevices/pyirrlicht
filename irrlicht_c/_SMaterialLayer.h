// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SMaterialLayer
IRRLICHT_C_API SMaterialLayer* SMaterialLayer_ctor1(){return new SMaterialLayer();}
IRRLICHT_C_API SMaterialLayer* SMaterialLayer_ctor2(const SMaterialLayer& other){return new SMaterialLayer(other);}
//IRRLICHT_C_API void SMaterialLayer_Destructor(SMaterialLayer* pointer){delete pointer;}
IRRLICHT_C_API SMaterialLayer* SMaterialLayer_set(SMaterialLayer& pointer, const SMaterialLayer& other){return &pointer.operator=(other);}
IRRLICHT_C_API void SMaterialLayer_set_Texture(SMaterialLayer& pointer, ITexture* value){pointer.Texture = value;}
IRRLICHT_C_API ITexture* SMaterialLayer_get_Texture(SMaterialLayer& pointer){return pointer.Texture;}
IRRLICHT_C_API void SMaterialLayer_set_TextureWrapU(SMaterialLayer& pointer, u8 value){pointer.TextureWrapU = value;}
IRRLICHT_C_API u8 SMaterialLayer_get_TextureWrapU(SMaterialLayer& pointer){return pointer.TextureWrapU;}
IRRLICHT_C_API void SMaterialLayer_set_TextureWrapV(SMaterialLayer& pointer, u8 value){pointer.TextureWrapV = value;}
IRRLICHT_C_API u8 SMaterialLayer_get_TextureWrapV(SMaterialLayer& pointer){return pointer.TextureWrapV;}
IRRLICHT_C_API void SMaterialLayer_set_BilinearFilter(SMaterialLayer& pointer, bool value){pointer.BilinearFilter = value;}
IRRLICHT_C_API bool SMaterialLayer_get_BilinearFilter(SMaterialLayer& pointer){return pointer.BilinearFilter;}
IRRLICHT_C_API void SMaterialLayer_set_TrilinearFilter(SMaterialLayer& pointer, bool value){pointer.TrilinearFilter = value;}
IRRLICHT_C_API bool SMaterialLayer_get_TrilinearFilter(SMaterialLayer& pointer){return pointer.TrilinearFilter;}
IRRLICHT_C_API void SMaterialLayer_set_AnisotropicFilter(SMaterialLayer& pointer, u8 value){pointer.AnisotropicFilter = value;}
IRRLICHT_C_API u8 SMaterialLayer_get_AnisotropicFilter(SMaterialLayer& pointer){return pointer.AnisotropicFilter;}
IRRLICHT_C_API void SMaterialLayer_set_LODBias(SMaterialLayer& pointer, s8* value){pointer.LODBias = *value;}
IRRLICHT_C_API s8* SMaterialLayer_get_LODBias(SMaterialLayer& pointer){return &pointer.LODBias;}
IRRLICHT_C_API matrix4* SMaterialLayer_getTextureMatrix(SMaterialLayer& pointer){return &pointer.getTextureMatrix();}
IRRLICHT_C_API void SMaterialLayer_setTextureMatrix(SMaterialLayer& pointer, const core::matrix4& mat){pointer.setTextureMatrix(mat);}
IRRLICHT_C_API bool SMaterialLayer_operator_eq(SMaterialLayer& pointer, const SMaterialLayer& b){return pointer.operator==(b);}
IRRLICHT_C_API bool SMaterialLayer_operator_noteq(SMaterialLayer& pointer, const SMaterialLayer& b){return pointer.operator!=(b);}

#ifdef __cplusplus
}
#endif

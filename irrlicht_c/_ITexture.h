// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ITexture
//IRRLICHT_C_API ITexture* ITexture_ctor(const io::path& name){return new ITexture(name);}
IRRLICHT_C_API void* ITexture_lock(ITexture* pointer, bool readOnly = false, u32 mipmapLevel = 0){return pointer->lock(readOnly, mipmapLevel);}
IRRLICHT_C_API void ITexture_unlock(ITexture* pointer){pointer->unlock();}
IRRLICHT_C_API const dimension2d<u32>& ITexture_getOriginalSize(ITexture* pointer){return (const dimension2d<u32>&)pointer->getOriginalSize();}
IRRLICHT_C_API const dimension2d<u32>& ITexture_getSize(ITexture* pointer){return (const dimension2d<u32>&)pointer->getSize();}
IRRLICHT_C_API E_DRIVER_TYPE ITexture_getDriverType(ITexture* pointer){return pointer->getDriverType();}
IRRLICHT_C_API ECOLOR_FORMAT ITexture_getColorFormat(ITexture* pointer){return pointer->getColorFormat();}
IRRLICHT_C_API u32 ITexture_getPitch(ITexture* pointer){return pointer->getPitch();}
IRRLICHT_C_API bool ITexture_hasMipMaps(ITexture* pointer){return pointer->hasMipMaps();}
IRRLICHT_C_API bool ITexture_hasAlpha(ITexture* pointer){return pointer->hasAlpha();}
IRRLICHT_C_API void ITexture_regenerateMipMapLevels(ITexture* pointer){pointer->regenerateMipMapLevels();}
IRRLICHT_C_API bool ITexture_isRenderTarget(ITexture* pointer){return pointer->isRenderTarget();}
IRRLICHT_C_API const io::path& ITexture_getName(ITexture* pointer){return (const io::path&)pointer->getName();}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ITexture
//IRRLICHT_C_API ITexture* ITexture_ctor(const io::path& name){return new ITexture(name);}
IRRLICHT_C_API void ITexture_delete(ITexture* pointer){delete pointer;}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API void* ITexture_lock(ITexture* pointer, bool readOnly = false, u32 mipmapLevel = 0){return pointer->lock(readOnly, mipmapLevel);}
#else
IRRLICHT_C_API void* ITexture_lock(ITexture* pointer, E_TEXTURE_LOCK_MODE mode = ETLM_READ_WRITE, u32 mipmapLevel = 0){return pointer->lock(mode, mipmapLevel);}
#endif
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
#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 7)
IRRLICHT_C_API const fschar_t* ITexture_getName(ITexture* pointer){return pointer->getName().c_str();}
#else
IRRLICHT_C_API const fschar_t* ITexture_getName(ITexture* pointer){return pointer->getName().getPath().c_str();}
#endif

#ifdef __cplusplus
}
#endif

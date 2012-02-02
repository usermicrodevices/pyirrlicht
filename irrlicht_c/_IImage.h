// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class IImage : public virtual IReferenceCounted

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IImage* IImage_ctor(){return new IImage();}

IRRLICHT_C_API void* IImage_lock(IImage* pointer){return pointer->lock();}
IRRLICHT_C_API void IImage_unlock(IImage* pointer){pointer->unlock();}
IRRLICHT_C_API const core::dimension2d<u32>& IImage_getDimension(IImage* pointer){return pointer->getDimension();}
IRRLICHT_C_API u32 IImage_getBitsPerPixel(IImage* pointer){return pointer->getBitsPerPixel();}
IRRLICHT_C_API u32 IImage_getBytesPerPixel(IImage* pointer){return pointer->getBytesPerPixel();}
IRRLICHT_C_API u32 IImage_getImageDataSizeInBytes(IImage* pointer){return pointer->getImageDataSizeInBytes();}
IRRLICHT_C_API u32 IImage_getImageDataSizeInPixels(IImage* pointer){return pointer->getImageDataSizeInPixels();}
IRRLICHT_C_API SColor* IImage_getPixel(IImage* pointer, u32 x, u32 y){return &pointer->getPixel(x, y);}
IRRLICHT_C_API void IImage_setPixel(IImage* pointer, u32 x, u32 y, const SColor &color, bool blend = false){pointer->setPixel(x, y, color, blend);}
IRRLICHT_C_API ECOLOR_FORMAT IImage_getColorFormat(IImage* pointer){return pointer->getColorFormat();}
IRRLICHT_C_API u32 IImage_getRedMask(IImage* pointer){return pointer->getRedMask();}
IRRLICHT_C_API u32 IImage_getGreenMask(IImage* pointer){return pointer->getGreenMask();}
IRRLICHT_C_API u32 IImage_getBlueMask(IImage* pointer){return pointer->getBlueMask();}
IRRLICHT_C_API u32 IImage_getAlphaMask(IImage* pointer){return pointer->getAlphaMask();}
IRRLICHT_C_API u32 IImage_getPitch(IImage* pointer){return pointer->getPitch();}
IRRLICHT_C_API void IImage_copyToScaling1(IImage* pointer, void* target, u32 width, u32 height, ECOLOR_FORMAT format=ECF_A8R8G8B8, u32 pitch=0){pointer->copyToScaling(target, width, height, format, pitch);}
IRRLICHT_C_API void IImage_copyToScaling2(IImage* pointer, IImage* target){pointer->copyToScaling(target);}
IRRLICHT_C_API void IImage_copyTo1(IImage* pointer, IImage* target, const core::position2d<s32>& pos=core::position2d<s32>(0,0)){pointer->copyTo(target, pos);}
IRRLICHT_C_API void IImage_copyTo2(IImage* pointer, IImage* target, const core::position2d<s32>& pos, const core::rect<s32>& sourceRect, const core::rect<s32>* clipRect=0){pointer->copyTo(target, pos, sourceRect, clipRect);}
IRRLICHT_C_API void IImage_copyToWithAlpha(IImage* pointer, IImage* target, const core::position2d<s32>& pos, const core::rect<s32>& sourceRect, const SColor &color, const core::rect<s32>* clipRect = 0){pointer->copyToWithAlpha(target, pos, sourceRect, color, clipRect);}
IRRLICHT_C_API void IImage_copyToScalingBoxFilter(IImage* pointer, IImage* target, s32 bias = 0, bool blend = false){pointer->copyToScalingBoxFilter(target, bias, blend);}
IRRLICHT_C_API void IImage_fill(IImage* pointer, const SColor &color){pointer->fill(color);}
IRRLICHT_C_API u32 IImage_getBitsPerPixelFromFormat(IImage* pointer, const ECOLOR_FORMAT format){return pointer->getBitsPerPixelFromFormat(format);}
IRRLICHT_C_API bool IImage_isRenderTargetOnlyFormat(IImage* pointer, const ECOLOR_FORMAT format){return pointer->isRenderTargetOnlyFormat(format);}

#ifdef __cplusplus
}
#endif

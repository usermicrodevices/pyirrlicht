// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIImage
IRRLICHT_C_API IGUIImage* IGUIImage_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIImage*)new IGUIElement(EGUIET_IMAGE, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIImage_setImage(IGUIImage* pointer, video::ITexture* image)
{pointer->setImage(image);}
IRRLICHT_C_API void IGUIImage_setColor(IGUIImage* pointer, video::SColor& color)
{pointer->setColor(color);}
IRRLICHT_C_API void IGUIImage_setScaleImage(IGUIImage* pointer, bool scale)
{pointer->setScaleImage(scale);}
IRRLICHT_C_API void IGUIImage_setUseAlphaChannel(IGUIImage* pointer, bool use)
{pointer->setUseAlphaChannel(use);}
IRRLICHT_C_API bool IGUIImage_isImageScaled(IGUIImage* pointer)
{return pointer->isImageScaled();}
IRRLICHT_C_API bool IGUIImage_isAlphaChannelUsed(IGUIImage* pointer)
{return pointer->isAlphaChannelUsed();}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API SViewFrustum* SViewFrustum_ctor1(const core::matrix4& mat){return new SViewFrustum(mat);}
IRRLICHT_C_API SViewFrustum* SViewFrustum_ctor2(const SViewFrustum& other){return new SViewFrustum(other);}
//IRRLICHT_C_API void SViewFrustum_Destructor(SViewFrustum* pointer){delete pointer;}
IRRLICHT_C_API void SViewFrustum_transform(SViewFrustum* pointer, const core::matrix4& mat){pointer->transform(mat);}
IRRLICHT_C_API const core::vector3df* SViewFrustum_getFarLeftUp(SViewFrustum* pointer){return &pointer->getFarLeftUp();}
IRRLICHT_C_API const core::vector3df* SViewFrustum_getFarLeftDown(SViewFrustum* pointer){return &pointer->getFarLeftDown();}
IRRLICHT_C_API const core::vector3df* SViewFrustum_getFarRightUp(SViewFrustum* pointer){return &pointer->getFarRightUp();}
IRRLICHT_C_API const core::vector3df* SViewFrustum_getFarRightDown(SViewFrustum* pointer){return &pointer->getFarRightDown();}
IRRLICHT_C_API const core::aabbox3d<f32>* SViewFrustum_getBoundingBox(SViewFrustum* pointer){return &pointer->getBoundingBox();}
IRRLICHT_C_API void SViewFrustum_recalculateBoundingBox(SViewFrustum* pointer){pointer->recalculateBoundingBox();}
IRRLICHT_C_API void SViewFrustum_setFrom(SViewFrustum* pointer, const core::matrix4& mat){pointer->setFrom(mat);}
IRRLICHT_C_API core::matrix4& SViewFrustum_getTransform(SViewFrustum* pointer, video::E_TRANSFORMATION_STATE state){return pointer->getTransform(state);}
IRRLICHT_C_API bool SViewFrustum_clipLine(SViewFrustum* pointer, core::line3d<f32>& line){return pointer->clipLine(line);}

#ifdef __cplusplus
}
#endif

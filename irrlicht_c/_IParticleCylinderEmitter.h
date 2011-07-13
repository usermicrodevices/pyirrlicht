// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleCylinderEmitter : public IParticleEmitter
IRRLICHT_C_API void IParticleCylinderEmitter_setCenter(IParticleCylinderEmitter* pointer, const core::vector3df* center)
{pointer->setCenter(*center);}
IRRLICHT_C_API void IParticleCylinderEmitter_setNormal(IParticleCylinderEmitter* pointer, const core::vector3df* normal)
{pointer->setNormal(*normal);}
IRRLICHT_C_API void IParticleCylinderEmitter_setRadius(IParticleCylinderEmitter* pointer, f32 radius)
{pointer->setRadius(radius);}
IRRLICHT_C_API void IParticleCylinderEmitter_setLength(IParticleCylinderEmitter* pointer, f32 length)
{pointer->setLength(length);}
IRRLICHT_C_API void IParticleCylinderEmitter_setOutlineOnly(IParticleCylinderEmitter* pointer, bool outlineOnly = true)
{pointer->setOutlineOnly(outlineOnly);}
IRRLICHT_C_API const core::vector3df* IParticleCylinderEmitter_getCenter(IParticleCylinderEmitter* pointer)
{return &pointer->getCenter();}
IRRLICHT_C_API const core::vector3df* IParticleCylinderEmitter_getNormal(IParticleCylinderEmitter* pointer)
{return &pointer->getNormal();}
IRRLICHT_C_API f32 IParticleCylinderEmitter_getRadius(IParticleCylinderEmitter* pointer)
{return pointer->getRadius();}
IRRLICHT_C_API f32 IParticleCylinderEmitter_getLength(IParticleCylinderEmitter* pointer)
{return pointer->getLength();}
IRRLICHT_C_API bool IParticleCylinderEmitter_getOutlineOnly(IParticleCylinderEmitter* pointer)
{return pointer->getOutlineOnly();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleCylinderEmitter_getType(IParticleCylinderEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

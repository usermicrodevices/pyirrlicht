// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleSphereEmitter : public IParticleEmitter
IRRLICHT_C_API void IParticleSphereEmitter_setCenter(IParticleSphereEmitter* pointer, const core::vector3df* center)
{pointer->setCenter(*center);}
IRRLICHT_C_API void IParticleSphereEmitter_setRadius(IParticleSphereEmitter* pointer, f32 radius)
{pointer->setRadius(radius);}
IRRLICHT_C_API const core::vector3df* IParticleSphereEmitter_getCenter(IParticleSphereEmitter* pointer)
{return &pointer->getCenter();}
IRRLICHT_C_API f32 IParticleSphereEmitter_getRadius(IParticleSphereEmitter* pointer)
{return pointer->getRadius();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleSphereEmitter_getType(IParticleSphereEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

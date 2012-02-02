// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleRingEmitter : public IParticleEmitter
IRRLICHT_C_API void IParticleRingEmitter_setCenter(IParticleRingEmitter* pointer, const core::vector3df* center)
{pointer->setCenter(*center);}
IRRLICHT_C_API void IParticleRingEmitter_setRadius(IParticleRingEmitter* pointer, f32 radius)
{pointer->setRadius(radius);}
IRRLICHT_C_API void IParticleRingEmitter_setRingThickness(IParticleRingEmitter* pointer, f32 ringThickness)
{pointer->setRingThickness(ringThickness);}
IRRLICHT_C_API const core::vector3df* IParticleRingEmitter_getCenter(IParticleRingEmitter* pointer)
{return &pointer->getCenter();}
IRRLICHT_C_API f32 IParticleRingEmitter_getRadius(IParticleRingEmitter* pointer)
{return pointer->getRadius();}
IRRLICHT_C_API f32 IParticleRingEmitter_getRingThickness(IParticleRingEmitter* pointer)
{return pointer->getRingThickness();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleRingEmitter_getType(IParticleRingEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

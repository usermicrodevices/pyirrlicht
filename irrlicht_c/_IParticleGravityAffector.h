// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleGravityAffector : public IParticleAffector
IRRLICHT_C_API void IParticleGravityAffector_setTimeForceLost(IParticleGravityAffector* pointer, f32 timeForceLost)
{pointer->setTimeForceLost(timeForceLost);}
IRRLICHT_C_API void IParticleGravityAffector_setGravity(IParticleGravityAffector* pointer, const core::vector3df* gravity)
{pointer->setGravity(*gravity);}
IRRLICHT_C_API f32 IParticleGravityAffector_getTimeForceLost(IParticleGravityAffector* pointer)
{return pointer->getTimeForceLost();}
IRRLICHT_C_API const core::vector3df* IParticleGravityAffector_getGravity(IParticleGravityAffector* pointer)
{return &pointer->getGravity();}
IRRLICHT_C_API E_PARTICLE_AFFECTOR_TYPE IParticleGravityAffector_getType(IParticleGravityAffector* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

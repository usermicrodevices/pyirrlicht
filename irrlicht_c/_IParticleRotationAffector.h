// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleRotationAffector : public IParticleAffector
IRRLICHT_C_API void IParticleRotationAffector_setPivotPoint(IParticleRotationAffector* pointer, const core::vector3df* point)
{pointer->setPivotPoint(*point);}
IRRLICHT_C_API void IParticleRotationAffector_setSpeed(IParticleRotationAffector* pointer, const core::vector3df* speed)
{pointer->setSpeed(*speed);}
IRRLICHT_C_API const core::vector3df* IParticleRotationAffector_getPivotPoint(IParticleRotationAffector* pointer)
{return &pointer->getPivotPoint();}
IRRLICHT_C_API const core::vector3df* IParticleRotationAffector_getSpeed(IParticleRotationAffector* pointer)
{return &pointer->getSpeed();}
IRRLICHT_C_API E_PARTICLE_AFFECTOR_TYPE IParticleRotationAffector_getType(IParticleRotationAffector* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

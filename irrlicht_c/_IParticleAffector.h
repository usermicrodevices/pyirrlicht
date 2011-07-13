// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleAffector : public IAttributeExchangingObject
IRRLICHT_C_API IParticleAffector* IParticleAffector_ctor()
{
	//return new IParticleAffector();
	IParticleAffector* result = 0;
	return result;
}

IRRLICHT_C_API void IParticleAffector_affect(IParticleAffector* pointer, u32 now, SParticle* particlearray, u32 count)
{pointer->affect(now, particlearray, count);}

IRRLICHT_C_API void IParticleAffector_setEnabled(IParticleAffector* pointer, bool enabled)
{pointer->setEnabled(enabled);}

IRRLICHT_C_API bool IParticleAffector_getEnabled(IParticleAffector* pointer)
{return pointer->getEnabled();}

IRRLICHT_C_API E_PARTICLE_AFFECTOR_TYPE IParticleAffector_getType(IParticleAffector* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

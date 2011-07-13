// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleFadeOutAffector : public IParticleAffector
IRRLICHT_C_API void IParticleFadeOutAffector_setTargetColor(IParticleFadeOutAffector* pointer, const video::SColor* targetColor)
{pointer->setTargetColor(*targetColor);}
IRRLICHT_C_API void IParticleFadeOutAffector_setFadeOutTime(IParticleFadeOutAffector* pointer, f32 fadeOutTime)
{pointer->setFadeOutTime(fadeOutTime);}
IRRLICHT_C_API const video::SColor* IParticleFadeOutAffector_getTargetColor(IParticleFadeOutAffector* pointer)
{return &pointer->getTargetColor();}
IRRLICHT_C_API f32 IParticleFadeOutAffector_getFadeOutTime(IParticleFadeOutAffector* pointer)
{return pointer->getFadeOutTime();}
IRRLICHT_C_API E_PARTICLE_AFFECTOR_TYPE IParticleFadeOutAffector_getType(IParticleFadeOutAffector* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleEmitter : public IAttributeExchangingObject
IRRLICHT_C_API s32 IParticleEmitter_emitt(IParticleEmitter* pointer, u32 now, u32 timeSinceLastCall, SParticle*& outArray)
{return pointer->emitt(now, timeSinceLastCall, outArray);}
IRRLICHT_C_API void IParticleEmitter_setDirection(IParticleEmitter* pointer, const core::vector3df* newDirection)
{pointer->setDirection(*newDirection);}
IRRLICHT_C_API void IParticleEmitter_setMinParticlesPerSecond(IParticleEmitter* pointer, u32 minPPS)
{pointer->setMinParticlesPerSecond(minPPS);}
IRRLICHT_C_API void IParticleEmitter_setMaxParticlesPerSecond(IParticleEmitter* pointer, u32 maxPPS)
{pointer->setMaxParticlesPerSecond(maxPPS);}
IRRLICHT_C_API void IParticleEmitter_setMinStartColor(IParticleEmitter* pointer, const video::SColor* color)
{pointer->setMinStartColor(*color);}
IRRLICHT_C_API void IParticleEmitter_setMaxStartColor(IParticleEmitter* pointer, const video::SColor* color)
{pointer->setMaxStartColor(*color);}
IRRLICHT_C_API void IParticleEmitter_setMaxStartSize(IParticleEmitter* pointer, const core::dimension2df* size)
{pointer->setMaxStartSize(*size);}
IRRLICHT_C_API void IParticleEmitter_setMinStartSize(IParticleEmitter* pointer, const core::dimension2df* size)
{pointer->setMinStartSize(*size);}
IRRLICHT_C_API const core::vector3df* IParticleEmitter_getDirection(IParticleEmitter* pointer)
{return &pointer->getDirection();}
IRRLICHT_C_API u32 IParticleEmitter_getMinParticlesPerSecond(IParticleEmitter* pointer)
{return pointer->getMinParticlesPerSecond();}
IRRLICHT_C_API u32 IParticleEmitter_getMaxParticlesPerSecond(IParticleEmitter* pointer)
{return pointer->getMaxParticlesPerSecond();}
IRRLICHT_C_API const video::SColor* IParticleEmitter_getMinStartColor(IParticleEmitter* pointer)
{return &pointer->getMinStartColor();}
IRRLICHT_C_API const video::SColor* IParticleEmitter_getMaxStartColor(IParticleEmitter* pointer)
{return &pointer->getMaxStartColor();}
IRRLICHT_C_API const core::dimension2df* IParticleEmitter_getMaxStartSize(IParticleEmitter* pointer)
{return &pointer->getMaxStartSize();}
IRRLICHT_C_API const core::dimension2df* IParticleEmitter_getMinStartSize(IParticleEmitter* pointer)
{return &pointer->getMinStartSize();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleEmitter_getType(IParticleEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

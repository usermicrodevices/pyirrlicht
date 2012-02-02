// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleAttractionAffector : public IParticleAffector
IRRLICHT_C_API void IParticleAttractionAffector_setPoint(IParticleAttractionAffector* pointer, const core::vector3df* point)
{pointer->setPoint(*point);}
IRRLICHT_C_API void IParticleAttractionAffector_setAttract(IParticleAttractionAffector* pointer, bool attract)
{pointer->setAttract(attract);}
IRRLICHT_C_API void IParticleAttractionAffector_setAffectX(IParticleAttractionAffector* pointer, bool affect)
{pointer->setAffectX(affect);}
IRRLICHT_C_API void IParticleAttractionAffector_setAffectY(IParticleAttractionAffector* pointer, bool affect)
{pointer->setAffectY(affect);}
IRRLICHT_C_API void IParticleAttractionAffector_setAffectZ(IParticleAttractionAffector* pointer, bool affect)
{pointer->setAffectZ(affect);}
IRRLICHT_C_API const core::vector3df* IParticleAttractionAffector_getPoint(IParticleAttractionAffector* pointer)
{return &pointer->getPoint();}
IRRLICHT_C_API bool IParticleAttractionAffector_getAttract(IParticleAttractionAffector* pointer)
{return pointer->getAttract();}
IRRLICHT_C_API bool IParticleAttractionAffector_getAffectX(IParticleAttractionAffector* pointer)
{return pointer->getAffectX();}
IRRLICHT_C_API bool IParticleAttractionAffector_getAffectY(IParticleAttractionAffector* pointer)
{return pointer->getAffectY();}
IRRLICHT_C_API bool IParticleAttractionAffector_getAffectZ(IParticleAttractionAffector* pointer)
{return pointer->getAffectZ();}
IRRLICHT_C_API E_PARTICLE_AFFECTOR_TYPE IParticleAttractionAffector_getType(IParticleAttractionAffector* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

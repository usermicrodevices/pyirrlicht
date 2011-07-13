// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleMeshEmitter : public IParticleEmitter
IRRLICHT_C_API void IParticleMeshEmitter_setMesh(IParticleMeshEmitter* pointer, IMesh* mesh)
{pointer->setMesh(mesh);}
IRRLICHT_C_API void IParticleMeshEmitter_setUseNormalDirection(IParticleMeshEmitter* pointer, bool useNormalDirection = true)
{pointer->setUseNormalDirection(useNormalDirection);}
IRRLICHT_C_API void IParticleMeshEmitter_setNormalDirectionModifier(IParticleMeshEmitter* pointer, f32 normalDirectionModifier)
{pointer->setNormalDirectionModifier(normalDirectionModifier);}
IRRLICHT_C_API void IParticleMeshEmitter_setEveryMeshVertex(IParticleMeshEmitter* pointer, bool everyMeshVertex = true)
{pointer->setEveryMeshVertex(everyMeshVertex);}
IRRLICHT_C_API const IMesh* IParticleMeshEmitter_getMesh(IParticleMeshEmitter* pointer)
{return pointer->getMesh();}
IRRLICHT_C_API bool IParticleMeshEmitter_isUsingNormalDirection(IParticleMeshEmitter* pointer)
{return pointer->isUsingNormalDirection();}
IRRLICHT_C_API f32 IParticleMeshEmitter_getNormalDirectionModifier(IParticleMeshEmitter* pointer)
{return pointer->getNormalDirectionModifier();}
IRRLICHT_C_API bool IParticleMeshEmitter_getEveryMeshVertex(IParticleMeshEmitter* pointer)
{return pointer->getEveryMeshVertex();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleMeshEmitter_getType(IParticleMeshEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

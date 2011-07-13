// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleAnimatedMeshSceneNodeEmitter : public IParticleEmitter
IRRLICHT_C_API void IParticleAnimatedMeshSceneNodeEmitter_setAnimatedMeshSceneNode(IParticleAnimatedMeshSceneNodeEmitter* pointer, IAnimatedMeshSceneNode* node)
{pointer->setAnimatedMeshSceneNode(node);}
IRRLICHT_C_API void IParticleAnimatedMeshSceneNodeEmitter_setUseNormalDirection(IParticleAnimatedMeshSceneNodeEmitter* pointer, bool useNormalDirection = true)
{pointer->setUseNormalDirection(useNormalDirection);}
IRRLICHT_C_API void IParticleAnimatedMeshSceneNodeEmitter_setNormalDirectionModifier(IParticleAnimatedMeshSceneNodeEmitter* pointer, f32 normalDirectionModifier)
{pointer->setNormalDirectionModifier(normalDirectionModifier);}
IRRLICHT_C_API void IParticleAnimatedMeshSceneNodeEmitter_setEveryMeshVertex(IParticleAnimatedMeshSceneNodeEmitter* pointer, bool everyMeshVertex = true)
{pointer->setEveryMeshVertex(everyMeshVertex);}
IRRLICHT_C_API const IAnimatedMeshSceneNode* IParticleAnimatedMeshSceneNodeEmitter_getAnimatedMeshSceneNode(IParticleAnimatedMeshSceneNodeEmitter* pointer)
{return pointer->getAnimatedMeshSceneNode();}
IRRLICHT_C_API bool IParticleAnimatedMeshSceneNodeEmitter_isUsingNormalDirection(IParticleAnimatedMeshSceneNodeEmitter* pointer)
{return pointer->isUsingNormalDirection();}
IRRLICHT_C_API f32 IParticleAnimatedMeshSceneNodeEmitter_getNormalDirectionModifier(IParticleAnimatedMeshSceneNodeEmitter* pointer)
{return pointer->getNormalDirectionModifier();}
IRRLICHT_C_API bool IParticleAnimatedMeshSceneNodeEmitter_getEveryMeshVertex(IParticleAnimatedMeshSceneNodeEmitter* pointer)
{return pointer->getEveryMeshVertex();}
IRRLICHT_C_API E_PARTICLE_EMITTER_TYPE IParticleAnimatedMeshSceneNodeEmitter_getType(IParticleAnimatedMeshSceneNodeEmitter* pointer)
{return pointer->getType();}

#ifdef __cplusplus
}
#endif

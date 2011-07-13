// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IParticleSystemSceneNode : public ISceneNode
IRRLICHT_C_API IParticleSystemSceneNode* IParticleSystemSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = core::vector3df(0,0,0), const core::vector3df& scale = core::vector3df(1.0f, 1.0f, 1.0f))
//{return new IParticleSystemSceneNode(parent, mgr, id, position, rotation, scale);}
{
	IParticleSystemSceneNode* node = 0;
	node->setParent(parent);
	//node->setSceneManager(mgr);
	node->setID(id);
	node->setPosition(position);
	node->setRotation(rotation);
	node->setScale(scale);
	return node;
}
IRRLICHT_C_API void IParticleSystemSceneNode_setParticleSize(IParticleSystemSceneNode* pointer, const core::dimension2d<f32>& size = core::dimension2d<f32>(5.0f, 5.0f))
{pointer->setParticleSize(size);}
IRRLICHT_C_API void IParticleSystemSceneNode_setParticlesAreGlobal(IParticleSystemSceneNode* pointer, bool global = true)
{pointer->setParticlesAreGlobal(global);}
IRRLICHT_C_API IParticleEmitter* IParticleSystemSceneNode_getEmitter(IParticleSystemSceneNode* pointer)
{return pointer->getEmitter();}
IRRLICHT_C_API void IParticleSystemSceneNode_setEmitter(IParticleSystemSceneNode* pointer, IParticleEmitter* emitter)
{pointer->setEmitter(emitter);}
IRRLICHT_C_API void IParticleSystemSceneNode_addAffector(IParticleSystemSceneNode* pointer, IParticleAffector* affector)
{pointer->addAffector(affector);}
IRRLICHT_C_API void IParticleSystemSceneNode_removeAllAffectors(IParticleSystemSceneNode* pointer)
{pointer->removeAllAffectors();}
IRRLICHT_C_API IParticleAnimatedMeshSceneNodeEmitter* IParticleSystemSceneNode_createAnimatedMeshSceneNodeEmitter(IParticleSystemSceneNode* pointer, scene::IAnimatedMeshSceneNode* node, bool useNormalDirection = true, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), f32 normalDirectionModifier = 100.0f, s32 mbNumber = -1, bool everyMeshVertex = false, u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createAnimatedMeshSceneNodeEmitter(node, useNormalDirection, direction, normalDirectionModifier, mbNumber, everyMeshVertex, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleBoxEmitter* IParticleSystemSceneNode_createBoxEmitter(IParticleSystemSceneNode* pointer, const core::aabbox3df& box = core::aabbox3df(-10,28,-10,10,30,10), const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createBoxEmitter(box, direction, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleCylinderEmitter* IParticleSystemSceneNode_createCylinderEmitter(IParticleSystemSceneNode* pointer, const core::vector3df& center, f32 radius, const core::vector3df& normal, f32 length, bool outlineOnly = false, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createCylinderEmitter(center, radius, normal, length, outlineOnly, direction, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleMeshEmitter* IParticleSystemSceneNode_createMeshEmitter(IParticleSystemSceneNode* pointer, scene::IMesh* mesh, bool useNormalDirection = true, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), f32 normalDirectionModifier = 100.0f, s32 mbNumber = -1, bool everyMeshVertex = false, u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createMeshEmitter(mesh, useNormalDirection, direction, normalDirectionModifier, mbNumber, everyMeshVertex, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticlePointEmitter* IParticleSystemSceneNode_createPointEmitter(IParticleSystemSceneNode* pointer, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createPointEmitter(direction, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleRingEmitter* IParticleSystemSceneNode_createRingEmitter(IParticleSystemSceneNode* pointer, const core::vector3df& center, f32 radius, f32 ringThickness, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createRingEmitter(center, radius, ringThickness, direction, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleSphereEmitter* IParticleSystemSceneNode_createSphereEmitter(IParticleSystemSceneNode* pointer, const core::vector3df& center, f32 radius, const core::vector3df& direction = core::vector3df(0.0f,0.03f,0.0f), u32 minParticlesPerSecond = 5, u32 maxParticlesPerSecond = 10, const video::SColor& minStartColor = video::SColor(255,0,0,0), const video::SColor& maxStartColor = video::SColor(255,255,255,255), u32 lifeTimeMin = 2000, u32 lifeTimeMax = 4000, s32 maxAngleDegrees = 0, const core::dimension2df& minStartSize = core::dimension2df(5.0f,5.0f), const core::dimension2df& maxStartSize = core::dimension2df(5.0f,5.0f))
{return pointer->createSphereEmitter(center, radius, direction, minParticlesPerSecond, maxParticlesPerSecond, minStartColor, maxStartColor, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize, maxStartSize);}
IRRLICHT_C_API IParticleAttractionAffector* IParticleSystemSceneNode_createAttractionAffector(IParticleSystemSceneNode* pointer, const core::vector3df* point, f32 speed = 1.0f, bool attract = true, bool affectX = true, bool affectY = true, bool affectZ = true)
{return pointer->createAttractionAffector(*point, speed, attract, affectX, affectY, affectZ);}
IRRLICHT_C_API IParticleAffector* IParticleSystemSceneNode_createScaleParticleAffector(IParticleSystemSceneNode* pointer, const core::dimension2df& scaleTo = core::dimension2df(1.0f, 1.0f))
{return pointer->createScaleParticleAffector(scaleTo);}
IRRLICHT_C_API IParticleFadeOutAffector* IParticleSystemSceneNode_createFadeOutParticleAffector(IParticleSystemSceneNode* pointer, const video::SColor& targetColor = video::SColor(0,0,0,0), u32 timeNeededToFadeOut = 1000)
{return pointer->createFadeOutParticleAffector(targetColor, timeNeededToFadeOut);}
IRRLICHT_C_API IParticleGravityAffector* IParticleSystemSceneNode_createGravityAffector(IParticleSystemSceneNode* pointer, const core::vector3df& gravity = core::vector3df(0.0f,-0.03f,0.0f), u32 timeForceLost = 1000)
{return pointer->createGravityAffector(gravity, timeForceLost);}
IRRLICHT_C_API IParticleRotationAffector* IParticleSystemSceneNode_createRotationAffector(IParticleSystemSceneNode* pointer, const core::vector3df& speed = core::vector3df(5.0f,5.0f,5.0f), const core::vector3df& pivotPoint = core::vector3df(0.0f,0.0f,0.0f))
{return pointer->createRotationAffector(speed, pivotPoint);}

#ifdef __cplusplus
}
#endif

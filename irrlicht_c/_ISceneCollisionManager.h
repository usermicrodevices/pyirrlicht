// Copyright(c) Max Kolosov 2010-2012 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API ISceneCollisionManager* ISceneCollisionManager_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0)){return new ISceneCollisionManager(parent, mgr, id, position);}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API bool ISceneCollisionManager_getCollisionPoint(ISceneCollisionManager* pointer, const core::line3d<f32>& ray, ITriangleSelector* selector, core::vector3df& outCollisionPoint, core::triangle3df& outTriangle, const ISceneNode*& outNode)
#else
IRRLICHT_C_API bool ISceneCollisionManager_getCollisionPoint(ISceneCollisionManager* pointer, const core::line3d<f32>& ray, ITriangleSelector* selector, core::vector3df& outCollisionPoint, core::triangle3df& outTriangle, ISceneNode*& outNode)
#endif
{return pointer->getCollisionPoint(ray, selector, outCollisionPoint, outTriangle, outNode);}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API core::vector3df* ISceneCollisionManager_getCollisionResultPosition(ISceneCollisionManager* pointer, ITriangleSelector* selector, const core::vector3df& ellipsoidPosition, const core::vector3df& ellipsoidRadius, const core::vector3df& ellipsoidDirectionAndSpeed, core::triangle3df& triout, core::vector3df& hitPosition, bool& outFalling, const ISceneNode*& outNode, f32 slidingSpeed = 0.0005f, const core::vector3df& gravityDirectionAndSpeed = core::vector3df(0.0f, 0.0f, 0.0f))
#else
IRRLICHT_C_API core::vector3df* ISceneCollisionManager_getCollisionResultPosition(ISceneCollisionManager* pointer, ITriangleSelector* selector, const core::vector3df& ellipsoidPosition, const core::vector3df& ellipsoidRadius, const core::vector3df& ellipsoidDirectionAndSpeed, core::triangle3df& triout, core::vector3df& hitPosition, bool& outFalling, ISceneNode*& outNode, f32 slidingSpeed = 0.0005f, const core::vector3df& gravityDirectionAndSpeed = core::vector3df(0.0f, 0.0f, 0.0f))
#endif
{return new core::vector3df(pointer->getCollisionResultPosition(selector, ellipsoidPosition, ellipsoidRadius, ellipsoidDirectionAndSpeed, triout, hitPosition, outFalling, outNode, slidingSpeed, gravityDirectionAndSpeed));}

IRRLICHT_C_API core::line3d<f32>* ISceneCollisionManager_getRayFromScreenCoordinates(ISceneCollisionManager* pointer, const core::position2d<s32>* pos, ICameraSceneNode* camera = 0)
{return new core::line3d<f32>(pointer->getRayFromScreenCoordinates(*pos, camera));}
IRRLICHT_C_API core::position2d<s32>* ISceneCollisionManager_getScreenCoordinatesFrom3DPosition(ISceneCollisionManager* pointer, const core::vector3df* pos, ICameraSceneNode* camera=0)
{return new core::position2d<s32>(pointer->getScreenCoordinatesFrom3DPosition(*pos, camera));}
IRRLICHT_C_API ISceneNode* ISceneCollisionManager_getSceneNodeFromScreenCoordinatesBB(ISceneCollisionManager* pointer, const core::position2d<s32>* pos, s32 idBitMask=0, bool bNoDebugObjects=false, ISceneNode* root=0)
{return pointer->getSceneNodeFromScreenCoordinatesBB(*pos, idBitMask, bNoDebugObjects, root);}
IRRLICHT_C_API ISceneNode* ISceneCollisionManager_getSceneNodeFromRayBB(ISceneCollisionManager* pointer, const core::line3d<f32>* ray, s32 idBitMask=0, bool bNoDebugObjects=false, ISceneNode* root=0)
{return pointer->getSceneNodeFromRayBB(*ray, idBitMask, bNoDebugObjects, root);}
IRRLICHT_C_API ISceneNode* ISceneCollisionManager_getSceneNodeFromCameraBB(ISceneCollisionManager* pointer, ICameraSceneNode* camera, s32 idBitMask=0, bool bNoDebugObjects = false)
{return pointer->getSceneNodeFromCameraBB(camera, idBitMask, bNoDebugObjects);}
IRRLICHT_C_API ISceneNode* ISceneCollisionManager_getSceneNodeAndCollisionPointFromRay(ISceneCollisionManager* pointer, const core::line3d<f32>* ray, core::vector3df* outCollisionPoint, core::triangle3df* outTriangle, s32 idBitMask = 0, ISceneNode* collisionRootNode = 0, bool noDebugObjects = false)
{return pointer->getSceneNodeAndCollisionPointFromRay(*ray, *outCollisionPoint, *outTriangle, idBitMask, collisionRootNode, noDebugObjects);}

#ifdef __cplusplus
}
#endif

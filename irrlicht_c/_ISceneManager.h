// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ISceneManager
IRRLICHT_C_API IAnimatedMesh* ISceneManager_getMesh(ISceneManager* pointer, const fschar_t* filename)
{return pointer->getMesh(filename);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_getMesh2(ISceneManager* pointer, io::IReadFile* file)
{return pointer->getMesh(file);}
IRRLICHT_C_API IMeshCache* ISceneManager_getMeshCache(ISceneManager* pointer)
{return pointer->getMeshCache();}
IRRLICHT_C_API video::IVideoDriver* ISceneManager_getVideoDriver(ISceneManager* pointer)
{return pointer->getVideoDriver();}
IRRLICHT_C_API gui::IGUIEnvironment* ISceneManager_getGUIEnvironment(ISceneManager* pointer)
{return pointer->getGUIEnvironment();}
IRRLICHT_C_API io::IFileSystem* ISceneManager_getFileSystem(ISceneManager* pointer)
{return pointer->getFileSystem();}
IRRLICHT_C_API IVolumeLightSceneNode* ISceneManager_addVolumeLightSceneNode(ISceneManager* pointer, ISceneNode* parent=0, s32 id=-1, const u32 subdivU = 32, const u32 subdivV = 32, const SColor& foot = SColor(51, 0, 230, 180), const SColor& tail = SColor(0, 0, 0, 0), const vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = core::vector3df(0,0,0), const core::vector3df& scale = core::vector3df(1.0f, 1.0f, 1.0f))
{return pointer->addVolumeLightSceneNode(parent, id, subdivU, subdivV, foot, tail, position, rotation, scale);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addCubeSceneNode(ISceneManager* pointer, f32 size=10.0f, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = core::vector3df(0,0,0), const core::vector3df& scale = vector3df(1.0f, 1.0f, 1.0f))
{return pointer->addCubeSceneNode(size, parent, id, position, rotation, scale);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addSphereSceneNode(ISceneManager* pointer, f32 radius=5.0f, s32 polyCount=16, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const vector3df& rotation = vector3df(0,0,0), const vector3df& scale = vector3df(1.0f, 1.0f, 1.0f))
{return pointer->addSphereSceneNode(radius, polyCount, parent, id, position, rotation, scale);}
IRRLICHT_C_API IAnimatedMeshSceneNode* ISceneManager_addAnimatedMeshSceneNode(ISceneManager* pointer, IAnimatedMesh* mesh, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const vector3df& rotation = vector3df(0,0,0), const vector3df& scale = vector3df(1.0f, 1.0f, 1.0f), bool alsoAddIfMeshPointerZero=false)
{return pointer->addAnimatedMeshSceneNode(mesh, parent, id, position, rotation, scale, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API IAnimatedMeshSceneNode* ISceneManager_addAnimatedMeshSceneNode2(ISceneManager* pointer, IAnimatedMesh* mesh)
{return pointer->addAnimatedMeshSceneNode(mesh);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addMeshSceneNode(ISceneManager* pointer, IMesh* mesh, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = vector3df(0,0,0), const core::vector3df& scale = core::vector3df(1.0f, 1.0f, 1.0f), bool alsoAddIfMeshPointerZero=false)
{return pointer->addMeshSceneNode(mesh, parent, id, position, rotation, scale, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API ISceneNode* ISceneManager_addWaterSurfaceSceneNode(ISceneManager* pointer, IMesh* mesh, f32 waveHeight=2.0f, f32 waveSpeed=300.0f, f32 waveLength=10.0f, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = core::vector3df(0,0,0), const core::vector3df& scale = core::vector3df(1.0f, 1.0f, 1.0f))
{return pointer->addWaterSurfaceSceneNode(mesh, waveHeight, waveSpeed, waveLength, parent, id, position, rotation, scale);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addOctTreeSceneNode(ISceneManager* pointer, IAnimatedMesh* mesh, ISceneNode* parent=0, s32 id=-1, s32 minimalPolysPerNode=512, bool alsoAddIfMeshPointerZero=false)
{return pointer->addOctTreeSceneNode(mesh, parent, id, minimalPolysPerNode, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addOctTreeSceneNode2(ISceneManager* pointer, IMesh* mesh, ISceneNode* parent=0, s32 id=-1, s32 minimalPolysPerNode=256, bool alsoAddIfMeshPointerZero=false)
{return pointer->addOctTreeSceneNode(mesh, parent, id, minimalPolysPerNode, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addOctreeSceneNode(ISceneManager* pointer, IAnimatedMesh* mesh, ISceneNode* parent=0, s32 id=-1, s32 minimalPolysPerNode=512, bool alsoAddIfMeshPointerZero=false)
{return pointer->addOctreeSceneNode(mesh, parent, id, minimalPolysPerNode, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addOctreeSceneNode2(ISceneManager* pointer, IMesh* mesh, ISceneNode* parent=0, s32 id=-1, s32 minimalPolysPerNode=256, bool alsoAddIfMeshPointerZero=false)
{return pointer->addOctreeSceneNode(mesh, parent, id, minimalPolysPerNode, alsoAddIfMeshPointerZero);}
IRRLICHT_C_API ICameraSceneNode* ISceneManager_addCameraSceneNode(ISceneManager* pointer, ISceneNode* parent = 0, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& lookat = core::vector3df(0,0,100), s32 id=-1)
{return pointer->addCameraSceneNode(parent, position, lookat, id);}
IRRLICHT_C_API ICameraSceneNode* ISceneManager_addCameraSceneNodeMaya(ISceneManager* pointer, ISceneNode* parent = 0, f32 rotateSpeed = -1500.0f, f32 zoomSpeed = 200.0f, f32 translationSpeed = 1500.0f, s32 id=-1)
{return pointer->addCameraSceneNodeMaya(parent, rotateSpeed, zoomSpeed, translationSpeed, id);}
IRRLICHT_C_API ICameraSceneNode* ISceneManager_addCameraSceneNodeFPS(ISceneManager* pointer, ISceneNode* parent = 0, f32 rotateSpeed = 100.0f, f32 moveSpeed = 0.5f, s32 id=-1, SKeyMap* keyMapArray=0, s32 keyMapSize=0, bool noVerticalMovement=false, f32 jumpSpeed = 0.f, bool invertMouse=false)
{return pointer->addCameraSceneNodeFPS(parent, rotateSpeed, moveSpeed, id, keyMapArray, keyMapSize, noVerticalMovement, jumpSpeed, invertMouse);}
IRRLICHT_C_API ICameraSceneNode* ISceneManager_addCameraSceneNodeFPS2(ISceneManager* pointer)
{return pointer->addCameraSceneNodeFPS();}
IRRLICHT_C_API ILightSceneNode* ISceneManager_addLightSceneNode(ISceneManager* pointer, ISceneNode* parent = 0, const core::vector3df& position = core::vector3df(0,0,0), const video::SColorf& color = video::SColorf(1.0f, 1.0f, 1.0f), f32 radius=100.0f, s32 id=-1)
{return pointer->addLightSceneNode(parent, position, *&color, radius, id);}
IRRLICHT_C_API IBillboardSceneNode* ISceneManager_addBillboardSceneNode(ISceneManager* pointer, ISceneNode* parent = 0, const core::dimension2d<f32>& size = core::dimension2d<f32>(10.0f, 10.0f), const core::vector3df& position = vector3df(0,0,0), s32 id=-1, const SColor& colorTop = 0xFFFFFFFF, const SColor& colorBottom = 0xFFFFFFFF)
{return pointer->addBillboardSceneNode(parent, size, position, id, colorTop, colorBottom);}
IRRLICHT_C_API ISceneNode* ISceneManager_addSkyBoxSceneNode(ISceneManager* pointer, video::ITexture* top, video::ITexture* bottom, video::ITexture* left, video::ITexture* right, video::ITexture* front, video::ITexture* back, ISceneNode* parent = 0, s32 id=-1)
{return pointer->addSkyBoxSceneNode(top, bottom, left, right, front, back, parent, id);}
IRRLICHT_C_API ISceneNode* ISceneManager_addSkyDomeSceneNode(ISceneManager* pointer, video::ITexture* texture, u32 horiRes=16, u32 vertRes=8, f32 texturePercentage=0.9, f32 spherePercentage=2.0,f32 radius = 1000.f, ISceneNode* parent=0, s32 id=-1)
{return pointer->addSkyDomeSceneNode(texture, horiRes, vertRes, texturePercentage, spherePercentage, radius, parent, id);}
IRRLICHT_C_API IParticleSystemSceneNode* ISceneManager_addParticleSystemSceneNode(ISceneManager* pointer, bool withDefaultEmitter=true, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0,0,0), const core::vector3df& rotation = core::vector3df(0,0,0), const core::vector3df& scale = core::vector3df(1.0f, 1.0f, 1.0f))
{return pointer->addParticleSystemSceneNode(withDefaultEmitter, parent, id, position, rotation, scale);}
IRRLICHT_C_API ITerrainSceneNode* ISceneManager_addTerrainSceneNode(ISceneManager* pointer, const char* heightMapFileName, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0.0f,0.0f,0.0f), const core::vector3df& rotation = core::vector3df(0.0f,0.0f,0.0f), const core::vector3df& scale = core::vector3df(1.0f,1.0f,1.0f), const SColor& vertexColor = SColor(255,255,255,255), s32 maxLOD=5, E_TERRAIN_PATCH_SIZE patchSize=ETPS_17, s32 smoothFactor=0, bool addAlsoIfHeightmapEmpty = false)
{return pointer->addTerrainSceneNode(heightMapFileName, parent, id, position, rotation, scale, vertexColor, maxLOD, patchSize, smoothFactor, addAlsoIfHeightmapEmpty);}
IRRLICHT_C_API ITerrainSceneNode* ISceneManager_addTerrainSceneNode2(ISceneManager* pointer, io::IReadFile* heightMapFile, ISceneNode* parent=0, s32 id=-1, const core::vector3df& position = core::vector3df(0.0f,0.0f,0.0f), const core::vector3df& rotation = core::vector3df(0.0f,0.0f,0.0f), const core::vector3df& scale = core::vector3df(1.0f,1.0f,1.0f), const SColor& vertexColor = SColor(255,255,255,255), s32 maxLOD=5, E_TERRAIN_PATCH_SIZE patchSize=ETPS_17, s32 smoothFactor=0, bool addAlsoIfHeightmapEmpty = false)
{return pointer->addTerrainSceneNode(heightMapFile, parent, id, position, rotation, scale, vertexColor, maxLOD, patchSize, smoothFactor, addAlsoIfHeightmapEmpty);}
IRRLICHT_C_API IMeshSceneNode* ISceneManager_addQuake3SceneNode(ISceneManager* pointer, IMeshBuffer* meshBuffer, const quake3::IShader * shader, ISceneNode* parent=0, s32 id=-1)
{return pointer->addQuake3SceneNode(meshBuffer, shader, parent, id);}
IRRLICHT_C_API ISceneNode* ISceneManager_addEmptySceneNode(ISceneManager* pointer, ISceneNode* parent=0, s32 id=-1)
{return pointer->addEmptySceneNode(parent, id);}
IRRLICHT_C_API IDummyTransformationSceneNode* ISceneManager_addDummyTransformationSceneNode(ISceneManager* pointer, ISceneNode* parent=0, s32 id=-1)
{return pointer->addDummyTransformationSceneNode(parent, id);}
IRRLICHT_C_API ITextSceneNode* ISceneManager_addTextSceneNode(ISceneManager* pointer, gui::IGUIFont* font, const wchar_t* text, const SColor& color=SColor(100,255,255,255), ISceneNode* parent = 0, const core::vector3df& position = core::vector3df(0,0,0), s32 id=-1)
{return pointer->addTextSceneNode(font, text, color, parent, position, id);}
IRRLICHT_C_API IBillboardTextSceneNode* ISceneManager_addBillboardTextSceneNode(ISceneManager* pointer, gui::IGUIFont* font, const wchar_t* text, ISceneNode* parent = 0, const core::dimension2d<f32>& size = core::dimension2d<f32>(10.0f, 10.0f), const core::vector3df& position = vector3df(0,0,0), s32 id=-1, const SColor& colorTop = 0xFFFFFFFF, const SColor& colorBottom = 0xFFFFFFFF)
{return pointer->addBillboardTextSceneNode(font, text, parent, size, position, id, colorTop, colorBottom);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_addHillPlaneMesh(ISceneManager* pointer, const char* name, const core::dimension2d<f32>& tileSize, const core::dimension2d<u32>& tileCount, video::SMaterial* material = 0, f32 hillHeight = 0.0f, const core::dimension2d<f32>& countHills = dimension2d<f32>(0.0f, 0.0f), const core::dimension2d<f32>& textureRepeatCount = core::dimension2d<f32>(1.0f, 1.0f))
{return pointer->addHillPlaneMesh(name, tileSize, tileCount, material, hillHeight, countHills, textureRepeatCount);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_addTerrainMesh(ISceneManager* pointer, const char* meshname, video::IImage* texture, video::IImage* heightmap, const core::dimension2d<f32>& stretchSize = core::dimension2d<f32>(10.0f,10.0f), f32 maxHeight=200.0f, const core::dimension2d<u32>& defaultVertexBlockSize = core::dimension2d<u32>(64,64))
{return pointer->addTerrainMesh(meshname, texture, heightmap, stretchSize, maxHeight, defaultVertexBlockSize);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_addArrowMesh(ISceneManager* pointer, const char* name, const SColor& vtxColor0=0xFFFFFFFF, const SColor& vtxColor1=0xFFFFFFFF, u32 tesselationCylinder=4, u32 tesselationCone=8, f32 height=1.f, f32 cylinderHeight=0.6f, f32 width0=0.05f, f32 width1=0.3f)
{return pointer->addArrowMesh(name, vtxColor0, vtxColor1, tesselationCylinder, tesselationCone, height, cylinderHeight, width0, width1);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_addSphereMesh(ISceneManager* pointer, const char* name, f32 radius=5.f, u32 polyCountX = 16, u32 polyCountY = 16)
{return pointer->addSphereMesh(name, radius, polyCountX, polyCountY);}
IRRLICHT_C_API IAnimatedMesh* ISceneManager_addVolumeLightMesh(ISceneManager* pointer, const char* name, const u32 SubdivideU = 32, const u32 SubdivideV = 32, const SColor& FootColor = SColor(51, 0, 230, 180), const SColor& TailColor = SColor(0, 0, 0, 0))
{return pointer->addVolumeLightMesh(name, SubdivideU, SubdivideV, FootColor, TailColor);}
IRRLICHT_C_API ISceneNode* ISceneManager_getRootSceneNode(ISceneManager* pointer)
{return pointer->getRootSceneNode();}
IRRLICHT_C_API ISceneNode* ISceneManager_getSceneNodeFromId(ISceneManager* pointer, s32 id, ISceneNode* start=0)
{return pointer->getSceneNodeFromId(id, start);}
IRRLICHT_C_API ISceneNode* ISceneManager_getSceneNodeFromName(ISceneManager* pointer, const c8* name, ISceneNode* start=0)
{return pointer->getSceneNodeFromName(name, start);}
IRRLICHT_C_API ISceneNode* ISceneManager_getSceneNodeFromType(ISceneManager* pointer, scene::ESCENE_NODE_TYPE type, ISceneNode* start=0)
{return pointer->getSceneNodeFromType(type, start);}
IRRLICHT_C_API void ISceneManager_getSceneNodesFromType(ISceneManager* pointer, ESCENE_NODE_TYPE type, core::array<scene::ISceneNode*>& outNodes, ISceneNode* start=0)
{pointer->getSceneNodesFromType(type, outNodes, start);}
IRRLICHT_C_API ICameraSceneNode* ISceneManager_getActiveCamera(ISceneManager* pointer)
{return pointer->getActiveCamera();}
IRRLICHT_C_API void ISceneManager_setActiveCamera(ISceneManager* pointer, ICameraSceneNode* camera)
{pointer->setActiveCamera(camera);}
IRRLICHT_C_API void ISceneManager_setShadowColor(ISceneManager* pointer, const SColor& color = SColor(150,0,0,0))
{pointer->setShadowColor(color);}
IRRLICHT_C_API const SColor& ISceneManager_getShadowColor(ISceneManager* pointer)
{return (const SColor&)pointer->getShadowColor();}
IRRLICHT_C_API u32 ISceneManager_registerNodeForRendering(ISceneManager* pointer, ISceneNode* node, E_SCENE_NODE_RENDER_PASS pass = ESNRP_AUTOMATIC)
{return pointer->registerNodeForRendering(node, pass);}
IRRLICHT_C_API void ISceneManager_drawAll(ISceneManager* pointer)
{pointer->drawAll();}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createRotationAnimator(ISceneManager* pointer, const core::vector3df& rotationSpeed)
{return pointer->createRotationAnimator(rotationSpeed);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createFlyCircleAnimator(ISceneManager* pointer, const core::vector3df& center=core::vector3df(0.f,0.f,0.f), f32 radius=100.f, f32 speed=0.001f, const core::vector3df& direction=core::vector3df(0.f, 1.f, 0.f), f32 startPosition = 0.f, f32 radiusEllipsoid = 0.f)
{return pointer->createFlyCircleAnimator(center, radius, speed, direction, startPosition, radiusEllipsoid);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createFlyStraightAnimator(ISceneManager* pointer, const core::vector3df& startPoint, const core::vector3df& endPoint, u32 timeForWay, bool loop=false, bool pingpong = false)
{return pointer->createFlyStraightAnimator(startPoint, endPoint, timeForWay, loop, pingpong);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createTextureAnimator(ISceneManager* pointer, const core::array<video::ITexture*>* textures, s32 timePerFrame, bool loop=true)
{return pointer->createTextureAnimator(*textures, timePerFrame, loop);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createDeleteAnimator(ISceneManager* pointer, u32 timeMs)
{return pointer->createDeleteAnimator(timeMs);}
IRRLICHT_C_API ISceneNodeAnimatorCollisionResponse* ISceneManager_createCollisionResponseAnimator(ISceneManager* pointer, ITriangleSelector* world, ISceneNode* sceneNode, const core::vector3df& ellipsoidRadius = core::vector3df(30,60,30), const core::vector3df& gravityPerSecond = core::vector3df(0,-10.0f,0), const core::vector3df& ellipsoidTranslation = core::vector3df(0,0,0), f32 slidingValue = 0.0005f)
{return pointer->createCollisionResponseAnimator(world, sceneNode, ellipsoidRadius, gravityPerSecond, ellipsoidTranslation, slidingValue);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneManager_createFollowSplineAnimator(ISceneManager* pointer, s32 startTime, const core::array< core::vector3df >& points, f32 speed = 1.0f, f32 tightness = 0.5f)
{return pointer->createFollowSplineAnimator(startTime, points, speed, tightness);}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createTriangleSelector1(ISceneManager* pointer, IMesh* mesh, ISceneNode* node)
{return pointer->createTriangleSelector(mesh, node);}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createTriangleSelector2(ISceneManager* pointer, IAnimatedMeshSceneNode* node)
{return pointer->createTriangleSelector(node);}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createTriangleSelectorFromBoundingBox(ISceneManager* pointer, ISceneNode* node)
{return pointer->createTriangleSelectorFromBoundingBox(node);}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createOctTreeTriangleSelector(ISceneManager* pointer, IMesh* mesh, ISceneNode* node, s32 minimalPolysPerNode=32)
{return pointer->createOctTreeTriangleSelector(mesh, node, minimalPolysPerNode);}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createOctreeTriangleSelector(ISceneManager* pointer, IMesh* mesh, ISceneNode* node, s32 minimalPolysPerNode=32)
{return pointer->createOctreeTriangleSelector(mesh, node, minimalPolysPerNode);}
IRRLICHT_C_API IMetaTriangleSelector* ISceneManager_createMetaTriangleSelector(ISceneManager* pointer)
{return pointer->createMetaTriangleSelector();}
IRRLICHT_C_API ITriangleSelector* ISceneManager_createTerrainTriangleSelector(ISceneManager* pointer, ITerrainSceneNode* node, s32 LOD=0)
{return pointer->createTerrainTriangleSelector(node, LOD);}
IRRLICHT_C_API void ISceneManager_addExternalMeshLoader(ISceneManager* pointer, IMeshLoader* externalLoader)
{pointer->addExternalMeshLoader(externalLoader);}
IRRLICHT_C_API ISceneCollisionManager* ISceneManager_getSceneCollisionManager(ISceneManager* pointer)
{return pointer->getSceneCollisionManager();}
IRRLICHT_C_API IMeshManipulator* ISceneManager_getMeshManipulator(ISceneManager* pointer)
{return pointer->getMeshManipulator();}
IRRLICHT_C_API void ISceneManager_addToDeletionQueue(ISceneManager* pointer, ISceneNode* node)
{pointer->addToDeletionQueue(node);}
IRRLICHT_C_API bool ISceneManager_postEventFromUser(ISceneManager* pointer, const SEvent& event)
{return pointer->postEventFromUser(event);}
IRRLICHT_C_API void ISceneManager_clear(ISceneManager* pointer)
{pointer->clear();}
IRRLICHT_C_API io::IAttributes* ISceneManager_getParameters(ISceneManager* pointer)
{return pointer->getParameters();}
IRRLICHT_C_API E_SCENE_NODE_RENDER_PASS ISceneManager_getSceneNodeRenderPass(ISceneManager* pointer)
{return pointer->getSceneNodeRenderPass();}
IRRLICHT_C_API ISceneNodeFactory* ISceneManager_getDefaultSceneNodeFactory(ISceneManager* pointer)
{return pointer->getDefaultSceneNodeFactory();}
IRRLICHT_C_API void ISceneManager_registerSceneNodeFactory(ISceneManager* pointer, ISceneNodeFactory* factoryToAdd)
{pointer->registerSceneNodeFactory(factoryToAdd);}
IRRLICHT_C_API u32 ISceneManager_getRegisteredSceneNodeFactoryCount(ISceneManager* pointer)
{return pointer->getRegisteredSceneNodeFactoryCount();}
IRRLICHT_C_API ISceneNodeFactory* ISceneManager_getSceneNodeFactory(ISceneManager* pointer, u32 index)
{return pointer->getSceneNodeFactory(index);}
IRRLICHT_C_API ISceneNodeAnimatorFactory* ISceneManager_getDefaultSceneNodeAnimatorFactory(ISceneManager* pointer)
{return pointer->getDefaultSceneNodeAnimatorFactory();}
IRRLICHT_C_API void ISceneManager_registerSceneNodeAnimatorFactory(ISceneManager* pointer, ISceneNodeAnimatorFactory* factoryToAdd)
{pointer->registerSceneNodeAnimatorFactory(factoryToAdd);}
IRRLICHT_C_API u32 ISceneManager_getRegisteredSceneNodeAnimatorFactoryCount(ISceneManager* pointer)
{return pointer->getRegisteredSceneNodeAnimatorFactoryCount();}
IRRLICHT_C_API ISceneNodeAnimatorFactory* ISceneManager_getSceneNodeAnimatorFactory(ISceneManager* pointer, u32 index)
{return pointer->getSceneNodeAnimatorFactory(index);}
IRRLICHT_C_API const c8* ISceneManager_getSceneNodeTypeName(ISceneManager* pointer, ESCENE_NODE_TYPE type)
{return pointer->getSceneNodeTypeName(type);}
IRRLICHT_C_API const c8* ISceneManager_getAnimatorTypeName(ISceneManager* pointer, ESCENE_NODE_ANIMATOR_TYPE type)
{return pointer->getAnimatorTypeName(type);}
IRRLICHT_C_API ISceneNode* ISceneManager_addSceneNode(ISceneManager* pointer, const char* sceneNodeTypeName, ISceneNode* parent=0)
{return pointer->addSceneNode(sceneNodeTypeName, parent);}
IRRLICHT_C_API ISceneManager* ISceneManager_createNewSceneManager(ISceneManager* pointer, bool cloneContent=false)
{return pointer->createNewSceneManager(cloneContent);}
IRRLICHT_C_API bool ISceneManager_saveScene(ISceneManager* pointer, const char* filename, ISceneUserDataSerializer* userDataSerializer=0)
{return pointer->saveScene(filename, userDataSerializer);}
IRRLICHT_C_API bool ISceneManager_saveScene2(ISceneManager* pointer, io::IWriteFile* file, ISceneUserDataSerializer* userDataSerializer=0)
{return pointer->saveScene(file, userDataSerializer);}
IRRLICHT_C_API bool ISceneManager_loadScene(ISceneManager* pointer, const char* filename, ISceneUserDataSerializer* userDataSerializer=0)
{return pointer->loadScene(filename, userDataSerializer);}
IRRLICHT_C_API bool ISceneManager_loadScene2(ISceneManager* pointer, io::IReadFile* file, ISceneUserDataSerializer* userDataSerializer=0)
{return pointer->loadScene(file, userDataSerializer);}
IRRLICHT_C_API IMeshWriter* ISceneManager_createMeshWriter(ISceneManager* pointer, EMESH_WRITER_TYPE type)
{return pointer->createMeshWriter(type);}
IRRLICHT_C_API ISkinnedMesh* ISceneManager_createSkinnedMesh(ISceneManager* pointer)
{return pointer->createSkinnedMesh();}
IRRLICHT_C_API void ISceneManager_setAmbientLight(ISceneManager* pointer, const video::SColorf &ambientColor)
{pointer->setAmbientLight(ambientColor);}
IRRLICHT_C_API const video::SColorf& ISceneManager_getAmbientLight(ISceneManager* pointer)
{return pointer->getAmbientLight();}
IRRLICHT_C_API void ISceneManager_setLightManager(ISceneManager* pointer, ILightManager* lightManager)
{pointer->setLightManager(lightManager);}
IRRLICHT_C_API const IGeometryCreator* ISceneManager_getGeometryCreator(ISceneManager* pointer)
{return pointer->getGeometryCreator();}
IRRLICHT_C_API bool ISceneManager_isCulled(ISceneManager* pointer, const ISceneNode* node)
{return pointer->isCulled(node);}

#ifdef __cplusplus
}
#endif

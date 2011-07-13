// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license


class CustomSceneNode : public scene::ISceneNode
{
public:
	CustomSceneNode(ISceneNode* parent = 0, ISceneManager* mgr = 0, s32 id = -1) : scene::ISceneNode(parent, mgr, id)
	{
	}
	void OnRegisterSceneNode()
	{
		func_OnRegisterSceneNode();
	}
	void render()
	{
		func_render();
	}
	const core::aabbox3d<f32>& getBoundingBox() const
	{
		return *func_getBoundingBox();
	}
	video::SMaterial& getMaterial(u32 num)
	{
		return *func_getMaterial(num);
	}
	const u32 getMaterialCount()
	{
		return func_getMaterialCount();
	}
	void set_func_OnRegisterSceneNode(void(IRRCALLCONV *func)())
	{
		func_OnRegisterSceneNode = func;
	}
	void set_func_render(void(IRRCALLCONV *func)())
	{
		func_render = func;
	}
	void set_func_getBoundingBox(const core::aabbox3d<f32>*(IRRCALLCONV *func)())
	{
		func_getBoundingBox = func;
	}
	void set_func_getMaterial(video::SMaterial* (IRRCALLCONV *func)(u32))
	{
		func_getMaterial = func;
	}
	void set_func_getMaterialCount(const u32 (IRRCALLCONV *func)())
	{
		func_getMaterialCount = func;
	}
	//void set_BoundingBox(core::aabbox3d<f32>* value){Box = *value;}
	//void set_Vertices(video::S3DVertex* value){Vertices = *value;}
	//void set_Material(video::SMaterial* value){Material = *value;}
private:
	void(IRRCALLCONV *func_OnRegisterSceneNode)();
	void(IRRCALLCONV *func_render)();
	const core::aabbox3d<f32>*(IRRCALLCONV *func_getBoundingBox)();
	video::SMaterial* (IRRCALLCONV *func_getMaterial)(u32);
	const u32 (IRRCALLCONV *func_getMaterialCount)();

	//core::aabbox3d<f32> Box;
	//video::S3DVertex Vertices;
	//video::SMaterial Material;
};

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_CUBE = ESNT_CUBE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_SPHERE = ESNT_SPHERE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_TEXT = ESNT_TEXT;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_WATER_SURFACE = ESNT_WATER_SURFACE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_TERRAIN = ESNT_TERRAIN;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_SKY_BOX = ESNT_SKY_BOX;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_SKY_DOME = ESNT_SKY_DOME;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_SHADOW_VOLUME = ESNT_SHADOW_VOLUME;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_OCTREE = ESNT_OCTREE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_MESH = ESNT_MESH;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_LIGHT = ESNT_LIGHT;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_EMPTY = ESNT_EMPTY;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_DUMMY_TRANSFORMATION = ESNT_DUMMY_TRANSFORMATION;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_CAMERA = ESNT_CAMERA;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_BILLBOARD = ESNT_BILLBOARD;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_ANIMATED_MESH = ESNT_ANIMATED_MESH;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_PARTICLE_SYSTEM = ESNT_PARTICLE_SYSTEM;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_Q3SHADER_SCENE_NODE = ESNT_Q3SHADER_SCENE_NODE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_MD3_SCENE_NODE = ESNT_MD3_SCENE_NODE;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_VOLUME_LIGHT = ESNT_VOLUME_LIGHT;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_CAMERA_MAYA = ESNT_CAMERA_MAYA;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_CAMERA_FPS = ESNT_CAMERA_FPS;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_UNKNOWN = ESNT_UNKNOWN;
IRRLICHT_C_API ESCENE_NODE_TYPE _ESNT_ANY = ESNT_ANY;

//================= list<ISceneNodeAnimator*> (ISceneNodeAnimatorList)
class ISceneNodeAnimatorListExt
{
public:
	ISceneNodeAnimatorListExt(const list<ISceneNodeAnimator*>& other)
	{
		IList = new list<ISceneNodeAnimator*>(other);
		iteration = 0;
	};
	const list<ISceneNodeAnimator*>* get_list(){return IList;};
	ISceneNodeAnimator* current(){return (*it);};
	ISceneNodeAnimator* next(bool from_first = false)
	{
		if(IList->empty())
		{
			iteration = 0;
			return 0;
		}
		if(from_first || iteration == 0)
		{
			iteration = 1;
			it = IList->begin();
			return (*it);
		}
		if(++it == IList->end() && ++iteration >= IList->size())
		{
			iteration = 0;
			return 0;
		}
		else
			return (*it);
	};
	ISceneNodeAnimator* get_item(u32 index = 0)
	{
		if (index == 0)
			return *(IList->begin());
		else if (index >= 0 && index < IList->size())
		{
			list<ISceneNodeAnimator*>::ConstIterator it = IList->begin();
			for (u32 i = 0; it != IList->end(); ++it, ++i)
			{
				if (i == index)
					return (*it);
			}
		}
		else
			printf("ERROR: ISceneNodeAnimatorList get_item method invalid index %d\n", index);
		return 0;
	}
	~ISceneNodeAnimatorListExt(){delete IList;};
private:
	const list<ISceneNodeAnimator*>* IList;
	list<ISceneNodeAnimator*>::ConstIterator it;
	u32 iteration;
};
IRRLICHT_C_API u32 ISceneNodeAnimatorList_size(ISceneNodeAnimatorListExt* pointer){return pointer->get_list()->size();}
IRRLICHT_C_API void ISceneNodeAnimatorList_clear(ISceneNodeAnimatorListExt* pointer){const_cast<list<ISceneNodeAnimator*>*>(pointer->get_list())->clear();}
IRRLICHT_C_API bool ISceneNodeAnimatorList_empty(ISceneNodeAnimatorListExt* pointer){return pointer->get_list()->empty();}
IRRLICHT_C_API void ISceneNodeAnimatorList_push_back(ISceneNodeAnimatorListExt* pointer, ISceneNodeAnimator* element){const_cast<list<ISceneNodeAnimator*>*>(pointer->get_list())->push_back(element);}
IRRLICHT_C_API void ISceneNodeAnimatorList_push_front(ISceneNodeAnimatorListExt* pointer, ISceneNodeAnimator* element){const_cast<list<ISceneNodeAnimator*>*>(pointer->get_list())->push_front(element);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorList_first(ISceneNodeAnimatorListExt* pointer){return *pointer->get_list()->begin();}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorList_current(ISceneNodeAnimatorListExt* pointer){return pointer->current();}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorList_next(ISceneNodeAnimatorListExt* pointer, bool from_first = false){return pointer->next(from_first);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorList_last(ISceneNodeAnimatorListExt* pointer){return *pointer->get_list()->getLast();}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorList_get_item(ISceneNodeAnimatorListExt* pointer, u32 index){return pointer->get_item(index);}

//================= list<ISceneNode*> (ISceneNodeList)
class ISceneNodeListExt
{
public:
	ISceneNodeListExt(const list<ISceneNode*>* other)
	{
		IList = new list<ISceneNode*>(*other);
		iteration = 0;
	};
	const list<ISceneNode*>* get_list(){return IList;};
	ISceneNode* current(){return (*it);};
	ISceneNode* next(bool from_first = false)
	{
		if(IList->empty())
		{
			iteration = 0;
			return 0;
		}
		if(from_first || iteration == 0)
		{
			//printf("=== from_first %d | iteration %d | IList size %d\n", from_first, iteration, IList->size());
			iteration = 1;
			it = IList->begin();
			//printf("=== item %d | iteration %d\n", it, iteration);
			return (*it);
		}
		if(++it == IList->end() && iteration >= IList->size())
		{
			iteration = 0;
			return 0;
		}
		else
		{
			++iteration;
			//printf("=== item %d | iteration %d\n", it, iteration);
			return (*it);
		}
	};
	ISceneNode* get_item(u32 index = 0)
	{
		if (index == 0)
			return *(IList->begin());
		else if (index >= 0 && index < IList->size())
		{
			list<ISceneNode*>::ConstIterator it = IList->begin();
			for (u32 i = 0; it != IList->end(); ++it, ++i)
			{
				if (i == index)
					return (*it);
			}
		}
		else
			printf("ERROR: ISceneNodeList get_item method invalid index %d\n", index);
		return 0;
	}
	~ISceneNodeListExt(){delete IList;};
private:
	const list<ISceneNode*>* IList;
	list<ISceneNode*>::ConstIterator it;
	u32 iteration;
};
IRRLICHT_C_API ISceneNodeListExt* ISceneNodeList_ctor(const list<ISceneNode*>* pointer){return new ISceneNodeListExt(pointer);}
IRRLICHT_C_API u32 ISceneNodeList_size(ISceneNodeListExt* pointer){return pointer->get_list()->size();}
IRRLICHT_C_API void ISceneNodeList_clear(ISceneNodeListExt* pointer){const_cast<list<ISceneNode*>*>(pointer->get_list())->clear();}
IRRLICHT_C_API bool ISceneNodeList_empty(ISceneNodeListExt* pointer){return pointer->get_list()->empty();}
IRRLICHT_C_API void ISceneNodeList_push_back(ISceneNodeListExt* pointer, ISceneNode* element){const_cast<list<ISceneNode*>*>(pointer->get_list())->push_back(element);}
IRRLICHT_C_API void ISceneNodeList_push_front(ISceneNodeListExt* pointer, ISceneNode* element){const_cast<list<ISceneNode*>*>(pointer->get_list())->push_front(element);}
IRRLICHT_C_API ISceneNode* ISceneNodeList_first(ISceneNodeListExt* pointer){return *pointer->get_list()->begin();}
IRRLICHT_C_API ISceneNode* ISceneNodeList_current(ISceneNodeListExt* pointer){return pointer->current();}
IRRLICHT_C_API ISceneNode* ISceneNodeList_next(ISceneNodeListExt* pointer, bool from_first = false){return pointer->next();}
IRRLICHT_C_API ISceneNode* ISceneNodeList_last(ISceneNodeListExt* pointer){return *pointer->get_list()->getLast();}
IRRLICHT_C_API ISceneNode* ISceneNodeList_get_item(ISceneNodeListExt* pointer, u32 index = 0){return pointer->get_item(index);}

//================= ISceneNode
IRRLICHT_C_API ISceneNode* ISceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id=-1, const vector3df& position = vector3df(0,0,0), const vector3df& rotation = vector3df(0,0,0), const vector3df& scale = vector3df(1.0f, 1.0f, 1.0f))
{
	ISceneNode* node = 0;
	node->setParent(parent);
	//node->setSceneManager(mgr);
	node->setID(id);
	node->setPosition(position);
	node->setRotation(rotation);
	node->setScale(scale);
	return node;
}
//{return new ISceneNode(parent, mgr, id, position, rotation, scale);}
//IRRLICHT_C_API void ISceneNode_Destructor(ISceneNode* pointer){delete pointer;}
IRRLICHT_C_API void ISceneNode_OnRegisterSceneNode(ISceneNode* pointer){pointer->OnRegisterSceneNode();}
IRRLICHT_C_API void ISceneNode_OnAnimate(ISceneNode* pointer, u32 timeMs){pointer->OnAnimate(timeMs);}
IRRLICHT_C_API void ISceneNode_render(ISceneNode* pointer, void(IRRCALLCONV *func)())
//{&reinterpret_cast<void>(pointer->render) = func;}
{pointer->render();}
//{size_t* vptr =  *(size_t**)pointer; vptr[4] = (size_t)*func;}
IRRLICHT_C_API const c8* ISceneNode_getName(ISceneNode* pointer){return pointer->getName();}
IRRLICHT_C_API void ISceneNode_setName(ISceneNode* pointer, const c8* name){pointer->setName(name);}
IRRLICHT_C_API const aabbox3d<f32>* ISceneNode_getBoundingBox(ISceneNode* pointer){return &pointer->getBoundingBox();}
IRRLICHT_C_API const aabbox3d<f32>* ISceneNode_getTransformedBoundingBox(ISceneNode* pointer){return &pointer->getTransformedBoundingBox();}
IRRLICHT_C_API const matrix4* ISceneNode_getAbsoluteTransformation(ISceneNode* pointer){return &pointer->getAbsoluteTransformation();}
IRRLICHT_C_API matrix4* ISceneNode_getRelativeTransformation(ISceneNode* pointer){return &pointer->getRelativeTransformation();}
IRRLICHT_C_API bool ISceneNode_isVisible(ISceneNode* pointer){return pointer->isVisible();}
IRRLICHT_C_API bool ISceneNode_isTrulyVisible(ISceneNode* pointer){return pointer->isTrulyVisible();}
IRRLICHT_C_API void ISceneNode_setVisible(ISceneNode* pointer, bool isVisible){pointer->setVisible(isVisible);}
IRRLICHT_C_API s32 ISceneNode_getID(ISceneNode* pointer){return pointer->getID();}
IRRLICHT_C_API void ISceneNode_setID(ISceneNode* pointer, s32 id){pointer->setID(id);}
IRRLICHT_C_API void ISceneNode_addChild(ISceneNode* pointer, ISceneNode* child){pointer->addChild(child);}
IRRLICHT_C_API bool ISceneNode_removeChild(ISceneNode* pointer, ISceneNode* child){return pointer->removeChild(child);}
IRRLICHT_C_API void ISceneNode_removeAll(ISceneNode* pointer){pointer->removeAll();}
IRRLICHT_C_API void ISceneNode_remove(ISceneNode* pointer){pointer->remove();}
IRRLICHT_C_API void ISceneNode_addAnimator(ISceneNode* pointer, ISceneNodeAnimator* animator){pointer->addAnimator(animator);}
//IRRLICHT_C_API const list<ISceneNodeAnimator*>* ISceneNode_getAnimators(ISceneNode* pointer){return &pointer->getAnimators();}
IRRLICHT_C_API ISceneNodeAnimatorListExt* ISceneNode_getAnimators(ISceneNode* pointer){return new ISceneNodeAnimatorListExt(pointer->getAnimators());}
IRRLICHT_C_API void ISceneNode_removeAnimator(ISceneNode* pointer, ISceneNodeAnimator* animator){pointer->removeAnimator(animator);}
IRRLICHT_C_API void ISceneNode_removeAnimators(ISceneNode* pointer){pointer->removeAnimators();}
IRRLICHT_C_API SMaterial* ISceneNode_getMaterial(ISceneNode* pointer, u32 num){return &pointer->getMaterial(num);}
IRRLICHT_C_API void ISceneNode_setMaterial(ISceneNode* pointer, SMaterial* material, u32 num = 0){pointer->getMaterial(num) = *material;}
IRRLICHT_C_API u32 ISceneNode_getMaterialCount(ISceneNode* pointer){return pointer->getMaterialCount();}
IRRLICHT_C_API void ISceneNode_setMaterialFlag(ISceneNode* pointer, video::E_MATERIAL_FLAG flag, bool newvalue){pointer->setMaterialFlag(flag, newvalue);}
IRRLICHT_C_API void ISceneNode_setMaterialTexture(ISceneNode* pointer, u32 textureLayer, video::ITexture* texture){pointer->setMaterialTexture(textureLayer, texture);}
IRRLICHT_C_API void ISceneNode_setMaterialType(ISceneNode* pointer, video::E_MATERIAL_TYPE newType){pointer->setMaterialType(newType);}
IRRLICHT_C_API const vector3df& ISceneNode_getScale(ISceneNode* pointer){return pointer->getScale();}
IRRLICHT_C_API void ISceneNode_setScale(ISceneNode* pointer, const core::vector3df& scale){pointer->setScale(scale);}
IRRLICHT_C_API const vector3df& ISceneNode_getRotation(ISceneNode* pointer){return pointer->getRotation();}
IRRLICHT_C_API void ISceneNode_setRotation(ISceneNode* pointer, const core::vector3df& rotation){pointer->setRotation(rotation);}
IRRLICHT_C_API const vector3df& ISceneNode_getPosition(ISceneNode* pointer){return pointer->getPosition();}
IRRLICHT_C_API void ISceneNode_setPosition(ISceneNode* pointer, const vector3df& newpos){pointer->setPosition(newpos);}
IRRLICHT_C_API const vector3df& ISceneNode_getAbsolutePosition(ISceneNode* pointer){return (const vector3df&)pointer->getAbsolutePosition();}
IRRLICHT_C_API void ISceneNode_setAutomaticCulling(ISceneNode* pointer, E_CULLING_TYPE state){pointer->setAutomaticCulling(state);}
IRRLICHT_C_API E_CULLING_TYPE ISceneNode_getAutomaticCulling(ISceneNode* pointer){return pointer->getAutomaticCulling();}
IRRLICHT_C_API void ISceneNode_setDebugDataVisible(ISceneNode* pointer, s32 state){pointer->setDebugDataVisible(state);}
IRRLICHT_C_API s32 ISceneNode_isDebugDataVisible(ISceneNode* pointer){return pointer->isDebugDataVisible();}
IRRLICHT_C_API void ISceneNode_setIsDebugObject(ISceneNode* pointer, bool debugObject){pointer->setIsDebugObject(debugObject);}
IRRLICHT_C_API bool ISceneNode_isDebugObject(ISceneNode* pointer){return pointer->isDebugObject();}
//IRRLICHT_C_API const list<ISceneNode*>* ISceneNode_getChildren(ISceneNode* pointer){return &pointer->getChildren();}
IRRLICHT_C_API ISceneNodeListExt* ISceneNode_getChildren(ISceneNode* pointer){return new ISceneNodeListExt(&pointer->getChildren());}
IRRLICHT_C_API void ISceneNode_setParent(ISceneNode* pointer, ISceneNode* newParent){pointer->setParent(newParent);}
IRRLICHT_C_API ITriangleSelector* ISceneNode_getTriangleSelector(ISceneNode* pointer){return pointer->getTriangleSelector();}
IRRLICHT_C_API void ISceneNode_setTriangleSelector(ISceneNode* pointer, ITriangleSelector* selector){pointer->setTriangleSelector(selector);}
IRRLICHT_C_API void ISceneNode_updateAbsolutePosition(ISceneNode* pointer){pointer->updateAbsolutePosition();}
IRRLICHT_C_API ISceneNode* ISceneNode_getParent(ISceneNode* pointer){return pointer->getParent();}
IRRLICHT_C_API ESCENE_NODE_TYPE ISceneNode_getType(ISceneNode* pointer){return pointer->getType();}
IRRLICHT_C_API void ISceneNode_serializeAttributes(ISceneNode* pointer, io::IAttributes* out, io::SAttributeReadWriteOptions* options=0){pointer->serializeAttributes(out, options);}
IRRLICHT_C_API void ISceneNode_deserializeAttributes(ISceneNode* pointer, io::IAttributes* in, io::SAttributeReadWriteOptions* options=0){pointer->deserializeAttributes(in, options);}
IRRLICHT_C_API ISceneNode* ISceneNode_clone(ISceneNode* pointer, ISceneNode* newParent=0, ISceneManager* newManager=0){return pointer->clone(newParent, newManager);}
IRRLICHT_C_API ISceneManager* ISceneNode_getSceneManager(ISceneNode* pointer){return pointer->getSceneManager();}

//================= CustomSceneNode
IRRLICHT_C_API CustomSceneNode* CustomSceneNode_ctor(scene::ISceneNode* parent, scene::ISceneManager* mgr, s32 id)
{
	CustomSceneNode* node = new CustomSceneNode(parent, mgr, id);
	return node;
}
//IRRLICHT_C_API CustomSceneNode* CustomSceneNode_ctor2(){return new CustomSceneNode();}
IRRLICHT_C_API void CustomSceneNode_set_OnRegisterSceneNode(CustomSceneNode* pointer, void(IRRCALLCONV *func)()){pointer->set_func_OnRegisterSceneNode(func);}
IRRLICHT_C_API void CustomSceneNode_set_render(CustomSceneNode* pointer, void(IRRCALLCONV *func)()){pointer->set_func_render(func);}
IRRLICHT_C_API void CustomSceneNode_set_getBoundingBox(CustomSceneNode* pointer, const core::aabbox3d<f32>*(IRRCALLCONV *func)()){pointer->set_func_getBoundingBox(func);}
IRRLICHT_C_API void CustomSceneNode_set_getMaterial(CustomSceneNode* pointer, video::SMaterial* (IRRCALLCONV *func)(u32)){pointer->set_func_getMaterial(func);}
IRRLICHT_C_API void CustomSceneNode_set_getMaterialCount(CustomSceneNode* pointer, const u32 (IRRCALLCONV *func)()){pointer->set_func_getMaterialCount(func);}
//IRRLICHT_C_API void CustomSceneNode_set_BoundingBox(CustomSceneNode* pointer, core::aabbox3d<f32>* value){pointer->set_BoundingBox(value);}
//IRRLICHT_C_API void CustomSceneNode_set_Vertices(CustomSceneNode* pointer, video::S3DVertex* value){pointer->set_Vertices(value);}
//IRRLICHT_C_API void CustomSceneNode_set_Material(CustomSceneNode* pointer, video::SMaterial* value){pointer->set_Material(value);}

#ifdef __cplusplus
}
#endif

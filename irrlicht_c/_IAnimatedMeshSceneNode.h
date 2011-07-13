// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

class UserAnimationEndCallBack : public IAnimationEndCallBack
{
public:
	UserAnimationEndCallBack()
	{
		func_event = NULL;
	}
	UserAnimationEndCallBack(void(IRRCALLCONV *func)(IAnimatedMeshSceneNode*))
	{
		func_event = func;
	}
	void set_func_event(void(IRRCALLCONV *func)(IAnimatedMeshSceneNode*))
	{
		func_event = func;
	}
	virtual void OnAnimationEnd(IAnimatedMeshSceneNode* node)
	{
		if (func_event != NULL)
		{
#ifdef _MSC_VER
#ifdef DEBUG_EVENTS
			__try
			{
				(*func_event)(node);
			}
			__except(filter(_exception_code(), (struct _EXCEPTION_POINTERS *)_exception_info(), "IAnimationEndCallBack::OnAnimationEnd"))
			{
			}
#else
			(*func_event)(node);
#endif
#else
			(*func_event)(node);
#endif
		}
	}
	~UserAnimationEndCallBack()
	{
		if (func_event != NULL)
			func_event = NULL;
	}
private:
	void(IRRCALLCONV *func_event)(IAnimatedMeshSceneNode* node);
};

#ifdef __cplusplus
extern "C" {
#endif

//class IAnimationEndCallBack : public virtual IReferenceCounted
IRRLICHT_C_API UserAnimationEndCallBack* IAnimationEndCallBack_ctor1(){return new UserAnimationEndCallBack();}
IRRLICHT_C_API UserAnimationEndCallBack* IAnimationEndCallBack_ctor2(void(IRRCALLCONV *OnEventMethod)(IAnimatedMeshSceneNode* node)){return new UserAnimationEndCallBack(OnEventMethod);}
//IRRLICHT_C_API void IAnimationEndCallBack_Destructor(void* pointer){delete pointer;}
IRRLICHT_C_API void IAnimationEndCallBack_set_func_event(UserAnimationEndCallBack* pointer, void(IRRCALLCONV *OnEventMethod)(IAnimatedMeshSceneNode* node)){pointer->set_func_event(OnEventMethod);}
IRRLICHT_C_API UserAnimationEndCallBack* IAnimationEndCallBack_UserAnimationEndCallBack(IAnimationEndCallBack* pointer){return (UserAnimationEndCallBack*)pointer;}

//class IAnimatedMeshSceneNode : public ISceneNode
//IRRLICHT_C_API IAnimatedMeshSceneNode* IAnimatedMeshSceneNode_other_as_this(void* pointer){return (IAnimatedMeshSceneNode*)pointer;}

IRRLICHT_C_API IAnimatedMeshSceneNode* IAnimatedMeshSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr = 0, s32 id = -1, const vector3df& position = vector3df(0,0,0), const vector3df& rotation = vector3df(0,0,0), const vector3df& scale = vector3df(1.0f, 1.0f, 1.0f))
{
	//return new IAnimatedMeshSceneNode(parent, mgr, id, position, rotation, scale);
	IAnimatedMeshSceneNode* temp = 0;
	IAnimatedMeshSceneNode* node = (IAnimatedMeshSceneNode*)temp->clone(parent, mgr);
	temp->drop();
	if(id > -1)
		node->setID(id);
	if(&position)
		node->setPosition(position);
	if(&rotation)
		node->setRotation(rotation);
	if(&scale)
		node->setScale(scale);
	return node;
}
//IRRLICHT_C_API void IAnimatedMeshSceneNode_Destructor(IAnimatedMeshSceneNode* pointer){delete pointer;}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setCurrentFrame(IAnimatedMeshSceneNode* pointer, f32 frame)
{pointer->setCurrentFrame(frame);}
IRRLICHT_C_API bool IAnimatedMeshSceneNode_setFrameLoop(IAnimatedMeshSceneNode* pointer, s32 begin, s32 end)
{return pointer->setFrameLoop(begin, end);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setAnimationSpeed(IAnimatedMeshSceneNode* pointer, f32 framesPerSecond)
{pointer->setAnimationSpeed(framesPerSecond);}
IRRLICHT_C_API const f32 IAnimatedMeshSceneNode_getAnimationSpeed(IAnimatedMeshSceneNode* pointer)
{return pointer->getAnimationSpeed();}
IRRLICHT_C_API IShadowVolumeSceneNode* IAnimatedMeshSceneNode_addShadowVolumeSceneNode(IAnimatedMeshSceneNode* pointer, const IMesh* shadowMesh=0, s32 id=-1, bool zfailmethod=true, f32 infinity=10000.0f)
{return pointer->addShadowVolumeSceneNode(shadowMesh, id, zfailmethod, infinity);}
IRRLICHT_C_API IBoneSceneNode* IAnimatedMeshSceneNode_getJointNode1(IAnimatedMeshSceneNode* pointer, const c8* jointName)
{return pointer->getJointNode(jointName);}
IRRLICHT_C_API IBoneSceneNode* IAnimatedMeshSceneNode_getJointNode2(IAnimatedMeshSceneNode* pointer, u32 jointID)
{return pointer->getJointNode(jointID);}
IRRLICHT_C_API u32 IAnimatedMeshSceneNode_getJointCount(IAnimatedMeshSceneNode* pointer)
{return pointer->getJointCount();}
IRRLICHT_C_API ISceneNode* IAnimatedMeshSceneNode_getMS3DJointNode(IAnimatedMeshSceneNode* pointer, const c8* jointName)
{return pointer->getMS3DJointNode(jointName);}
IRRLICHT_C_API ISceneNode* IAnimatedMeshSceneNode_getXJointNode(IAnimatedMeshSceneNode* pointer, const c8* jointName)
{return pointer->getXJointNode(jointName);}
IRRLICHT_C_API bool IAnimatedMeshSceneNode_setMD2Animation1(IAnimatedMeshSceneNode* pointer, EMD2_ANIMATION_TYPE anim)
{return pointer->setMD2Animation(anim);}
IRRLICHT_C_API bool IAnimatedMeshSceneNode_setMD2Animation2(IAnimatedMeshSceneNode* pointer, const c8* animationName)
{return pointer->setMD2Animation(animationName);}
IRRLICHT_C_API f32 IAnimatedMeshSceneNode_getFrameNr(IAnimatedMeshSceneNode* pointer)
{return pointer->getFrameNr();}
IRRLICHT_C_API s32 IAnimatedMeshSceneNode_getStartFrame(IAnimatedMeshSceneNode* pointer)
{return pointer->getStartFrame();}
IRRLICHT_C_API s32 IAnimatedMeshSceneNode_getEndFrame(IAnimatedMeshSceneNode* pointer)
{return pointer->getEndFrame();}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setLoopMode(IAnimatedMeshSceneNode* pointer, bool playAnimationLooped)
{pointer->setLoopMode(playAnimationLooped);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setAnimationEndCallback(IAnimatedMeshSceneNode* pointer, IAnimationEndCallBack* callback=0)
{pointer->setAnimationEndCallback(callback);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setReadOnlyMaterials(IAnimatedMeshSceneNode* pointer, bool readonly)
{pointer->setReadOnlyMaterials(readonly);}
IRRLICHT_C_API bool IAnimatedMeshSceneNode_isReadOnlyMaterials(IAnimatedMeshSceneNode* pointer)
{return pointer->isReadOnlyMaterials();}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setMesh(IAnimatedMeshSceneNode* pointer, IAnimatedMesh* mesh)
{pointer->setMesh(mesh);}
IRRLICHT_C_API IAnimatedMesh* IAnimatedMeshSceneNode_getMesh(IAnimatedMeshSceneNode* pointer)
{return pointer->getMesh();}
IRRLICHT_C_API const SMD3QuaternionTag* IAnimatedMeshSceneNode_getMD3TagTransformation(IAnimatedMeshSceneNode* pointer, const c8* tagname)
{return pointer->getMD3TagTransformation(core::stringc(tagname));}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setJointMode(IAnimatedMeshSceneNode* pointer, E_JOINT_UPDATE_ON_RENDER mode)
{pointer->setJointMode(mode);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setTransitionTime(IAnimatedMeshSceneNode* pointer, f32 Time)
{pointer->setTransitionTime(Time);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_animateJoints(IAnimatedMeshSceneNode* pointer, bool CalculateAbsolutePositions=true)
{pointer->animateJoints(CalculateAbsolutePositions);}
IRRLICHT_C_API void IAnimatedMeshSceneNode_setRenderFromIdentity(IAnimatedMeshSceneNode* pointer, bool On)
{pointer->setRenderFromIdentity(On);}
IRRLICHT_C_API ISceneNode* IAnimatedMeshSceneNode_clone(IAnimatedMeshSceneNode* pointer, ISceneNode* newParent=0, ISceneManager* newManager=0)
{return pointer->clone(newParent, newManager);}

#ifdef __cplusplus
}
#endif

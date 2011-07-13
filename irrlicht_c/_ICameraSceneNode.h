// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

class UserCameraSceneNode : public ICameraSceneNode
{
public:
	virtual void set_func_event(bool(IRRCALLCONV *func)(const SEvent* event))
	{
		func_event = func;
	}
	virtual bool OnEvent(const SEvent& event)
	{
		if (func_event != NULL)
		{
			return func_event(&event);
		}
		else{return false;}
	}
	~UserCameraSceneNode()
	{
		func_event = NULL;
	}
private:
	bool(IRRCALLCONV *func_event)(const SEvent* event);
};
IRRLICHT_C_API UserCameraSceneNode* ICameraSceneNode_ctor(ICameraSceneNode* pointer){return (UserCameraSceneNode*)pointer;}
//IRRLICHT_C_API void ICameraSceneNode_Destructor(UserCameraSceneNode* pointer){delete pointer;}
IRRLICHT_C_API void ICameraSceneNode_set_func_event(UserCameraSceneNode* pointer, bool(IRRCALLCONV *OnEventMethod)(const SEvent* event)){pointer->set_func_event(OnEventMethod);}

IRRLICHT_C_API void ICameraSceneNode_setProjectionMatrix(UserCameraSceneNode* pointer, const core::matrix4& projection, bool isOrthogonal=false){pointer->setProjectionMatrix(projection, isOrthogonal);}
IRRLICHT_C_API const core::matrix4& ICameraSceneNode_getProjectionMatrix(UserCameraSceneNode* pointer){return pointer->getProjectionMatrix();}
IRRLICHT_C_API const core::matrix4& ICameraSceneNode_getViewMatrix(UserCameraSceneNode* pointer){return pointer->getViewMatrix();}
IRRLICHT_C_API void ICameraSceneNode_setViewMatrixAffector(UserCameraSceneNode* pointer, const core::matrix4& affector){pointer->setViewMatrixAffector(affector);}
IRRLICHT_C_API const core::matrix4& ICameraSceneNode_getViewMatrixAffector(UserCameraSceneNode* pointer){return pointer->getViewMatrixAffector();}
IRRLICHT_C_API void ICameraSceneNode_setTarget(UserCameraSceneNode* pointer, const core::vector3df& pos){pointer->setTarget(pos);}
IRRLICHT_C_API void ICameraSceneNode_setRotation(UserCameraSceneNode* pointer, const core::vector3df& rotation){pointer->setRotation(rotation);}
IRRLICHT_C_API const core::vector3df& ICameraSceneNode_getTarget(UserCameraSceneNode* pointer){return pointer->getTarget();}
IRRLICHT_C_API void ICameraSceneNode_setUpVector(UserCameraSceneNode* pointer, const core::vector3df& pos){pointer->setUpVector(pos);}
IRRLICHT_C_API const core::vector3df& ICameraSceneNode_getUpVector(UserCameraSceneNode* pointer){return pointer->getUpVector();}
IRRLICHT_C_API f32 ICameraSceneNode_getNearValue(UserCameraSceneNode* pointer){return pointer->getNearValue();}
IRRLICHT_C_API f32 ICameraSceneNode_getFarValue(UserCameraSceneNode* pointer){return pointer->getFarValue();}
IRRLICHT_C_API f32 ICameraSceneNode_getAspectRatio(UserCameraSceneNode* pointer){return pointer->getAspectRatio();}
IRRLICHT_C_API f32 ICameraSceneNode_getFOV(UserCameraSceneNode* pointer){return pointer->getFOV();}
IRRLICHT_C_API void ICameraSceneNode_setNearValue(UserCameraSceneNode* pointer, f32 zn){pointer->setNearValue(zn);}
IRRLICHT_C_API void ICameraSceneNode_setFarValue(UserCameraSceneNode* pointer, f32 zf){pointer->setFarValue(zf);}
IRRLICHT_C_API void ICameraSceneNode_setAspectRatio(UserCameraSceneNode* pointer, f32 aspect){pointer->setAspectRatio(aspect);}
IRRLICHT_C_API void ICameraSceneNode_setFOV(UserCameraSceneNode* pointer, f32 fovy){pointer->setFOV(fovy);}
IRRLICHT_C_API const SViewFrustum* ICameraSceneNode_getViewFrustum(UserCameraSceneNode* pointer){return pointer->getViewFrustum();}
IRRLICHT_C_API void ICameraSceneNode_setInputReceiverEnabled(UserCameraSceneNode* pointer, bool enabled){pointer->setInputReceiverEnabled(enabled);}
IRRLICHT_C_API bool ICameraSceneNode_isInputReceiverEnabled(UserCameraSceneNode* pointer){return pointer->isInputReceiverEnabled();}
IRRLICHT_C_API bool ICameraSceneNode_isOrthogonal(UserCameraSceneNode* pointer){return pointer->isOrthogonal();}
IRRLICHT_C_API void ICameraSceneNode_bindTargetAndRotation(UserCameraSceneNode* pointer, bool bound){pointer->bindTargetAndRotation(bound);}
IRRLICHT_C_API bool ICameraSceneNode_getTargetAndRotationBinding(UserCameraSceneNode* pointer){return pointer->getTargetAndRotationBinding();}

#ifdef __cplusplus
}
#endif

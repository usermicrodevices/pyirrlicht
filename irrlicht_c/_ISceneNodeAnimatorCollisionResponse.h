// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

class UserCollisionCallback : public ICollisionCallback
{
public:
	UserCollisionCallback(bool(IRRCALLCONV *func)(const ISceneNodeAnimatorCollisionResponse* animator) = false)
	{
		func_animator = func;
	}
	virtual void set_func_animator(bool(IRRCALLCONV *func)(const ISceneNodeAnimatorCollisionResponse* animator))
	{
		func_animator = func;
	}
	virtual bool onCollision(const ISceneNodeAnimatorCollisionResponse& animator)
	{
		if (func_animator != NULL)
		{
			return func_animator(&animator);
		}
		else{return false;}
	}
	~UserCollisionCallback()
	{
		func_animator = NULL;
	}
private:
	bool(IRRCALLCONV *func_animator)(const ISceneNodeAnimatorCollisionResponse* animator);
};
//IRRLICHT_C_API bool ICollisionCallback_onCollision(ICollisionCallback* pointer, const ISceneNodeAnimatorCollisionResponse& animator)
//{return pointer->onCollision(animator);}
IRRLICHT_C_API UserCollisionCallback* ICollisionCallback_ctor1(ICollisionCallback* pointer){return (UserCollisionCallback*)pointer;}
IRRLICHT_C_API UserCollisionCallback* ICollisionCallback_ctor2(bool(IRRCALLCONV *func)(const ISceneNodeAnimatorCollisionResponse* animator)){return new UserCollisionCallback(func);}
//IRRLICHT_C_API void ICollisionCallback_Destructor(UserCollisionCallback* pointer){delete pointer;}
IRRLICHT_C_API void ICollisionCallback_set_func_animator(UserCollisionCallback* pointer, bool(IRRCALLCONV *func)(const ISceneNodeAnimatorCollisionResponse* animator)){pointer->set_func_animator(func);}

//IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_Destructor(ISceneNodeAnimatorCollisionResponse* pointer){delete pointer;}
IRRLICHT_C_API bool ISceneNodeAnimatorCollisionResponse_isFalling(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->isFalling();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setEllipsoidRadius(ISceneNodeAnimatorCollisionResponse* pointer, const core::vector3df& radius){pointer->setEllipsoidRadius(radius);}
IRRLICHT_C_API core::vector3df* ISceneNodeAnimatorCollisionResponse_getEllipsoidRadius(ISceneNodeAnimatorCollisionResponse* pointer){return &pointer->getEllipsoidRadius();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setGravity(ISceneNodeAnimatorCollisionResponse* pointer, const core::vector3df& gravity){pointer->setGravity(gravity);}
IRRLICHT_C_API core::vector3df* ISceneNodeAnimatorCollisionResponse_getGravity(ISceneNodeAnimatorCollisionResponse* pointer){return &pointer->getGravity();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_jump(ISceneNodeAnimatorCollisionResponse* pointer, f32 jumpSpeed){pointer->jump(jumpSpeed);}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setAnimateTarget(ISceneNodeAnimatorCollisionResponse* pointer, bool enable){pointer->setAnimateTarget(enable);}
IRRLICHT_C_API bool ISceneNodeAnimatorCollisionResponse_getAnimateTarget(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getAnimateTarget();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setEllipsoidTranslation(ISceneNodeAnimatorCollisionResponse* pointer, const core::vector3df& translation){pointer->setEllipsoidTranslation(translation);}
IRRLICHT_C_API core::vector3df* ISceneNodeAnimatorCollisionResponse_getEllipsoidTranslation(ISceneNodeAnimatorCollisionResponse* pointer){return &pointer->getEllipsoidTranslation();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setWorld(ISceneNodeAnimatorCollisionResponse* pointer, ITriangleSelector* newWorld){pointer->setWorld(newWorld);}
IRRLICHT_C_API ITriangleSelector* ISceneNodeAnimatorCollisionResponse_getWorld(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getWorld();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setTargetNode(ISceneNodeAnimatorCollisionResponse* pointer, ISceneNode * node){pointer->setTargetNode(node);}
IRRLICHT_C_API ISceneNode* ISceneNodeAnimatorCollisionResponse_getTargetNode(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getTargetNode();}
IRRLICHT_C_API bool ISceneNodeAnimatorCollisionResponse_collisionOccurred(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->collisionOccurred();}
IRRLICHT_C_API const core::vector3df& ISceneNodeAnimatorCollisionResponse_getCollisionPoint(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getCollisionPoint();}
IRRLICHT_C_API const core::triangle3df& ISceneNodeAnimatorCollisionResponse_getCollisionTriangle(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getCollisionTriangle();}
IRRLICHT_C_API const core::vector3df& ISceneNodeAnimatorCollisionResponse_getCollisionResultPosition(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getCollisionResultPosition();}
IRRLICHT_C_API const ISceneNode* ISceneNodeAnimatorCollisionResponse_getCollisionNode(ISceneNodeAnimatorCollisionResponse* pointer){return pointer->getCollisionNode();}
IRRLICHT_C_API void ISceneNodeAnimatorCollisionResponse_setCollisionCallback(ISceneNodeAnimatorCollisionResponse* pointer, ICollisionCallback* callback){pointer->setCollisionCallback(callback);}

#ifdef __cplusplus
}
#endif

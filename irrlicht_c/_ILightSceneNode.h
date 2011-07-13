// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ILightSceneNode
IRRLICHT_C_API ILightSceneNode* ILightSceneNode_ctor(ISceneNode* parent = 0, ISceneManager* mgr = 0, s32 id = -1, const core::vector3df& position = core::vector3df(0,0,0))
{
	ILightSceneNode* temp = 0;
	ILightSceneNode* node = (ILightSceneNode*)temp->clone(parent, mgr);
	temp->drop();
	//if(parent)
		//node->setParent(parent);
	//if(mgr)
		//node->setSceneManager(mgr);
	if(id > -1)
		node->setID(id);
	if(&position)
		node->setPosition(position);
	return node;
}
IRRLICHT_C_API void ILightSceneNode_setLightData(ILightSceneNode* pointer, const video::SLight& light){pointer->setLightData(light);}
IRRLICHT_C_API const video::SLight& ILightSceneNode_getLightData(ILightSceneNode* pointer){return pointer->getLightData();}
IRRLICHT_C_API void ILightSceneNode_setVisible(ILightSceneNode* pointer, bool isVisible){pointer->setVisible(isVisible);}
IRRLICHT_C_API void ILightSceneNode_setRadius(ILightSceneNode* pointer, f32 radius){pointer->setRadius(radius);}
IRRLICHT_C_API f32 ILightSceneNode_getRadius(ILightSceneNode* pointer){return pointer->getRadius();}
IRRLICHT_C_API void ILightSceneNode_setLightType(ILightSceneNode* pointer, video::E_LIGHT_TYPE type){pointer->setLightType(type);}
IRRLICHT_C_API video::E_LIGHT_TYPE ILightSceneNode_getLightType(ILightSceneNode* pointer){return pointer->getLightType();}
IRRLICHT_C_API void ILightSceneNode_enableCastShadow(ILightSceneNode* pointer, bool shadow=true){pointer->enableCastShadow(shadow);}
IRRLICHT_C_API bool ILightSceneNode_getCastShadow(ILightSceneNode* pointer){return pointer->getCastShadow();}

#ifdef __cplusplus
}
#endif

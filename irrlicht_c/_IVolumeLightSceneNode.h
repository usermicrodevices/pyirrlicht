// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IVolumeLightSceneNode : public ISceneNode
IRRLICHT_C_API IVolumeLightSceneNode* IVolumeLightSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position, const core::vector3df& rotation, const core::vector3df& scale)
{
	vector3df* p_null = NULL;
	IVolumeLightSceneNode* temp = 0;
	IVolumeLightSceneNode* node = (IVolumeLightSceneNode*)temp->clone(parent, mgr);
	temp->drop();
	if(id > -1)
		node->setID(id);
	if(&position != p_null)
		node->setPosition(position);
	if(&rotation != p_null)
		node->setRotation(rotation);
	if(&scale != p_null)
		node->setScale(scale);
	return node;
}

IRRLICHT_C_API ESCENE_NODE_TYPE IVolumeLightSceneNode_getType(IVolumeLightSceneNode* pointer)
{return pointer->getType();}

IRRLICHT_C_API void IVolumeLightSceneNode_setSubDivideU(IVolumeLightSceneNode* pointer, const u32 inU)
{pointer->setSubDivideU(inU);}

IRRLICHT_C_API void IVolumeLightSceneNode_setSubDivideV(IVolumeLightSceneNode* pointer, const u32 inV)
{pointer->setSubDivideV(inV);}

IRRLICHT_C_API u32 IVolumeLightSceneNode_getSubDivideU(IVolumeLightSceneNode* pointer)
{return pointer->getSubDivideU();}

IRRLICHT_C_API u32 IVolumeLightSceneNode_getSubDivideV(IVolumeLightSceneNode* pointer)
{return pointer->getSubDivideV();}

IRRLICHT_C_API void IVolumeLightSceneNode_setFootColor(IVolumeLightSceneNode* pointer, const video::SColor* inColour)
{pointer->setFootColor(*inColour);}

IRRLICHT_C_API void IVolumeLightSceneNode_setTailColor(IVolumeLightSceneNode* pointer, const video::SColor* inColour)
{pointer->setTailColor(*inColour);}

IRRLICHT_C_API const video::SColor IVolumeLightSceneNode_getFootColor(IVolumeLightSceneNode* pointer)
{return pointer->getFootColor();}

IRRLICHT_C_API const video::SColor IVolumeLightSceneNode_getTailColor(IVolumeLightSceneNode* pointer)
{return pointer->getTailColor();}

#ifdef __cplusplus
}
#endif

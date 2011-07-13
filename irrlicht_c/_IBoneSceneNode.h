// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IBoneSceneNode : public ISceneNode
IRRLICHT_C_API IBoneSceneNode* IBoneSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id = -1)
{
	IBoneSceneNode* temp = 0;
	IBoneSceneNode* node = (IBoneSceneNode*)temp->clone(parent, mgr);
	if(id > -1)
		node->setID(id);
	return node;
}
IRRLICHT_C_API const c8* IBoneSceneNode_getBoneName(IBoneSceneNode* pointer)
{return pointer->getBoneName();}
IRRLICHT_C_API u32 IBoneSceneNode_getBoneIndex(IBoneSceneNode* pointer)
{return pointer->getBoneIndex();}
IRRLICHT_C_API bool IBoneSceneNode_setAnimationMode(IBoneSceneNode* pointer, E_BONE_ANIMATION_MODE mode)
{return pointer->setAnimationMode(mode);}
IRRLICHT_C_API E_BONE_ANIMATION_MODE IBoneSceneNode_getAnimationMode(IBoneSceneNode* pointer)
{return pointer->getAnimationMode();}
IRRLICHT_C_API const core::aabbox3d<f32>* IBoneSceneNode_getBoundingBox(IBoneSceneNode* pointer)
{return &pointer->getBoundingBox();}
IRRLICHT_C_API void IBoneSceneNode_OnAnimate(IBoneSceneNode* pointer, u32 timeMs)
{pointer->OnAnimate(timeMs);}
IRRLICHT_C_API void IBoneSceneNode_render(IBoneSceneNode* pointer)
{pointer->render();}
IRRLICHT_C_API void IBoneSceneNode_setSkinningSpace(IBoneSceneNode* pointer, E_BONE_SKINNING_SPACE space)
{pointer->setSkinningSpace(space);}
IRRLICHT_C_API E_BONE_SKINNING_SPACE IBoneSceneNode_getSkinningSpace(IBoneSceneNode* pointer)
{return pointer->getSkinningSpace();}
IRRLICHT_C_API void IBoneSceneNode_updateAbsolutePositionOfAllChildren(IBoneSceneNode* pointer)
{pointer->updateAbsolutePositionOfAllChildren();}
IRRLICHT_C_API void IBoneSceneNode_set_positionHint(IBoneSceneNode* pointer, s32 value)
{pointer->positionHint = value;}
IRRLICHT_C_API s32 IBoneSceneNode_get_positionHint(IBoneSceneNode* pointer)
{return pointer->positionHint;}
IRRLICHT_C_API void IBoneSceneNode_set_scaleHint(IBoneSceneNode* pointer, s32 value)
{pointer->scaleHint = value;}
IRRLICHT_C_API s32 IBoneSceneNode_get_scaleHint(IBoneSceneNode* pointer)
{return pointer->scaleHint;}
IRRLICHT_C_API void IBoneSceneNode_set_rotationHint(IBoneSceneNode* pointer, s32 value)
{pointer->rotationHint = value;}
IRRLICHT_C_API s32 IBoneSceneNode_get_rotationHint(IBoneSceneNode* pointer)
{return pointer->rotationHint;}


#ifdef __cplusplus
}
#endif

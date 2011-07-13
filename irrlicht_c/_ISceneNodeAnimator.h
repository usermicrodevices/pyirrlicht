// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ISceneNodeAnimator
IRRLICHT_C_API void ISceneNodeAnimator_animateNode(ISceneNodeAnimator* pointer, ISceneNode* node, u32 timeMs){pointer->animateNode(node, timeMs);}
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimator_createClone(ISceneNodeAnimator* pointer, ISceneNode* node, ISceneManager* newManager=0){return pointer->createClone(node, newManager);}
IRRLICHT_C_API bool ISceneNodeAnimator_isEventReceiverEnabled(ISceneNodeAnimator* pointer){return pointer->isEventReceiverEnabled();}
IRRLICHT_C_API bool ISceneNodeAnimator_OnEvent(ISceneNodeAnimator* pointer, const SEvent& event){return pointer->OnEvent(event);}
IRRLICHT_C_API ESCENE_NODE_ANIMATOR_TYPE ISceneNodeAnimator_getType(ISceneNodeAnimator* pointer){return pointer->getType();}
IRRLICHT_C_API bool ISceneNodeAnimator_hasFinished(ISceneNodeAnimator* pointer){return pointer->hasFinished();}
//IRRLICHT_C_API bool ISceneNodeAnimator_set_func_event(ISceneNodeAnimator* pointer, void* OnEventMethod)
IRRLICHT_C_API bool ISceneNodeAnimator_set_func_event(ISceneNodeAnimator* pointer, bool(IRRCALLCONV * OnEventMethod)(const SEvent&))
{
#ifdef _MSC_VER
#ifndef DEBUG
	//size_t* vptr =  *(size_t**)pointer;
	//__asm{mov ecx, pointer}
	//( (bool (IRRCALLCONV*)(const SEvent&)) (*(size_t**)pointer)[3] ) = OnEventMethod;
	(*(size_t**)pointer)[3] = (size_t)OnEventMethod;
	return true;
#else
	printf("ISceneNodeAnimator_set_func_event only for RELEASE mode, current is DEBUG!");
	return false;
#endif
#else
	//pointer->_vptr[3] = (int(*)(...))OnEventMethod;
	(*(size_t**)pointer)[3] = (size_t)OnEventMethod;
	return true;
#endif
}

#ifdef __cplusplus
}
#endif

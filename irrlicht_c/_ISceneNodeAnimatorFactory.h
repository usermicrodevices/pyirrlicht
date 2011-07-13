// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class ISceneNodeAnimatorFactory : public IReferenceCounted
IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorFactory_createSceneNodeAnimator1(ISceneNodeAnimatorFactory* pointer, ESCENE_NODE_ANIMATOR_TYPE type, ISceneNode* target)
{return pointer->createSceneNodeAnimator(type, target);}

IRRLICHT_C_API ISceneNodeAnimator* ISceneNodeAnimatorFactory_createSceneNodeAnimator2(ISceneNodeAnimatorFactory* pointer, const c8* typeName, ISceneNode* target)
{return pointer->createSceneNodeAnimator(typeName, target);}

IRRLICHT_C_API u32 ISceneNodeAnimatorFactory_getCreatableSceneNodeAnimatorTypeCount(ISceneNodeAnimatorFactory* pointer)
{return pointer->getCreatableSceneNodeAnimatorTypeCount();}

IRRLICHT_C_API ESCENE_NODE_ANIMATOR_TYPE ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorType(ISceneNodeAnimatorFactory* pointer, u32 idx)
{return pointer->getCreateableSceneNodeAnimatorType(idx);}

IRRLICHT_C_API const c8* ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1(ISceneNodeAnimatorFactory* pointer, u32 idx)
{return pointer->getCreateableSceneNodeAnimatorTypeName(idx);}

IRRLICHT_C_API const c8* ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2(ISceneNodeAnimatorFactory* pointer, ESCENE_NODE_ANIMATOR_TYPE type)
{return pointer->getCreateableSceneNodeAnimatorTypeName(type);}

#ifdef __cplusplus
}
#endif

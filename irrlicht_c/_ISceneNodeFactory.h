// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class ISceneNodeFactory : public IReferenceCounted
IRRLICHT_C_API ISceneNode* ISceneNodeFactory_addSceneNode1(ISceneNodeFactory* pointer, ESCENE_NODE_TYPE type, ISceneNode* parent = 0)
{return pointer->addSceneNode(type, parent);}

IRRLICHT_C_API ISceneNode* ISceneNodeFactory_addSceneNode2(ISceneNodeFactory* pointer, const c8* typeName, ISceneNode* parent = 0)
{return pointer->addSceneNode(typeName, parent);}

IRRLICHT_C_API u32 ISceneNodeFactory_getCreatableSceneNodeTypeCount(ISceneNodeFactory* pointer)
{return pointer->getCreatableSceneNodeTypeCount();}

IRRLICHT_C_API ESCENE_NODE_TYPE ISceneNodeFactory_getCreateableSceneNodeType(ISceneNodeFactory* pointer, u32 idx)
{return pointer->getCreateableSceneNodeType(idx);}

IRRLICHT_C_API const c8* ISceneNodeFactory_getCreateableSceneNodeTypeName1(ISceneNodeFactory* pointer, u32 idx)
{return pointer->getCreateableSceneNodeTypeName(idx);}

IRRLICHT_C_API const c8* ISceneNodeFactory_getCreateableSceneNodeTypeName2(ISceneNodeFactory* pointer, ESCENE_NODE_TYPE type)
{return pointer->getCreateableSceneNodeTypeName(type);}

#ifdef __cplusplus
}
#endif

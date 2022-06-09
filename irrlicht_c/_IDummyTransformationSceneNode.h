// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IDummyTransformationSceneNode
IRRLICHT_C_API IDummyTransformationSceneNode* IDummyTransformationSceneNode_ctor(ISceneNode* parent = 0, ISceneManager* mgr = 0, s32 id = -1)
{
	//IDummyTransformationSceneNode* node = (IDummyTransformationSceneNode*)mgr->addDummyTransformationSceneNode();
	//if(id > -1)
		//node->setID(id);
	return mgr->addDummyTransformationSceneNode(parent, id);
}
IRRLICHT_C_API core::matrix4& IDummyTransformationSceneNode_getRelativeTransformationMatrix(IDummyTransformationSceneNode* pointer)
{return pointer->getRelativeTransformationMatrix();}

#ifdef __cplusplus
}
#endif

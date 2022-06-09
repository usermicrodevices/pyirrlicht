// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IDummyTransformationSceneNode
IRRLICHT_C_API IDummyTransformationSceneNode* IDummyTransformationSceneNode_ctor(ISceneNode* parent = 0, ISceneManager* mgr = 0, s32 id = -1)
{return mgr->addDummyTransformationSceneNode(parent, id);}
IRRLICHT_C_API core::matrix4& IDummyTransformationSceneNode_getRelativeTransformationMatrix(IDummyTransformationSceneNode* pointer)
{return pointer->getRelativeTransformationMatrix();}

#ifdef __cplusplus
}
#endif

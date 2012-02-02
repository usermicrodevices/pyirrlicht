// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IMeshSceneNode
//IRRLICHT_C_API IMeshSceneNode* IMeshSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const vector3df& position = vector3df(0,0,0), const vector3df& rotation = vector3df(0,0,0), const vector3df& scale = vector3df(1,1,1))
//{return new IMeshSceneNode(parent, mgr, id, position, rotation, scale);}
IRRLICHT_C_API void IMeshSceneNode_setMesh(IMeshSceneNode* pointer, IMesh* mesh)
{pointer->setMesh(mesh);}
IRRLICHT_C_API IMesh* IMeshSceneNode_getMesh(IMeshSceneNode* pointer)
{return pointer->getMesh();}
IRRLICHT_C_API void IMeshSceneNode_setReadOnlyMaterials(IMeshSceneNode* pointer, bool readonly)
{pointer->setReadOnlyMaterials(readonly);}
IRRLICHT_C_API bool IMeshSceneNode_isReadOnlyMaterials(IMeshSceneNode* pointer)
{return pointer->isReadOnlyMaterials();}

#ifdef __cplusplus
}
#endif

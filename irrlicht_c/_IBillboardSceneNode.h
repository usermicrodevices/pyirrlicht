// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IBillboardSceneNode* IBillboardSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0))
{
	//return new IBillboardSceneNode(parent, mgr, id, position);
	IBillboardSceneNode* temp = 0;
	IBillboardSceneNode* node = (IBillboardSceneNode*)temp->clone(parent, mgr);
	temp->drop();
	if(id > -1)
		node->setID(id);
	if(&position)
		node->setPosition(position);
	return node;
}
IRRLICHT_C_API void IBillboardSceneNode_setSize(IBillboardSceneNode* pointer, const core::dimension2d<f32>& size){pointer->setSize(size);}
IRRLICHT_C_API const core::dimension2d<f32>& IBillboardSceneNode_getSize(IBillboardSceneNode* pointer){return pointer->getSize();}
IRRLICHT_C_API void IBillboardSceneNode_setColor(IBillboardSceneNode* pointer, const video::SColor & overallColor){pointer->setColor(overallColor);}
IRRLICHT_C_API void IBillboardSceneNode_setColor2(IBillboardSceneNode* pointer, const video::SColor & topColor, const video::SColor & bottomColor){pointer->setColor(topColor, bottomColor);}
IRRLICHT_C_API void IBillboardSceneNode_getColor(IBillboardSceneNode* pointer, video::SColor & topColor, video::SColor & bottomColor){pointer->getColor(topColor, bottomColor);}

#ifdef __cplusplus
}
#endif

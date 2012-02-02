// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IBillboardTextSceneNode
IRRLICHT_C_API IBillboardTextSceneNode* IBillboardTextSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0))
{
	//return new IBillboardTextSceneNode(parent, mgr, id, position);
	IBillboardTextSceneNode* temp = 0;
	IBillboardTextSceneNode* node = (IBillboardTextSceneNode*)temp->clone(parent, mgr);
	temp->drop();
	if(id > -1)
		node->setID(id);
	if(&position)
		node->setPosition(position);
	return node;
}
IRRLICHT_C_API void IBillboardTextSceneNode_setSize(IBillboardTextSceneNode* pointer, const core::dimension2d<f32>& size)
{pointer->setSize(size);}
IRRLICHT_C_API const core::dimension2d<f32>& IBillboardTextSceneNode_getSize(IBillboardTextSceneNode* pointer)
{return pointer->getSize();}
IRRLICHT_C_API void IBillboardTextSceneNode_setColor1(IBillboardTextSceneNode* pointer, const video::SColor& overallColor)
{pointer->setColor(overallColor);}
IRRLICHT_C_API void IBillboardTextSceneNode_setColor2(IBillboardTextSceneNode* pointer, const video::SColor& topColor, const video::SColor& bottomColor)
{pointer->setColor(topColor, bottomColor);}
IRRLICHT_C_API void IBillboardTextSceneNode_getColor(IBillboardTextSceneNode* pointer, video::SColor& topColor, video::SColor& bottomColor)
{pointer->getColor(topColor, bottomColor);}
IRRLICHT_C_API void IBillboardTextSceneNode_setText(IBillboardTextSceneNode* pointer, const wchar_t* text)
{pointer->setText(text);}
IRRLICHT_C_API void IBillboardTextSceneNode_setTextColor(IBillboardTextSceneNode* pointer, const video::SColor& color)
{pointer->setTextColor((video::SColor)color);}

#ifdef __cplusplus
}
#endif

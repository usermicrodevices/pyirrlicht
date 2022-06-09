// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IBillboardTextSceneNode
IRRLICHT_C_API IBillboardTextSceneNode* IBillboardTextSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0))
{
	vector3df* p_null = NULL;
	IBillboardTextSceneNode* node = reinterpret_cast<IBillboardTextSceneNode*>(mgr->addBillboardSceneNode());
	if(id > -1)
		node->setID(id);
	if(&position != p_null)
		node->setPosition(position);
	if(parent)
		parent->addChild(node);
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

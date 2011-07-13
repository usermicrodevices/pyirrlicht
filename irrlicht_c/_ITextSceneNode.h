// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ITextSceneNode
//IRRLICHT_C_API ITextSceneNode* ITextSceneNode_ctor(ISceneNode* parent, ISceneManager* mgr, s32 id, const core::vector3df& position = core::vector3df(0,0,0))
//{return (ITextSceneNode*)new ISceneNode(parent, mgr, id, position);}
IRRLICHT_C_API void ITextSceneNode_setText(ITextSceneNode* pointer, const wchar_t* text)
{pointer->setText(text);}
IRRLICHT_C_API void ITextSceneNode_setTextColor(ITextSceneNode* pointer, const video::SColor& color = SColor(0,0,0,0))
{pointer->setTextColor((video::SColor)color);}

#ifdef __cplusplus
}
#endif

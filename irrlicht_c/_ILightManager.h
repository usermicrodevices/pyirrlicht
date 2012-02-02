// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class ILightManager : public IReferenceCounted

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API void ILightManager_OnPreRender(ILightManager* pointer, core::array<ILightSceneNode*> & lightList)
{pointer->OnPreRender(lightList);}

IRRLICHT_C_API void ILightManager_OnPostRender(ILightManager* pointer)
{pointer->OnPostRender();}

IRRLICHT_C_API void ILightManager_OnRenderPassPreRender(ILightManager* pointer, E_SCENE_NODE_RENDER_PASS renderPass)
{pointer->OnRenderPassPreRender(renderPass);}

IRRLICHT_C_API void ILightManager_OnRenderPassPostRender(ILightManager* pointer, E_SCENE_NODE_RENDER_PASS renderPass)
{pointer->OnRenderPassPostRender(renderPass);}

IRRLICHT_C_API void ILightManager_OnNodePreRender(ILightManager* pointer, ISceneNode* node)
{pointer->OnNodePreRender(node);}

IRRLICHT_C_API void ILightManager_OnNodePostRender(ILightManager* pointer, ISceneNode* node)
{pointer->OnNodePostRender(node);}

#ifdef __cplusplus
}
#endif

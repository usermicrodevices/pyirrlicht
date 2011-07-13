// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#include "CGridSceneNode.h"

#ifdef __cplusplus
extern "C" {
#endif

//================= CGridSceneNode
IRRLICHT_C_API CGridSceneNode* CGridSceneNode_ctor(ISceneNode* parent, ISceneManager* smgr, s32 id = -1, u32 spacing = 8, u32 size = 1024, const video::SColor& gridcolor = video::SColor(255,128,128,128), u32 accentlineoffset = 8, const video::SColor& accentgridcolor = video::SColor(255,192,192,192), bool axislinestate = false)
{return new CGridSceneNode(parent, smgr, id, spacing, size, gridcolor, accentlineoffset, accentgridcolor, axislinestate);}
IRRLICHT_C_API CGridSceneNode* CGridSceneNode_clone(CGridSceneNode* pointer, ISceneNode* newParent = 0, ISceneManager* newSceneManager = 0)
{return pointer->clone(newParent, newSceneManager);}
IRRLICHT_C_API void CGridSceneNode_OnRegisterSceneNode(CGridSceneNode* pointer)
{pointer->OnRegisterSceneNode();}
IRRLICHT_C_API void CGridSceneNode_render(CGridSceneNode* pointer)
{pointer->render();}
IRRLICHT_C_API const core::aabbox3d<f32>& CGridSceneNode_getBoundingBox(CGridSceneNode* pointer)
{return pointer->getBoundingBox();}
IRRLICHT_C_API u32 CGridSceneNode_getMaterialCount(CGridSceneNode* pointer)
{return pointer->getMaterialCount();}
IRRLICHT_C_API video::SMaterial& CGridSceneNode_getMaterial(CGridSceneNode* pointer, u32 i)
{return pointer->getMaterial(i);}
IRRLICHT_C_API void CGridSceneNode_RegenerateGrid(CGridSceneNode* pointer)
{pointer->RegenerateGrid();}
IRRLICHT_C_API u32 CGridSceneNode_GetSpacing(CGridSceneNode* pointer)
{return pointer->GetSpacing();}
IRRLICHT_C_API u32 CGridSceneNode_GetSize(CGridSceneNode* pointer)
{return pointer->GetSize();}
IRRLICHT_C_API video::SColor* CGridSceneNode_GetGridColor(CGridSceneNode* pointer)
{return &pointer->GetGridColor();}
IRRLICHT_C_API u32 CGridSceneNode_GetAccentlineOffset(CGridSceneNode* pointer)
{return pointer->GetAccentlineOffset();}
IRRLICHT_C_API video::SColor* CGridSceneNode_GetAccentlineColor(CGridSceneNode* pointer)
{return &pointer->GetAccentlineColor();}
IRRLICHT_C_API bool CGridSceneNode_AreAxisLineActive(CGridSceneNode* pointer)
{return pointer->AreAxisLineActive();}
IRRLICHT_C_API video::SColor* CGridSceneNode_GetAxisLineXColor(CGridSceneNode* pointer)
{return &pointer->GetAxisLineXColor();}
IRRLICHT_C_API video::SColor* CGridSceneNode_GetAxisLineZColor(CGridSceneNode* pointer)
{return &pointer->GetAxisLineZColor();}
IRRLICHT_C_API void CGridSceneNode_SetSpacing(CGridSceneNode* pointer, u32 newspacing)
{pointer->SetSpacing(newspacing);}
IRRLICHT_C_API void CGridSceneNode_SetSize(CGridSceneNode* pointer, u32 newsize)
{pointer->SetSize(newsize);}
IRRLICHT_C_API void CGridSceneNode_SetGridColor(CGridSceneNode* pointer, const video::SColor& newcolor)
{pointer->SetGridColor(newcolor);}
IRRLICHT_C_API void CGridSceneNode_SetAccentlineOffset(CGridSceneNode* pointer, u32 newoffset)
{pointer->SetAccentlineOffset(newoffset);}
IRRLICHT_C_API void CGridSceneNode_SetAccentlineColor(CGridSceneNode* pointer, const video::SColor& newcolor)
{pointer->SetAccentlineColor(newcolor);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineActive(CGridSceneNode* pointer, bool active)
{pointer->SetAxisLineActive(active);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineXColor(CGridSceneNode* pointer, const video::SColor& XLine)
{pointer->SetAxisLineXColor(XLine);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineZColor(CGridSceneNode* pointer, const video::SColor& ZLine)
{pointer->SetAxisLineZColor(ZLine);}
IRRLICHT_C_API void CGridSceneNode_SetMaterial(CGridSceneNode* pointer, video::SMaterial* newMaterial)
{pointer->SetMaterial(*newMaterial);}

#ifdef __cplusplus
}
#endif

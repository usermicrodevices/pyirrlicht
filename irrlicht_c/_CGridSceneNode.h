// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#include "CGridSceneNode.h"

#ifdef __cplusplus
extern "C" {
#endif

//================= CGridSceneNode
IRRLICHT_C_API const std::shared_ptr<CGridSceneNode>& CGridSceneNode_ctor(ISceneNode* parent, ISceneManager* smgr, s32 id = -1, u32 spacing = 8, u32 size = 1024, const video::SColor& gridcolor = video::SColor(255,128,128,128), u32 accentlineoffset = 8, const video::SColor& accentgridcolor = video::SColor(255,192,192,192), bool axislinestate = false)
{return std::make_shared<CGridSceneNode>(parent, smgr, id, spacing, size, gridcolor, accentlineoffset, accentgridcolor, axislinestate);}
IRRLICHT_C_API void CGridSceneNode_delete(const std::shared_ptr<CGridSceneNode>& pointer){/*if(pointer)delete pointer;*/}
IRRLICHT_C_API const std::shared_ptr<CGridSceneNode>& CGridSceneNode_clone(const std::shared_ptr<CGridSceneNode>& pointer, ISceneNode* newParent = 0, ISceneManager* newSceneManager = 0)
{return std::shared_ptr<CGridSceneNode>(pointer->clone(newParent, newSceneManager));}
IRRLICHT_C_API void CGridSceneNode_OnRegisterSceneNode(const std::shared_ptr<CGridSceneNode>& pointer)
{pointer->OnRegisterSceneNode();}
IRRLICHT_C_API void CGridSceneNode_render(const std::shared_ptr<CGridSceneNode>& pointer)
{pointer->render();}
IRRLICHT_C_API const core::aabbox3d<f32>& CGridSceneNode_getBoundingBox(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->getBoundingBox();}
IRRLICHT_C_API u32 CGridSceneNode_getMaterialCount(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->getMaterialCount();}
IRRLICHT_C_API video::SMaterial& CGridSceneNode_getMaterial(const std::shared_ptr<CGridSceneNode>& pointer, u32 i)
{return pointer->getMaterial(i);}
IRRLICHT_C_API void CGridSceneNode_RegenerateGrid(const std::shared_ptr<CGridSceneNode>& pointer)
{pointer->RegenerateGrid();}
IRRLICHT_C_API u32 CGridSceneNode_GetSpacing(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetSpacing();}
IRRLICHT_C_API u32 CGridSceneNode_GetSize(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetSize();}
IRRLICHT_C_API const video::SColor CGridSceneNode_GetGridColor(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetGridColor();}
IRRLICHT_C_API u32 CGridSceneNode_GetAccentlineOffset(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetAccentlineOffset();}
IRRLICHT_C_API const video::SColor CGridSceneNode_GetAccentlineColor(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetAccentlineColor();}
IRRLICHT_C_API bool CGridSceneNode_AreAxisLineActive(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->AreAxisLineActive();}
IRRLICHT_C_API const video::SColor CGridSceneNode_GetAxisLineXColor(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetAxisLineXColor();}
IRRLICHT_C_API const video::SColor CGridSceneNode_GetAxisLineZColor(const std::shared_ptr<CGridSceneNode>& pointer)
{return pointer->GetAxisLineZColor();}
IRRLICHT_C_API void CGridSceneNode_SetSpacing(const std::shared_ptr<CGridSceneNode>& pointer, u32 newspacing)
{pointer->SetSpacing(newspacing);}
IRRLICHT_C_API void CGridSceneNode_SetSize(const std::shared_ptr<CGridSceneNode>& pointer, u32 newsize)
{pointer->SetSize(newsize);}
IRRLICHT_C_API void CGridSceneNode_SetGridColor(const std::shared_ptr<CGridSceneNode>& pointer, const video::SColor& newcolor)
{pointer->SetGridColor(newcolor);}
IRRLICHT_C_API void CGridSceneNode_SetAccentlineOffset(const std::shared_ptr<CGridSceneNode>& pointer, u32 newoffset)
{pointer->SetAccentlineOffset(newoffset);}
IRRLICHT_C_API void CGridSceneNode_SetAccentlineColor(const std::shared_ptr<CGridSceneNode>& pointer, const video::SColor& newcolor)
{pointer->SetAccentlineColor(newcolor);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineActive(const std::shared_ptr<CGridSceneNode>& pointer, bool active)
{pointer->SetAxisLineActive(active);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineXColor(const std::shared_ptr<CGridSceneNode>& pointer, const video::SColor& XLine)
{pointer->SetAxisLineXColor(XLine);}
IRRLICHT_C_API void CGridSceneNode_SetAxisLineZColor(const std::shared_ptr<CGridSceneNode>& pointer, const video::SColor& ZLine)
{pointer->SetAxisLineZColor(ZLine);}
IRRLICHT_C_API void CGridSceneNode_SetMaterial(const std::shared_ptr<CGridSceneNode>& pointer, video::SMaterial* newMaterial)
{pointer->SetMaterial(*newMaterial);}

#ifdef __cplusplus
}
#endif

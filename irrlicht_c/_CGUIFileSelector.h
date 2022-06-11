// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#include "CGUIFileSelector.h"

#ifdef __cplusplus
extern "C" {
#endif

//class CGUIFileSelector : public IGUIFileOpenDialog
IRRLICHT_C_API CGUIFileSelector* CGUIFileSelector_ctor(const wchar_t* title, IGUIEnvironment* environment, IGUIElement* parent, s32 id, E_FILESELECTOR_TYPE type)
{return new CGUIFileSelector(title, environment, parent, id, type);}
IRRLICHT_C_API void CGUIFileSelector_delete(CGUIFileSelector* pointer)
{delete pointer;}
IRRLICHT_C_API const wchar_t* CGUIFileSelector_getFileName(CGUIFileSelector* pointer)
{return pointer->getFileName();}
IRRLICHT_C_API const fschar_t* CGUIFileSelector_getDirectoryName(CGUIFileSelector* pointer)
{return pointer->getDirectoryName().c_str();}
IRRLICHT_C_API const wchar_t* CGUIFileSelector_getFileFilter(CGUIFileSelector* pointer)
{return pointer->getFileFilter().c_str();}
IRRLICHT_C_API E_FILESELECTOR_TYPE CGUIFileSelector_getDialogType(CGUIFileSelector* pointer)
{return pointer->getDialogType();}
IRRLICHT_C_API void CGUIFileSelector_addFileFilter(CGUIFileSelector* pointer, wchar_t* name, wchar_t* ext, video::ITexture* texture)
{pointer->addFileFilter(name, ext, texture);}
IRRLICHT_C_API void CGUIFileSelector_setCustomFileIcon(CGUIFileSelector* pointer, video::ITexture* texture)
{pointer->setCustomFileIcon(texture);}
IRRLICHT_C_API void CGUIFileSelector_setCustomDirectoryIcon(CGUIFileSelector* pointer, video::ITexture* texture)
{pointer->setCustomDirectoryIcon(texture);}
IRRLICHT_C_API void CGUIFileSelector_setDirectoryChoosable(CGUIFileSelector* pointer, bool choosable)
{pointer->setDirectoryChoosable(choosable);}

#ifdef __cplusplus
}
#endif

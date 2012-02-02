// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIFileOpenDialog
IRRLICHT_C_API IGUIFileOpenDialog* IGUIFileOpenDialog_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIFileOpenDialog*)new IGUIElement(EGUIET_FILE_OPEN_DIALOG, environment, parent, id, *rectangle);}
IRRLICHT_C_API const wchar_t* IGUIFileOpenDialog_getFileName(IGUIFileOpenDialog* pointer)
{return pointer->getFileName();}
IRRLICHT_C_API const fschar_t* IGUIFileOpenDialog_getDirectoryName(IGUIFileOpenDialog* pointer)
{return pointer->getDirectoryName().c_str();}

#ifdef __cplusplus
}
#endif

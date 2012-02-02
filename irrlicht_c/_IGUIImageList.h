// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIImageList
IRRLICHT_C_API void IGUIImageList_draw(IGUIImageList* pointer, s32 index, const core::position2d<s32>& destPos, const core::rect<s32>* clip = 0)
{pointer->draw(index, destPos, clip);}
IRRLICHT_C_API s32 IGUIImageList_getImageCount(IGUIImageList* pointer)
{return pointer->getImageCount();}
IRRLICHT_C_API core::dimension2d<s32>* IGUIImageList_getImageSize(IGUIImageList* pointer)
{return &pointer->getImageSize();}

#ifdef __cplusplus
}
#endif

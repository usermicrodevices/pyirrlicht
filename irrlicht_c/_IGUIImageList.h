// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIImageList
IRRLICHT_C_API void IGUIImageList_draw(IGUIImageList* pointer, s32 index, const core::position2d<s32>& destPos, const core::rect<s32>* clip = 0)
{pointer->draw(index, destPos, clip);}
IRRLICHT_C_API s32 IGUIImageList_getImageCount(IGUIImageList* pointer)
{return pointer->getImageCount();}
IRRLICHT_C_API const core::dimension2d<s32> IGUIImageList_getImageSize(IGUIImageList* pointer)
{return pointer->getImageSize();}

#ifdef __cplusplus
}
#endif

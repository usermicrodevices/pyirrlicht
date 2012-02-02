// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IVideoModeList
IRRLICHT_C_API s32 IVideoModeList_getVideoModeCount(IVideoModeList* pointer){return pointer->getVideoModeCount();}
IRRLICHT_C_API const dimension2d<u32>& IVideoModeList_getVideoModeResolution(IVideoModeList* pointer, s32 modeNumber){return (const dimension2d<u32>&)pointer->getVideoModeResolution(modeNumber);}
IRRLICHT_C_API const dimension2d<u32>& IVideoModeList_getVideoModeResolution2(IVideoModeList* pointer, const core::dimension2d<u32>& minSize, const core::dimension2d<u32>& maxSize){return (const dimension2d<u32>&)pointer->getVideoModeResolution(minSize, maxSize);}
IRRLICHT_C_API s32 IVideoModeList_getVideoModeDepth(IVideoModeList* pointer, s32 modeNumber){return pointer->getVideoModeDepth(modeNumber);}
IRRLICHT_C_API const dimension2d<u32>& IVideoModeList_getDesktopResolution(IVideoModeList* pointer){return pointer->getDesktopResolution();}
IRRLICHT_C_API s32 IVideoModeList_getDesktopDepth(IVideoModeList* pointer){return pointer->getDesktopDepth();}

#ifdef __cplusplus
}
#endif

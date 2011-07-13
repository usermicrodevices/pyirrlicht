// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SIrrlichtCreationParameters
IRRLICHT_C_API SIrrlichtCreationParameters* SIrrlichtCreationParameters_ctor()
{return new SIrrlichtCreationParameters();}
//IRRLICHT_C_API SIrrlichtCreationParameters* SIrrlichtCreationParameters_ctor2(SIrrlichtCreationParameters* other)
//{return new SIrrlichtCreationParameters(*other);}

IRRLICHT_C_API E_DEVICE_TYPE SIrrlichtCreationParameters_get_DeviceType(SIrrlichtCreationParameters* pointer){return pointer->DeviceType;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_DeviceType(SIrrlichtCreationParameters* pointer, E_DEVICE_TYPE value){pointer->DeviceType = value;}

IRRLICHT_C_API video::E_DRIVER_TYPE SIrrlichtCreationParameters_get_DriverType(SIrrlichtCreationParameters* pointer){return pointer->DriverType;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_DriverType(SIrrlichtCreationParameters* pointer, video::E_DRIVER_TYPE value){pointer->DriverType = value;}

IRRLICHT_C_API core::dimension2d<u32>* SIrrlichtCreationParameters_get_WindowSize(SIrrlichtCreationParameters* pointer){return &pointer->WindowSize;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_WindowSize(SIrrlichtCreationParameters* pointer, core::dimension2d<u32>* value){pointer->WindowSize = *value;}

IRRLICHT_C_API u8 SIrrlichtCreationParameters_get_Bits(SIrrlichtCreationParameters* pointer){return pointer->Bits;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Bits(SIrrlichtCreationParameters* pointer, u8 value){pointer->Bits = value;}

IRRLICHT_C_API u8 SIrrlichtCreationParameters_get_ZBufferBits(SIrrlichtCreationParameters* pointer){return pointer->ZBufferBits;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_ZBufferBits(SIrrlichtCreationParameters* pointer, u8 value){pointer->ZBufferBits = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_Fullscreen(SIrrlichtCreationParameters* pointer){return pointer->Fullscreen;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Fullscreen(SIrrlichtCreationParameters* pointer, bool value){pointer->Fullscreen = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_Stencilbuffer(SIrrlichtCreationParameters* pointer){return pointer->Stencilbuffer;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Stencilbuffer(SIrrlichtCreationParameters* pointer, bool value){pointer->Stencilbuffer = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_Vsync(SIrrlichtCreationParameters* pointer){return pointer->Vsync;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Vsync(SIrrlichtCreationParameters* pointer, bool value){pointer->Vsync = value;}

IRRLICHT_C_API u8 SIrrlichtCreationParameters_get_AntiAlias(SIrrlichtCreationParameters* pointer){return pointer->AntiAlias;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_AntiAlias(SIrrlichtCreationParameters* pointer, u8 value){pointer->AntiAlias = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_WithAlphaChannel(SIrrlichtCreationParameters* pointer){return pointer->WithAlphaChannel;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_WithAlphaChannel(SIrrlichtCreationParameters* pointer, bool value){pointer->WithAlphaChannel = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_Doublebuffer(SIrrlichtCreationParameters* pointer){return pointer->Doublebuffer;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Doublebuffer(SIrrlichtCreationParameters* pointer, bool value){pointer->Doublebuffer = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_IgnoreInput(SIrrlichtCreationParameters* pointer){return pointer->IgnoreInput;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_IgnoreInput(SIrrlichtCreationParameters* pointer, bool value){pointer->IgnoreInput = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_Stereobuffer(SIrrlichtCreationParameters* pointer){return pointer->Stereobuffer;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_Stereobuffer(SIrrlichtCreationParameters* pointer, bool value){pointer->Stereobuffer = value;}

IRRLICHT_C_API bool SIrrlichtCreationParameters_get_HighPrecisionFPU(SIrrlichtCreationParameters* pointer){return pointer->HighPrecisionFPU;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_HighPrecisionFPU(SIrrlichtCreationParameters* pointer, bool value){pointer->HighPrecisionFPU = value;}

IRRLICHT_C_API IEventReceiver* SIrrlichtCreationParameters_get_EventReceiver(SIrrlichtCreationParameters* pointer){return pointer->EventReceiver;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_EventReceiver(SIrrlichtCreationParameters* pointer, IEventReceiver* value){pointer->EventReceiver = value;}

IRRLICHT_C_API void* SIrrlichtCreationParameters_get_WindowId(SIrrlichtCreationParameters* pointer){return pointer->WindowId;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_WindowId(SIrrlichtCreationParameters* pointer, void* value){pointer->WindowId = value;}

IRRLICHT_C_API ELOG_LEVEL SIrrlichtCreationParameters_get_LoggingLevel(SIrrlichtCreationParameters* pointer){return pointer->LoggingLevel;}
IRRLICHT_C_API void SIrrlichtCreationParameters_set_LoggingLevel(SIrrlichtCreationParameters* pointer, ELOG_LEVEL value){pointer->LoggingLevel = value;}

IRRLICHT_C_API const c8* const SIrrlichtCreationParameters_get_SDK_version_do_not_use(SIrrlichtCreationParameters* pointer){return pointer->SDK_version_do_not_use;}
//IRRLICHT_C_API void SIrrlichtCreationParameters_set_SDK_version_do_not_use(SIrrlichtCreationParameters* pointer, const c8* const value){printf("DO NOT USE THIS METHOD")/*pointer->SDK_version_do_not_use = value*/;}

#ifdef __cplusplus
}
#endif

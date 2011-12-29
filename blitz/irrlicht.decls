; library declarations for Irrlicht Blitz3D wrapper
; original idea by Atulos, many thanks him
; programming Maxim Kolosov

.lib "irrlicht_c_stdcall.dll"

tool_char_to_wchar% (value$) : "_tool_char_to_wchar@4"
tool_get_stdin% () : "_tool_get_stdin@0"
tool_get_stdout% () : "_tool_get_stdout@0"
tool_close_streams% () : "_tool_close_streams@0"
tool_close_stream% (stream%) : "_tool_close_stream@4"
tool_redirect_stdout_to_file% (file_name$, mode$) : "_tool_redirect_stdout_to_file@8"

dimension2du_ctor2% (w%, h%) : "_dimension2du_ctor2@8"

SColor_ctor2% (a%, r%, g%, b%) : "_SColor_ctor2@16"

vector3df_ctor2% (x#, y#, z#) : "_vector3df_ctor2@12"

recti_ctor2% (x%, y%, x2%, y2%) : "_recti_ctor2@16"

SExposedVideoData_ctor2% (Window%) : "_SExposedVideoData_ctor2@4"

SIrrlichtCreationParameters_ctor% () : "_SIrrlichtCreationParameters_ctor@0"
SIrrlichtCreationParameters_set_DeviceType (pointer%, value%) : "_SIrrlichtCreationParameters_set_DeviceType@8"
SIrrlichtCreationParameters_set_DriverType (pointer%, value%) : "_SIrrlichtCreationParameters_set_DriverType@8"
SIrrlichtCreationParameters_set_WindowSize (pointer%, value%) : "_SIrrlichtCreationParameters_set_WindowSize@8"
SIrrlichtCreationParameters_set_Bits (pointer%, value%) : "_SIrrlichtCreationParameters_set_Bits@8"
SIrrlichtCreationParameters_set_ZBufferBits (pointer%, value%) : "_SIrrlichtCreationParameters_set_ZBufferBits@8"
SIrrlichtCreationParameters_set_Fullscreen (pointer%, value%) : "_SIrrlichtCreationParameters_set_Fullscreen@8"
SIrrlichtCreationParameters_set_Stencilbuffer (pointer%, value%) : "_SIrrlichtCreationParameters_set_Stencilbuffer@8"
SIrrlichtCreationParameters_set_Vsync (pointer%, value%) : "_SIrrlichtCreationParameters_set_Vsync@8"
SIrrlichtCreationParameters_set_AntiAlias (pointer%, value%) : "_SIrrlichtCreationParameters_set_AntiAlias@8"
SIrrlichtCreationParameters_set_WithAlphaChannel (pointer%, value%) : "_SIrrlichtCreationParameters_set_WithAlphaChannel@8"
SIrrlichtCreationParameters_set_Doublebuffer (pointer%, value%) : "_SIrrlichtCreationParameters_set_Doublebuffer@8"
SIrrlichtCreationParameters_set_IgnoreInput (pointer%, value%) : "_SIrrlichtCreationParameters_set_IgnoreInput@8"
SIrrlichtCreationParameters_set_Stereobuffer (pointer%, value%) : "_SIrrlichtCreationParameters_set_Stereobuffer@8"
SIrrlichtCreationParameters_set_HighPrecisionFPU (pointer%, value%) : "_SIrrlichtCreationParameters_set_HighPrecisionFPU@8"
SIrrlichtCreationParameters_set_EventReceiver (pointer%, value%) : "_SIrrlichtCreationParameters_set_EventReceiver@8"
SIrrlichtCreationParameters_set_WindowId (pointer%, value%) : "_SIrrlichtCreationParameters_set_WindowId@8"
SIrrlichtCreationParameters_set_LoggingLevel (pointer%, value%) : "_SIrrlichtCreationParameters_set_LoggingLevel@8"

IEventReceiver_ctor2% (event_method%) : "_IEventReceiver_ctor2@4"

ISceneNode_setMaterialFlag (pointer%, flag%, newvalue%) : "_ISceneNode_setMaterialFlag@12"
ISceneNode_setMaterialTexture (pointer%, textureLayer%, texture%) : "_ISceneNode_setMaterialTexture@12"

IAnimatedMeshSceneNode_setMD2Animation1 (pointer%, flag%) : "_IAnimatedMeshSceneNode_setMD2Animation1@8"

ISceneManager_getMesh% (pointer%, path$) : "_ISceneManager_getMesh@8"
ISceneManager_addAnimatedMeshSceneNode% (pointer%, mesh%, parent%, id%, position%, rotation%, scale%, alsoAddIfMeshPointerZero%) : "_ISceneManager_addAnimatedMeshSceneNode@32"
ISceneManager_addCameraSceneNode% (pointer%, parent%, position%, lookat%, id%) : "_ISceneManager_addCameraSceneNode@20"
ISceneManager_drawAll (pointer%) : "_ISceneManager_drawAll@4"

IGUIFont_draw (pointer%, text%, position%, color%, hcenter%, vcenter%, clip%) : "_IGUIFont_draw@28"

IGUIEnvironment_drawAll (pointer%) : "_IGUIEnvironment_drawAll@4"
IGUIEnvironment_clear (pointer%) : "_IGUIEnvironment_clear@4"
IGUIEnvironment_getFont% (pointer%, filename$) : "_IGUIEnvironment_getFont@8"
IGUIEnvironment_getBuiltInFont% (pointer%) : "_IGUIEnvironment_getBuiltInFont@4"
IGUIEnvironment_addStaticText% (pointer%, text%, rectangle%, border%, wordWrap%, parent%, id%, fillBackground%) : "_IGUIEnvironment_addStaticText@32"

IVideoDriver_beginScene% (pointer%, backBuffer%, zBuffer%, color%, videoData%, sourceRect%) : "_IVideoDriver_beginScene@6"
IVideoDriver_beginSceneDefault% (pointer%, backBuffer%, zBuffer%, color%) : "_IVideoDriver_beginSceneDefault@16"
IVideoDriver_endScene% (pointer%) : "_IVideoDriver_endScene@4"
IVideoDriver_getTexture1% (pointer%, filename$) : "_IVideoDriver_getTexture1@8"

IrrlichtDevice_createDevice% (deviceType%, windowSize%, bits%, fullscreen%, stencilbuffer%, vsync%, receiver%) : "_IrrlichtDevice_createDevice@28"
IrrlichtDevice_createDevice2% (deviceType%, windowSize%, bits%, fullscreen%, stencilbuffer%, vsync%, create_receiver%) : "_IrrlichtDevice_createDevice2@28"
IrrlichtDevice_createDeviceEx% (parameters%) : "_IrrlichtDevice_createDeviceEx@4"
IrrlichtDevice_createDeviceEx_% (parameters*) : "_IrrlichtDevice_createDeviceEx@4"
IrrlichtDevice_run% (pointer%) : "_IrrlichtDevice_run@4"
IrrlichtDevice_yield (pointer%) : "_IrrlichtDevice_yield@4"
IrrlichtDevice_sleep (pointer%, timeMs%, pauseTimer%) : "_IrrlichtDevice_sleep@12"
IrrlichtDevice_getVideoDriver% (pointer%) : "_IrrlichtDevice_getVideoDriver@4"
IrrlichtDevice_getSceneManager% (pointer%) : "_IrrlichtDevice_getSceneManager@4"
IrrlichtDevice_getGUIEnvironment% (pointer%) : "_IrrlichtDevice_getGUIEnvironment@4"
IrrlichtDevice_getCursorControl% (pointer%) : "_IrrlichtDevice_getCursorControl@4"
IrrlichtDevice_getLogger% (pointer%) : "_IrrlichtDevice_getLogger@4"
IrrlichtDevice_setWindowCaption (pointer%, text%) : "_IrrlichtDevice_setWindowCaption@8"
IrrlichtDevice_isWindowActive% (pointer%) : "_IrrlichtDevice_isWindowActive@4"
IrrlichtDevice_closeDevice (pointer%) : "_IrrlichtDevice_closeDevice@4"
IrrlichtDevice_getVersion$ (pointer%) : "_IrrlichtDevice_getVersion@4"
IrrlichtDevice_setResizable (pointer%, resize%) : "_IrrlichtDevice_setResizable@8"

;.lib "user32.dll"
;http://www.blitzmax.com/codearcs/codearcs.php?code=656
;GetActiveWindow%():"GetActiveWindow"

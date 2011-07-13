#include "const.inc"

Declare Function SColor_ctor1 CDECL Lib "irrlicht_c.dll" ALIAS "SColor_ctor1" () As DWORD
Declare Function SColor_ctor2 CDECL Lib "irrlicht_c.dll" ALIAS "SColor_ctor2" (ByVal a As WORD, ByVal r As WORD, ByVal g As WORD, ByVal b As WORD) As DWORD
Declare Function SColor_ctor3 CDECL Lib "irrlicht_c.dll" ALIAS "SColor_ctor3" (ByVal clr As WORD) As DWORD

Declare Function dimension2du_ctor1 CDECL Lib "irrlicht_c.dll" ALIAS "dimension2du_ctor1" () As DWORD
Declare Function dimension2du_ctor2 CDECL Lib "irrlicht_c.dll" ALIAS "dimension2du_ctor2" (ByVal w As WORD, ByVal h As WORD) As DWORD

Declare Function recti_ctor1 CDECL Lib "irrlicht_c.dll" ALIAS "recti_ctor1" () As DWORD

Declare Function vector3df_ctor2 CDECL Lib "irrlicht_c.dll" ALIAS "vector3df_ctor2" (ByVal x As SINGLE, ByVal y As SINGLE, ByVal z As SINGLE) As DWORD

Declare Sub ISceneNode_setMaterialFlag CDECL Lib "irrlicht_c.dll" ALIAS "ISceneNode_setMaterialFlag" (ByVal pointer As DWORD, ByVal flag As INTEGER, ByVal newvalue As BYTE)
Declare Sub ISceneNode_setMaterialTexture CDECL Lib "irrlicht_c.dll" ALIAS "ISceneNode_setMaterialTexture" (ByVal pointer As DWORD, ByVal textureLayer As WORD, ByVal texture As DWORD)

Declare Function IAnimatedMeshSceneNode_setMD2Animation1 CDECL Lib "irrlicht_c.dll" ALIAS "IAnimatedMeshSceneNode_setMD2Animation1" (ByVal pointer As DWORD, ByVal anim As INTEGER) As BYTE

Declare Function IVideoDriver_beginScene CDECL Lib "irrlicht_c.dll" ALIAS "IVideoDriver_beginScene" (ByVal pointer As DWORD, ByVal backBuffer As BYTE, ByVal zBuffer As BYTE, ByVal scolor As DWORD, ByVal videoData As DWORD, ByVal sourceRect As DWORD) As BYTE
Declare Function IVideoDriver_beginSceneDefault CDECL Lib "irrlicht_c.dll" ALIAS "IVideoDriver_beginSceneDefault" (ByVal pointer As DWORD, ByVal backBuffer As BYTE, ByVal zBuffer As BYTE, ByVal scolor As DWORD) As BYTE
Declare Function IVideoDriver_endScene CDECL Lib "irrlicht_c.dll" ALIAS "IVideoDriver_endScene" (ByVal pointer As DWORD) As BYTE
Declare Function IVideoDriver_getTexture1 CDECL Lib "irrlicht_c.dll" ALIAS "IVideoDriver_getTexture1" (ByVal pointer As DWORD, ByVal filename As ASCIIZ) As DWORD
Declare Function IVideoDriver_getName CDECL Lib "irrlicht_c.dll" ALIAS "IVideoDriver_getName" (ByVal pointer As DWORD) As STRING

Declare Function ISceneManager_getMesh CDECL Lib "irrlicht_c.dll" ALIAS "ISceneManager_getMesh" (ByVal pointer As DWORD, ByVal path As ASCIIZ) As DWORD
Declare Function ISceneManager_addAnimatedMeshSceneNode CDECL Lib "irrlicht_c.dll" ALIAS "ISceneManager_addAnimatedMeshSceneNode" (ByVal pointer As DWORD, ByVal mesh As DWORD, ByVal parent As DWORD, ByVal id As INTEGER, ByVal position As DWORD, ByVal rotation As DWORD, ByVal scale As DWORD, ByVal alsoAddIfMeshPointerZero As BYTE) As DWORD
Declare Function ISceneManager_addCameraSceneNode CDECL Lib "irrlicht_c.dll" ALIAS "ISceneManager_addCameraSceneNode" (ByVal pointer As DWORD, ByVal parent As DWORD, ByVal position As DWORD, ByVal lookat As DWORD, ByVal id As INTEGER) As DWORD

Declare Sub ISceneManager_drawAll CDECL Lib "irrlicht_c.dll" ALIAS "ISceneManager_drawAll" (ByVal pointer As DWORD)

Declare Sub IGUIEnvironment_drawAll CDECL Lib "irrlicht_c.dll" ALIAS "IGUIEnvironment_drawAll" (ByVal pointer As DWORD)

Declare Function IrrlichtDevice_createDevice CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_createDevice" (ByVal deviceType As INTEGER, ByVal windowSize As DWORD, ByVal bits As WORD, ByVal fullscreen As BYTE, ByVal stencilbuffer As BYTE, ByVal vsync As BYTE, ByVal receiver As DWORD) As DWORD
Declare Function IrrlichtDevice_createDevice2 CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_createDevice2" (ByVal deviceType As INTEGER, ByVal windowSize As DWORD, ByVal bits As WORD, ByVal fullscreen As BYTE, ByVal stencilbuffer As BYTE, ByVal vsync As BYTE, ByVal create_receiver As BYTE) As DWORD
Declare Function IrrlichtDevice_createDeviceEx CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_createDeviceEx" (ByVal parameters As DWORD) As DWORD
Declare Function IrrlichtDevice_run CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_run" (ByVal pointer As DWORD) As BYTE
Declare Sub IrrlichtDevice_yield CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_yield" (ByVal pointer As DWORD)
Declare Sub IrrlichtDevice_sleep CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_sleep" (ByVal pointer As DWORD, ByVal timeMs As WORD, ByVal pauseTimer As BYTE)
Declare Function IrrlichtDevice_getVideoDriver CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getVideoDriver" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getFileSystem CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getFileSystem" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getGUIEnvironment CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getGUIEnvironment" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getSceneManager CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getSceneManager" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getCursorControl CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getCursorControl" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getLogger CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getLogger" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getVideoModeList CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getVideoModeList" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getOSOperator CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getOSOperator" (ByVal pointer As DWORD) As DWORD
Declare Function IrrlichtDevice_getTimer CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getTimer" (ByVal pointer As DWORD) As DWORD
Declare Sub IrrlichtDevice_setWindowCaption CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_setWindowCaption" (ByVal pointer As DWORD, ByVal text As ASCIIZ)
Declare Function IrrlichtDevice_isWindowActive CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_isWindowActive" (ByVal pointer As DWORD) As BYTE
Declare Function IrrlichtDevice_isWindowFocused CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_isWindowFocused" (ByVal pointer As DWORD) As BYTE
Declare Function IrrlichtDevice_isWindowMinimized CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_isWindowMinimized" (ByVal pointer As DWORD) As BYTE
Declare Function IrrlichtDevice_isFullscreen CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_isFullscreen" (ByVal pointer As DWORD) As BYTE
Declare Function IrrlichtDevice_getColorFormat CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getColorFormat" (ByVal pointer As DWORD) As INTEGER
Declare Sub IrrlichtDevice_closeDevice CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_closeDevice" (ByVal pointer As DWORD)
Declare Function IrrlichtDevice_getVersion CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getVersion" (ByVal pointer As DWORD) As ASCIIZ
Declare Sub IrrlichtDevice_setEventReceiver CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_setEventReceiver" (ByVal pointer As DWORD, ByVal receiver As DWORD)
Declare Function IrrlichtDevice_getEventReceiver CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getEventReceiver" (ByVal pointer As DWORD) As DWORD
Declare Sub IrrlichtDevice_setInputReceivingSceneManager CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_setInputReceivingSceneManager" (ByVal pointer As DWORD, ByVal sceneManager As DWORD)
Declare Sub IrrlichtDevice_setResizable CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_setResizable" (ByVal pointer As DWORD, ByVal resize As BYTE)
Declare Sub IrrlichtDevice_minimizeWindow CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_minimizeWindow" (ByVal pointer As DWORD)
Declare Sub IrrlichtDevice_maximizeWindow CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_maximizeWindow" (ByVal pointer As DWORD)
Declare Sub IrrlichtDevice_restoreWindow CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_restoreWindow" (ByVal pointer As DWORD)
Declare Function IrrlichtDevice_setGammaRamp CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_setGammaRamp" (ByVal pointer As DWORD, ByVal red As SINGLE, ByVal green As SINGLE, ByVal blue As SINGLE, ByVal relativebrightness As SINGLE, ByVal relativecontrast As SINGLE) As BYTE
Declare Function IrrlichtDevice_getGammaRamp CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getGammaRamp" (ByVal pointer As DWORD, ByRef red As SINGLE, ByRef green As SINGLE, ByRef blue As SINGLE, ByRef relativebrightness As SINGLE, ByRef relativecontrast As SINGLE) As BYTE
Declare Function IrrlichtDevice_getType CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_getType" (ByVal pointer As DWORD) As INTEGER
Declare Function IrrlichtDevice_isDriverSupported CDECL Lib "irrlicht_c.dll" ALIAS "IrrlichtDevice_isDriverSupported" (ByVal pointer As DWORD, ByVal driver As INTEGER) As BYTE

Declare Function SExposedVideoData_ctor1 CDECL Lib "irrlicht_c.dll" ALIAS "SExposedVideoData_ctor1" () As DWORD

Declare Function SIrrlichtCreationParameters_ctor CDECL Lib "irrlicht_c.dll" ALIAS "SIrrlichtCreationParameters_ctor" () As DWORD

Declare Function MainLoop_ctor CDECL Lib "irrlicht_c.dll" ALIAS "MainLoop_ctor" (ByVal device As DWORD, ByVal driver As DWORD, ByVal smgr As DWORD, ByVal guienv As DWORD, ByVal backBuffer As BYTE, ByVal zBuffer As BYTE, ByVal scolor As DWORD, ByVal videoData As DWORD, ByVal sourceRect As DWORD, ByVal time_ms As WORD, ByVal pause_timer As Byte) As DWORD
Function MainLoop_Constructor(device As DWORD, driver As DWORD, optional smgr As DWORD = $NUL, guienv As DWORD = $NUL, backBuffer As BYTE = true, zBuffer As BYTE = true, scolor As DWORD = $NUL, videoData As DWORD = $NUL, sourceRect As DWORD = $NUL, time_ms As WORD = 0, pause_timer As Byte = false)
	If Not scolor Then
		scolor = SColor_ctor1()
	End If
	Return MainLoop_ctor(device, driver, smgr, guienv, backBuffer, zBuffer, scolor, videoData, sourceRect, time_ms, pause_timer)
End Function
Declare Sub MainLoop_start CDECL Lib "irrlicht_c.dll" ALIAS "MainLoop_start" (ByVal pointer As DWORD)
Declare Sub MainLoop_stop CDECL Lib "irrlicht_c.dll" ALIAS "MainLoop_stop" (ByVal pointer As DWORD)

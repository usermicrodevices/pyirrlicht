#inclib "../irrlicht_c"

#define FALSE 0
#define TRUE 1

Enum E_DRIVER_TYPE
	EDT_NULL = 0
	EDT_SOFTWARE
	EDT_BURNINGSVIDEO
	EDT_DIRECT3D8
	EDT_DIRECT3D9
	EDT_OPENGL
End Enum

Extern "c"

Declare Sub delete_pointer Alias "delete_pointer" (ByVal _pointer_ As Any Ptr)

Declare Function SExposedVideoData_constructor1 Alias "SExposedVideoData_constructor1" () As Any Ptr

Declare Function dimension2du_ctor1 Alias "dimension2du_ctor1" () As Any Ptr
Declare Function dimension2du_ctor2 Alias "dimension2du_ctor2" (ByVal x As UInteger, ByVal y As UInteger) As Any Ptr

Declare Function SColor_ctor1 Alias "SColor_ctor1" () As Any Ptr
Declare Function SColor_ctor2 Alias "SColor_ctor2" (ByVal a As UInteger, ByVal r As UInteger, ByVal g As UInteger, ByVal b As UInteger) As Any Ptr

Declare Function IVideoDriver_beginScene Alias "IVideoDriver_beginScene" (ByVal _pointer_ As Any Ptr, ByVal backBuffer As UByte = true, ByVal zBuffer As UByte = true, ByVal _color_ As Any Ptr = 0, ByVal videoData As Any Ptr = 0, ByVal sourceRect As Any Ptr = 0) As UByte
Declare Function IVideoDriver_beginSceneDefault Alias "IVideoDriver_beginSceneDefault" (ByVal _pointer_ As Any Ptr, ByVal backBuffer As UByte = true, ByVal zBuffer As UByte = true, ByVal _color_ As Any Ptr = 0) As UByte
Declare Function IVideoDriver_endScene Alias "IVideoDriver_endScene" (ByVal _pointer_ As Any Ptr) As UByte

declare function IrrlichtDevice_createDevice alias "IrrlichtDevice_createDevice" (byval deviceType as E_DRIVER_TYPE = EDT_NULL, byval windowSize as any ptr = 0, byval bits as uinteger = 16, ByVal fullscreen As UByte = False, ByVal stencilbuffer As UByte = False, ByVal vsync As UByte = False, ByVal receiver As any ptr = 0) As any ptr
Declare Function IrrlichtDevice_run Alias "IrrlichtDevice_run" (ByVal _pointer_ As Any Ptr) As UByte
Declare Function IrrlichtDevice_getVideoDriver Alias "IrrlichtDevice_getVideoDriver" (ByVal _pointer_ As Any Ptr) As Any Ptr

End Extern


dim t as long = 0
'~ dim video_data as any ptr = SExposedVideoData_constructor1()
dim scolor as any ptr = SColor_ctor2(255, 100, 100, 140)
dim wsize as any ptr = dimension2du_ctor2(320, 240)
Dim device As any ptr = IrrlichtDevice_createDevice(EDT_OPENGL, wsize)
Dim driver As any ptr = IrrlichtDevice_getVideoDriver(device)
while IrrlichtDevice_run(device)
	'~ if IVideoDriver_beginScene(driver, True, True, scolor, video_data) then
	if IVideoDriver_beginSceneDefault(driver, True, True, scolor) then
		IVideoDriver_endScene(driver)
	end if
	print "device pointer "; device; " times "; t
	sleep 500
	t += 1
wend

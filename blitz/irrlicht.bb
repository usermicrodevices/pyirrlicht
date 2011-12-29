; Replaces Blitz3D to Irrlicht functions
; original idea by Atulos, many thanks him
; main part this is replaces Blitz3D internal functions, like Graphics3D (again thanks Atulos)
; programming Maxim Kolosov

Include "constant.bb"

Type D3D8
	Field D3D8
	Field D3DDev8
	Field HWnd
End Type
Type D3D9
	Field D3D9
	Field D3DDev9
	Field HWnd
End Type
Type OpenGLWin32
	Field HDc
	Field HRc
	Field HWnd
End Type
Type OpenGLLinux
	Field X11Display
	Field X11Context
	Field X11Window
End Type
Type SExposedVideoData 
	Field c_pointer
	Field d3d8.D3D8
	Field d3d9.D3D9
	Field openglwin32.OpenGLWin32
	Field opengllinux.OpenGLLinux
End Type

Type SIrrlichtCreationParameters
	Field DeviceType
	Field DriverType
	Field WindowSize
	Field Bits
	Field ZBufferBits
	Field Fullscreen
	Field Stencilbuffer
	Field Vsync
	Field AntiAlias
	Field WithAlphaChannel
	Field Doublebuffer
	Field IgnoreInput
	Field Stereobuffer
	Field HighPrecisionFPU
	Field EventReceiver
	Field WindowId
	Field LoggingLevel
	Field SDK_version_do_not_use$
End Type

Type dimension2du 
	Field c_pointer
End Type

Type IrrlichtDevice 
	Field c_pointer
End Type

Type RECT
	Field leftRect
	Field topRect
	Field rightRect
	Field bottomRect
End Type

Global irrlicht_device%, global_font%, irrlicht_creation_parameters% = SIrrlichtCreationParameters_ctor()

Function WBuffer (enable%)
	SIrrlichtCreationParameters_set_Doublebuffer irrlicht_creation_parameters, enable
End Function

Function AntiAlias (enable%)
	SIrrlichtCreationParameters_set_AntiAlias irrlicht_creation_parameters, enable
End Function

Function Graphics (x%, y%, depth%, mode%, driver_type% = EDT_DIRECT3D9)
	;window_handle% = SystemProperty("AppHWND")
	window_handle% = GetActiveWindow()
	rect.RECT = New RECT
	GetWindowRect GetDesktopWindow(), rect
	posx% = rect\rightRect/2-x/2
	If posx < 0
		posx = 0
	EndIf
	posy% = rect\bottomRect/2-y/2
	If posy < 0
		posy = 0
	EndIf
	MoveWindow window_handle, posx, posy, x, y, False
	;window_size% = dimension2du_ctor2(x, y)
	;irrlicht_creation_parameters = SIrrlichtCreationParameters_ctor()
	SIrrlichtCreationParameters_set_DriverType irrlicht_creation_parameters, driver_type
	SIrrlichtCreationParameters_set_WindowId irrlicht_creation_parameters, window_handle
	;SIrrlichtCreationParameters_set_WindowSize irrlicht_creation_parameters, window_size
	SIrrlichtCreationParameters_set_Bits irrlicht_creation_parameters, depth
	SIrrlichtCreationParameters_set_ZBufferBits irrlicht_creation_parameters, depth
	If mode <> 1
		SIrrlichtCreationParameters_set_Fullscreen irrlicht_creation_parameters, False
	Else
		SIrrlichtCreationParameters_set_Fullscreen irrlicht_creation_parameters, True
	EndIf
	SIrrlichtCreationParameters_set_Stencilbuffer irrlicht_creation_parameters, True
	SIrrlichtCreationParameters_set_Vsync irrlicht_creation_parameters, True
	SIrrlichtCreationParameters_set_IgnoreInput irrlicht_creation_parameters, True
	irrlicht_device = IrrlichtDevice_createDeviceEx(irrlicht_creation_parameters)
	global_font = IGUIEnvironment_getBuiltInFont(IrrlichtDevice_getGUIEnvironment(irrlicht_device))
End Function

Function Graphics3D (x%, y%, depth%, mode%, driver_type% = EDT_DIRECT3D9)
	Graphics x, y, depth, mode, driver_type
End Function

Function End ()
	IrrlichtDevice_closeDevice irrlicht_device
End Function

Function Text (x%, y%, string_value$, center_x% = False, center_y% = False)
	If global_font
		IGUIFont_draw global_font, tool_char_to_wchar(string_value), recti_ctor2(x, y, 100, 20), SColor_ctor2(255, 255, 255, 255), center_x, center_y, 0
	EndIf
End Function

Include "irrlicht.bb"

irr_log_stream = tool_redirect_stdout_to_file("irr_log.txt", "w")

;mesh_path = tool_char_to_wchar("media/sydney.md2")
mesh_path$ = "media/sydney.md2"
texture_path$ = "media/sydney.bmp"

;log_file = WriteFile("log.txt")
;WriteLine(log_file, "Irrlicht test application")

;Graphics3D 640,480,0,2
;SetFont LoadFont("Tahoma",30)

;AppTitle "Irrlicht test window"
;hWnd = FindWindow("Blitz Runtime Class", title$)
hWnd = GetActiveWindow()
Print "GetActiveWindow " + hWnd
;hWnd = SystemProperty("AppHWND")
;Print "SystemProperty " + hWnd

window_size = dimension2du_ctor2(800, 600)

Function event_function%(event_pointer%)
	DebugLog "event message from event_function"
	Return False
End Function
Global evt%
event_function_pointer = FunctionPointer()
	Goto skip
	res% = event_function(evt)
	.skip
event_receiver = IEventReceiver_ctor2(event_function_pointer)

parameters = SIrrlichtCreationParameters_ctor()
SIrrlichtCreationParameters_set_DriverType parameters, EDT_DIRECT3D9
SIrrlichtCreationParameters_set_WindowId parameters, hWnd
SIrrlichtCreationParameters_set_WindowSize parameters, window_size
SIrrlichtCreationParameters_set_EventReceiver parameters, event_receiver

;Local parameters.SIrrlichtCreationParameters = New SIrrlichtCreationParameters
;parameters\DriverType = EDT_DIRECT3D9
;parameters\WindowId = hWnd
;parameters\WindowSize = window_size

;device = IrrlichtDevice_createDevice(EDT_DIRECT3D9, window_size, 16, False, False, False, 0)
device = IrrlichtDevice_createDeviceEx(parameters)
;device = IrrlichtDevice_createDeviceEx_(parameters)

If device

	DebugLog "Irrlicht version: " + IrrlichtDevice_getVersion(device)

	IrrlichtDevice_setWindowCaption device, tool_char_to_wchar("Irrlicht version: " + IrrlichtDevice_getVersion(device))
	;AppTitle "Irrlicht version: " + IrrlichtDevice_getVersion(device)
	IrrlichtDevice_setResizable device, True

	video_driver = IrrlichtDevice_getVideoDriver(device)
	;irr_log_stream = IrrlichtDevice_getLogger(device)
	;DebugLog ReadLine$(irr_log_stream)

	scene_manager = IrrlichtDevice_getSceneManager(device)
	i_animated_mesh = ISceneManager_getMesh(scene_manager, mesh_path)
	If i_animated_mesh
		position = vector3df_ctor2(0.0, 0.0, 0.0)
		rotation = vector3df_ctor2(0.0, 0.0, 0.0)
		scale = vector3df_ctor2(1.0, 1.0, 1.0)
		node = ISceneManager_addAnimatedMeshSceneNode(scene_manager, i_animated_mesh, 0, -1, position, rotation, scale, False)
		If node
			ISceneNode_setMaterialFlag node, EMF_LIGHTING, False
			IAnimatedMeshSceneNode_setMD2Animation1 node, EMAT_STAND
			texture = IVideoDriver_getTexture1(video_driver, texture_path)
			ISceneNode_setMaterialTexture node, 0, texture
			position_camera = vector3df_ctor2(0.0, 30.0, -40.0)
			lookat = vector3df_ctor2(0.0, 5.0, 0.0)
			camera = ISceneManager_addCameraSceneNode(scene_manager, node, position_camera, lookat, -1)
		Else
			DebugLog "ERROR : IAnimatedMeshSceneNode not created"
		EndIf
	Else
		DebugLog "ERROR : IAnimatedMesh not created"
	EndIf

	scolor = SColor_ctor2(255, 100, 101, 140)

	While IrrlichtDevice_run(device)

		;DebugLog ReadLine$(irr_log_stream)

		If IrrlichtDevice_isWindowActive(device)

			;CallFunctionVarInt(event_function_pointer, evt)

			If IVideoDriver_beginSceneDefault(video_driver, True, True, scolor)

				ISceneManager_drawAll scene_manager

				IVideoDriver_endScene video_driver

				IrrlichtDevice_sleep device, 10, False

			EndIf

		Else

			IrrlichtDevice_yield device

		EndIf

	Wend

	IrrlichtDevice_closeDevice device

Else

	DebugLog "ERROR : Irrlicht device not created."

EndIf

;CloseFile(log_file)

;WaitKey()
;End

tool_close_stream irr_log_stream

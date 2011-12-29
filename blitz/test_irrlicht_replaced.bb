Include "irrlicht.bb"

mesh_path$ = "media/sydney.md2"
texture_path$ = "media/sydney.bmp"

Graphics3D 640, 480, 32, 2
SetFont LoadFont("Tahoma", 30)

If irrlicht_device

	;AppTitle "Irrlicht version: " + IrrlichtDevice_getVersion(irrlicht_device)
	IrrlichtDevice_setWindowCaption irrlicht_device, tool_char_to_wchar("Irrlicht version: " + IrrlichtDevice_getVersion(irrlicht_device))
	IrrlichtDevice_setResizable irrlicht_device, True

	video_driver = IrrlichtDevice_getVideoDriver(irrlicht_device)

	scene_manager = IrrlichtDevice_getSceneManager(irrlicht_device)
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

	gui_environment = IrrlichtDevice_getGUIEnvironment(irrlicht_device)

	scolor = SColor_ctor2(255, 100, 101, 140)

	While IrrlichtDevice_run(irrlicht_device) And (Not KeyHit(1))

		If IrrlichtDevice_isWindowActive(irrlicht_device)

			If IVideoDriver_beginSceneDefault(video_driver, True, True, scolor)

				Text 20, 20, "Hello There!", True, True

				ISceneManager_drawAll(scene_manager)
				IGUIEnvironment_drawAll(gui_environment)

				IVideoDriver_endScene(video_driver)

				IrrlichtDevice_sleep(irrlicht_device, 10, False)

			EndIf

		Else

			IrrlichtDevice_yield(irrlicht_device)

		EndIf

	Wend

Else

	Print "ERROR : Irrlicht device not created."

EndIf

End
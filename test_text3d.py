'Text3D - Irrlicht Engine Demo'

driver_type = 5
full_screen = False
stencil_buffer = False
vsync = False

run_app = True

from video_choice_dialog import has_pywingui
if has_pywingui:
	from video_choice_dialog import ChoiceDialog, IDOK, IDCANCEL
	dialog = ChoiceDialog()
	dialog.driver_type = driver_type
	dialog.full_screen = full_screen
	dialog.stencil_buffer = stencil_buffer
	dialog.vsync = vsync
	dialogResult = dialog.DoModal()
	if dialogResult == IDOK:
		driver_type = dialog.driver_type
		full_screen = dialog.full_screen
		stencil_buffer = dialog.stencil_buffer
		vsync = dialog.vsync
	elif dialogResult == IDCANCEL:
		run_app = False

if run_app:
	from pyirrlicht import *
	if not driver_type:
		#driver_type = EDT_SOFTWARE
		#driver_type = EDT_DIRECT3D9
		driver_type = EDT_OPENGL
	window_size = dimension2du(640, 480)
	device = createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync, 0)

	if device:
		window_caption = __doc__
		device.setResizable(True)
		driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		guienv = device.getGUIEnvironment()
		static_text = guienv.addStaticText(window_caption, recti(10, 10, 300, 22), True)
		root_scene_node = scene_manager.getRootSceneNode()

		# set text 3d
		text3d1 = IText3D(root_scene_node, scene_manager)
		result_set_text = text3d1.setText(window_caption, color = SColor(255, 0, 255, 0))#, size = 10, primitive_type = EPT_POINTS)#, EPT_LINE_LOOP, EPT_POLYGON
		print('result_set_text %s' % repr(bool(result_set_text)))
		text3d1.setPosition(vector3df(300, 500, 1800))
		text3d1.setRotation(vector3df(0, 90, 0))
		text3d1.setDebugDataVisible(EDS_BBOX)

		# set other text 3d
		russian_text_from_wx_StyledTextCtrl_example = '\xd0\x9f\xd0\xb8\xd1\x82\xd0\xbe\xd0\xbd - \xd0\xbb\xd1\x83\xd1\x87\xd1\x88\xd0\xb8\xd0\xb9 \xd1\x8f\xd0\xb7\xd1\x8b\xd0\xba \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f!'.decode('utf-8')
		text3d2 = IText3D(root_scene_node, scene_manager)
		result_set_text = text3d2.setText(russian_text_from_wx_StyledTextCtrl_example, color_random = RCC_CUSTOM, algorithm_build_vertices = ABSV_LINEAR)
		print('result_set_text %s' % repr(bool(result_set_text)))
		text3d2.setPosition(vector3df(300, 0, 1800))
		text3d2.setRotation(vector3df(0, 90, 0))

		# set yet one text 3d
		text3d3 = IText3D(root_scene_node, scene_manager)
		result_set_text = text3d3.setText(window_caption, color_random = RCC_CUSTOM, algorithm_build_vertices = ABSV_LINEAR_TWO_PASS)
		print('result_set_text %s' % repr(bool(result_set_text)))
		text3d3.setPosition(vector3df(300, -500, 1800))
		text3d3.setRotation(vector3df(0, 90, 0))

		# set camera
		camera = scene_manager.addCameraSceneNodeFPS(moveSpeed = 1.0)
		camera.setFarValue(9000.0)
		camera.setPosition(vector3df(-1300, 500, -1300))

		device.getCursorControl().setVisible(False)

		scolor = SColor(255, 100, 100, 100)
		lastFPS = -1
		while device.run():
			if device.isWindowActive():
				if driver.beginScene(True, True, scolor):
					if device.getTimer().getTime()/500 % 2:
						text3d2.set_auto_custom_color()
					scene_manager.drawAll()
					guienv.drawAll()
					driver.endScene()
				device.sleep(1)
				fps = driver.getFPS()
				if lastFPS != fps:
					text = '%s [%s] FPS:%d' % (window_caption, driver.getName(), fps)
					device.setWindowCaption(text)
					static_text.setText(text)
					lastFPS = fps
			else:
				device._yield()
		device.closeDevice()
	else:
		print('ERROR createDevice')

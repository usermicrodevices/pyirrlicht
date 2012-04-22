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
		#~ root_scene_node = scene_manager.getRootSceneNode()
		root_scene_node = scene_manager.addEmptySceneNode()

		# set points text 3d
		text3d0 = IText3D(root_scene_node, scene_manager)
		result_set_text = text3d0.setText('Some not understandable blinking 3d text', color_random = RCC_CUSTOM, primitive_type = EPT_POINTS, algorithm_build_vertices = ABSV_LINEAR_TWO_PASS)
		print('result_set_text %s' % repr(result_set_text))
		text3d0.setPosition(vector3df(300, 1000, 1800))
		text3d0.setRotation(vector3df(0, 90, 0))
		#~ text3d0.setDebugDataVisible(EDS_BBOX)

		# set curve text 3d
		text3d1 = IText3D(root_scene_node, scene_manager)
		text3d1.getMaterial(0).EmissiveColor = SColor(255, 0, 255, 0)
		result_set_text = text3d1.setText(window_caption)#, size = 10, primitive_type = EPT_POINTS)#, EPT_LINE_LOOP, EPT_POLYGON
		print('result_set_text %s' % repr(result_set_text))
		text3d1.setPosition(vector3df(300, 500, 1800))
		text3d1.setRotation(vector3df(0, 90, 0))

		# set flat text 3d
		russian_text_from_wx_StyledTextCtrl_example = '\xd0\x9f\xd0\xb8\xd1\x82\xd0\xbe\xd0\xbd - \xd0\xbb\xd1\x83\xd1\x87\xd1\x88\xd0\xb8\xd0\xb9 \xd1\x8f\xd0\xb7\xd1\x8b\xd0\xba \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f!'
		try:
			russian_text_from_wx_StyledTextCtrl_example = russian_text_from_wx_StyledTextCtrl_example.decode('utf-8')
		except:
			print('ERROR decode russian text')
		text3d_rus = IText3D(root_scene_node, scene_manager)
		result_set_text = text3d_rus.setText(russian_text_from_wx_StyledTextCtrl_example, color_random = RCC_CUSTOM, algorithm_build_vertices = ABSV_LINEAR)
		print('result_set_text %s' % repr(result_set_text))
		text3d_rus.setPosition(vector3df(300, 0, 1800))
		text3d_rus.setRotation(vector3df(0, 90, 0))

		# set double flat text 3d
		text3d3 = IText3D(root_scene_node, scene_manager)
		text3d3.getMaterial(0).EmissiveColor = SColor(255, 255, 255, 0)
		result_set_text = text3d3.setText('Irrlicht - the best 2D/3D game Engine', color_random = RCC_CUSTOM, algorithm_build_vertices = ABSV_LINEAR_TWO_PASS)
		print('result_set_text %s' % repr(result_set_text))
		text3d3.setPosition(vector3df(300, -500, 1800))
		text3d3.setRotation(vector3df(0, 90, 0))

		#~ # set text with 3d figures, figures can have it's own material
		material_figures = SMaterial()
		material_figures.EmissiveColor = SColor(255, 255, 255, 255)
		material_figures.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
		text3d4 = IText3D(root_scene_node, scene_manager)
		text3d4.getMaterial(0).EmissiveColor = SColor(255, 255, 0, 0)
		result_set_text = text3d4.setText('Mixed 3d text with figures', depth = 25, algorithm_build_vertices = ABSV_LINEAR)
		text3d4.set_draw_as_figures(DAF_SPHERE|DAF_MIXED, material_figures)
		print('result_set_text %s' % repr(result_set_text))
		text3d4.setPosition(vector3df(300, -1000, 1800))
		text3d4.setRotation(vector3df(0, 90, 0))

		# set curve text 3d with two pass
		text3d_tri = IText3D(root_scene_node, scene_manager)
		text3d_tri.getMaterial(0).EmissiveColor = SColor(255, 0, 255, 255)
		result_set_text = text3d_tri.setText('Text 3d as triangles', algorithm_build_vertices = ABSV_INTERLEAVE_TWO_PASS, primitive_type = EPT_LINE_LOOP)#ABSV_PRIMITIVES,)EPT_TRIANGLES
		print('result set curve text 3d with two pass %s' % repr(result_set_text))
		text3d_tri.setPosition(vector3df(300, -1500, 1800))
		text3d_tri.setRotation(vector3df(0, 90, 0))

		# set camera
		camera = scene_manager.addCameraSceneNodeFPS(moveSpeed = 1.0)
		camera.setFarValue(9000.0)
		camera.setPosition(vector3df(-1300, 500, -1300))

		device.getCursorControl().setVisible(False)

		scolor = SColor(255, 100, 100, 100)
		lastFPS = -1
		angle = 0
		while device.run():
			if device.isWindowActive():
				if driver.beginScene(True, True, scolor):
					if device.getTimer().getTime()/500 % 2:
						text3d0.set_auto_emissive_color()
					else:
						text3d_rus.set_auto_emissive_color()
					root_scene_node.setRotation(vector3df(0, angle, 0))
					if angle < 360:
						angle = angle + 1
					else:
						angle = 0
					scene_manager.drawAll()
					guienv.drawAll()
					driver.endScene()
				#~ device.sleep(1)
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

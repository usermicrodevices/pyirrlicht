'First Irrlicht example HelloWorld.py'

driver_type = 1
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
	import pyirrlicht
	if not driver_type:
		#driver_type = pyirrlicht.EDT_NULL
		driver_type = pyirrlicht.EDT_SOFTWARE
		#driver_type = pyirrlicht.EDT_BURNINGSVIDEO
		#driver_type = pyirrlicht.EDT_DIRECT3D8
		#driver_type = pyirrlicht.EDT_DIRECT3D9
		#driver_type = pyirrlicht.EDT_OPENGL
	window_size = pyirrlicht.dimension2du(640, 480)
	device = pyirrlicht.createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync, 0)

	if device:
		window_caption = 'Hello World! - Irrlicht Engine Demo'
		#device.setWindowCaption(window_caption)
		device.setResizable(True)
		driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		guienv = device.getGUIEnvironment()
		static_text = guienv.addStaticText('Hello World! This is the Irrlicht Software renderer!', pyirrlicht.recti(10,10,300,22), True)
		i_animated_mesh = scene_manager.getMesh('media//sydney.md2')
		if i_animated_mesh:
			node = scene_manager.addAnimatedMeshSceneNode(i_animated_mesh)
			if node:
				node.setMaterialFlag(pyirrlicht.EMF_LIGHTING, False)
				node.setMD2Animation(pyirrlicht.EMAT_STAND)
				node.setMaterialTexture(0, driver.getTexture('media//sydney.bmp'))
			else:
				print('ERROR result method addAnimatedMeshSceneNode, scene_manager')
			position = pyirrlicht.vector3df(0.0, 30.0, -40.0)
			lookat = pyirrlicht.vector3df(0.0, 5.0, 0.0)
			scene_manager.addCameraSceneNode(node, position, lookat)
			scolor = pyirrlicht.SColor(255,100,101,140)
			lastFPS = -1
			while device.run():
				if device.isWindowActive():
					if driver.beginScene(True, True, scolor):
						scene_manager.drawAll()
						guienv.drawAll()
						driver.endScene()
					#device.sleep(1)

					fps = driver.getFPS()
					if lastFPS != fps:
						text = '%s [%s] FPS:%d' % (window_caption, driver.getName(), fps)
						device.setWindowCaption(text)
						static_text.setText(text)
						lastFPS = fps
				else:
					device._yield()
		else:
			print('ERROR getMesh')
		device.closeDevice()
	else:
		print('ERROR createDevice')

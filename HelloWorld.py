import pyirrlicht

#~ driverType = pyirrlicht.EDT_NULL
driverType = pyirrlicht.EDT_SOFTWARE
#~ driverType = pyirrlicht.EDT_BURNINGSVIDEO
#~ driverType = pyirrlicht.EDT_DIRECT3D8
#~ driverType = pyirrlicht.EDT_DIRECT3D9
#~ driverType = pyirrlicht.EDT_OPENGL

windowSize = pyirrlicht.dimension2du(640, 480)
device = pyirrlicht.createDevice(driverType, windowSize, 16, False, False, False, 0)

if device:
	window_caption = 'Hello World! - Irrlicht Engine Demo'
	#~ device.setWindowCaption(window_caption)
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()
	guienv.addStaticText('Hello World! This is the Irrlicht Software renderer!', pyirrlicht.recti(10,10,260,22), True)
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
				# device.sleep(10)

				fps = driver.getFPS()
				if lastFPS != fps:
					device.setWindowCaption('%s [%s] FPS:%d' % (window_caption, driver.getName(), fps))
					lastFPS = fps
			else:
				device._yield()
	else:
		print('ERROR getMesh')
	device.closeDevice()
else:
	print('ERROR createDevice')

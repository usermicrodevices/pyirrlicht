import pyirrlicht

#~ driverType = pyirrlicht.EDT_NULL
#~ driverType = pyirrlicht.EDT_SOFTWARE
#~ driverType = pyirrlicht.EDT_BURNINGSVIDEO
#~ driverType = pyirrlicht.EDT_DIRECT3D8
#~ driverType = pyirrlicht.EDT_DIRECT3D9
driverType = pyirrlicht.EDT_OPENGL

device = pyirrlicht.createDevice(driverType, pyirrlicht.dimension2du(640, 480))
if device:
	window_caption = 'Quake 3 Map! - Irrlicht Engine Demo'
	#~ device.setWindowCaption(window_caption)
	device.setResizable(True)
	scene_manager = device.getSceneManager()
	if pyirrlicht.IRRLICHT_VERSION < 180:
		device.getFileSystem().addZipFileArchive('media//map-20kdm2.pk3')
	else:
		device.getFileSystem().addFileArchive("media//map-20kdm2.pk3")
	i_animated_mesh = scene_manager.getMesh('20kdm2.bsp')
	if i_animated_mesh:
		i_mesh = i_animated_mesh.getMesh(0)
		if i_mesh:
			i_meshscene_node = scene_manager.addOctTreeSceneNode(i_mesh, 0, -1, 1024)
			if i_meshscene_node:
				i_meshscene_node.setPosition(pyirrlicht.vector3df(-1300.0, -144.0, -1249.0))
			else:
				print ('ERROR result method addOctTreeSceneNode2, SceneManager')
		else:
			print ('ERROR result method getMesh, IAnimatedMesh')
		scene_manager.addCameraSceneNodeFPS()
		device.getCursorControl().setVisible(False)
		#~ guienv = device.getGUIEnvironment()
		driver = device.getVideoDriver()
		scolor = pyirrlicht.SColor(255, 200, 200, 200)
		lastFPS = -1
		while device.run():
			if device.isWindowActive():
				if driver.beginScene(True, True, scolor):
					scene_manager.drawAll()
					# guienv.drawAll()
					driver.endScene()
				# device.sleep(10)

				fps = driver.getFPS()
				if lastFPS != fps:
					device.setWindowCaption('%s [%s] FPS:%d' % (window_caption, driver.getName(), fps))
					lastFPS = fps
			else:
				device.yield_self()
	else:
		print ('ERROR result method getMesh, SceneManager')
	device.drop()
else:
	print ('ERROR createDevice')

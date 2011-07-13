import irrlicht

device = irrlicht.createDevice(irrlicht.EDT_OPENGL, irrlicht.dimension2du(640, 480))
if device:
	device.setWindowCaption('Quake 3 Map! - Irrlicht Engine Demo')
	device.setResizable(True)
	scene_manager = device.getSceneManager()
	device.getFileSystem().addZipFileArchive('media//map-20kdm2.pk3')
	i_animated_mesh = scene_manager.getMesh('20kdm2.bsp')
	if i_animated_mesh:
		i_mesh = i_animated_mesh.getMesh(0)
		if i_mesh:
			i_meshscene_node = scene_manager.addOctreeSceneNode(i_mesh, None, -1, 1024)
			if i_meshscene_node:
				i_meshscene_node.setPosition(irrlicht.vector3df(-1300.0, -144.0, -1249.0))
			else:
				print ('ERROR result method addOctTreeSceneNode2, SceneManager')
		else:
			print ('ERROR result method getMesh, IAnimatedMesh')
		scene_manager.addCameraSceneNodeFPS()
		device.getCursorControl().setVisible(False)
		#~ guienv = device.getGUIEnvironment()
		driver = device.getVideoDriver()
		scolor = irrlicht.SColor(255, 200, 200, 200)
		while device.run():
			if device.isWindowActive():
				driver.beginScene(True, True, scolor)
				scene_manager.drawAll()
				#~ guienv.drawAll()
				driver.endScene()
				device.sleep(10)
			else:
				device.yield_self()
	else:
		device.drop()
		print ('ERROR result method getMesh, SceneManager')
	device.drop()
else:
	print ('ERROR createDevice')

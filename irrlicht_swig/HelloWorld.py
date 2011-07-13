from irrlicht import *

windowSize = dimension2du(640, 480)
device = createDevice(EDT_OPENGL, windowSize, 16)

if device:
	device.setWindowCaption('Hello World! - Irrlicht Engine Demo')
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()
	guienv.addStaticText('Hello World! This is the Irrlicht Software renderer!', recti(10,10,260,22), True)
	i_animated_mesh = scene_manager.getMesh('media//sydney.md2')
	if i_animated_mesh:
		node = scene_manager.addAnimatedMeshSceneNode(i_animated_mesh)
		if node:
			node.setMaterialFlag(EMF_LIGHTING, False)
			node.setMD2Animation(EMAT_STAND)
			node.setMaterialTexture(0, driver.getTexture('media//sydney.bmp'))
		else:
			print ('ERROR result method addAnimatedMeshSceneNode, scene_manager')
		position = vector3df(0.0, 30.0, -40.0)
		lookat = vector3df(0.0, 5.0, 0.0)
		scene_manager.addCameraSceneNode(node, position, lookat)
		scolor = SColor(255,100,101,140)
		while device.run():
			if device.isWindowActive():
				driver.beginScene(True, True, scolor)
				scene_manager.drawAll()
				guienv.drawAll()
				driver.endScene()
			else:
				device._yield()
	else:
		device.drop()
		print ('ERROR getMesh')
	device.drop()
else:
	print ('ERROR createDevice')

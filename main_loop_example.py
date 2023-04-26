import pyirrlicht

#~ driverType = pyirrlicht.EDT_NULL
driverType = pyirrlicht.EDT_SOFTWARE
#~ driverType = pyirrlicht.EDT_BURNINGSVIDEO
#~ driverType = pyirrlicht.EDT_DIRECT3D8
#~ driverType = pyirrlicht.EDT_DIRECT3D9
#~ driverType = pyirrlicht.EDT_OPENGL

class UserIEventReceiver(pyirrlicht.IEventReceiver):
	main_loop = None
	def OnEvent(self, event):
		'PRESS ESCAPE FOR EXIT FROM MAIN LOOP'
		if self.GetEventType(event) is pyirrlicht.EET_KEY_INPUT_EVENT:
			if self.KeyInput_Key(self.GetKeyInput(event)) == pyirrlicht.KEY_ESCAPE:
				if self.main_loop:
					self.main_loop.stop()
		return False

windowSize = pyirrlicht.dimension2du(640, 480)
i_event_receiver = UserIEventReceiver()
device = pyirrlicht.createDevice(driverType, windowSize, 16, False, False, False, i_event_receiver)

if device:
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()
	guienv.addStaticText('Hello World! This is C++ example main loop realisation!', pyirrlicht.recti(10,10,260,22), True)
	i_animated_mesh = scene_manager.getMesh('..//irrlicht//media//sydney.md2')
	if i_animated_mesh:
		node = scene_manager.addAnimatedMeshSceneNode2(i_animated_mesh)
		if node:
			node.setMaterialFlag(pyirrlicht.EMF_LIGHTING, False)
			node.setMD2Animation(pyirrlicht.EMAT_STAND)
			node.setMaterialTexture(0, driver.getTexture('..//irrlicht//media//sydney.bmp'))
		position = pyirrlicht.vector3df(0.0, 30.0, -40.0)
		lookat = pyirrlicht.vector3df(0.0, 5.0, 0.0)
		scene_manager.addCameraSceneNode(node, position, lookat)

		main_loop = pyirrlicht.MainLoop(device, driver, scene_manager, guienv)
		i_event_receiver.main_loop = main_loop
		print('START MAIN LOOP')
		main_loop.start()
		print('STOP MAIN LOOP')
	else:
		print('ERROR getMesh')
	device.drop()
else:
	print('ERROR createDevice')

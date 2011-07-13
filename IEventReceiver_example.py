import pyirrlicht

#~ driverType = pyirrlicht.EDT_NULL
driverType = pyirrlicht.EDT_SOFTWARE
#~ driverType = pyirrlicht.EDT_BURNINGSVIDEO
#~ driverType = pyirrlicht.EDT_DIRECT3D8
#~ driverType = pyirrlicht.EDT_DIRECT3D9
#~ driverType = pyirrlicht.EDT_OPENGL

class UserIEventReceiver(pyirrlicht.IEventReceiver):
	def OnEvent(self, event):
		'for more C++ style look IEventReceiver_c++.py'
		#~ event_type = event.contents.EventType
		event_type = self.GetEventType(event)
		if event_type is pyirrlicht.EET_GUI_EVENT:
			print('GUI EVENT', event_type)
		elif event_type is pyirrlicht.EET_MOUSE_INPUT_EVENT:
			print('MOUSE INPUT EVENT', event_type)
			mouse_event = self.GetMouseInput(event)
			print('X', self.MouseInput_X(mouse_event), 'Y', self.MouseInput_Y(mouse_event), 'EventType', self.MouseInput_EventType(mouse_event), 'left', bool(self.MouseInput_isLeftPressed(mouse_event)), 'right', bool(self.MouseInput_isRightPressed(mouse_event)), 'middle', bool(self.MouseInput_isMiddlePressed(mouse_event)))
		elif event_type is pyirrlicht.EET_KEY_INPUT_EVENT:
			print('KEY INPUT EVENT', event_type)
			key_event = self.GetKeyInput(event)
			print('Key', self.KeyInput_Key(key_event), 'Char', self.KeyInput_Char(key_event))
		elif event_type is pyirrlicht.EET_JOYSTICK_INPUT_EVENT:
			print('JOYSTICK INPUT EVENT', event_type)
		elif event_type is pyirrlicht.EET_LOG_TEXT_EVENT:
			print('LOG TEXT EVENT', event_type)
			log_event = self.GetLogEvent(event)
			print(self.LogEvent_Level(log_event), self.LogEvent_Text(log_event))
		elif event_type is pyirrlicht.EET_USER_EVENT:
			print('USER EVENT', event_type)
		else:
			print('Unknown EventType', event_type)
		return False

windowSize = pyirrlicht.dimension2du(640, 480)

i_event_receiver = UserIEventReceiver()
device = pyirrlicht.createDevice(pyirrlicht.EDT_OPENGL, windowSize, 16, False, False, False, i_event_receiver)

if device:
	device.setWindowCaption('Hello World! - Irrlicht Engine Demo')
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()
	guienv.addStaticText('Hello World! This is the Irrlicht Software renderer!', pyirrlicht.recti(10,10,260,22), True)
	i_animated_mesh = scene_manager.getMesh('media//sydney.md2')
	if i_animated_mesh:
		node = scene_manager.addAnimatedMeshSceneNode2(i_animated_mesh)
		if node:
			node.setMaterialFlag(pyirrlicht.EMF_LIGHTING, False)
			node.setMD2Animation(pyirrlicht.EMAT_STAND)
			node.setMaterialTexture(0, driver.getTexture('media//sydney.bmp'))
		position = pyirrlicht.vector3df(0.0, 30.0, -40.0)
		lookat = pyirrlicht.vector3df(0.0, 5.0, 0.0)
		scene_manager.addCameraSceneNode(node, position, lookat)
		scolor = pyirrlicht.SColor(255,100,101,140)
		while device.run():
			if device.isWindowActive():
				if driver.beginScene(True, True, scolor):
					scene_manager.drawAll()
					guienv.drawAll()
					driver.endScene()
				device.sleep(10)
			else:
				device.yield_self()
	else:
		print('ERROR getMesh')
	device.drop()
else:
	print('ERROR createDevice')

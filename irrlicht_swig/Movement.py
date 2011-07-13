from irrlicht import *

class UserIEventReceiver(IEventReceiver):
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	def OnEvent(self, event):
		event_type = self.GetEventType(event)
		if event_type is EET_KEY_INPUT_EVENT:
			key_event = self.GetKeyInput(event)
			self.KeyIsDown[self.KeyInput_Key(key_event)] = self.KeyInput_PressedDown(key_event)
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode];

windowSize = dimension2du(640, 480)
i_event_receiver = UserIEventReceiver()
device = createDevice(EDT_OPENGL, windowSize, 16, False, False, False, i_event_receiver)

if device:
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	i_scene_node = scene_manager.addSphereSceneNode()
	if i_scene_node:
		i_scene_node.setPosition(vector3df(0,0,30))
		i_scene_node.setMaterialTexture(0, driver.getTexture("media//wall.bmp"))
		i_scene_node.setMaterialFlag(EMF_LIGHTING, False)
	i_scene_node2 = scene_manager.addCubeSceneNode()
	if i_scene_node2:
		i_scene_node2.setMaterialTexture(0, driver.getTexture("media//t351sml.jpg"))
		i_scene_node2.setMaterialFlag(EMF_LIGHTING, False)
		i_scene_node_animator = scene_manager.createFlyCircleAnimator(vector3df(0,0,30), 20.0)
		if i_scene_node_animator:
			i_scene_node2.addAnimator(i_scene_node_animator)
			i_scene_node_animator.drop()
	i_animated_mesh_scene_node = scene_manager.addAnimatedMeshSceneNode(scene_manager.getMesh("media//ninja.b3d"))
	if i_animated_mesh_scene_node:
		i_scene_node_animator = scene_manager.createFlyStraightAnimator(vector3df(100,0,60), vector3df(-100,0,60), 3500, True)
		if i_scene_node_animator:
			i_animated_mesh_scene_node.addAnimator(i_scene_node_animator)
			i_scene_node_animator.drop()
		i_animated_mesh_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		i_animated_mesh_scene_node.setFrameLoop(0, 13)
		i_animated_mesh_scene_node.setAnimationSpeed(15)
		i_animated_mesh_scene_node.setScale(vector3df(2,2,2))
		i_animated_mesh_scene_node.setRotation(vector3df(0,-90,0))

	scene_manager.addCameraSceneNodeFPS()
	device.getCursorControl().setVisible(False)
	guienv = device.getGUIEnvironment()
	guienv.addImage(driver.getTexture("media//irrlichtlogoalpha2.tga"), position2di(10,20))

	i_gui_static_text = guienv.addStaticText("Movement Example - Irrlicht Engine", recti(10, 10, 400, 20))
	i_gui_static_text.setOverrideColor(SColor(255, 255, 255, 0))

	lastFPS = -1
	then = device.getTimer().getTime()
	MOVEMENT_SPEED = 5.0
	scolor = SColor(255,113,113,133)
	nodePosition = i_scene_node.getPosition()
	while device.run():
		if device.isWindowActive():
			now = device.getTimer().getTime()
			frameDeltaTime = (now - then) / 1000.0
			then = now
			if i_event_receiver.IsKeyDown(KEY_KEY_W):
				nodePosition.Y += MOVEMENT_SPEED * frameDeltaTime
			elif i_event_receiver.IsKeyDown(KEY_KEY_S):
				nodePosition.Y -= MOVEMENT_SPEED * frameDeltaTime
			if i_event_receiver.IsKeyDown(KEY_KEY_A):
				nodePosition.X -= MOVEMENT_SPEED * frameDeltaTime
			elif i_event_receiver.IsKeyDown(KEY_KEY_D):
				nodePosition.X += MOVEMENT_SPEED * frameDeltaTime
			i_scene_node.setPosition(nodePosition)

			driver.beginScene(True, True, scolor)
			scene_manager.drawAll()
			guienv.drawAll()
			driver.endScene()

			fps = driver.getFPS()
			if lastFPS != fps:
				tmp = "Movement Example - Irrlicht Engine ["
				tmp += driver.getName() + "] fps: %d" % fps
				device.setWindowCaption(tmp)
				lastFPS = fps
			device.sleep(10)
		else:
			device._yield()
	device.drop()
else:
	print ('ERROR createDevice')

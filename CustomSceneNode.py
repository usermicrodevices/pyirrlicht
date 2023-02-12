from pyirrlicht import *

#driverType = EDT_NULL
#driverType = EDT_SOFTWARE
#driverType = EDT_BURNINGSVIDEO
#driverType = EDT_DIRECT3D8
#driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

iType = EIT_32BIT

class CSampleSceneNode(CustomSceneNode):
	def __init__(self, *args, **kwargs):
		self.Material = SMaterial()
		self.Material.Wireframe = False
		self.Material.Lighting = False

		self.Vertices = S3DVertex(4)
		self.Vertices[0] = S3DVertex(vector3df(0.0,0.0,10.0), vector3df(1.0,1.0,0.0), SColor(255,0,255,255), vector2df(0.0, 1.0))
		self.Vertices[1] = S3DVertex(vector3df(10.0,0.0,-10.0), vector3df(1.0,0.0,0.0), SColor(255,255,0,255), vector2df(1.0, 1.0))
		self.Vertices[2] = S3DVertex(vector3df(0.0,20.0,0.0), vector3df(0.0,1.0,1.0), SColor(255,255,255,0), vector2df(1.0, 0.0))
		self.Vertices[3] = S3DVertex(vector3df(-10.0,0.0,-10.0), vector3df(0.0,0.0,1.0), SColor(255,0,255,0), vector2df(0.0, 0.0))

		self.Box = aabbox3df()
		self.Box.reset(self.Vertices[0].Pos)
		for i in range(1, 4):
			self.Box.addInternalPoint(self.Vertices[i].Pos)

		CustomSceneNode.__init__(self, *args, **kwargs)

	# def getTypeS3DVertex(self):
		# return 0

	def OnRegisterSceneNode(self):
		if self.isVisible():
			self.getSceneManager().registerNodeForRendering(self)

	def render(self):
		indices = (ctypes.c_int * 12)(0,2,3, 2,1,3, 1,0,3, 2,0,1)
		driver = self.getSceneManager().getVideoDriver()
		driver.setMaterial(self.Material)
		driver.setTransform(ETS_WORLD, self.getAbsoluteTransformation())
		driver.drawVertexPrimitiveList(self.Vertices, 4, indices, 4, EVT_STANDARD, EPT_TRIANGLES, iType)

	def getBoundingBox(self):
		return self.Box.c_pointer

	def getMaterialCount(self):
		return 1

	def getMaterial(self, num):
		return self.Material.c_pointer

device = createDevice(driverType, dimension2du(640, 480), 16, False)
if device:
	window_caption = 'Custom Scene Node - Irrlicht Engine Demo'
	#device.setWindowCaption(window_caption)
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	scene_manager.addCameraSceneNode(0, vector3df(0,-40,0), vector3df(0,0,0))
	myNode = CSampleSceneNode(scene_manager.getRootSceneNode(), scene_manager)
	i_scene_node_animator = scene_manager.createRotationAnimator(vector3df(0.8, 0.0, 0.8))
	if i_scene_node_animator:
		myNode.addAnimator(i_scene_node_animator)
		del i_scene_node_animator
	del myNode
	frames = 0
	scene_color = SColor(0, 100, 100, 100)
	while device.run():
		if device.isWindowActive():
			frames += 1
			if driver.beginScene(True, True, scene_color):
				scene_manager.drawAll()
				driver.endScene()
		else:
			device.yield_self()
		if frames == 100:
			device.setWindowCaption("%s [%s] FPS: %d" % (window_caption, driver.getName(), driver.getFPS()))
			frames=0
	device.drop()
else:
	print('ERROR createDevice')

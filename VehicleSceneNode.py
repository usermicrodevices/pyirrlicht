from pyirrlicht import *

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

class WheelSceneNode(CustomSceneNode):
	def __init__(self, *args, **kwargs):
		self.Material = SMaterial()
		self.Material.Wireframe = False
		self.Material.Lighting = False
		self.Material.BackfaceCulling = False

		self.ver_count = 10
		self.Vertices = S3DVertex(self.ver_count)
		self.Vertices[0] = S3DVertex(vector3df(0.0,0.0,10.0), vector3df(0.0,1.0,1.0), SColor(255,0,255,255), vector2df(0.0, 1.0))
		self.Vertices[1] = S3DVertex(vector3df(0.0,20.0,0.0), vector3df(1.0,-1.0,0.0), SColor(255,255,0,255), vector2df(1.0, 1.0))
		self.Vertices[2] = S3DVertex(vector3df(15.0,15.0,0.0), vector3df(-1.0,1.0,0.0), SColor(255,255,255,0), vector2df(1.0, 0.0))
		self.Vertices[3] = S3DVertex(vector3df(20.0,0.0,0.0), vector3df(-1.0,-1.0,0.0), SColor(255,0,255,0), vector2df(0.0, 0.0))
		self.Vertices[4] = S3DVertex(vector3df(15.0,-15.0,0.0), vector3df(-1.0,-1.0,0.0), SColor(255,0,0,255), vector2df(0.0, 1.0))
		self.Vertices[5] = S3DVertex(vector3df(0.0,-20.0,0.0), vector3df(-1.0,1.0,0.0), SColor(255,255,0,0), vector2df(1.0, 1.0))
		self.Vertices[6] = S3DVertex(vector3df(-15.0,-15.0,0.0), vector3df(1.0,1.0,0.0), SColor(255,0,128,128), vector2df(1.0, 0.0))
		self.Vertices[7] = S3DVertex(vector3df(-20.0,0.0,0.0), vector3df(1.0,1.0,0.0), SColor(255,128,0,128), vector2df(0.0, 0.0))
		self.Vertices[8] = S3DVertex(vector3df(-15.0,15.0,0.0), vector3df(1.0,1.0,0.0), SColor(255,128,128,0), vector2df(0.0, 0.0))
		self.Vertices[9] = S3DVertex(vector3df(0.0,0.0,-10.0), vector3df(0.0,0.0,-1.0), SColor(255,0,128,0), vector2df(0.0, 0.0))

		self.Box = aabbox3df()
		self.Box.reset(self.Vertices[0].Pos)
		for i in range(1, self.ver_count):
			self.Box.addInternalPoint(self.Vertices[i].Pos)

		CustomSceneNode.__init__(self, *args, **kwargs)

		self.iType = EIT_32BIT
		self.scene_manager = self.getSceneManager()
		self.video_driver = self.scene_manager.getVideoDriver()

	def getTypeS3DVertex(self):
		return 0

	def OnRegisterSceneNode(self):
		if self.isVisible():
			self.scene_manager.registerNodeForRendering(self)

	def render(self):
		triangles = self.ver_count-2
		list_indices = []
		for i in range(0, triangles):
			list_indices.append(0)
			list_indices.append(i+1)
			if i == triangles-1:
				list_indices.append(1)
			else:
				list_indices.append(i+2)
		for i in range(0, triangles):
			list_indices.append(9)
			list_indices.append(i+1)
			if i == triangles-1:
				list_indices.append(1)
			else:
				list_indices.append(i+2)
		indices = (ctypes.c_int * (6 * triangles))(*list_indices)
		self.video_driver.setMaterial(self.Material)
		self.video_driver.setTransform(ETS_WORLD, self.getAbsoluteTransformation())
		self.video_driver.drawVertexPrimitiveList(self.Vertices, self.ver_count, indices, (self.ver_count-2)*2, EVT_STANDARD, EPT_TRIANGLES, self.iType)
		#~ self.video_driver.draw3DBox(self.Box)

	def getBoundingBox(self):
		return self.Box.c_pointer

	def getMaterialCount(self):
		return 1

	def getMaterial(self, num):
		return self.Material.c_pointer

device = createDevice(driverType, dimension2du(460, 240), 32, False)
if device:
	window_caption = 'Vehicle Scene Node - Irrlicht Engine Demo'
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	camera = scene_manager.addCameraSceneNodeMaya(distance = 300.0)
	camera.setTarget(vector3df(0,50,0))
	base = scene_manager.addEmptySceneNode()
	platform = scene_manager.addCubeSceneNode(15.0, base, position = vector3df(50,0,25), scale = vector3df(8.0, 1.0, 2.0))
	platform.setMaterialFlag(EMF_LIGHTING, False)
	material = platform.getMaterial(0)
	material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
	platform.setMaterialTexture(0, generate_texture(driver, ECF_A8R8G8B8))
	geometry_creator = scene_manager.getGeometryCreator()
	cylinder_mesh = geometry_creator.createCylinderMesh(radius = 1, length = 50, tesselation = 4, color = SColor(255,255,0,0), closeTop = True, oblique = 0.0)
	pipe1 = scene_manager.addMeshSceneNode(cylinder_mesh, base)
	pipe1.setRotation(vector3df(90.0, 0.0, 0.0))
	pipe2 = scene_manager.addMeshSceneNode(cylinder_mesh, base)
	pipe2.setRotation(vector3df(90.0, 0.0, 0.0))
	pipe2.setPosition(vector3df(100.0, 0.0, 0.0))
	wheels = (WheelSceneNode(base, scene_manager),
		WheelSceneNode(base, scene_manager),
		WheelSceneNode(base, scene_manager),
		WheelSceneNode(base, scene_manager))
	wheels[1].setPosition(vector3df(100.0, 0.0, 0.0))
	wheels[2].setPosition(vector3df(100.0, 0.0, 50.0))
	wheels[3].setPosition(vector3df(0.0, 0.0, 50.0))
	anim_pos = vector3df(0.0, 0.0, 1.0)
	animators = (scene_manager.createRotationAnimator(anim_pos),
		scene_manager.createRotationAnimator(anim_pos),
		scene_manager.createRotationAnimator(anim_pos),
		scene_manager.createRotationAnimator(anim_pos))
	i = 0
	for w in wheels:
		w.addAnimator(animators[i])
		animators[i].drop()
		w.drop()
		i = i + 1
	base.setRotation(vector3df(0.0, 90.0, 0.0))
	base.addAnimator(scene_manager.createRotationAnimator(vector3df(0.0, 0.06, 0.0)))
	base.addAnimator(scene_manager.createFlyCircleAnimator(radius = 200.0, speed = 0.0001))
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

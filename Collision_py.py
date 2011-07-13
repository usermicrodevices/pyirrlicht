from pyirrlicht import *

ID_IsNotPickable = 0
IDFlag_IsPickable = 1
IDFlag_IsHighlightable = 2

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

device = createDevice(driverType, dimension2du(640, 480), 16, False)

if device:
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()

	device.getFileSystem().addZipFileArchive("media/map-20kdm2.pk3")

	q3levelmesh = scene_manager.getMesh("20kdm2.bsp")

	q3node = IMeshSceneNode(0)

	if q3levelmesh:
		q3node = scene_manager.addOctreeSceneNode(q3levelmesh.getMesh(0), 0, IDFlag_IsPickable)

	selector = ITriangleSelector(0)

	if q3node:
		q3node.setPosition(vector3df(-1350,-130,-1400))

		selector = scene_manager.createOctreeTriangleSelector(q3node.getMesh(), q3node, 128)
		q3node.setTriangleSelector(selector)

	camera = scene_manager.addCameraSceneNodeFPS(0, 100.0, 0.3, ID_IsNotPickable, 0, 0, True, 3.0)
	camera.setPosition(vector3df(50,50,-60))
	camera.setTarget(vector3df(-70,30,-60))

	if selector:
		anim = scene_manager.createCollisionResponseAnimator(selector, camera, vector3df(30,50,30), vector3df(0,-10,0), vector3df(0,30,0))
		#~ selector.drop()
		camera.addAnimator(anim)
		anim.drop()

	device.getCursorControl().setVisible(False)

	billboard = scene_manager.addBillboardSceneNode()
	billboard.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
	billboard.setMaterialTexture(0, driver.getTexture("media/particle.bmp"))
	billboard.setMaterialFlag(EMF_LIGHTING, False)
	billboard.setMaterialFlag(EMF_ZBUFFER, False)
	billboard.setSize(dimension2df(20.0, 20.0))
	billboard.setID(ID_IsNotPickable)

	node = scene_manager.addAnimatedMeshSceneNode(scene_manager.getMesh("media/faerie.md2"), 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	node.setPosition(vector3df(-70,-15,-120))
	node.setScale(vector3df(2, 2, 2))
	node.setMD2Animation(EMAT_POINT)
	node.setAnimationSpeed(20.0)
	material = node.getMaterial(0)
	material.setTexture(0, driver.getTexture("media/faerie2.bmp"))
	material.Lighting = True
	material.NormalizeNormals = True
	#~ node.setMaterial(material)

	selector = scene_manager.createTriangleSelector(node)
	node.setTriangleSelector(selector)
	#~ selector.drop()

	node = scene_manager.addAnimatedMeshSceneNode(scene_manager.getMesh("media/dwarf.x"), 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	node.setPosition(vector3df(-70,-66,0))
	node.setRotation(vector3df(0,-90,0))
	node.setAnimationSpeed(20.0)
	selector = scene_manager.createTriangleSelector(node)
	node.setTriangleSelector(selector)
	#~ selector.drop()

	node = scene_manager.addAnimatedMeshSceneNode(scene_manager.getMesh("media/ninja.b3d"), 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	node.setScale(vector3df(10, 10, 10))
	node.setPosition(vector3df(-70,-66,-60))
	node.setRotation(vector3df(0,90,0))
	node.setAnimationSpeed(10.0)
	node.getMaterial(0).NormalizeNormals = True
	selector = scene_manager.createTriangleSelector(node)
	node.setTriangleSelector(selector)
	#~ selector.drop()

	#~ material.setTexture(0, ITexture(0))
	#~ material.Lighting = False

	light = scene_manager.addLightSceneNode(0, vector3df(-60,100,400), SColorf(1.0,1.0,1.0,1.0), 600.0)
	light.setID(ID_IsNotPickable)

	highlightedSceneNode = ISceneNode(0)
	collMan = scene_manager.getSceneCollisionManager()
	lastFPS = -1

	material = SMaterial()
	material.setTexture(0, ITexture(0))
	material.Lighting = False
	material.NormalizeNormals = True
	material.Wireframe = True

	scolor = SColor()
	scolor_triangle = SColor(0,255,0,0)

	ray = line3df()
	intersection = vector3df()
	hitTriangle = triangle3df()
	ctarget = camera.getTarget()

	while device.run():
		if device.isWindowActive():
			driver.beginScene(True, True, scolor)
			scene_manager.drawAll()

			if highlightedSceneNode:
				highlightedSceneNode.setMaterialFlag(EMF_LIGHTING, True)
				highlightedSceneNode = 0

			#~ ray = line3df()
			ray.start = camera.getPosition()
			#~ ray.end = ray.start + (camera.getTarget() - ray.start).normalize() * 1000.0
			v = vector3df(ctarget.X-ray.start.X, ctarget.Y-ray.start.Y, ctarget.Z-ray.start.Z)
			#~ v.normalize()
			v = vector3df(v.X*1000.0, v.Y*1000.0, v.Z*1000.0)
			ray.end = vector3df(v.X+ray.start.X, v.Y+ray.start.Y, v.Z+ray.start.Z)
			#~ del v

			#~ intersection = vector3df()
			#~ hitTriangle = triangle3df()

			selectedSceneNode = collMan.getSceneNodeAndCollisionPointFromRay(ray, intersection, hitTriangle, IDFlag_IsPickable)

			if selectedSceneNode:
				billboard.setPosition(intersection)
				driver.setTransform(ETS_WORLD, matrix4())
				driver.setMaterial(material)
				driver.draw3DTriangle(hitTriangle, scolor_triangle)

				if (selectedSceneNode.getID() & IDFlag_IsHighlightable) == IDFlag_IsHighlightable:
					highlightedSceneNode = selectedSceneNode
					highlightedSceneNode.setMaterialFlag(EMF_LIGHTING, False)

			driver.endScene()
			#~ device.sleep(10)

			fps = driver.getFPS()
			if lastFPS != fps:
				str = "Collision detection example - Irrlicht Engine ["
				str += driver.getName()
				str += "] FPS:%d" % fps
				device.setWindowCaption(str)
				lastFPS = fps
		else:
			device.yield_self()

	device.drop()

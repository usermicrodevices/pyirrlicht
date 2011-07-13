from pyirrlicht import *

ID_IsNotPickable = 0
IDFlag_IsPickable = 1
IDFlag_IsHighlightable = 2

size_window = dimension2du(640, 480)
device = createDevice(EDT_OPENGL, size_window, 16, False)

if device:
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()

	fs = device.getFileSystem()
	fs.addZipFileArchive("media//map-20kdm2.pk3")

	q3levelmesh = scene_manager.getMesh("20kdm2.bsp")

	q3node = IMeshSceneNode(0)

	if q3levelmesh:
		mesh = q3levelmesh.getMesh(0)
		q3node = scene_manager.addOctreeSceneNode(mesh, 0, IDFlag_IsPickable)

	selector1 = ITriangleSelector(0)

	if q3node:
		v1 = vector3df(-1350,-130,-1400)
		q3node.setPosition(v1)
		m1 = q3node.getMesh()
		selector1 = scene_manager.createOctreeTriangleSelector(m1, q3node, 128)
		q3node.setTriangleSelector(selector1)

	camera = scene_manager.addCameraSceneNodeFPS(0, 100.0, 0.3, ID_IsNotPickable, 0, 0, True, 3.0)
	v2, v3 = vector3df(50,50,-60), vector3df(-70,30,-60)
	camera.setPosition(v2)
	camera.setTarget(v3)

	if selector1:
		v4, v5, v6 = vector3df(30,50,30), vector3df(0,-10,0), vector3df(0,30,0)
		anim = scene_manager.createCollisionResponseAnimator(selector1, camera, v4, v5, v6)
		#~ selector1.drop()
		camera.addAnimator(anim)
		anim.drop()

	cursor = device.getCursorControl()
	cursor.setVisible(False)

	billboard = scene_manager.addBillboardSceneNode()
	billboard.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
	t1 = driver.getTexture("media//particle.bmp")
	billboard.setMaterialTexture(0, t1)
	billboard.setMaterialFlag(EMF_LIGHTING, False)
	billboard.setMaterialFlag(EMF_ZBUFFER, False)
	d1 = dimension2df(20.0, 20.0)
	billboard.setSize(d1)
	billboard.setID(ID_IsNotPickable)

	m3 = scene_manager.getMesh("media//faerie.md2")
	node1 = scene_manager.addAnimatedMeshSceneNode(m3, 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	v7 = vector3df(-70.0,-15.0,-120.0)
	node1.setPosition(v7)
	v8 = vector3df(2.0, 2.0, 2.0)
	node1.setScale(v8)
	node1.setMD2Animation(EMAT_POINT)
	node1.setAnimationSpeed(20.0)
	material = node1.getMaterial(0)
	t2 = driver.getTexture("media//faerie2.bmp")
	material.setTexture(0, t2)
	material.Lighting = True
	material.NormalizeNormals = True
	#~ node1.setMaterial(material)

	selector2 = scene_manager.createTriangleSelector(node1)
	node1.setTriangleSelector(selector2)
	selector2.drop()

	m4 = scene_manager.getMesh("media//dwarf.x")
	node2 = scene_manager.addAnimatedMeshSceneNode(m4, 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	v9 = vector3df(-70.0,-66.0,0.0)
	node2.setPosition(v9)
	v10 = vector3df(0.0,-90.0,0.0)
	node2.setRotation(v10)
	node2.setAnimationSpeed(20.0)
	selector3 = scene_manager.createTriangleSelector(node2)
	node2.setTriangleSelector(selector3)
	selector3.drop()

	m5 = scene_manager.getMesh("media//ninja.b3d")
	node3 = scene_manager.addAnimatedMeshSceneNode(m5, 0, IDFlag_IsPickable | IDFlag_IsHighlightable)
	v11 = vector3df(10.0, 10.0, 10.0)
	node3.setScale(v11)
	v12 = vector3df(-70.0,-66.0,-60.0)
	node3.setPosition(v12)
	v13 = vector3df(0.0,90.0,0.0)
	node3.setRotation(v13)
	node3.setAnimationSpeed(10.0)
	mt = node3.getMaterial(0)
	mt.NormalizeNormals = True
	selector4 = scene_manager.createTriangleSelector(node3)
	node3.setTriangleSelector(selector4)
	selector4.drop()

	itex = ITexture(0)
	material.setTexture(0, itex)
	material.Lighting = False

	v14 = vector3df(-60.0,100.0,400.0)
	scf = SColorf(1.0,1.0,1.0,1.0)
	light = scene_manager.addLightSceneNode(0, v14, scf, 600.0)
	light.setID(ID_IsNotPickable)

	highlightedSceneNode = ISceneNode(0)
	collMan = scene_manager.getSceneCollisionManager()
	lastFPS = -1

	material.Wireframe = True

	scolor = SColor()
	ray = line3df()
	intersection = vector3df()
	hitTriangle = triangle3df()
	mtrx = matrix4()
	sc_red = SColor(0,255,0,0)
	while device.run():
		if device.isWindowActive():
			driver.beginScene(True, True, scolor)
			scene_manager.drawAll()

			if highlightedSceneNode:
				highlightedSceneNode.setMaterialFlag(EMF_LIGHTING, True)
				highlightedSceneNode = 0

			ray.start = camera.getPosition()
			ray.end = ray.start + (camera.getTarget() - ray.start).normalize() * 1000.0

			try:
				selectedSceneNode = collMan.getSceneNodeAndCollisionPointFromRay(ray, intersection, hitTriangle, IDFlag_IsPickable, 0)
				if selectedSceneNode:
					#~ print intersection
					billboard.setPosition(intersection)
					driver.setTransform(ETS_WORLD, mtrx)
					driver.setMaterial(material)
					driver.draw3DTriangle(hitTriangle, sc_red)
					if (selectedSceneNode.getID() & IDFlag_IsHighlightable) == IDFlag_IsHighlightable:
						highlightedSceneNode = selectedSceneNode
						highlightedSceneNode.setMaterialFlag(EMF_LIGHTING, False)
			except Exception, e:
				print e

			driver.endScene()

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

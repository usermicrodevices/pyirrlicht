import os
os.environ['IRRLICHT_C_LIBRARY'] = 'irrlicht_c_173'

from pyirrlicht import *

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL


def main():
	#~ print("Please press 'y' if you want to use realtime shadows.")
	#~ shadows = True
	shadows = False

	if driverType == EDT_COUNT:
		return 1

	device = createDevice(driverType, dimension2du(640, 480), 16, False, shadows)

	if not device:
		return 1

	driver = device.getVideoDriver()
	smgr = device.getSceneManager()

	mesh = smgr.getMesh("media/room.3ds")

	if mesh:
		smgr.getMeshManipulator().makePlanarTextureMapping(mesh.getMesh(0), 0.004)
		node = smgr.addAnimatedMeshSceneNode(mesh)
		if node:
			node.setMaterialTexture(0, driver.getTexture("media/wall.jpg"))
			node.getMaterial(0).SpecularColor.set(0,0,0,0)

	mesh = smgr.addHillPlaneMesh("myHill", dimension2df(20,20), dimension2du(40,40), textureRepeatCount = dimension2df(10,10))
	#~ mesh = smgr.addHillPlaneMesh("myHill", dimension2df(20,20), dimension2du(40,40), SMaterial(0), 0.0, dimension2df(0.0, 0.0), dimension2df(10,10))
	if mesh:
		node = smgr.addWaterSurfaceSceneNode(mesh.getMesh(0), 3.0, 300.0, 30.0)
		node.setPosition(vector3df(0,7,0))
		node.setMaterialTexture(0, driver.getTexture("media/stones.jpg"))
		node.setMaterialTexture(1, driver.getTexture("media/water.jpg"))
		node.setMaterialType(EMT_REFLECTION_2_LAYER)

	node = smgr.addLightSceneNode(0, vector3df(0,0,0), SColorf(1.0, 0.6, 0.7, 1.0), 800.0)
	if node:
		anim = smgr.createFlyCircleAnimator(vector3df(0,150,0), 250.0)
		node.addAnimator(anim)
		anim.drop()

		node = smgr.addBillboardSceneNode(node, dimension2df(50, 50))
		if node:
			node.setMaterialFlag(EMF_LIGHTING, False)
			node.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
			node.setMaterialTexture(0, driver.getTexture("media/particlewhite.bmp"))

	ps = smgr.addParticleSystemSceneNode(False)
	em = ps.createBoxEmitter(aabbox3df(-7,0,-7,7,1,7), vector3df(0.0,0.06,0.0), 80, 100, SColor(0,255,255,255), SColor(0,255,255,255), 800, 2000, 0, dimension2df(10.0,10.0), dimension2df(20.0,20.0))
	ps.setEmitter(em)
	em.drop()

	paf = ps.createFadeOutParticleAffector()
	ps.addAffector(paf)
	paf.drop()

	ps.setPosition(vector3df(-70,60,40))
	ps.setScale(vector3df(2,2,2))
	ps.setMaterialFlag(EMF_LIGHTING, False)
	ps.setMaterialFlag(EMF_ZWRITE_ENABLE, False)
	ps.setMaterialTexture(0, driver.getTexture("media/fire.bmp"))
	ps.setMaterialType(EMT_TRANSPARENT_VERTEX_ALPHA)

	n = smgr.addVolumeLightSceneNode(0, -1, 32, 32, SColor(0, 255, 255, 255), SColor(0, 0, 0, 0))
	if n:
		n.setScale(vector3df(56.0, 56.0, 56.0))
		n.setPosition(vector3df(-120,50,40))

		textures = array(ITexture)
		#~ for g in range(1, 8):
			#~ textures.push_front(driver.getTexture('media/portal%d.bmp' % g))
		for g in range(7, 0, -1):
			textures.push_back(driver.getTexture('media/portal%d.bmp' % g))

		glow = smgr.createTextureAnimator(textures, 150)
		n.addAnimator(glow)
		glow.drop()

	mesh = smgr.getMesh("media/dwarf.x")
	if mesh:
		anode = smgr.addAnimatedMeshSceneNode(mesh)
		if anode:
			anode.setPosition(vector3df(-50,20,-60))
			anode.setAnimationSpeed(15)
			anode.addShadowVolumeSceneNode()
			smgr.setShadowColor(SColor(150,0,0,0))
			anode.setScale(vector3df(2,2,2))
			anode.setMaterialFlag(EMF_NORMALIZE_NORMALS, True)

	camera = smgr.addCameraSceneNodeFPS()
	camera.setPosition(vector3df(-50,50,-150))

	device.getCursorControl().setVisible(False)

	lastFPS = -1

	while device.run():
		if device.isWindowActive():
			driver.beginScene(True, True)
			smgr.drawAll()
			driver.endScene()
			fps = driver.getFPS()
			if lastFPS != fps:
				device.setWindowCaption("Irrlicht Engine - SpecialFX example [%s] FPS:%d" % (driver.getName(), fps))
				lastFPS = fps

	device.drop()
	return 0


if __name__ == "__main__":
	main()

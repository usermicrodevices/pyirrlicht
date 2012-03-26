# original on http://zenprogramming.tripod.com

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

	windowSize = dimension2du(640, 480)
	device = createDevice(driverType, windowSize)

	driver = device.getVideoDriver()
	smgr = device.getSceneManager()

	mesh = smgr.addHillPlaneMesh("Hill",
		dimension2df(20,20),
		dimension2du(20,20), SMaterial(0), 20,
		dimension2df(2,2),
		dimension2df(1,1))

	node = smgr.addAnimatedMeshSceneNode(mesh)
	node.setPosition(vector3df(0,7,0))

	node.setMaterialTexture(0,	driver.getTexture("media/snow.bmp"))

	node.setMaterialFlag(EMF_LIGHTING, False)


	ps = smgr.addParticleSystemSceneNode(False)
	ps.setPosition(vector3df(-160,170,80))
	ps.setScale(vector3df(2,2,2))

	ps.setParticleSize(dimension2df(5.0, 5.0))

	em = ps.createBoxEmitter(
		#~ aabbox3df(-270,-200,-270,270,300,300), 
		aabbox3df(-170,-100,-170,170,200,200), 
		vector3df(0.01,-0.02,0.0), 400, 800, 
		SColor(0,255,255,255), SColor(0,255,255,255), 100, 1000)#, 1800, 3000)

	ps.setEmitter(em)
	em.drop()

	paf = ps.createGravityAffector(vector3df(-0.05,-0.03, 0.0), 2000)

	ps.addAffector(paf)
	paf.drop()

	ps.setMaterialFlag(EMF_LIGHTING, False)
	ps.setMaterialTexture(0, driver.getTexture("media/snowparticle.bmp"))
	ps.setMaterialType(EMT_TRANSPARENT_VERTEX_ALPHA)

	mesh = smgr.getMesh("media/snowman.3ds")

	anode = smgr.addAnimatedMeshSceneNode(mesh)
	anode.setPosition(vector3df(-50,45,-60))
	anode.setMaterialTexture(0, driver.getTexture("media/snowman.jpg"))
	anode.setMaterialFlag(EMF_LIGHTING, False)


	skyboxNode = smgr.addSkyBoxSceneNode(
		driver.getTexture("media/mountain.jpg"),
		driver.getTexture("media/mountain.jpg"),
		driver.getTexture("media/mountainleft.jpg"),
		driver.getTexture("media/mountainright.jpg"),
		driver.getTexture("media/mountainmid.jpg"),
		driver.getTexture("media/mountain.jpg"))

	#~ camera = smgr.addCameraSceneNode(0, vector3df(-50, 80, -200), vector3df(0, 0, 250))
	camera = smgr.addCameraSceneNodeFPS()
	camera.setPosition(vector3df(-50,80,-150))

	lastFPS = -1

	while device.run():
		if device.isWindowActive():
			if driver.beginScene(True, True):
				smgr.drawAll()
				driver.endScene()
			device.sleep(50)
			fps = driver.getFPS()
			if fps != lastFPS:
				device.setWindowCaption("Example from http://zenprogramming.tripod.com - Irrlicht Engine(fps:%d) Triangles:%d" % (fps, driver.getPrimitiveCountDrawn()))
				lastFPS = fps
		else:
			device.yield_self()

	device.drop()
	
	return 0


if __name__ == "__main__":
	main()

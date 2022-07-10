from pyirrlicht import *


#driverType = EDT_NULL
#driverType = EDT_SOFTWARE
#driverType = EDT_BURNINGSVIDEO
#driverType = EDT_DIRECT3D8
#driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL


def main():

	device = createDevice(driverType, dimension2du(640, 480))
	driver = device.getVideoDriver()
	smgr = device.getSceneManager()
	camera = smgr.addCameraSceneNodeFPS()
	camera.setPosition(vector3df(50,200,50))
	#camera = smgr.addCameraSceneNodeMaya()
	#camera.setTarget(vector3df(50,200,50))
	m = SMaterial()
	m.Lighting = False
	matrix = matrix4()
	while device.run():
		driver.beginScene(True, True, SColor(255,0,0,255))
		driver.setMaterial(m)# for valid color
		driver.setTransform(ETS_WORLD, matrix)# for valid detection 3d coords
		driver.draw3DBox(aabbox3df(0,0,0,100,0,100), SColor(128,255,0,0))
		smgr.drawAll()
		driver.endScene()
	device.drop()
	
	return 0


if __name__ == "__main__":
	main()

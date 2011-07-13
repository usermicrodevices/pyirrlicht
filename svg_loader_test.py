from pyirrlicht import *

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

windowSize = dimension2du(320, 240)
device = createDevice(driverType, windowSize, 16, False, False, False, 0)
if device:
	device.setWindowCaption('Irrlicht Engine - SVG Loader Demo')
	device.setResizable(True)
	video_driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()

	# add SVG Image loader here for normal work such functions as getTexture
	video_driver.addAggSvgImageLoader()

	i_texture = video_driver.getTexture('bee.svg')
	if i_texture:
		i_texture_size = i_texture.getOriginalSize()

	rect = recti(0,0,i_texture_size.X,i_texture_size.Y)

	scolor = SColor(255,120,102,136)
	img_scolor = SColor(255,255,255,255)

	cursor_control = device.getCursorControl()

	while device.run():
		if device.isWindowActive():
			if video_driver.beginScene(True, True, scolor):
				x, y = cursor_control.getPosition().get_XY()
				video_driver.draw2DImage(i_texture, position2di(int(x-i_texture_size.X/2),int(y-i_texture_size.Y/2)), rect, 0, img_scolor, True)
				video_driver.endScene()
			device.sleep(100)
		else:
			device.yield_self()
	device.drop()
else:
	print('ERROR createDevice')

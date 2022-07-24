from pyirrlicht import *

#driverType = EDT_NULL
driverType = EDT_SOFTWARE
#driverType = EDT_BURNINGSVIDEO
#driverType = EDT_DIRECT3D8
#driverType = EDT_DIRECT3D9
#driverType = EDT_OPENGL

windowSize = dimension2du(512, 384)
device = createDevice(driverType, windowSize, 16, False, False, False, 0)
if device:
	device.setWindowCaption('Irrlicht Engine - 2D Graphics Demo')
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()
	i_texture = driver.getTexture("..//irrlicht//media//2ddemo.png")

	driver.makeColorKeyTexture(i_texture, position2di(0,0))

	i_gui_font = guienv.getBuiltInFont()
	i_gui_font2 = guienv.getFont("..//irrlicht//media//fonthaettenschweiler.bmp")

	text1pos = recti(130,10,300,50)
	text1color = SColor(255,255,255,255)
	text2pos = recti(130,20,300,60)

	imp1 = recti(349,15,385,78)
	imp2 = recti(387,15,423,78)

	scolor = SColor(255,120,102,136)
	scolor_2drectangle = SColor(100,255,255,255)

	cursor_control = device.getCursorControl()

	while device.run():
		if device.isWindowActive():
			if driver.beginScene(True, True, scolor):
				time = device.getTimer().getTime()
				driver.draw2DImage(i_texture, position2di(50,50), recti(0,0,342,224), 0, SColor(255,255,255,255), True)
				if time/500 % 2:
					imp = imp1
				else:
					imp = imp2
				driver.draw2DImage(i_texture, position2di(164,125),  imp, 0, SColor(255,255,255,255), True)
				driver.draw2DImage(i_texture, position2di(270,105), imp, 0, SColor(255,(time) % 255,255,255), True)
				if i_gui_font:
					i_gui_font.draw("This demo shows that Irrlicht is also capable of drawing 2D graphics.", text1pos, text1color)
				if i_gui_font2:
					i_gui_font2.draw("Also mixing with 3d graphics is possible.", text2pos, SColor(255,time % 255,time % 255,255))
				#driver.enableMaterial2D()
				driver.draw2DImage(i_texture, position2di(10,10), recti(354,87,442,118))
				#driver.enableMaterial2D(False)
				#x, y = cursor_control.getPosition().get_XY()
				#driver.draw2DRectangle(scolor_2drectangle, recti(x-20, y-20, x+20, y+20))
				pos = cursor_control.getPosition()
				driver.draw2DRectangle(scolor_2drectangle, recti(pos.X-20, pos.Y-20, pos.X+20, pos.Y+20))
				driver.endScene()
			device.sleep(50)
		else:
			device.yield_self()
	device.drop()
else:
	print('ERROR createDevice')

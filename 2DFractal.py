#!/usr/bin/env python
#Fractalss ver 0.1
#Vadim Kataev 2006
#www.compuvisor.net
#www.technopedia.org
#vkataev at gmail.com

# adaptation for pyirrlicht - Maxim Kolosov 2011
# http://pir.sourceforge.net

#we use following fact:
# x ** ((0 + 1j) * t) = sinusoid movement
# x != 0,1


from pyirrlicht import *

IMG_WIDTH = 160
IMG_HEIGHT = 160
CENTER_X = IMG_WIDTH/2
CENTER_Y = IMG_HEIGHT/2

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

max_iteration = 70
scale = 3.0/(IMG_HEIGHT*500.0)


def iteration_color(c):
	i = 0
	z = 0
	mag = 0.0
	while mag < 4.0 and i < max_iteration:
		z = z**2 + c
		mag = z.imag * z.imag + z.real * z.real
		i = i + 1
	return i

def set_color(i, a = 128):
	if i == max_iteration:
		return SColor(a, 0, 0, 0)
	else:
		c = int(i * 15)
		r = 255
		g = 255 - c
		b = 255
		if r < 0:
			r = 0
			g = 510 - c
			if g < 0:
				g = 0
				b = 765 - c
				if b < 0:
					r = g = b = 0
		return SColor(a, r, g, b)


windowSize = dimension2du(320, 240)
device = createDevice(driverType, windowSize, 32, False, False, False, 0)

if device:
	device.setWindowCaption('Please wait...')
	device.setResizable(True)
	video_driver = device.getVideoDriver()

	video_driver.SetIcon(IDI_EXCLAMATION)
	#~ SetIcon1(video_driver, IDI_EXCLAMATION)

	j = 0 + 1j
	blend = True
	image_size = dimension2du(IMG_WIDTH, IMG_HEIGHT)
	image = video_driver.createImage(ECF_R8G8B8, image_size)
	def texture_fractal():
		for row in range(IMG_HEIGHT):
			for column in range(IMG_WIDTH):
				x = (column - CENTER_X) * scale - 0.001
				y = (row - CENTER_Y) * scale - 0.75
				c = x + y * j
				image.setPixel(row, column, set_color(iteration_color(c)), blend)
		texture = video_driver.addTexture('fractal', image)
		image.drop()
		return texture

	scolor = SColor(255,120,102,136)
	img_color = SColor(255,255,255,255)
	rect = recti(0, 0, int(image_size.X), int(image_size.Y))

	tex = texture_fractal()

	device.setWindowCaption('Irrlicht Engine - 2D Fractal')
	while device.run():
		if device.isWindowActive():
			screen_size = video_driver.getScreenSize()
			x, y = device.getCursorControl().getPosition().get_XY()
			if x < 0 or y < 0 or x > screen_size.X or y > screen_size.Y:
				device.getCursorControl().setVisible(True)
			else:
				device.getCursorControl().setVisible(False)
			if video_driver.beginScene(True, True, scolor):
				video_driver.draw2DImage(tex, position2di(int(x-image_size.X/2),int(y-image_size.Y/2)), rect, 0, img_color, True)
				video_driver.endScene()
			device.sleep(50)
		else:
			device.yield_self()
	device.drop()
	device.closeDevice()
else:
	print('ERROR createDevice')

# from http://zenpython.blogspot.com/

import os
from pyirrlicht import *
from random import randrange as rand

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

def mazeDFS(width,height):
	stack   = []
	grid    = [[x%2*y%2 for x in range(width)] for y in range(height)]
	total   = ((width-1)/2)*((height-1)/2)
	cy      = rand(1,height,2)
	cx      = rand(1,width,2)
	visited = 1 

	while visited<total:
		possible= [[y,x] for y,x in
				  [[cy-2,cx],[cy,cx+2],[cy+2,cx],[cy,cx-2]]
				  if y>0 and x>0 and y<height-1 and x<width-1]

		neighbor= [[y,x] for y,x in possible if grid[y-1][x]!=2 and grid[y+1][x]!=2 and grid[y][x-1]!=2 and grid[y][x+1]!=2]

		if len(neighbor)>0:
			ny,nx   = neighbor[rand(0,len(neighbor))]
			wy      = ny if nx!=cx else (ny-1 if ny>cy else cy-1)
			wx      = nx if ny!=cy else (nx-1 if nx>cx else cx-1)

			grid[wy][wx] = 2
			stack.append([cy,cx])
			cy = ny
			cx = nx
			visited+=1
		else:
			cy,cx = stack.pop()

	grid[0][1] = 1
	grid[height-1][width-2] = 1
	return grid

def makeMaze(w, h, fore, back, scale = 0):
	window_size = dimension2du(800, 600)
	device = createDevice(driverType, window_size, 16, False, False, False, 0)
	if device:
		device.setWindowCaption('Please wait...')
		device.setResizable(True)
		video_driver = device.getVideoDriver()
		video_driver.SetIcon(IDI_EXCLAMATION)
		gui_environment = device.getGUIEnvironment()

		font_ext = '.ttf'
		font_path = os.environ['SYSTEMROOT']+'/Fonts/'
		font_file = font_path + 'arial' + font_ext
		gui_font = CGUITTFont(gui_environment, font_file, 20)
		if not gui_font:
			gui_font = gui_environment.getBuiltInFont()

		skin = gui_environment.getSkin()
		skin.setFont(gui_font)
		gui_font.drop()

		if scale != 0:
			w, h = int(w/scale), int(h/scale)
		width = w if w%2 else w-1
		height = h if h%2 else h-1

		if width < 3 or height < 3:
			print('Error: Width/Height too small given Scale.')
			return

		grid = mazeDFS(width, height)
		data = [back if grid[y][x] else fore for y in range(height) for x in range(width)]

		color_format = ECF_R8G8B8
		image_size = dimension2du(width, height)
		image = video_driver.createImage(color_format, image_size)
		alpha = 0
		blend = False
		if image.getColorFormat() in (ECF_A1R5G5B5, ECF_A8R8G8B8, ECF_A16B16G16R16F, ECF_A32B32G32R32F):
			alpha = alpha_value
			blend = True
		i = 0
		for row in range(image_size.Height):
			for column in range(image_size.Width):
				red, green, blue = data[i]
				image.setPixel(column, row, SColor(alpha, red, green, blue), blend)
				i = i + 1

		texture_name = '2d_maze'
		stored_file_name = texture_name + '.png'
		texture = None
		if scale != 0:
			image_size.X, image_size.Y = image_size.X * scale, image_size.Y * scale
			scale_image = video_driver.createImage(color_format, image_size)
			image.copyToScaling(scale_image)
			texture = video_driver.addTexture(texture_name, scale_image)
			video_driver.writeImageToFile(scale_image, stored_file_name)
			scale_image.drop()
		else:
			texture = video_driver.addTexture(texture_name, image)
			video_driver.writeImageToFile(image, stored_file_name)
		image.drop()
		#~ print('maze saved in a file %s' % stored_file_name)
		gui_environment.addMessageBox('Warning', 'maze saved in a file %s' % stored_file_name)

		scolor = SColor(255,120,100,130)
		img_color = SColor(255,255,255,255)
		rect = recti(0, 0, int(image_size.X), int(image_size.Y))
		texture_position = position2di(3, 3)

		device.setWindowCaption('Irrlicht Engine - 2D Maze generator')
		#~ _createScreenShot = True
		while device.run():
			if device.isWindowActive():
				#~ screen_size = video_driver.getScreenSize()
				#~ x, y = device.getCursorControl().getPosition().get_XY()
				#~ if x < 0 or y < 0 or x > screen_size.X or y > screen_size.Y:
					#~ device.getCursorControl().setVisible(True)
				#~ else:
					#~ device.getCursorControl().setVisible(False)
				if video_driver.beginScene(True, True, scolor):
					#~ video_driver.draw2DImage(texture, position2di(int(x-image_size.X/2),int(y-image_size.Y/2)), rect, 0, img_color, True)
					video_driver.draw2DImage(texture, texture_position, rect, 0, img_color, True)
					#~ if _createScreenShot:
						#~ _createScreenShot = False
						#~ video_driver.writeImageToFile(video_driver.createScreenShot(), '2d_maze_screen_shot.png')
					gui_environment.drawAll()
					video_driver.endScene()
				device.sleep(100)
			else:
				device.yield_self()
		device.drop()
		device.closeDevice()
	else:
		print('ERROR createDevice')

if __name__ == '__main__':
	makeMaze(800, 600, (0,0,255), (225,225,225), 20)

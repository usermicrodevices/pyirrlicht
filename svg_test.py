from pyirrlicht import *

if not BUILD_WITH_AGG:
	print('Current version build without simple AGG SVG support.\nSee _COMPILE_WITH_AGG_ flag into irrlicht_c.h C++ header file.')
else:
	#~ driverType = EDT_NULL
	driverType = EDT_SOFTWARE
	#~ driverType = EDT_BURNINGSVIDEO
	#~ driverType = EDT_DIRECT3D8
	#~ driverType = EDT_DIRECT3D9
	#~ driverType = EDT_OPENGL

	use_parameters = True

	device = None
	windowSize = dimension2du(640, 580)

	if use_parameters:
		p = SIrrlichtCreationParameters()
		#~ p.DeviceType = 0
		p.DriverType = driverType
		p.WindowSize = windowSize
		p.Bits = 16
		#~ p.ZBufferBits = False
		#~ p.Fullscreen = False
		#~ p.Stencilbuffer = False
		#~ p.Vsync = False
		p.AntiAlias = 4
		device = createDeviceEx(p)
	else:
		device = createDevice(driverType, windowSize, 16, False, False, False, 0)

	if device:
		device.setWindowCaption('Irrlicht Engine - SVG Demo')
		device.setResizable(True)
		video_driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		guienv = device.getGUIEnvironment()

		svg_file_name = 'tiger.svg'
		path_renderer = svg_path_renderer_from_file(svg_file_name)
		try:
			path_renderer = svg_path_renderer_from_file(svg_file_name)
		except:
			print('ERROR svg_path_renderer_from_file %s' % svg_file_name)
			if 'win' in platform:
				raise ctypes.WinError()
		image = svg_IImage(path_renderer, video_driver)
		i_texture = video_driver.addTexture(svg_file_name, image)
		image.drop()
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

#~ import sys
#~ sys.stdout.close()
#~ sys.stdout = open("irr_log.txt", "w")

from pyirrlicht import *

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

def test():
	p = SIrrlichtCreationParameters()
	p.DriverType = driverType
	p.WindowSize = dimension2du(320, 240)
	p.AntiAlias = 2
	p.WithAlphaChannel = True
	device = createDeviceEx(p)
	if device:
		video_driver = device.getVideoDriver()
		device.setResizable(True)
		color = SColor(255,100,100,140)
		#~ svg_file_name = 'tiger.svg'
		#~ svg_file_name = 'cartoon_tiger.svg'
		svg_file_name = 'bee.svg'
		s = svg_agg_image(video_driver, device.getFileSystem(), svg_file_name, True, 0, ECF_A8R8G8B8, 4)
		s.scale_rateably(2.2)
		tex = s.get_texture()
		if tex:
			tex_size = tex.getOriginalSize()
			try:
				rect = GetIrrWindowRect(video_driver)
				MoveWindow(video_driver, rect.left, rect.top, tex_size.X, tex_size.Y + 20, True)
			except:
				print('GetIrrWindowRect and MoveWindow only for windows platform.')
			while device.run():
				if device.isWindowActive():
					if video_driver.beginScene(True, True, color):
						video_driver.draw2DImage(tex, position2di(0,0), recti(0,0,int(tex_size.X),int(tex_size.Y)), useAlphaChannelOfTexture = True)
						video_driver.endScene()
					device.sleep(50)
				else:
					device._yield()
		else:
			print('ERROR CREATE TEXTURE FROM %s' % svg_file_name)
		device.closeDevice()
		device.drop()
	else:
		print ('ERROR createDevice')

if __name__ == "__main__":
	if BUILD_WITH_IRR_SVG_AGG:
		test()
	else:
		print('WARNING: irrlicht_c library build without AGG SVG support')

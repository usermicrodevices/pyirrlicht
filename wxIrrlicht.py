import wx
from pyirrlicht import *

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL


SW_HIDE            = 0
SW_SHOWNORMAL      = 1
SW_NORMAL          = 1
SW_SHOWMINIMIZED   = 2
SW_SHOWMAXIMIZED   = 3
SW_MAXIMIZE        = 3
SW_SHOWNOACTIVATE  = 4
SW_SHOW            = 5
SW_MINIMIZE        = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA          = 8
SW_RESTORE         = 9
SW_SHOWDEFAULT     = 10
SW_FORCEMINIMIZE   = 11
SW_MAX             = 11

if 'wxMSW' in wx.PlatformInfo:
	user32_module = ctypes.WinDLL('user32')
	ShowWindow = ctypes.WINFUNCTYPE(ctypes.c_byte, ctypes.c_void_p, ctypes.c_int)(('ShowWindow', user32_module))
	SetParent = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SetParent', user32_module))
	SetFocus = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(('SetFocus', user32_module))
	SetActiveWindow = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(('SetActiveWindow', user32_module))
	SetForegroundWindow = ctypes.WINFUNCTYPE(ctypes.c_byte, ctypes.c_void_p)(('SetForegroundWindow', user32_module))


#~ from wx import glcanvas
#~ class irrlicht_canvas(glcanvas.GLCanvas):
class irrlicht_canvas(wx.ScrolledWindow):
#~ class irrlicht_canvas(wx.Button):
	def __init__(self, *args, **kwargs):
		super(irrlicht_canvas, self).__init__(*args, **kwargs)
		self.scale_x = 1.0
		self.scale_y = 1.0
		self.scale_delta = 0.05
		#~ self.SetScrollRate(20, 20)
		self.param = SIrrlichtCreationParameters()
		self.param.DriverType = driverType
		if (self.param.DriverType == EDT_OPENGL):
			self.param.WindowId = self.GetHandle()
		self.param.IgnoreInput = True
		self.device = createDeviceEx(self.param)
		if self.device:
			self.device.setWindowCaption('Quake 3 Map! - Irrlicht Engine Demo')
			self.device.setResizable(True)
			#~ self.device.getCursorControl().setVisible(False)
			self.scene_manager = self.device.getSceneManager()
			#~ self.guienv = self.device.getGUIEnvironment()
			self.driver = self.device.getVideoDriver()
			self.video_data = self.driver.getExposedVideoData()
			#~ self.video_data.D3D9.HWnd = self.GetHandle()
			#~ print ('OpenGLWin32', self.video_data.OpenGLWin32.HWnd)
			#~ print ('D3D9', self.video_data.D3D9.HWnd)
			#~ print ('GetHandle', self.driver.GetHandle())
			print (SetParent(self.driver.GetHandle(), self.GetHandle()))
			#~ print (SetParent(self.driver.GetHandle(), self.GetParent().GetHandle()))
			#~ print (ctypes.FormatError())
			#~ print (SetActiveWindow(self.driver.GetHandle()))
			#~ print (ctypes.FormatError())
			#~ print (SetFocus(self.driver.GetHandle()))
			#~ print (ctypes.FormatError())
			self.ScreenSize = self.driver.getViewPort().getSize()
			self.SetVirtualSize((self.ScreenSize.X, self.ScreenSize.Y))
			#~ self.camera = self.scene_manager.addCameraSceneNodeFPS()
			self.camera = self.scene_manager.addCameraSceneNodeMaya()
			#~ self.camera = self.scene_manager.addCameraSceneNode()
			self.scolor = SColor(255, 200, 200, 200)
			self.device.getFileSystem().addZipFileArchive('media//map-20kdm2.pk3')
			i_animated_mesh = self.scene_manager.getMesh('20kdm2.bsp')
			if i_animated_mesh:
				i_mesh = i_animated_mesh.getMesh(0)
				if i_mesh:
					i_meshscene_node = self.scene_manager.addOctTreeSceneNode(i_mesh, 0, -1, 1024)
					if i_meshscene_node:
						i_meshscene_node.setPosition(vector3df(-1300.0, -144.0, -1249.0))
					else:
						print ('ERROR result method addOctTreeSceneNode2, SceneManager')
				else:
					print ('ERROR result method getMesh, IAnimatedMesh')
			else:
				print ('ERROR result method getMesh, SceneManager')
		else:
			print ('ERROR createDevice')

		self.Bind(wx.EVT_IDLE, self.event_idle)
		self.Bind(wx.EVT_SIZE, self.event_size)
		#~ self.Bind(wx.EVT_PAINT, self.event_paint)
		#~ self.Bind(wx.EVT_MOUSEWHEEL, self.event_mousewheel)
		#~ self.SetFocus()

	def __del__(self):
		self.device.closeDevice()
		self.device.drop()

	def event_paint(self, event):
		if self.device:
			#~ self.device.getTimer().tick()
			#~ if self.device.isWindowActive():
			if self.device.run():
				self.driver.beginScene(True, True, self.scolor)
				self.scene_manager.drawAll()
				#~ self.guienv.drawAll()
				self.driver.endScene()
				#~ self.device.sleep(100)
			event.Skip()

	def event_size(self, event):
		if self.device:
			event_size = event.GetSize()
			w = event_size.GetWidth()
			h = event_size.GetHeight()
			self.ScreenSize = dimension2du(w, h)
			self.driver.OnResize(self.ScreenSize)
			#~ self.driver.setViewPort(recti(0, 0, w, h))
			self.scene_manager.getActiveCamera().setAspectRatio(float(w)/float(h))
			self.device.run()

	def event_idle(self, event):
		if self.device:
			#~ self.device.getTimer().tick()
			#~ if self.device.isWindowActive():
			#~ if self.device.run():
			self.driver.beginScene(True, True, self.scolor)
			self.scene_manager.drawAll()
			#~ self.guienv.drawAll()
			self.driver.endScene()
			self.device.sleep(100)
			#~ else:
				#~ self.device.yield_self()
			#~ event.RequestMore()

	def event_mousewheel(self, event):
		old_x, old_y = self.scale_x, self.scale_y
		if event.GetWheelRotation() > 0:
			self.scale_x += self.scale_delta
			self.scale_y += self.scale_delta
		else:
			self.scale_x -= self.scale_delta
			self.scale_y -= self.scale_delta
			if self.scale_x < self.scale_delta:
				self.scale_x = self.scale_delta
			if self.scale_y < self.scale_delta:
				self.scale_y = self.scale_delta
		if (self.scale_x, self.scale_y) != (old_x, old_y):
			self.scale()

	def scale(self):
		pass


def main():
	from wx.lib.scrolledpanel import ScrolledPanel
	app = wx.PySimpleApp()
	frame = wx.Frame(None, wx.ID_ANY, 'wxPython Irrlicht canvas')
	#~ sizer = wx.GridSizer(1, 1)
	#~ canvas = irrlicht_canvas(frame)
	panel = ScrolledPanel(frame, wx.ID_ANY)
	sizer = wx.GridSizer(1, 1)
	canvas = irrlicht_canvas(panel)
	sizer.Add(canvas, 0, wx.EXPAND | wx.ALL)
	panel.SetSizer(sizer)
	panel.SetAutoLayout(1)
	panel.SetupScrolling()
	#~ frame.SetSizer(sizer)
	#~ frame.SetAutoLayout(1)
	app.SetTopWindow(frame)
	#~ frame.SetIcon(wx.IconFromBitmap(svg_to_bitmap(logo, (32, 32), use_cairo = False)))
	#~ frame.SetSize(canvas.GetVirtualSize())
	frame.Show()
	app.MainLoop()


if __name__=='__main__':
	main()

# Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license

import os, sys
from pyirrlicht import *
from locale import getdefaultlocale

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

GUI_ID_QUIT = 0x10000
GUI_ID_ABOUT = 0x10001
GUI_ID_LOAD = 0x10002
GUI_ID_SAVE = 0x10003
GUI_ID_CAMERA_NONE = 0x10004
GUI_ID_CAMERA_MAYA = 0x10005
GUI_ID_CAMERA_FPS = 0x10006
GUI_ID_LOG = 0x10007
GUI_ID_DRIVER = 0x10008
GUI_ID_EDT_SOFTWARE = GUI_ID_DRIVER | EDT_SOFTWARE
GUI_ID_EDT_BURNINGSVIDEO = GUI_ID_DRIVER | EDT_BURNINGSVIDEO
GUI_ID_EDT_DIRECT3D9 = GUI_ID_DRIVER | EDT_DIRECT3D9
GUI_ID_EDT_OPENGL = GUI_ID_DRIVER | EDT_OPENGL
GUI_ID_SOUND_ON_OFF = 0x1000E
GUI_ID_TEXTURE_FROM_FILE = 0x1000F
GUI_ID_MENU_SOUND_VOLUME = 0x10010
GUI_ID_WINDOW_SOUND_VOLUME = 0x10011
GUI_ID_SOUND_VOLUME = 0x10012

app_name = os.path.basename(sys.argv[0].split('.')[0])

# simple language translator
default_locale = getdefaultlocale()[0]
translation_catalog = 'lang'
if not os.path.isdir(translation_catalog):
	os.mkdir(translation_catalog)
translation_catalog += '//'# only for python 2.4.4 version and isdir function
translation_file_name = translation_catalog + app_name + '_' + default_locale + '.lng'
if not os.path.exists(translation_file_name):
	default_locale = 'en_US'
	translation_file_name = translation_catalog + app_name + '_' + default_locale + '.lng'
if not os.path.exists(translation_file_name):
	f = open(translation_file_name, 'w')
	f.close()
translation_file = open(translation_file_name, 'r+')
translations = {}
for line in translation_file.readlines():
	if len(line.strip()) > 2 and line.find('='):
		key, value = line.split('=', 1)
		translations[key.strip()] = value.strip()
def _(source = ''):
	if not source in translations:
		translation_file.write('\n' + source + ' = ' + source + '\n')
		translation_file.flush()
		translations[source] = source
	try:
		return unicode(translations[source], 'cp1251')
	except:
		return translations[source]

class config(object):
	def __init__(self, *args, **kwargs):
		self.file_name = kwargs.pop('file_name', 'config.ini')
		self._items_ = {}
		self.load()
	def load(self):
		if os.path.exists(self.file_name):
			for line in open(self.file_name, 'r').readlines():
				if len(line.strip()) > 2 and line.find('='):
					key, value = line.split('=', 1)
					self._items_[key.strip()] = eval(value.strip())
	def read_from_file(self):
		result = {}
		if os.path.exists(self.file_name):
			for line in open(self.file_name, 'r').readlines():
				if len(line.strip()) > 2 and line.find('='):
					key, value = line.split('=', 1)
					result[key.strip()] = eval(value.strip())
		return result
	def save(self):
		f = open(self.file_name, 'w')
		for key, value in self._items_.items():
			f.write(key + ' = ' + repr(value) + '\n')
		f.close()
	def items(self):
		return self._items_.items()
	def get(self, key, default = ''):
		if not key in self._items_:
			self._items_[key] = default
			open(self.file_name, 'a').write(key + ' = ' + repr(default) + '\n')
		return self._items_[key]
	def get_bool(self, key, default = ''):
		return bool(self.get(key, default))
	def get_int(self, key, default = ''):
		return int(self.get(key, default))
	def get_long(self, key, default = ''):
		return long(self.get(key, default))
	def get_float(self, key, default = ''):
		return float(self.get(key, default))
	def set(self, key, value = ''):
		self._items_[key] = value
	def set_many(self, keys_values):
		if len(keys_values) > 0:
			for key, value in keys_values:
				self._items_[key] = value
	def keys(self):
		return self._items_.keys()
	def values(self):
		return self._items_.values()
	def has_key(self, key):
		return key in self._items_
	def __getitem__(self, key):
		if key in self._items_:
			return self._items_[key]
		else:
			return None
	def __setitem__(self, key, value):
		self._items_[key] = value
	def __delitem__(self, key):
		if key in self._items_:
			del self._items_[key]
	def __len__(self):
		return len(self._items_)
	def __contains__(self, key):
		return key in self._items_
	def close(self):
		items_from_file = self.read_from_file()
		if self._items_.keys() != items_from_file.keys() or self._items_.values() != items_from_file.values():
			self.save()

class UserIEventReceiver(IEventReceiver):
	app = None
	about_dialog = None
	show_cursor = False
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	def OnEvent(self, event_pointer):
		event = SEvent(event_pointer)
		if event.EventType is EET_MOUSE_INPUT_EVENT:
			if event.MouseInput.EventType is EMIE_MOUSE_WHEEL:
				if self.app.scale > 0.1:
					self.app.scale = self.app.scale + event.MouseInput.Wheel/10
					self.app.create_texture()
				else:
					self.app.scale = self.app.scale + 0.1
		elif event.EventType is EET_GUI_EVENT:
			gui_event_type = event.GUIEvent.EventType
			if gui_event_type in (EGET_MESSAGEBOX_YES, EGET_MESSAGEBOX_NO, EGET_MESSAGEBOX_OK, EGET_MESSAGEBOX_CANCEL):
				self.about_dialog = None
			elif gui_event_type == EGET_ELEMENT_LEFT:
				self.show_cursor = False
			elif gui_event_type == EGET_ELEMENT_HOVERED:
				self.show_cursor = True
			elif gui_event_type == EGET_MENU_ITEM_SELECTED:
				self.about_dialog = None
				menu = IGUIContextMenu(event.GUIEvent.Caller)
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				elif menu_id == GUI_ID_ABOUT:
					self.about_dialog = self.app.guienv.addMessageBox(_('About'), _('SVG Viewer'))
				elif menu_id == GUI_ID_LOAD:
					self.app.guienv.addFileOpenDialog(_('Please select a SVG file to open'), id = GUI_ID_LOAD)
				elif menu_id == GUI_ID_SAVE:
					self.app.guienv.addFileOpenDialog(_('Please write a file name to save'), id = GUI_ID_SAVE)
				elif menu_id == GUI_ID_EDT_SOFTWARE:
					self.app.set_device_type(EDT_SOFTWARE)
				elif menu_id == GUI_ID_EDT_OPENGL:
					self.app.set_device_type(EDT_OPENGL)
				elif menu_id == GUI_ID_EDT_DIRECT3D9:
					self.app.set_device_type(EDT_DIRECT3D9)
				elif menu_id == GUI_ID_EDT_BURNINGSVIDEO:
					self.app.set_device_type(EDT_BURNINGSVIDEO)
			elif gui_event_type == EGET_FILE_SELECTED:
				dialog = IGUIFileOpenDialog(event.GUIEvent.Caller)
				if dialog.getID() == GUI_ID_LOAD:
					self.app.open_file(dialog.getFileName())
				elif dialog.getID() == GUI_ID_SAVE:
					print(dialog.getFileName(), dialog.getDirectoryName())
					#~ self.app.guienv.addEditBox(_('Please write a file name to save'), recti(0, 50, 400, 100))
					#~ IImage* self.app.video_driver.createScreenShot()
					#~ IImage* self.app.video_driver.createImage(ITexture* texture, position2d<s32>& pos, dimension2d<u32>& size)
					#~ self.app.video_driver.writeImageToFile(IImage* image, const io::path& filename)
				else:
					print('it is not required', dialog.getID(), dialog.getTypeName(), dialog.getText())
		elif event.EventType is EET_KEY_INPUT_EVENT:
			self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode]

class app:
	def __init__(self, *args, **kwargs):
		self.config_file_name = kwargs.pop('config_file_name', 'svg_view.ini')
		self.config = config(file_name = self.config_file_name)
		self.time_delay = self.config.get_int('time_delay', 2)
		self.menu_options = None
		self.driver_type = self.config.get_int('driver_type', driverType)
		self.window_size = dimension2du(self.config.get_int('window_width', 640), self.config.get_int('window_height', 480))
		#~ self.device = createDevice(self.driver_type, self.window_size)
		p = SIrrlichtCreationParameters()
		p.DriverType = self.driver_type
		p.WindowSize = self.window_size
		p.AntiAlias = True
		self.device = createDeviceEx(p)
		self.menu_device_types = {}
		self.help_dialog = None
		self.scale = 1.0
		self.path_renderer = None
		self.i_texture = None
		self.texture_name = ''
		self.i_texture_size = dimension2du()
		self.texture_rect = recti(0,0,10,10)

	def __del__(self):
		if self.device:
			self.stop()

	def show_warning(self):
		self.guienv.addMessageBox(_('Warning'), _('For finish this operation you need restart game!'))

	def set_device_type(self, new_device_type = 0):
		self.driver_type = new_device_type
		for dev_type, menu_index in self.menu_device_types.items():
			self.menu_device_type.setItemChecked(menu_index, (self.driver_type == dev_type))
		self.config.set('driver_type', self.driver_type)
		self.config.save()
		self.show_warning()

	def create_texture(self):
		if self.path_renderer:
			if self.i_texture:
				self.video_driver.removeTexture(self.i_texture)
			#~ image = svg_IImage(self.path_renderer, self.video_driver, self.scale, rotate_value = 0.0, color_format = ECF_A8R8G8B8, stride_value = 1)
			#~ self.i_texture = self.video_driver.addTexture(self.texture_name, image)
			#~ image.drop()
			#~ del image
			self.i_texture = svg_ITexture(self.path_renderer, self.video_driver, self.texture_name, self.scale, rotate_value = 0.0, color_format = ECF_A8R8G8B8, stride_value = 1)
			if self.i_texture:
				self.i_texture_size = self.i_texture.getOriginalSize()
			self.texture_rect = recti(0,0,self.i_texture_size.X,self.i_texture_size.Y)
			#~ if self.scale > 0:
				#~ self.texture_rect.addInternalPoint(self.i_texture_size.X,self.i_texture_size.Y)
			#~ print('+++getTextureCount', self.video_driver.getTextureCount())

	def open_file(self, file_name):
		try:
			self.path_renderer = svg_path_renderer_from_file(file_name)
		except:
			if 'win' in platform:
				raise ctypes.WinError()
			print('ERROR svg_path_renderer_from_file %s' % file_name)
		else:
			self.texture_name = file_name
			self.scale = 1.0
			self.create_texture()
			self.guienv.addMessageBox(_('Warning'), _('Scrolling mouse for scale image.'))

	def start(self):
		if self.device:
			self.device.setWindowCaption(_(app_name))
			self.device.setResizable(True)
			self.video_driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.guienv = self.device.getGUIEnvironment()

			if is_frozen():
				self.video_driver.SetIcon(101)
			else:
				self.video_driver.SetIcon()

			self.font_size = 20
			font_ext = '.ttf'
			font_path = os.environ['SYSTEMROOT']+'/Fonts/'
			self.font_file = font_path + 'arial' + font_ext
			#~ self.font_file = font_path + 'cour' + font_ext
			#~ self.font_file = font_path + 'comic' + font_ext
			self.font = CGUITTFont(self.guienv, self.font_file, self.font_size)
			self.skin = self.guienv.getSkin()
			if self.font:
				self.skin.setFont(self.font)
				self.font.drop()
			else:
				print ('++++ ERROR vect_font not created !!!')
			menu_height = self.skin.getSize(EGDS_MENU_HEIGHT)

			self.menu = self.guienv.addMenu()
			self.menu.addItem(_('File'), -1, True, True)
			self.menu.addItem(_('View'), -1, True, True)
			self.menu.addItem(_('Options'), -1, True, True)
			self.menu.addItem(_('Help'), -1, True, True)

			submenu = self.menu.getSubMenu(0)
			submenu.addItem(_('Open svg file'), GUI_ID_LOAD)
			submenu.addItem(_('Save image'), GUI_ID_SAVE)
			submenu.addSeparator()
			submenu.addItem(_('Quit'), GUI_ID_QUIT)

			submenu = self.menu.getSubMenu(1)
			submenu.addItem(_('Camera off'), GUI_ID_CAMERA_NONE)
			submenu.addItem(_('Perspective view'), GUI_ID_CAMERA_MAYA)
			submenu.addItem(_('First Person view'), GUI_ID_CAMERA_FPS)

			self.menu_options = self.menu.getSubMenu(2)
			self.menu_options.addItem(_('Start/stop log'), GUI_ID_LOG)
			self.menu_options.addItem(_('Choose graphics driver'), GUI_ID_DRIVER, True, True)
			self.menu_device_type = self.menu_options.getSubMenu(1)
			self.menu_device_types[EDT_SOFTWARE] = self.menu_device_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (self.driver_type == EDT_SOFTWARE))
			self.menu_device_types[EDT_OPENGL] = self.menu_device_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (self.driver_type == EDT_OPENGL))
			self.menu_device_types[EDT_DIRECT3D9] = self.menu_device_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (self.driver_type == EDT_DIRECT3D9))
			self.menu_device_types[EDT_BURNINGSVIDEO] = self.menu_device_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (self.driver_type == EDT_BURNINGSVIDEO))

			submenu = self.menu.getSubMenu(3)
			submenu.addItem(_('About'), GUI_ID_ABOUT)

			scolor = SColor(255,120,102,136)
			img_scolor = SColor(255,255,255,255)

			cursor_control = self.device.getCursorControl()

			i_event_receiver = UserIEventReceiver()
			i_event_receiver.app = self
			self.device.setEventReceiver(i_event_receiver)

			#~ print('===getTextureCount', self.video_driver.getTextureCount())

			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.IsKeyDown(KEY_ESCAPE):
						break
					if self.video_driver.beginScene(True, True, scolor):
						#~ texture = self.video_driver.getTexture(self.texture_name)
						#~ texture = self.video_driver.getTextureByIndex(1)
						if self.i_texture:
						#~ if texture:
							#~ screen_size = self.video_driver.getScreenSize()
							x, y = cursor_control.getPosition().get_XY()
							self.video_driver.draw2DImage(self.i_texture, position2di(int(x-self.i_texture_size.X/2),int(y-self.i_texture_size.Y/2)), self.texture_rect, 0, img_scolor, True)
							#~ self.video_driver.draw2DImage(texture, position2di(int(x-self.i_texture_size.X/2),int(y-self.i_texture_size.Y/2)), self.texture_rect, 0, img_scolor, True)
						self.guienv.drawAll()
						self.video_driver.endScene()
					self.device.sleep(10)
				else:
					self.device.yield_self()
		else:
			print('ERROR createDevice')

	def stop(self):
		if self.device:
			#~ self.device.drop()
			self.device.closeDevice()
			self.device = None
			if self.window_size.Width < 320:
				self.window_size.Width = 320
			if self.window_size.Height < 240:
				self.window_size.Height = 240
			self.config.set_many((('window_width', int(self.window_size.Width)), ('window_height', int(self.window_size.Height))))
		self.config.close()

def main():
	a = app()
	a.start()

if __name__ == "__main__":
	main()
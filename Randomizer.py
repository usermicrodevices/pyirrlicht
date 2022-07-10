# Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
# github.com/usermicrodevices
# BSD license

import os, sys
from pyirrlicht import *
from random import seed, randint
from locale import getdefaultlocale

try:
	import pybass
except:
	pybass = None
	print ('++++ PYBASS module not accessible!!!')

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
		#~ if not key in self._items_:
			#~ self._items_[key] = value
			#~ open(self.file_name, 'a').write(key + ' = ' + repr(value) + '\n')
		#~ else:
			#~ self._items_[key] = value
			#~ self.save()
		self._items_[key] = value
	def set_many(self, keys_values):
		if len(keys_values) > 0:
			for key, value in keys_values:
				self._items_[key] = value
			#~ self.save()
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
	game = None
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	NumbersKeys = {}
	value = 0
	for key in range(KEY_KEY_0, KEY_KEY_9 + 1):
		NumbersKeys[key] = str(value)
		value += 1
	value = 0
	for key in range(KEY_NUMPAD0, KEY_NUMPAD9 + 1):
		NumbersKeys[key] = str(value)
		value += 1
	answer = ''
	def OnEvent(self, event):
		if self.game.help_dialog:
			try:
				self.game.help_dialog.getID()
			except:
				self.game.help_dialog = None
		event_type = self.GetEventType(event)
		if event_type is EET_KEY_INPUT_EVENT:
			key_event = self.GetKeyInput(event)
			pressed_down = self.KeyInput_PressedDown(key_event)
			self.KeyIsDown[self.KeyInput_Key(key_event)] = pressed_down
			if self.KeyInput_Key(key_event) in (KEY_KEY_0, KEY_KEY_1, KEY_KEY_2, KEY_KEY_3, KEY_KEY_4, KEY_KEY_5, KEY_KEY_6, KEY_KEY_7, KEY_KEY_8, KEY_KEY_9, KEY_NUMPAD0, KEY_NUMPAD1, KEY_NUMPAD2, KEY_NUMPAD3, KEY_NUMPAD4, KEY_NUMPAD5, KEY_NUMPAD6, KEY_NUMPAD7, KEY_NUMPAD8, KEY_NUMPAD9) and not pressed_down:
				self.answer += self.NumbersKeys[self.KeyInput_Key(key_event)]
			elif self.KeyInput_Key(key_event) in (KEY_BACK, KEY_DELETE) and not pressed_down:
				self.answer = ''
			elif self.KeyInput_Key(key_event) == KEY_RETURN and not pressed_down and not self.game.help_dialog:
				check_answer = _('Correctly')
				self.answer_color = SColor(255, 0, 0, 255)
				if str(self.game.a * self.game.b) != self.answer:
					check_answer = _('Not correctly') + '\n' + _('Correctly answer is') + ' %d' % (self.game.a * self.game.b)
					self.answer_color = SColor(255, 255, 0, 0)
				else:
					self.game.create_tree()
					self.game.results += 1
				self.game.answer_exists = True
				self.answer_text = self.answer + '\n' + check_answer
				self.answer = ''
				self.game.a, self.game.b = randint(0, 9), randint(0, 9)
		elif event_type == EET_GUI_EVENT:
			GUIEvent = self.GetGUIEvent(event)
			gui_event_type = self.GUIEvent_EventType(GUIEvent)
			caller = self.GUIEvent_Caller(GUIEvent)
			id = caller.getID()
			if gui_event_type == EGET_SCROLL_BAR_CHANGED:
				#~ self.game.device.getLogger().log('=== EGET_SCROLL_BAR_CHANGED')
				scroll_bar = caller.as_IGUIScrollBar()
				if id == GUI_ID_SOUND_VOLUME:
					#~ self.game.device.getLogger().log('+++ GUI_ID_SOUND_VOLUME ' + str(scroll_bar.getPos()))
					self.game.set_sound_volume(scroll_bar.getPos())
			elif gui_event_type == EGET_MENU_ITEM_SELECTED:
				self.game.help_dialog = None
				menu = caller.as_IGUIContextMenu()
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				elif menu_id == GUI_ID_CAMERA_NONE:
					self.game.setActiveCameraOff()
					self.game.cursor_control.setVisible(True)
				elif menu_id == GUI_ID_CAMERA_MAYA:
					self.game.setActiveCamera(self.game.camera[0])
					self.game.cursor_control.setVisible(True)
				elif menu_id == GUI_ID_CAMERA_FPS:
					self.game.setActiveCamera(self.game.camera[1])
					self.game.cursor_control.setVisible(False)
				elif menu_id == GUI_ID_EDT_SOFTWARE:
					self.game.set_device_type(EDT_SOFTWARE)
				elif menu_id == GUI_ID_EDT_OPENGL:
					self.game.set_device_type(EDT_OPENGL)
				elif menu_id == GUI_ID_EDT_DIRECT3D9:
					self.game.set_device_type(EDT_DIRECT3D9)
				elif menu_id == GUI_ID_EDT_BURNINGSVIDEO:
					self.game.set_device_type(EDT_BURNINGSVIDEO)
				elif menu_id == GUI_ID_SOUND_ON_OFF:
					self.game.sound_on_off()
				elif menu_id == GUI_ID_MENU_SOUND_VOLUME:
					self.game.create_sound_volume()
				elif menu_id == GUI_ID_TEXTURE_FROM_FILE:
					self.game.set_textures()
				elif menu_id == GUI_ID_ABOUT:
					self.game.guienv.addMessageBox(_('About'), _('Magic Room - Randomizer'))
		elif event_type == EET_LOG_TEXT_EVENT:
			log_event = self.GetLogEvent(event)
			#~ if self.LogEvent_Level(log_event) == 0:
				#~ if 'Resizing window' in self.LogEvent_Text(log_event):
			if self.LogEvent_Level(log_event) == 0 and self.LogEvent_Text(log_event).find('Resizing window') > -1:
				self.game.window_size = self.game.driver.getScreenSize()
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode]

class game:
	def __init__(self, *args, **kwargs):
		self.config_file_name = kwargs.pop('config_file_name', 'randomiz.ini')
		self.config = config(file_name = self.config_file_name)
		self.time_delay = self.config.get_int('time_delay', 2)
		self.play_sound = self.config.get_bool('play_sound', True)
		self.texture_from_file = self.config.get_bool('texture_from_file', False)
		self.sound_volume = self.config.get_float('sound_volume', 1.0)
		self.sound_file = self.config.get('sound_file', 'media//sound.mod')
		self.bass_handle = None
		self.sound_playing = False
		self.menu_options = None
		if pybass:
			if pybass.BASS_Init(-1, 44100, 0, 0, 0):
				pybass.BASS_SetVolume(self.sound_volume)
				if os.path.isfile(self.sound_file):
					self.bass_handle = pybass.BASS_MusicLoad(False, self.sound_file, 0, 0, pybass.BASS_MUSIC_PRESCAN | pybass.BASS_SAMPLE_LOOP, 0)
					if self.play_sound:
						self.sound_play()
		self.device_type = self.config.get_int('device_type', EDT_OPENGL)
		self.window_size = dimension2du(self.config.get_int('window_width', 640), self.config.get_int('window_height', 480))
		self.device = createDevice(self.device_type, self.window_size)
		self.menu_device_types = {}
		self.help_dialog = None
		self.fog_enable = self.config.get_bool('fog_enable', True)
		self.fog_color = SColor(*self.config.get('fog_color', (0,255,255,255)))
		self.fog_type = self.config.get_int('fog_type', EFT_FOG_LINEAR)
		self.fog_start = self.config.get_float('fog_start', 500.0)
		self.fog_end = self.config.get_float('fog_end', 1000.0)
		self.fog_density = self.config.get_float('fog_density', 0.01)
		self.fog_pixel = self.config.get_bool('fog_pixel', False)
		self.fog_range = self.config.get_bool('fog_range', False)
		# random volume variable
		self.tile_count = randint(10, 50)
		# len tile
		self.tile_len = 100
		self.results = 0

	def __del__(self):
		if self.device:
			self.stop()
		#~ self.config.close()
		
	def set_sound_volume(self, value):
		self.sound_volume = value / 100.0
		if pybass:
			pybass.BASS_SetVolume(self.sound_volume)
		#~ print(self.config.get_float('sound_volume', 1.0), self.sound_volume)
		#~ if self.config.get_float('sound_volume', 1.0) != self.sound_volume:
		self.config.set('sound_volume', self.sound_volume)

	def create_sound_volume(self):
		#~ if not self.guienv.getRootGUIElement().getElementFromId(GUI_ID_WINDOW_SOUND_VOLUME, True):
		e = self.guienv.getRootGUIElement().getElementFromId(GUI_ID_WINDOW_SOUND_VOLUME, True)
		if e:
			e.remove()
		window = self.guienv.addWindow(recti(10,45,400,150), False, _('Sound volume window'), id = GUI_ID_WINDOW_SOUND_VOLUME)
		self.guienv.addStaticText(_('Select sound volume'), recti(10,30,380,60), True, False, window)
		scrollbar = self.guienv.addScrollBar(True, recti(10,80,380,100), window, GUI_ID_SOUND_VOLUME)
		#~ scrollbar.setMin(0)
		#~ scrollbar.setMax(100)
		scrollbar.setPos(int(self.sound_volume * 100))
		#~ scrollbar.setSmallStep(1)

	def set_textures(self):
		self.texture_from_file = not self.texture_from_file
		if self.menu_options:
			self.menu_options.setItemChecked(self.menu_texture_from_file, self.texture_from_file)
		self.show_warning()
		self.config.set('texture_from_file', self.texture_from_file)

	def sound_play(self):
		if self.bass_handle:
			self.sound_playing = pybass.BASS_ChannelPlay(self.bass_handle, False)

	def sound_on_off(self):
		if self.play_sound:
			self.play_sound = False
			if self.bass_handle and self.sound_playing:
				self.sound_playing = False
				pybass.BASS_ChannelStop(self.bass_handle)
		else:
			self.play_sound = True
			self.sound_play()
		if self.menu_options:
			self.menu_options.setItemChecked(self.menu_sound, self.play_sound)
		self.config.set('play_sound', self.play_sound)

	def show_warning(self):
		self.guienv.addMessageBox(_('Warning'), _('For finish this operation you need restart game!'))

	def set_device_type(self, new_device_type = 0):
		self.device_type = new_device_type
		for dev_type, menu_index in self.menu_device_types.items():
			self.menu_device_type.setItemChecked(menu_index, (self.device_type == dev_type))
		self.config.set('device_type', self.device_type)
		self.show_warning()
		#~ self.device.drop()
		#~ self.device.closeDevice()
		#~ self.device = createDevice(self.device_type, self.window_size)
		#~ self.start()

	def texture_generator(self, image_format = ECF_R8G8B8, image_size = dimension2du(2, 2), texture_name = 'texture_01', alpha_value = 128, red = (0, 255), green = (0, 255), blue = (0, 255)):
		image = self.driver.createImage(image_format, image_size)
		alpha = 0
		blend = False
		if image.getColorFormat() in (ECF_A1R5G5B5, ECF_A8R8G8B8, ECF_A16B16G16R16F, ECF_A32B32G32R32F):
			alpha = alpha_value
			blend = True
		for row in range(image_size.Height):
			for column in range(image_size.Width):
				image.setPixel(row, column, SColor(alpha, randint(*red), randint(*green), randint(*blue)), blend)
		texture = self.driver.addTexture(texture_name, image)
		image.drop()
		return texture

	def texture_generator_01(self, image_format = ECF_R8G8B8, image_size = dimension2du(2, 2), texture_name = 'texture_01', alpha_value = 128, red = (0, 255), green = (0, 255), blue = (0, 255)):
		return generate_texture(self.driver, image_format, image_size, texture_name, alpha_value, red, green, blue)

	def create_wall_plane_selector(self, tileSize, tileCount, material, textureRepeatCount, pos = None, rotation = None):
		i_mesh = self.i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)
		i_mesh_scene_node = self.scene_manager.addMeshSceneNode(i_mesh)
		if pos:
			i_mesh_scene_node.setPosition(pos)
		if rotation:
			i_mesh_scene_node.setRotation(rotation)
		selector = self.scene_manager.createTriangleSelector(i_mesh, i_mesh_scene_node)
		#~ selector = self.scene_manager.createTriangleSelector(i_mesh_scene_node.getMesh(), i_mesh_scene_node)
		i_mesh_scene_node.setTriangleSelector(selector)
		#~ i_mesh.drop()
		return selector

	def create_tree(self):
		x, z = randint(self.tile_count * self.tile_len / 2 * -1, self.tile_count * self.tile_len / 2), randint(self.tile_count * self.tile_len / 2 * -1, self.tile_count * self.tile_len / 2)
		#
		#~ cylinder_mesh = self.i_geometry_creator.createCylinderMesh(radius = 20, length = 20, tesselation = 4, color = SColor(255,255,0,0), closeTop = True, oblique = 0.0)
		#~ cylinder_scene_node = self.scene_manager.addMeshSceneNode(cylinder_mesh)
		#~ cylinder_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		#~ cylinder_scene_node.setMaterialTexture(0, self.texture_generator_01(ECF_A8R8G8B8, dimension2du(8, 8), 'tree', 255))
		#~ cylinder_scene_node.setPosition(vector3df(x, 0, z))
		#~ cylinder_scene_node.drop()
		#~ cone_mesh = self.i_geometry_creator.createConeMesh(radius = 50, length = 180, tesselation = 8, colorTop = SColor(255,0,255,0), colorBottom = SColor(255,0,255,0), oblique = 0.0)
		#~ cone_scene_node = self.scene_manager.addMeshSceneNode(cone_mesh)
		#~ cone_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		#~ cone_scene_node.setMaterialTexture(0, self.texture_generator_01(ECF_A8R8G8B8, dimension2du(8, 8), 'tree', 255))
		#~ cone_scene_node.setPosition(vector3df(x, 20, z))
		#~ cone_scene_node.drop()
		#
		arrow_mesh = self.i_geometry_creator.createArrowMesh(tesselationCylinder = 4, tesselationCone = 8, height = 200.0, cylinderHeight = 20.0, widthCylinder = 20.0, widthCone = 70.0, colorCylinder = SColor(255,255,0,0), colorCone = SColor(255,0,255,0))
		arrow_scene_node = self.scene_manager.addMeshSceneNode(arrow_mesh)
		arrow_scene_node.setPosition(vector3df(x, 0, z))
		arrow_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		arrow_scene_node.setMaterialTexture(0, self.texture_generator_01(ECF_A8R8G8B8, dimension2du(8, 8), 'tree', 255))
		arrow_scene_node.drop()
		#
		#~ arrow_mesh = self.scene_manager.addArrowMesh('tree', vtxColorCylinder = SColor(255, 255, 0, 0), vtxColorCone = SColor(255, 0, 255, 0), tesselationCylinder = 4, tesselationCone = 8, height = 200.0, cylinderHeight = 20.0, widthCylinder = 20.0, widthCone = 70.0)
		#~ arrow_scene_node = self.scene_manager.addMeshSceneNode(arrow_mesh)
		#~ arrow_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		#~ arrow_scene_node.setMaterialTexture(0, self.texture_generator_01(ECF_A8R8G8B8, dimension2du(8, 8), 'tree', 255))
		#~ arrow_scene_node.setPosition(vector3df(x, 0, z))

	def setActiveCamera(self, camera):
		if self.device and camera:
			active = self.device.getSceneManager().getActiveCamera()
			if active:
				active.setInputReceiverEnabled(False)
			camera.setInputReceiverEnabled(True)
			self.device.getSceneManager().setActiveCamera(camera)

	def setActiveCameraOff(self):
		#~ self.answer_exists = False
		self.cursor_control.setVisible(True)
		cam = self.scene_manager.getActiveCamera()
		if cam:
			cam.setInputReceiverEnabled(not cam.isInputReceiverEnabled())

	def start(self):
		if self.device:
			self.device.setWindowCaption(_(app_name))
			self.device.setResizable(True)
			self.driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.guienv = self.device.getGUIEnvironment()

			if is_frozen():
				self.driver.SetIcon(101)
			else:
				self.driver.SetIcon()

			self.driver.setFog(self.fog_color, self.fog_type, self.fog_start, self.fog_end, self.fog_density, self.fog_pixel, self.fog_range)

			self.font_size = 24
			fonts_path = '/usr/local/share/fonts'
			if 'win' in sys.platform:
				fonts_path = '{}/Fonts'.format(os.environ['SYSTEMROOT'])
			self.font_file = '{}/arial.ttf'.format(fonts_path)
			print(self.font_file)
			self.font = CGUITTFont(self.guienv, self.font_file, self.font_size)
			print(self.font)
			self.skin = self.guienv.getSkin()
			if self.font:
				self.skin.setFont(self.font)
				self.font.drop()
			else:
				print('++++ ERROR vect_font not created !!!')
				self.font = self.guienv.getBuiltInFont()
			menu_height = self.skin.getSize(EGDS_MENU_HEIGHT)

			self.menu = self.guienv.addMenu()
			self.menu.addItem(_('File'), -1, True, True)
			self.menu.addItem(_('View'), -1, True, True)
			self.menu.addItem(_('Options'), -1, True, True)
			self.menu.addItem(_('Help'), -1, True, True)

			submenu = self.menu.getSubMenu(0)
			submenu.addItem(_('Load game'), GUI_ID_LOAD)
			submenu.addItem(_('Save game'), GUI_ID_SAVE)
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
			self.menu_device_types[EDT_SOFTWARE] = self.menu_device_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (self.device_type == EDT_SOFTWARE))
			self.menu_device_types[EDT_OPENGL] = self.menu_device_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (self.device_type == EDT_OPENGL))
			self.menu_device_types[EDT_DIRECT3D9] = self.menu_device_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (self.device_type == EDT_DIRECT3D9))
			self.menu_device_types[EDT_BURNINGSVIDEO] = self.menu_device_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (self.device_type == EDT_BURNINGSVIDEO))
			self.menu_sound = self.menu_options.addItem(_('Sound on/off'), GUI_ID_SOUND_ON_OFF, checked = self.play_sound)
			self.menu_sound_volume = self.menu_options.addItem(_('Sound volume'), GUI_ID_MENU_SOUND_VOLUME)
			self.menu_texture_from_file = self.menu_options.addItem(_('Textures from files'), GUI_ID_TEXTURE_FROM_FILE, checked = self.texture_from_file)

			submenu = self.menu.getSubMenu(3)
			submenu.addItem(_('About'), GUI_ID_ABOUT)

			self.i_geometry_creator = self.scene_manager.getGeometryCreator()

			# height volume
			height = 200
			# texture from file or dynamic generator
			texture = None
			seed()
			file_name = '..//irrlicht//media//skydome.jpg'
			if os.path.isfile(file_name) and self.texture_from_file:
				texture = self.driver.getTexture(file_name)
			else:
				texture = self.texture_generator_01(ECF_R8G8B8, dimension2du(64, 64), 'skydome', 0, (150, 200), (150, 200), (0, 0))
			sky_node = self.scene_manager.addSkyDomeSceneNode(texture)

			# top and bottom plane
			tileSize = dimension2df(self.tile_len, self.tile_len)
			tileCount = dimension2du(self.tile_count, self.tile_count)
			textureRepeatCount = dimension2df(self.tile_count, self.tile_count)
			material = SMaterial()
			material.FogEnable = self.fog_enable
			file_name = '..//irrlicht//media//stones.jpg'
			material.EmissiveColor = SColor(0,255,255,255)
			if os.path.isfile(file_name) and self.texture_from_file:
				material.setTexture(0, self.driver.getTexture(file_name))
			else:
				texture = self.texture_generator(ECF_R8G8B8, dimension2du(4, 4), 'bottom', 0, (0, 0), (0, 255), (0, 100))
				material.setTexture(0, texture)
			i_mesh_top = self.i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)

			logo_file_name = '..//irrlicht//media//opengllogo.png'
			if self.device_type == EDT_SOFTWARE:
				logo_file_name = '..//irrlicht//media//irrlichtlogo3.png'
			elif self.device_type == EDT_BURNINGSVIDEO:
				logo_file_name = '..//irrlicht//media//burninglogo.png'
			elif self.device_type in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				logo_file_name = '..//irrlicht//media//directxlogo.png'
			material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
			if os.path.isfile(logo_file_name) and self.texture_from_file:
				material.setTexture(0, self.driver.getTexture(logo_file_name))
			else:
				texture = self.texture_generator_01(ECF_A8R8G8B8, dimension2du(4, 4), 'top', 196)
				material.setTexture(0, texture)
			i_mesh_bottom = self.i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)
			#~ scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_mesh_bottom)
			i_mesh_scene_node_top = self.scene_manager.addOctreeSceneNode(i_mesh_top)
			i_mesh_scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_mesh_bottom)
			#~ i_mesh_scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_mesh_bottom, i_mesh_scene_node_top)
			i_mesh_scene_node_bottom.setPosition(vector3df(0,height,0))
			i_mesh_scene_node_bottom.setRotation(vector3df(180,0,0))
			selector_top = self.scene_manager.createOctreeTriangleSelector(i_mesh_top)
			selector_bottom = self.scene_manager.createOctreeTriangleSelector(i_mesh_bottom)
			#~ selector_top = self.scene_manager.createOctreeTriangleSelector(i_mesh_scene_node_top.getMesh(), i_mesh_scene_node_top)
			#~ selector_bottom = self.scene_manager.createOctreeTriangleSelector(i_mesh_scene_node_bottom.getMesh(), i_mesh_scene_node_bottom)
			i_mesh_scene_node_top.setTriangleSelector(selector_top)
			i_mesh_scene_node_bottom.setTriangleSelector(selector_bottom)

			# left, right, front and back plane
			tileCount = dimension2du(self.tile_count, int(height / self.tile_len))
			textureRepeatCount = dimension2df(self.tile_count, height / self.tile_len)
			file_name = '..//irrlicht//media//wall.jpg'
			if os.path.isfile(file_name) and self.texture_from_file:
				material.MaterialType = EMT_LIGHTMAP
				material.setTexture(0, self.driver.getTexture(file_name))
			else:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'front', 196, (0, 255), (0, 0), (0, 100))
				material.setTexture(0, texture)
			p = self.tile_count * self.tile_len / 2
			selector_front = self.create_wall_plane_selector(
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(0, height / 2, p), 
				vector3df(-90,0,0))
			if not self.texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'back', 196, (0, 0), (0, 50), (0, 255))
				material.setTexture(0, texture)
			selector_back = self.create_wall_plane_selector(
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(0, height / 2, -p), 
				vector3df(90,0,0))
			if not self.texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'left', 196, (0, 0), (0, 0), (100, 255))
				material.setTexture(0, texture)
			selector_left = self.create_wall_plane_selector(
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(-p, height / 2, 0),
				vector3df(90,90,0))
			if not self.texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'right', 196, (0, 0), (100, 255), (0, 0))
				material.setTexture(0, texture)
			selector_right = self.create_wall_plane_selector(
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(p, height / 2, 0),
				vector3df(90,-90,0))

			# ADD MAGIC VOLUME
			self.magic_i_scene_node = self.scene_manager.addSphereSceneNode(40.0, id = 1, position = vector3df(0,60,0))
			#~ material.MaterialType = EMT_SPHERE_MAP
			if self.magic_i_scene_node:
				#~ file_name = 'media//wall.jpg'
				self.magic_i_scene_node.setMaterialFlag(EMF_FOG_ENABLE, self.fog_enable)
				self.magic_i_scene_node.setMaterialFlag(EMF_LIGHTING, False)
				if os.path.isfile(logo_file_name) and self.texture_from_file:
					self.magic_i_scene_node.setMaterialTexture(0, self.driver.getTexture(logo_file_name))
				else:
					material = self.magic_i_scene_node.getMaterial(0)
					material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
					texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(8, 8), 'magic', 196)
					self.magic_i_scene_node.setMaterialTexture(0, texture)
			selector_magic = self.scene_manager.createTriangleSelector(self.magic_i_scene_node.getMesh())#, self.magic_i_scene_node)
			self.magic_i_scene_node.setTriangleSelector(selector_magic)
			self.magic_i_scene_node.setName('magic_scene_node')
			#~ material.MaterialType = EMT_SOLID

			# ADD CAPTION
			#~ self.text_scene_node1 = self.scene_manager.addTextSceneNode(self.font, 'MAGIC RANDOMIZER', SColor(255,255,0,0), self.magic_i_scene_node)
			self.text_scene_node1 = self.scene_manager.addBillboardTextSceneNode(self.guienv.getBuiltInFont(), 'MAGIC RANDOMIZER', self.magic_i_scene_node, dimension2df(400.0, 100.0), vector3df(0,70,0), colorTop = SColor(255,255,0,0), colorBottom = SColor(255,0,0,255))

			# ADD SIX SPHERES
			p = 30
			if self.texture_from_file:
				p = 40
			self.ext_scene_node1 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(-p,0,0))
			self.ext_scene_node2 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(p,0,0))
			self.ext_scene_node3 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(0,0,-p))
			self.ext_scene_node4 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(0,0,p))
			self.ext_scene_node5 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(0,-p,0))
			self.ext_scene_node6 = self.scene_manager.addSphereSceneNode(10.0, parent = self.magic_i_scene_node, position = vector3df(0,p,0))

			# ADD CUBE VOLUME
			self.cube = self.scene_manager.addCubeSceneNode(180.0, self.magic_i_scene_node, position = vector3df(0,40,0))
			if self.cube:
				#~ file_name = 'media//wall.jpg'
				self.cube.setMaterialFlag(EMF_LIGHTING, False)
				if os.path.isfile(logo_file_name) and self.texture_from_file:
					self.cube.setMaterialTexture(0, self.driver.getTexture(logo_file_name))
				else:
					material = self.cube.getMaterial(0)
					material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
					texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'cube', 128, (200, 255), (0, 0), (0, 0))
					material.setTexture(0, texture)
					material.BackfaceCulling = False
					material.FogEnable = self.fog_enable
					material.AmbientColor = SColor(128, 255, 0, 0)
					material.DiffuseColor = SColor(128, 255, 0, 0)
					material.EmissiveColor = SColor(128, 255, 0, 0)
					material.SpecularColor = SColor(128, 255, 0, 0)
					#~ self.cube.setMaterialTexture(0, texture)
			self.cube.setVisible(False)
			#~ selector_cube = self.scene_manager.createTriangleSelector(self.cube.getMesh())
			#~ self.cube.setTriangleSelector(selector_cube)

			keyMap = SKeyMap(10)
			keyMap.set(0, EKA_MOVE_FORWARD, KEY_UP)
			keyMap.set(1, EKA_MOVE_FORWARD, KEY_KEY_W)
			keyMap.set(2, EKA_MOVE_BACKWARD, KEY_DOWN)
			keyMap.set(3, EKA_MOVE_BACKWARD, KEY_KEY_S)
			keyMap.set(4, EKA_STRAFE_LEFT, KEY_LEFT)
			keyMap.set(5, EKA_STRAFE_LEFT, KEY_KEY_A)
			keyMap.set(6, EKA_STRAFE_RIGHT, KEY_RIGHT)
			keyMap.set(7, EKA_STRAFE_RIGHT, KEY_KEY_D)
			keyMap.set(8, EKA_JUMP_UP, KEY_KEY_J)
			keyMap.set(9, EKA_CROUCH, KEY_KEY_C)
			self.camera = (self.scene_manager.addCameraSceneNodeMaya(), self.scene_manager.addCameraSceneNodeFPS(keyMapArray = keyMap, keyMapSize = keyMap.length, jumpSpeed = 5))
			#~ self.camera[0].setPosition(vector3df(0,600,0))
			self.camera[0].setTarget(vector3df(0,600,0))
			self.camera[1].setPosition(vector3df(200,60,200))
			self.camera[1].setFarValue(9000.0)
			self.setActiveCamera(self.camera[1])

			i_meta_triangle_selector = self.scene_manager.createMetaTriangleSelector()
			i_meta_triangle_selector.addTriangleSelector(selector_top)
			i_meta_triangle_selector.addTriangleSelector(selector_bottom)
			i_meta_triangle_selector.addTriangleSelector(selector_front)
			i_meta_triangle_selector.addTriangleSelector(selector_back)
			i_meta_triangle_selector.addTriangleSelector(selector_left)
			i_meta_triangle_selector.addTriangleSelector(selector_right)
			i_meta_triangle_selector.addTriangleSelector(selector_magic)
			#~ i_meta_triangle_selector.addTriangleSelector(selector_cube)

			anim = self.scene_manager.createCollisionResponseAnimator(i_meta_triangle_selector, self.camera[1])
			self.camera[1].addAnimator(anim)
			anim.drop()

			self.cursor_control = self.device.getCursorControl()
			self.cursor_control.setVisible(False)

			scolor = SColor(255,120,102,136)

			self.collision_manager = self.scene_manager.getSceneCollisionManager()

			i_event_receiver = UserIEventReceiver()
			i_event_receiver.game = self
			self.device.setEventReceiver(i_event_receiver)

			dlg = None
			a, b = 0, 0

			self.answer_exists = False
			question_pos1 = recti(10, menu_height, 0, 0)
			question_pos2 = recti(10, menu_height + self.font_size, 0, 0)
			answer_pos = recti(10, menu_height + self.font_size * 2, 0, 0)
			question_color = SColor(255, 0, 255, 0)
			answer_color = SColor(255, 255, 255, 0)
			self.a, self.b = randint(0, 9), randint(0, 9)
			get_start_time = True
			start_time = self.device.getTimer().getRealTime()
			start_3dline = vector3df(-1500,60,0)
			end_3dline = vector3df(1500,60,0)
			color_3dline = SColor(255, 0, 255, 255)

			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.IsKeyDown(KEY_ESCAPE):
						break
					elif i_event_receiver.IsKeyDown(KEY_F2):
						#~ self.scene_manager.setActiveCamera()
						self.setActiveCameraOff()
					elif i_event_receiver.IsKeyDown(KEY_F1) and not self.help_dialog:
						self.setActiveCameraOff()
						self.help_dialog = self.guienv.addMessageBox(_('Help'), _('F2 - cursor on; ESC - exit'))
					if self.driver.beginScene(True, True, scolor):
						self.scene_manager.drawAll()
						self.window_size = self.driver.getScreenSize()
						#self.font.draw('%d' % self.results, recti(self.window_size.Width - self.font_size * 2, self.window_size.Height - self.font_size, 0, 0), answer_color)
						#if not self.answer_exists:
							#self.font.draw('%d x %d =' % (self.a, self.b), question_pos1, question_color)
							#if i_event_receiver.answer:
								#self.font.draw(i_event_receiver.answer, recti(10, self.window_size.Height - self.font_size, 0, 0), answer_color)

						selectedSceneNode = self.collision_manager.getSceneNodeFromCameraBB(self.camera[1])
						if selectedSceneNode:
							if self.answer_exists:
								if get_start_time:
									start_time = self.device.getTimer().getRealTime()
									get_start_time = False
								tick_time = self.device.getTimer().getRealTime()
								if (tick_time - start_time) < self.time_delay * 1000:
									#self.font.draw(i_event_receiver.answer_text, question_pos1, i_event_receiver.answer_color)
									self.cube.setVisible(True)
								else:
									get_start_time = True
									self.answer_exists = False
									self.cube.setVisible(False)
							#else:
								#if selectedSceneNode.getType() == ESNT_SPHERE:
									#~ self.font.draw('%d x %d =' % (self.a, self.b), question_pos1, question_color)
									#self.font.draw(_('Please enter answer and press "Enter"'), question_pos2, question_color)
									#~ if i_event_receiver.answer:
										#~ self.font.draw(i_event_receiver.answer, recti(10, self.window_size.Height - 40, 0, 0), answer_color)

						self.guienv.drawAll()
						self.driver.endScene()

					self.device.sleep(1)
					self.magic_i_scene_node.setRotation(self.magic_i_scene_node.getRotation() + 1)
					#~ if not self.texture_from_file:
						#~ sky_node.setMaterialTexture(0, self.texture_generator_01(ECF_R8G8B8, dimension2du(64, 64), 'skydome', 0, (150, 200), (150, 200), (0, 0)))
				else:
					self.device._yield()
			self.stop()
		else:
			print ('++++ ERROR Irrlicht createDevice')

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
	g = game()
	g.start()

if __name__ == "__main__":
	main()
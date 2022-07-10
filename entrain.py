# Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
# github.com/usermicrodevices
# BSD license

import os, sys
from pyirrlicht import *
from random import seed, randint
from locale import getdefaultlocale

pybass = None
try:
	import pybass
except:
	print ('++++ PYBASS module not accessible!!!')

pyespeak = None
try:
	import pyespeak
except:
	print ('++++ pyespeak module not accessible!!!')

GUI_ID_QUIT = 0x10000
GUI_ID_ABOUT = 0x10001
GUI_ID_LOAD = 0x10002
GUI_ID_SAVE = 0x10003
GUI_ID_RESULTS = 0x10004
GUI_ID_MOVIE = 0x10005
GUI_ID_HELP_CONTENT = 0x10006
GUI_ID_LOG = 0x10007
GUI_ID_DRIVER = 0x10008
GUI_ID_EDT_SOFTWARE = GUI_ID_DRIVER | EDT_SOFTWARE
GUI_ID_EDT_BURNINGSVIDEO = GUI_ID_DRIVER | EDT_BURNINGSVIDEO
GUI_ID_EDT_DIRECT3D9 = GUI_ID_DRIVER | EDT_DIRECT3D9
GUI_ID_EDT_OPENGL = GUI_ID_DRIVER | EDT_OPENGL
GUI_ID_SOUND_ON_OFF = 0x1000E
GUI_ID_MENU_SOUND_VOLUME = 0x1000F
GUI_ID_WINDOW_SOUND_VOLUME = 0x10010
GUI_ID_SOUND_VOLUME = 0x10011
GUI_ID_VOICE_SPEED = 0x10012
GUI_ID_WINDOW_VOICE_SPEED = 0x10013
GUI_ID_VOICE_RATE = 0x10014
GUI_ID_VOICE_PITCH = 0x10015
GUI_ID_VOICE_TEST_BUTTON = 0x10016
GUI_ID_VOICE_REPEAT = 0x10017
GUI_ID_VOICE_ON_OFF = 0x10018

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

def recursion_search_files_into_dirs(root_dir, name_file):
	result = []
	import re
	prog = re.compile(name_file)
	from os import walk
	for root, dirs, files in walk(root_dir):
		root = root.replace('\\', '/')
		if prog.search(root) is not None:
			result.append(('ROOT', root))
		for name in files:
			if prog.search(name) is not None:
				if root:
					result.append(('FILE', root + '/' + name))
				else:
					result.append(('FILE', name))
		for name in dirs:
			if prog.search(name) is not None:
				if root:
					result.append(('DIR', root + '/' + name))
				else:
					result.append(('DIR', name))
	return result

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
	game = None
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	question = ''
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
			current_character = str(self.KeyInput_Char(key_event))
			if '0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(current_character) > -1 and pressed_down:
			#if current_character.isalpha() > -1 and pressed_down:
				self.answer += current_character
			elif self.KeyInput_Key(key_event) == KEY_BACK and not pressed_down:
				try:
					self.answer = self.answer[:-1]
				except:
					self.answer = self.answer[:-2]
			elif self.KeyInput_Key(key_event) == KEY_DELETE and not pressed_down:
				self.answer = ''
			elif self.KeyInput_Key(key_event) == KEY_RETURN and not pressed_down and not self.game.help_dialog:
				if self.question != self.answer:
					self.game.bad_results += 1
				self.game.answer_exists = True
				self.answer = ''
			elif self.KeyInput_Key(key_event) == KEY_F1:
				self.help()
		elif event_type == EET_GUI_EVENT:
			GUIEvent = self.GetGUIEvent(event)
			gui_event_type = self.GUIEvent_EventType(GUIEvent)
			caller = self.GUIEvent_Caller(GUIEvent)
			id = caller.getID()
			if gui_event_type == EGET_SCROLL_BAR_CHANGED:
				scroll_bar = caller.as_IGUIScrollBar()
				if id == GUI_ID_SOUND_VOLUME:
					self.game.set_sound_volume(scroll_bar.getPos())
				elif id == GUI_ID_VOICE_RATE:
					self.game.set_voice_param('rate', scroll_bar.getPos())
				elif id == GUI_ID_VOICE_PITCH:
					self.game.set_voice_param('pitch', scroll_bar.getPos())
			elif gui_event_type == EGET_BUTTON_CLICKED:
				#button = caller.as_IGUIButton()
				if id == GUI_ID_VOICE_TEST_BUTTON:
					self.game.say('voice testing')
			elif gui_event_type == EGET_MENU_ITEM_SELECTED:
				self.game.help_dialog = None
				menu = caller.as_IGUIContextMenu()
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				elif menu_id == GUI_ID_RESULTS:
					self.game.cursor_control.setVisible(True)
				elif menu_id == GUI_ID_MOVIE:
					self.game.cursor_control.setVisible(True)
				elif menu_id == GUI_ID_EDT_SOFTWARE:
					self.game.set_driver_type(EDT_SOFTWARE)
				elif menu_id == GUI_ID_EDT_OPENGL:
					self.game.set_driver_type(EDT_OPENGL)
				elif menu_id == GUI_ID_EDT_DIRECT3D9:
					self.game.set_driver_type(EDT_DIRECT3D9)
				elif menu_id == GUI_ID_EDT_BURNINGSVIDEO:
					self.game.set_driver_type(EDT_BURNINGSVIDEO)
				elif menu_id == GUI_ID_SOUND_ON_OFF:
					self.game.sound_on_off()
				elif menu_id == GUI_ID_MENU_SOUND_VOLUME:
					self.game.create_sound_volume_control()
				elif menu_id == GUI_ID_VOICE_REPEAT:
					self.game.say(self.question)
				elif menu_id == GUI_ID_VOICE_SPEED:
					self.game.create_voice_speed_control()
				elif menu_id == GUI_ID_VOICE_ON_OFF:
					self.game.voise_on_off()
				elif menu_id == GUI_ID_ABOUT:
					self.game.guienv.addMessageBox(_('About'), _('English words trainer'))
				elif menu_id == GUI_ID_HELP_CONTENT:
					self.help()
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode];
	def help(self):
		if not self.game.help_dialog:
			self.game.help_dialog = self.game.guienv.addMessageBox(_('Help'), _('F1 - help; ESC - exit') + '\n' + _('Please enter answer or press "Enter"'))

class game:
	def __init__(self, *args, **kwargs):
		global pybass, pyespeak
		self.config_file_name = kwargs.pop('config_file_name', 'entrain.ini')
		self.config = config(file_name = self.config_file_name)
		self.time_delay = self.config.get_int('time_delay', 5)
		self.play_sound = self.config.get_bool('play_sound', True)
		self.sound_volume = self.config.get_float('sound_volume', 0.5)
		self.music_file = self.config.get('music_file', 'music//Ranger_Song.s3m')
		self.svg_directory = self.config.get('svg_dir', 'svg_data')
		if not os.path.isdir(self.svg_directory):
			self.svg_directory = ''
		self.bass_handle = None
		self.sound_playing = False
		self.menu_options = None
		if pybass:
			if pybass.BASS_Init(-1, 44100, 0, 0, 0):
				pybass.BASS_SetVolume(self.sound_volume)
				if os.path.isfile(self.music_file):
					self.bass_handle = pybass.BASS_MusicLoad(False, self.music_file, 0, 0, pybass.BASS_MUSIC_PRESCAN | pybass.BASS_SAMPLE_LOOP, 0)
					if self.play_sound:
						self.sound_play()
			else:
				pybass = None
		self.voice_rate = self.config.get_int('voice_rate', 150)
		self.voice_pitch = self.config.get_int('voice_pitch', 50)
		if pyespeak:
			if pyespeak.espeak_Initialize(pyespeak.AUDIO_OUTPUT_SYNCH_PLAYBACK, 0, '.', 0) == pyespeak.EE_INTERNAL_ERROR:
				pyespeak = None
			else:
				pyespeak.espeak_SetVoiceByName('default')
				pyespeak.espeak_SetParameter(pyespeak.espeakRATE, self.voice_rate, 0)
				pyespeak.espeak_SetParameter(pyespeak.espeakPITCH, self.voice_pitch, 0)
		fonts_path = '/usr/local/share/fonts'
		default_driver_type = EDT_SOFTWARE
		if 'win' in sys.platform:
			default_driver_type = EDT_DIRECT3D9
			fonts_path = '{}/Fonts'.format(os.environ['SYSTEMROOT'])
		elif 'linux' in sys.platform:
			default_driver_type = EDT_OPENGL
		self.device_parameters = SIrrlichtCreationParameters()
		self.device_parameters.DriverType = self.config.get_int('driver_type', default_driver_type)
		self.device_parameters.WindowSize = dimension2du(self.config.get_int('window_width', 640), self.config.get_int('window_height', 480))
		self.device_parameters.AntiAlias = self.config.get_int('anti_alias', 2)
		self.device_parameters.WithAlphaChannel = self.config.get_bool('with_alpha_channel', True)
		self.device = createDeviceEx(self.device_parameters)
		self.menu_driver_types = {}
		self.help_dialog = None
		self.good_results = 0
		self.bad_results = 0
		#self.button_repeat_voice = None
		self.voice_on = self.config.get_bool('voice_on', True)
		self.font_size = self.config.get_int('font_size', 32)
		font_file_path = '{}/arial.ttf'.format(fonts_path)
		self.font_file = self.config.get('font_file', font_file_path)
		self.gui_font_size = self.config.get_int('gui_font_size', 24)
		self.gui_font_file = self.config.get('gui_font_file', font_file_path)
		self.svg_image = None

	def __del__(self):
		if self.device:
			self.stop()

	def set_sound_volume(self, value):
		self.sound_volume = value / 100.0
		if pybass:
			pybass.BASS_SetVolume(self.sound_volume)
		self.config.set('sound_volume', self.sound_volume)

	def create_sound_volume_control(self):
		e = self.guienv.getRootGUIElement().getElementFromId(GUI_ID_WINDOW_SOUND_VOLUME, True)
		if e:
			e.remove()
		window = self.guienv.addWindow(recti(10,45,400,150), False, _('Sound volume window'), id = GUI_ID_WINDOW_SOUND_VOLUME)
		self.guienv.addStaticText(_('Select sound volume'), recti(10,30,380,60), True, False, window)
		scrollbar = self.guienv.addScrollBar(True, recti(10,80,380,100), window, GUI_ID_SOUND_VOLUME)
		scrollbar.setPos(int(self.sound_volume * 100))

	def set_voice_param(self, type, value):
		if type == 'rate':
			self.voice_rate = int(value)
			if pyespeak:
				pyespeak.espeak_SetParameter(pyespeak.espeakRATE, self.voice_rate, 0)
			self.config.set('voice_rate', self.voice_rate)
		elif type == 'pitch':
			self.voice_pitch = int(value)
			if pyespeak:
				pyespeak.espeak_SetParameter(pyespeak.espeakPITCH, self.voice_pitch, 0)
			self.config.set('voice_pitch', self.voice_pitch)

	def create_voice_speed_control(self):
		e = self.guienv.getRootGUIElement().getElementFromId(GUI_ID_WINDOW_VOICE_SPEED, True)
		if e:
			e.remove()
		window = self.guienv.addWindow(recti(10,45,400,270), False, _('Voice speed window'), id = GUI_ID_WINDOW_VOICE_SPEED)
		self.guienv.addStaticText(_('Select voice rate'), recti(10,30,380,60), False, False, window)
		scrollbar = self.guienv.addScrollBar(True, recti(10,70,380,90), window, GUI_ID_VOICE_RATE)
		scrollbar.setMin(80)
		scrollbar.setMax(450)
		scrollbar.setPos(self.voice_rate)
		self.guienv.addStaticText(_('Select voice pitch'), recti(10,120,380,150), False, False, window)
		scrollbar = self.guienv.addScrollBar(True, recti(10,160,380,180), window, GUI_ID_VOICE_PITCH)
		scrollbar.setPos(self.voice_pitch)
		self.guienv.addButton(recti(10,190,380,210), window, GUI_ID_VOICE_TEST_BUTTON, _('Test'), _('Testing current voice speed settings'))

	def sound_play(self):
		if self.bass_handle:
			self.sound_playing = pybass.BASS_ChannelPlay(self.bass_handle, False)

	def voise_on_off(self):
		self.voice_on = not self.voice_on
		if self.menu_voice:
			self.menu_voice.setItemChecked(self.menu_voice_on, self.voice_on)
		self.config.set('voice_on', self.voice_on)

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

	def set_driver_type(self, new_driver_type = 0):
		self.device_parameters.DriverType = new_driver_type
		for driver_type, menu_index in self.menu_driver_types.items():
			self.menu_driver_type.setItemChecked(menu_index, (self.device_parameters.DriverType == driver_type))
		self.config.set('driver_type', self.device_parameters.DriverType)
		self.show_warning()

	def start(self):
		if self.device:
			self.device.setWindowCaption(_(app_name))
			self.device.setResizable(True)
			self.video_driver = self.device.getVideoDriver()
			#self.scene_manager = self.device.getSceneManager()
			self.guienv = self.device.getGUIEnvironment()

			if is_frozen():
				self.video_driver.SetIcon(1)
			else:
				self.video_driver.SetIcon()

			self.gui_font = CGUITTFont(self.guienv, self.gui_font_file, self.gui_font_size)
			self.skin = self.guienv.getSkin()
			if self.gui_font:
				self.skin.setFont(self.gui_font)
				self.gui_font.drop()
			else:
				print ('++++ ERROR vect_font not created !!!')
			self.menu_height = self.skin.getSize(EGDS_MENU_HEIGHT)

			self.font = CGUITTFont(self.guienv, self.font_file, self.font_size)

			self.menu = self.guienv.addMenu()
			self.menu.addItem(_('File'), -1, True, True)
			self.menu.addItem(_('View'), -1, True, True)
			self.menu.addItem(_('Voice'), -1, True, True)
			self.menu.addItem(_('Options'), -1, True, True)
			self.menu.addItem(_('Help'), -1, True, True)

			submenu = self.menu.getSubMenu(0)
			submenu.addItem(_('Load game'), GUI_ID_LOAD)
			submenu.addItem(_('Save game'), GUI_ID_SAVE)
			submenu.addSeparator()
			submenu.addItem(_('Quit'), GUI_ID_QUIT)

			submenu = self.menu.getSubMenu(1)
			submenu.addItem(_('Results'), GUI_ID_RESULTS)
			submenu.addItem(_('Movie'), GUI_ID_MOVIE)

			self.menu_voice = self.menu.getSubMenu(2)
			self.menu_voice_on = self.menu_voice.addItem(_('On/Off'), GUI_ID_VOICE_ON_OFF, checked = self.voice_on)
			self.menu_voice.addItem(_('Repeat'), GUI_ID_VOICE_REPEAT)
			self.menu_voice.addItem(_('Speed'), GUI_ID_VOICE_SPEED)

			self.menu_options = self.menu.getSubMenu(3)
			self.menu_options.addItem(_('Start/stop log'), GUI_ID_LOG)
			self.menu_options.addItem(_('Choose graphics driver'), GUI_ID_DRIVER, True, True)
			self.menu_driver_type = self.menu_options.getSubMenu(1)
			self.menu_driver_types[EDT_SOFTWARE] = self.menu_driver_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (self.device_parameters.DriverType == EDT_SOFTWARE))
			self.menu_driver_types[EDT_OPENGL] = self.menu_driver_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (self.device_parameters.DriverType == EDT_OPENGL))
			self.menu_driver_types[EDT_DIRECT3D9] = self.menu_driver_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (self.device_parameters.DriverType == EDT_DIRECT3D9))
			self.menu_driver_types[EDT_BURNINGSVIDEO] = self.menu_driver_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (self.device_parameters.DriverType == EDT_BURNINGSVIDEO))
			self.menu_sound = self.menu_options.addItem(_('Music on/off'), GUI_ID_SOUND_ON_OFF, checked = self.play_sound)
			self.menu_sound_volume = self.menu_options.addItem(_('Sound volume'), GUI_ID_MENU_SOUND_VOLUME)

			submenu = self.menu.getSubMenu(4)
			submenu.addItem(_('Help content'), GUI_ID_HELP_CONTENT)
			submenu.addItem(_('About'), GUI_ID_ABOUT)

			#self.button_repeat_voice = self.guienv.addButton(recti(10,50,100,70), 0, GUI_ID_VOICE_REPEAT_BUTTON, _('Repeat'), _('Repeat current voice text'))

			self.cursor_control = self.device.getCursorControl()
			#self.cursor_control.setVisible(False)

			scolor = SColor(255, 100, 100, 140)
			color_white = SColor(0, 255, 255, 255)

			i_event_receiver = UserIEventReceiver()
			i_event_receiver.game = self
			self.device.setEventReceiver(i_event_receiver)

			dlg = None
			a, b = 0, 0

			self.answer_exists = False
			answer_height_pos = self.menu_height + 5
			answer_color1 = SColor(255, 0, 0, 255)
			answer_color2 = SColor(255, 255, 255, 0)
			question_pos1 = recti(10, answer_height_pos + self.font_size, 0, 0)
			question_pos2 = recti(10, answer_height_pos + self.font_size * 2, 0, 0)
			question_color1 = SColor(255, 255, 0, 0)
			question_color2 = SColor(255, 0, 255, 0)
			scolor_2drectangle = SColor(50,250,0,0)

			self.svg_file_name_container = []
			for obj in recursion_search_files_into_dirs(self.svg_directory, '\.svg$'):
				if obj[0] == 'FILE':
					self.svg_file_name_container.append(obj[1])
			#for svg_file_name in self.svg_file_name_container:
				#print('===', svg_file_name)
			tex, tex_size, i_event_receiver.question = self.create_texture_from_svg_file_name_container()
			flag_say = True
			flag_drawed = True
			animation_flag = False
			animation_scale = 0.9
			animation_time = 3000
			animation_time_step = 50
			animation_scale_step = 0.01

			screen_size = vector2du(self.video_driver.getScreenSize())
			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.IsKeyDown(KEY_ESCAPE):
						break
					if self.video_driver.beginScene(True, True, scolor):
						if screen_size != self.video_driver.getScreenSize():
							screen_size = vector2du(self.video_driver.getScreenSize())
							svg_file_name = tex.getName()
							self.video_driver.removeTexture(tex)
							tex = self.create_texture_from_svg_image(svg_file_name)
							tex_size = tex.getOriginalSize()
						#self.button_repeat_voice.setRelativePosition(position2di(screen_size.X - 100, self.menu_height))
						#self.scene_manager.drawAll()
						if animation_flag and self.device.getTimer().getTime()/animation_time_step%2:
							svg_file_name = tex.getName()
							self.video_driver.removeTexture(tex)
							tex = self.create_texture_from_svg_image(svg_file_name, animation_scale)
							tex_size = tex.getOriginalSize()
							animation_scale -= animation_scale_step
						if tex:
							self.video_driver.draw2DImage2(tex, position2di(int((screen_size.X - tex_size.X) / 2), int((screen_size.Y - tex_size.Y + self.menu_height) / 2)), recti(0, 0, int(tex_size.X), int(tex_size.Y)), useAlphaChannelOfTexture = True)
							flag_drawed = True
						if self.answer_exists and not animation_flag:
							self.answer_exists = False
							self.video_driver.removeTexture(tex)
							tex, tex_size, i_event_receiver.question = self.create_texture_from_svg_file_name_container()
							flag_say = True
							flag_drawed = False
						else:
							if i_event_receiver.question:
								i = 0
								for character_question in i_event_receiver.question:
									character_answer = ''
									if len(i_event_receiver.answer) > i:
										character_answer = i_event_receiver.answer[i]
									if character_question == character_answer:
										self.font.draw(character_answer, recti(10 + i * self.font_size, answer_height_pos, 0, 0), answer_color1)
									else:
										if character_question == ' ':
											self.font.draw('X', recti(10 + i * self.font_size, answer_height_pos, 0, 0), answer_color2)
										else:
											self.font.draw('X', recti(10 + i * self.font_size, answer_height_pos, 0, 0), question_color1)
									i = i + 1
								if i_event_receiver.question == i_event_receiver.answer and not animation_flag:
									self.good_results += 1
									self.device.getTimer().setTime(0)
									animation_flag = True
							#self.font.draw(_('Please enter answer or press "Enter"'), question_pos2, question_color2)
							self.font.draw(i_event_receiver.answer, recti(10, screen_size.Y - self.font_size, 0, 0), answer_color2)
							self.video_driver.draw2DRectangle(scolor_2drectangle, recti(screen_size.X / 2, screen_size.Y - self.font_size, screen_size.X / 2 + self.font_size * 3, screen_size.Y))
							self.font.draw(str(self.good_results), recti(screen_size.X / 2, screen_size.Y - self.font_size, 0, 0), answer_color2)
							self.video_driver.draw2DRectangle(scolor_2drectangle, recti(screen_size.X - self.font_size * 2, screen_size.Y - self.font_size, screen_size.X, screen_size.Y))
							self.font.draw(str(self.bad_results), recti(screen_size.X - self.font_size * 2, screen_size.Y - self.font_size, 0, 0), question_color1)

						self.guienv.drawAll()
						self.video_driver.endScene()

						if flag_say and flag_drawed and self.voice_on:
							self.say(i_event_receiver.question)
							flag_say = False

					self.device.sleep(self.time_delay)
				else:
					self.device._yield()
				if i_event_receiver.answer == i_event_receiver.question:
					self.answer_exists = True
				if animation_flag and self.device.getTimer().getTime() > animation_time:
					animation_flag = False
					animation_scale = 0.9
					self.device.getTimer().setTime(0)
					i_event_receiver.answer = ''
			i_event_receiver.game = None
			self.stop()
		else:
			print ('++++ ERROR Irrlicht createDevice')

	def create_texture_from_svg_file_name_container(self):
		svg_file_count = len(self.svg_file_name_container)
		if svg_file_count:
			svg_file_name = self.svg_file_name_container[randint(0, svg_file_count - 1)]
			if os.path.isfile(svg_file_name):
				words = os.path.basename(svg_file_name).split('.svg')[0].split('.')[0].replace('_', ' ')
				try:
					if self.svg_image:
						self.svg_image.parse(self.device.getFileSystem(), svg_file_name)
					else:
						self.svg_image = svg_agg_image(self.video_driver, self.device.getFileSystem(), svg_file_name)
				except:
					print('=== NOT VALID TEXTURE %s' % svg_file_name)
					return generate_texture(self.video_driver, ECF_A8R8G8B8), dimension2du(2, 2), words
				else:
					texture = self.create_texture_from_svg_image(svg_file_name)
					texture_size = texture.getOriginalSize()
					return texture, texture_size, words
			else:
				print('=== NOT EXISTS FILE %s' % svg_file_name)
				return None, dimension2du(100, 100), ''
		else:
			print('=== NOT EXISTS TEXTURES')
			return None, dimension2du(100, 100), ''

	def create_texture_from_svg_image(self, svg_file_name = '', scale = 1.0):
		if self.svg_image:
			screen_size = self.video_driver.getScreenSize()
			svg_size = self.svg_image.get_size()
			dx = float(screen_size.X) / float(svg_size.X)
			dy = float((screen_size.Y - self.menu_height)) / float(svg_size.Y)
			if dx > 0.1 or dy > 0.1:
				if dx <= dy:
					self.svg_image.scale_rateably(dx * scale)
				else:
					self.svg_image.scale_rateably(dy * scale)
			return self.video_driver.addTexture(svg_file_name, self.svg_image.get_image(True))

	def say(self, word = ''):
		if pyespeak and word:
			text = ctypes.create_string_buffer(word, len(word))
			pyespeak.espeak_Synth(text, ctypes.sizeof(text)+1, 0, pyespeak.POS_CHARACTER, 0, pyespeak.espeakCHARS_AUTO | pyespeak.espeakPHONEMES | pyespeak.espeakENDPAUSE, None, None)

	def stop(self):
		if pybass:
			pybass.BASS_Free()
		if pyespeak:
			pyespeak.espeak_Terminate()
		if self.device:
			s = self.video_driver.getScreenSize()
			self.device.closeDevice()
			self.device = None
			if s.Width < 320:
				s.Width = 320
			if s.Height < 240:
				s.Height = 240
			self.config.set_many((('window_width', int(s.Width)), ('window_height', int(s.Height))))
		self.config.close()


def main():
	g = game()
	g.start()

if __name__ == "__main__":
	main()
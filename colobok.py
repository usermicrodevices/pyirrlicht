import os, sys
from random import randint
from pyirrlicht import *
from locale import getdefaultlocale

try:
	import pybass
except:
	pybass = None
	print ('++++ PYBASS module not accessible!!!')

#driverType = EDT_NULL
#driverType = EDT_SOFTWARE
#driverType = EDT_BURNINGSVIDEO
#driverType = EDT_DIRECT3D8
#driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

GUI_ID_QUIT = 0x10000
GUI_ID_ABOUT = 0x10001
GUI_ID_LOAD = 0x10002
GUI_ID_SAVE = 0x10003
GUI_ID_LOG = 0x10004
GUI_ID_SOUND_ON_OFF = 0x10005
GUI_ID_DRIVER = 0x10006
GUI_ID_EDT_SOFTWARE = GUI_ID_DRIVER | EDT_SOFTWARE
GUI_ID_EDT_BURNINGSVIDEO = GUI_ID_DRIVER | EDT_BURNINGSVIDEO
GUI_ID_EDT_DIRECT3D9 = GUI_ID_DRIVER | EDT_DIRECT3D9
GUI_ID_EDT_OPENGL = GUI_ID_DRIVER | EDT_OPENGL

menu_device_types = {}

app_name = os.path.basename(sys.argv[0].split('.')[0])
media_catalog = 'media'
if os.path.isdir('colobok_bin'):
	media_catalog = 'colobok_bin/colobok/media'

# simple language translator
id_codec = 'cp1251'
default_locale = getdefaultlocale()[0]
translation_catalog = 'lang'
if os.path.isdir('colobok_bin'):
	translation_catalog = 'colobok_bin/colobok/lang'
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
		return unicode(translations[source], id_codec)
	except:
		return translations[source]

gui_evt_types = {
EGET_ELEMENT_FOCUS_LOST:'EGET_ELEMENT_FOCUS_LOST',
EGET_ELEMENT_FOCUSED:'EGET_ELEMENT_FOCUSED',
EGET_ELEMENT_HOVERED:'EGET_ELEMENT_HOVERED',
EGET_ELEMENT_LEFT:'EGET_ELEMENT_LEFT',
EGET_ELEMENT_CLOSED:'EGET_ELEMENT_CLOSED',
EGET_BUTTON_CLICKED:'EGET_BUTTON_CLICKED',
EGET_SCROLL_BAR_CHANGED:'EGET_SCROLL_BAR_CHANGED',
EGET_CHECKBOX_CHANGED:'EGET_CHECKBOX_CHANGED',
EGET_LISTBOX_CHANGED:'EGET_LISTBOX_CHANGED',
EGET_LISTBOX_SELECTED_AGAIN:'EGET_LISTBOX_SELECTED_AGAIN',
EGET_FILE_SELECTED:'EGET_FILE_SELECTED',
EGET_DIRECTORY_SELECTED:'EGET_DIRECTORY_SELECTED',
EGET_FILE_CHOOSE_DIALOG_CANCELLED:'EGET_FILE_CHOOSE_DIALOG_CANCELLED',
EGET_MESSAGEBOX_YES:'EGET_MESSAGEBOX_YES',
EGET_MESSAGEBOX_NO:'EGET_MESSAGEBOX_NO',
EGET_MESSAGEBOX_OK:'EGET_MESSAGEBOX_OK',
EGET_MESSAGEBOX_CANCEL:'EGET_MESSAGEBOX_CANCEL',
EGET_EDITBOX_ENTER:'EGET_EDITBOX_ENTER',
EGET_EDITBOX_CHANGED:'EGET_EDITBOX_CHANGED',
EGET_EDITBOX_MARKING_CHANGED:'EGET_EDITBOX_MARKING_CHANGED',
EGET_TAB_CHANGED:'EGET_TAB_CHANGED',
EGET_MENU_ITEM_SELECTED:'EGET_MENU_ITEM_SELECTED',
EGET_COMBO_BOX_CHANGED:'EGET_COMBO_BOX_CHANGED',
EGET_SPINBOX_CHANGED:'EGET_SPINBOX_CHANGED',
EGET_TABLE_CHANGED:'EGET_TABLE_CHANGED',
EGET_TABLE_HEADER_CHANGED:'EGET_TABLE_HEADER_CHANGED',
EGET_TABLE_SELECTED_AGAIN:'EGET_TABLE_SELECTED_AGAIN',
EGET_TREEVIEW_NODE_DESELECT:'EGET_TREEVIEW_NODE_DESELECT',
EGET_TREEVIEW_NODE_SELECT:'EGET_TREEVIEW_NODE_SELECT',
EGET_TREEVIEW_NODE_EXPAND:'EGET_TREEVIEW_NODE_EXPAND',
EGET_TREEVIEW_NODE_COLLAPS:'EGET_TREEVIEW_NODE_COLLAPS',
EGET_COUNT:'EGET_COUNT'
}

bass_handle = None
play_sound = True
sound_playing = False
sound_volume = 1.0
sound_file = '%s/sound.mp3' % media_catalog

def sound_play():
	global sound_playing, bass_handle
	if bass_handle:
		sound_playing = pybass.BASS_ChannelPlay(bass_handle, False)

def sound_on_off():
	global play_sound, sound_playing, bass_handle
	if play_sound:
		play_sound = False
		if bass_handle and sound_playing:
			sound_playing = False
			pybass.BASS_ChannelStop(bass_handle)
	else:
		play_sound = True
		sound_play()
	if menu_options:
		menu_options.setItemChecked(menu_sound, play_sound)
	#~ config.set('play_sound', play_sound)

class UserIEventReceiver(IEventReceiver):
	about_dialog = None
	video_driver = None
	gui = None
	screen_size = dimension2du()
	show_cursor = False
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	mouse_state = {'x':-1, 'y':-1, 'type':-1, 'left':False, 'right':False, 'm':False}
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
	def OnEvent(self, evt):
		event = SEvent(evt)
		if event.EventType is EET_MOUSE_INPUT_EVENT:
			self.mouse_state['x'] = event.MouseInput.X
			self.mouse_state['y'] = event.MouseInput.Y
			self.mouse_state['type'] = event.MouseInput.EventType
			self.mouse_state['left'] = bool(event.MouseInput.isLeftPressed())
			self.mouse_state['right'] = bool(event.MouseInput.isRightPressed())
			self.mouse_state['middle'] = bool(event.MouseInput.isMiddlePressed())
		elif event.EventType is EET_KEY_INPUT_EVENT:
			key = event.KeyInput.Key
			pressed_down = event.KeyInput.PressedDown
			self.KeyIsDown[key] = pressed_down
			if key in (KEY_KEY_0, KEY_KEY_1, KEY_KEY_2, KEY_KEY_3, KEY_KEY_4, KEY_KEY_5, KEY_KEY_6, KEY_KEY_7, KEY_KEY_8, KEY_KEY_9, KEY_NUMPAD0, KEY_NUMPAD1, KEY_NUMPAD2, KEY_NUMPAD3, KEY_NUMPAD4, KEY_NUMPAD5, KEY_NUMPAD6, KEY_NUMPAD7, KEY_NUMPAD8, KEY_NUMPAD9) and not pressed_down:
				self.answer += self.NumbersKeys[key]
			elif key in (KEY_BACK, KEY_DELETE) and not pressed_down:
				self.answer = ''
		elif event.EventType is EET_GUI_EVENT:
			gui_event_type = event.GUIEvent.EventType
			#~ print(gui_evt_types[gui_event_type])
			if gui_event_type in (EGET_MESSAGEBOX_YES, EGET_MESSAGEBOX_NO, EGET_MESSAGEBOX_OK, EGET_MESSAGEBOX_CANCEL):
				self.about_dialog = None
			elif gui_event_type == EGET_ELEMENT_LEFT:
				self.show_cursor = False
			elif gui_event_type == EGET_ELEMENT_HOVERED:
				self.show_cursor = True
			elif gui_event_type == EGET_MENU_ITEM_SELECTED:
				self.about_dialog = None
				menu = event.GUIEvent.Caller.as_IGUIContextMenu()
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				#~ elif menu_id == GUI_ID_EDT_SOFTWARE:
					#~ self.game.set_device_type(EDT_SOFTWARE)
				#~ elif menu_id == GUI_ID_EDT_OPENGL:
					#~ self.game.set_device_type(EDT_OPENGL)
				#~ elif menu_id == GUI_ID_EDT_DIRECT3D9:
					#~ self.game.set_device_type(EDT_DIRECT3D9)
				#~ elif menu_id == GUI_ID_EDT_BURNINGSVIDEO:
					#~ self.game.set_device_type(EDT_BURNINGSVIDEO)
				elif menu_id == GUI_ID_SOUND_ON_OFF:
					sound_on_off()
				elif menu_id == GUI_ID_ABOUT:
					self.about_dialog = self.gui.addMessageBox(_('About'), _('2D Game COLOBOK'))
		elif event.EventType is EET_KEY_INPUT_EVENT:
			self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
		elif event.EventType is EET_JOYSTICK_INPUT_EVENT:
			pass
		elif event.EventType is EET_LOG_TEXT_EVENT:
			if event.LogEvent.Level == 0 and event.LogEvent.Text.find('Resizing window') > -1:
				self.screen_size = self.video_driver.getScreenSize()
		elif event.EventType is EET_USER_EVENT:
			pass
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode];
	def show_warning(self):
		self.gui.addMessageBox(_('Warning'), _('For finish this operation you need restart game!'))
	def set_device_type(self, new_device_type = 0):
		driverType = new_device_type
		for dev_type, menu_index in menu_device_types.items():
			menu_device_type.setItemChecked(menu_index, (driverType == dev_type))
		config.set('device_type', driverType)
		self.show_warning()

windowSize = dimension2du(640, 480)
device = createDevice(driverType, windowSize, 16, False, False, False, 0)
if device:
	device.setWindowCaption(_('Colobok'))
	device.setResizable(True)
	driver = device.getVideoDriver()
	scene_manager = device.getSceneManager()
	guienv = device.getGUIEnvironment()

	if is_frozen():
		driver.SetIcon(101)
	else:
		driver.SetIcon()

	i_event_receiver = UserIEventReceiver()
	i_event_receiver.video_driver = driver
	i_event_receiver.gui = guienv
	device.setEventReceiver(i_event_receiver)

	img_path = driver.getTexture('%s/path.png'%media_catalog)
	if img_path:
		img_path_size = img_path.getOriginalSize()

	img_stump = driver.getTexture('%s/stump.png'%media_catalog)
	if img_stump:
		img_stump_size = img_stump.getOriginalSize()

	img_01 = driver.getTexture('%s/01.png'%media_catalog)
	if img_01:
		img_01_size = img_01.getOriginalSize()
	img_02 = driver.getTexture('%s/02.png'%media_catalog)
	if img_02:
		img_02_size = img_02.getOriginalSize()
	img_03 = driver.getTexture('%s/03.png'%media_catalog)
	if img_03:
		img_03_size = img_03.getOriginalSize()
	img_04 = driver.getTexture('%s/04.png'%media_catalog)
	if img_04:
		img_04_size = img_04.getOriginalSize()
	img_05 = driver.getTexture('%s/05.png'%media_catalog)
	if img_05:
		img_05_size = img_05.getOriginalSize()
	img_06 = driver.getTexture('%s/06.png'%media_catalog)
	if img_06:
		img_06_size = img_06.getOriginalSize()
	img_07 = driver.getTexture('%s/07.png'%media_catalog)
	if img_07:
		img_07_size = img_07.getOriginalSize()

	img_dad = driver.getTexture('%s/dad.png'%media_catalog)
	if img_dad:
		img_dad_size = img_dad.getOriginalSize()

	img_granny = driver.getTexture('%s/granny.png'%media_catalog)
	if img_granny:
		img_granny_size = img_granny.getOriginalSize()

	img_hare = driver.getTexture('%s/hare.png'%media_catalog)
	if img_hare:
		img_hare_size = img_hare.getOriginalSize()

	img_wolf = driver.getTexture('%s/wolf.png'%media_catalog)
	if img_wolf:
		img_wolf_size = img_wolf.getOriginalSize()

	img_bear = driver.getTexture('%s/bear.png'%media_catalog)
	if img_bear:
		img_bear_size = img_bear.getOriginalSize()

	img_fox = driver.getTexture('%s/fox.png'%media_catalog)
	if img_fox:
		img_fox_size = img_fox.getOriginalSize()

	img_cloud1 = driver.getTexture('%s/cloud1.png'%media_catalog)
	if img_cloud1:
		img_cloud1_size = img_cloud1.getOriginalSize()
	img_cloud2 = driver.getTexture('%s/cloud2.png'%media_catalog)
	if img_cloud2:
		img_cloud2_size = img_cloud2.getOriginalSize()

	cur_img = driver.getTexture('%s/cursor.png'%media_catalog)
	if cur_img:
		cur_img_size = cur_img.getOriginalSize()

	cam = scene_manager.addCameraSceneNode()
	cam.setPosition(vector3df(0,100,0))
	cam.setTarget(vector3df(0,0,0))
	cam.setNearValue(0.01)

	font_file = '2DGame/Quiltpatches-OVoaO.ttf'
	try:
		font_path = os.environ['SYSTEMROOT']+'/Fonts/'
	except Exception as e:
		print(e)
	else:
		font_file = font_path + 'arial.ttf'
	gui_font = CGUITTFont(guienv, font_file, 20)
	if not gui_font:
		gui_font = guienv.getBuiltInFont()

	skin = guienv.getSkin()
	skin.setFont(gui_font)
	gui_font.drop()
	menu_height = skin.getSize(EGDS_MENU_HEIGHT)

	if pybass:
		if pybass.BASS_Init(-1, 44100, 0, 0, 0):
			pybass.BASS_SetVolume(sound_volume)
			if os.path.isfile(sound_file):
				#bass_handle = pybass.BASS_MusicLoad(False, sound_file, 0, 0, pybass.BASS_MUSIC_PRESCAN | pybass.BASS_SAMPLE_LOOP, 0)
				bass_handle = pybass.BASS_StreamCreateFile(False, sound_file, 0, 0, pybass.BASS_MUSIC_PRESCAN | pybass.BASS_SAMPLE_LOOP)
				if play_sound:
					sound_play()

	menu_options = None

	menu = guienv.addMenu()
	menu.addItem(_('File'), -1, True, True)
	menu.addItem(_('Options'), -1, True, True)
	menu.addItem(_('Help'), -1, True, True)

	submenu = menu.getSubMenu(0)
	submenu.addItem(_('Load game'), GUI_ID_LOAD)
	submenu.addItem(_('Save game'), GUI_ID_SAVE)
	submenu.addSeparator()
	submenu.addItem(_('Quit'), GUI_ID_QUIT)

	menu_options = menu.getSubMenu(1)
	menu_options.addItem(_('Start/stop log'), GUI_ID_LOG)
	menu_options.addItem(_('Choose graphics driver'), GUI_ID_DRIVER, True, True)
	menu_device_type = menu_options.getSubMenu(1)
	menu_device_types[EDT_SOFTWARE] = menu_device_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (driverType == EDT_SOFTWARE))
	menu_device_types[EDT_OPENGL] = menu_device_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (driverType == EDT_OPENGL))
	menu_device_types[EDT_DIRECT3D9] = menu_device_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (driverType == EDT_DIRECT3D9))
	menu_device_types[EDT_BURNINGSVIDEO] = menu_device_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (driverType == EDT_BURNINGSVIDEO))
	menu_sound = menu_options.addItem(_('Sound on/off'), GUI_ID_SOUND_ON_OFF, checked = play_sound)

	submenu = menu.getSubMenu(2)
	submenu.addItem(_('About'), GUI_ID_ABOUT)

	img_font = CGUITTFont(guienv, font_file, 36)
	if not img_font:
		img_font = guienv.getBuiltInFont()
	question_font = CGUITTFont(guienv, font_file, 72)
	if not question_font:
		question_font = guienv.getBuiltInFont()

	text1 = _('COLOBOK!')
	text1_size = img_font.getDimension(text1)
	text2 = _('WINNER!')
	text2_size = img_font.getDimension(text2)

	text2pos = recti(50,10,0,0)

	scolor = SColor(0,50,150,255)
	img_color = SColor(255,255,255,255)
	img_dad_color = SColor(255,255,255,255)
	img_granny_color = SColor(255,255,255,255)
	img_cloud_color = SColor(150,255,255,255)
	question_color = SColor(255, 255, 0, 0)
	answer_color = SColor(255, 0, 255, 0)
	hero_color = SColor(255,255,255,255)

	x_delta = 20
	y_delta = 0
	y_offset = 0
	img_path_size_x_orig = int(img_path_size.X)
	img_path_size_x = img_path_size_x_orig - x_delta
	img_path_x1 = -x_delta
	img_path_x2 = img_path_size_x + img_path_x1
	img_path_x3 = img_path_size_x + img_path_x2

	id_img = 0
	id_img_animal = 0
	last_time_answer = 0
	last_time0 = 0
	last_time1 = 0
	last_time2 = 0

	answer_state = False
	def question(from_value = 0, to_value = 9):
		a, b = randint(from_value, to_value), randint(from_value, to_value)
		return a, b, '%d x %d =' % (a, b)
	value1, value2, text_question = question()
	text_question_size = question_font.getDimension(text_question)

	state_dad = 2
	state_granny = 2

	while device.run():
		if device.isWindowActive():
			if i_event_receiver.IsKeyDown(KEY_ESCAPE):
				break
			elif i_event_receiver.IsKeyDown(KEY_RETURN):
				if i_event_receiver.answer:
					if value1 * value2 == int(i_event_receiver.answer):
						question_color = SColor(255, 0, 255, 0)
						hero_color = SColor(255, 255, 255, 255)
						answer_state = True
					else:
						question_color = SColor(255, 255, 0, question_color.b+10)
						hero_color = SColor(hero_color.a-10, 255, hero_color.g-50, hero_color.b-50)
				i_event_receiver.KeyIsDown[KEY_RETURN] = False
			time = device.getTimer().getTime()
			i_event_receiver.screen_size = driver.getScreenSize()
			x, y = device.getCursorControl().getPosition().get_XY()
			if x < 0 or y < menu_height or x > i_event_receiver.screen_size.X or y > i_event_receiver.screen_size.Y or i_event_receiver.about_dialog or i_event_receiver.show_cursor:
				device.getCursorControl().setVisible(True)
			else:
				if not i_event_receiver.show_cursor:
					device.getCursorControl().setVisible(False)

			if time > last_time_answer + 5000:# change answer state
				last_time_answer = time
				if answer_state:
					answer_state = False
					if id_img_animal > 2:
						id_img_animal = 0
					else:
						id_img_animal = id_img_animal + 1
					question_color = SColor(255, 255, 0, 0)
					i_event_receiver.answer = ''
					if id_img_animal == 0:
						state_dad = 2
						state_granny = 2
						img_dad_color = SColor(255, 255, 255, 255)
						img_granny_color = SColor(255, 255, 255, 255)
					value1, value2, text_question = question()

			if time > last_time0 + 2:# movie path
				last_time0 = time
				if -img_path_x1 > img_path_size_x_orig:
					img_path_x1 = img_path_size_x * 2 - x_delta
				else:
					img_path_x1 = img_path_x1 - 1
				if -img_path_x2 > img_path_size_x_orig:
					img_path_x2 = img_path_size_x * 2 - x_delta
				else:
					img_path_x2 = img_path_x2 - 1
				if -img_path_x3 > img_path_size_x_orig:
					img_path_x3 = img_path_size_x * 2 - x_delta
				else:
					img_path_x3 = img_path_x3 - 1

			img_path_y = int(i_event_receiver.screen_size.Y-img_path_size.Y)

			if time > last_time1 + 100:# change height colobok
				last_time1 = time
				if y_offset > 39:
					y_delta = -1
				elif y_offset < 1:
					y_delta = 1
				y_offset = y_offset + y_delta
			if time > last_time2 + 150:# change sprite
				last_time2 = time
				if id_img < 6:
					id_img = id_img + 1
				else:
					id_img = 0

			img_dad_y = img_path_y - 80
			img_granny_y = img_path_y - 270
			if i_event_receiver.mouse_state['left'] and not i_event_receiver.show_cursor:
				action_help = False
				if x < img_dad_size.X and img_dad_y < y < img_dad_y+img_dad_size.Y and state_dad:
					action_help = True
					state_dad = state_dad - 1
					img_dad_color = SColor(img_dad_color.a-100, 255, 255, 255)
				elif x < img_granny_size.X and img_granny_y < y < img_granny_y+img_granny_size.Y and state_granny:
					action_help = True
					state_granny = state_granny - 1
					img_granny_color = SColor(img_granny_color.a-100, 255, 255, 255)
				if action_help:
					i_event_receiver.answer = str(value1 * value2)
					i_event_receiver.KeyIsDown[KEY_RETURN] = True
				i_event_receiver.mouse_state['left'] = False

			if driver.beginScene(True, True, scolor):
				driver.draw2DImage(img_path, position2di(img_path_x1,img_path_y), recti(0,0,int(img_path_size.X),int(img_path_size.Y)), 0, img_color, True)
				driver.draw2DImage(img_path, position2di(img_path_x2,img_path_y), recti(0,0,int(img_path_size.X),int(img_path_size.Y)), 0, img_color, True)
				driver.draw2DImage(img_path, position2di(img_path_x3,img_path_y), recti(0,0,int(img_path_size.X),int(img_path_size.Y)), 0, img_color, True)
				if id_img == 0:
					driver.draw2DImage(img_01, position2di(int((i_event_receiver.screen_size.X-img_01_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_01_size.X),int(img_01_size.Y)), 0, hero_color, True)
				elif id_img == 1:
					driver.draw2DImage(img_02, position2di(int((i_event_receiver.screen_size.X-img_02_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_02_size.X),int(img_02_size.Y)), 0, hero_color, True)
				elif id_img == 2:
					driver.draw2DImage(img_03, position2di(int((i_event_receiver.screen_size.X-img_03_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_03_size.X),int(img_03_size.Y)), 0, hero_color, True)
				elif id_img == 3:
					driver.draw2DImage(img_04, position2di(int((i_event_receiver.screen_size.X-img_04_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_04_size.X),int(img_04_size.Y)), 0, hero_color, True)
				elif id_img == 4:
					driver.draw2DImage(img_05, position2di(int((i_event_receiver.screen_size.X-img_05_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_05_size.X),int(img_05_size.Y)), 0, hero_color, True)
				elif id_img == 5:
					driver.draw2DImage(img_06, position2di(int((i_event_receiver.screen_size.X-img_06_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_06_size.X),int(img_06_size.Y)), 0, hero_color, True)
				else:
					driver.draw2DImage(img_07, position2di(int((i_event_receiver.screen_size.X-img_07_size.X)/3),img_path_y + 35 + y_offset), recti(0,0,int(img_07_size.X),int(img_07_size.Y)), 0, hero_color, True)

				# helpers
				driver.draw2DImage(img_dad, position2di(0, img_dad_y), recti(0,0,int(img_dad_size.X),int(img_dad_size.Y)), 0, img_dad_color, True)
				driver.draw2DImage(img_granny, position2di(0, img_granny_y), recti(0,0,int(img_granny_size.X),int(img_granny_size.Y)), 0, img_granny_color, True)

				# animals
				if id_img_animal == 0:
					driver.draw2DImage(img_hare, position2di(int(i_event_receiver.screen_size.X - img_hare_size.X), img_path_y - 200), recti(0,0,int(img_hare_size.X),int(img_hare_size.Y)), 0, img_color, True)
				elif id_img_animal == 1:
					driver.draw2DImage(img_wolf, position2di(int(i_event_receiver.screen_size.X - img_wolf_size.X), img_path_y - 200), recti(0,0,int(img_wolf_size.X),int(img_wolf_size.Y)), 0, img_color, True)
				elif id_img_animal == 2:
					driver.draw2DImage(img_bear, position2di(int(i_event_receiver.screen_size.X - img_bear_size.X), img_path_y - 200), recti(0,0,int(img_bear_size.X),int(img_bear_size.Y)), 0, img_color, True)
				else:
					driver.draw2DImage(img_fox, position2di(int(i_event_receiver.screen_size.X - img_fox_size.X), img_path_y - 200), recti(0,0,int(img_fox_size.X),int(img_fox_size.Y)), 0, img_color, True)

				# stumps
				driver.draw2DImage(img_stump, position2di(img_path_x1+450,img_path_y+90), recti(0,0,int(img_stump_size.X),int(img_stump_size.Y)), 0, img_color, True)
				driver.draw2DImage(img_stump, position2di(img_path_x2+450,img_path_y+90), recti(0,0,int(img_stump_size.X),int(img_stump_size.Y)), 0, img_color, True)
				driver.draw2DImage(img_stump, position2di(img_path_x3+450,img_path_y+90), recti(0,0,int(img_stump_size.X),int(img_stump_size.Y)), 0, img_color, True)

				# clouds
				driver.draw2DImage(img_cloud1, position2di(img_path_x1+250, 10), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x1+450, 30), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud1, position2di(img_path_x1+650, 20), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x1+850, 40), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)

				driver.draw2DImage(img_cloud1, position2di(img_path_x2+250, 30), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x2+450, 10), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud1, position2di(img_path_x2+650, 20), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x2+850, 40), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)

				driver.draw2DImage(img_cloud1, position2di(img_path_x3+250, 20), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x3+450, 30), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud1, position2di(img_path_x3+650, 10), recti(0,0,int(img_cloud1_size.X),int(img_cloud1_size.Y)), 0, img_cloud_color, True)
				driver.draw2DImage(img_cloud2, position2di(img_path_x3+850, 40), recti(0,0,int(img_cloud2_size.X),int(img_cloud2_size.Y)), 0, img_cloud_color, True)

				#img_font.draw(text1, recti(int((i_event_receiver.screen_size.X-text1_size.X)/2),int(text1_size.Y),0,0), SColor(150, 0, 255, 0))
				#question_font.draw(text_question, recti(int((i_event_receiver.screen_size.X-text_question_size.X)/2-20),100,0,0), question_color)
				#if i_event_receiver.answer:
				#	question_font.draw(i_event_receiver.answer, recti(int((i_event_receiver.screen_size.X-text_question_size.X)/2+text_question_size.X), 100, 0, 0), answer_color)
				#if answer_state:
				#	img_font.draw(text2, recti(int((i_event_receiver.screen_size.X-text2_size.X)/2),200,0,0), SColor(150, 0, 255, 0))

				# draw cursor
				driver.draw2DImage(cur_img, position2di(int(x-cur_img_size.X/2),int(y-cur_img_size.Y/2)), recti(0,0,int(cur_img_size.X),int(cur_img_size.Y)), 0, img_color, True)
				scene_manager.drawAll()
				guienv.drawAll()
				driver.endScene()
			device.sleep(10)
		else:
			device.yield_self()
	device.drop()
	device.closeDevice()
else:
	print('ERROR createDevice')

'small and simple 2d game example'

driver_type = 5
full_screen = False
stencil_buffer = False
vsync = False

run_app = True

from video_choice_dialog import has_pywingui
if has_pywingui:
	from video_choice_dialog import ChoiceDialog, IDOK, IDCANCEL
	dialog = ChoiceDialog()
	dialog.driver_type = driver_type
	dialog.full_screen = full_screen
	dialog.stencil_buffer = stencil_buffer
	dialog.vsync = vsync
	dialogResult = dialog.DoModal()
	if dialogResult == IDOK:
		driver_type = dialog.driver_type
		full_screen = dialog.full_screen
		stencil_buffer = dialog.stencil_buffer
		vsync = dialog.vsync
	elif dialogResult == IDCANCEL:
		run_app = False


if run_app:
	import os, sys
	os.environ['IRRLICHT_C_LIBRARY'] = 'irrlicht_c'

	from random import randint
	from locale import getdefaultlocale

	try:
		import pybass
	except:
		pybass = None
		print ('++++ PYBASS module not accessible!!!')

	from pyirrlicht import *
	#~ driverType = EDT_NULL
	#~ driverType = EDT_SOFTWARE
	#~ driverType = EDT_BURNINGSVIDEO
	#~ driverType = EDT_DIRECT3D8
	#~ driverType = EDT_DIRECT3D9
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

	# simple language translator
	id_codec = 'cp1251'
	default_locale = getdefaultlocale()[0]
	translation_catalog = '2DGame'
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
	sound_file = '2DGame/jinbels.mod'

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
			print('play_sound',play_sound)
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
		#~ log_file = open('log_2dgame.txt', 'w')
		#~ def __del__(self):
			#~ self.log_file.close()
		def OnEvent(self, evt):
			event = SEvent(evt)
			if event.EventType is EET_MOUSE_INPUT_EVENT:
				self.mouse_state['x'] = event.MouseInput.X
				self.mouse_state['y'] = event.MouseInput.Y
				self.mouse_state['type'] = event.MouseInput.EventType
				self.mouse_state['left'] = bool(event.MouseInput.isLeftPressed())
				self.mouse_state['right'] = bool(event.MouseInput.isRightPressed())
				self.mouse_state['middle'] = bool(event.MouseInput.isMiddlePressed())
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
						self.about_dialog = self.gui.addMessageBox(_('About'), _('2D Game'))
			elif event.EventType is EET_KEY_INPUT_EVENT:
				self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
			elif event.EventType is EET_JOYSTICK_INPUT_EVENT:
				pass
			elif event.EventType is EET_LOG_TEXT_EVENT:
				#~ self.log_file.write('event.LogEvent.Text\n')
				#~ self.log_file.flush()
				#~ self.log_file.write(event.LogEvent.Text)# + '\n')
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

	window_size = dimension2du(320, 240)
	device = createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync, 0)
	if device:
		device.setWindowCaption('Irrlicht Engine - 2D Game')
		device.setResizable(True)
		driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		guienv = device.getGUIEnvironment()

		i_event_receiver = UserIEventReceiver()
		i_event_receiver.video_driver = driver
		i_event_receiver.gui = guienv
		device.setEventReceiver(i_event_receiver)

		bells = driver.getTexture('2DGame/bells.png')
		if bells:
			bells_size = bells.getOriginalSize()
		santa = driver.getTexture('2DGame/santa.png')
		if santa:
			santa_size = santa.getOriginalSize()
		santa_pipe = driver.getTexture('2DGame/santa_pipe.png')
		if santa_pipe:
			santa_pipe_size = santa_pipe.getOriginalSize()
		present_red = driver.getTexture('2DGame/present-red.png')
		if present_red:
			present_red_size = present_red.getOriginalSize()
		cur_img = driver.getTexture('2DGame/laurel.png')
		if cur_img:
			cur_img_size = cur_img.getOriginalSize()

		#~ snowflake = driver.getTexture('2DGame/snowflake.png')
		#~ if snowflake:
			#~ snowflake_size = snowflake.getOriginalSize()
		#~ snowflake_scene_node = scene_manager.addBillboardSceneNode()
		#~ snowflake_scene_node.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
		#~ snowflake_scene_node.setMaterialTexture(0, driver.getTexture('2DGame/snowflake.png'))
		#~ snowflake_scene_node.setMaterialFlag(EMF_LIGHTING, False)
		#~ snowflake_scene_node.setMaterialFlag(EMF_ZBUFFER, False)
		#~ snowflake_scene_node.setSize(dimension2df(20.0, 20.0))
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
		#gui_font = CGUITTFont(guienv, font_file, 12)
		#if not gui_font:
			#gui_font = guienv.getBuiltInFont()
		skin = guienv.getSkin()
		#skin.setFont(gui_font)
		#gui_font.drop()
		menu_height = skin.getSize(EGDS_MENU_HEIGHT)

		if pybass:
			if pybass.BASS_Init(-1, 44100, 0, 0, 0):
				pybass.BASS_SetVolume(sound_volume)
				if os.path.isfile(sound_file):
					bass_handle = pybass.BASS_MusicLoad(False, sound_file, 0, 0, pybass.BASS_MUSIC_PRESCAN | pybass.BASS_SAMPLE_LOOP, 0)
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
		menu_device_types[EDT_SOFTWARE] = menu_device_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (driver_type == EDT_SOFTWARE))
		menu_device_types[EDT_OPENGL] = menu_device_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (driver_type == EDT_OPENGL))
		menu_device_types[EDT_DIRECT3D9] = menu_device_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (driver_type == EDT_DIRECT3D9))
		menu_device_types[EDT_BURNINGSVIDEO] = menu_device_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (driver_type == EDT_BURNINGSVIDEO))
		menu_sound = menu_options.addItem(_('Sound on/off'), GUI_ID_SOUND_ON_OFF, checked = play_sound)

		submenu = menu.getSubMenu(2)
		submenu.addItem(_('About'), GUI_ID_ABOUT)

		img_font = CGUITTFont(guienv, font_file, 36)
		if not img_font:
			img_font = guienv.getBuiltInFont()

		text1 = 'Merry Christmas!'
		text1_size = img_font.getDimension(text1)
		text2 = 'Happy New Year!'
		text2_size = img_font.getDimension(text2)

		text2pos = recti(50,10,0,0)

		scolor = SColor(255,120,102,136)
		img_color = SColor(255,255,255,255)

		#~ snowflake_x = 0
		#~ snowflake_y = 10
		#~ snowflake_z = 0

		ps = scene_manager.addParticleSystemSceneNode(False)
		em = ps.createBoxEmitter(aabbox3df(-100,-100,-100,100,0,100), vector3df(-0.01, 0.0, 0.0), 50, 100, SColor(0,255,255,255), SColor(0,255,255,255), 100, 1000)
		ps.setEmitter(em)
		#~ em.drop()
		paf = ps.createGravityAffector(vector3df(-0.05,-0.03, 0.0), 2000)
		ps.addAffector(paf)
		#~ try:
			#~ paf.drop()
		#~ except:
			#~ print('=== driver_type = %d, cause error with IParticleGravityAffector drop operation' % driver_type)
		ps.setMaterialFlag(EMF_LIGHTING, False)
		ps.setMaterialTexture(0, driver.getTexture('2DGame/snowflake.png'))
		ps.setMaterialType(EMT_TRANSPARENT_VERTEX_ALPHA)


		while device.run():
			if device.isWindowActive():
				if i_event_receiver.IsKeyDown(KEY_ESCAPE):
					break
				time = device.getTimer().getTime()
				i_event_receiver.screen_size = driver.getScreenSize()
				driver.beginScene(True, True, scolor)
				x, y = device.getCursorControl().getPosition().get_XY()
				if i_event_receiver.mouse_state['left']:
					if int(time/1500) % 2:
						driver.draw2DImage(santa, position2di(int((i_event_receiver.screen_size.X-santa_size.X)/2),int((i_event_receiver.screen_size.Y-santa_size.Y)/2)), recti(0,0,int(santa_size.X),int(santa_size.Y)), 0, img_color, True)
					else:
						driver.draw2DImage(santa_pipe, position2di(int((i_event_receiver.screen_size.X-santa_pipe_size.X)/2),int((i_event_receiver.screen_size.Y-santa_pipe_size.Y)/2)), recti(0,0,int(santa_pipe_size.X),int(santa_pipe_size.Y)), 0, img_color, True)
					#img_font.draw(text2, recti(int((i_event_receiver.screen_size.X-text2_size.X)/2),int((i_event_receiver.screen_size.Y-text2_size.Y)/2),0,0), SColor(255,time % 155,time % 155,255))
				else:
					if int(time/1500) % 2:
						#~ print('=== type', type(i_event_receiver.screen_size.X/2-bells_size.X/2))
						driver.draw2DImage(bells, position2di(int((i_event_receiver.screen_size.X-bells_size.X)/2),int((i_event_receiver.screen_size.Y-bells_size.Y)/2)), recti(0,0,int(bells_size.X),int(bells_size.Y)), 0, img_color, True)
					else:
						driver.draw2DImage(present_red, position2di(int((i_event_receiver.screen_size.X-present_red_size.X)/2),int((i_event_receiver.screen_size.Y-present_red_size.Y)/2)), recti(0,0,int(present_red_size.X),int(present_red_size.Y)), 0, img_color, True)
					#img_font.draw(text1, recti(int((i_event_receiver.screen_size.X-text1_size.X)/2),int((i_event_receiver.screen_size.Y-text1_size.Y)/2),0,0), SColor(255,time % 255,time % 255,255))
				driver.draw2DImage(cur_img, position2di(int(x-cur_img_size.X/2),int(y-cur_img_size.Y/2)), recti(0,0,int(cur_img_size.X),int(cur_img_size.Y)), 0, img_color, True)
				#~ if x < 0 or y < 0 or x > i_event_receiver.screen_size.X or y > i_event_receiver.screen_size.Y:
				if x < 0 or y < menu_height or x > i_event_receiver.screen_size.X or y > i_event_receiver.screen_size.Y or i_event_receiver.about_dialog or i_event_receiver.show_cursor:
					device.getCursorControl().setVisible(True)
				else:
					if not i_event_receiver.show_cursor:
						device.getCursorControl().setVisible(False)
				#~ driver.draw2DImage(snowflake, position2di(0,0), recti(0,0,int(snowflake_size.X),int(snowflake_size.Y)), 0, img_color, True)
				#~ if snowflake_y < 0:
					#~ snowflake_x = randint(-80, 80)
					#~ snowflake_y = 10
					#~ snowflake_z = randint(-80, 80)
				#~ else:
					#~ snowflake_y = snowflake_y - 1
				#~ snowflake_scene_node.setPosition(vector3df(snowflake_x, snowflake_y, snowflake_z))
				scene_manager.drawAll()
				guienv.drawAll()
				driver.endScene()
				device.sleep(50)
			else:
				device.yield_self()
		device.drop()
		device.closeDevice()
	else:
		print('ERROR createDevice')

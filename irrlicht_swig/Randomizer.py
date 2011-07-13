# Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license


import os, sys
from irrlicht import *
from random import randint
from locale import getdefaultlocale

GUI_ID_QUIT = 0x10000
GUI_ID_ABOUT = 0x10001
GUI_ID_CAMERA_NONE = 0x10002
GUI_ID_CAMERA_MAYA = 0x10003
GUI_ID_CAMERA_FIRST_PERSON = 0x10004
GUI_ID_LOG = 0x10005
GUI_ID_DRIVER = 0x10006

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
	#~ if not translations.has_key(source):
	if not source in translations:
		translation_file.write('\n' + source + ' = ' + source + '\n')
		translation_file.flush()
		translations[source] = source
	try:
		return unicode(translations[source], 'cp1251')
	except:
		return translations[source]

class UserIEventReceiver(IEventReceiver):
	game = None
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	NumbersKeys = {}
	value = 0
	for key in range(KEY_KEY_0, KEY_KEY_9):
		NumbersKeys[key] = str(value)
		value += 1
	value = 0
	for key in range(KEY_NUMPAD0, KEY_NUMPAD9):
		NumbersKeys[key] = str(value)
		value += 1
	answer = ''
	def OnEvent(self, event):
		#~ print ('EventType', event.EventType)
		#~ if event.EventType == EET_MOUSE_INPUT_EVENT:
			#~ print 'MouseInput', event.MouseInput.X, event.MouseInput.Y
			#~ print 'isLeftPressed(), isRightPressed(), isMiddlePressed()', event.MouseInput.isLeftPressed(), event.MouseInput.isRightPressed(), event.MouseInput.isMiddlePressed()
		event_type = self.GetEventType(event)
		if event_type is EET_KEY_INPUT_EVENT:
			key_event = self.GetKeyInput(event)
			pressed_down = self.KeyInput_PressedDown(key_event)
			self.KeyIsDown[self.KeyInput_Key(key_event)] = pressed_down
			if self.KeyInput_Key(key_event) in (KEY_KEY_0, KEY_KEY_1, KEY_KEY_2, KEY_KEY_3, KEY_KEY_4, KEY_KEY_5, KEY_KEY_6, KEY_KEY_7, KEY_KEY_8, KEY_KEY_9, KEY_NUMPAD0, KEY_NUMPAD1, KEY_NUMPAD2, KEY_NUMPAD3, KEY_NUMPAD4, KEY_NUMPAD5, KEY_NUMPAD6, KEY_NUMPAD7, KEY_NUMPAD8, KEY_NUMPAD9) and not pressed_down:
				#~ #print self.KeyInput_Key(key_event), self.KeyInput_PressedDown(key_event)
				self.answer += self.NumbersKeys[self.KeyInput_Key(key_event)]
			elif self.KeyInput_Key(key_event) in (KEY_BACK, KEY_DELETE) and not pressed_down:
				self.answer = ''
			#~ return True
		elif event.EventType == EET_GUI_EVENT:
			gui_event_type = self.GUIEvent_EventType(event.GUIEvent)
			caller = self.GUIEvent_Caller(event.GUIEvent)
			id = caller.getID()
			#~ self.game.device.getLogger().log('==='+str(id)+str(gui_event_type))
			if gui_event_type == EGET_MENU_ITEM_SELECTED:
				menu = caller.as_IGUIContextMenu()
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				#~ self.game.device.getLogger().log('+++ menu_id'+str(menu_id))
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				elif menu_id == GUI_ID_CAMERA_NONE:
					cam = self.game.scene_manager.getActiveCamera()
					cam.setInputReceiverEnabled(not cam.isInputReceiverEnabled())
				elif menu_id == GUI_ID_CAMERA_MAYA:
					self.game.setActiveCamera(self.game.camera[0])
				elif menu_id == GUI_ID_CAMERA_FIRST_PERSON:
					self.game.setActiveCamera(self.game.camera[1])
		return False
	def IsKeyDown(self, keyCode):
		return self.KeyIsDown[keyCode];

class game:
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

	def create_wall_plane_selector(self, i_geometry_creator, tileSize, tileCount, material, textureRepeatCount, pos = None, rotation = None):
		i_mesh = i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)
		i_mesh_scene_node = self.scene_manager.addMeshSceneNode(i_mesh)
		if pos:
			i_mesh_scene_node.setPosition(pos)
		if rotation:
			i_mesh_scene_node.setRotation(rotation)
		selector = self.scene_manager.createTriangleSelector(i_mesh_scene_node.getMesh(), i_mesh_scene_node)
		i_mesh_scene_node.setTriangleSelector(selector)
		i_mesh.drop()
		return selector

	def setActiveCamera(self, camera):
		if self.device and camera:
			active = self.device.getSceneManager().getActiveCamera()
			active.setInputReceiverEnabled(False)
			camera.setInputReceiverEnabled(True)
			self.device.getSceneManager().setActiveCamera(camera)

	def start(self):
		#~ self.drv = EDT_SOFTWARE
		self.drv = EDT_OPENGL
		#~ self.drv = EDT_DIRECT3D9
		#~ self.drv = EDT_BURNINGSVIDEO
		self.windowSize = dimension2du(640, 480)
		#~ i_event_receiver = UserIEventReceiver()
		#~ self.device = createDevice(drv, windowSize, receiver = i_event_receiver)
		#~ i_event_receiver.game = self
		self.device = createDevice(self.drv, self.windowSize)

		if self.device:
			self.device.setWindowCaption(_(app_name))
			self.device.setResizable(True)
			self.driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.guienv = self.device.getGUIEnvironment()

			self.font_size = 24
			font_ext = '.ttf'
			font_path = os.environ['SYSTEMROOT']+'/Fonts/'
			self.font_file = font_path + 'arial' + font_ext
			#~ self.font_file = font_path + 'E111Viva' + font_ext
			#~ self.font_file = font_path + 'Lithogrl' + font_ext
			#~ self.vect_font = self.guienv.getBuiltInFont().createTTFont(self.guienv, self.font_file, self.font_size)
			if IRR_COMPILE_WITH_CGUITTFONT:
				self.vect_font = self.guienv.getFont(self.font_file, self.font_size)
			else:
				self.vect_font = self.guienv.createTTFont(self.font_file, self.font_size)
			self.skin = self.guienv.getSkin()
			#~ self.vect_font = skin.getFont().as_CGUITTFont().createTTFont(guienv, font_file, font_size)
			if self.vect_font:
				self.skin.setFont(self.vect_font)
				self.vect_font.drop()
			else:
				print ('ERROR vect_font not created !!!')
			menu_height = self.skin.getSize(EGDS_MENU_HEIGHT)

			menu = self.guienv.addMenu()
			menu.addItem(_('File'), -1, True, True)
			menu.addItem(_('View'), -1, True, True)
			menu.addItem(_('Options'), -1, True, True)
			menu.addItem(_('Help'), -1, True, True)

			submenu = menu.getSubMenu(0)
			#~ submenu.addItem("Open Model File & Texture...", GUI_ID_OPEN_MODEL)
			#~ submenu.addItem("Set Model Archive...", GUI_ID_SET_MODEL_ARCHIVE)
			#~ submenu.addItem("Load as Octree", GUI_ID_LOAD_AS_OCTREE)
			#~ submenu.addSeparator()
			submenu.addItem(_('Quit'), GUI_ID_QUIT)

			submenu = menu.getSubMenu(1)
			submenu.addItem(_('Without camera'), GUI_ID_CAMERA_NONE)
			submenu.addItem(_('Maya Style'), GUI_ID_CAMERA_MAYA)
			submenu.addItem(_('First Person'), GUI_ID_CAMERA_FIRST_PERSON)

			submenu = menu.getSubMenu(2)
			submenu.addItem(_('Start/stop log'), GUI_ID_LOG)
			submenu.addItem(_('Choose graphics driver'), GUI_ID_DRIVER)

			submenu = menu.getSubMenu(3)
			submenu.addItem(_('About'), GUI_ID_ABOUT)

			i_gui_static_text = self.guienv.addStaticText('', recti(0, menu_height, self.windowSize.Width, self.windowSize.Height - menu_height))

			i_geometry_creator = self.scene_manager.getGeometryCreator()

			# random volume variable
			tile_count = 50#randint(10, 50)
			# height volume
			height = 200
			# len tile
			tile_len = 100
			# texture from file or dynamic generator
			#~ texture_from_file = True
			texture_from_file = False


			texture = None
			file_name = 'media//skydome.jpg'
			if os.path.exists(file_name) and texture_from_file:
				texture = self.driver.getTexture(file_name)
			else:
				texture = self.texture_generator(ECF_R8G8B8, dimension2du(64, 64), 'skydome')
			sky_node = self.scene_manager.addSkyDomeSceneNode(texture)

			# top and bottom plane
			tileSize = dimension2df(tile_len, tile_len)
			tileCount = dimension2du(tile_count, tile_count)
			textureRepeatCount = dimension2df(tile_count, tile_count)
			material = SMaterial()
			file_name = 'media//stones.jpg'
			material.EmissiveColor = SColor(0,255,255,255)
			if os.path.exists(file_name) and texture_from_file:
				material.setTexture(0, self.driver.getTexture(file_name))
			else:
				texture = self.texture_generator(ECF_R8G8B8, dimension2du(4, 4), 'bottom', 0, (0, 0), (0, 255), (0, 100))
				material.setTexture(0, texture)

			i_mesh_top = i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)
			file_name = 'media//opengllogo.png'
			if self.drv == EDT_SOFTWARE:
				file_name = 'media//irrlichtlogoalpha.tga'
			elif self.drv == EDT_BURNINGSVIDEO:
				file_name = 'media//burninglogo.png'
			elif self.drv in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				file_name = 'media//directxlogo.png'
			if os.path.exists(file_name) and texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				material.setTexture(0, self.driver.getTexture(file_name))
			else:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(2, 2), 'top', 196)
				material.setTexture(0, texture)
			i_mesh_bottom = i_geometry_creator.createPlaneMesh(tileSize, tileCount, material, textureRepeatCount)
			i_mesh_scene_node_top = self.scene_manager.addOctreeSceneNode(i_mesh_top)
			i_mesh_scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_mesh_bottom)
			#~ i_mesh_scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_mesh_bottom, i_mesh_scene_node_top)
			i_mesh_scene_node_bottom.setPosition(vector3df(0,height,0))
			i_mesh_scene_node_bottom.setRotation(vector3df(180,0,0))
			selector_top = self.scene_manager.createOctreeTriangleSelector(i_mesh_scene_node_top.getMesh(), i_mesh_scene_node_top)
			selector_bottom = self.scene_manager.createOctreeTriangleSelector(i_mesh_scene_node_bottom.getMesh(), i_mesh_scene_node_bottom)
			i_mesh_scene_node_top.setTriangleSelector(selector_top)
			i_mesh_scene_node_bottom.setTriangleSelector(selector_bottom)
			#~ print i_mesh_scene_node_top.getPosition()

			# left, right, front and back plane
			tileCount = dimension2du(tile_count, height / tile_len)
			textureRepeatCount = dimension2df(tile_count, height / tile_len)
			file_name = 'media//wall.jpg'
			if os.path.exists(file_name) and texture_from_file:
				material.MaterialType = EMT_LIGHTMAP
				material.setTexture(0, self.driver.getTexture(file_name))
			else:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'front', 196, (0, 255), (0, 0), (0, 100))
				material.setTexture(0, texture)
			p = tile_count * tile_len / 2
			selector_front = self.create_wall_plane_selector(
				i_geometry_creator, 
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(0, height / 2, p), 
				vector3df(-90,0,0))
			if not texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'back', 196, (0, 0), (0, 50), (0, 255))
				material.setTexture(0, texture)
			selector_back = self.create_wall_plane_selector(
				i_geometry_creator, 
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(0, height / 2, -p), 
				vector3df(90,0,0))
			if not texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'left', 196, (0, 0), (0, 0), (100, 255))
				material.setTexture(0, texture)
			selector_left = self.create_wall_plane_selector(
				i_geometry_creator, 
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(-p, height / 2, 0),
				vector3df(90,90,0))
			if not texture_from_file:
				material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'right', 196, (0, 0), (100, 255), (0, 0))
				material.setTexture(0, texture)
			selector_right = self.create_wall_plane_selector(
				i_geometry_creator, 
				tileSize, 
				tileCount, 
				material, 
				textureRepeatCount, 
				vector3df(p, height / 2, 0),
				vector3df(90,-90,0))

			# ADD MAGIC VOLUME
			i_scene_node = self.scene_manager.addSphereSceneNode(40.0, id = 1, position = vector3df(0,60,0))
			if i_scene_node:
				file_name = 'media//wall.jpg'
				if os.path.exists(file_name) and texture_from_file:
					i_scene_node.setMaterialFlag(EMF_LIGHTING, False)
					i_scene_node.setMaterialTexture(0, driver.getTexture(file_name))
				else:
					material = i_scene_node.getMaterial(0)
					material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
					texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(8, 8), 'magic', 196)
					i_scene_node.setMaterialTexture(0, texture)
			selector_magic = self.scene_manager.createTriangleSelector(i_scene_node.getMesh(), i_scene_node)
			i_scene_node.setTriangleSelector(selector_magic)
			i_scene_node.setName('magic_scene_node')

			keyMap = self.scene_manager.create_keymaps(10)
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
			#~ def addCameraSceneNodeFPS(self, parent = ISceneNode(0), rotateSpeed = 100.0, moveSpeed = 0.5, id = -1, keyMapArray = KeyMap, keyMapSize = 0, noVerticalMovement = False, jumpSpeed = 0.0, invertMouse = False):
			#~ camera = self.scene_manager.addCameraSceneNodeFPS(i_mesh_scene_node_top)
			#~ camera = self.scene_manager.addCameraSceneNodeFPS()
			self.camera = (self.scene_manager.addCameraSceneNodeMaya(), self.scene_manager.addCameraSceneNodeFPS(keyMapArray = keyMap, keyMapSize = 10, jumpSpeed = 5))
			self.camera[0].setPosition(vector3df(100,60,0))
			self.camera[0].setTarget(vector3df(0,30,0))
			self.camera[1].setPosition(vector3df(100,60,0))
			self.setActiveCamera(self.camera[0])

			i_meta_triangle_selector = self.scene_manager.createMetaTriangleSelector()
			i_meta_triangle_selector.addTriangleSelector(selector_top)
			i_meta_triangle_selector.addTriangleSelector(selector_bottom)
			i_meta_triangle_selector.addTriangleSelector(selector_front)
			i_meta_triangle_selector.addTriangleSelector(selector_back)
			i_meta_triangle_selector.addTriangleSelector(selector_left)
			i_meta_triangle_selector.addTriangleSelector(selector_right)
			i_meta_triangle_selector.addTriangleSelector(selector_magic)

			anim = self.scene_manager.createCollisionResponseAnimator(i_meta_triangle_selector, self.camera[1])
			self.camera[1].addAnimator(anim)
			anim.drop()

			#~ i_timer = self.device.getTimer()
			#~ i_timer.stop()

			self.cursor_control = self.device.getCursorControl()
			#~ self.cursor_control.setVisible(False)

			scolor = SColor(255,120,102,136)

			self.collision_manager = self.scene_manager.getSceneCollisionManager()

			i_event_receiver = UserIEventReceiver()
			i_event_receiver.game = self
			self.device.setEventReceiver(i_event_receiver)

			dlg = None
			a, b = 0, 0

			check_collisions = True
			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.IsKeyDown(KEY_ESCAPE):
						break
					self.driver.beginScene(True, True, scolor)
					self.scene_manager.drawAll()

					if not dlg:
						# if not i_timer.isStopped():
							# if i_timer.getTime() > 1000:
								# i_timer.stop()
								# i_timer.setTime(0)
								# check_collisions = True
							# else:
								# i_timer.tick()
								# check_collisions = False
						if check_collisions:
							selectedSceneNode = self.collision_manager.getSceneNodeFromCameraBB(self.camera[1])
							if selectedSceneNode:
								if selectedSceneNode.getType() == ESNT_SPHERE:
									# print selectedSceneNode.getName(), selectedSceneNode.getID()
									a, b = randint(0, 9), randint(0, 9)
									dlg = self.guienv.addMessageBox(_('Warning'), _('Please enter answer and press "Enter"') + '\n%d x %d =' % (a, b))
					else:
						if i_event_receiver.IsKeyDown(KEY_RETURN):
							check_answer = _('Correctly')
							if str(a * b) != i_event_receiver.answer:
								check_answer = _('Not correctly') + '\n' + _('Correctly answer is') + ' %d' % (a * b)
								i_gui_static_text.setDrawBackground(True)
								i_gui_static_text.setBackgroundColor(SColor(128,255,0,0))
							else:
								i_gui_static_text.setDrawBackground(False)
							i_gui_static_text.setText(i_event_receiver.answer + '\n' + check_answer)
							i_event_receiver.answer = ''
							# btn_close = dlg.getCloseButton()
							# btn_close.setPressed()
							dlg.remove()
							dlg = None
							# i_timer.start()
						# else:
							# if dlg.IsNull():
								# dlg = None
					# if dlg:
						# cursor_control.setVisible(True)
					# else:
						# cursor_control.setVisible(False)

					self.guienv.drawAll()
					self.driver.endScene()
					self.device.sleep(10)
					#~ print self.scene_manager.getActiveCamera().getPosition()
				else:
					self.device._yield()
			self.device.drop()
		else:
			print ('ERROR createDevice')

def main():
	g = game()
	g.start()

if __name__ == "__main__":
	main()
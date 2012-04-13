# Copyright(c) Max Kolosov 2010-2012 maxkolosov@inbox.ru
# http://pir.sourceforge.net     http://pyirrlicht.googlecode.com
# BSD license
'Python 3d Game Editor for create 3d world'

import os
#~ os.environ['IRRLICHT_C_LIBRARY'] = 'irrlicht_c_173'

import sys
from math import pow, sqrt, acos, tan, atan, degrees
from pyirrlicht import *
from random import randint
from locale import getdefaultlocale

app_name = __doc__
app_path = os.getcwd()
app_file_name = os.path.basename(sys.argv[0].split('.')[0])

GUI_ID_QUIT = 0x10000
GUI_ID_ABOUT = 0x10001
GUI_ID_LOAD = 0x10002
GUI_ID_SAVE = 0x10003
GUI_ID_CAMERA_NONE = 0x10004
GUI_ID_CAMERA_MAYA = 0x10005
GUI_ID_CAMERA_FPS = 0x10006
GUI_ID_CAMERA_TOP = 0x10007
GUI_ID_LOG = 0x10008
GUI_ID_TEXTURE_FROM_FILE = 0x10009
GUI_ID_DRIVER = 0x1000A
GUI_ID_EDT_SOFTWARE = GUI_ID_DRIVER | EDT_SOFTWARE
GUI_ID_EDT_BURNINGSVIDEO = GUI_ID_DRIVER | EDT_BURNINGSVIDEO
GUI_ID_EDT_DIRECT3D9 = GUI_ID_DRIVER | EDT_DIRECT3D9
GUI_ID_EDT_OPENGL = GUI_ID_DRIVER | EDT_OPENGL
GUI_ID_OPEN_FILE_DIALOG_WALL_TEXTURE = 0x1000F
GUI_ID_MODEL_INSERT = 0x10010
GUI_ID_MODEL_INSERT_DIALOG = 0x10011
GUI_ID_MODEL_SET_ARCHIVE = 0x10012
GUI_ID_MODEL_SET_ARCHIVE_DIALOG = 0x10013
GUI_ID_FILE_DIALOG_LOAD_PROJECT = 0x10014
GUI_ID_FILE_DIALOG_SAVE_PROJECT = 0x10015

# simple language translator
default_locale = getdefaultlocale()[0]
translation_catalog = 'lang'
if not os.path.isdir(translation_catalog):
	os.mkdir(translation_catalog)
translation_catalog += '//'# only for python 2.4.4 version and isdir function
translation_file_name = translation_catalog + app_file_name + '_' + default_locale + '.lng'
if not os.path.exists(translation_file_name):
	default_locale = 'en_US'
	translation_file_name = translation_catalog + app_file_name + '_' + default_locale + '.lng'
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
	framework = None
	KeyIsDown = {}
	for key in range(KEY_KEY_CODES_COUNT):
		KeyIsDown[key] = False
	mouse_position = position2di()
	mouse_position_3d_start = vector3df()
	mouse_position_3d = vector3df()
	exists_mouse_3d = False
	l_mouse_pressed = False
	r_mouse_pressed = False
	is_gui_active = False

	def OnEvent(self, event):
		event_type = self.GetEventType(event)
		if event_type is EET_KEY_INPUT_EVENT:
			key_event = self.GetKeyInput(event)
			pressed_down = self.KeyInput_PressedDown(key_event)
			self.KeyIsDown[self.KeyInput_Key(key_event)] = pressed_down
		elif event_type == EET_GUI_EVENT and (not self.l_mouse_pressed or not self.r_mouse_pressed):
			self.is_gui_active = True
			GUIEvent = self.GetGUIEvent(event)
			gui_event_type = self.GUIEvent_EventType(GUIEvent)
			caller = self.GUIEvent_Caller(GUIEvent)
			caller_id = caller.getID()
			if gui_event_type == EGET_MENU_ITEM_SELECTED:
				menu = caller.as_IGUIContextMenu()
				menu_id = menu.getItemCommandId(menu.getSelectedItem())
				if menu_id == GUI_ID_QUIT:
					self.KeyIsDown[KEY_ESCAPE] = True
				elif menu_id == GUI_ID_ABOUT:
					self.framework.guienv.addMessageBox(_('About'), app_file_name + ' - ' + _(app_name))
				elif menu_id == GUI_ID_LOAD:
					dlg = self.framework.guienv.addFileSelectorDialog(_('Please select project file name for load'), rectangle = recti(10,30,500,450), id = GUI_ID_FILE_DIALOG_LOAD_PROJECT)
					dlg.addFileFilter('XML', 'xml')
					return True
				elif menu_id == GUI_ID_SAVE:
					dlg = self.framework.guienv.addFileSelectorDialog(_('Please insert project file name for save'), rectangle = recti(10,30,500,450), id = GUI_ID_FILE_DIALOG_SAVE_PROJECT, type = EFST_SAVE_DIALOG)
					dlg.addFileFilter('XML', 'xml')
					return True
				elif menu_id == GUI_ID_CAMERA_NONE:
					self.framework.active_camera_off()
				elif menu_id == GUI_ID_CAMERA_MAYA:
					self.framework.set_active_camera(self.framework.camera[0])
					self.framework.ceiling.setVisible(True)
				elif menu_id == GUI_ID_CAMERA_FPS:
					self.framework.set_active_camera(self.framework.camera[1])
					self.framework.ceiling.setVisible(True)
				elif menu_id == GUI_ID_CAMERA_TOP:
					self.framework.ceiling.setVisible(False)
					self.framework.set_active_camera(self.framework.camera[2])
				elif menu_id == GUI_ID_LOG:
					if self.framework.log_file_stream:
						tool_close_stream(self.framework.log_file_stream)
						self.framework.log_file_stream = None
					else:
						self.framework.log_file_stream = tool_redirect_stdout_to_file(app_file_name + '.log', 'w')
				elif menu_id == GUI_ID_TEXTURE_FROM_FILE:
					self.framework.set_textures()
				elif menu_id == GUI_ID_EDT_SOFTWARE:
					self.framework.set_device_type(EDT_SOFTWARE)
				elif menu_id == GUI_ID_EDT_OPENGL:
					self.framework.set_device_type(EDT_OPENGL)
				elif menu_id == GUI_ID_EDT_DIRECT3D9:
					self.framework.set_device_type(EDT_DIRECT3D9)
				elif menu_id == GUI_ID_EDT_BURNINGSVIDEO:
					self.framework.set_device_type(EDT_BURNINGSVIDEO)
				elif menu_id == GUI_ID_MODEL_INSERT:
					self.framework.guienv.addFileOpenDialog(_('Please select a model file to insert'), id = GUI_ID_MODEL_INSERT_DIALOG)
				elif menu_id == GUI_ID_MODEL_SET_ARCHIVE:
					self.framework.guienv.addFileOpenDialog(_('Please select models archive/directory'), id = GUI_ID_MODEL_SET_ARCHIVE_DIALOG)
			elif gui_event_type == EGET_FILE_SELECTED and caller_id == GUI_ID_FILE_DIALOG_LOAD_PROJECT:
				project_file = type_str(CGUIFileSelector(caller).getFileName())
				print('=== LOAD PROJECT FILE %s' % project_file)
				self.framework.scene_manager.loadScene(project_file)
			elif gui_event_type == EGET_FILE_SELECTED and caller_id == GUI_ID_FILE_DIALOG_SAVE_PROJECT:
				project_file = type_str(CGUIFileSelector(caller).getFileName())
				print('=== SAVE PROJECT FILE %s' % project_file)
				result = self.framework.scene_manager.saveScene(project_file)
			elif gui_event_type == EGET_FILE_SELECTED and caller_id == GUI_ID_OPEN_FILE_DIALOG_WALL_TEXTURE:
				gui_dialog = IGUIFileOpenDialog(caller)
				wall_texture_file = type_str(gui_dialog.getFileName())
				i_mesh_scene_node = self.framework.walls[-1]
				texture = self.framework.driver.getTexture(wall_texture_file)
				#~ self.framework.driver.makeNormalMapTexture(texture)
				i_mesh_scene_node.setMaterialTexture(0, texture)
				self.is_gui_active = False
			elif gui_event_type == EGET_FILE_SELECTED and caller_id == GUI_ID_MODEL_INSERT_DIALOG:
				file_name = type_str(IGUIFileOpenDialog(caller).getFileName())
				mesh = self.framework.scene_manager.getMesh(file_name)
				#~ model = self.framework.scene_manager.addOctreeSceneNode(mesh.getMesh(0))
				model = self.framework.scene_manager.addAnimatedMeshSceneNode(mesh)
				model.setPosition(self.mouse_position_3d_start)
				model.setMaterialFlag(EMF_LIGHTING, True)
				model.setMaterialFlag(EMF_NORMALIZE_NORMALS, True)
				model.setDebugDataVisible(EDS_BBOX | EDS_MESH_WIRE_OVERLAY)
			elif gui_event_type == EGET_FILE_SELECTED and caller_id == GUI_ID_MODEL_SET_ARCHIVE_DIALOG:
				file_name = type_str(IGUIFileOpenDialog(caller).getFileName())
				if file_name.rsplit('.', 1) in ('.pk3', '.zip', '.pak', '.npk'):
					self.framework.file_system.addFileArchive(file_name)
			if gui_event_type in (EGET_ELEMENT_FOCUS_LOST, EGET_ELEMENT_LEFT):
				self.is_gui_active = False
		elif event_type == EET_MOUSE_INPUT_EVENT and not self.is_gui_active:
			active_camera_top = self.framework.is_active_camera_top()
			if active_camera_top > 0:
				mouse_event = self.GetMouseInput(event)
				mouse_event_type = self.MouseInput_EventType(mouse_event)
				if active_camera_top < 2:
					self.framework.active_camera_on()
				if mouse_event_type == EMIE_MOUSE_WHEEL:
					self.framework.scale_delta = self.MouseInput_Wheel(mouse_event)
					self.framework.scale_camera_top()
				elif mouse_event_type == EMIE_MOUSE_MOVED:
					self.mouse_position.X = self.MouseInput_X(mouse_event)
					self.mouse_position.Y = self.MouseInput_Y(mouse_event)
					#~ self.exists_mouse_3d = False
					#~ if self.mouse_position.Y > self.framework.menu_height:
					ray = self.framework.scene_manager.getSceneCollisionManager().getRayFromScreenCoordinates(self.mouse_position, self.framework.camera[2])
					plane = plane3df(self.framework.grid.getPosition(), vector3df(0, 10, 0))
					self.exists_mouse_3d = plane.getIntersectionWithLine(ray.start, ray.getVector(), self.mouse_position_3d)
					#~ else:
						#~ self.mouse_position_3d = vector3df()
					self.framework.device.setWindowCaption(_(app_name) + ' 2d(x = %d  y = %d), 3d(x = %f  y = %f  z = %f)' % (self.mouse_position.X, self.mouse_position.Y, self.mouse_position_3d.X, self.mouse_position_3d.Y, self.mouse_position_3d.Z))
				elif mouse_event_type == EMIE_RMOUSE_PRESSED_DOWN:
					self.r_mouse_pressed = True
					self.cursor_start()
				elif mouse_event_type == EMIE_LMOUSE_PRESSED_DOWN:
					self.l_mouse_pressed = True
					if not self.framework.last_wall:
						self.cursor_start()
				elif mouse_event_type == EMIE_LMOUSE_LEFT_UP:
					if self.l_mouse_pressed and (self.mouse_position_3d_start.X != self.mouse_position_3d.X or self.mouse_position_3d_start.Z != self.mouse_position_3d.Z):
						delta_x = self.mouse_position_3d_start.X - self.mouse_position_3d.X
						delta_z = self.mouse_position_3d_start.Z - self.mouse_position_3d.Z
						#~ length = sqrt(pow(delta_x,2)+pow(delta_z,2))
						length = self.mouse_position_3d.getDistanceFrom(self.mouse_position_3d_start)
						vlength = length/self.framework.tile_count.X
						x = self.mouse_position_3d_start.X - (delta_x / 2)
						y = self.framework.wall_height / 2
						z = self.mouse_position_3d_start.Z - (delta_z / 2)

						if self.mouse_position_3d_start.Z > self.mouse_position_3d.Z:
							delta_x *= -1
						angle = 180
						if self.mouse_position_3d_start.X == self.mouse_position_3d.X:
							angle = 90
						elif self.mouse_position_3d_start.Z == self.mouse_position_3d.Z:
							angle = 0
						else:
							angle = degrees(acos(delta_x/length))

						self.framework.guienv.addFileOpenDialog(_('Please select a texture wall file to open'), id = GUI_ID_OPEN_FILE_DIALOG_WALL_TEXTURE)

						selector_wall = self.framework.create_wall_plane_selector(
							vector3df(x, y, z),# POSITION
							vector3df(270,angle,0),# ROTATION
							vector2df(vlength, 100),# TILE_SIZE
							#~ texture_repeat = vector2df(1,1),
							texture_repeat = vector2df(
								self.framework.wall_texture_repeat_count.X / vlength,
								self.framework.wall_texture_repeat_count.Y
							),
							selector_from_bounding_box = True
						)
						self.framework.i_meta_triangle_selector.addTriangleSelector(selector_wall)
						#~ self.framework.last_wall = selector_wall
						#~ self.framework.last_wall.setRotation(vector3df(0, 0, 90))
						#~ self.framework.walls.append(self.framework.last_wall)
					self.l_mouse_pressed = False
				elif mouse_event_type == EMIE_RMOUSE_LEFT_UP:
					self.r_mouse_pressed = False
					new_pos = vector3df(self.mouse_position_3d_start.X, self.framework.camera[2].getPosition().Y, self.mouse_position_3d_start.Z)
					self.framework.camera[2].setPosition(new_pos)
					new_pos.Y = 0
					self.framework.camera[2].setTarget(new_pos)
					#~ self.framework.camera[2].setUpVector(new_pos)
		elif event_type == EET_LOG_TEXT_EVENT:
			log_event = self.GetLogEvent(event)
			if self.LogEvent_Level(log_event) == 0 and self.LogEvent_Text(log_event).find('Resizing window') > -1:
				self.framework.window_size = self.framework.driver.getScreenSize()
		return False

	def cursor_start(self):
		self.mouse_position_3d_start.X = self.mouse_position_3d.X
		self.mouse_position_3d_start.Y = self.mouse_position_3d.Y
		self.mouse_position_3d_start.Z = self.mouse_position_3d.Z

	def is_key_down(self, keyCode):
		return self.KeyIsDown[keyCode];

class framework:
	def __init__(self, *args, **kwargs):
		self.config_file_name = kwargs.pop('config_file_name', '%s.ini'%app_file_name)
		self.config = config(file_name = self.config_file_name)
		self.view_scale = self.config.get_float('view_scale', 1.0)
		self.scale_delta = 0.0
		self.sleep_delay = self.config.get_int('sleep_delay', 10)
		self.texture_from_file = self.config.get_bool('texture_from_file', False)
		#~ self.device_type = self.config.get_int('device_type', EDT_OPENGL)
		self.driver = None
		self.device_parameters = SIrrlichtCreationParameters()
		self.device_parameters.DriverType = self.config.get_int('driver_type', EDT_OPENGL)
		self.device_parameters.WindowSize = dimension2du(self.config.get_int('window_width', 640), self.config.get_int('window_height', 480))
		self.device_parameters.AntiAlias = 2
		self.device_parameters.WithAlphaChannel = True
		self.device = createDeviceEx(self.device_parameters)
		self.init_framework()
		self.i_geometry_creator = None
		self.i_meta_triangle_selector = None
		self.menu_options = None
		self.menu_device_types = {}
		self.help_dialog = None
		self.walls = []
		self.last_wall = None
		self.wall_height = self.config.get_int('wall_height', 200)
		self.tile_count_x = self.config.get_int('tile_count_x', 0)
		if self.tile_count_x == 0:
			self.tile_count_x = randint(10, 50)
		self.tile_count_y = self.config.get_int('tile_count_y', 0)
		if self.tile_count_y == 0:
			self.tile_count_y = randint(10, 50)
		self.tile_count_y = self.tile_count_x
		self.tile_count = vector2du(self.tile_count_x, self.tile_count_y)
		self.tile_size = vector2df(*self.config.get('tile_size', (100, 100)))
		self.texture_repeat_count = vector2df(self.tile_count_x, self.tile_count_y)
		#===================wall=====================
		self.wall_tile_size = vector2df(*self.config.get('wall_tile_size', (100, 100)))
		self.wall_tile_count = vector2du(self.tile_count_x, int(self.wall_height / self.wall_tile_size.X))
		#~ self.wall_tile_count = vector2du(self.tile_count_x, self.tile_count_y)
		self.wall_texture_repeat_count = vector2df(self.wall_tile_count.X, self.wall_tile_count.Y)
		#===================SMaterial=====================
		self.material = SMaterial()
		file_name = 'media//stones.jpg'
		self.material.EmissiveColor = SColor(0,255,255,255)
		self.material.Wireframe = True
		self.material.FogEnable = True
		if self.driver:
			if os.path.exists(file_name) and self.texture_from_file:
				self.material.setTexture(0, self.driver.getTexture(file_name))
			else:
				texture = self.texture_generator(ECF_R8G8B8, dimension2du(4, 4), 'material', 0, (0, 0), (0, 255), (0, 100))
				self.material.setTexture(0, texture)
			#===================Fog=====================
			self.driver.setFog(start=1.0, end=1000.0)
			#================SVG IImageLoader=============
			self.driver.addExternalImageLoader(agg_svg_loader(self.driver))
			#~ self.driver.addAggSvgImageLoader()
		self.log_file_stream = None

	def __del__(self):
		if self.device:
			self.stop()
		self.config.close()
		if self.log_file_stream:
			tool_close_stream(self.log_file_stream)
			self.log_file_stream = None

	def init_framework(self):
		if self.device:
			self.device.setWindowCaption(_(app_name))
			self.device.setResizable(True)
			self.driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.guienv = self.device.getGUIEnvironment()
			self.file_system = self.device.getFileSystem()

	def show_warning(self):
		self.guienv.addMessageBox(_('Warning'), _('For finish this operation you need restart application!'))

	def set_device_type(self, new_driver_type = 0):
		self.device_parameters.DriverType = new_driver_type
		for dev_type, menu_index in self.menu_device_types.items():
			self.menu_device_type.setItemChecked(menu_index, (self.device_parameters.DriverType == dev_type))
		self.config.set('driver_type', self.device_parameters.DriverType)
		self.show_warning()

	def set_textures(self):
		self.texture_from_file = not self.texture_from_file
		if self.menu_options:
			self.menu_options.setItemChecked(self.menu_texture_from_file, self.texture_from_file)
		self.show_warning()
		self.config.set('texture_from_file', self.texture_from_file)

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

	def create_wall_plane_selector(self, pos = None, rotation = None, tile_size = None, tile_count = None, texture_repeat = None, selector_from_bounding_box = False, material = None):
		if not tile_size:
			tile_size = self.wall_tile_size
		if not tile_count:
			tile_count = self.wall_tile_count
		if not texture_repeat:
			texture_repeat = self.wall_texture_repeat_count
		if not material:
			material = self.material
		i_mesh = self.i_geometry_creator.createPlaneMesh(tile_size, tile_count, material, texture_repeat)
		i_mesh_scene_node = self.scene_manager.addMeshSceneNode(i_mesh)
		if pos:
			i_mesh_scene_node.setPosition(pos)
		if rotation:
			i_mesh_scene_node.setRotation(rotation)
		if selector_from_bounding_box:
			selector = self.scene_manager.createTriangleSelectorFromBoundingBox(i_mesh_scene_node)
		else:
			selector = self.scene_manager.createTriangleSelector(i_mesh_scene_node.getMesh(), i_mesh_scene_node)
		i_mesh_scene_node.setTriangleSelector(selector)
		self.walls.append(i_mesh_scene_node)
		return selector

	def is_active_camera_top(self):
		result = 0
		cam = self.scene_manager.getActiveCamera()
		if cam:
			if cam.getID() == GUI_ID_CAMERA_TOP:
				result = 1
				if cam.isInputReceiverEnabled():
					result = 2
		return result

	def active_camera_on(self):
		cam = self.scene_manager.getActiveCamera()
		if cam:
			cam.setInputReceiverEnabled(True)

	def active_camera_off(self):
		cam = self.scene_manager.getActiveCamera()
		if cam:
			cam.setInputReceiverEnabled(not cam.isInputReceiverEnabled())

	def set_active_camera(self, new_active_camera):
		if new_active_camera:
			old_active_camera = self.scene_manager.getActiveCamera()
			if old_active_camera:
				old_active_camera.setInputReceiverEnabled(False)
			new_active_camera.setInputReceiverEnabled(True)
			self.scene_manager.setActiveCamera(new_active_camera)

	def scale_camera_top(self):
		self.camera[2].setPosition(vector3df(self.camera[2].getPosition().X, self.camera[2].getPosition().Y + self.scale_delta * 10, self.camera[2].getPosition().Z))

	def start(self):
		if self.device:
			self.font_size = 24
			font_ext = '.ttf'
			font_path = os.environ['SYSTEMROOT']+'/Fonts/'
			self.font_file = font_path + 'arial' + font_ext
			#~ self.font_file = font_path + 'cour' + font_ext
			#~ self.font_file = font_path + 'comic' + font_ext
			self.vect_font = CGUITTFont(self.guienv, self.font_file, self.font_size)
			self.skin = self.guienv.getSkin()
			if self.vect_font:
				self.skin.setFont(self.vect_font)
				self.vect_font.drop()
			else:
				print ('ERROR vect_font not created !!!')
				#~ self.font = self.guienv.getBuiltInFont()
			self.menu_height = self.skin.getSize(EGDS_MENU_HEIGHT)

			self.menu = self.guienv.addMenu()
			self.menu.addItem(_('File'), -1, True, True)
			self.menu.addItem(_('View'), -1, True, True)
			self.menu.addItem(_('Models'), -1, True, True)
			self.menu.addItem(_('Options'), -1, True, True)
			self.menu.addItem(_('Help'), -1, True, True)

			submenu = self.menu.getSubMenu(0)
			submenu.addItem(_('Load project'), GUI_ID_LOAD)
			submenu.addItem(_('Save project'), GUI_ID_SAVE)
			submenu.addSeparator()
			submenu.addItem(_('Quit'), GUI_ID_QUIT)

			submenu = self.menu.getSubMenu(1)
			submenu.addItem(_('Without camera'), GUI_ID_CAMERA_NONE)
			submenu.addItem(_('Maya Style'), GUI_ID_CAMERA_MAYA)
			submenu.addItem(_('First Person'), GUI_ID_CAMERA_FPS)
			submenu.addItem(_('Top view'), GUI_ID_CAMERA_TOP)

			submenu = self.menu.getSubMenu(2)
			submenu.addItem(_('Insert'), GUI_ID_MODEL_INSERT)
			submenu.addItem(_('Set archive'), GUI_ID_MODEL_SET_ARCHIVE)

			self.menu_options = self.menu.getSubMenu(3)
			self.menu_options.addItem(_('Start/stop log'), GUI_ID_LOG)
			self.menu_options.addItem(_('Choose graphics driver'), GUI_ID_DRIVER, True, True)
			self.menu_device_type = self.menu_options.getSubMenu(1)
			self.menu_device_types[EDT_SOFTWARE] = self.menu_device_type.addItem(_('Software'), GUI_ID_EDT_SOFTWARE, checked = (self.device_parameters.DriverType == EDT_SOFTWARE))
			self.menu_device_types[EDT_OPENGL] = self.menu_device_type.addItem(_('OpenGL'), GUI_ID_EDT_OPENGL, checked = (self.device_parameters.DriverType == EDT_OPENGL))
			self.menu_device_types[EDT_DIRECT3D9] = self.menu_device_type.addItem(_('DirectX 9'), GUI_ID_EDT_DIRECT3D9, checked = (self.device_parameters.DriverType == EDT_DIRECT3D9))
			self.menu_device_types[EDT_BURNINGSVIDEO] = self.menu_device_type.addItem(_('Burningsvideo'), GUI_ID_EDT_BURNINGSVIDEO, checked = (self.device_parameters.DriverType == EDT_BURNINGSVIDEO))
			self.menu_texture_from_file = self.menu_options.addItem(_('Textures from files'), GUI_ID_TEXTURE_FROM_FILE, checked = self.texture_from_file)

			submenu = self.menu.getSubMenu(4)
			submenu.addItem(_('About'), GUI_ID_ABOUT)

			self.i_geometry_creator = self.scene_manager.getGeometryCreator()

			texture = None
			file_name = 'media//skydome.jpg'
			if os.path.exists(file_name) and self.texture_from_file:
				texture = self.driver.getTexture(file_name)
			else:
				texture = self.texture_generator(ECF_R8G8B8, dimension2du(64, 64), 'skydome')
			sky_node = self.scene_manager.addSkyDomeSceneNode(texture)

			# bottom(low) and top(height) plane
			file_name = 'media//opengllogo.png'
			if self.device_parameters.DriverType == EDT_SOFTWARE:
				file_name = 'media//irrlichtlogoalpha.tga'
			elif self.device_parameters.DriverType == EDT_BURNINGSVIDEO:
				file_name = 'media//burninglogo.png'
			elif self.device_parameters.DriverType in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				file_name = 'media//directxlogo.png'
			self.material.Wireframe = False
			if os.path.exists(file_name) and self.texture_from_file:
				self.material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				self.material.setTexture(0, self.driver.getTexture(file_name))
			i_mesh_top = self.i_geometry_creator.createPlaneMesh(self.tile_size, self.tile_count, self.material, self.texture_repeat_count)
			self.ceiling = self.scene_manager.addOctreeSceneNode(i_mesh_top)
			self.ceiling.setPosition(vector3df(0,self.wall_height,0))
			self.ceiling.setRotation(vector3df(180,0,0))
			selector_top = self.scene_manager.createTriangleSelector(self.ceiling.getMesh(), self.ceiling)
			self.ceiling.setTriangleSelector(selector_top)
			self.ceiling.setVisible(False)

			i_mesh_bottom = self.i_geometry_creator.createPlaneMesh(self.tile_size, self.tile_count, self.material, self.texture_repeat_count)
			#~ self.floor = self.scene_manager.addOctreeSceneNode(i_mesh_bottom)
			#~ selector_bottom = self.scene_manager.createOctreeTriangleSelector(self.floor.getMesh(), self.floor)
			#~ self.floor.setTriangleSelector(selector_bottom)
			#~ self.floor.setVisible(False)

			# CGridSceneNode
			self.grid = CGridSceneNode(self.scene_manager.getRootSceneNode(), self.scene_manager, size = int(self.tile_size.X * self.tile_count.X), axislinestate = True)
			#~ selector_bottom = self.scene_manager.createTriangleSelectorFromBoundingBox(self.grid)
			selector_bottom = self.scene_manager.createOctreeTriangleSelector(i_mesh_bottom, self.grid)
			self.grid.setTriangleSelector(selector_bottom)
			self.grid.drop()
			#~ self.grid.SetMaterial(self.material)
			#~ #self.grid.SetGridColor(SColor(255,100,100,100))
			#~ #self.grid.SetAccentlineColor(SColor(255,200,200,200))
			#~ self.grid.SetSpacing(64)

			# left, right, front and back plane
			file_name = 'media//wall.jpg'
			if os.path.isfile(file_name) and self.texture_from_file:
				self.material.MaterialType = EMT_LIGHTMAP
				self.material.setTexture(0, self.driver.getTexture(file_name))
			else:
				self.material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'front', 196, (0, 255), (0, 0), (0, 100))
				self.material.setTexture(0, texture)
			p = self.tile_count_x * self.tile_size.X / 2
			selector_front = self.create_wall_plane_selector(
				vector3df(0, self.wall_height / 2, p), 
				vector3df(-90,0,0))
			if not self.texture_from_file:
				self.material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'back', 196, (0, 0), (0, 50), (0, 255))
				self.material.setTexture(0, texture)
			selector_back = self.create_wall_plane_selector(
				vector3df(0, self.wall_height / 2, -p), 
				vector3df(90,0,0))
			if not self.texture_from_file:
				self.material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'left', 196, (0, 0), (0, 0), (100, 255))
				self.material.setTexture(0, texture)
			selector_left = self.create_wall_plane_selector(
				vector3df(-p, self.wall_height / 2, 0),
				vector3df(90,90,0))
			if not self.texture_from_file:
				self.material.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
				texture = self.texture_generator(ECF_A8R8G8B8, dimension2du(4, 4), 'right', 196, (0, 0), (100, 255), (0, 0))
				self.material.setTexture(0, texture)
			selector_right = self.create_wall_plane_selector(
				vector3df(p, self.wall_height / 2, 0),
				vector3df(90,-90,0))

			self.material.BackfaceCulling = False

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
			self.camera = (self.scene_manager.addCameraSceneNodeMaya(id = GUI_ID_CAMERA_MAYA), self.scene_manager.addCameraSceneNodeFPS(keyMapArray = keyMap, keyMapSize = keyMap.length, jumpSpeed = 5, id = GUI_ID_CAMERA_FPS), self.scene_manager.addCameraSceneNode(id = GUI_ID_CAMERA_TOP))
			self.camera[0].setTarget(vector3df(0,1000,0))
			self.camera[1].setPosition(vector3df(100,60,0))
			#~ self.camera[1].setNearValue(0.1)
			self.camera[2].setPosition(vector3df(0,1000,0))
			self.camera[2].setTarget(vector3df(0,0,0))
			self.camera[2].setNearValue(0.01)
			for cam in self.camera:
				cam.setFarValue(9000)
			#~ self.set_active_camera(self.camera[2])
			#~ self.scale_camera_top()

			self.i_meta_triangle_selector = self.scene_manager.createMetaTriangleSelector()
			self.i_meta_triangle_selector.addTriangleSelector(selector_bottom)
			self.i_meta_triangle_selector.addTriangleSelector(selector_top)
			self.i_meta_triangle_selector.addTriangleSelector(selector_front)
			self.i_meta_triangle_selector.addTriangleSelector(selector_back)
			self.i_meta_triangle_selector.addTriangleSelector(selector_left)
			self.i_meta_triangle_selector.addTriangleSelector(selector_right)

			anim = self.scene_manager.createCollisionResponseAnimator(self.i_meta_triangle_selector, self.camera[1])
			self.camera[1].addAnimator(anim)
			anim.drop()

			self.cursor_control = self.device.getCursorControl()
			#~ self.cursor_control.setVisible(False)

			scolor = SColor(255,120,102,136)

			#~ self.collision_manager = self.scene_manager.getSceneCollisionManager()

			i_event_receiver = UserIEventReceiver()
			i_event_receiver.framework = self
			self.device.setEventReceiver(i_event_receiver)

			dlg = None
			a, b = 0, 0

			# for draw3DLine
			m = SMaterial()
			m.Lighting = False
			#~ self.driver.setMaterial(m)
			matrix = matrix4()
			#~ self.driver.setTransform(ETS_WORLD, matrix)
			blue_color_3dline = SColor(255,0,0,255)
			red_color_3dline = SColor(255,255,0,0)

			check_collisions = True
			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.is_key_down(KEY_ESCAPE):
						break
					elif i_event_receiver.is_key_down(KEY_F2):
						self.scene_manager.setActiveCamera()
					self.driver.beginScene(True, True, scolor)
					self.scene_manager.drawAll()
					if i_event_receiver.l_mouse_pressed:
						self.driver.setMaterial(m)
						self.driver.setTransform(ETS_WORLD, matrix)
						self.driver.draw3DLine(i_event_receiver.mouse_position_3d_start, i_event_receiver.mouse_position_3d, blue_color_3dline)
					else:
						self.driver.setMaterial(m)
						self.driver.setTransform(ETS_WORLD, matrix)
						x = i_event_receiver.mouse_position_3d_start.X
						y = 0
						z = i_event_receiver.mouse_position_3d_start.Z
						self.driver.draw3DLine(vector3df(x-20,y,z+20), vector3df(x+20,y,z-20), red_color_3dline)
						self.driver.draw3DLine(vector3df(x+20,y,z+20), vector3df(x-20,y,z-20), red_color_3dline)
					self.guienv.drawAll()
					self.driver.endScene()
					self.device.sleep(self.sleep_delay)
				else:
					self.device._yield()
			self.device.drop()
			# framework attribute must be deleted for worked __del__ method
			i_event_receiver.framework = None
		else:
			print('ERROR createDevice')

	def stop(self):
		if self.device:
			#~ self.device.drop()
			self.device.closeDevice()
			self.device = None
			if self.device_parameters.WindowSize.Width < 320:
				self.device_parameters.WindowSize.Width = 320
			if self.device_parameters.WindowSize.Height < 240:
				self.device_parameters.WindowSize.Height = 240
			self.config.set_many((('window_width', int(self.device_parameters.WindowSize.Width)), ('window_height', int(self.device_parameters.WindowSize.Height))))

def main():
	frmwrk = framework()
	frmwrk.start()

if __name__ == '__main__':
	main()

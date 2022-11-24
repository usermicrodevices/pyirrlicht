'''3d maze generator from Dolkar, thanks to him.
Irrlicht adaptation by Maxim Kolosov.
(http://www.python-forum.org/pythonforum/viewtopic.php?f=2&t=28246)'''

import os
from pyirrlicht import *
from random import randint, randrange, shuffle

try:
	from cellular import Cellular
except:
	class Cellular:
		def __init__(self, *args, **kwargs):
			pass
		def get_texture(self):
			return None

#driverType = EDT_NULL
#driverType = EDT_SOFTWARE
#driverType = EDT_BURNINGSVIDEO
#driverType = EDT_DIRECT3D8
#driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

ID_FINISH_NODE = 0


def maze2d(video_driver, width = 20, height = 20, fore = (0,255,0), back = (0,255,225), scale = 0, color_format = ECF_R8G8B8):
	'based on code from http://zenpython.blogspot.com see 2d_maze.py'
	stack   = []
	grid    = [[x%2*y%2 for x in range(width)] for y in range(height)]
	total   = ((width-1)/2)*((height-1)/2)
	cy      = randrange(1,height,2)
	cx      = randrange(1,width,2)
	visited = 1
	while visited<total:
		possible = [[y,x] for y,x in [[cy-2,cx],[cy,cx+2],[cy+2,cx],[cy,cx-2]] if y>0 and x>0 and y<height-1 and x<width-1]
		neighbor = [[y,x] for y,x in possible if grid[y-1][x]!=2 and grid[y+1][x]!=2 and grid[y][x-1]!=2 and grid[y][x+1]!=2]
		if len(neighbor) > 0:
			ny,nx   = neighbor[randrange(0,len(neighbor))]
			wy      = ny if nx!=cx else (ny-1 if ny>cy else cy-1)
			wx      = nx if ny!=cy else (nx-1 if nx>cx else cx-1)
			grid[wy][wx] = 2
			stack.append([cy,cx])
			cy = ny
			cx = nx
			visited = visited + 1
		else:
			if len(stack) > 0:
				cy, cx = stack.pop()
			else:
				cy, cx = 1, 1
	grid[0][1] = 1
	grid[height-1][width-2] = 1
	data = [back if grid[y][x] else fore for y in range(height) for x in range(width)]
	# now generate texture
	image_size = dimension2du(width, height)
	image = video_driver.createImage(color_format, image_size)
	alpha = 0
	blend = False
	if image.getColorFormat() in (ECF_A1R5G5B5, ECF_A8R8G8B8, ECF_A16B16G16R16F, ECF_A32B32G32R32F):
		alpha = alpha_value
		blend = True
	i = 0
	for row in range(image_size.Height):
		for column in range(image_size.Width):
			red, green, blue = data[i]
			image.setPixel(column, row, SColor(alpha, red, green, blue), blend)
			i = i + 1
	return video_driver.addTexture('maze2d', image)

class event_receiver(IEventReceiver):
	game = None
	stop = False
	def OnEvent(self, evt):
		if self.game.help_dialog:
			try:
				self.game.help_dialog.getID()
			except:
				self.game.help_dialog = None
		event = SEvent(evt)
		if event.EventType is EET_KEY_INPUT_EVENT:
			pressed_down = event.KeyInput.PressedDown
			if not self.game.help_dialog:
				self.check_input(event.KeyInput.Key)
		return False
	def help(self):
		if not self.game.help_dialog:
			self.game.help_dialog = self.game.gui_environment.addMessageBox(_('Help'), _('Copyright (C) Dolkar') + '\n' + _('pyIrrlicht version - Maxim Kolosov') + '\n' + _('F1 - help; ESC - exit'))
	def check_input(self, key):
		if key == KEY_F1:
			self.help()
		elif key == KEY_ESCAPE:
			self.stop = True

class MazeIsDone(Exception):
	pass

class Maze(object):

	def __init__(self, size):
		if isinstance(size, tuple):
			self.size = size
		else:
			self.size = (size, size, size)
		self.cell_count = self.size[0] * self.size[1] * self.size[2]
		self.init_maze()

		self.help_dialog = None
		self.device = None
		self.video_driver = None
		self.scene_manager = None
		self.gui_environment = None
		self.i_meta_triangle_selector = None
		self.camera_animator = None
		self.maze_walls = []

	def init_maze(self):
		self.grid = []
		self.cells = {}
		self.sets = []
		self._makeGrid(self.size)
		try:
			self._makeMaze()
		#except MazeIsDone:
		except:# for Python 3 compatibility
			del(self.cells)
			del(self.sets)

	def _makeGrid(self, size):
		'''
		Makes grid of walls, initializes cells and sets.
		Number of walls in a cube: n^2*(n-1)*3
		Number of loops: n^2*(n-1)
		'''

		grid = self.grid
		id = 0
		for x in range(size[0]):
			x_ = x + 0.5
			for y in range(size[1]):
				y_ = y + 0.5
				for z in range(size[2]):
					z_ = z + 0.5
					if x_ < size[0] - 1:
						grid.append([x_, y, z, 0])
					if y_ < size[1] - 1:
						grid.append([x, y_, z, 1])
					if z_ < size[2] - 1:
						grid.append([x, y, z_, 2])   
					self.cells[(x, y, z)] = id
					self.sets.append([(x, y, z)])
					id += 1             

	def _cellOffset(self, pos, direction, val):
		'''Gets the pos of cell on given side from wall.'''
		temp = pos[0:3]
		temp[direction] += 0.5 * val
		return tuple(temp)

	def _merge(self, set1, set2):
		'''
		Merges given sets and adjusts cells' set pointer.
		Also catches when is mazing completed by comparing set cell count with
		total cell count.
		'''

		for cell in self.sets[set2]:
			self.cells[cell] = set1

		self.sets[set1].extend(self.sets[set2])
		self.sets[set2] = None

		if len(self.sets[set1]) == self.cell_count:
			self.start_cell = self.sets[set1][0]
			self.end_cell = self.sets[set1][-1]
			#raise MazeIsDone('No need for future computations')

	def _makeMaze(self):
		'''
		Computes a maze using Kruskal's algorithm.
		Uses both a dictionary of cell:set and a list of [set] = list of cells
		which efficiently trades memory for time.
		'''

		shuffle(self.grid)
		for i in range(len(self.grid)):
			pos_set = self.cells[self._cellOffset(self.grid[i], self.grid[i][3], 1)]
			neg_set = self.cells[self._cellOffset(self.grid[i], self.grid[i][3], -1)]
			if neg_set != pos_set:
				self.grid[i] = None
				if len(self.sets[neg_set]) > len(self.sets[pos_set]):
					self._merge(neg_set, pos_set)
				else:
					self._merge(pos_set, neg_set)

	def create_level(self):
		material = SMaterial()
		material.setTexture(0, generate_texture(self.video_driver))
		material.EmissiveColor = SColor(255, 0, 100, 100)
		for pos in self.grid:
			if pos == None:
				continue
			size = [1, 1, 1]
			temp = []
			for i in range(3):
				if pos[i] % 1 == 0.5:
					size[i] = 0.1
			box_scene_node = self.scene_manager.addCubeSceneNode(1, position = vector3df(*pos[0:3]), scale = vector3df(*size))
			if not material:
				material = box_scene_node.getMaterial(0)
				material.EmissiveColor = SColor(255, 0, 0, 255)
				#material.BackfaceCulling = False
			if randint(0, 1) and self.cell.get_texture():
				material.setTexture(0, self.cell.get_texture())
			else:
				material.setTexture(0, maze2d(self.video_driver, fore = (128,0,0), back = (0,128,0)))
			box_scene_node.setMaterial(material)
			selector = self.scene_manager.createOctreeTriangleSelector(box_scene_node.getMesh(), box_scene_node)
			#self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createTriangleSelectorFromBoundingBox(box_scene_node))
			self.i_meta_triangle_selector.addTriangleSelector(selector)
			self.maze_walls.append((box_scene_node, selector))

	def recreate_level(self):
		self.camera.removeAnimator(self.camera_animator)
		for item, selector in self.maze_walls:
			self.i_meta_triangle_selector.removeTriangleSelector(selector)
			#item.removeAll()
			item.remove()
		self.maze_walls = []
		self.init_maze()
		position_start = vector3df(*self.start_cell)
		self.camera.setPosition(position_start)
		self.sphere_start.setPosition(position_start)
		position_finish = vector3df(*self.end_cell)
		self.sphere_finish.setPosition(position_finish)
		self.finish_box = aabbox3df(position_finish-0.5, position_finish+0.5)
		#self.finish_box.reset(*self.end_cell)
		self.create_level()
		self.add_animator_to_camera()

	def create_outer_walls(self):
		# OUTER WALLS AS PLANES
		x_outer_wall = self.size[0]/2-0.5
		if self.size[0]%2:
			x_outer_wall = self.size[0]/2
		y_outer_wall = self.size[1]/2-0.5
		if self.size[1]%2:
			y_outer_wall = self.size[1]/2
		z_outer_wall = self.size[2]/2-0.5
		if self.size[2]%2:
			z_outer_wall = self.size[2]/2

		i_geometry_creator = self.scene_manager.getGeometryCreator()

		# CREATE TOP AND BOTTOM WALLS

		material = SMaterial()
		#material.AmbientColor = SColor(255, 255, 0, 0)
		#material.DiffuseColor = SColor(255, 255, 0, 0)
		material.EmissiveColor = SColor(255, 255, 0, 0)
		#material.SpecularColor = SColor(255, 255, 0, 0)
		#material.BackfaceCulling = False

		material.setTexture(0, maze2d(self.video_driver, 100, 100, (255,0,0), (0,0,225)))
		i_plane_mesh_top = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[2]), dimension2du(1, 1), material, dimension2df(1, 1))
		i_plane_mesh_scene_node_top = self.scene_manager.addOctreeSceneNode(i_plane_mesh_top)
		i_plane_mesh_scene_node_top.setPosition(vector3df(x_outer_wall, self.size[1] - 0.5, z_outer_wall))
		i_plane_mesh_scene_node_top.setRotation(vector3df(180,0,0))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(i_plane_mesh_scene_node_top.getMesh(), i_plane_mesh_scene_node_top))
		#i_plane_mesh_scene_node_top.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_top.isDebugDataVisible()^EDS_BBOX_BUFFERS))
		i_plane_mesh_top.drop()

		material.EmissiveColor = SColor(255, 0, 0, 255)
		material.setTexture(0, maze2d(self.video_driver, 100, 100))
		i_plane_mesh_bottom = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[2]), dimension2du(1, 1), material, dimension2df(1, 1))
		i_plane_mesh_scene_node_bottom = self.scene_manager.addOctreeSceneNode(i_plane_mesh_bottom)
		i_plane_mesh_scene_node_bottom.setPosition(vector3df(x_outer_wall, -0.5, z_outer_wall))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(i_plane_mesh_scene_node_bottom.getMesh(), i_plane_mesh_scene_node_bottom))
		#i_plane_mesh_scene_node_bottom.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_bottom.isDebugDataVisible()^EDS_BBOX_BUFFERS))
		i_plane_mesh_bottom.drop()

		# CREATE LEFT AND RIGHT AND FORWARD AND BACKWARD WALLS

		material.EmissiveColor = SColor(255, 0, 255, 255)
		material.setTexture(0, maze2d(self.video_driver, 100, 100, (0,255,0), (225,0,0)))
		mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
		node = self.scene_manager.addOctreeSceneNode(mesh)
		node.setRotation(vector3df(90,0,0))
		node.setPosition(vector3df(x_outer_wall, y_outer_wall, -0.5))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
		mesh.drop()

		material.EmissiveColor = SColor(255, 255, 255, 255)
		material.setTexture(0, maze2d(self.video_driver, 100, 100, (255,0,0), (255,255,255)))
		mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
		node = self.scene_manager.addOctreeSceneNode(mesh)
		node.setRotation(vector3df(90,180,0))
		node.setPosition(vector3df(x_outer_wall, y_outer_wall, self.size[2]-0.5))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
		mesh.drop()

		material.EmissiveColor = SColor(255, 255, 0, 255)
		material.setTexture(0, maze2d(self.video_driver, 100, 100, (0,0,255), (225,0,0)))
		mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[2], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
		node = self.scene_manager.addOctreeSceneNode(mesh)
		node.setRotation(vector3df(90,90,0))
		node.setPosition(vector3df(-0.5, y_outer_wall, z_outer_wall))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
		mesh.drop()

		material.EmissiveColor = SColor(255, 200, 200, 200)
		material.setTexture(0, maze2d(self.video_driver, 100, 100, (0,255,255), (255,255,0)))
		mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[2], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
		node = self.scene_manager.addOctreeSceneNode(mesh)
		node.setRotation(vector3df(90,-90,0))
		node.setPosition(vector3df(self.size[0]-0.5, y_outer_wall, z_outer_wall))
		self.i_meta_triangle_selector.addTriangleSelector(self.scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
		mesh.drop()

	def add_animator_to_camera(self):
		self.camera_animator = self.scene_manager.createCollisionResponseAnimator(self.i_meta_triangle_selector, self.camera, vector3df(0.1, 0.2, 0.1), vector3df(0.0, -1.0, 0.0))
		self.camera.addAnimator(self.camera_animator)
		#self.camera_animator.drop()

	def show(self):
		"""Shows maze using pyirrlicht. Outer walls as optional"""
		#self.device = createDevice(driverType, dimension2du(800, 600))
		p = SIrrlichtCreationParameters()
		p.DriverType = driverType
		#p.Fullscreen = True
		p.WindowSize = dimension2du(800, 600)
		p.AntiAlias = True
		p.WithAlphaChannel = True
		self.device = createDeviceEx(p)
		if self.device:
			self.device.setWindowCaption('Irrlicht Engine - 3D Maze generator, written Dolkar from http://www.python-forum.org')
			self.video_driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.gui_environment = self.device.getGUIEnvironment()

			#gui_font = CGUITTFont(self.gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', 20)
			#if gui_font:
				#self.gui_environment.getSkin().setFont(gui_font)
				#gui_font.drop()

			# meta triangle selector
			self.i_meta_triangle_selector = self.scene_manager.createMetaTriangleSelector()

			# cellular texture generator
			self.cell = Cellular(self.video_driver, 128, 128, 128)

			#sky_node = self.scene_manager.addSkyDomeSceneNode(generate_texture(self.video_driver))
			m2d = maze2d(self.video_driver, 50, 50, (255,255,255), (100,100,100))
			sky_node = self.scene_manager.addSkyBoxSceneNode(m2d, m2d, m2d, m2d, m2d, m2d)

			# create maze volume
			self.create_level()
			self.create_outer_walls()

			# START SPHERE
			self.sphere_start = self.scene_manager.addSphereSceneNode(0.25, position = vector3df(*self.start_cell))
			material1 = self.sphere_start.getMaterial(0)
			material1.EmissiveColor = SColor(255, 0, 255, 0)

			# FINISH SPHERE
			finish_position = vector3df(*self.end_cell)
			self.sphere_finish = self.scene_manager.addSphereSceneNode(0.3, id = ID_FINISH_NODE, position = finish_position)
			material2 = self.sphere_finish.getMaterial(0)
			material2.EmissiveColor = SColor(255, 255, 0, 0)
			self.finish_box = aabbox3df(finish_position-0.5, finish_position+0.5)

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

			self.camera = self.scene_manager.addCameraSceneNodeFPS(moveSpeed = 0.005, jumpSpeed = 0.5, keyMapArray = keyMap, keyMapSize = keyMap.length)
			self.camera.setPosition(vector3df(*self.start_cell))
			self.camera.setNearValue(0.001)

			self.add_animator_to_camera()

			light_radius = 10.0
			if driverType in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				light_radius = 1.5
			elif driverType == EDT_OPENGL:
				light_radius = 0.1
			light = self.scene_manager.addLightSceneNode(self.camera, radius = light_radius)

			#collision_manager = self.scene_manager.getSceneCollisionManager()
			self.win_dialog = None

			scolor = SColor(255, 100, 100, 140)
			i_event_receiver = event_receiver()
			i_event_receiver.game = self
			self.device.setEventReceiver(i_event_receiver)
			while self.device.run():
				if self.device.isWindowActive():
					if i_event_receiver.stop:
						break
					if self.video_driver.beginScene(True, True, scolor):
						try:
							self.win_dialog.getID()
						except:
							self.win_dialog = None
							self.camera.setInputReceiverEnabled(True)
						self.scene_manager.drawAll()
						if self.finish_box.isPointInside(self.camera.getPosition()) and not self.win_dialog:
							self.camera.setInputReceiverEnabled(False)
							self.win_dialog = self.gui_environment.addMessageBox('Warning', 'You is Winner!!!')
							self.finish_box.reset(0.1, 0.1, 0.1)
							self.recreate_level()
						#collision_node = collision_manager.getSceneNodeFromCameraBB(self.camera)
						#if collision_node:
							#if collision_node.getID() == ID_FINISH_NODE:
								#self.gui_environment.addMessageBox('Warning', 'You is Winner!!!')
						self.gui_environment.drawAll()
						self.video_driver.endScene()
					self.device.sleep(1)
				else:
					self.device.yield_self()
			self.device.drop()
			self.device.closeDevice()
		else:
			print('ERROR createDevice')


def main():
	maze = Maze((4, 2, 5))
	maze.show()


if __name__ == "__main__":
	main()

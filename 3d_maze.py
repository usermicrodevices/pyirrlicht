'''3d maze generator from Dolkar, thanks him.
Irrlicht adaptation by Maxim Kolosov.
(http://www.python-forum.org/pythonforum/viewtopic.php?f=2&t=28246)'''

import os
from pyirrlicht import *
from random import randrange, shuffle

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

ID_FINISH_NODE = 0

def fractal_texture(video_driver, width = 20, height = 20, max_iteration = 70, alpha = 128):
	'based on code Vadim Kataev (vkataev at gmail.com) see 2DFractal.py'
	def iteration_color(c):
		i = 0
		z = 0
		mag = 0.0
		while mag < 4.0 and i < max_iteration:
			z = z**2 + c
			mag = z.imag * z.imag + z.real * z.real
			i = i + 1
		return i
	def set_color(i):
		if i == max_iteration:
			return SColor(alpha, 0, 0, 0)
		else:
			c = int(i * 15)
			r = 255
			g = 255 - c
			b = 255
			if r < 0:
				r = 0
				g = 510 - c
				if g < 0:
					g = 0
					b = 765 - c
					if b < 0:
						r = g = b = 0
			return SColor(alpha, r, g, b)
	scale = 3.0/(height*500.0)
	j = 0 + 1j
	blend = True
	image_size = dimension2du(width, height)
	image = video_driver.createImage(ECF_R8G8B8, image_size)
	for row in range(height):
		for column in range(width):
			x = (column - width/2) * scale - 0.001
			y = (row - height/2) * scale - 0.75
			c = x + y * j
			image.setPixel(row, column, set_color(iteration_color(c)), blend)
	texture = video_driver.addTexture('fractal', image)
	image.drop()
	return texture

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

class MazeIsDone(Exception):
	pass

class Maze(object):

	def __init__(self, size):
		if isinstance(size, tuple):
			self.size = size
		else:
			self.size = (size, size, size)
		self.cell_count = self.size[0] * self.size[1] * self.size[2]
		self.grid = []
		self.cells = {}
		self.sets = []
		self._makeGrid(self.size)
		try:
			self._makeMaze()
		#~ except MazeIsDone:
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
		for x in xrange(size[0]):
			x_ = x + 0.5
			for y in xrange(size[1]):
				y_ = y + 0.5
				for z in xrange(size[2]):
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
			#~ raise MazeIsDone('No need for future computations')

	def _makeMaze(self):
		'''
		Computes a maze using Kruskal's algorithm.
		Uses both a dictionary of cell:set and a list of [set] = list of cells
		which efficiently trades memory for time.
		'''

		shuffle(self.grid)
		for i in xrange(len(self.grid)):
			pos_set = self.cells[self._cellOffset(self.grid[i], self.grid[i][3], 1)]
			neg_set = self.cells[self._cellOffset(self.grid[i], self.grid[i][3], -1)]
			if neg_set != pos_set:
				self.grid[i] = None
				if len(self.sets[neg_set]) > len(self.sets[pos_set]):
					self._merge(neg_set, pos_set)
				else:
					self._merge(pos_set, neg_set)

	def show(self):
		"""Shows maze using pyirrlicht. Outer walls as optional"""
		device = createDevice(driverType, dimension2du(640, 480))

		if device:
			device.setWindowCaption('Irrlicht Engine - 3D Maze generator, written Dolkar from http://www.python-forum.org')
			video_driver = device.getVideoDriver()
			scene_manager = device.getSceneManager()
			gui_environment = device.getGUIEnvironment()

			gui_font = CGUITTFont(gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', 20)
			if gui_font:
				gui_environment.getSkin().setFont(gui_font)
				gui_font.drop()

			#~ sky_node = scene_manager.addSkyDomeSceneNode(generate_texture(video_driver))
			m2d = maze2d(video_driver, 50, 50, (255,255,255), (100,100,100))
			sky_node = scene_manager.addSkyBoxSceneNode(m2d, m2d, m2d, m2d, m2d, m2d)
			#~ fractal = fractal_texture(video_driver, 400, 400)
			#~ sky_node = scene_manager.addSkyBoxSceneNode(fractal, fractal, fractal, fractal, fractal, fractal)

			material = SMaterial()
			material.setTexture(0, generate_texture(video_driver))

			i_meta_triangle_selector = scene_manager.createMetaTriangleSelector()

			material.EmissiveColor = SColor(255, 0, 100, 100)

			for pos in self.grid:
				if pos == None:
					continue
				size = [1, 1, 1]
				temp = []
				for i in range(3):
					if pos[i] % 1 == 0.5:
						size[i] = 0.1
				box_scene_node = scene_manager.addCubeSceneNode(1, position = vector3df(*pos[0:3]), scale = vector3df(*size))
				if not material:
					material = box_scene_node.getMaterial(0)
					material.EmissiveColor = SColor(255, 0, 0, 255)
					#~ material.BackfaceCulling = False
				material.setTexture(0, maze2d(video_driver, fore = (128,0,0), back = (0,128,0)))
				box_scene_node.setMaterial(material)
				#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(box_scene_node))
				i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(box_scene_node.getMesh(), box_scene_node))

			sphere_scene_node1 = scene_manager.addSphereSceneNode(0.25, position = vector3df(*self.start_cell))
			material1 = sphere_scene_node1.getMaterial(0)
			material1.EmissiveColor = SColor(255, 0, 255, 0)
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(sphere_scene_node1.getMesh(), sphere_scene_node1))

			finish_position = vector3df(*self.end_cell)
			sphere_scene_node2 = scene_manager.addSphereSceneNode(0.3, id = ID_FINISH_NODE, position = finish_position)
			material2 = sphere_scene_node2.getMaterial(0)
			material2.EmissiveColor = SColor(255, 255, 0, 0)
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(sphere_scene_node2.getMesh(), sphere_scene_node2))
			#~ finish_box = sphere_scene_node2.getBoundingBox()
			finish_box = aabbox3df(finish_position-0.5, finish_position+0.5)
			#~ sphere_scene_node2.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(sphere_scene_node2.isDebugDataVisible()^EDS_BBOX_BUFFERS))

			# OUTER WALLS AS PLANES
			x_outer_wall = self.size[0]/2
			z_outer_wall = self.size[2]/2

			i_geometry_creator = scene_manager.getGeometryCreator()

			# CREATE TOP AND BOTTOM WALLS

			#~ material.AmbientColor = SColor(255, 255, 0, 0)
			#~ material.DiffuseColor = SColor(255, 255, 0, 0)
			material.EmissiveColor = SColor(255, 255, 0, 0)
			#~ material.SpecularColor = SColor(255, 255, 0, 0)
			#~ material.BackfaceCulling = False

			material.setTexture(0, maze2d(video_driver, 100, 100, (255,0,0), (0,0,225)))
			i_plane_mesh_top = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[2]), dimension2du(1, 1), material, dimension2df(1, 1))
			i_plane_mesh_scene_node_top = scene_manager.addOctreeSceneNode(i_plane_mesh_top)
			i_plane_mesh_scene_node_top.setPosition(vector3df(x_outer_wall, self.size[1] - 0.5, z_outer_wall))
			i_plane_mesh_scene_node_top.setRotation(vector3df(180,0,0))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(i_plane_mesh_scene_node_top.getMesh(), i_plane_mesh_scene_node_top))
			#~ i_plane_mesh_scene_node_top.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_top.isDebugDataVisible()^EDS_BBOX_BUFFERS))
			i_plane_mesh_top.drop()

			material.EmissiveColor = SColor(255, 0, 0, 255)
			material.setTexture(0, maze2d(video_driver, 100, 100))
			i_plane_mesh_bottom = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[2]), dimension2du(1, 1), material, dimension2df(1, 1))
			i_plane_mesh_scene_node_bottom = scene_manager.addOctreeSceneNode(i_plane_mesh_bottom)
			i_plane_mesh_scene_node_bottom.setPosition(vector3df(x_outer_wall, -0.5, z_outer_wall))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(i_plane_mesh_scene_node_bottom.getMesh(), i_plane_mesh_scene_node_bottom))
			#~ i_plane_mesh_scene_node_bottom.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_bottom.isDebugDataVisible()^EDS_BBOX_BUFFERS))
			i_plane_mesh_bottom.drop()

			# CREATE LEFT AND RIGHT AND FORWARD AND BACKWARD WALLS

			material.EmissiveColor = SColor(255, 0, 255, 255)
			material.setTexture(0, maze2d(video_driver, 100, 100, (0,255,0), (225,0,0)))
			mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
			node = scene_manager.addOctreeSceneNode(mesh)
			node.setRotation(vector3df(90,0,0))
			node.setPosition(vector3df(x_outer_wall, 0.5, -0.5))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
			mesh.drop()

			material.EmissiveColor = SColor(255, 255, 255, 255)
			material.setTexture(0, maze2d(video_driver, 100, 100, (255,0,0), (255,255,255)))
			mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[0], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
			node = scene_manager.addOctreeSceneNode(mesh)
			node.setRotation(vector3df(90,180,0))
			node.setPosition(vector3df(x_outer_wall, 0.5, self.size[2]-0.5))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
			mesh.drop()

			material.EmissiveColor = SColor(255, 255, 0, 255)
			material.setTexture(0, maze2d(video_driver, 100, 100, (0,0,255), (225,0,0)))
			mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[2], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
			node = scene_manager.addOctreeSceneNode(mesh)
			node.setRotation(vector3df(90,90,0))
			node.setPosition(vector3df(-0.5, 0.5, z_outer_wall))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
			mesh.drop()

			material.EmissiveColor = SColor(255, 200, 200, 200)
			material.setTexture(0, maze2d(video_driver, 100, 100, (0,255,255), (255,255,0)))
			mesh = i_geometry_creator.createPlaneMesh(dimension2df(self.size[2], self.size[1]), dimension2du(1, 1), material, dimension2df(1, 1))
			node = scene_manager.addOctreeSceneNode(mesh)
			node.setRotation(vector3df(90,-90,0))
			node.setPosition(vector3df(self.size[0]-0.5, 0.5, z_outer_wall))
			i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(node.getMesh(), node))
			mesh.drop()

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

			camera = scene_manager.addCameraSceneNodeFPS(moveSpeed = 0.005, jumpSpeed = 0.5, keyMapArray = keyMap, keyMapSize = keyMap.length)
			camera.setPosition(vector3df(*self.start_cell))
			camera.setNearValue(0.001)

			anim = scene_manager.createCollisionResponseAnimator(i_meta_triangle_selector, camera, vector3df(0.1, 0.2, 0.1), vector3df(0.0, -1.0, 0.0))
			camera.addAnimator(anim)
			anim.drop()

			light_radius = 10.0
			if driverType in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				light_radius = 1.5
			elif driverType == EDT_OPENGL:
				light_radius = 0.1
			light = scene_manager.addLightSceneNode(camera, radius = light_radius)

			#~ collision_manager = scene_manager.getSceneCollisionManager()

			scolor = SColor(255, 100, 100, 140)
			while device.run():
				if device.isWindowActive():
					if video_driver.beginScene(True, True, scolor):
						scene_manager.drawAll()
						if finish_box.isPointInside(camera.getPosition()):
							gui_environment.addMessageBox('Warning', 'You is Winner!!!')
							finish_box.reset(0.1, 0.1, 0.1)
						#~ collision_node = collision_manager.getSceneNodeFromCameraBB(camera)
						#~ if collision_node:
							#~ if collision_node.getID() == ID_FINISH_NODE:
								#~ gui_environment.addMessageBox('Warning', 'You is Winner!!!')
						gui_environment.drawAll()
						video_driver.endScene()
					device.sleep(10)
				else:
					device.yield_self()
			device.drop()
			device.closeDevice()
		else:
			print('ERROR createDevice')


def main():
	maze = Maze((3, 2, 5))
	maze.show()


if __name__ == "__main__":
	main()

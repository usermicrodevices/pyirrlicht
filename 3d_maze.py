'thanks Dolkar (http://www.python-forum.org/pythonforum/viewtopic.php?f=2&t=28246)'

from pyirrlicht import *
from random import shuffle

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

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
		"""Shows maze using pyirrlicht. No outer walls"""
		device = createDevice(driverType, dimension2du(640, 480))

		if device:
			video_driver = device.getVideoDriver()
			scene_manager = device.getSceneManager()

			sky_node = scene_manager.addSkyDomeSceneNode(generate_texture(video_driver))

			material = SMaterial()
			material.setTexture(0, generate_texture(video_driver))

			i_meta_triangle_selector = scene_manager.createMetaTriangleSelector()


			# CREATE TOP AND BOTTOM PLANES

			i_geometry_creator = scene_manager.getGeometryCreator()

			#~ material.AmbientColor = SColor(255, 0, 255, 100)
			#~ material.DiffuseColor = SColor(255, 0, 255, 100)
			#~ material.EmissiveColor = SColor(255, 0, 255, 100)
			#~ material.SpecularColor = SColor(255, 0, 255, 100)
			#~ material.BackfaceCulling = False

			i_plane_mesh_top = i_geometry_creator.createPlaneMesh(dimension2df(50, 50), dimension2du(1, 1), material, dimension2df(1, 1))
			i_plane_mesh_scene_node_top = scene_manager.addOctreeSceneNode(i_plane_mesh_top)
			#~ i_plane_mesh_top.drop()
			i_plane_mesh_scene_node_top.setPosition(vector3df(10,3,5))
			#~ i_plane_mesh_scene_node_top.setRotation(vector3df(180,0,0))
			selector_top = scene_manager.createOctreeTriangleSelector(i_plane_mesh_top)
			#~ i_plane_mesh_scene_node_top.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_top.isDebugDataVisible()^EDS_BBOX_BUFFERS))

			material.EmissiveColor = SColor(255, 0, 0, 255)

			material.setTexture(0, generate_texture(video_driver, image_size = dimension2du(128, 128)))
			i_plane_mesh_bottom = i_geometry_creator.createPlaneMesh(dimension2df(50, 50), dimension2du(10, 10), material, dimension2df(10, 10))
			i_plane_mesh_scene_node_bottom = scene_manager.addOctreeSceneNode(i_plane_mesh_bottom)
			i_plane_mesh_scene_node_bottom.setPosition(vector3df(10,-1,5))
			selector_bottom = scene_manager.createOctreeTriangleSelector(i_plane_mesh_bottom)
			#~ i_plane_mesh_bottom.drop()
			#~ i_plane_mesh_scene_node_bottom.setDebugDataVisible(E_DEBUG_SCENE_TYPE+(i_plane_mesh_scene_node_bottom.isDebugDataVisible()^EDS_BBOX_BUFFERS))

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
				material.setTexture(0, generate_texture(video_driver, image_size = dimension2du(8, 8)))
				box_scene_node.setMaterial(material)
				#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(box_scene_node))
				i_meta_triangle_selector.addTriangleSelector(scene_manager.createOctreeTriangleSelector(box_scene_node.getMesh(), box_scene_node))

			sphere_scene_node1 = scene_manager.addSphereSceneNode(0.25, position = vector3df(*self.start_cell))
			material1 = sphere_scene_node1.getMaterial(0)
			material1.EmissiveColor = SColor(255, 0, 255, 0)

			sphere_selector1 = scene_manager.createOctreeTriangleSelector(sphere_scene_node1.getMesh())
			sphere_scene_node1.setTriangleSelector(sphere_selector1)

			sphere_scene_node2 = scene_manager.addSphereSceneNode(0.25, position = vector3df(*self.end_cell))
			material2 = sphere_scene_node2.getMaterial(0)
			material2.EmissiveColor = SColor(255, 255, 0, 0)

			sphere_selector2 = scene_manager.createOctreeTriangleSelector(sphere_scene_node2.getMesh())
			sphere_scene_node2.setTriangleSelector(sphere_selector2)

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
			#~ camera.setPosition(vector3df(self.size[0] / 2, self.size[1] / 2, self.size[1] / 2))
			camera.setPosition(vector3df(-10, 2, -10))
			camera.setNearValue(0.001)

			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(i_plane_mesh_scene_node_top))
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(i_plane_mesh_scene_node_bottom))
			i_meta_triangle_selector.addTriangleSelector(selector_top)
			i_meta_triangle_selector.addTriangleSelector(selector_bottom)
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(box_scene_node))
			i_meta_triangle_selector.addTriangleSelector(sphere_selector1)
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(sphere_scene_node1))
			i_meta_triangle_selector.addTriangleSelector(sphere_selector2)
			#~ i_meta_triangle_selector.addTriangleSelector(scene_manager.createTriangleSelectorFromBoundingBox(sphere_scene_node2))

			anim = scene_manager.createCollisionResponseAnimator(i_meta_triangle_selector, camera, vector3df(0.1, 0.2, 0.1), vector3df(0.0, -1.0, 0.0))
			camera.addAnimator(anim)
			anim.drop()

			light_radius = 10.0
			if driverType in (EDT_DIRECT3D8, EDT_DIRECT3D9):
				light_radius = 1.5
			elif driverType == EDT_OPENGL:
				light_radius = 0.1
			light = scene_manager.addLightSceneNode(camera, radius = light_radius)

			device.setWindowCaption('Irrlicht Engine - 3D Maze generator, written Dolkar from http://www.python-forum.org')
			scolor = SColor(255, 100, 100, 140)
			while device.run():
				if device.isWindowActive():
					if video_driver.beginScene(True, True, scolor):
						scene_manager.drawAll()
						video_driver.endScene()
					device.sleep(10)
				else:
					device.yield_self()
			device.drop()
			device.closeDevice()
		else:
			print('ERROR createDevice')


def main():
	maze = Maze((20, 3, 10))
	maze.show()


if __name__ == "__main__":
	main()

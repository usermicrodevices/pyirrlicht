'procedural cellular texture generator'

import os, math, random
from pyirrlicht import *

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

ID_BUTTON_REGENERATE = 1000
ID_BUTTON_SAVE = 1001

class Cellular:
	def __init__(self, video_driver, width = 64, height = 64, alpha = 255):
		self.video_driver = video_driver
		self.width = width
		self.height = height
		self.alpha = alpha
		# create Irrlicht image
		self.blend = True
		image_format = ECF_R8G8B8
		if self.alpha < 255:
			image_format = ECF_A8R8G8B8
			self.blend = False
		self.image = video_driver.createImage(image_format, dimension2du(self.width, self.height))
		self.texture = None
		self.scolor = SColor(self.alpha, 0, 0, 0)
		self.generate()

	def generate(self, cellSize = 4, density = 8.0, maxDist = 0.11, mFact = 1.0, lPower = 1.0, s = 0.0, rand_range_count = 10):
		'original version based on PIL, author Alex V. Boreskoff <steps3d@narod.ru> from http://steps3d.narod.ru/tutorials/cellular-textures-tutorial.html'
		# compute probabilities for verious 
		# numbers of points
		k1 = 1.0 / float(cellSize)
		k2 = 1.0 / float(cellSize)
		pointProbs = []
		for m in range(rand_range_count):
			p = lPower * math.exp(-density) / mFact
			s = s + p
			mFact = mFact * (m + 1)
			lPower = lPower * density
			pointProbs.append(s)
		def	numPointsForCell():
			r = random.random();
			for i in range(rand_range_count):
				if r < pointProbs[i]:
					return i
			return i
		def distance(p1, p2): # L2 distance function
			dx = abs(p1[0] - p2[0])
			dy = abs(p1[1] - p2[1])
			if dx > 0.5:
				dx = 1 - dx
			if dy > 0.5:
				dy = 1 - dy
			d = math.sqrt(dx * dx + dy * dy) / maxDist
			if d > 1:
				d = 1
			return d
		#~ points = []
		# generate random points
		cells = []
		for i1 in range(cellSize):
			cells.append([])
			for i2 in range(cellSize):
				cells[i1].append([])
				x1 = i1 * k1
				y1 = i2 * k2
				numPoints = numPointsForCell()
				for i3 in range(numPoints):
					x = x1 + k1 * random.random()
					y = y1 + k2 * random.random()
					#~ points.append((x, y))
					cells[i1][i2].append((x, y))
		# create textures F1, F2, F3, F4
		for x in range(self.width):
			for y in range(self.height):
				d  = []
				pt = (float(x) / float(self.width), float(y) / float(self.height))
				# cell of this point
				i1 = (x * cellSize) / self.width
				j1 = (y * cellSize) / self.height
				cellList = [(i1, j1)] # create candidate list of cells
				for i in range(-1, 2): # add every neighbouring cell
					for j in range(-1, 2):
						i2 = i1 + i
						j2 = j1 + j
						if i2 < 0:
							i2 = cellSize + i2
						if i2 >= cellSize:
							i2 = i2 - cellSize
						if j2 < 0:
							j2 = cellSize + j2
						if j2 >= cellSize:
							j2 = j2 - cellSize
						cellList.append((i2, j2))
				for (i,j) in cellList:
					for p in cells[i][j]:
						d.append(distance(p, pt))
				d.sort()
				# now take four closest distances and map to colors, excluding duplicates
				fs = []
				j = 0
				for i in range(4):
					if j >= len(d):
						j = len(d) - 1
					v = d[j]
					j = j + 1
					fs.append(v)
					while j < len(d) and d[j] == v:
						j = j + 1
				self.scolor.r = int(255 * fs [0] + 0.5)
				self.scolor.g = int(255 * fs [1] + 0.5)
				self.scolor.b = int(255 * fs [2] + 0.5)
				self.image.setPixel(x, y, self.scolor, self.blend)

	def get_texture(self, name = 'cellular_texture'):
		if not self.texture:
			self.texture = self.video_driver.addTexture(name, self.image)
		return self.texture

	def get_new_texture(self, cellSize = 4, density = 8.0, maxDist = 0.11, mFact = 1.0, lPower = 1.0, s = 0.0, rand_range_count = 10, name = 'cellular_texture'):
		self.generate(cellSize, density, maxDist, mFact, lPower, s, rand_range_count)
		if self.texture:
			self.video_driver.removeTexture(self.texture)
		self.texture = self.video_driver.addTexture(name, self.image)
		return self.texture

	def __del__(self):
		self.image.drop()
		if self.texture:
			self.video_driver.removeTexture(self.texture)

class UserIEventReceiver(IEventReceiver):
	app = None
	name_counter = 0
	def OnEvent(self, evt):
		event = SEvent(evt)
		if event.EventType is EET_GUI_EVENT:
			gui_event_type = event.GUIEvent.EventType
			if gui_event_type == EGET_BUTTON_CLICKED:
				gui_id = event.GUIEvent.Caller.getID()
				if gui_id == ID_BUTTON_REGENERATE:
					if self.app.texture:
						self.app.video_driver.removeTexture(self.app.texture)
					self.app.texture = self.app.cell.get_new_texture()
				else:
					file_name = 'cellular_%02d.png' % name_counter
					self.app.video_driver.writeImageToFile(self.app.cell.image, file_name)
					self.app.gui_environment.addMessageBox('Warning', 'Cellular texture is saved to file %s' % file_name)
					name_counter += 1
		return False

class application:
	def __init__(self, driver_type = driverType, width = 320, height = 240):
		self.device = createDevice(driver_type, dimension2du(width, height))
		if self.device:
			self.device.setWindowCaption('Please wait one moment...')
			self.video_driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.gui_environment = self.device.getGUIEnvironment()

			font_height = 20
			gui_font = CGUITTFont(self.gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', font_height)
			if gui_font:
				self.gui_environment.getSkin().setFont(gui_font)
				gui_font.drop()

			self.cell = Cellular(self.video_driver, 128, 128)
			self.anim_cell = Cellular(self.video_driver, 16, 16)

			self.device.setWindowCaption('Irrlicht Engine - Cellular texture generator')
			self.gui_environment.addMessageBox('Warning', 'You is have\nrandom generated\ncellular texture.')
			self.gui_environment.addButton(recti(0,0,100,font_height), IGUIElement(), ID_BUTTON_REGENERATE, 'regenerate', 'random generate cellular texture')
			self.gui_environment.addButton(recti(110,0,200,font_height), IGUIElement(), ID_BUTTON_SAVE, 'save', 'save cellular texture')
			event_receiver = UserIEventReceiver()
			event_receiver.app = self
			self.device.setEventReceiver(event_receiver)
		else:
			print('ERROR createDevice')

	def run(self):
		self.texture = self.cell.get_texture()
		if self.texture:
			texture_size = self.texture.getOriginalSize()
		self.anim_texture = self.anim_cell.get_texture()
		if self.anim_texture:
			anim_texture_size = self.anim_texture.getOriginalSize()
		scolor = SColor(255, 100, 100, 140)
		while self.device.run():
			if self.device.isWindowActive():
				if self.video_driver.beginScene(True, True, scolor):
					screen_size = self.video_driver.getScreenSize()
					self.video_driver.draw2DImage(self.texture, position2di(int((screen_size.X-texture_size.X)/2),int((screen_size.Y-texture_size.Y)/2)), recti(0,0,int(texture_size.X),int(texture_size.Y)), 0, scolor, True)
					if int(self.device.getTimer().getTime()/500) % 2:
						self.anim_texture = self.anim_cell.get_new_texture()
					self.video_driver.draw2DImage(self.anim_texture, position2di(250, 10), recti(0, 0, int(anim_texture_size.X), int(anim_texture_size.Y)), 0, scolor, True)
					self.scene_manager.drawAll()
					self.gui_environment.drawAll()
					self.video_driver.endScene()
				self.device.sleep(50)
			else:
				self.device.yield_self()
		self.device.drop()
		self.device.closeDevice()


if __name__ == "__main__":
	app = application()
	if app.device:
		app.run()

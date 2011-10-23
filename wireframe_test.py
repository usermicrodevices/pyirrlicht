"""
 Wireframe 3D cube simulation.
 Developed by Leonel Machava <leonelmachava@gmail.com>
 http://codeNtronix.com

 Irrlicht adaptation Maxim Kolosov
 http://pir.sourceforge.net
"""

import wireframe_core
from pyirrlicht import *

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

width, height = 300, 300
window_size = dimension2du(width, height)
background = SColor(255, 10, 10, 50)

class ProjectionViewer:
	def __init__(self, width, height):
		self.models = {}
		self.width = width
		self.height = height
		self.displayNodes = True
		self.displayEdges = True
		self.nodeColour = SColor(255,255,255,255)
		self.edgeColour = SColor(255,200,200,200)
		self.nodeRadius = 4

	def addModel(self, name, wireframe):
		self.models[name] = wireframe

	def display(self, video_driver):
		for model in self.models.values():
			if self.displayEdges:
				for edge in model.edges:
					video_driver.draw2DLine(position2di(int(edge.start.x), int(edge.start.y)), position2di(int(edge.stop.x), int(edge.stop.y)), self.edgeColour)

			if self.displayNodes:
				for node in model.nodes:
					video_driver.draw2DPolygon(position2di(int(node.x), int(node.y)), self.nodeRadius, self.nodeColour, 20)

def main():
	device = createDevice(driverType, window_size, 16, False, False, False, 0)
	if device:
		device.setWindowCaption('Wireframe Display')
		device.setResizable(True)
		video_driver = device.getVideoDriver()
		video_driver.SetIcon(IDI_EXCLAMATION)
		#~ scene_manager = device.getSceneManager()

		cube = wireframe_core.Wireframe()
		cube.addNodes([(x,y,z) for x in (50,250) for y in (50,250) for z in (50,250)])
		cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])

		pv = ProjectionViewer(width, height)
		pv.addModel('cube', cube)

		while device.run():
			if device.isWindowActive():
				if video_driver.beginScene(True, True, background):
					pv.display(video_driver)  
					#~ scene_manager.drawAll()
					video_driver.endScene()
				device.sleep(50)
			else:
				device._yield()
		device.drop()


if __name__ == "__main__":
	main()

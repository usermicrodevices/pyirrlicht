"""
 Wireframe 3D cube simulation.
 Developed by Leonel Machava <leonelmachava@gmail.com>
 http://codeNtronix.com

 Irrlicht adaptation Maxim Kolosov
 http://pir.sourceforge.net
"""

import sys, math
from pyirrlicht import *

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

class Point3D:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x, self.y, self.z = float(x), float(y), float(z)

	def rotateX(self, angle):
		""" Rotates the point around the X axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		y = self.y * cosa - self.z * sina
		z = self.y * sina + self.z * cosa
		return Point3D(self.x, y, z)

	def rotateY(self, angle):
		""" Rotates the point around the Y axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		z = self.z * cosa - self.x * sina
		x = self.z * sina + self.x * cosa
		return Point3D(x, self.y, z)

	def rotateZ(self, angle):
		""" Rotates the point around the Z axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		x = self.x * cosa - self.y * sina
		y = self.x * sina + self.y * cosa
		return Point3D(x, y, self.z)

	def project(self, win_width, win_height, fov, viewer_distance):
		""" Transforms this 3D point to 2D using a perspective projection. """
		factor = fov / (viewer_distance + self.z)
		x = self.x * factor + win_width / 2
		y = -self.y * factor + win_height / 2
		return Point3D(x, y, 1)

class Simulation:
	def __init__(self, win_width = 640, win_height = 480):
		window_size = dimension2du(win_width, win_height)
		self.device = createDevice(driverType, window_size, 16, False, False, False, 0)

		if self.device:
			self.device.setWindowCaption("(http://codeNtronix.com) 3D Wireframe Cube Simulation (http://pir.sourceforge.net)")
			self.device.setResizable(True)
			self.video_driver = self.device.getVideoDriver()
			self.video_driver.SetIcon(IDI_EXCLAMATION)
			#~ self.scene_manager = self.device.getSceneManager()

		self.vertices = [
			Point3D(-1,1,-1),
			Point3D(1,1,-1),
			Point3D(1,-1,-1),
			Point3D(-1,-1,-1),
			Point3D(-1,1,1),
			Point3D(1,1,1),
			Point3D(1,-1,1),
			Point3D(-1,-1,1)
		]

		# Define the vertices that compose each of the 6 faces. These numbers are
		# indices to the vertices list defined above.
		self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

		self.angleX, self.angleY, self.angleZ = 0, 0, 0

	def run(self):
		""" Main Loop """
		if self.device:
			color_background = SColor(255, 10, 10, 50)
			color_line = SColor(255, 255, 255, 255)
			while self.device.run():
				if self.device.isWindowActive():
					if self.video_driver.beginScene(True, True, color_background):
						screen_size = self.video_driver.getScreenSize()

						# Will hold transformed vertices.
						t = []

						for v in self.vertices:
							# Rotate the point around X axis, then around Y axis, and finally around Z axis.
							r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
							# Transform the point from 3D to 2D
							p = r.project(screen_size.X, screen_size.Y, 256, 4)
							# Put the point in the list of transformed vertices
							t.append(p)
						for f in self.faces:
							for i in range(3):
								self.video_driver.draw2DLine(position2di(int(t[f[i]].x), int(t[f[i]].y)), position2di(int(t[f[i+1]].x), int(t[f[i+1]].y)), color_line)
							self.video_driver.draw2DLine(position2di(int(t[f[3]].x), int(t[f[3]].y)), position2di(int(t[f[0]].x), int(t[f[0]].y)), color_line)

						self.angleX += 1
						self.angleY += 1
						self.angleZ += 1

						#~ self.scene_manager.drawAll()
						self.video_driver.endScene()

					self.device.sleep(10)
				else:
					self.device._yield()

			self.device.drop()


if __name__ == "__main__":
	Simulation().run()

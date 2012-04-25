"""
quick demo of using triangulate.py to triangulate/convexise(?) a concave polygon
not good code as such, but functional and cheap

display:
thick red line: drawn polygon
medium blue lines: triangles after triangulation
thin white lines: convex polygons after convexisation(?)

input:
click points (in clockwise order)* to draw a polygon
press space to reset

* triangulate() and convexise() actually work on anticlockwise polys to match pymunk,
  but this demo's coords are upside-down compared to pymunk (pygame style),
  so click clockwise to compensate :)
"""

driver_type = 0
full_screen = False
stencil_buffer = False
vsync = False
run_app = True
screen_x, screen_y = 640, 480

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

	from pymunk.vec2d import Vec2d
	from pymunk.util import *
	import pyirrlicht as irr

	def draw_lines(video_driver, coords, color, width = 0):
		len_coords = len(coords)
		i = 0
		while i < len_coords:
			x1, y1 = coords[i]
			if i+1 < len_coords:
				x2, y2 = coords[i+1]
			else:
				x2, y2 = coords[0]
			video_driver.draw2DLineWf(x1, y1, x2, y2, color, width)
			i = i + 2

	class PolyPoints(object):
		def __init__(self, points):
			self.poly = [Vec2d(point) for point in points]
			self.triangles = triangulate(self.poly)
			self.convexes = convexise(self.triangles)

	class UserIEventReceiver(irr.IEventReceiver):
		mouse_button_down = False
		mouse_position = Vec2d(0, 0)
		KeyIsDown = {}
		for key in range(irr.KEY_KEY_CODES_COUNT):
			KeyIsDown[key] = False
		def OnEvent(self, evt):
			event = irr.SEvent(evt)
			self.mouse_button_down = False
			self.mouse_position = Vec2d(0, 0)
			if event.EventType is irr.EET_KEY_INPUT_EVENT:
				self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
			elif event.EventType is irr.EET_MOUSE_INPUT_EVENT:
				if event.MouseInput.EventType == irr.EMIE_LMOUSE_PRESSED_DOWN:
					self.mouse_button_down = True
					self.mouse_position.x = event.MouseInput.X
					self.mouse_position.y = event.MouseInput.Y
			return False
		def IsKeyDown(self, keyCode):
			return self.KeyIsDown[keyCode]

	if not driver_type:
		driver_type = irr.EDT_SOFTWARE

	window_size = irr.dimension2du(screen_x, screen_y)
	device = irr.createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync)

	if device:
		device.setWindowCaption('pyMunk triangulate test')
		device.setResizable(True)
		video_driver = device.getVideoDriver()

		# init clicked points
		clicked_points = []
		poly = PolyPoints(clicked_points)

		i_event_receiver = UserIEventReceiver()
		device.setEventReceiver(i_event_receiver)
		color_screen = irr.SColor(255, 100, 100, 100)
		color_poly = irr.SColor(255, 150, 0, 0)
		color_triangle = irr.SColor(255, 0, 0, 200)
		color_hull = irr.SColor(255, 255, 255, 255)
		while device.run():
			if device.isWindowActive():
				# handle imput
				if i_event_receiver.IsKeyDown(irr.KEY_ESCAPE):
					break
				elif i_event_receiver.IsKeyDown(irr.KEY_SPACE):
					clicked_points = []
					poly = PolyPoints(clicked_points)
				if i_event_receiver.mouse_button_down:
					clicked_points += [i_event_receiver.mouse_position]
					poly = PolyPoints(clicked_points)

				if video_driver.beginScene(True, True, color_screen):
					# draw poly
					len_clicked_points = len(clicked_points)
					if len_clicked_points == 1:
						x, y = clicked_points[0]
						video_driver.draw2DPolygon_f(x, y, 10, color_poly)
					elif len_clicked_points > 1:
						draw_lines(video_driver, clicked_points, color_poly, 20)

					# draw triangles
					if len(poly.triangles) > 0:
						for triangle in poly.triangles:
							draw_lines(video_driver, triangle, color_triangle, 12)

					# draw hulls
					if len(poly.convexes) > 0:
						for convex in poly.convexes:
							draw_lines(video_driver, convex, color_hull, 2)

					video_driver.endScene()
				device.sleep(50)
			else:
				device._yield()
		device.closeDevice()
	else:
		print('ERROR createDevice')

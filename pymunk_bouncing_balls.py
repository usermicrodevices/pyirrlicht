'pyMunk bouncing balls example'

### video choice dialog pyWinGUI block
driver_type = 1
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
	import pymunk as pm
	from pymunk import Vec2d
	import math, sys, random

	screen_x, screen_y = 640, 480

	def reverse_y(y):
		"""Small hack to convert pymunk to screen coordinates"""
		return -y+screen_y

	### Physics stuff
	space = pm.Space()
	space.gravity = (0.0, -900.0)

	## Balls
	balls = []

	### walls
	static_body = pm.Body()
	static_lines = [pm.Segment(static_body, (111.0, 280.0), (407.0, 246.0), 0.0)
					,pm.Segment(static_body, (407.0, 246.0), (407.0, 343.0), 0.0)
					]
	for line in static_lines:
		line.elasticity = 0.95
	space.add(static_lines)

	ticks_to_next_ball = 10

	### pyIrrlicht block
	from pyirrlicht import *
	if not driver_type:
		driver_type = EDT_SOFTWARE

	window_size = dimension2du(screen_x, screen_y)
	device = createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync)

	if device:
		window_caption = __doc__
		device.setWindowCaption(window_caption)
		device.setResizable(True)
		video_driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		gui_environment = device.getGUIEnvironment()
		static_text = gui_environment.addStaticText(window_caption, recti(10,10,400,22), True)
		color_screen = SColor(255, 100, 100, 100)
		color_line = SColor(255, 200, 200, 200)
		color_ball = SColor(255, 0, 0, 255)
		lastFPS = -1
		update_physics = False
		while device.run():
			if device.isWindowActive():
				if device.getTimer().getTime() > 30:
					### compute balls
					ticks_to_next_ball = ticks_to_next_ball - 1
					if ticks_to_next_ball <= 0:
						ticks_to_next_ball = 100
						mass = 10
						radius = 25
						inertia = pm.moment_for_circle(mass, 0, radius, (0,0))
						body = pm.Body(mass, inertia)
						x = random.randint(115,350)
						body.position = x, 400
						shape = pm.Circle(body, radius, (0,0))
						shape.elasticity = 0.95
						space.add(body, shape)
						balls.append(shape)
					device.getTimer().setTime(0)
					update_physics = True
				### Draw stuff
				if video_driver.beginScene(True, True, color_screen):
					balls_to_remove = []
					for ball in balls:
						if ball.body.position.y < 200:
							balls_to_remove.append(ball)
						video_driver.draw2DPolygon_f(ball.body.position.x, reverse_y(ball.body.position.y), ball.radius, color_ball, 100)
					for ball in balls_to_remove:
						space.remove(ball, ball.body)
						balls.remove(ball)
					for line in static_lines:
						body = line.body
						pv1 = body.position + line.a.rotated(body.angle)
						pv2 = body.position + line.b.rotated(body.angle)
						video_driver.draw2DLine_f(pv1.x, reverse_y(pv1.y), pv2.x, reverse_y(pv2.y), color_line)
					#~ scene_manager.drawAll()
					gui_environment.drawAll()
					### Update physics
					if update_physics:
						dt = 1.0/60.0
						for x in range(1):
							space.step(dt)
						update_physics = False
					### END DRAWING
					video_driver.endScene()
				device.sleep(1)
				### FPS information
				fps = video_driver.getFPS()
				if lastFPS != fps:
					text = '%s [%s] FPS:%d' % (window_caption, video_driver.getName(), fps)
					device.setWindowCaption(text)
					static_text.setText(text)
					lastFPS = fps
			else:
				device._yield()
		device.closeDevice()
	else:
		print('ERROR createDevice')

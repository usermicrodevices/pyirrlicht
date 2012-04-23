'pyMunk balls and lines example'

X,Y = 0,1
### Physics collision types
COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

screen_x, screen_y = 640, 480

text = """\nLMB: Create ball
LMB + Shift: Create many balls
RMB: Drag to create wall, release to finish
Space: Pause physics simulation"""

### Static line
line_point1 = None
static_lines = []
run_physics = True

def flipy(y):
    """Small hack to convert chipmunk physics to screen coordinates"""
    return -y+screen_y

def mouse_coll_func(space, arbiter):
    """Simple callback that increases the radius of circles touching the mouse"""
    s1,s2 = arbiter.shapes
    s2.unsafe_set_radius(s2.radius + 0.15)
    return False

def main():
	global text, line_point1, static_lines, run_physics
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
		import os, math
		import pymunk as pm
		from pymunk import Vec2d

		### Physics stuff
		space = pm.Space()
		space.gravity = Vec2d(0.0, -900.0)

		## Balls
		balls = []

		### Mouse
		mouse_body = pm.Body()
		mouse_shape = pm.Circle(mouse_body, 3, Vec2d(0,0))
		mouse_shape.collision_type = COLLTYPE_MOUSE
		space.add(mouse_shape)

		space.add_collision_handler(COLLTYPE_MOUSE, COLLTYPE_BALL, None, mouse_coll_func, None, None)   

		### pyIrrlicht block
		import pyirrlicht as irr
		if not driver_type:
			driver_type = irr.EDT_SOFTWARE

		class UserIEventReceiver(irr.IEventReceiver):
			shift = False
			control = False
			pressed_down = False
			video_driver = None
			screen_size = irr.dimension2du()
			mouse_position = Vec2d(0, flipy(0))
			KeyIsDown = {}
			for key in range(irr.KEY_KEY_CODES_COUNT):
				KeyIsDown[key] = False
			def OnEvent(self, evt):
				global line_point1
				event = irr.SEvent(evt)
				if event.EventType is irr.EET_KEY_INPUT_EVENT:
					self.shift = event.KeyInput.Shift
					self.control = event.KeyInput.Control
					self.pressed_down = event.KeyInput.PressedDown
					self.KeyIsDown[event.KeyInput.Key] = self.pressed_down
				elif event.EventType is irr.EET_MOUSE_INPUT_EVENT:
					if event.MouseInput.EventType == irr.EMIE_MOUSE_MOVED:
						self.mouse_position.x = event.MouseInput.X
						self.mouse_position.y = event.MouseInput.Y
					elif event.MouseInput.EventType == irr.EMIE_LMOUSE_PRESSED_DOWN:
						body = pm.Body(10, 100)
						body.position = (event.MouseInput.X, flipy(event.MouseInput.Y))
						shape = pm.Circle(body, 10, (0,0))
						shape.friction = 0.5
						shape.collision_type = COLLTYPE_BALL
						space.add(body, shape)
						balls.append(shape)
					elif event.MouseInput.EventType == irr.EMIE_RMOUSE_PRESSED_DOWN: 
						if line_point1 is None:
							line_point1 = Vec2d(event.MouseInput.X, flipy(event.MouseInput.Y))
					elif event.MouseInput.EventType == irr.EMIE_RMOUSE_LEFT_UP: 
						if line_point1 is not None:
							line_point2 = Vec2d(event.MouseInput.X, flipy(event.MouseInput.Y))
							body = pm.Body()
							shape= pm.Segment(body, line_point1, line_point2, 0.0)
							shape.friction = 0.99
							space.add(shape)
							static_lines.append(shape)
							line_point1 = None
				return False
			def IsKeyDown(self, keyCode):
				return self.KeyIsDown[keyCode]
			def mouse_pos(self):
				return self.mouse_position

		window_size = irr.dimension2du(screen_x, screen_y)
		device = irr.createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync)

		if device:
			window_caption = __doc__
			device.setWindowCaption(window_caption)
			device.setResizable(True)
			video_driver = device.getVideoDriver()
			scene_manager = device.getSceneManager()
			gui_environment = device.getGUIEnvironment()
			font = irr.CGUITTFont(gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', 16)
			if not font:
				font = gui_environment.getBuiltInFont()
			gui_environment.getSkin().setFont(font)
			static_text = gui_environment.addStaticText(window_caption + text, irr.recti(10, 10, screen_x-20, 110), True)
			color_red = irr.SColor(255, 255, 0, 0)
			color_blue = irr.SColor(255, 0, 0, 255)
			color_black = irr.SColor(255, 0, 0, 0)
			color_lightgray = irr.SColor(255, 200, 200, 200)
			color_text = irr.SColor(255, 0, 0, 0)
			color_screen = irr.SColor(255, 100, 100, 100)
			lastFPS = -1
			i_event_receiver = UserIEventReceiver()
			i_event_receiver.video_driver = video_driver
			i_event_receiver.gui = gui_environment
			device.setEventReceiver(i_event_receiver)
			while device.run():
				if device.isWindowActive():
					if i_event_receiver.IsKeyDown(irr.KEY_ESCAPE):
						run_physics = not run_physics
						break

					p = i_event_receiver.mouse_pos()
					mouse_pos = Vec2d(p[X],flipy(p[Y]))
					mouse_body.position = mouse_pos

					if i_event_receiver.shift and i_event_receiver.pressed_down:
						body = pm.Body(10, 10)
						body.position = mouse_pos
						shape = pm.Circle(body, 10, (0,0))
						shape.collision_type = COLLTYPE_BALL
						space.add(body, shape)
						balls.append(shape)

					### Update physics
					if run_physics:
						dt = 1.0/60.0
						for x in range(1):
							space.step(dt)

					if video_driver.beginScene(True, True, color_screen):

						### Display some text
						#~ font.draw(text, irr.recti(5, 40, screen_x-10, 50), color_text)

						for ball in balls:           
							r = ball.radius
							v = ball.body.position
							rot = ball.body.rotation_vector
							x1, y1 = v.x, flipy(v.y)
							#~ x2, y2 = (Vec2d(rot.x, -rot.y) * r * 0.9 + (x1, y1)).int_tuple
							end = (Vec2d(rot.x, -rot.y) * r * 0.9 + (x1, y1))
							video_driver.draw2DPolygon_f(x1, y1, r, color_blue, 100)
							video_driver.draw2DLine_f(x1, y1, end.x, end.y, color_red)

						if line_point1 is not None:
							video_driver.draw2DLine_f(line_point1.x, flipy(line_point1.y), mouse_pos.x, flipy(mouse_pos.y), color_black)

						for line in static_lines:
							body = line.body
							pv1 = body.position + line.a.rotated(body.angle)
							pv2 = body.position + line.b.rotated(body.angle)
							video_driver.draw2DLine_f(pv1.x, flipy(pv1.y), pv2.x, flipy(pv2.y), color_lightgray)

						gui_environment.drawAll()
						video_driver.endScene()

					device.sleep(10)

					fps = video_driver.getFPS()
					if lastFPS != fps:
						caption = '%s [%s] FPS:%d' % (window_caption, video_driver.getName(), fps)
						device.setWindowCaption(caption)
						static_text.setText(caption + text)
						lastFPS = fps
				else:
					device._yield()

			device.closeDevice()
		else:
			print('ERROR createDevice')


if __name__ == '__main__':
	doprof = 0
	if not doprof: 
		main()
	else:
		import cProfile, pstats

		prof = cProfile.run("main()", "profile.prof")
		stats = pstats.Stats("profile.prof")
		stats.strip_dirs()
		stats.sort_stats('cumulative', 'time', 'calls')
		stats.print_stats(30)
'pyMunk breakout game from Victor Blomqvist, pyIrrlicht adaptation Maxim Kolosov'

global pymunk, irr, Vec2d, color_darkgray

width, height = 600,600

def to_screen(p):
	"""Small hack to convert pymunk to screen coordinates"""
	return int(p.x), int(-p.y+height)
def from_screen(p): 
	return to_screen(p)

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

def spawn_ball(space, position, direction):
	global pymunk, irr, Vec2d
	ball_body = pymunk.Body(1, pymunk.inf)
	ball_body.position = position

	ball_shape = pymunk.Circle(ball_body, 5)
	ball_shape.color = irr.SColor(255,0,255,0)
	ball_shape.elasticity = 1.0

	ball_body.apply_impulse(Vec2d(direction))

	# Keep ball velocity at a static value
	def constant_velocity(body, gravity, damping, dt):
		body.velocity = body.velocity.normalized() * 400
	ball_body.velocity_func = constant_velocity

	space.add(ball_body, ball_shape)

def setup_level(space, player_body):
	import random
	# Remove balls and bricks
	for s in space.shapes[:]:
		if s.body not in [player_body]:
			space.remove(s.body, s)

	# Spawn a ball for the player to have something to play with
	spawn_ball(space, player_body.position + (0,40), random.choice([(1,1),(-1,1)]))

	# Spawn bricks
	for x in range(0,21):
		x = x * 20 + 100
		for y in range(0,5):
			y = y * 10 + 400
			brick_body = pymunk.Body(pymunk.inf, pymunk.inf)
			brick_body.position = x, y
			brick_shape = pymunk.Poly.create_box(brick_body, (20,10))
			brick_shape.elasticity = 1.0
			brick_shape.color = irr.SColor(255,0,0,255)
			brick_shape.group = 1
			brick_shape.collision_type = 2
			space.add(brick_body, brick_shape)
	# Make bricks be removed when hit by ball
	def remove_first(space, arbiter):
		first_shape = arbiter.shapes[0]
		space.add_post_step_callback(space.remove, first_shape, first_shape.body)
	space.add_collision_handler(2, 0, separate = remove_first)

def draw_space(video_driver, space):
	# Static shapes (the walls)
	for line in space.static_shapes:
		body = line.body
		pv1 = body.position + line.a.rotated(body.angle)
		pv2 = body.position + line.b.rotated(body.angle)
		p1 = to_screen(pv1)
		p2 = to_screen(pv2)
		draw_lines(video_driver, [p1,p2], line.color, int(line.radius))

	# Constraints
	for c in space.constraints:
		if isinstance(c, pymunk.GrooveJoint):
			pv1 = c.a.position + c.groove_a
			pv2 = c.a.position + c.groove_b
		else:
			pv1 = c.a.position + c.anchr1
			pv2 = c.b.position + c.anchr2
		p1 = to_screen(pv1)
		p2 = to_screen(pv2)
		draw_lines(video_driver, [p1,p2], color_darkgray)

	# moving shapes including player
	for shape in space.shapes:
		if isinstance(shape, pymunk.Circle):
			p = to_screen(shape.body.position)
			video_driver.draw2DPolygon_f(p[0], p[1], int(shape.radius), shape.color, 20)
		if isinstance(shape, pymunk.Poly):
			ps = shape.get_points()
			ps = [to_screen(p) for p in ps]
			ps += [ps[0]]
			draw_lines(video_driver, ps, shape.color, 1)

def main():
	driver_type = 0
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
		global pymunk, irr, Vec2d, color_darkgray

		import math, random
		import os

		import pymunk
		from pymunk import Vec2d

		import pyirrlicht as irr

		### Physics stuff
		space = pymunk.Space()   

		### Game area
		# walls - the left-top-right walls
		static_lines = [pymunk.Segment(space.static_body, (50, 50), (50, 550), 5)
					,pymunk.Segment(space.static_body, (50, 550), (550, 550), 5)
					,pymunk.Segment(space.static_body, (550, 550), (550, 50), 5)
					]  
		for line in static_lines:
			line.color = irr.SColor(255, 200, 200, 200)
			line.elasticity = 1.0

		space.add_static(static_lines)

		# bottom - a sensor that removes anything touching it
		bottom = pymunk.Segment(space.static_body, (50, 50), (550, 50), 5)
		bottom.sensor = True
		bottom.collision_type = 1
		bottom.color = irr.SColor(255,255,0,0)
		def remove_first(space, arbiter):
			first_shape = arbiter.shapes[0]
			space.add_post_step_callback(space.remove, first_shape, first_shape.body)
			return True
		space.add_collision_handler(0, 1, begin = remove_first)
		space.add_static(bottom)

		### Player ship
		player_body = pymunk.Body(500, pymunk.inf)
		player_shape = pymunk.Circle(player_body, 35)
		player_shape.color = irr.SColor(255,255,0,0)
		player_shape.elasticity = 1.0
		player_body.position = 300,100
		# restrict movement of player to a straigt line 
		move_joint = pymunk.GrooveJoint(space.static_body, player_body, (100,100), (500,100), (0,0))
		space.add(player_body, player_shape, move_joint)

		# Start game
		setup_level(space, player_body)

		### pyirrlicht init
		class UserIEventReceiver(irr.IEventReceiver):
			#~ mouse_button_down = False
			#~ mouse_position = Vec2d(0, 0)
			KeyIsDown = {}
			for key in range(irr.KEY_KEY_CODES_COUNT):
				KeyIsDown[key] = False
			def OnEvent(self, evt):
				event = irr.SEvent(evt)
				self.mouse_button_down = False
				self.mouse_position = Vec2d(0, 0)
				if event.EventType is irr.EET_KEY_INPUT_EVENT:
					self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
					if event.KeyInput.Key == irr.KEY_LEFT:
						if event.KeyInput.PressedDown:
							player_body.velocity = (-600,0)
						else:
							player_body.velocity = 0,0
					elif event.KeyInput.Key == irr.KEY_RIGHT:
						if event.KeyInput.PressedDown:
							player_body.velocity = (600,0)
						else:
							player_body.velocity = 0,0
					elif event.KeyInput.Key == irr.KEY_KEY_R:
						setup_level(space, player_body)
				#~ elif event.EventType is irr.EET_MOUSE_INPUT_EVENT:
					#~ if event.MouseInput.EventType == irr.EMIE_LMOUSE_PRESSED_DOWN:
						#~ self.mouse_button_down = True
						#~ self.mouse_position.x = event.MouseInput.X
						#~ self.mouse_position.y = event.MouseInput.Y
				return False
			def IsKeyDown(self, keyCode):
				return self.KeyIsDown[keyCode]

		if not driver_type:
			driver_type = irr.EDT_SOFTWARE

		window_size = irr.dimension2du(width, height)
		device = irr.createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync)

		if device:
			device.setWindowCaption('pyMunk breakout game')
			device.setResizable(True)
			video_driver = device.getVideoDriver()
			gui_environment = device.getGUIEnvironment()
			font = irr.CGUITTFont(gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', 16)
			if not font:
				font = gui_environment.getBuiltInFont()

			i_event_receiver = UserIEventReceiver()
			device.setEventReceiver(i_event_receiver)
			color_white = irr.SColor(255, 255, 255, 255)
			color_darkgray = irr.SColor(255, 100, 100, 100)
			color_screen = irr.SColor(255, 0, 0, 0)
			ticks = 60
			dt = 1./ticks
			while device.run():
				if device.isWindowActive():
					if i_event_receiver.IsKeyDown(irr.KEY_ESCAPE):
						break
					elif i_event_receiver.IsKeyDown(irr.KEY_SPACE):
						spawn_ball(space, player_body.position + (0,40), random.choice([(1,1),(-1,1)]))

					### Clear screen
					if video_driver.beginScene(True, True, color_screen):

						### Draw stuff
						draw_space(video_driver, space)

						### Info
						font.draw("fps: %d" % video_driver.getFPS(), irr.recti(0, 0, 100, 20), color_white)
						font.draw("Move with left/right arrows, space to spawn a ball", irr.recti(5, height - 35, 300, 20), color_darkgray)
						font.draw("Press R to reset, ESC or Q to quit", irr.recti(5, height - 20, 300, 20), color_darkgray)

						video_driver.endScene()

					### Update physics
					if device.getTimer().getTime() > ticks:
						space.step(dt)

					device.sleep(1)
				else:
					device._yield()

			device.closeDevice()

if __name__ == '__main__':
	import sys
	sys.exit(main())

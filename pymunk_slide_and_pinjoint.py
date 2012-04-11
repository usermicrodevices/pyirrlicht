'pyMunk slide and pinjoint example'

def main():
	driver_type = 5
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
		import os, math, random
		X,Y,Z = 0,1,2 # Easy indexing

		info_text = '\nJoints. Just wait and the L will tip over'

		### Physics stuff
		space = pm.Space()
		space.gravity = 0.0, -900.0

		## Balls
		balls = []

		### static stuff
		rot_center_body = pm.Body()
		rot_center_body.position = (300,300)

		### To hold back the L
		rot_limit_body = pm.Body()
		rot_limit_body.position = (200,300)

		### The moving L shape
		l1 = [(-150, 0), (255.0, 0.0)]
		l2 = [(-150.0, 0), (-150.0, 50.0)]

		body = pm.Body(10,10000)
		body.position = (300,300)

		lines = [pm.Segment(body, l1[0], l1[1], 5.0), pm.Segment(body, l2[0], l2[1], 5.0)]

		space.add(body)
		space.add(lines)

		### The L rotates around this
		rot_center = pm.PinJoint(body, rot_center_body, (0,0), (0,0))
		### And is constrained by this
		joint_limit = 25
		rot_limit = pm.SlideJoint(body, rot_limit_body, (-100,0), (0,0), 0, joint_limit)
		space.add(rot_center, rot_limit)

		ticks_to_next_ball = 10

		screen_x, screen_y = 640, 480
		def reverse_coords(p):
			"""Small hack to convert pymunk to pygame coordinates"""
			return int(p.x), int(-p.y+screen_y)

		### pyIrrlicht block
		import pyirrlicht as irr
		if not driver_type:
			driver_type = irr.EDT_SOFTWARE

		class UserIEventReceiver(irr.IEventReceiver):
			KeyIsDown = {}
			for key in range(irr.KEY_KEY_CODES_COUNT):
				KeyIsDown[key] = False
			def OnEvent(self, evt):
				event = irr.SEvent(evt)
				if event.EventType is irr.EET_KEY_INPUT_EVENT:
					self.KeyIsDown[event.KeyInput.Key] = event.KeyInput.PressedDown
				return False
			def IsKeyDown(self, keyCode):
				return self.KeyIsDown[keyCode]

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
			static_text = gui_environment.addStaticText(window_caption + info_text, irr.recti(10, 10, screen_x-20, 50), True)
			color_red = irr.SColor(255, 255, 0, 0)
			color_green = irr.SColor(255, 0, 255, 0)
			color_blue = irr.SColor(255, 0, 0, 255)
			color_black = irr.SColor(255, 0, 0, 0)
			color_lightgray = irr.SColor(255, 200, 200, 200)
			color_text = irr.SColor(255, 0, 0, 0)
			color_screen = irr.SColor(255, 100, 100, 100)
			lastFPS = -1
			i_event_receiver = UserIEventReceiver()
			device.setEventReceiver(i_event_receiver)
			while device.run():
				if device.isWindowActive():
					if i_event_receiver.IsKeyDown(irr.KEY_ESCAPE):
						break

					ticks_to_next_ball -= 1
					if ticks_to_next_ball <= 0:
						ticks_to_next_ball = 25
						mass = 1
						radius = 14
						inertia = pm.moment_for_circle(mass, 0, radius, (0,0))
						body = pm.Body(mass, inertia)
						x = random.randint(120,380)
						body.position = x, 550
						shape = pm.Circle(body, radius, (0,0))
						space.add(body, shape)
						balls.append(shape)

					### Draw stuff
					if video_driver.beginScene(True, True, color_screen):
						balls_to_remove = []
						for ball in balls:
							if ball.body.position.y < 150:
								balls_to_remove.append(ball)

							x1, y1 = reverse_coords(ball.body.position)
							#~ pygame.draw.circle(screen, THECOLORS["blue"], p, int(ball.radius), 2)
							video_driver.draw2DPolygon(irr.recti(x1, y1, x1+int(ball.radius*2), y1+int(ball.radius*2)), int(ball.radius), color_blue)

						for ball in balls_to_remove:
							space.remove(ball, ball.body)
							balls.remove(ball)

						for line in lines:
							body = line.body
							pv1 = body.position + line.a.rotated(body.angle)
							pv2 = body.position + line.b.rotated(body.angle)
							x1, y1 = reverse_coords(pv1)
							x2, y2 = reverse_coords(pv2)
							video_driver.draw2DLine(irr.position2di(x1, y1), irr.position2di(x2, y2), color_lightgray)

						### The rotation center of the L shape
						x, y = reverse_coords(rot_center_body.position)
						video_driver.draw2DPolygon(irr.recti(x, y, x+10, y+10), 5, color_red)
						### The limits where it can move.
						x, y = reverse_coords(rot_limit_body.position)
						video_driver.draw2DPolygon(irr.recti(x, y, x+int(joint_limit*2), y+int(joint_limit*2)), joint_limit, color_green, 100)

						gui_environment.drawAll()
						video_driver.endScene()

					### Update physics
					dt = 1.0/50.0/10.0
					for x in range(10):
						space.step(dt)

					device.sleep(1)

					fps = video_driver.getFPS()
					if lastFPS != fps:
						caption = '%s [%s] FPS:%d' % (window_caption, video_driver.getName(), fps)
						device.setWindowCaption(caption)
						static_text.setText(caption + info_text)
						lastFPS = fps
				else:
					device._yield()

			device.closeDevice()
		else:
			print('ERROR createDevice')


if __name__ == '__main__':
	import sys
	sys.exit(main())

"""
 bricka (a breakout clone)
 Original version developed by Leonel Machava <leonelmachava@gmail.com> http://codentronix.com

 pyIrrlicht version - Maxim Kolosov
"""

import os, sys
from pyirrlicht import *

try:
	from cellular import Cellular
except:
	class Cellular:
		def get_texture(self): return None

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

# Object dimensions
BALL_DIAMETER = 16
BALL_RADIUS = BALL_DIAMETER / 2

PADDLE_STEP = 10

# State constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3

def _(value): return value

class event_receiver(IEventReceiver):
	game = None
	stop = False
	def OnEvent(self, evt):
		if self.game.help_dialog:
			try:
				self.game.help_dialog.getID()
			except:
				self.game.help_dialog = None
		event = SEvent(evt)
		if event.EventType is EET_KEY_INPUT_EVENT:
			pressed_down = event.KeyInput.PressedDown
			if not self.game.help_dialog:
				self.check_input(event.KeyInput.Key)
		return False
	def help(self):
		if not self.game.help_dialog:
			self.game.help_dialog = self.game.gui_environment.addMessageBox(_('Help'), _('Copyright (C) Leonel Machava') + '\n' + _('pyIrrlicht version - Maxim Kolosov') + '\n' + _('F1 - help; ESC - exit') + '\n' + _('press space to launch the ball') + '\n' + _('left/right to move paddle') + '\n' + _('resize window before new game'))
	def check_input(self, key):
		if key == KEY_LEFT:
			self.game.offset_x(self.game.paddle, -PADDLE_STEP)
			if self.game.paddle.UpperLeftCorner.X < 0:
				self.game.set_paddle_x(0)
		if key == KEY_RIGHT:
			self.game.offset_x(self.game.paddle, PADDLE_STEP)
			if self.game.paddle.UpperLeftCorner.X > self.game.max_paddle_x:
				self.game.set_paddle_x(self.game.max_paddle_x)
		if key == KEY_SPACE and self.game.state == STATE_BALL_IN_PADDLE:
			self.game.ball_vel = self.game.ball_vel_default
			self.game.state = STATE_PLAYING
		elif key == KEY_RETURN and (self.game.state == STATE_GAME_OVER or self.game.state == STATE_WON):
			self.game.use_cellular_paddle = not self.game.use_cellular_paddle
			self.game.use_cellular_brick = not self.game.use_cellular_brick
			self.game.init_game()
		elif key == KEY_F1:
			self.help()
		elif key == KEY_ESCAPE:
			self.stop = True


class Bricka:
	def __init__(self, driver_type = driverType, width = 320, height = 240):
		self.use_cellular_paddle = False
		self.use_cellular_brick = False
		self.font_height = 20
		self.back_color = SColor(255, 80, 80, 80)
		self.white = SColor(255, 255, 255, 255)
		self.brick_color = SColor(255, 200, 200, 0)
		self.blue = SColor(255, 0, 0, 255)
		self.ball_vel_default = position2di(2, -2)
		self.texture_paddle = None
		self.texture_brick = None
		self.help_dialog = None
		self.video_driver = None
		self.scene_manager = None
		self.gui_environment = None
		self.font_text = None
		self.font_chess = None
		self.skin = None
		p = SIrrlichtCreationParameters()
		p.DriverType = driverType
		p.WindowSize = dimension2du(width, height)
		p.AntiAlias = True
		p.WithAlphaChannel = True
		self.device = createDeviceEx(p)
		if self.device:
			self.device.setResizable(True)
			self.device.setWindowCaption('bricka (a breakout clone by codeNtronix.com)')
			self.video_driver = self.device.getVideoDriver()
			self.scene_manager = self.device.getSceneManager()
			self.gui_environment = self.device.getGUIEnvironment()
			# icon
			if is_frozen():
				self.video_driver.SetIcon(101)
			else:
				self.video_driver.SetIcon()
			# skin
			self.skin = self.gui_environment.getSkin()
			for i in range(EGDC_COUNT):
				col = self.skin.getColor(i)
				col.setAlpha(200)
				self.skin.setColor(i, col)
				if (i + 2) > EGDC_COUNT:
					break
			# font
			self.font = CGUITTFont(self.gui_environment, os.environ['SYSTEMROOT']+'/Fonts/arial.ttf', self.font_height)
			if self.font:
				self.skin.setFont(self.font)
			self.init_game()

	def offset_x(self, rect, value):
		rect.UpperLeftCorner.X += value
		rect.LowerRightCorner.X += value

	def offset_y(self, rect, value):
		rect.UpperLeftCorner.Y += value
		rect.LowerRightCorner.Y += value

	def offset(self, rect, x, y):
		self.offset_x(rect, x)
		self.offset_y(rect, y)

	def set_ball_x(self, value):
		self.ball.UpperLeftCorner.X = value
		self.ball.LowerRightCorner.X = value + BALL_DIAMETER

	def set_ball_y(self, value):
		self.ball.UpperLeftCorner.Y = value
		self.ball.LowerRightCorner.Y = value + BALL_DIAMETER

	def set_paddle_x(self, value):
		self.paddle.UpperLeftCorner.X = value
		self.paddle.LowerRightCorner.X = value + self.paddle_width

	def set_paddle_y(self, value):
		self.paddle.UpperLeftCorner.Y = value
		self.paddle.LowerRightCorner.Y = value + self.paddle_height

	def init_game(self):
		screen_size = self.video_driver.getScreenSize()
		self.brick_width = abs(screen_size.X / 11)
		self.brick_height = abs(screen_size.X / 32)
		self.paddle_width = 60
		self.paddle_height = 12
		self.max_paddle_x = screen_size.X - self.paddle_width
		self.max_ball_x = screen_size.X - BALL_DIAMETER
		self.max_ball_y = screen_size.Y - BALL_DIAMETER
		# Paddle X,Y coordinate
		self.paddle_x = (screen_size.X - self.paddle_width) / 2
		self.paddle_y = screen_size.Y - self.paddle_height - 10
		# ball X,Y coordinate
		self.ball_x = self.paddle_x
		self.ball_y = self.paddle_y - BALL_DIAMETER
		self.lives = 3
		self.score = 0
		self.state = STATE_BALL_IN_PADDLE
		self.paddle = recti(self.paddle_x, self.paddle_y, self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)
		self.ball = recti(self.ball_x, self.ball_y, self.ball_x + BALL_DIAMETER, self.ball_y + BALL_DIAMETER)
		self.ball_vel = self.ball_vel_default
		# cellular texture generator
		self.cell_paddle = Cellular(self.video_driver, self.paddle_width, self.paddle_height, 128)
		self.cell_brick = Cellular(self.video_driver, self.brick_width, self.brick_height, 128)
		if not self.texture_paddle:
			self.texture_paddle = self.cell_paddle.get_texture()
		else:
			self.texture_paddle = self.cell_paddle.get_new_texture(cellSize = 8, density = 4.0, rand_range_count = 25)
		if not self.texture_brick:
			self.texture_brick = self.cell_brick.get_texture()
		else:
			self.texture_brick = self.cell_brick.get_new_texture(mFact = .5, lPower = .5)
		self.create_bricks()

	def show_stats(self):
		if self.font:
			text = 'SCORE: %d    LIVES: %d' % (self.score, self.lives)
			screen_size = self.video_driver.getScreenSize()
			text_dimension = self.font.getDimension(text)
			self.font.draw(text, recti((screen_size.X - text_dimension.Width) / 2, 5, text_dimension.Width, self.font_height), self.white)

	def show_message(self, message):
		if self.font:
			screen_size = self.video_driver.getScreenSize()
			delta_y = 0
			for text in message:
				text_dimension = self.font.getDimension(text)
				self.font.draw(text, recti((screen_size.X - text_dimension.Width) / 2, screen_size.Y / 2 + delta_y, text_dimension.Width, (screen_size.Y - text_dimension.Height) / 2 + delta_y), self.white)
				delta_y += text_dimension.Height

	def create_bricks(self):
		screen_size = self.video_driver.getScreenSize()
		x_delta = self.brick_width + 10
		count_rows = abs(screen_size.Y/68)
		count_columns = abs(screen_size.X/x_delta-1)
		x1 = (screen_size.X - x_delta * count_columns) / 2
		y_ofs = 35
		self.bricks = []
		for i in range(count_rows):
			x_ofs = x1
			for j in range(count_columns):
				self.bricks.append(recti(x_ofs, y_ofs, x_ofs + self.brick_width, y_ofs + self.brick_height))
				x_ofs += x_delta
			y_ofs += self.brick_height + 5

	def draw_bricks(self):
		for brick in self.bricks:
			if self.texture_brick and self.use_cellular_brick:
				self.video_driver.draw2DImage(self.texture_brick, brick.UpperLeftCorner)
			else:
				self.video_driver.draw2DRectangle(self.brick_color, brick)

	def move_ball(self):
		self.offset(self.ball, self.ball_vel.X, self.ball_vel.Y)
		if self.ball.UpperLeftCorner.X <= 0:
			self.set_ball_x(0)
			self.ball_vel.X = -self.ball_vel.X
		elif self.ball.UpperLeftCorner.X >= self.max_ball_x:
			self.set_ball_x(self.max_ball_x)
			self.ball_vel.X = -self.ball_vel.X
		if self.ball.UpperLeftCorner.Y < 0:
			self.set_ball_y(0)
			self.ball_vel.Y = -self.ball_vel.Y
		elif self.ball.UpperLeftCorner.Y >= self.max_ball_y:            
			self.set_ball_y(self.max_ball_y)
			self.ball_vel.Y = -self.ball_vel.Y

	def handle_collisions(self):
		for brick in self.bricks:
			if self.ball.isRectCollided(brick):
				self.score += 3
				self.ball_vel.Y = -self.ball_vel.Y
				self.bricks.remove(brick)
				break
		if len(self.bricks) == 0:
			self.state = STATE_WON
		if self.ball.isRectCollided(self.paddle):
			self.set_ball_y(self.paddle_y - BALL_DIAMETER)
			self.ball_vel.Y = -self.ball_vel.Y
		elif self.ball.UpperLeftCorner.Y > self.paddle.UpperLeftCorner.Y:
			self.lives -= 1
			if self.lives > 0:
				self.state = STATE_BALL_IN_PADDLE
			else:
				self.state = STATE_GAME_OVER

	def run(self):
		i_event_receiver = event_receiver()
		i_event_receiver.game = self
		self.device.setEventReceiver(i_event_receiver)
		while self.device.run():
			if self.device.isWindowActive():
				if i_event_receiver.stop:
					break
				if self.video_driver.beginScene(True, True, self.back_color):
					if self.state == STATE_PLAYING:
						if not self.help_dialog:
							self.move_ball()
							self.handle_collisions()
					elif self.state == STATE_BALL_IN_PADDLE:
						self.set_ball_x(self.paddle.UpperLeftCorner.X + self.paddle.getWidth() / 2)
						self.set_ball_y(self.paddle.UpperLeftCorner.Y - self.ball.getHeight())
						self.show_message(('PRESS SPACE', 'TO LAUNCH THE BALL', 'F1 - help, ESC - exit'))
					elif self.state == STATE_GAME_OVER:
						self.show_message(('GAME OVER', 'PRESS ENTER TO PLAY AGAIN'))
					elif self.state == STATE_WON:
						self.show_message(('YOU WON!', 'PRESS ENTER TO PLAY AGAIN'))
					self.draw_bricks()
					# Draw paddle
					if self.texture_paddle and self.use_cellular_paddle:
						self.video_driver.draw2DImage(self.texture_paddle, self.paddle.UpperLeftCorner)
					else:
						self.video_driver.draw2DRectangle(self.blue, self.paddle)
					# Draw ball
					#~ self.video_driver.draw2DRectangle(self.white, self.ball)
					self.video_driver.draw2DPolygon(self.ball, BALL_RADIUS, self.white)
					self.show_stats()
					if self.help_dialog:
						self.gui_environment.drawAll()
					self.video_driver.endScene()
				self.device.sleep(10)
			else:
				self.device._yield()
		self.device.closeDevice()
		self.device.drop()


if __name__ == "__main__":
	Bricka().run()

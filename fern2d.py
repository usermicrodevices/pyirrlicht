# Fern Fractal - original was written on Actionscript 3 Version by Jim Bumgardner 2008

import os, math, sys
from pyirrlicht import *

GUI_ID_RECURSION_LEVELS = 101
GUI_CAPTION_RECURSION_LEVELS = 'Recursion: %d'
GUI_ID_BEND_ANGLE = 102
GUI_CAPTION_BEND_ANGLE = 'Bend Angle: %d'
GUI_ID_BRANCH_ANGLE = 103
GUI_CAPTION_BRANCH_ANGLE = 'Branch Angle: %d'
GUI_ID_TRUNK_RATIO = 104
GUI_CAPTION_TRUNK_RATIO = 'Trunk Ratio: %.2f'
GUI_ID_BRANCH_RATIO = 105
GUI_CAPTION_BRANCH_RATIO = 'Branch Ratio: %.1f'
GUI_ID_HEIGHT_SCALE = 106
GUI_CAPTION_HEIGHT_SCALE = 'Height Scale: %.1f'

class EventReceiver(IEventReceiver):
	app = None
	def OnEvent(self, evt):
		event = SEvent(evt)
		if event.EventType == EET_GUI_EVENT:
			if event.GUIEvent.EventType == EGET_SCROLL_BAR_CHANGED:
				id = event.GUIEvent.Caller.getID()
				if id == GUI_ID_RECURSION_LEVELS:
					self.app.maxLevels = self.app.scroll_levels.getPos()
					self.app.scroll_levels_caption.setText(GUI_CAPTION_RECURSION_LEVELS % self.app.maxLevels)
				elif id == GUI_ID_BEND_ANGLE:
					self.app.initBendAngle = self.app.scroll_bend_angle.getPos()
					self.app.scroll_bend_angle_caption.setText(GUI_CAPTION_BEND_ANGLE % self.app.initBendAngle)
				elif id == GUI_ID_BRANCH_ANGLE:
					self.app.initBranchAngle = self.app.scroll_branch_angle.getPos()
					self.app.scroll_branch_angle_caption.setText(GUI_CAPTION_BRANCH_ANGLE % self.app.initBranchAngle)
				elif id == GUI_ID_TRUNK_RATIO:
					self.app.trunkRatio = self.app.scroll_trunk_ratio.getPos() * 0.01
					self.app.scroll_trunk_ratio_caption.setText(GUI_CAPTION_TRUNK_RATIO % self.app.trunkRatio)
				elif id == GUI_ID_BRANCH_RATIO:
					self.app.branchRatio = self.app.scroll_branch_ratio.getPos() * 0.1
					self.app.scroll_branch_ratio_caption.setText(GUI_CAPTION_BRANCH_RATIO % self.app.branchRatio)
				elif id == GUI_ID_HEIGHT_SCALE:
					self.app.heightScale = self.app.scroll_height_scale.getPos() * 0.1
					self.app.scroll_height_scale_caption.setText(GUI_CAPTION_HEIGHT_SCALE % self.app.heightScale)
				self.app.redraw()
		return False

class fern():
	'Irrlicht Engine - 2D Fern Fractal generator'

	maxLevels = 6
	initBendAngle = 15
	initBranchAngle = 37
	trunkRatio = 0.1
	branchRatio = 0.4
	heightScale = 2.5
	colors = []
	texture = None

	def __init__(self, width = 800, height = 600, driver_type = 1):
		self.w = width
		self.h = height
		self.device = createDevice(driver_type, dimension2du(self.w, self.h), 16, False, False, False, 0)
		if self.device:
			self.device.setWindowCaption('Please wait...')
			self.device.setResizable(True)
			self.video_driver = self.device.getVideoDriver()
			self.video_driver.SetIcon(IDI_EXCLAMATION)
			self.gui_environment = self.device.getGUIEnvironment()

			fonts_path = '/usr/local/share/fonts'
			if 'win' in sys.platform:
				fonts_path = '{}/Fonts'.format(os.environ['SYSTEMROOT'])
			font_file = '{}/arial.ttf'.format(fonts_path)
			if not os.path.isdir(font_file):
				font_file = '2DGame/arial.ttf'
			gui_font = CGUITTFont(self.gui_environment, font_file, 20)
			if not gui_font:
				gui_font = self.gui_environment.getBuiltInFont()
			skin = self.gui_environment.getSkin()
			skin.setFont(gui_font)
			#gui_font.drop()
			for i in range(EGDC_COUNT):
				col = skin.getColor(i)
				col.setAlpha(100)
				skin.setColor(i, col)

			self.scroll_levels_caption = self.gui_environment.addStaticText(GUI_CAPTION_RECURSION_LEVELS % self.maxLevels, recti(512, 0, 712, 20))
			self.scroll_levels = self.gui_environment.addScrollBar(True, recti(512, 20, 712, 40), id = GUI_ID_RECURSION_LEVELS)
			self.scroll_levels.setMin(1)
			self.scroll_levels.setMax(10)
			self.scroll_levels.setSmallStep(1)
			self.scroll_levels.setLargeStep(2)
			self.scroll_levels.setPos(self.maxLevels)
			self.scroll_levels.setToolTipText('Levels of recursion (1 - 10)')

			self.scroll_bend_angle_caption = self.gui_environment.addStaticText(GUI_CAPTION_BEND_ANGLE % self.initBendAngle, recti(512, 50, 712, 70))
			self.scroll_bend_angle = self.gui_environment.addScrollBar(True, recti(512, 70, 712, 90), id = GUI_ID_BEND_ANGLE)
			self.scroll_bend_angle.setMin(-60)
			self.scroll_bend_angle.setMax(60)
			self.scroll_bend_angle.setSmallStep(1)
			self.scroll_bend_angle.setLargeStep(10)
			self.scroll_bend_angle.setPos(self.initBendAngle)
			self.scroll_bend_angle.setToolTipText('Bend Angle (-60 - 60)')

			self.scroll_branch_angle_caption = self.gui_environment.addStaticText(GUI_CAPTION_BRANCH_ANGLE % self.initBranchAngle, recti(512, 100, 712, 120))
			self.scroll_branch_angle = self.gui_environment.addScrollBar(True, recti(512, 120, 712, 140), id = GUI_ID_BRANCH_ANGLE)
			self.scroll_branch_angle.setMin(0)
			self.scroll_branch_angle.setMax(90)
			self.scroll_branch_angle.setSmallStep(1)
			self.scroll_branch_angle.setLargeStep(10)
			self.scroll_branch_angle.setPos(self.initBranchAngle)
			self.scroll_branch_angle.setToolTipText('Branch Angle (0 - 90)')

			self.scroll_trunk_ratio_caption = self.gui_environment.addStaticText(GUI_CAPTION_TRUNK_RATIO % self.trunkRatio, recti(512, 150, 712, 170))
			self.scroll_trunk_ratio = self.gui_environment.addScrollBar(True, recti(512, 170, 712, 190), id = GUI_ID_TRUNK_RATIO)
			self.scroll_trunk_ratio.setMin(0)
			self.scroll_trunk_ratio.setMax(75)
			self.scroll_trunk_ratio.setSmallStep(1)
			self.scroll_trunk_ratio.setLargeStep(5)
			self.scroll_trunk_ratio.setPos(int(self.trunkRatio * 100))
			self.scroll_trunk_ratio.setToolTipText('Trunk Ratio (0 - 0.75)')

			self.scroll_branch_ratio_caption = self.gui_environment.addStaticText(GUI_CAPTION_BRANCH_RATIO % self.branchRatio, recti(512, 200, 712, 220))
			self.scroll_branch_ratio = self.gui_environment.addScrollBar(True, recti(512, 220, 712, 240), id = GUI_ID_BRANCH_RATIO)
			self.scroll_branch_ratio.setMin(1)
			self.scroll_branch_ratio.setMax(20)
			self.scroll_branch_ratio.setSmallStep(1)
			self.scroll_branch_ratio.setLargeStep(2)
			self.scroll_branch_ratio.setPos(int(self.branchRatio * 10))
			self.scroll_branch_ratio.setToolTipText('Branch Ratio (0.1 - 2)')

			self.scroll_height_scale_caption = self.gui_environment.addStaticText(GUI_CAPTION_HEIGHT_SCALE % self.heightScale, recti(512, 250, 712, 270))
			self.scroll_height_scale = self.gui_environment.addScrollBar(True, recti(512, 270, 712, 290), id = GUI_ID_HEIGHT_SCALE)
			self.scroll_height_scale.setMin(1)
			self.scroll_height_scale.setMax(80)
			self.scroll_height_scale.setSmallStep(1)
			self.scroll_height_scale.setLargeStep(10)
			self.scroll_height_scale.setPos(int(self.heightScale * 10))
			self.scroll_height_scale.setToolTipText('Height Scale (0.1 - 8)')
		else:
			print('ERROR createDevice')

	def draw(self, px, py, a, rad, level):
		cx = int(px + math.cos(a) * rad * self.trunkRatio)
		cy = int(py + math.sin(a) * rad * self.trunkRatio)
		color = SColor(100, 0, 100 + level * 3, 0)
		self.video_driver.draw2DLineW(vector2di(px, py), vector2di(cx, cy), color, level)
		if (level > 0):
			a += self.bendAngle
			level -= 1
			self.draw(cx, cy, a - self.branchAngle, rad * self.branchRatio, level)	  
			self.video_driver.draw2DLineW(vector2di(px, py), vector2di(cx, cy), color, level)
			self.draw(cx, cy, a + self.branchAngle, rad * self.branchRatio, level)	  
			self.video_driver.draw2DLineW(vector2di(px, py), vector2di(cx, cy), color, level)
			self.draw(cx, cy, a, rad * self.antiTrunkRatio, level)

	def redraw(self):
		if self.video_driver.queryFeature(EVDF_RENDER_TO_TARGET):
			rname = 'RTT1'
			if not IRR_WCHAR_FILESYSTEM:
				rname = rname.encode('ascii')
			self.texture = self.video_driver.addRenderTargetTexture(dimension2du(512, 512), rname, ECF_A8R8G8B8)

		if self.texture:
			self.video_driver.setRenderTarget(self.texture, True, True, SColor(0,255,255,255))
			texture_size = self.texture.getOriginalSize()
			w, h = texture_size.X, texture_size.Y
		else:
			w, h = self.w, self.h

		self.bendAngle = self.initBendAngle * math.pi / 180
		self.branchAngle = self.initBranchAngle * math.pi / 180
		self.lastMaxLevels = self.maxLevels
		self.antiTrunkRatio = 1 - self.trunkRatio
		self.startAngle = -math.pi / 2
		px = int(w / 2)
		py = int(h - 5)

		self.draw(px, py, self.startAngle, (h - 100) * self.heightScale, self.maxLevels)

		if self.texture:
			self.video_driver.setRenderTarget(0)
		else:
			self.texture = self.video_driver.addTexture('fern_fractal', self.video_driver.createScreenShot())

	def run(self):
		self.redraw()

		scolor = SColor(255, 100, 100, 200)
		texture_position = position2di(0, 0)

		receiver = EventReceiver()
		receiver.app = self
		self.device.setEventReceiver(receiver)

		self.device.setWindowCaption(self.__doc__)
		while self.device.run():
			if self.device.isWindowActive():
				if self.video_driver.beginScene(True, True, scolor):
					self.video_driver.draw2DImage(self.texture, texture_position)
					self.gui_environment.drawAll()
					self.video_driver.endScene()
				self.device.sleep(1)
			else:
				self.device.yield_self()
		self.device.drop()
		self.device.closeDevice()
		receiver.app = None

if __name__ == '__main__':
	f = fern()
	if f.device:
		f.run()

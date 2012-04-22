'Timer3D - Irrlicht Engine Demo'

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
	from pyirrlicht import *
	if not driver_type:
		#driver_type = EDT_SOFTWARE
		#driver_type = EDT_DIRECT3D9
		driver_type = EDT_OPENGL
	window_size = dimension2du(640, 480)
	device = createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync, 0)

	if device:
		window_caption = __doc__
		device.setResizable(True)
		driver = device.getVideoDriver()
		scene_manager = device.getSceneManager()
		guienv = device.getGUIEnvironment()
		static_text = guienv.addStaticText(window_caption, recti(10, 10, 300, 22), True)
		#~ base = scene_manager.getRootSceneNode()
		base = scene_manager.addEmptySceneNode()

		# 3d timer
		#~ print device.getTimer().getRealTimeAndDateAsTuple()
		rtd = device.getTimer().getRealTimeAndDate()
		#~ material_figures = SMaterial()
		#~ material_figures.EmissiveColor = SColor(255, 255, 0, 0)
		#~ material_figures.MaterialType = EMT_TRANSPARENT_ALPHA_CHANNEL
		timer3d = IText3D(base, scene_manager)
		timer3d.getMaterial(0).EmissiveColor = SColor(255, 0, 0, 255)
		#~ result_set_text = timer3d.setText('%02d:%02d:%02d' % (rtd.Hour, rtd.Minute, rtd.Second), depth = 25, algorithm_build_vertices = ABSV_LINEAR)
		result_set_text = timer3d.setText('%02d:%02d:%02d' % (rtd.Hour, rtd.Minute, rtd.Second), algorithm_build_vertices = ABSV_INTERLEAVE_TWO_PASS, primitive_type = EPT_LINE_LOOP)
		#~ if result_set_text:
			#~ timer3d.set_draw_as_figures(DAF_SPHERE|DAF_MIXED, material_figures)
		print('result_set_text %s' % repr(bool(result_set_text)))
		timer3d.setRotation(vector3df(0, 270, 0))
		#~ timer3d.setScale(vector3df(0.5, 0.5, 0.5))
		timer3d.setIsDebugObject(True)

		# rotation animator
		#~ animator = scene_manager.createRotationAnimator(vector3df(0.0, 0.5, 0.0))
		#~ base.addAnimator(animator)
		#~ animator.drop()
		#~ timer3d.drop()

		# set camera
		camera = scene_manager.addCameraSceneNodeMaya(distance = 2000)
		#~ camera.setTarget(timer3d.getPosition())
		timer3d.setPosition(vector3df(0, 0, -1500))

		scene_color = SColor(255, 100, 100, 100)
		white_color = SColor(255, 255, 255, 255)
		lastFPS = -1
		angle = 0
		while device.run():
			if device.getTimer().getTime() > 1000:
				rtd = device.getTimer().getRealTimeAndDate()
				timer3d.setText('%02d:%02d:%02d' % (rtd.Hour, rtd.Minute, rtd.Second), algorithm_build_vertices = ABSV_INTERLEAVE_TWO_PASS, primitive_type = EPT_LINE_LOOP)
				#~ animator.animateNode(timer3d, 10000)
				#~ timer3d.updateAbsolutePosition()
				#~ if timer3d.setText('%02d:%02d:%02d' % (rtd.Hour, rtd.Minute, rtd.Second), algorithm_build_vertices = ABSV_LINEAR):
					#~ timer3d.set_draw_as_figures(DAF_SPHERE|DAF_MIXED, material_figures)
				device.getTimer().setTime(0)
			if device.isWindowActive():
				if driver.beginScene(True, True, scene_color):
					base.setRotation(vector3df(0, angle, 0))
					if angle < 360:
						angle = angle + 1
					else:
						angle = 0
					scene_manager.drawAll()
					guienv.drawAll()
					driver.endScene()
				device.sleep(1)
				fps = driver.getFPS()
				if lastFPS != fps:
					text = '%s [%s] FPS:%d' % (window_caption, driver.getName(), fps)
					device.setWindowCaption(text)
					static_text.setText(text)
					lastFPS = fps
			else:
				device._yield()
		device.closeDevice()
	else:
		print('ERROR createDevice')

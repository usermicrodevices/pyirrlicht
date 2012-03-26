# pyODE example 3: Collision detection

# Originally by Matthias Baas.
# Updated by Pierre Gay to work without pygame or cgkit.

# pyirrlicht adaptation Maxim Kolosov

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
	import time
	import sys, os, random
	from math import *

	#~ os.environ['IRRLICHT_C_LIBRARY'] = 'irrlicht_c_173'

	from pyirrlicht import *

	import ode


	# A list with ODE bodies
	bodies = []

	# The geoms for each of the bodies
	geoms = []

	# Create a world object
	world = ode.World()
	world.setGravity( (0,-9.81,0) )
	world.setERP(0.8)
	world.setCFM(1E-5)

	# Create a space object
	space = ode.Space()

	# Create a plane geom which prevent the objects from falling forever
	floor = ode.GeomPlane(space, (0,1,0), 0)

	# A joint group for the contact joints that are generated whenever
	# two bodies collide
	contactgroup = ode.JointGroup()

	# Some variables used inside the simulation loop
	fps = 50
	dt = 1.0/fps
	running = True
	state = 0
	counter = 0
	objcount = 0
	lasttime = time.time()

	material = None
	scene_manager = None

	# geometric utility functions
	def scalp (vec, scal):
		vec[0] *= scal
		vec[1] *= scal
		vec[2] *= scal

	def length (vec):
		return sqrt (vec[0]**2 + vec[1]**2 + vec[2]**2)


	# draw_body
	def draw_body(node, body):
		"""Draw an ODE body.
		"""
		x,y,z = body.getPosition()
		node.setPosition(vector3df(x,y,z)*10)
		w,xx,yy,zz = body.getQuaternion()
		node.setRotation(vector3df(degrees(xx), degrees(yy), degrees(zz)))
		if body.shape == "box":
			sx,sy,sz = body.boxsize
			node.setScale(vector3df(sx,sy,sz))


	# create_box
	def create_box(world, space, density, lx, ly, lz):
		"""Create a box body and its corresponding geom."""

		# Create body
		body = ode.Body(world)
		M = ode.Mass()
		M.setBox(density, lx, ly, lz)
		body.setMass(M)

		# Set parameters for drawing the body
		body.shape = "box"
		body.boxsize = (lx, ly, lz)

		# Create a box geom for collision detection
		geom = ode.GeomBox(space, lengths = body.boxsize)
		geom.setBody(body)

		return body, geom

	# drop_object
	def drop_object():
		"""Drop an object into the scene."""

		global bodies, geom, counter, objcount

		body, geom = create_box(world, space, 1000, 1.0, 0.2, 0.2)
		body_position = (random.gauss(0, 0.1), 3.0, random.gauss(0, 0.1))
		body.setPosition(body_position)
		theta = random.uniform(0,2 * pi)
		ct = cos(theta)
		st = sin(theta)
		body.setRotation([ct, 0.0, -st, 0.0, 1.0, 0.0, st, 0.0, ct])
		node = scene_manager.addCubeSceneNode(position = vector3df(*body_position))
		node.setMaterial(material)
		node.setMaterialFlag(EMF_LIGHTING, False)
		w,xx,yy,zz = body.getQuaternion()
		node.setRotation(vector3df(degrees(xx), degrees(yy), degrees(zz)))
		bodies.append((node, body))
		geoms.append(geom)
		counter = 0
		objcount += 1

	# explosion
	def explosion():
		"""Simulate an explosion.

		Every object is pushed away from the origin.
		The force is dependent on the objects distance from the origin.
		"""
		global bodies

		for n, b in bodies:
			l = b.getPosition()
			d = length(l)
			a = max(0, 40000 * (1.0 - 0.2 * d * d))
			l = [l[0] / 4, l[1], l[2] /4]
			scalp(l, a / length(l))
			b.addForce(l)

	# pull
	def pull():
		"""Pull the objects back to the origin.

		Every object will be pulled back to the origin.
		Every couple of frames there'll be a thrust upwards so that
		the objects won't stick to the ground all the time.
		"""
		global bodies, counter

		for n, b in bodies:
			l = list(b.getPosition())
			scalp (l, -1000 / length(l))
			b.addForce(l)
			if counter%60 == 0:
				b.addForce((0, 10000, 0))

	# Collision callback
	def near_callback(args, geom1, geom2):
		"""Callback function for the collide() method.

		This function checks if the given geoms do collide and
		creates contact joints if they do.
		"""

		# Check if the objects do collide
		contacts = ode.collide(geom1, geom2)

		# Create contact joints
		world,contactgroup = args
		for c in contacts:
			c.setBounce(0.2)
			c.setMu(5000)
			j = ode.ContactJoint(world, contactgroup, c)
			j.attach(geom1.getBody(), geom2.getBody())




	# draw callback
	def _drawfunc():
		# Draw the scene
		for n, b in bodies:
			draw_body(n, b)


	# idle callback
	def _idlefunc():
		global counter, state, lasttime
		t = dt - (time.time() - lasttime)
		if (t > 0):
			time.sleep(t)
		counter += 1
		if state == 0:
			if counter == 20:
				drop_object()
			if objcount == 30:
				state = 1
				counter = 0
		# State 1: Explosion and pulling back the objects
		elif state == 1:
			if counter == 100:
				explosion()
			if counter > 300:
				pull()
			if counter == 500:
				counter = 20
		# Simulate
		n = 4
		for i in range(n):
			# Detect collisions and create contact joints
			space.collide((world,contactgroup), near_callback)
			# Simulation step
			world.step(dt/n)
			# Remove all contact joints
			contactgroup.empty()
		lasttime = time.time()


	if not driver_type:
		driver_type = EDT_OPENGL

	class UserIEventReceiver(IEventReceiver):
		def OnEvent(self, evt):
			#~ event = SEvent(evt)
			#~ print('EventType', event.EventType)
			return False

	window_size = dimension2du(320, 240)
	device = createDevice(driver_type, window_size, 16, full_screen, stencil_buffer, vsync, 0)

	if device:
		device.setWindowCaption('PyODE example 3 - Irrlicht Engine Demo')
		device.setResizable(True)
		video_driver = device.getVideoDriver()
		video_driver.SetIcon(IDI_EXCLAMATION)
		scene_manager = device.getSceneManager()
		gui_environment = device.getGUIEnvironment()
		#~ camera = scene_manager.addCameraSceneNode(position = vector3df(0,0,10))
		#~ camera = scene_manager.addCameraSceneNodeFPS()
		camera = scene_manager.addCameraSceneNodeMaya(distance = 30.0)
		camera.setTarget(vector3df(0,15,0))
		#~ camera.setPosition(vector3df(10,0,10))
		camera.setNearValue(0.1)
		camera.setFarValue(1000.0)
		scolor = SColor(255,100,100,100)
		i_event_receiver = UserIEventReceiver()
		device.setEventReceiver(i_event_receiver)
		material = SMaterial()
		material.setTexture(0, generate_texture(video_driver))
		while device.run():
			if device.isWindowActive():
				if video_driver.beginScene(True, True, scolor):
					_idlefunc()
					_drawfunc()
					scene_manager.drawAll()
					#~ gui_environment.drawAll()
					video_driver.endScene()
				device.sleep(fps)
			else:
				device.yield_self()
		device.drop()
	else:
		print('ERROR createDevice')

import os
from irrlicht import *

FIRED = 1

def deletePathFromFilename(value = ''):
	return os.path.basename(value)
	
def cutFilenameExtension(value = ''):
	return os.path.splitext(value)[0]

def getNoiser():
	return float(((0x69666966 * 3631 + 1) & 0x7FFF ) * (1.0 / (0x7FFF >> 1))) - 1.0

def dropElement(x):
	if x:
		x.remove()
		x = 0

def setTimeFire(t, delta, flags = 0):
	t.next = 0
	t.delta = delta
	t.flags = flags

def checkTimeFire(t, listSize, now):
	i = 0
	#~ for i in range(listSize):
	while i < listSize:
		if now < t[i].next:
			continue
		#~ t[i].next = max( now + t[i].delta, t[i].next + t[i].delta)
		t[i].flags |= FIRED
		i += 1

class TimeFire:
	flags = 0
	next = 0
	delta = 0

class GameData:
	debugState = 0
	gravityState = 0
	flyTroughState = 0
	wireFrame = 0
	guiActive = 0
	guiInputActive = 0
	GammaValue = 0.0
	retVal = 0
	sound = 0
	StartupDir = ''
	CurrentMapName = ''
	CurrentArchiveList = []
	PlayerPosition = vector3df()
	PlayerRotation = vector3df()
	#~ Variable = tQ3EntityList()
	loadParam = Q3LevelLoadParameter()
	deviceParam = SIrrlichtCreationParameters()
	createExDevice = createDeviceEx#funcptr_createDeviceEx
	Device = None

	def __init__(self, startupDir = ''):
		self.StartupDir = startupDir
		self.setDefault()

	def setDefault(self):
		self.debugState = EDS_OFF
		self.gravityState = 1
		self.flyTroughState = 0
		self.wireFrame = 0
		self.guiActive = 1
		self.guiInputActive = 0
		self.GammaValue = 1.0
		#~ self.deviceParam.DriverType = EDT_DIRECT3D9
		self.deviceParam.DriverType = EDT_OPENGL
		self.deviceParam.WindowSize.Width = 800
		self.deviceParam.WindowSize.Height = 600
		self.deviceParam.Fullscreen = False
		self.deviceParam.Bits = 24
		self.deviceParam.ZBufferBits = 16
		self.deviceParam.Vsync = False
		self.deviceParam.AntiAlias = False
		self.loadParam.defaultLightMapMaterial = EMT_LIGHTMAP
		self.loadParam.defaultModulate = EMFN_MODULATE_1X
		self.loadParam.defaultFilter = EMF_ANISOTROPIC_FILTER
		self.loadParam.verbose = 2
		self.loadParam.mergeShaderBuffer = 1		# merge meshbuffers with same material
		self.loadParam.cleanUnResolvedMeshes = 1	# should unresolved meshes be cleaned. otherwise blue texture
		self.loadParam.loadAllShaders = 1			# load all scripts in the script directory
		self.loadParam.loadSkyShader = 0			# load sky Shader
		self.loadParam.alpharef = 1
		self.sound = 0
		self.CurrentMapName = ""
		self.CurrentArchiveList = []
		self.CurrentArchiveList.append(self.StartupDir + "media/")
		#~ self.CurrentArchiveList.append("/q/baseq3/")
		self.CurrentArchiveList.append(self.StartupDir + "media/map-20kdm2.pk3")

	def load(self, filename = ''):
		if not self.Device:
			return 0
		# the quake3 mesh loader can also handle *.shader and *.cfg file
		#(IQ3LevelMesh*)
		mesh = self.Device.getSceneManager().getMesh(filename)
		if not mesh:
			return 0
		#tQ3EntityList &
		#~ entityList = mesh.as_IQ3LevelMesh().getEntityList()
		entityList = mesh.as_IQ3LevelMesh().get_EntityList()
		s = ''
		pos = 0
		for e in range(len(entityList)):
			#dumpShader ( s, &entityList[e], False )
			for g in range(entityList[e].getGroupSize()):
				#const SVarGroup *
				group = entityList[e].getGroup(g)
				for index in range(group.Variable.size()):
					#const SVariable &
					v = group.Variable[index]
					pos = 0
					if v.name == "playerposition":
						self.PlayerPosition = getAsVector3df(v.content, pos)
					else:
						if v.name == "playerrotation":
							self.PlayerRotation = getAsVector3df(v.content, pos)
		return 1

	def save(self, filename = ''):
		if not self.Device:
			return 0
		# Store current Archive for restart
		#~ self.CurrentArchiveList.clear()
		fs = self.Device.getFileSystem()
		for i in range(fs.getFileArchiveCount()):
			self.CurrentArchiveList.append(fs.getFileArchive(i).getFileList().getPath())
		# Store Player Position and Rotation
		camera = self.Device.getSceneManager().getActiveCamera()
		if camera:
			self.PlayerPosition = camera.getPosition()
			self.PlayerRotation = camera.getRotation()
		file = fs.createAndWriteFile(filename)
		if not file:
			return 0
		buf = "playerposition %.f %.f %.f\nplayerrotation %.f %.f %.f\n" % (self.PlayerPosition.X, self.PlayerPosition.Z, self.PlayerPosition.Y, self.PlayerRotation.X, self.PlayerRotation.Z, self.PlayerRotation.Y)
		file.write(buf, len(buf))
		for i in range(fs.getFileArchiveCount()):
			buf = "archive %s\n" % fs.getFileArchive(i).getFileList().getPath()
			file.write(buf, len(buf))
		file.drop()
		return 1

class Q3Player(IAnimationEndCallBack):
	def __init__(self):
		self.Device = None
		self.MapParent = None
		self.Mesh = None
		self.WeaponNode = None
		self.StartPositionCurrent = 0
		self.Anim = [TimeFire(), TimeFire(), TimeFire(), TimeFire()]
		self.animation = ''
		self.buf = ''

	def cam(self):
		camera = self.Device.getSceneManager().getActiveCamera()
		for a in camera.get_animators():
			if a.getType() == ESNAT_COLLISION_RESPONSE:
				return a.as_ISceneNodeAnimatorCollisionResponse()
		return None

	def shutdown(self):
		self.setAnim(0)
		dropElement(self.WeaponNode)
		if self.Device:
			camera = self.Device.getSceneManager().getActiveCamera()
			dropElement(camera)
			self.Device = None
		self.MapParent = None
		self.Mesh = None

	def getGravity(self, surface):
		if surface == "earth": return vector3df(0.0, -90.0, 0.0)
		elif surface == "moon": return vector3df(0.0, -6.0 / 100.0, 0.0)
		elif surface == "water": return vector3df(0.1 / 100.0, -2.0 / 100.0, 0.0)
		elif surface == "ice": return vector3df(0.2 / 100.0, -9.0 / 100.0, 0.3 / 100.0)
		else: return vector3df(0.0, 0.0, 0.0)

	def create(self, device, mesh, mapNode, meta):
		if not device:
			return
		setTimeFire(self.Anim[0], 200, FIRED)
		setTimeFire(self.Anim[1], 5000)
		self.Device = device
		self.Mesh = mesh
		self.MapParent = mapNode
		smgr = self.Device.getSceneManager()
		driver = self.Device.getVideoDriver()
		#~ keyMap = newSKeyMap(10)
		#~ keyMap[0].Action = EKA_MOVE_FORWARD
		#~ keyMap[0].KeyCode = KEY_UP
		#~ keyMap[1].Action = EKA_MOVE_FORWARD
		#~ keyMap[1].KeyCode = KEY_KEY_W
		#~ keyMap[2].Action = EKA_MOVE_BACKWARD
		#~ keyMap[2].KeyCode = KEY_DOWN
		#~ keyMap[3].Action = EKA_MOVE_BACKWARD
		#~ keyMap[3].KeyCode = KEY_KEY_S
		#~ keyMap[4].Action = EKA_STRAFE_LEFT
		#~ keyMap[4].KeyCode = KEY_LEFT
		#~ keyMap[5].Action = EKA_STRAFE_LEFT
		#~ keyMap[5].KeyCode = KEY_KEY_A
		#~ keyMap[6].Action = EKA_STRAFE_RIGHT
		#~ keyMap[6].KeyCode = KEY_RIGHT
		#~ keyMap[7].Action = EKA_STRAFE_RIGHT
		#~ keyMap[7].KeyCode = KEY_KEY_D
		#~ keyMap[8].Action = EKA_JUMP_UP
		#~ keyMap[8].KeyCode = KEY_KEY_J
		#~ keyMap[9].Action = EKA_CROUCH
		#~ keyMap[9].KeyCode = KEY_KEY_C
		keyMap = smgr.create_keymaps(10)
		smgr.set_keymap(keyMap, 0, EKA_MOVE_FORWARD, KEY_UP)
		smgr.set_keymap(keyMap, 1, EKA_MOVE_FORWARD, KEY_KEY_W)
		smgr.set_keymap(keyMap, 2, EKA_MOVE_BACKWARD, KEY_DOWN)
		smgr.set_keymap(keyMap, 3, EKA_MOVE_BACKWARD, KEY_KEY_S)
		smgr.set_keymap(keyMap, 4, EKA_STRAFE_LEFT, KEY_LEFT)
		smgr.set_keymap(keyMap, 5, EKA_STRAFE_LEFT, KEY_KEY_A)
		smgr.set_keymap(keyMap, 6, EKA_STRAFE_RIGHT, KEY_RIGHT)
		smgr.set_keymap(keyMap, 7, EKA_STRAFE_RIGHT, KEY_KEY_D)
		smgr.set_keymap(keyMap, 8, EKA_JUMP_UP, KEY_KEY_J)
		smgr.set_keymap(keyMap, 9, EKA_CROUCH, KEY_KEY_C)
		camera = smgr.addCameraSceneNodeFPS(None, 100.0, 0.6, -1, keyMap, 10, False, 0.6)
		camera.setName("First Person Camera")
		#camera.setFOV(100.0 * DEGTORAD)
		camera.setFarValue(20000.0)
		weaponMesh = smgr.getMesh("gun.md2").as_IAnimatedMeshMD2()
		if not weaponMesh:
			return
		if weaponMesh.getMeshType() == EAMT_MD2:
			i = 0
			count = weaponMesh.getAnimationCount()
			while i < count:
				buf = "Animation: %s" % weaponMesh.getAnimationName(i)
				device.getLogger().log(buf, ELL_INFORMATION)
				i += 1
		self.WeaponNode = smgr.addAnimatedMeshSceneNode(weaponMesh, smgr.getActiveCamera(), 10, vector3df( 0, 0, 0), vector3df(-90,-90,90))
		self.WeaponNode.setMaterialFlag(EMF_LIGHTING, False)
		self.WeaponNode.setMaterialTexture(0, driver.getTexture("gun.jpg"))
		self.WeaponNode.setLoopMode(False)
		self.WeaponNode.setName("tommi the gun man")
		anim = smgr.createCollisionResponseAnimator(meta, camera, vector3df(30,45,30), self.getGravity("earth"), vector3df(0,40,0), 0.0005)
		camera.addAnimator(anim)
		anim.drop()
		if meta:
			meta.drop()
		self.respawn()
		self.setAnim("idle")

	def respawn(self):
		if not self.Device:
			return
		camera = self.Device.getSceneManager().getActiveCamera()
		self.Device.getLogger().log("respawn")
		i_scene_node_animator_collision_response = self.cam()
		if i_scene_node_animator_collision_response:
			if self.StartPositionCurrent >= self.Q3StartPosition(camera, self.StartPositionCurrent+1, i_scene_node_animator_collision_response.getEllipsoidTranslation()):
				self.StartPositionCurrent = 0

	def Q3StartPosition(self, camera, startposIndex, translation):
		if not self.Mesh:
			return 0
		entityList = self.Mesh.getEntityList()
		search = IEntity()
		search.name = "info_player_start"# "info_player_deathmatch"
		lastIndex = 0
		index = entityList.binary_search_multi(search, lastIndex)
		if index < 0:
			search.name = "info_player_deathmatch"
			index = entityList.binary_search_multi(search, lastIndex)
		if index < 0:
			return 0
		index += max(min(startposIndex, 0), lastIndex - index)
		group = SVarGroup()
		group = entityList[index].getGroup(1)
		parsepos = 0
		pos = getAsVector3df(group.get("origin"), parsepos)
		pos += translation
		parsepos = 0
		angle = getAsFloat(group.get("angle"), parsepos)
		target = vector3df(0.0, 0.0, 1.0)
		target.rotateXZBy(angle - 90.0, vector3df())
		if camera:
			camera.setPosition(pos)
			camera.setTarget(pos + target)
			camera.OnAnimate(0)
		return lastIndex - index + 1

	def setpos(self, pos, rotation):
		if self.Device:
			self.Device.getLogger().log("setpos")
			camera = self.Device.getSceneManager().getActiveCamera()
			if camera:
				camera.setPosition(pos)
				camera.setRotation(rotation)
				camera.OnAnimate(0)

	def setAnim(self, name):
		if name:
			self.animation = name
			if self.WeaponNode:
				#~ self.WeaponNode.setAnimationEndCallback(self.get_this())
				self.WeaponNode.setAnimationEndCallback(self.Device.getSceneManager().as_IAnimationEndCallBack(self))
				self.WeaponNode.setMD2Animation(self.animation)
		else:
			self.animation = ''
			if self.WeaponNode:
				self.WeaponNode.setAnimationEndCallback(None)

	def OnAnimationEnd(self, node):
		self.setAnim('')

class GUI:
	VideoDriver = None
	VideoMode = None
	FullScreen = None
	Bit32 = None
	MultiSample = None
	SetVideoMode = None
	Tesselation = None
	Gamma = None
	Collision = None
	Visible_Map = None
	Visible_Shader = None
	Visible_Fog = None
	Visible_Unresolved = None
	Visible_Skydome = None
	Respawn = None
	ArchiveList = None
	ArchiveAdd = None
	ArchiveRemove = None
	ArchiveFileOpen = None
	ArchiveUp = None
	ArchiveDown = None
	MapList = None
	SceneTree = None
	StatusLine = None
	Logo = None
	Window = None
	def drop(self):
		dropElement(self.Window)
		dropElement(self.Logo)

class CQuake3EventHandler(IEventReceiver):
	Game = None
	Mesh = None
	MapParent = None
	ShaderParent = None
	ItemParent = None
	UnresolvedParent = None
	BulletParent = None
	FogParent = None
	SkyNode = None
	Meta = None
	bank = None
	buf = ''
	Player = [Q3Player(), Q3Player()]
	class SParticleImpact:
		when = 0
		pos = vector3df()
		outVector = vector3df()
	#~ array<SParticleImpact> Impacts
	Impacts = []
	gui = GUI()

	def init_game(self, game = GameData()):
		if game:
			self.Game = game
		else:
			if not self.Game:
				self.Game = GameData()
		if self.Game.deviceParam.Bits == 16:
			game.Device.getVideoDriver().setTextureCreationFlag(ETCF_ALWAYS_16_BIT, True)
		game.Device.getSceneManager().getParameters().setAttribute(ALLOW_ZWRITE_ON_TRANSPARENT, True)
		self.createTextures()
		#~ self.sound_init(game.Device)
		self.Game.Device.setEventReceiver(self)

	def uninit_game(self):
		self.Player[0].shutdown()
		#~ self.sound_shutdown()
		self.Game.save("explorer.cfg")
		self.Game.Device.drop()

	def GetPlayer(self, index):
		return self.Player[index]

	def createTextures(self):
		driver = self.Game.Device.getVideoDriver()
		dim = dimension2du(64, 64)
		texture = None
		for i in range(8):
			image = driver.createImage(ECF_A8R8G8B8, dim)
			#~ data = image.lock()
			for y in range(dim.Height):
				for x in range(dim.Width):
					#~ data[x] = 0xFFFFFFFF
					image.setPixel(x, y, SColor(int(0xFFFF)))
				#~ data = data + image.getPitch()
			#~ image.unlock()
			buf = "smoke_%02d" % i
			texture = driver.addTexture(buf, image)
			image.drop()
		# fog
		for i in range(1):
			image = driver.createImage(ECF_A8R8G8B8, dim)
			#~ data = image.lock()
			for y in range(dim.Height):
				for x in range(dim.Width):
					#~ data[x] = 0xFFFFFFFF
					image.setPixel(x, y, SColor(int(0xFFFF)))
				#~ data = data + image.getPitch()
			#~ image.unlock()
			buf = "fog_%02d" % i
			texture = driver.addTexture(buf, image)
			image.drop()

	def CreateGUI(self):
		env = self.Game.Device.getGUIEnvironment()
		driver = self.Game.Device.getVideoDriver()
		self.gui.drop()
		# set skin font
		font = env.getFont("fontlucida.png")
		if font:
			env.getSkin().setFont(font)
		env.getSkin().setColor(EGDC_BUTTON_TEXT, SColor(240,int(0xAA),int(0xAA),int(0xAA)))
		env.getSkin().setColor(EGDC_3D_HIGH_LIGHT, SColor(240,int(0x22),int(0x22),int(0x22)))
		env.getSkin().setColor(EGDC_3D_FACE, SColor(240,int(0x44),int(0x44),int(0x44)))
		env.getSkin().setColor(EGDC_WINDOW, SColor(240,int(0x66),int(0x66),int(0x66)))
		# minimal gui size 800x600
		dim = dimension2du(800, 600)
		vdim = self.Game.Device.getVideoDriver().getScreenSize()
		self.gui.Window = env.addWindow(recti(0, 0, dim.Width, dim.Height), False, "Quake3 Explorer")
		self.gui.Window.setToolTipText("Quake3Explorer. Loads and show various BSP File Format and Shaders.")
		self.gui.Window.getCloseButton().setToolTipText("Quit Quake3 Explorer")
		# add a status line help text
		self.gui.StatusLine = env.addStaticText('', recti(5, dim.Height - 30, dim.Width - 5, dim.Height - 10), False, False, self.gui.Window, -1, True)
		env.addStaticText("VideoDriver:", recti(dim.Width - 400, 24, dim.Width - 310, 40 ),False, False, self.gui.Window, -1, False)
		self.gui.VideoDriver = env.addComboBox(recti(dim.Width - 300, 24, dim.Width - 10, 40 ), self.gui.Window)
		self.gui.VideoDriver.addItem("Direct3D 9.0c", EDT_DIRECT3D9)
		self.gui.VideoDriver.addItem("Direct3D 8.1", EDT_DIRECT3D8)
		self.gui.VideoDriver.addItem("OpenGL 1.5", EDT_OPENGL)
		self.gui.VideoDriver.addItem("Software Renderer", EDT_SOFTWARE)
		self.gui.VideoDriver.addItem("Burning's Video (TM) Thomas Alten", EDT_BURNINGSVIDEO)
		self.gui.VideoDriver.setSelected(self.gui.VideoDriver.getIndexForItemData(self.Game.deviceParam.DriverType))
		self.gui.VideoDriver.setToolTipText("Use a VideoDriver")
		env.addStaticText("VideoMode:", recti(dim.Width - 400, 44, dim.Width - 310, 60 ),False, False, self.gui.Window, -1, False)
		self.gui.VideoMode = env.addComboBox(recti(dim.Width - 300, 44, dim.Width - 10, 60 ), self.gui.Window)
		self.gui.VideoMode.setToolTipText("Supported Screenmodes")
		modeList = self.Game.Device.getVideoModeList()
		if modeList:
			for i in range(modeList.getVideoModeCount()):
				d = modeList.getVideoModeDepth(i)
				if d < 16:
					continue
				w = modeList.getVideoModeResolution(i).Width
				h = modeList.getVideoModeResolution(i).Height
				val = w << 16 | h
				if self.gui.VideoMode.getIndexForItemData(val) >= 0:
					continue
				aspect = w / h
				a = ""
				if aspect <= 1.3333333333: a = "4:3"
				elif aspect == 1.6666666: a = "15:9 widescreen"
				elif aspect == 1.7777777: a = "16:9 widescreen"
				elif aspect == 1.6: a = "16:10 widescreen"
				elif aspect == 2.133333: a = "20:9 widescreen"
				self.buf =  "%d x %d, %s" % (w, h, a)
				self.gui.VideoMode.addItem(self.buf, val)
		self.gui.VideoMode.setSelected(self.gui.VideoMode.getIndexForItemData(self.Game.deviceParam.WindowSize.Width << 16 | self.Game.deviceParam.WindowSize.Height))
		self.gui.FullScreen = env.addCheckBox(self.Game.deviceParam.Fullscreen, recti( dim.Width - 400, 64, dim.Width - 300, 80), self.gui.Window, -1, "Fullscreen")
		self.gui.FullScreen.setToolTipText("Set Fullscreen or Window Mode")
		self.gui.Bit32 = env.addCheckBox(self.Game.deviceParam.Bits == 32, recti(dim.Width - 300, 64, dim.Width - 240, 80), self.gui.Window, -1, "32Bit")
		self.gui.Bit32.setToolTipText("Use 16 or 32 Bit")
		env.addStaticText("MultiSample:", recti( dim.Width - 235, 64, dim.Width - 150, 80),False, False, self.gui.Window, -1, False)
		self.gui.MultiSample = env.addScrollBar( True, recti( dim.Width - 150, 64, dim.Width - 70, 80), self.gui.Window, -1)
		self.gui.MultiSample.setMin(0)
		self.gui.MultiSample.setMax(8)
		self.gui.MultiSample.setSmallStep(1)
		self.gui.MultiSample.setLargeStep(1)
		self.gui.MultiSample.setPos(self.Game.deviceParam.AntiAlias)
		self.gui.MultiSample.setToolTipText("Set the MultiSample (disable, 1x, 2x, 4x, 8x)")
		self.gui.SetVideoMode = env.addButton(recti( dim.Width - 60, 64, dim.Width - 10, 80), self.gui.Window, -1, "set")
		self.gui.SetVideoMode.setToolTipText("Set Video Mode with current values")
		env.addStaticText("Gamma:", recti(dim.Width - 400, 104, dim.Width - 310, 120),False, False, self.gui.Window, -1, False)
		self.gui.Gamma = env.addScrollBar(True, recti(dim.Width - 300, 104, dim.Width - 10, 120), self.gui.Window,-1)
		self.gui.Gamma.setMin(50)
		self.gui.Gamma.setMax(350)
		self.gui.Gamma.setSmallStep(1)
		self.gui.Gamma.setLargeStep(10)
		self.gui.Gamma.setPos(self.Game.GammaValue * 100.0)
		self.gui.Gamma.setToolTipText("Adjust Gamma Ramp ( 0.5 - 3.5)" )
		self.Game.Device.setGammaRamp(self.Game.GammaValue, self.Game.GammaValue, self.Game.GammaValue, 0.0, 0.0)
		env.addStaticText("Tesselation:", recti(dim.Width - 400, 124, dim.Width - 310, 140),False, False, self.gui.Window, -1, False)
		self.gui.Tesselation = env.addScrollBar(True, recti( dim.Width - 300, 124, dim.Width - 10, 140), self.gui.Window, -1)
		self.gui.Tesselation.setMin(2)
		self.gui.Tesselation.setMax(12)
		self.gui.Tesselation.setSmallStep(1)
		self.gui.Tesselation.setLargeStep(1)
		self.gui.Tesselation.setPos(self.Game.loadParam.patchTesselation )
		self.gui.Tesselation.setToolTipText("How smooth should curved surfaces be rendered")
		self.gui.Collision = env.addCheckBox(True, recti( dim.Width - 400, 150, dim.Width - 300, 166), self.gui.Window, -1, "Collision")
		self.gui.Collision.setToolTipText("Set collision on or off ( flythrough ). \nPress F7 on your Keyboard")
		self.gui.Visible_Map = env.addCheckBox(True, recti( dim.Width - 300, 150, dim.Width - 240, 166), self.gui.Window, -1, "Map")
		self.gui.Visible_Map.setToolTipText("Show or not show the static part the Level. \nPress F3 on your Keyboard")
		self.gui.Visible_Shader = env.addCheckBox(True, recti( dim.Width - 240, 150, dim.Width - 170, 166), self.gui.Window, -1, "Shader")
		self.gui.Visible_Shader.setToolTipText("Show or not show the Shader Nodes. \nPress F4 on your Keyboard")
		self.gui.Visible_Fog = env.addCheckBox(True, recti( dim.Width - 170, 150, dim.Width - 110, 166), self.gui.Window, -1, "Fog")
		self.gui.Visible_Fog.setToolTipText("Show or not show the Fog Nodes. \nPress F5 on your Keyboard")
		self.gui.Visible_Unresolved = env.addCheckBox(True, recti( dim.Width - 110, 150, dim.Width - 10, 166), self.gui.Window,-1, "Unresolved")
		self.gui.Visible_Unresolved.setToolTipText("Show the or not show the Nodes the Engine can't handle. \nPress F6 on your Keyboard")
		self.gui.Visible_Skydome = env.addCheckBox(True, recti(dim.Width - 110, 180, dim.Width - 10, 196), self.gui.Window,-1, "Skydome")
		self.gui.Visible_Skydome.setToolTipText("Show the or not show the Skydome.")
		self.gui.Respawn = env.addButton(recti(dim.Width - 260, 90, dim.Width - 10, 106), None, -1, "Respawn")
		env.addStaticText("Archives:", recti(5, dim.Height - 530, dim.Width - 600,dim.Height - 514),False, False, self.gui.Window, -1, False)
		self.gui.ArchiveAdd = env.addButton(recti(dim.Width - 725, dim.Height - 530, dim.Width - 665, dim.Height - 514), self.gui.Window,-1, "add")
		self.gui.ArchiveAdd.setToolTipText("Add an archive, usually packed zip-archives (*.pk3) to the Filesystem")
		self.gui.ArchiveRemove = env.addButton(recti(dim.Width - 660, dim.Height - 530, dim.Width - 600, dim.Height - 514), self.gui.Window,-1, "del")
		self.gui.ArchiveRemove.setToolTipText("Remove the selected archive from the FileSystem.")
		self.gui.ArchiveUp = env.addButton(recti(dim.Width - 575, dim.Height - 530, dim.Width - 515, dim.Height - 514), self.gui.Window,-1, "up")
		self.gui.ArchiveUp.setToolTipText("Arrange Archive Look-up Hirachy. Move the selected Archive up")
		self.gui.ArchiveDown = env.addButton(recti(dim.Width - 510, dim.Height - 530, dim.Width - 440, dim.Height - 514), self.gui.Window,-1, "down")
		self.gui.ArchiveDown.setToolTipText("Arrange Archive Look-up Hirachy. Move the selected Archive down")
		self.gui.ArchiveList = env.addTable(recti(5,dim.Height - 510, dim.Width - 450,dim.Height - 410), self.gui.Window)
		self.gui.ArchiveList.addColumn("Type", 0)
		self.gui.ArchiveList.addColumn("Real File Path", 1)
		self.gui.ArchiveList.setColumnWidth(0, 60)
		self.gui.ArchiveList.setColumnWidth(1, 284)
		self.gui.ArchiveList.setToolTipText("Show the attached Archives")
		env.addStaticText("Maps:", recti(5, dim.Height - 400, dim.Width - 450,dim.Height - 380), False, False, self.gui.Window, -1, False)
		self.gui.MapList = env.addListBox(recti(5,dim.Height - 380, dim.Width - 450,dim.Height - 40), self.gui.Window, -1, True)
		self.gui.MapList.setToolTipText("Show the current Maps in all Archives.\n Double-Click the Map to start the level")
		# create a visible Scene Tree
		env.addStaticText("Scenegraph:", recti(dim.Width - 400, dim.Height - 400, dim.Width - 5,dim.Height - 380 ), False, False, self.gui.Window, -1, False)
		self.gui.SceneTree = env.addTreeView(recti(dim.Width - 400, dim.Height - 380, dim.Width - 5, dim.Height - 40), self.gui.Window, -1, True, True, False)
		self.gui.SceneTree.setToolTipText("Show the current Scenegraph")
		self.gui.SceneTree.getRoot().clearChilds()
		self.addSceneTreeItem(self.Game.Device.getSceneManager().getRootSceneNode(), self.gui.SceneTree.getRoot())
		imageList = env.createImageList(driver.getTexture("iconlist.png"), dimension2di(32, 32), True)
		if imageList:
			self.gui.SceneTree.setImageList(imageList)
			imageList.drop()
		# load the engine logo
		self.gui.Logo = env.addImage(driver.getTexture("irrlichtlogo3.png"), position2di(5, 16), True, None)
		self.gui.Logo.setToolTipText("The great Irrlicht Engine")
		self.AddArchive("")

	def AddArchive(self, archiveName):
		fs = self.Game.Device.getFileSystem()
		if archiveName:
			exists = False
			for i in range(fs.getFileArchiveCount()):
				if fs.getFileArchive(i).getFileList().getPath() == archiveName:
					exists = True
					break
			if not exists:
				fs.addFileArchive(archiveName, True, False)
		# store the current archives in game data
		# show the attached Archive in proper order
		if self.gui.ArchiveList:
			self.gui.ArchiveList.clearRows()
			for i in range(fs.getFileArchiveCount()):
				archive = fs.getFileArchive(i)
				index = self.gui.ArchiveList.addRow(i)
				typeName = 'archive'
				archive_type = archive.getType()
				if archive_type == EFAT_ZIP:
					typeName = "ZIP"
					break
				elif archive_type == EFAT_GZIP:
					typeName = "gzip"
					break
				elif archive_type == EFAT_FOLDER:
					typeName = "Mount"
					break
				elif archive_type == EFAT_PAK:
					typeName = "PAK"
					break
				elif archive_type == EFAT_TAR:
					typeName = "TAR"
					break
				self.gui.ArchiveList.setCellText(index, 0, typeName)
				self.gui.ArchiveList.setCellText(index, 1, archive.getFileList().getPath())
		# browse the archives for maps
		if self.gui.MapList:
			self.gui.MapList.clear()
			self.bank = self.Game.Device.getGUIEnvironment().getSpriteBank("sprite_q3map")
			if not self.bank:
				self.bank = self.Game.Device.getGUIEnvironment().addEmptySpriteBank("sprite_q3map")
			self.sprite = SGUISprite()
			self.frame = SGUISpriteFrame()
			r = recti()
			self.bank.sprites_clear()
			self.bank.positions_clear()
			self.gui.MapList.setSpriteBank(self.bank)
			s = ''
			# browse the attached file system
			fs.setFileListSystem(FILESYSTEM_VIRTUAL)
			fs.changeWorkingDirectoryTo("/maps/")
			fileList = fs.createFileList()
			fs.setFileListSystem(FILESYSTEM_NATIVE)
			g = 0
			file_count = fileList.getFileCount()
			i = 0
			while i < file_count:
				s = fileList.getFullFileName(i)
				if s.find(".bsp") > -1:
					# get level screenshot. reformat texture to 128x128
					s = "levelshots/" + cutFilenameExtension(deletePathFromFilename(s))
					dim = dimension2du(128, 128)
					driver = self.Game.Device.getVideoDriver()
					image = None
					tex = None
					filename = s + ".jpg"
					if fs.existFile(filename):
						image = driver.createImageFromFile(filename)
					if 0 == image:
						filename = s + ".tga"
						if fs.existFile(filename):
							image = driver.createImageFromFile(filename)
					if image:
						filter = driver.createImage(ECF_R8G8B8, dim)
						image.copyToScalingBoxFilter(filter, 0)
						image.drop()
						image = filter
					if image:
						tex = driver.addTexture(filename, image)
						image.drop()
					self.bank.setTexture(g, tex)
					r.LowerRightCorner.X = dim.Width
					r.LowerRightCorner.Y = dim.Height
					self.gui.MapList.setItemHeight(r.LowerRightCorner.Y + 4)
					self.frame.rectNumber = self.bank.positions_size()
					self.frame.textureNumber = g
					self.bank.positions_push_back(r)
					self.sprite.frames_set_used(0)
					self.sprite.frames_push_back(self.frame)
					self.sprite.frameTime = 0
					self.bank.sprites_push_back(self.sprite)
					self.gui.MapList.addItem(s, g)
					g += 1
				i += 1
			fileList.drop()
			self.gui.MapList.setSelected(-1)
			bar = self.gui.MapList.getElementFromId(0).as_IGUIScrollBar()
			if bar:
				bar.setPos(0)


	def dropMap(self):
		driver = self.Game.Device.getVideoDriver()
		driver.removeAllHardwareBuffers()
		driver.removeAllTextures()
		self.Player[0].shutdown()
		dropElement(self.ItemParent)
		dropElement(self.ShaderParent)
		dropElement(self.UnresolvedParent)
		dropElement(self.FogParent)
		dropElement(self.BulletParent)
		self.Impacts.clear()
		if self.Meta:
			self.Meta = 0
		dropElement(self.MapParent)
		dropElement(self.SkyNode)
		# clean out meshes, because textures are invalid
		# TODO: better texture handling;-)
		cache = self.Game.Device.getSceneManager().getMeshCache()
		cache.clear()
		self.Mesh = None

	def LoadMap(self, mapName, collision):
		if 0 == mapName.size():
			return
		self.dropMap()
		fs = self.Game.Device.getFileSystem()
		smgr = self.Game.Device.getSceneManager()
		file = fs.createMemoryReadFile(self.Game.loadParam, len(self.Game.loadParam), "levelparameter.cfg", False)
		# load cfg file
		smgr.getMesh(file)
		file.drop()
		# load the actual map
		self.Mesh = smgr.getMesh(mapName)
		if not self.Mesh:
			return
		geometry = self.Mesh.getMesh(E_Q3_MESH_GEOMETRY)
		if not geometry and geometry.getMeshBufferCount() == 0:
			return
		self.Game.CurrentMapName = mapName
		#create a collision list
		self.Meta = None
		selector = None
		if collision:
			self.Meta = smgr.createMetaTriangleSelector()
		#IMeshBuffer *b0 = geometry.getMeshBuffer(0)
		#s32 minimalNodes = b0 ? core::s32_max ( 2048, b0.getVertexCount() / 32 ) : 2048
		minimalNodes = 2048
		self.MapParent = smgr.addOctreeSceneNode(geometry, 0, -1, minimalNodes)
		self.MapParent.setName(mapName)
		if self.Meta:
			selector = smgr.createOctreeTriangleSelector(geometry, MapParent, minimalNodes)
			#selector = smgr.createTriangleSelector ( geometry, MapParent )
			self.Meta.addTriangleSelector(selector)
			selector.drop()
		# logical parent for the items
		self.ItemParent = smgr.addEmptySceneNode()
		if self.ItemParent:
			self.ItemParent.setName("Item Container")
		self.ShaderParent = smgr.addEmptySceneNode()
		if self.ShaderParent:
			self.ShaderParent.setName("Shader Container")
		self.UnresolvedParent = smgr.addEmptySceneNode()
		if self.UnresolvedParent:
			self.UnresolvedParent.setName("Unresolved Container")
		self.FogParent = smgr.addEmptySceneNode()
		if self.FogParent:
			self.FogParent.setName("Fog Container")
		# logical parent for the bullets
		self.BulletParent = smgr.addEmptySceneNode()
		if self.BulletParent:
			self.BulletParent.setName("Bullet Container")
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_ITEMS, self.ShaderParent, self.Meta, False)
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_FOG, self.FogParent, 0, False)
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_UNRESOLVED, self.UnresolvedParent, self.Meta, True)
		Q3ModelFactory(self.Game.loadParam, self.Game.Device, self.Mesh, ItemParent, False)

	def addSceneTreeItem(self, parent, nodeParent):
		node = None
		msg = ''
		imageIndex = -1
		childrens = parent.get_childrens()
		childrens_count = len(childrens)
		idx_children = 0
		while idx_children < childrens_count:
			children = childrens[idx_children]
			idx_children += 1
			children_type = children.getType()
			if children_type == ESNT_Q3SHADER_SCENE_NODE: imageIndex = 0
			elif children_type == ESNT_CAMERA: imageIndex = 1
			elif children_type == ESNT_EMPTY: imageIndex = 2
			elif children_type == ESNT_MESH: imageIndex = 3
			elif children_type == ESNT_OCTREE: imageIndex = 3
			elif children_type == ESNT_ANIMATED_MESH: imageIndex = 4
			elif children_type == ESNT_SKY_BOX: imageIndex = 5
			elif children_type == ESNT_BILLBOARD: imageIndex = 6
			elif children_type == ESNT_PARTICLE_SYSTEM: imageIndex = 7
			elif children_type == ESNT_TEXT: imageIndex = 8
			if imageIndex < 0:
				msg = "%hs,%hs" % (self.Game.Device.getSceneManager().getSceneNodeTypeName(children_type), children.getName())
			else:
				msg = "%hs" % children.getName()
			node = nodeParent.addChildBack(msg, None, imageIndex)
			# Add all Animators
			animators = children.get_animators()
			animators_count = len(animators)
			idx_animator = 0
			while idx_animator < animators_count:
				animator = animators[idx_animator]
				idx_animator += 1
				imageIndex = -1
				animator_type  = animator.getType()
				msg = "%hs" % self.Game.Device.getSceneManager().getAnimatorTypeName(animator_type)
				if animator_type == ESNAT_FLY_CIRCLE: pass
				elif animator_type == ESNAT_FLY_STRAIGHT: pass
				elif animator_type == ESNAT_FOLLOW_SPLINE: pass
				elif animator_type == ESNAT_ROTATION: pass
				elif animator_type == ESNAT_TEXTURE: pass
				elif animator_type == ESNAT_DELETION: pass
				elif animator_type == ESNAT_COLLISION_RESPONSE: pass
				elif animator_type == ESNAT_CAMERA_FPS: pass
				elif animator_type == ESNAT_CAMERA_MAYA: pass
				node.addChildBack(msg, None, imageIndex)
			self.addSceneTreeItem(children, node)

	# Adds life!
	def CreatePlayers(self):
		self.Player[0].create(self.Game.Device, self.Mesh, self.MapParent, self.Meta)

	# Adds a skydome to the scene
	def AddSky(self, dome, texture):
		smgr = self.Game.Device.getSceneManager()
		driver = self.Game.Device.getVideoDriver()
		oldMipMapState = driver.getTextureCreationFlag(ETCF_CREATE_MIP_MAPS)
		driver.setTextureCreationFlag(ETCF_CREATE_MIP_MAPS, False)
		if 0 == dome:
			p = ("ft", "rt", "bk", "lf", "up", "dn")
			i = 0
			buf = "%s_%s.jpg" % (texture, p[i])
			self.SkyNode = smgr.addSkyBoxSceneNode(driver.getTexture(buf), 0, 0, 0, 0, 0)
			if self.SkyNode:
				for i in range(6):
					buf = "%s_%s.jpg" % (texture, p[i])
					self.SkyNode.getMaterial(i).setTexture(0, driver.getTexture(buf))
		else:
			if 1 == dome:
				buf = "%s.jpg" % texture
				self.SkyNode = smgr.addSkyDomeSceneNode(driver.getTexture(buf), 32, 32, 1.0, 1.0, 1000.0, None, 11)
			else:
				if 2 == dome:
					buf = "%s.jpg" % texture
					self.SkyNode = smgr.addSkyDomeSceneNode(driver.getTexture(buf), 16, 8, 0.95, 2.0, 1000.0, None, 11)
			if self.SkyNode:
				self.SkyNode.setName("Skydome")
			#self.SkyNode.getMaterial(0).ZBuffer = EMDF_DEPTH_LESS_EQUAL
			driver.setTextureCreationFlag(ETCF_CREATE_MIP_MAPS, oldMipMapState)

	# enable GUI elements
	def SetGUIActive(self, command):
		inputState = False
		camera = self.Game.Device.getSceneManager().getActiveCamera()
		if command == 0:
			self.Game.guiActive = 0
			inputState = not self.Game.guiActive
		elif command == 1:
			self.Game.guiActive = 1
			inputState = not self.Game.guiActive
		elif command == 2:
			self.Game.guiActive ^= 1
			inputState = not self.Game.guiActivebreak
		elif command == 3:
			if camera:
				inputState = not camera.isInputReceiverEnabled()
		if camera:
			camera.setInputReceiverEnabled(inputState)
			self.Game.Device.getCursorControl().setVisible(not inputState)
		if self.gui.Window:
			self.gui.Window.setVisible(self.Game.guiActive != 0)
		if self.Game.guiActive and self.gui.SceneTree and self.Game.Device.getGUIEnvironment().getFocus() != self.gui.SceneTree:
			self.gui.SceneTree.getRoot().clearChilds()
			self.addSceneTreeItem(self.Game.Device.getSceneManager().getRootSceneNode(), self.gui.SceneTree.getRoot())
		w = None
		if self.Game.guiActive:
			w = self.gui.Window
		self.Game.Device.getGUIEnvironment().setFocus(w)

	def OnEvent(self, event):
		#~ print "=== OnEvent", event.EventType, EET_LOG_TEXT_EVENT, EET_MOUSE_INPUT_EVENT, EET_GUI_EVENT
		#~ self.Game.Device.getLogger().log("=== OnEvent")
		if event.EventType == EET_LOG_TEXT_EVENT:
			return False
		if self.Game.guiActive and event.EventType == EET_GUI_EVENT:
			#~ gui_event_type = event.GUIEvent.EventType
			#~ caller = event.GUIEvent.Caller
			gui_event_type = self.GUIEvent_EventType(event.GUIEvent)
			caller = self.GUIEvent_Caller(event.GUIEvent)
			#~ print caller.getType(), caller.getTypeName(), gui_event_type, EGET_ELEMENT_FOCUSED
			#~ if repr(self.GUIEvent_Caller(event.GUIEvent).as_IGUIListBox()) == repr(self.gui.MapList.as_IGUIListBox()) and gui_event_type == EGET_LISTBOX_SELECTED_AGAIN:
			if caller.getType() == self.gui.MapList.getType() and gui_event_type == EGET_LISTBOX_SELECTED_AGAIN:
				caller = caller.as_IGUIListBox()
				selected = self.gui.MapList.getSelected()
				if selected >= 0:
					loadMap = self.gui.MapList.getListItem(selected)
					if not self.MapParent or loadMap != self.Game.CurrentMapName:
						self.Game.Device.getLogger().log("Loading map %ls\n" % loadMap, ELL_INFORMATION)
						self.LoadMap(loadMap, 1)
						if not self.Game.loadParam.loadSkyShader:
							self.AddSky(1, "skydome2")
						self.CreatePlayers()
						self.CreateGUI()
						self.SetGUIActive(0)
						return True
			elif caller.getType() == self.gui.ArchiveRemove.getType() and gui_event_type == EGET_BUTTON_CLICKED:
				self.Game.Device.getFileSystem().removeFileArchive(self.gui.ArchiveList.getSelected())
				self.Game.CurrentMapName = ""
				self.AddArchive("")
			elif caller.getType() == self.gui.ArchiveAdd.getType() and gui_event_type == EGET_BUTTON_CLICKED:
				if not self.gui.ArchiveFileOpen:
					self.Game.Device.getFileSystem().setFileListSystem(FILESYSTEM_NATIVE)
					self.gui.ArchiveFileOpen = self.Game.Device.getGUIEnvironment().addFileOpenDialog("Add Game Archive", False, self.gui.Window)
			elif caller.getType() == EGUIET_FILE_OPEN_DIALOG and gui_event_type == EGET_FILE_SELECTED:
				self.AddArchive(self.gui.ArchiveFileOpen.getFileName())
				self.gui.ArchiveFileOpen = None
			elif caller.getType() == EGUIET_FILE_OPEN_DIALOG and gui_event_type == EGET_DIRECTORY_SELECTED:
				self.AddArchive(self.gui.ArchiveFileOpen.getDirectoryName())
			elif caller.getType() == EGUIET_FILE_OPEN_DIALOG and gui_event_type == EGET_FILE_CHOOSE_DIALOG_CANCELLED:
				self.gui.ArchiveFileOpen = None
			elif (caller.getType() == self.gui.ArchiveUp.getType() or caller.getType() == self.gui.ArchiveDown.getType()) and gui_event_type == EGET_BUTTON_CLICKED:
				rel = 1
				if caller.getType() == self.gui.ArchiveUp.getType():
					rel = -1
				if self.Game.Device.getFileSystem().moveFileArchive(self.gui.ArchiveList.getSelected(), rel):
					newIndex = min(max(self.gui.ArchiveList.getSelected() + rel, 0), self.gui.ArchiveList.getRowCount() - 1)
					AddArchive('')
					self.gui.ArchiveList.setSelected(newIndex)
					self.Game.CurrentMapName = ''
			elif caller.getType() == self.gui.VideoDriver.getType() and gui_event_type == EGET_COMBO_BOX_CHANGED:
				self.Game.deviceParam.DriverType = gui.VideoDriver.getItemData(self.gui.VideoDriver.getSelected())
			elif caller.getType() == self.gui.VideoMode.getType() and gui_event_type == EGET_COMBO_BOX_CHANGED:
				val = self.gui.VideoMode.getItemData(self.gui.VideoMode.getSelected())
				self.Game.deviceParam.WindowSize.Width = val >> 16
				self.Game.deviceParam.WindowSize.Height = val & 0xFFFF
			elif caller.getType() == self.gui.FullScreen.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				self.Game.deviceParam.Fullscreen = self.gui.FullScreen.isChecked()
			elif caller.getType() == self.gui.Bit32.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				self.Game.deviceParam.Bits = 16
				if self.gui.Bit32.isChecked():
					self.Game.deviceParam.Bits = 32
			elif caller.getType() == self.gui.MultiSample.getType() and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.deviceParam.AntiAlias = self.gui.MultiSample.getPos()
			elif caller.getType() == self.gui.Tesselation.getType() and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.loadParam.patchTesselation = self.gui.Tesselation.getPos()
			elif caller.getType() == self.gui.Gamma.getType() and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.GammaValue = self.gui.Gamma.getPos() * 0.01
				self.Game.Device.setGammaRamp(self.Game.GammaValue, self.Game.GammaValue, self.Game.GammaValue, 0.0, 0.0)
			elif caller.getType() == self.gui.SetVideoMode.getType() and gui_event_type == EGET_BUTTON_CLICKED:
				self.Game.retVal = 2
				self.Game.Device.closeDevice()
			elif caller.getType() == self.gui.Window.getType() and gui_event_type == EGET_ELEMENT_CLOSED:
				self.Game.Device.closeDevice()
			elif caller.getType() == self.gui.Collision.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				# set fly through active
				self.Game.flyTroughState ^= 1
				self.Player[0].cam().setAnimateTarget(Game.flyTroughState == 0)
				self.Game.Device.getLogger().log("collision %d\n" % bool(Game.flyTroughState == 0), ELL_INFORMATION)
			elif caller.getType() == self.gui.Visible_Map.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				v = self.gui.Visible_Map.isChecked()
				if self.MapParent:
					self.Game.Device.getLogger().log("static node set visible %d\n" % v, ELL_INFORMATION)
					self.MapParent.setVisible(v)
			elif caller.getType() == self.gui.Visible_Shader.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				v = self.gui.Visible_Shader.isChecked()
				if self.ShaderParent:
					self.Game.Device.getLogger().log("shader node set visible %d\n" % v, ELL_INFORMATION)
					self.ShaderParent.setVisible(v)
			elif caller.getType() == self.gui.Visible_Skydome.getType() and gui_event_type == EGET_CHECKBOX_CHANGED:
				if self.SkyNode:
					v = not self.SkyNode.isVisible()
					self.Game.Device.getLogger().log("skynode set visible %d\n" % v, ELL_INFORMATION)
					self.SkyNode.setVisible(v)
			elif caller.getType() == self.gui.Respawn.getType() and gui_event_type == EGET_BUTTON_CLICKED:
				self.Player[0].respawn()
			return False

		# fire
		#~ if ((event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_SPACE and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and event.MouseInput.Event == EMIE_LMOUSE_LEFT_UP)):
		if ((event.EventType == EET_KEY_INPUT_EVENT and self.KeyInput_Key(event.KeyInput) == KEY_SPACE and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and self.MouseInput_EventType(event.MouseInput) == EMIE_LMOUSE_LEFT_UP)):
			camera = self.Game.Device.getSceneManager().getActiveCamera()
			if camera and camera.isInputReceiverEnabled():
				self.useItem(self.Player[0])
		# gui active
		#~ if (event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_F1 and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and event.MouseInput.Event == EMIE_RMOUSE_LEFT_UP):
		if (event.EventType == EET_KEY_INPUT_EVENT and self.KeyInput_Key(event.KeyInput) == KEY_F1 and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and self.MouseInput_EventType(event.MouseInput) == EMIE_RMOUSE_LEFT_UP):
			self.SetGUIActive(2)
		# check if user presses the key
		if event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.PressedDown == False:
			# Escape toggles camera Input
			#~ if event.KeyInput.Key == KEY_ESCAPE:
			if self.KeyInput_Key(event.KeyInput) == KEY_ESCAPE:
				self.SetGUIActive(3)
			else:
				#~ if event.KeyInput.Key == KEY_F11:
				if self.KeyInput_Key(event.KeyInput) == KEY_F11:
					# screenshot are taken without gamma!
					image = self.Game.Device.getVideoDriver().createScreenShot()
					if image:
						pos = vector3df()
						rot = vector3df()
						cam = self.Game.Device.getSceneManager().getActiveCamera()
						if cam:
							pos = cam.getPosition()
							rot = cam.getRotation()
						dName = ("null", "software", "burning", "d3d8", "d3d9", "opengl")
						buf = "%s_%ls_%.0f_%.0f_%.0f_%.0f_%.0f_%.0f.jpg" % (dName[self.Game.Device.getVideoDriver().getDriverType()], self.Game.CurrentMapName, pos.X, pos.Y, pos.Z, rot.X, rot.Y, rot.Z)
						filename = buf
						filename.replace('/', '_')
						self.Game.Device.getLogger().log("screenshot : %s\n" % filename, ELL_INFORMATION)
						self.Game.Device.getVideoDriver().writeImageToFile(image, filename, 100)
						image.drop()
				else:
					#~ if event.KeyInput.Key == KEY_F9:
					if self.KeyInput_Key(event.KeyInput) == KEY_F9:
						value = EDS_OFF
						self.Game.debugState = (self.Game.debugState + 1) & 3
						if self.Game.debugState == 1: value = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_BBOX_ALL
						elif self.Game.debugState == 2: value = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_SKELETON
						# set debug map data on/off
						if debugState == EDS_OFF:
							debugState = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_BBOX_ALL
						else:
							debugState = EDS_OFF
						if self.ItemParent:
							for it in self.ItemParent.getChildren():
								it.setDebugDataVisible(value)
						if self.ShaderParent:
							for it in self.ShaderParent.getChildren():
								it.setDebugDataVisible(value)
						if self.UnresolvedParent:
							for it in self.UnresolvedParent.getChildren():
								it.setDebugDataVisible(value)
						if self.FogParent:
							for it in self.FogParent.getChildren():
								it.setDebugDataVisible(value)
						if self.SkyNode:
							self.SkyNode.setDebugDataVisible(value)
					else:
						#~ if event.KeyInput.Key == KEY_F8:
						if self.KeyInput_Key(event.KeyInput) == KEY_F8:
							# set gravity on/off
							self.Game.gravityState ^= 1
							gravity_state = "none"
							if self.Game.gravityState:
								gravity_state = "earth"
							self.Player[0].cam().setGravity(self.getGravity(gravity_state))
							self.Game.Device.getLogger().log("gravity %s\n" % gravity_state, ELL_INFORMATION)
						else:
							#~ if event.KeyInput.Key == KEY_F7:
							if self.KeyInput_Key(event.KeyInput) == KEY_F7:
								# set fly through active
								self.Game.flyTroughState ^= 1
								self.Player[0].cam().setAnimateTarget(self.Game.flyTroughState == 0)
								if self.gui.Collision:
									self.gui.Collision.setChecked(self.Game.flyTroughState == 0)
								self.Game.Device.getLogger().log("collision %d\n" % bool(Game.flyTroughState == 0), ELL_INFORMATION)
							else:
								#~ if event.KeyInput.Key == KEY_F2:
								if self.KeyInput_Key(event.KeyInput) == KEY_F2:
									self.Player[0].respawn()
								else:
									#~ if event.KeyInput.Key == KEY_F3:
									if self.KeyInput_Key(event.KeyInput) == KEY_F3:
										if self.MapParent:
											v = not self.MapParent.isVisible()
											self.Game.Device.getLogger().log("static node set visible %d\n" % v, ELL_INFORMATION)
											self.MapParent.setVisible(v)
											if self.gui.Visible_Map:
												self.gui.Visible_Map.setChecked(v)
									else:
										#~ if event.KeyInput.Key == KEY_F4:
										if self.KeyInput_Key(event.KeyInput) == KEY_F4:
											if self.ShaderParent:
												v = not self.ShaderParent.isVisible()
												self.Game.Device.getLogger().log("shader node set visible %d\n" % v, ELL_INFORMATION)
												self.ShaderParent.setVisible(v)
												if self.gui.Visible_Shader:
													self.gui.Visible_Shader.setChecked(v)
										else:
											#~ if event.KeyInput.Key == KEY_F5:
											if self.KeyInput_Key(event.KeyInput) == KEY_F5:
												if self.FogParent:
													v = not self.FogParent.isVisible()
													self.Game.Device.getLogger().log("fog node set visible %d\n" % v, ELL_INFORMATION)
													self.FogParent.setVisible(v)
													if self.gui.Visible_Fog:
														self.gui.Visible_Fog.setChecked(v)
											else:
												#~ if event.KeyInput.Key == KEY_F6:
												if self.KeyInput_Key(event.KeyInput) == KEY_F6:
													if self.UnresolvedParent:
														v = not self.UnresolvedParent.isVisible()
														self.Game.Device.getLogger().log("unresolved node set visible %d\n" % v, ELL_INFORMATION)
														self.UnresolvedParent.setVisible(v)
														if self.gui.Visible_Unresolved:
															self.gui.Visible_Unresolved.setChecked(v)
		# check if user presses the key C ( for crouch)
		#~ if event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_KEY_C:
		if event.EventType == EET_KEY_INPUT_EVENT and self.KeyInput_Key(event.KeyInput) == KEY_KEY_C:
			# crouch
			anim = self.Player[0].cam()
			if anim and 0 == self.Game.flyTroughState:
				if False == event.KeyInput.PressedDown:
					# stand up
					anim.setEllipsoidRadius(vector3df(30,45,30))
					anim.setEllipsoidTranslation(vector3df(0,40,0))
				else:
					# on your knees
					anim.setEllipsoidRadius(vector3df(30,20,30))
					anim.setEllipsoidTranslation(vector3df(0,20,0))
				return True
		return False

	def useItem(self, player):
		smgr = self.Game.Device.getSceneManager()
		camera = smgr.getActiveCamera()
		if not camera:
			return
		imp = SParticleImpact()
		imp.when = 0
		start = camera.getPosition()
		if player.WeaponNode:
			start.X += 0.0
			start.Y += 0.0
			start.Z += 0.0
		end = vector3df(camera.getTarget() - start)
		end.normalize()
		start += end * 20.0
		end = start + (end * camera.getFarValue())
		triangle = triangle3df()
		line = line3df(start, end)
		hitNode = None
		if smgr.getSceneCollisionManager().getCollisionPoint(line, self.Meta, end, triangle, hitNode):
			out = triangle.getNormal()
			out.setLength(0.03)
			imp.when = 1
			imp.outVector = out
			imp.pos = end
			player.setAnim("pow")
			player.Anim[1].next += player.Anim[1].delta
		else:
			start = camera.getPosition()
			#~ if player.WeaponNode:
				#start.X += 10.0
				#start.Y += -5.0
				#start.Z += 1.0
			end = vector3df(camera.getTarget() - start)
			end.normalize()
			start += end*20.0
			end = start + (end * camera.getFarValue())
		node = smgr.addBillboardSceneNode(self.BulletParent, dimension2df(10, 10), start)
		node.setMaterialFlag(EMF_LIGHTING, False)
		node.setMaterialTexture(0, self.Game.Device.getVideoDriver().getTexture("fireball.bmp"))
		node.setMaterialFlag(EMF_ZWRITE_ENABLE, False)
		node.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
		length = (end - start).getLength()
		speed = 5.8
		time = length / speed
		anim = smgr.createFlyStraightAnimator(start, end, time)
		node.addAnimator(anim)
		anim.drop()
		bullet = "nohit"
		if imp.when:
			bullet = "hit"
		buf = "bullet: %s on %.1f,%1.f,%1.f" % (bullet, end.X, end.Y, end.Z)
		node.setName(buf)
		anim = smgr.createDeleteAnimator(time)
		node.addAnimator(anim)
		anim.drop()
		if imp.when:
			imp.when = self.Game.Device.getTimer().getTime() + (time + (1.0 + getNoiser()) * 250.0)
			self.Impacts.append(imp)

	# rendered when bullets hit something
	def createParticleImpacts(self, now):
		sm = self.Game.Device.getSceneManager()
		class smokeLayer:
			def __init__(self, *args):
				self.texture = args[0]
				self.scale = args[1]
				self.minparticleSize = args[2]
				self.maxparticleSize = args[3]
				self.boxSize = args[4]
				self.minParticle = args[5]
				self.maxParticle = args[6]
				self.fadeout = args[7]
				self.lifetime = args[8]
		smoke = (smokeLayer("smoke2.jpg", 0.4, 1.5, 18.0, 20.0, 20, 50, 2000, 10000), smokeLayer("smoke3.jpg", 0.2, 1.2, 15.0, 20.0, 10, 30, 1000, 12000))
		i = 0
		g = 0
		factor = 1
		for g in range(2):
			smoke[g].minParticle *= factor
			smoke[g].maxParticle *= factor
			smoke[g].lifetime *= factor
			smoke[g].boxSize *= getNoiser() * 0.5
		for i in range(len(self.Impacts)):
			if now < self.Impacts[i].when:
				continue
			# create smoke particle system
			pas = None
			for g in range(2):
				pas = sm.addParticleSystemSceneNode(False, self.BulletParent, -1, self.Impacts[i].pos)
				buf = "bullet impact smoke at %.1f,%.1f,%1.f" % (self.Impacts[i].pos.X, self.Impacts[i].pos.Y, self.Impacts[i].pos.Z)
				pas.setName(buf)
				# create a flat smoke
				direction = self.Impacts[i].outVector
				direction *= smoke[g].scale
				em = pas.createBoxEmitter(aabbox3df(-4.0, 0.0, -4.0, 20.0, smoke[g].minparticleSize, 20.0), direction, smoke[g].minParticle, smoke[g].maxParticle, SColor(0,0,0,0), SColor(0,128,128,128), 250, 4000, 60)
				em.setMinStartSize(dimension2df(smoke[g].minparticleSize, smoke[g].minparticleSize))
				em.setMaxStartSize(dimension2df(smoke[g].maxparticleSize, smoke[g].maxparticleSize))
				pas.setEmitter(em)
				em.drop()
				# particles get invisible
				paf = pas.createFadeOutParticleAffector(SColor(0, 0, 0, 0), smoke[g].fadeout)
				pas.addAffector(paf)
				paf.drop()
				# particle system life time
				anim = sm.createDeleteAnimator(smoke[g].lifetime)
				pas.addAnimator(anim)
				anim.drop()
				pas.setMaterialFlag(EMF_LIGHTING, False)
				pas.setMaterialFlag(EMF_ZWRITE_ENABLE, False)
				pas.setMaterialType(EMT_TRANSPARENT_VERTEX_ALPHA )
				pas.setMaterialTexture(0, self.Game.Device.getVideoDriver().getTexture(smoke[g].texture))
			# play impact sound
			#ifdef USE_IRRKLANG
			#~ if irrKlang:
				#~ audio::ISound* sound = irrKlang.play3D(impactSound, Impacts[i].pos, False, False, True)
				#~ if sound:
					#~ # adjust max value a bit to make to sound of an impact louder
					#~ sound.setMinDistance(400)
					#~ sound.drop()
			#endif
			# delete entry
			self.Impacts.erase(i)
			i -= 1

	def Render(self):
		driver = self.Game.Device.getVideoDriver()
		if 0 == driver:
			return
		scolor = SColor(0,0,0,0)
		driver.beginScene(True, True, scolor)
		# TODO: This does not work, yet.
		anaglyph = False
		if anaglyph:
			cameraOld = self.Game.Device.getSceneManager().getActiveCamera()
			driver.getOverrideMaterial().Material.ColorMask = ECP_NONE
			driver.getOverrideMaterial().EnableFlags  = EMF_COLOR_MASK
			driver.getOverrideMaterial().EnablePasses = ESNRP_SKY_BOX + ESNRP_SOLID + ESNRP_TRANSPARENT + ESNRP_TRANSPARENT_EFFECT + ESNRP_SHADOW
			self.Game.Device.getSceneManager().drawAll()
			driver.clearZBuffer()
			oldPosition = cameraOld.getPosition()
			oldTarget = cameraOld.getTarget()
			startMatrix = cameraOld.getAbsoluteTransformation()
			focusPoint = (oldTarget - cameraOld.getAbsolutePosition()).setLength(10000) + cameraOld.getAbsolutePosition()
			camera = cameraOld#self.Game.Device.getSceneManager().addCameraSceneNode()
			#Left eye...
			pos = vector3df()
			move = matrix4()
			move.setTranslation(vector3df(-1.5,0.0,0.0))
			pos = (startMatrix*move).getTranslation()
			driver.getOverrideMaterial().Material.ColorMask = ECP_RED
			driver.getOverrideMaterial().EnableFlags = EMF_COLOR_MASK
			driver.getOverrideMaterial().EnablePasses = ESNRP_SKY_BOX|ESNRP_SOLID|ESNRP_TRANSPARENT|ESNRP_TRANSPARENT_EFFECT|ESNRP_SHADOW
			camera.setPosition(pos)
			camera.setTarget(focusPoint)
			self.Game.Device.getSceneManager().drawAll()
			driver.clearZBuffer()
			#Right eye...
			move.setTranslation(vector3df(1.5,0.0,0.0))
			pos = (startMatrix*move).getTranslation()
			driver.getOverrideMaterial().Material.ColorMask = ECP_GREEN + ECP_BLUE
			driver.getOverrideMaterial().EnableFlags = EMF_COLOR_MASK
			driver.getOverrideMaterial().EnablePasses = ESNRP_SKY_BOX|ESNRP_SOLID|ESNRP_TRANSPARENT|ESNRP_TRANSPARENT_EFFECT|ESNRP_SHADOW
			camera.setPosition(pos)
			camera.setTarget(focusPoint)
			self.Game.Device.getSceneManager().drawAll()
			driver.getOverrideMaterial().Material.ColorMask = ECP_ALL
			driver.getOverrideMaterial().EnableFlags = 0
			driver.getOverrideMaterial().EnablePasses = 0
			if camera != cameraOld:
				self.Game.Device.getSceneManager().setActiveCamera(cameraOld)
				camera.remove()
			else:
				camera.setPosition(oldPosition)
				camera.setTarget(oldTarget)
		else:
			self.Game.Device.getSceneManager().drawAll()
		self.Game.Device.getGUIEnvironment().drawAll()
		driver.endScene()

	def Animate(self):
		now = self.Game.Device.getTimer().getTime()
		player = self.Player[0]
		checkTimeFire(player.Anim, 4, now)
		# Query Scene Manager attributes
		if player.Anim[0].flags & FIRED:
			smgr = self.Game.Device.getSceneManager()
			driver = self.Game.Device.getVideoDriver()
			attr = smgr.getParameters()
			msg = "Q3 %s [%ls], FPS:%03d Tri:%.03fm Cull %d/%d nodes (%d,%d,%d)" % (self.Game.CurrentMapName, driver.getName(), driver.getFPS(), driver.getPrimitiveCountDrawn(0) * (1.0 / 1000000.0), attr.getAttributeAsInt("culled"), attr.getAttributeAsInt("calls"), attr.getAttributeAsInt("drawn_solid"), attr.getAttributeAsInt("drawn_transparent"), attr.getAttributeAsInt("drawn_transparent_effect"))
			self.Game.Device.setWindowCaption(msg)
			msg = "%03d fps, F1 GUI on/off, F2 respawn, F3-F6 toggle Nodes, F7 Collision on/off, F8 Gravity on/off, Right Mouse Toggle GUI" % self.Game.Device.getVideoDriver().getFPS()
			if self.gui.StatusLine:
				self.gui.StatusLine.setText(msg)
			player.Anim[0].flags &= ~FIRED
		# idle..
		if player.Anim[1].flags & FIRED:
			if player.animation == "idle":
				player.setAnim("idle")
			player.Anim[1].flags &= ~FIRED
		self.createParticleImpacts(now)


def runGame(game):
	if game.retVal >= 3:
		return

	#~ game.Device = game.createExDevice(game.deviceParam)
	game.Device = createDevice(EDT_OPENGL, dimension2du(800, 600), 16)
	if not game.Device:
		# could not create selected driver.
		game.retVal = 0
		return

	# create an event receiver based on current game data
	eventHandler = CQuake3EventHandler()
	eventHandler.init_game(game)

	# load stored config
	game.load("explorer.cfg")

	# add our media directory and archive to the file system
	for i in range(len(game.CurrentArchiveList)):
		eventHandler.AddArchive(game.CurrentArchiveList[i])

	# Load a Map or startup to the GUI
	if game.CurrentMapName:
		eventHandler.LoadMap(game.CurrentMapName, 1)
		if 0 == game.loadParam.loadSkyShader:
			eventHandler.AddSky(1, "skydome2")
		eventHandler.CreatePlayers()
		eventHandler.CreateGUI()
		eventHandler.SetGUIActive(0)

		# set player to last position on restart
		if game.retVal == 2:
			eventHandler.GetPlayer(0).setpos(game.PlayerPosition, game.PlayerRotation)
	else:
		# start up empty
		eventHandler.AddSky(1, "skydome2")
		eventHandler.CreatePlayers()
		eventHandler.CreateGUI()
		eventHandler.SetGUIActive(1)
		#~ background_music("IrrlichtTheme.ogg")

	game.retVal = 3
	#~ game.Device.getLogger().log('===' + str(game.retVal) + ' == ' + str(game.Device), ELL_INFORMATION)
	#~ try:
		#~ game.Device.run()
	#~ except:
		#~ game.Device.getLogger().log('=== ERROR GAME DEVICE RUN', ELL_INFORMATION)
	while game.Device.run():
		eventHandler.Animate()
		eventHandler.Render()
		if not game.Device.isWindowActive():
			game.Device._yield()

	game.Device.setGammaRamp(1.0, 1.0, 1.0, 0.0, 0.0)
	eventHandler.uninit_game()
	#~ del eventHandler

def main():
	import sys
	prgname = sys.argv[0]
	game = GameData(deletePathFromPath(prgname, 1))
	# dynamically load irrlicht
	dllName = "irrlicht.dll"
	if len(sys.argv) > 1:
		dllName = sys.argv[1]
	game.createExDevice = createDeviceEx
	if 0 == game.createExDevice:
		game.retVal = 3
		print("Could not load %s.\n" % dllName)
		return game.retVal # could not load dll
	# start without asking for driver
	game.retVal = 1
	while game.retVal < 3:
		# if driver could not created, ask for another driver
		if game.retVal == 0:
			game.setDefault()
			# ask user for driver
			game.deviceParam.DriverType = EDT_OPENGL
			if game.deviceParam.DriverType == EDT_COUNT:
				game.retVal = 3
		runGame(game)
	return game.retVal

if __name__ == "__main__":
	main()
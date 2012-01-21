import os
#~ from struct import *
from math import floor
from pyirrlicht import *

###############################
eItemGroup = 0
WEAPON = 0
AMMO = 1
ARMOR = 2
HEALTH = 3
POWERUP = 4

eItemSubGroup = 0
SUB_NONE = 0
GAUNTLET = 1
MACHINEGUN = 2
SHOTGUN = 3
GRENADE_LAUNCHER = 4
ROCKET_LAUNCHER = 5
LIGHTNING = 6
RAILGUN = 7
PLASMAGUN = 8
BFG = 9
GRAPPLING_HOOK = 10
NAILGUN = 11
PROX_LAUNCHER = 12
CHAINGUN = 13

eItemSpecialEffect = 0
SPECIAL_SFX_NONE		= 0
SPECIAL_SFX_ROTATE		= 1
SPECIAL_SFX_BOUNCE		= 2
SPECIAL_SFX_ROTATE_1	= 4
###############################
class _Q3LevelLoadParameter(ctypes.Structure):
	_fields_ = [('defaultLightMapMaterial', ctypes.c_int),
				('defaultModulate', ctypes.c_int),
				('defaultFilter', ctypes.c_int),
				('patchTesselation', ctypes.c_int),
				('verbose', ctypes.c_int),
				('startTime', ctypes.c_uint),
				('endTime', ctypes.c_uint),
				('mergeShaderBuffer', ctypes.c_int),
				('cleanUnResolvedMeshes', ctypes.c_int),
				('loadAllShaders', ctypes.c_int),
				('loadSkyShader', ctypes.c_int),
				('alpharef', ctypes.c_int),
				('swapLump', ctypes.c_int),
				('swapHeader', ctypes.c_int),
				('scriptDir', ctypes.c_char*64)
				]
	def pack(self):
		return pack('iiiiiIIiiiiiii64s',
					self.defaultLightMapMaterial,
					self.defaultModulate,
					self.defaultFilter,
					self.patchTesselation,
					self.verbose,
					self.startTime,
					self.endTime,
					self.mergeShaderBuffer,
					self.cleanUnResolvedMeshes,
					self.loadAllShaders,
					self.loadSkyShader,
					self.alpharef,
					self.swapLump,
					self.swapHeader,
					self.scriptDir
					)
class SItemElement(ctypes.Structure):
	_fields_ = [#('key', ctypes.c_char_p),
				('model', ctypes.c_char_p*2),
				('sound', ctypes.c_char_p),
				('icon', ctypes.c_char_p),
				('pickup', ctypes.c_char_p),
				('value', ctypes.c_int),
				('group', ctypes.c_int),
				('sub', ctypes.c_int),
				('special', ctypes.c_uint)
				]
Quake3ItemElement = {
	"item_health":SItemElement(
	("models/powerups/health/medium_cross.md3",
	"models/powerups/health/medium_sphere.md3"),
	"sound/items/n_health.wav",
	"icons/iconh_yellow",
	"25 Health",
	25,
	HEALTH,
	SUB_NONE,
	SPECIAL_SFX_BOUNCE | SPECIAL_SFX_ROTATE_1
),
	"item_health_large":SItemElement(
	("models/powerups/health/large_cross.md3",
	"models/powerups/health/large_sphere.md3"),
	"sound/items/l_health.wav",
	"icons/iconh_red",
	"50 Health",
	50,
	HEALTH,
	SUB_NONE,
	SPECIAL_SFX_BOUNCE | SPECIAL_SFX_ROTATE_1
),
	"item_health_mega":SItemElement(
	("models/powerups/health/mega_cross.md3",
	"models/powerups/health/mega_sphere.md3"),
	"sound/items/m_health.wav",
	"icons/iconh_mega",
	"Mega Health",
	100,
	HEALTH,
	SUB_NONE,
	SPECIAL_SFX_BOUNCE | SPECIAL_SFX_ROTATE_1
),
	"item_health_small":SItemElement(
	("models/powerups/health/small_cross.md3",
	"models/powerups/health/small_sphere.md3"),
	"sound/items/s_health.wav",
	"icons/iconh_green",
	"5 Health",
	5,
	HEALTH,
	SUB_NONE,
	SPECIAL_SFX_BOUNCE | SPECIAL_SFX_ROTATE_1
),
	"ammo_bullets":SItemElement(
	("models/powerups/ammo/machinegunam.md3",
	""),
	"sound/misc/am_pkup.wav",
	"icons/icona_machinegun",
	"Bullets",
	50,
	AMMO,
	MACHINEGUN,
	SPECIAL_SFX_BOUNCE,
),
	"ammo_cells":SItemElement(
	("models/powerups/ammo/plasmaam.md3",
	""),
	"sound/misc/am_pkup.wav",
	"icons/icona_plasma",
	"Cells",
	30,
	AMMO,
	PLASMAGUN,
	SPECIAL_SFX_BOUNCE
),
	"ammo_rockets":SItemElement(
	("models/powerups/ammo/rocketam.md3",
	""),
	"",
	"icons/icona_rocket",
	"Rockets",
	5,
	AMMO,
	ROCKET_LAUNCHER,
	SPECIAL_SFX_ROTATE
),
	"ammo_shells":SItemElement(
	("models/powerups/ammo/shotgunam.md3",
	""),
	"sound/misc/am_pkup.wav",
	"icons/icona_shotgun",
	"Shells",
	10,
	AMMO,
	SHOTGUN,
	SPECIAL_SFX_ROTATE
),
	"ammo_slugs":SItemElement(
	("models/powerups/ammo/railgunam.md3",
	""),
	"sound/misc/am_pkup.wav",
	"icons/icona_railgun",
	"Slugs",
	10,
	AMMO,
	RAILGUN,
	SPECIAL_SFX_ROTATE
),
	"item_armor_body":SItemElement(
	("models/powerups/armor/armor_red.md3",
	""),
	"sound/misc/ar2_pkup.wav",
	"icons/iconr_red",
	"Heavy Armor",
	100,
	ARMOR,
	SUB_NONE,
	SPECIAL_SFX_ROTATE
),
	"item_armor_combat":SItemElement(
	("models/powerups/armor/armor_yel.md3",
	""),
	"sound/misc/ar2_pkup.wav",
	"icons/iconr_yellow",
	"Armor",
	50,
	ARMOR,
	SUB_NONE,
	SPECIAL_SFX_ROTATE
),
	"item_armor_shard":SItemElement(
	("models/powerups/armor/shard.md3",
	""),
	"sound/misc/ar1_pkup.wav",
	"icons/iconr_shard",
	"Armor Shared",
	5,
	ARMOR,
	SUB_NONE,
	SPECIAL_SFX_ROTATE
),
	"weapon_gauntlet":SItemElement(
	("models/weapons2/gauntlet/gauntlet.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_gauntlet",
	"Gauntlet",
	0,
	WEAPON,
	GAUNTLET,
	SPECIAL_SFX_ROTATE
),
	"weapon_shotgun":SItemElement(
	("models/weapons2/shotgun/shotgun.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_shotgun",
	"Shotgun",
	10,
	WEAPON,
	SHOTGUN,
	SPECIAL_SFX_ROTATE
),
	"weapon_machinegun":SItemElement(
	("models/weapons2/machinegun/machinegun.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_machinegun",
	"Machinegun",
	40,
	WEAPON,
	MACHINEGUN,
	SPECIAL_SFX_ROTATE
),
	"weapon_grenadelauncher":SItemElement(
	("models/weapons2/grenadel/grenadel.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_grenade",
	"Grenade Launcher",
	10,
	WEAPON,
	GRENADE_LAUNCHER,
	SPECIAL_SFX_ROTATE
),
	"weapon_rocketlauncher":SItemElement(
	("models/weapons2/rocketl/rocketl.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_rocket",
	"Rocket Launcher",
	10,
	WEAPON,
	ROCKET_LAUNCHER,
	SPECIAL_SFX_ROTATE
),
	"weapon_lightning":SItemElement(
	("models/weapons2/lightning/lightning.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_lightning",
	"Lightning Gun",
	100,
	WEAPON,
	LIGHTNING,
	SPECIAL_SFX_ROTATE
),
	"weapon_railgun":SItemElement(
	("models/weapons2/railgun/railgun.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_railgun",
	"Railgun",
	10,
	WEAPON,
	RAILGUN,
	SPECIAL_SFX_ROTATE
),
	"weapon_plasmagun":SItemElement(
	("models/weapons2/plasma/plasma.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_plasma",
	"Plasma Gun",
	50,
	WEAPON,
	PLASMAGUN,
	SPECIAL_SFX_ROTATE
),
	"weapon_bfg":SItemElement(
	("models/weapons2/bfg/bfg.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_bfg",
	"BFG10K",
	20,
	WEAPON,
	BFG,
	SPECIAL_SFX_ROTATE
),
	"weapon_grapplinghook":SItemElement(
	("models/weapons2/grapple/grapple.md3",
	""),
	"sound/misc/w_pkup.wav",
	"icons/iconw_grapple",
	"Grappling Hook",
	0,
	WEAPON,
	GRAPPLING_HOOK,
	SPECIAL_SFX_ROTATE
)
}
###############################

FIRED = 1

#~ DRIVER_TYPE = EDT_SOFTWARE
#~ DRIVER_TYPE = EDT_BURNINGSVIDEO
#~ DRIVER_TYPE = EDT_DIRECT3D9
DRIVER_TYPE = EDT_OPENGL

def fract(x = 0.0):
	return x - floor(x)

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

engine = None
backMusic = None
def background_music(file = ''):
	if not engine:
		return
	if backMusic:
		backMusic.stop()
		backMusic.drop()
	backMusic = engine.play2D(file, True, False, True)
	if backMusic:
		backMusic.setVolume(0.5)

#~ void Q3ShaderFactory (Q3LevelLoadParameter &loadParam,
					#~ IrrlichtDevice *device,
					#~ IQ3LevelMesh* mesh,
					#~ eQ3MeshIndex meshIndex,
					#~ ISceneNode *parent,
					#~ IMetaTriangleSelector *meta,
					#~ bool showShaderName )
def Q3ShaderFactory(loadParam, device, mesh, meshIndex, parent, meta, showShaderName):
	if not mesh or not device:
		return
	node = None
	smgr = device.getSceneManager()
	#~ // the additional mesh can be quite huge and is unoptimized
	#~ // Save to cast to SMesh
	additional_mesh = SMesh(mesh.getMesh(meshIndex))
	if not additional_mesh:
		return
	elif additional_mesh.getMeshBufferCount() == 0:
		return
	if loadParam.verbose > 0:
		loadParam.startTime = device.getTimer().getRealTime()
		if loadParam.verbose > 1:
			device.getLogger().log("q3shaderfactory start", ELL_INFORMATION)
	font = device.getGUIEnvironment().getBuiltInFont()
	if showShaderName:
		font = device.getGUIEnvironment().getFont("fontlucida.png")
	driver = device.getVideoDriver()
	#~ // create helper textures
	if 1:
		pos = 0
		tex = tTexArray()
		getTextures(tex, "$redimage $blueimage $whiteimage $checkerimage", pos, device.getFileSystem(), driver)
		#~ tex = getTextures("$redimage $blueimage $whiteimage $checkerimage", pos, device.getFileSystem(), driver)
	sceneNodeID = 0
	for i in range(additional_mesh.getMeshBufferCount()):
		meshBuffer = additional_mesh.getMeshBuffer(i)
		material = meshBuffer.getMaterial()
		#~ //! The ShaderIndex is stored in the second material parameter
		shaderIndex = int(material.MaterialTypeParam2)
		#~ // the meshbuffer can be rendered without additional support, or it has no shader
		shader = IShader(mesh.getShader(shaderIndex))
		#~ // no shader, or mapped to existing material
		if not shader:
			if 1:
			#~ // clone mesh
				m = SMesh()
				m.addMeshBuffer(meshBuffer)
				mat = m.getMeshBuffer(0).getMaterial()
				if not mat.getTexture(0):
					mat.setTexture(0, driver.getTexture("$blueimage"))
				if not mat.getTexture(1):
					mat.setTexture(1, driver.getTexture("$redimage"))
				store = smgr.getMeshManipulator().createMeshWith2TCoords(m)
				#~ m.drop()
				node = smgr.addMeshSceneNode(store, parent, sceneNodeID)
				node.setAutomaticCulling(EAC_OFF)
				#~ store.drop()
				sceneNodeID += 1
		elif 1:
			#~ stringc s;
			#~ dumpShader ( s, shader );
			#~ printf ( s.c_str () );
			#~ // create sceneNode
			node = smgr.addQuake3SceneNode(meshBuffer, shader, parent, sceneNodeID)
			node.setAutomaticCulling(EAC_FRUSTUM_BOX)
			sceneNodeID += 1
		#~ // show Debug Shader Name
		if showShaderName and node:
			buf = "%hs:%d" % (node.getName(),node.getID())
			node2 = smgr.addBillboardTextSceneNode(font, buf, node, dimension2df(80.0, 8.0), vector3df(0, 10, 0), sceneNodeID)
			#~ snprintf ( buf, 64, "%s:%d", node.getName(),node.getID() );
			#~ //node2.setName ( buf );
			sceneNodeID += 1
		#~ // create Portal Rendertargets
		if shader:
			group = shader.getGroup(1)#const SVarGroup
			if group.isDefined("surfaceparm", "portal"):
				pass
		#~ // add collision
		#~ // find out if shader is marked als nonsolid
		doCreate = (meta != 0)
		if shader:
			group = shader.getGroup(1)#const SVarGroup
			if group.isDefined("surfaceparm", "trans"):
					#~ or group.isDefined( "surfaceparm", "sky" )
					#~ or group.isDefined( "surfaceparm", "nonsolid" ):
				if not group.isDefined("surfaceparm", "metalsteps"):
					doCreate = 0
		if doCreate:
			m = None
			#~ //! controls if triangles are modified by the scenenode during runtime
			takeOriginal = True
			if takeOriginal:
				m = SMesh()
				m.addMeshBuffer(meshBuffer)
			else:
				m = node.getMesh()
			if meta:
				selector = smgr.createOctreeTriangleSelector(m, 0, 128)
				#~ selector = smgr.createTriangleSelector(m, 0)
				meta.addTriangleSelector(selector)
				#~ selector.drop()
			if takeOriginal:
				del m
	if 0:
		if meta:
			selector = smgr.createOctreeTriangleSelector(additional_mesh, 0)
			meta.addTriangleSelector(selector)
			#~ selector.drop()
	if loadParam.verbose > 0:
		loadParam.endTime = device.getTimer().getRealTime()
		buf = "q3shaderfactory needed %04d ms to create %d shader nodes" % (loadParam.endTime - loadParam.startTime, sceneNodeID)
		device.getLogger().log(buf, ELL_INFORMATION)

#~ void Q3ModelFactory (Q3LevelLoadParameter &loadParam,
					#~ IrrlichtDevice *device,
					#~ IQ3LevelMesh* masterMesh,
					#~ ISceneNode *parent,
					#~ bool showShaderName)
def Q3ModelFactory (loadParam, device, masterMesh, parent, showShaderName):
	if not masterMesh or not device:
		return

	entity = masterMesh.getEntityList()#tQ3EntityList
	smgr = device.getSceneManager()


	#~ char buf[128];
	#~ const SVarGroup *group;
	search = IEntity()
	#~ s32 index;
	lastIndex = 0

#~ /*
	#~ stringc s;
	#~ FILE *f = 0;
	#~ f = fopen ( "entity.txt", "wb" );
	#~ for ( index = 0; (u32) index < entityList.size (); ++index )
	#~ {
		#~ const IEntity *entity = &entityList[ index ];
		#~ s = entity.name;
		#~ dumpShader ( s, entity );
		#~ fwrite ( s.c_str(), 1, s.size(), f );
	#~ }
	#~ fclose ( f );
#~ */
	#~ IAnimatedMeshMD3* model;
	#~ SMD3Mesh * mesh;
	#~ const SMD3MeshBuffer *meshBuffer;
	#~ IMeshSceneNode* node;
	#~ ISceneNodeAnimator* anim;
	#~ const IShader *shader;
	#~ u32 pos;
	#~ vector3df p;
	nodeCount = 0
	#~ tTexArray textureArray;

	font = device.getGUIEnvironment().getBuiltInFont()
	if showShaderName:
		font = device.getGUIEnvironment().getFont("fontlucida.png")

	#~ const SItemElement *itemElement;

	#~ // walk list
	for index in range(entity.size()):
		itemElement_key = entity[index].name
		#~ itemElement = getItemElement(itemElement_key)
		#~ if not itemElement:
			#~ continue
		if itemElement_key in Quake3ItemElement:
			itemElement = Quake3ItemElement[itemElement_key]
		else:
			continue

		pos = 0
		#~ p = getAsVector3df(entity[index].getGroup(1).get("origin"), pos)
		p, pos = getAsVector3df(entity[index].getGroup(1).get("origin"))

		nodeCount += 1
		for g in range(2):
			if not itemElement.model[g] or itemElement.model[g][0] == 0:
				continue
			model = IAnimatedMeshMD3(smgr.getMesh(itemElement.model[g]))
			if not model:
				continue

			mesh = model.getOriginalMesh()
			for j in range(mesh.Buffer.size()):
				meshBuffer = mesh.Buffer[j]
				if not meshBuffer:
					continue

				shader = masterMesh.getShader(meshBuffer.Shader, False)
				final = model.getMesh(0).getMeshBuffer(j)
				if shader:
					#~ //!TODO: Hack don't modify the vertexbuffer. make it better;-)
					final.getMaterial().ColorMask = 0
					node = smgr.addQuake3SceneNode(final, shader, parent)
					final.getMaterial().ColorMask = 15
				else:
					#~ // clone mesh
					m = SMesh()
					m.addMeshBuffer(final)
					node = smgr.addMeshSceneNode(m,  parent)
					#~ m.drop()

				if not node:
					device.getLogger().log("q3ModelFactory shader %s failed" % meshBuffer.Shader)
					continue

				#~ // node was maybe centered by shaderscenenode
				node.setPosition(p)
				node.setName(meshBuffer.Shader)
				node.setAutomaticCulling(EAC_BOX)

				#~ // add special effects to node
				if itemElement.special & SPECIAL_SFX_ROTATE or (g == 0 and itemElement.special & SPECIAL_SFX_ROTATE_1):
					anim = smgr.createRotationAnimator(vector3df(0.0, 2.0, 0.0))
					node.addAnimator(anim)
					#~ anim.drop()

				if itemElement.special & SPECIAL_SFX_BOUNCE:
					#~ anim = smgr.createFlyStraightAnimator(p, p + vector3df(0.0, 60.0, 0.0), 1000, True, True)
					anim = smgr.createFlyCircleAnimator(p + vector3df(0.0, 20.0, 0.0), 20.0, 0.005, vector3df(1.0, 0.0, 0.0), fract(nodeCount * 0.05), 1.0)
					node.addAnimator(anim)
					#~ anim.drop()
		#~ // show name
		if showShaderName:
			node2 = smgr.addBillboardTextSceneNode(font, "%hs" % itemElement_key, parent, dimension2df(80.0, 8.0), p + vector3df(0, 30, 0), 0)

	#~ // music
	search.name = "worldspawn"
	index = entity.binary_search_multi(search, lastIndex)

	if index >= 0:
		group = entity[index].getGroup(1)
		background_music(group.get("music"))

	#~ // music
	search.name = "worldspawn"
	index = entity.binary_search_multi(search, lastIndex)

	if index >= 0:
		group = entity[index].getGroup(1)
		background_music(group.get("music"))


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
		self.guiActivebreak = False
		self.guiInputActive = 0
		self.GammaValue = 1.0
		self.deviceParam.DriverType = DRIVER_TYPE
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
		self.CurrentMapName = ''
		self.CurrentArchiveList = []
		self.CurrentArchiveList.append(self.StartupDir + 'media/')
		#~ self.CurrentArchiveList.append('/q/baseq3/')
		self.CurrentArchiveList.append(self.StartupDir + 'media/map-20kdm2.pk3')

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
		entityList = IQ3LevelMesh(mesh).getEntityList()
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
					if v.name == 'playerposition':
						self.PlayerPosition = getAsVector3df(v.content, pos)
					else:
						if v.name == 'playerrotation':
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
		buf = 'playerposition %.f %.f %.f\nplayerrotation %.f %.f %.f\n' % (self.PlayerPosition.X, self.PlayerPosition.Z, self.PlayerPosition.Y, self.PlayerRotation.X, self.PlayerRotation.Z, self.PlayerRotation.Y)
		file.write(buf, len(buf))
		for i in range(fs.getFileArchiveCount()):
			buf = 'archive %s\n' % fs.getFileArchive(i).getFileList().getPath()
			file.write(buf, len(buf))
		#~ file.drop()
		return 1

class Q3Player(IAnimationEndCallBack):
	Device = None
	MapParent = None
	Mesh = None
	WeaponNode = None
	StartPositionCurrent = 0
	Anim = [TimeFire(), TimeFire(), TimeFire(), TimeFire()]
	animation = ''
	buf = ''
	#~ def __init__(self):
		#~ self.Device = None
		#~ self.MapParent = None
		#~ self.Mesh = None
		#~ self.WeaponNode = None
		#~ self.StartPositionCurrent = 0
		#~ self.Anim = [TimeFire(), TimeFire(), TimeFire(), TimeFire()]
		#~ self.animation = ''
		#~ self.buf = ''
		#~ IAnimationEndCallBack.__init__(self)

	def setAnim(self, name):
		if name:
			self.animation = name
			if self.WeaponNode:
				self.WeaponNode.setAnimationEndCallback(self)
				self.WeaponNode.setMD2Animation(self.animation)
		else:
			self.animation = ''
			if self.WeaponNode:
				self.WeaponNode.setAnimationEndCallback(IAnimationEndCallBack(0))

	def OnAnimationEnd(self, node):
		#~ self.Device.getLogger().log('=== OnAnimationEnd %s' % IAnimatedMeshSceneNode(node), ELL_INFORMATION)
		self.setAnim('')

	def cam(self):
		camera = self.Device.getSceneManager().getActiveCamera()
		for a in camera.getAnimators():
			if a.getType() == ESNAT_COLLISION_RESPONSE:
				return ISceneNodeAnimatorCollisionResponse(a)
		return ISceneNodeAnimatorCollisionResponse()

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
		if surface == 'earth':
			return vector3df(0.0, -90.0, 0.0)
		elif surface == 'moon':
			return vector3df(0.0, -6.0 / 100.0, 0.0)
		elif surface == 'water':
			return vector3df(0.1 / 100.0, -2.0 / 100.0, 0.0)
		elif surface == 'ice':
			return vector3df(0.2 / 100.0, -9.0 / 100.0, 0.3 / 100.0)
		else:
			return vector3df(0.0, 0.0, 0.0)

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
		keyMap = SKeyMap(10)
		keyMap.set(0, EKA_MOVE_FORWARD, KEY_UP)
		keyMap.set(1, EKA_MOVE_FORWARD, KEY_KEY_W)
		keyMap.set(2, EKA_MOVE_BACKWARD, KEY_DOWN)
		keyMap.set(3, EKA_MOVE_BACKWARD, KEY_KEY_S)
		keyMap.set(4, EKA_STRAFE_LEFT, KEY_LEFT)
		keyMap.set(5, EKA_STRAFE_LEFT, KEY_KEY_A)
		keyMap.set(6, EKA_STRAFE_RIGHT, KEY_RIGHT)
		keyMap.set(7, EKA_STRAFE_RIGHT, KEY_KEY_D)
		keyMap.set(8, EKA_JUMP_UP, KEY_KEY_J)
		keyMap.set(9, EKA_CROUCH, KEY_KEY_C)
		camera = smgr.addCameraSceneNodeFPS(None, 100.0, 0.6, -1, keyMap, 10, False, 0.6)
		camera.setName('First Person Camera')
		#camera.setFOV(100.0 * DEGTORAD)
		camera.setFarValue(20000.0)
		#~ weaponMesh = smgr.getMesh('gun.md2').as_IAnimatedMeshMD2()
		weaponMesh = IAnimatedMeshMD2(smgr.getMesh('gun.md2'))
		if not weaponMesh:
			return
		if weaponMesh.getMeshType() == EAMT_MD2:
			i = 0
			count = weaponMesh.getAnimationCount()
			while i < count:
				buf = 'Animation: %s' % weaponMesh.getAnimationName(i)
				device.getLogger().log(buf, ELL_INFORMATION)
				i += 1
		self.WeaponNode = smgr.addAnimatedMeshSceneNode(weaponMesh, smgr.getActiveCamera(), 10, vector3df( 0, 0, 0), vector3df(-90,-90,90))
		self.WeaponNode.setMaterialFlag(EMF_LIGHTING, False)
		self.WeaponNode.setMaterialTexture(0, driver.getTexture('gun.jpg'))
		self.WeaponNode.setLoopMode(False)
		self.WeaponNode.setName('tommi the gun man')
		anim = smgr.createCollisionResponseAnimator(meta, camera, vector3df(30,45,30), self.getGravity('earth'), vector3df(0,40,0), 0.0005)
		camera.addAnimator(anim)
		#~ anim.drop()
		#~ if meta:
			#~ meta.drop()
		self.respawn()
		self.setAnim('idle')

	def respawn(self):
		if not self.Device:
			return
		camera = self.Device.getSceneManager().getActiveCamera()
		self.Device.getLogger().log('=== respawn')
		i_scene_node_animator_collision_response = self.cam()
		if i_scene_node_animator_collision_response:
			if self.StartPositionCurrent >= self.Q3StartPosition(camera, self.StartPositionCurrent+1, i_scene_node_animator_collision_response.getEllipsoidTranslation()):
				self.StartPositionCurrent = 0

	def Q3StartPosition(self, camera, startposIndex, translation):
		if not self.Mesh:
			return 0
		entityList = IQ3LevelMesh(self.Mesh).getEntityList()
		search = IEntity()
		search.name = 'info_player_start'# 'info_player_deathmatch'
		lastIndex = 0
		index = entityList.binary_search_multi(search, lastIndex)
		if index < 0:
			search.name = 'info_player_deathmatch'
			index = entityList.binary_search_multi(search, lastIndex)
		if index < 0:
			return 0
		index += max(min(startposIndex, 0), lastIndex - index)
		group = SVarGroup()
		group = entityList[index].getGroup(1)
		parsepos = 0
		if self.Device:
			self.Device.getLogger().log('=== origin %s' % group.get('origin'))
		#~ pos = getAsVector3df(group.get('origin'), parsepos) + translation
		pos, parsepos = getAsVector3df(group.get('origin'))
		pos += translation
		if self.Device:
			self.Device.getLogger().log('=== parsepos %d' % parsepos)
		parsepos = 0
		if self.Device:
			self.Device.getLogger().log('=== angle %s' % group.get('angle'))
		#~ angle = getAsFloat(group.get('angle'), parsepos)
		angle, parsepos = getAsFloat(group.get('angle'))
		if self.Device:
			self.Device.getLogger().log('=== parsepos %d' % parsepos)
		target = vector3df(0.0, 0.0, 1.0)
		target.rotateXZBy(angle - 90.0, vector3df())
		if camera:
			camera.setPosition(pos)
			camera.setTarget(pos + target)
			camera.OnAnimate(0)
		if self.Device:
			self.Device.getLogger().log('=== 2 Q3StartPosition %d, %s, %s, %d' % (startposIndex, pos, target, lastIndex - index + 1))
		return lastIndex - index + 1

	def setpos(self, pos, rotation):
		if self.Device:
			self.Device.getLogger().log('=== setpos %s, %s' % (pos, rotation))
			camera = self.Device.getSceneManager().getActiveCamera()
			if camera:
				camera.setPosition(pos)
				camera.setRotation(rotation)
				camera.OnAnimate(0)

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
	scolor_scene = SColor(0,0,80,150)
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
		self.Game.save('explorer.cfg')
		#~ self.Game.Device.drop()

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
					#~ image.setPixel(x, y, SColor(int(0xFFFF)))
					image.setPixel(x, y, SColor(255,255,255,255))
				#~ data = data + image.getPitch()
			#~ image.unlock()
			buf = 'smoke_%02d' % i
			texture = driver.addTexture(buf, image)
			#~ image.drop()
		# fog
		for i in range(1):
			image = driver.createImage(ECF_A8R8G8B8, dim)
			#~ data = image.lock()
			for y in range(dim.Height):
				for x in range(dim.Width):
					#~ data[x] = 0xFFFFFFFF
					#~ image.setPixel(x, y, SColor(int(0xFFFF)))
					image.setPixel(x, y, SColor(255,255,255,255))
				#~ data = data + image.getPitch()
			#~ image.unlock()
			buf = 'fog_%02d' % i
			texture = driver.addTexture(buf, image)
			#~ image.drop()

	def CreateGUI(self):
		env = self.Game.Device.getGUIEnvironment()
		driver = self.Game.Device.getVideoDriver()
		self.gui.drop()
		# set skin font
		font = env.getFont('fontlucida.png')
		if font:
			env.getSkin().setFont(font)
		env.getSkin().setColor(EGDC_BUTTON_TEXT, SColor(240,int(0xAA),int(0xAA),int(0xAA)))
		env.getSkin().setColor(EGDC_3D_HIGH_LIGHT, SColor(240,int(0x22),int(0x22),int(0x22)))
		env.getSkin().setColor(EGDC_3D_FACE, SColor(240,int(0x44),int(0x44),int(0x44)))
		env.getSkin().setColor(EGDC_WINDOW, SColor(240,int(0x66),int(0x66),int(0x66)))
		# minimal gui size 800x600
		dim = dimension2du(800, 600)
		vdim = self.Game.Device.getVideoDriver().getScreenSize()
		self.gui.Window = env.addWindow(recti(0, 0, dim.Width, dim.Height), False, 'Quake3 Explorer')
		self.gui.Window.setToolTipText('Quake3Explorer. Loads and show various BSP File Format and Shaders.')
		self.gui.Window.getCloseButton().setToolTipText('Quit Quake3 Explorer')
		# add a status line help text
		self.gui.StatusLine = env.addStaticText('', recti(5, dim.Height - 30, dim.Width - 5, dim.Height - 10), False, False, self.gui.Window, -1, True)
		env.addStaticText('VideoDriver:', recti(dim.Width - 400, 24, dim.Width - 310, 40 ),False, False, self.gui.Window, -1, False)
		self.gui.VideoDriver = env.addComboBox(recti(dim.Width - 300, 24, dim.Width - 10, 40 ), self.gui.Window)
		self.gui.VideoDriver.addItem('Direct3D 9.0c', EDT_DIRECT3D9)
		self.gui.VideoDriver.addItem('Direct3D 8.1', EDT_DIRECT3D8)
		self.gui.VideoDriver.addItem('OpenGL 1.5', EDT_OPENGL)
		self.gui.VideoDriver.addItem('Software Renderer', EDT_SOFTWARE)
		self.gui.VideoDriver.addItem("Burning's Video (TM) Thomas Alten", EDT_BURNINGSVIDEO)
		self.gui.VideoDriver.setSelected(self.gui.VideoDriver.getIndexForItemData(self.Game.deviceParam.DriverType))
		self.gui.VideoDriver.setToolTipText('Use a VideoDriver')
		env.addStaticText('VideoMode:', recti(dim.Width - 400, 44, dim.Width - 310, 60 ),False, False, self.gui.Window, -1, False)
		self.gui.VideoMode = env.addComboBox(recti(dim.Width - 300, 44, dim.Width - 10, 60 ), self.gui.Window)
		self.gui.VideoMode.setToolTipText('Supported Screenmodes')
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
				a = ''
				if aspect <= 1.3333333333: a = '4:3'
				elif aspect == 1.6666666: a = '15:9 widescreen'
				elif aspect == 1.7777777: a = '16:9 widescreen'
				elif aspect == 1.6: a = '16:10 widescreen'
				elif aspect == 2.133333: a = '20:9 widescreen'
				self.buf =  '%d x %d, %s' % (w, h, a)
				self.gui.VideoMode.addItem(self.buf, val)
		self.gui.VideoMode.setSelected(self.gui.VideoMode.getIndexForItemData(self.Game.deviceParam.WindowSize.Width << 16 | self.Game.deviceParam.WindowSize.Height))
		#~ print '===', self.Game.deviceParam.Fullscreen, self.gui.Window, self.gui.Window.c_pointer
		#~ self.gui.FullScreen = env.addCheckBox(False, recti(dim.Width - 400, 64, dim.Width - 300, 80), self.gui.Window, -1, 'Fullscreen')
		self.gui.FullScreen = env.addCheckBox(self.Game.deviceParam.Fullscreen, recti(dim.Width - 400, 64, dim.Width - 300, 80), self.gui.Window, -1, 'Fullscreen')
		self.gui.FullScreen.setToolTipText('Set Fullscreen or Window Mode')
		self.gui.Bit32 = env.addCheckBox(self.Game.deviceParam.Bits == 32, recti(dim.Width - 300, 64, dim.Width - 240, 80), self.gui.Window, -1, '32Bit')
		self.gui.Bit32.setToolTipText('Use 16 or 32 Bit')
		env.addStaticText('MultiSample:', recti(dim.Width - 235, 64, dim.Width - 150, 80),False, False, self.gui.Window, -1, False)
		self.gui.MultiSample = env.addScrollBar(True, recti(dim.Width - 150, 64, dim.Width - 70, 80), self.gui.Window, -1)
		self.gui.MultiSample.setMin(0)
		self.gui.MultiSample.setMax(8)
		self.gui.MultiSample.setSmallStep(1)
		self.gui.MultiSample.setLargeStep(1)
		self.gui.MultiSample.setPos(self.Game.deviceParam.AntiAlias)
		self.gui.MultiSample.setToolTipText('Set the MultiSample (disable, 1x, 2x, 4x, 8x)')
		self.gui.SetVideoMode = env.addButton(recti( dim.Width - 60, 64, dim.Width - 10, 80), self.gui.Window, -1, 'set')
		self.gui.SetVideoMode.setToolTipText('Set Video Mode with current values')
		env.addStaticText('Gamma:', recti(dim.Width - 400, 104, dim.Width - 310, 120),False, False, self.gui.Window, -1, False)
		self.gui.Gamma = env.addScrollBar(True, recti(dim.Width - 300, 104, dim.Width - 10, 120), self.gui.Window,-1)
		self.gui.Gamma.setMin(50)
		self.gui.Gamma.setMax(350)
		self.gui.Gamma.setSmallStep(1)
		self.gui.Gamma.setLargeStep(10)
		self.gui.Gamma.setPos(int(self.Game.GammaValue * 100))
		self.gui.Gamma.setToolTipText('Adjust Gamma Ramp ( 0.5 - 3.5)')
		self.Game.Device.setGammaRamp(self.Game.GammaValue, self.Game.GammaValue, self.Game.GammaValue, 0.0, 0.0)
		env.addStaticText('Tesselation:', recti(dim.Width - 400, 124, dim.Width - 310, 140),False, False, self.gui.Window, -1, False)
		self.gui.Tesselation = env.addScrollBar(True, recti( dim.Width - 300, 124, dim.Width - 10, 140), self.gui.Window, -1)
		self.gui.Tesselation.setMin(2)
		self.gui.Tesselation.setMax(12)
		self.gui.Tesselation.setSmallStep(1)
		self.gui.Tesselation.setLargeStep(1)
		self.gui.Tesselation.setPos(self.Game.loadParam.patchTesselation)
		self.gui.Tesselation.setToolTipText('How smooth should curved surfaces be rendered')
		self.gui.Collision = env.addCheckBox(True, recti( dim.Width - 400, 150, dim.Width - 300, 166), self.gui.Window, -1, 'Collision')
		self.gui.Collision.setToolTipText('Set collision on or off ( flythrough ). \nPress F7 on your Keyboard')
		self.gui.Visible_Map = env.addCheckBox(True, recti( dim.Width - 300, 150, dim.Width - 240, 166), self.gui.Window, -1, 'Map')
		self.gui.Visible_Map.setToolTipText('Show or not show the static part the Level. \nPress F3 on your Keyboard')
		self.gui.Visible_Shader = env.addCheckBox(True, recti( dim.Width - 240, 150, dim.Width - 170, 166), self.gui.Window, -1, 'Shader')
		self.gui.Visible_Shader.setToolTipText('Show or not show the Shader Nodes. \nPress F4 on your Keyboard')
		self.gui.Visible_Fog = env.addCheckBox(True, recti( dim.Width - 170, 150, dim.Width - 110, 166), self.gui.Window, -1, 'Fog')
		self.gui.Visible_Fog.setToolTipText('Show or not show the Fog Nodes. \nPress F5 on your Keyboard')
		self.gui.Visible_Unresolved = env.addCheckBox(True, recti( dim.Width - 110, 150, dim.Width - 10, 166), self.gui.Window,-1, 'Unresolved')
		self.gui.Visible_Unresolved.setToolTipText("Show the or not show the Nodes the Engine can't handle. \nPress F6 on your Keyboard")
		self.gui.Visible_Skydome = env.addCheckBox(True, recti(dim.Width - 110, 180, dim.Width - 10, 196), self.gui.Window,-1, 'Skydome')
		self.gui.Visible_Skydome.setToolTipText('Show the or not show the Skydome.')
		self.gui.Respawn = env.addButton(recti(dim.Width - 260, 90, dim.Width - 10, 106), None, -1, 'Respawn')
		env.addStaticText('Archives:', recti(5, dim.Height - 530, dim.Width - 600,dim.Height - 514),False, False, self.gui.Window, -1, False)
		self.gui.ArchiveAdd = env.addButton(recti(dim.Width - 725, dim.Height - 530, dim.Width - 665, dim.Height - 514), self.gui.Window,-1, 'add')
		self.gui.ArchiveAdd.setToolTipText('Add an archive, usually packed zip-archives (*.pk3) to the Filesystem')
		self.gui.ArchiveRemove = env.addButton(recti(dim.Width - 660, dim.Height - 530, dim.Width - 600, dim.Height - 514), self.gui.Window,-1, 'del')
		self.gui.ArchiveRemove.setToolTipText('Remove the selected archive from the FileSystem.')
		self.gui.ArchiveUp = env.addButton(recti(dim.Width - 575, dim.Height - 530, dim.Width - 515, dim.Height - 514), self.gui.Window,-1, 'up')
		self.gui.ArchiveUp.setToolTipText('Arrange Archive Look-up Hirachy. Move the selected Archive up')
		self.gui.ArchiveDown = env.addButton(recti(dim.Width - 510, dim.Height - 530, dim.Width - 440, dim.Height - 514), self.gui.Window,-1, 'down')
		self.gui.ArchiveDown.setToolTipText('Arrange Archive Look-up Hirachy. Move the selected Archive down')
		self.gui.ArchiveList = env.addTable(recti(5,dim.Height - 510, dim.Width - 450,dim.Height - 410), self.gui.Window)
		self.gui.ArchiveList.addColumn('Type', 0)
		self.gui.ArchiveList.addColumn('Real File Path', 1)
		self.gui.ArchiveList.setColumnWidth(0, 60)
		self.gui.ArchiveList.setColumnWidth(1, 284)
		self.gui.ArchiveList.setToolTipText('Show the attached Archives')
		env.addStaticText('Maps:', recti(5, dim.Height - 400, dim.Width - 450,dim.Height - 380), False, False, self.gui.Window, -1, False)
		self.gui.MapList = env.addListBox(recti(5,dim.Height - 380, dim.Width - 450,dim.Height - 40), self.gui.Window, -1, True)
		self.gui.MapList.setToolTipText('Show the current Maps in all Archives.\n Double-Click the Map to start the level')
		# create a visible Scene Tree
		env.addStaticText('Scenegraph:', recti(dim.Width - 400, dim.Height - 400, dim.Width - 5,dim.Height - 380 ), False, False, self.gui.Window, -1, False)
		self.gui.SceneTree = env.addTreeView(recti(dim.Width - 400, dim.Height - 380, dim.Width - 5, dim.Height - 40), self.gui.Window, -1, True, True, False)
		self.gui.SceneTree.setToolTipText('Show the current Scenegraph')
		if IRRLICHT_VERSION < 180:
			self.gui.SceneTree.getRoot().clearChilds()
		self.addSceneTreeItem(self.Game.Device.getSceneManager().getRootSceneNode(), self.gui.SceneTree.getRoot())
		imageList = env.createImageList(driver.getTexture('iconlist.png'), dimension2di(32, 32), True)
		if imageList:
			self.gui.SceneTree.setImageList(imageList)
			#~ imageList.drop()
		# load the engine logo
		self.gui.Logo = env.addImage(driver.getTexture('irrlichtlogo3.png'), position2di(5, 16), True)
		self.gui.Logo.setToolTipText('The great Irrlicht Engine')
		self.AddArchive('')

	def AddArchive(self, archiveName):
		fs = self.Game.Device.getFileSystem()
		if archiveName:
			exists = False
			for i in range(fs.getFileArchiveCount()):
				if fs.getFileArchive(i).getFileList().getPath() == archiveName:
					exists = True
					break
			if not exists:
				try:
					if not fs.addFileArchive(archiveName, True, False):
						print ('--- ERROR LOAD FILE ARCHIVE', archiveName)
					#~ else:
						#~ print ('+++ FILE ARCHIVE LOADED', archiveName)
				except:
					print ('--- ERROR LOAD FILE ARCHIVE', archiveName)
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
					typeName = 'ZIP'
				elif archive_type == EFAT_GZIP:
					typeName = 'gzip'
				elif archive_type == EFAT_FOLDER:
					typeName = 'Mount'
				elif archive_type == EFAT_PAK:
					typeName = 'PAK'
				elif archive_type == EFAT_TAR:
					typeName = 'TAR'
				self.gui.ArchiveList.setCellText(index, 0, typeName)
				self.gui.ArchiveList.setCellText(index, 1, archive.getFileList().getPath())
		# browse the archives for maps
		if self.gui.MapList:
			self.gui.MapList.clear()
			self.bank = self.Game.Device.getGUIEnvironment().getSpriteBank('sprite_q3map')
			if not self.bank:
				self.bank = self.Game.Device.getGUIEnvironment().addEmptySpriteBank('sprite_q3map')
			self.sprite = SGUISprite()
			self.frame = SGUISpriteFrame()
			r = recti()
			self.bank.getSprites().clear()
			self.bank.getPositions().clear()
			self.gui.MapList.setSpriteBank(self.bank)
			s = ''
			# browse the attached file system
			fs.setFileListSystem(FILESYSTEM_VIRTUAL)
			fs.changeWorkingDirectoryTo('/maps/')
			fileList = fs.createFileList()
			fs.setFileListSystem(FILESYSTEM_NATIVE)
			g = 0
			file_count = fileList.getFileCount()
			i = 0
			while i < file_count:
				s = fileList.getFullFileName(i)
				if s.find('.bsp') > -1:
					# get level screenshot. reformat texture to 128x128
					c = 'levelshots/' + cutFilenameExtension(deletePathFromFilename(s))
					dim = dimension2du(128, 128)
					driver = self.Game.Device.getVideoDriver()
					image = IImage(0)
					tex = ITexture()
					filename = c + '.jpg'
					if fs.existFile(filename):
						image = driver.createImageFromFile(filename)
					if not image:
						filename = c + '.tga'
						if fs.existFile(filename):
							image = driver.createImageFromFile(filename)
					if image:
						filter = driver.createImage(ECF_R8G8B8, dim)
						image.copyToScalingBoxFilter(filter, 0)
						#~ image.drop()
						image = filter
					if image:
						tex = driver.addTexture(filename, image)
						#~ image.drop()
					self.bank.setTexture(g, tex)
					r.LowerRightCorner.X = dim.Width
					r.LowerRightCorner.Y = dim.Height
					self.gui.MapList.setItemHeight(r.LowerRightCorner.Y + 4)
					self.frame.rectNumber = self.bank.getPositions().size()
					self.frame.textureNumber = g
					self.bank.getPositions().push_back(r)
					self.sprite.Frames.set_used(0)
					self.sprite.Frames.push_back(self.frame)
					self.sprite.frameTime = 0
					self.bank.getSprites().push_back(self.sprite)
					self.gui.MapList.addItem(s, g)
					g = g + 1
				i = i + 1
			#~ fileList.drop()
			self.gui.MapList.setSelected(-1)
			bar = IGUIScrollBar(self.gui.MapList.getElementFromId(0))
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
		#~ self.Impacts.clear()
		self.Impacts = []
		if self.Meta:
			self.Meta = None
		dropElement(self.MapParent)
		dropElement(self.SkyNode)
		# clean out meshes, because textures are invalid
		# TODO: better texture handling;-)
		cache = self.Game.Device.getSceneManager().getMeshCache()
		cache.clear()
		self.Mesh = None

	def LoadMap(self, mapName, collision = True):
		if not mapName:
			return
		self.dropMap()
		fs = self.Game.Device.getFileSystem()
		smgr = self.Game.Device.getSceneManager()
		#~ file = fs.createMemoryReadFile(ctypes.pointer(self.Game.loadParam), ctypes.sizeof(self.Game.loadParam), 'levelparameter.cfg', False)
		#~ file = fs.createMemoryReadFile(self.Game.loadParam.pack(), ctypes.sizeof(self.Game.loadParam), 'levelparameter.cfg', False)
		file = fs.createMemoryReadFile(self.Game.loadParam, self.Game.loadParam.size(), 'levelparameter.cfg', False)
		# load cfg file
		cfgMesh = smgr.getMesh(file)
		#~ file.drop()
		# load the actual map
		self.Mesh = IQ3LevelMesh(smgr.getMesh(mapName))#levelshots/20kdm2
		if not self.Mesh:
			return
		geometry = self.Mesh.getMesh(E_Q3_MESH_GEOMETRY)
		if not geometry:
			return
		elif geometry.getMeshBufferCount() == 0:
			return
		self.Game.CurrentMapName = mapName
		#create a collision list
		self.Meta = None
		if collision:
			self.Meta = smgr.createMetaTriangleSelector()
		minimalNodes = 2048
		self.MapParent = smgr.addOctreeSceneNode(geometry, 0, -1, minimalNodes)
		self.MapParent.setName(mapName)
		if self.Meta:
			selector = smgr.createOctreeTriangleSelector(geometry, self.MapParent, minimalNodes)
			#~ selector = smgr.createTriangleSelector(geometry, self.MapParent)
			self.Meta.addTriangleSelector(selector)
			#~ selector.drop()
		# logical parent for the items
		self.ItemParent = smgr.addEmptySceneNode()
		if self.ItemParent:
			self.ItemParent.setName('Item Container')
		self.ShaderParent = smgr.addEmptySceneNode()
		if self.ShaderParent:
			self.ShaderParent.setName('Shader Container')
		self.UnresolvedParent = smgr.addEmptySceneNode()
		if self.UnresolvedParent:
			self.UnresolvedParent.setName('Unresolved Container')
		self.FogParent = smgr.addEmptySceneNode()
		if self.FogParent:
			self.FogParent.setName('Fog Container')
		# logical parent for the bullets
		self.BulletParent = smgr.addEmptySceneNode()
		if self.BulletParent:
			self.BulletParent.setName('Bullet Container')
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_ITEMS, self.ShaderParent, self.Meta, False)
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_FOG, self.FogParent, 0, False)
		Q3ShaderFactory(self.Game.loadParam, self.Game.Device, self.Mesh, E_Q3_MESH_UNRESOLVED, self.UnresolvedParent, self.Meta, True)
		#Now construct Models from Entity List
		Q3ModelFactory(self.Game.loadParam, self.Game.Device, self.Mesh, self.ItemParent, False)

	def addSceneTreeItem(self, parent, nodeParent):
		node = None
		msg = ''
		imageIndex = -1
		childrens = parent.getChildren()
		childrens_count = len(childrens)
		#~ idx_children = 0
		for children in childrens:
		#~ while idx_children < childrens_count:
			#~ children = childrens[idx_children]
			#~ idx_children = idx_children + 1
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
				msg = '%hs,%hs' % (self.Game.Device.getSceneManager().getSceneNodeTypeName(children_type), children.getName())
			else:
				msg = '%hs' % children.getName()
			node = nodeParent.addChildBack(msg, None, imageIndex)
			# Add all Animators
			animators = children.getAnimators()
			animators_count = len(animators)
			idx_animator = 0
			#~ for animator in animators:
			while idx_animator < animators_count:
				animator = animators[idx_animator]
				idx_animator = idx_animator + 1
				imageIndex = -1
				animator_type  = animator.getType()
				msg = '%hs' % self.Game.Device.getSceneManager().getAnimatorTypeName(animator_type)
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
		if not self.Meta:
			self.Meta = IMetaTriangleSelector()
		self.Player[0].create(self.Game.Device, self.Mesh, self.MapParent, self.Meta)

	# Adds a skydome to the scene
	def AddSky(self, dome, texture):
		#~ self.Game.Device.getLogger().log('===' + texture)
		smgr = self.Game.Device.getSceneManager()
		driver = self.Game.Device.getVideoDriver()
		oldMipMapState = driver.getTextureCreationFlag(ETCF_CREATE_MIP_MAPS)
		driver.setTextureCreationFlag(ETCF_CREATE_MIP_MAPS, False)
		if dome == 0:
			p = ('ft', 'rt', 'bk', 'lf', 'up', 'dn')
			i = 0
			buf = '%s_%s.jpg' % (texture, p[i])
			self.SkyNode = smgr.addSkyBoxSceneNode(driver.getTexture(buf), 0, 0, 0, 0, 0)
			if self.SkyNode:
				for i in range(6):
					buf = '%s_%s.jpg' % (texture, p[i])
					self.SkyNode.getMaterial(i).setTexture(0, driver.getTexture(buf))
		else:
			if dome == 1:
				buf = '%s.jpg' % texture
				self.SkyNode = smgr.addSkyDomeSceneNode(driver.getTexture(buf), 32, 32, 1.0, 1.0, 1000.0, None, 11)
			elif dome == 2:
				buf = '%s.jpg' % texture
				self.SkyNode = smgr.addSkyDomeSceneNode(driver.getTexture(buf), 16, 8, 0.95, 2.0, 1000.0, None, 11)
			if self.SkyNode:
				self.SkyNode.setName('Skydome')
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
		else:
			w = IGUIWindow()
		self.Game.Device.getGUIEnvironment().setFocus(w)

	def OnEvent(self, evt):
		event = SEvent(evt)
		if event.EventType == EET_LOG_TEXT_EVENT:
			return False
		if self.Game.guiActive and event.EventType == EET_GUI_EVENT:
			gui_event_type = event.GUIEvent.EventType
			caller = event.GUIEvent.Caller
			if caller == self.gui.MapList and gui_event_type == EGET_LISTBOX_SELECTED_AGAIN:
				#~ caller = IGUIListBox(caller)
				selected = self.gui.MapList.getSelected()
				if selected >= 0:
					loadMap = self.gui.MapList.getListItem(selected)
					if not self.MapParent or loadMap != self.Game.CurrentMapName:
						self.Game.Device.getLogger().log('=== Loading map %ls' % loadMap, ELL_INFORMATION)
						self.LoadMap(loadMap, True)
						#~ self.LoadMap(loadMap, False)
						#~ print('=== SkyShader', self.Game.loadParam.loadSkyShader)
						if not self.Game.loadParam.loadSkyShader:
							self.AddSky(1, 'skydome2')
						self.CreatePlayers()
						self.CreateGUI()
						self.SetGUIActive(0)
						#~ return True
						return False
			elif caller == self.gui.ArchiveRemove and gui_event_type == EGET_BUTTON_CLICKED:
				self.Game.Device.getFileSystem().removeFileArchive(self.gui.ArchiveList.getSelected())
				self.Game.CurrentMapName = ''
				self.AddArchive('')
			elif caller == self.gui.ArchiveAdd and gui_event_type == EGET_BUTTON_CLICKED:
				if not self.gui.ArchiveFileOpen:
					self.Game.Device.getFileSystem().setFileListSystem(FILESYSTEM_NATIVE)
					self.gui.ArchiveFileOpen = self.Game.Device.getGUIEnvironment().addFileOpenDialog('Add Game Archive', False, self.gui.Window)
			elif caller == self.gui.ArchiveFileOpen and gui_event_type == EGET_FILE_SELECTED:
				self.AddArchive(self.gui.ArchiveFileOpen.getFileName())
				self.gui.ArchiveFileOpen = None
			elif caller == self.gui.ArchiveFileOpen and gui_event_type == EGET_DIRECTORY_SELECTED:
				self.AddArchive(self.gui.ArchiveFileOpen.getDirectoryName())
			elif caller == self.gui.ArchiveFileOpen and gui_event_type == EGET_FILE_CHOOSE_DIALOG_CANCELLED:
				self.gui.ArchiveFileOpen = None
			elif (caller == self.gui.ArchiveUp or caller == self.gui.ArchiveDown) and gui_event_type == EGET_BUTTON_CLICKED:
				rel = 1
				if caller == self.gui.ArchiveUp:
					rel = -1
				if self.Game.Device.getFileSystem().moveFileArchive(self.gui.ArchiveList.getSelected(), rel):
					newIndex = min(max(self.gui.ArchiveList.getSelected() + rel, 0), self.gui.ArchiveList.getRowCount() - 1)
					self.AddArchive('')
					self.gui.ArchiveList.setSelected(newIndex)
					self.Game.CurrentMapName = ''
			elif caller == self.gui.VideoDriver and gui_event_type == EGET_COMBO_BOX_CHANGED:
				self.Game.deviceParam.DriverType = self.gui.VideoDriver.getItemData(self.gui.VideoDriver.getSelected())
			elif caller == self.gui.VideoMode and gui_event_type == EGET_COMBO_BOX_CHANGED:
				val = self.gui.VideoMode.getItemData(self.gui.VideoMode.getSelected())
				self.Game.deviceParam.WindowSize.Width = val >> 16
				self.Game.deviceParam.WindowSize.Height = val & 0xFFFF
			elif caller == self.gui.FullScreen and gui_event_type == EGET_CHECKBOX_CHANGED:
				self.Game.deviceParam.Fullscreen = self.gui.FullScreen.isChecked()
			elif caller == self.gui.Bit32 and gui_event_type == EGET_CHECKBOX_CHANGED:
				self.Game.deviceParam.Bits = 16
				if self.gui.Bit32.isChecked():
					self.Game.deviceParam.Bits = 32
			elif caller == self.gui.MultiSample and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.deviceParam.AntiAlias = self.gui.MultiSample.getPos()
			elif caller == self.gui.Tesselation and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.loadParam.patchTesselation = self.gui.Tesselation.getPos()
			elif caller == self.gui.Gamma and gui_event_type == EGET_SCROLL_BAR_CHANGED:
				self.Game.GammaValue = self.gui.Gamma.getPos() * 0.01
				self.Game.Device.setGammaRamp(self.Game.GammaValue, self.Game.GammaValue, self.Game.GammaValue, 0.0, 0.0)
			elif caller == self.gui.SetVideoMode and gui_event_type == EGET_BUTTON_CLICKED:
				self.Game.retVal = 2
				self.Game.Device.closeDevice()
			elif caller == self.gui.Window and gui_event_type == EGET_ELEMENT_CLOSED:
				self.Game.Device.closeDevice()
			elif caller == self.gui.Collision and gui_event_type == EGET_CHECKBOX_CHANGED:
				# set fly through active
				self.Game.flyTroughState ^= 1
				self.Player[0].cam().setAnimateTarget(Game.flyTroughState == 0)
				#~ self.Game.Device.getLogger().log('collision %d\n' % bool(Game.flyTroughState == 0), ELL_INFORMATION)
			elif caller == self.gui.Visible_Map and gui_event_type == EGET_CHECKBOX_CHANGED:
				v = self.gui.Visible_Map.isChecked()
				if self.MapParent:
					#~ self.Game.Device.getLogger().log('static node set visible %d\n' % v, ELL_INFORMATION)
					self.MapParent.setVisible(v)
			elif caller == self.gui.Visible_Shader and gui_event_type == EGET_CHECKBOX_CHANGED:
				v = self.gui.Visible_Shader.isChecked()
				if self.ShaderParent:
					#~ self.Game.Device.getLogger().log('shader node set visible %d\n' % v, ELL_INFORMATION)
					self.ShaderParent.setVisible(v)
			elif caller == self.gui.Visible_Skydome and gui_event_type == EGET_CHECKBOX_CHANGED:
				if self.SkyNode:
					v = not self.SkyNode.isVisible()
					#~ self.Game.Device.getLogger().log('skynode set visible %d\n' % v, ELL_INFORMATION)
					self.SkyNode.setVisible(v)
			elif caller == self.gui.Respawn and gui_event_type == EGET_BUTTON_CLICKED:
				self.Player[0].respawn()
			return False

		# fire
		if ((event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_SPACE and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and event.MouseInput.Event == EMIE_LMOUSE_LEFT_UP)):
			camera = self.Game.Device.getSceneManager().getActiveCamera()
			if camera and camera.isInputReceiverEnabled():
				self.useItem(self.Player[0])
		# gui active
		if (event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_F1 and event.KeyInput.PressedDown == False) or (event.EventType == EET_MOUSE_INPUT_EVENT and event.MouseInput.Event == EMIE_RMOUSE_LEFT_UP):
			self.SetGUIActive(2)
		# check if user presses the key
		if event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.PressedDown == False:
			# Escape toggles camera Input
			if event.KeyInput.Key == KEY_ESCAPE:
				self.SetGUIActive(3)
			else:
				if event.KeyInput.Key == KEY_F11:
					# screenshot are taken without gamma!
					image = self.Game.Device.getVideoDriver().createScreenShot()
					if image:
						pos = vector3df()
						rot = vector3df()
						cam = self.Game.Device.getSceneManager().getActiveCamera()
						if cam:
							pos = cam.getPosition()
							rot = cam.getRotation()
						dName = ('null', 'software', 'burning', 'd3d8', 'd3d9', 'opengl')
						buf = '%s_%ls_%.0f_%.0f_%.0f_%.0f_%.0f_%.0f.jpg' % (dName[self.Game.Device.getVideoDriver().getDriverType()], self.Game.CurrentMapName, pos.X, pos.Y, pos.Z, rot.X, rot.Y, rot.Z)
						filename = buf
						filename.replace('/', '_')
						#~ self.Game.Device.getLogger().log('screenshot : %s\n' % filename, ELL_INFORMATION)
						self.Game.Device.getVideoDriver().writeImageToFile(image, filename, 100)
						#~ image.drop()
				else:
					if event.KeyInput.Key == KEY_F9:
						value = EDS_OFF
						self.Game.debugState = (self.Game.debugState + 1) & 3
						if self.Game.debugState == 1:
							value = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_BBOX_ALL
						elif self.Game.debugState == 2:
							value = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_SKELETON
						# set debug map data on/off
						if self.Game.debugState == EDS_OFF:
							self.Game.debugState = EDS_NORMALS | EDS_MESH_WIRE_OVERLAY | EDS_BBOX_ALL
						else:
							self.Game.debugState = EDS_OFF
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
						if event.KeyInput.Key == KEY_F8:
							# set gravity on/off
							self.Game.gravityState ^= 1
							gravity_state = 'none'
							if self.Game.gravityState:
								gravity_state = 'earth'
							self.Player[0].cam().setGravity(self.Player[0].getGravity(gravity_state))
							#~ self.Game.Device.getLogger().log('gravity %s\n' % gravity_state, ELL_INFORMATION)
						else:
							if event.KeyInput.Key == KEY_F7:
								# set fly through active
								self.Game.flyTroughState ^= 1
								self.Player[0].cam().setAnimateTarget(self.Game.flyTroughState == 0)
								if self.gui.Collision:
									self.gui.Collision.setChecked(self.Game.flyTroughState == 0)
								#~ self.Game.Device.getLogger().log('collision %d\n' % bool(Game.flyTroughState == 0), ELL_INFORMATION)
							else:
								if event.KeyInput.Key == KEY_F2:
									self.Player[0].respawn()
								else:
									if event.KeyInput.Key == KEY_F3:
										if self.MapParent:
											v = not self.MapParent.isVisible()
											#~ self.Game.Device.getLogger().log('static node set visible %d\n' % v, ELL_INFORMATION)
											self.MapParent.setVisible(v)
											if self.gui.Visible_Map:
												self.gui.Visible_Map.setChecked(v)
									else:
										if event.KeyInput.Key == KEY_F4:
											if self.ShaderParent:
												v = not self.ShaderParent.isVisible()
												#~ self.Game.Device.getLogger().log('shader node set visible %d\n' % v, ELL_INFORMATION)
												self.ShaderParent.setVisible(v)
												if self.gui.Visible_Shader:
													self.gui.Visible_Shader.setChecked(v)
										else:
											if event.KeyInput.Key == KEY_F5:
												if self.FogParent:
													v = not self.FogParent.isVisible()
													#~ self.Game.Device.getLogger().log('fog node set visible %d\n' % v, ELL_INFORMATION)
													self.FogParent.setVisible(v)
													if self.gui.Visible_Fog:
														self.gui.Visible_Fog.setChecked(v)
											else:
												if event.KeyInput.Key == KEY_F6:
													if self.UnresolvedParent:
														v = not self.UnresolvedParent.isVisible()
														#~ self.Game.Device.getLogger().log('unresolved node set visible %d\n' % v, ELL_INFORMATION)
														self.UnresolvedParent.setVisible(v)
														if self.gui.Visible_Unresolved:
															self.gui.Visible_Unresolved.setChecked(v)
		# check if user presses the key C ( for crouch)
		if event.EventType == EET_KEY_INPUT_EVENT and event.KeyInput.Key == KEY_KEY_C:
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
		imp = self.SParticleImpact()
		imp.when = 0
		start = camera.getPosition()
		if player.WeaponNode:
			start.X += 0.0
			start.Y += 0.0
			start.Z += 0.0
		end = camera.getTarget() - start
		end.normalize()
		start += end * 20.0
		end = start + (end * camera.getFarValue())
		triangle = triangle3df()
		line = line3df(start, end)
		hitNode = ISceneNode(0)
		
		if smgr.getSceneCollisionManager().getCollisionPoint(line, self.Meta, end, triangle, hitNode):
			out = triangle.getNormal()
			out.setLength(0.03)
			imp.when = 1
			imp.outVector = out
			imp.pos = end
			player.setAnim('pow')
			player.Anim[1].next += player.Anim[1].delta
		else:
			start = camera.getPosition()
			#if player.WeaponNode:
				#start.X += 10.0
				#start.Y += -5.0
				#start.Z += 1.0
			end = camera.getTarget() - start
			end.normalize()
			start += end*20.0
			end = start + (end * camera.getFarValue())
		node = smgr.addBillboardSceneNode(self.BulletParent, dimension2df(10, 10), start)
		node.setMaterialFlag(EMF_LIGHTING, False)
		node.setMaterialTexture(0, self.Game.Device.getVideoDriver().getTexture('fireball.bmp'))
		node.setMaterialFlag(EMF_ZWRITE_ENABLE, False)
		node.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
		length = (end - start).getLength()
		speed = 5.8
		try:
			time = int(length / speed)
		except:
			time = 1
		anim = smgr.createFlyStraightAnimator(start, end, time)
		node.addAnimator(anim)
		#~ anim.drop()
		bullet = 'nohit'
		if imp.when:
			bullet = 'hit'
		buf = 'bullet: %s on %.1f,%1.f,%1.f' % (bullet, end.X, end.Y, end.Z)
		node.setName(buf)
		anim = smgr.createDeleteAnimator(time)
		node.addAnimator(anim)
		#~ anim.drop()
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
		smoke = (smokeLayer('smoke2.jpg', 0.4, 1.5, 18.0, 20.0, 20, 50, 2000, 10000), smokeLayer('smoke3.jpg', 0.2, 1.2, 15.0, 20.0, 10, 30, 1000, 12000))
		i = 0
		g = 0
		factor = 1
		for g in range(2):
			smoke[g].minParticle *= factor
			smoke[g].maxParticle *= factor
			smoke[g].lifetime *= factor
			smoke[g].boxSize *= getNoiser() * 0.5
		#~ for i in range(len(self.Impacts)):
		for Impact in self.Impacts:
			#~ if now < self.Impacts[i].when:
			if now < Impact.when:
				continue
			# create smoke particle system
			pas = None
			for g in range(2):
				#~ pas = sm.addParticleSystemSceneNode(False, self.BulletParent, -1, self.Impacts[i].pos)
				pas = sm.addParticleSystemSceneNode(False, self.BulletParent, -1, Impact.pos)
				#~ buf = 'bullet impact smoke at %.1f,%.1f,%1.f' % (self.Impacts[i].pos.X, self.Impacts[i].pos.Y, self.Impacts[i].pos.Z)
				buf = 'bullet impact smoke at %.1f,%.1f,%1.f' % (Impact.pos.X, Impact.pos.Y, Impact.pos.Z)
				pas.setName(buf)
				# create a flat smoke
				#~ direction = self.Impacts[i].outVector
				direction = Impact.outVector
				direction *= smoke[g].scale
				em = pas.createBoxEmitter(aabbox3df(-4.0, 0.0, -4.0, 20.0, smoke[g].minparticleSize, 20.0), direction, smoke[g].minParticle, smoke[g].maxParticle, SColor(0,0,0,0), SColor(0,128,128,128), 250, 4000, 60)
				em.setMinStartSize(dimension2df(smoke[g].minparticleSize, smoke[g].minparticleSize))
				em.setMaxStartSize(dimension2df(smoke[g].maxparticleSize, smoke[g].maxparticleSize))
				pas.setEmitter(em)
				#~ em.drop()
				# particles get invisible
				paf = pas.createFadeOutParticleAffector(SColor(0, 0, 0, 0), smoke[g].fadeout)
				pas.addAffector(paf)
				#~ paf.drop()
				# particle system life time
				anim = sm.createDeleteAnimator(smoke[g].lifetime)
				pas.addAnimator(anim)
				#~ anim.drop()
				pas.setMaterialFlag(EMF_LIGHTING, False)
				pas.setMaterialFlag(EMF_ZWRITE_ENABLE, False)
				pas.setMaterialType(EMT_TRANSPARENT_VERTEX_ALPHA )
				pas.setMaterialTexture(0, self.Game.Device.getVideoDriver().getTexture(smoke[g].texture))
			# play impact sound
			#ifdef USE_IRRKLANG
			#~ if irrKlang:
				#audio::ISound* sound = irrKlang.play3D(impactSound, Impacts[i].pos, False, False, True)
				#~ audio::ISound* sound = irrKlang.play3D(impactSound, Impact.pos, False, False, True)
				#~ if sound:
					#~ # adjust max value a bit to make to sound of an impact louder
					#~ sound.setMinDistance(400)
					#~ sound.drop()
			#endif
			# delete entry
			#~ self.Impacts.erase(i)
			self.Impacts.remove(Impact)
			#~ i -= 1

	def Render(self):
		driver = self.Game.Device.getVideoDriver()
		if not driver:
			return
		driver.beginScene(True, True, self.scolor_scene)
		# TODO: This does not work, yet.
		anaglyph = False
		#~ anaglyph = True
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
			startMatrix *= move
			pos = startMatrix.getTranslation()
			driver.getOverrideMaterial().Material.ColorMask = ECP_RED
			driver.getOverrideMaterial().EnableFlags = EMF_COLOR_MASK
			driver.getOverrideMaterial().EnablePasses = ESNRP_SKY_BOX|ESNRP_SOLID|ESNRP_TRANSPARENT|ESNRP_TRANSPARENT_EFFECT|ESNRP_SHADOW
			camera.setPosition(pos)
			camera.setTarget(focusPoint)
			self.Game.Device.getSceneManager().drawAll()
			driver.clearZBuffer()
			#Right eye...
			move.setTranslation(vector3df(1.5,0.0,0.0))
			startMatrix *= move
			pos = startMatrix.getTranslation()
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
			msg = 'Q3 %s [%ls], FPS:%03d Tri:%.03fm Cull %d/%d nodes (%d,%d,%d)' % (self.Game.CurrentMapName, driver.getName(), driver.getFPS(), driver.getPrimitiveCountDrawn(0) * (1.0 / 1000000.0), attr.getAttributeAsInt('culled'), attr.getAttributeAsInt('calls'), attr.getAttributeAsInt('drawn_solid'), attr.getAttributeAsInt('drawn_transparent'), attr.getAttributeAsInt('drawn_transparent_effect'))
			self.Game.Device.setWindowCaption(msg)
			msg = '%03d fps, F1 GUI on/off, F2 respawn, F3-F6 toggle Nodes, F7 Collision on/off, F8 Gravity on/off, Right Mouse Toggle GUI' % self.Game.Device.getVideoDriver().getFPS()
			if self.gui.StatusLine:
				self.gui.StatusLine.setText(msg)
			player.Anim[0].flags &= ~FIRED
		# idle..
		if player.Anim[1].flags & FIRED:
			if player.animation == 'idle':
				player.setAnim('idle')
			player.Anim[1].flags &= ~FIRED
		self.createParticleImpacts(now)


def runGame(game):
	if game.retVal >= 3:
		return

	#~ game.Device = game.createExDevice(game.deviceParam)
	game.Device = createDevice(DRIVER_TYPE, dimension2du(800, 600), 16)
	if not game.Device:
		# could not create selected driver.
		game.retVal = 0
		return

	# create an event receiver based on current game data
	eventHandler = CQuake3EventHandler()
	eventHandler.init_game(game)

	# load stored config
	game.load('explorer.cfg')

	# add our media directory and archive to the file system
	for i in range(len(game.CurrentArchiveList)):
		eventHandler.AddArchive(game.CurrentArchiveList[i])
		#~ game.Device.getLogger().log('===' + game.CurrentArchiveList[i])

	# Load a Map or startup to the GUI
	if game.CurrentMapName:
		eventHandler.LoadMap(game.CurrentMapName, True)
		if not game.loadParam.loadSkyShader:
			eventHandler.AddSky(1, 'skydome2')
		eventHandler.CreatePlayers()
		eventHandler.CreateGUI()
		eventHandler.SetGUIActive(0)

		# set player to last position on restart
		if game.retVal == 2:
			eventHandler.GetPlayer(0).setpos(game.PlayerPosition, game.PlayerRotation)
	else:
		# start up empty
		eventHandler.AddSky(1, 'skydome2')
		eventHandler.CreatePlayers()
		eventHandler.CreateGUI()
		eventHandler.SetGUIActive(1)
		#~ background_music('IrrlichtTheme.ogg')

	game.retVal = 3
	while game.Device.run():
		eventHandler.Animate()
		eventHandler.Render()
		if not game.Device.isWindowActive():
			game.Device._yield()

	game.Device.setGammaRamp(1.0, 1.0, 1.0, 0.0, 0.0)
	eventHandler.uninit_game()

def deletePathFromPath(fullpath, item = 1):
	paths = list(os.path.split(fullpath))
	del paths[item]
	return paths[0]

def main():
	import sys
	prgname = sys.argv[0]
	game = GameData(deletePathFromPath(prgname, 1))
	# dynamically load irrlicht
	dllName = 'irrlicht_c.dll'
	if len(sys.argv) > 1:
		dllName = sys.argv[1]
	game.createExDevice = createDeviceEx
	if 0 == game.createExDevice:
		game.retVal = 3
		print('Could not load %s.\n' % dllName)
		return game.retVal # could not load dll
	# start without asking for driver
	game.retVal = 1
	while game.retVal < 3:
		# if driver could not created, ask for another driver
		if game.retVal == 0:
			game.setDefault()
			# ask user for driver
			game.deviceParam.DriverType = DRIVER_TYPE
			if game.deviceParam.DriverType == EDT_COUNT:
				game.retVal = 3
		runGame(game)
	return game.retVal

if __name__ == '__main__':
	main()
from pyirrlicht import *

Device = None
StartUpModelFile = ''
Caption = ''
MessageText = ''
Model = None
SkyBox = None
Octree = False
UseLight = False

Camera = [None, None]

# Values used to identify individual GUI elements
GUI_ID_DIALOG_ROOT_WINDOW = 0x10000

GUI_ID_X_SCALE = 0x10001
GUI_ID_Y_SCALE = 0x10002
GUI_ID_Z_SCALE = 0x10003

GUI_ID_OPEN_MODEL = 0x10004
GUI_ID_SET_MODEL_ARCHIVE = 0x10005
GUI_ID_LOAD_AS_OCTREE = 0x10006

GUI_ID_SKY_BOX_VISIBLE = 0x10007
GUI_ID_TOGGLE_DEBUG_INFO = 0x10008

GUI_ID_DEBUG_OFF = 0x10009
GUI_ID_DEBUG_BOUNDING_BOX = 0x10010
GUI_ID_DEBUG_NORMALS = 0x10011
GUI_ID_DEBUG_SKELETON = 0x10012
GUI_ID_DEBUG_WIRE_OVERLAY = 0x10013
GUI_ID_DEBUG_HALF_TRANSPARENT = 0x10014
GUI_ID_DEBUG_BUFFERS_BOUNDING_BOXES = 0x10015
GUI_ID_DEBUG_ALL = 0x10016

GUI_ID_MODEL_MATERIAL_SOLID = 0x10017
GUI_ID_MODEL_MATERIAL_TRANSPARENT = 0x10018
GUI_ID_MODEL_MATERIAL_REFLECTION = 0x10019

GUI_ID_CAMERA_MAYA = 0x10020
GUI_ID_CAMERA_FIRST_PERSON = 0x10021

GUI_ID_POSITION_TEXT = 0x10022

GUI_ID_ABOUT = 0x10023
GUI_ID_QUIT = 0x10024

GUI_ID_TEXTUREFILTER = 0x10025
GUI_ID_SKIN_TRANSPARENCY = 0x10026
GUI_ID_SKIN_ANIMATION_FPS = 0x10027

GUI_ID_BUTTON_SET_SCALE = 0x10028
GUI_ID_BUTTON_SCALE_MUL10 = 0x10029
GUI_ID_BUTTON_SCALE_DIV10 = 0x10030
GUI_ID_BUTTON_OPEN_MODEL = 0x10031
GUI_ID_BUTTON_SHOW_ABOUT = 0x10032
GUI_ID_BUTTON_SHOW_TOOLBOX = 0x10033
GUI_ID_BUTTON_SELECT_ARCHIVE = 0x10034

GUI_ID_ANIMATION_INFO = 0x10035

# And some magic numbers
MAX_FRAMERATE = 80
DEFAULT_FRAMERATE = 30


#Toggle between various cameras
def setActiveCamera(newActive):
	global Device
	if Device:
		active = Device.getSceneManager().getActiveCamera()
		active.setInputReceiverEnabled(False)
		newActive.setInputReceiverEnabled(True)
		Device.getSceneManager().setActiveCamera(newActive)

#Set the skin transparency by changing the alpha values of all skin-colors
def SetSkinTransparency(alpha, skin):
	for i in range(EGDC_COUNT):
		col = skin.getColor(i)
		col.setAlpha(alpha)
		skin.setColor(i, col)
		if (i + 2) > EGDC_COUNT:
			break

#Update the display of the model scaling
def UpdateScaleInfo(model):
	global Device
	toolboxWnd = Device.getGUIEnvironment().getRootGUIElement().getElementFromId(GUI_ID_DIALOG_ROOT_WINDOW, True)
	if toolboxWnd:
		if model:
			scale = model.getScale()
			toolboxWnd.getElementFromId(GUI_ID_X_SCALE, True).setText( str(scale.X) )
			toolboxWnd.getElementFromId(GUI_ID_Y_SCALE, True).setText( str(scale.Y) )
			toolboxWnd.getElementFromId(GUI_ID_Z_SCALE, True).setText( str(scale.Z) )
		else:
			toolboxWnd.getElementFromId(GUI_ID_X_SCALE, True).setText( "-" )
			toolboxWnd.getElementFromId(GUI_ID_Y_SCALE, True).setText( "-" )
			toolboxWnd.getElementFromId(GUI_ID_Z_SCALE, True).setText( "-" )

# The three following functions do several stuff used by the mesh viewer. The
# first function showAboutText() simply displays a messagebox with a caption and
# a message text. The texts will be stored in the MessageText and Caption
# variables at startup.
def showAboutText():
	global Device, Caption, MessageText
	# create modal message box with the text
	# loaded from the xml file.
	Device.getGUIEnvironment().addMessageBox(Caption, MessageText)


# The second function loadModel() loads a model and displays it using an
# addAnimatedMeshSceneNode and the scene manager. Nothing difficult. It also
# displays a short message box, if the model could not be loaded.
def loadModel(fn):
	global Device, StartUpModelFile, Model, Octree, UseLight
	# modify the name if it a .pk3 file
	filename = fn
	extension = ''
	name_ext = filename.rsplit('.', 1)
	if len(name_ext) > 1:
		extension = name_ext[1].lower()
	#~ Device.getLogger().log(filename + '|' + extension)

	# if a texture is loaded apply it to the current model..
	if extension in (".jpg", ".pcx", ".jpg", ".pcx", ".png", ".ppm", ".pgm", ".pbm", ".psd", ".tga", ".bmp", ".wal", ".rgb", '.rgba'):
		texture = Device.getVideoDriver().getTexture( filename )
		if texture and Model:
			# always reload texture
			Device.getVideoDriver().removeTexture(texture)
			texture = Device.getVideoDriver().getTexture( filename )
			Model.setMaterialTexture(0, texture)
	# if a archive is loaded add it to the FileArchive..
	elif extension in (".pk3", ".zip", ".pak", ".npk"):
		Device.getFileSystem().addFileArchive(filename)

	# load a model into the engine
	if Model:
		Model.remove()
	Model = None

	if extension==".irr":
		outNodes = arrayISceneNode()
		Device.getSceneManager().loadScene(filename)
		Device.getSceneManager().getSceneNodesFromType(ESNT_ANIMATED_MESH, outNodes)
		if outNodes.size():
			Model = outNodes[0]
	m = Device.getSceneManager().getMesh(filename)
	if not m:
		# model could not be loaded
		if StartUpModelFile != filename:
			Device.getGUIEnvironment().addMessageBox(Caption, "The model could not be loaded. Maybe it is not a supported file format.")
	else:
		# set default material properties
		if Octree:
			Model = Device.getSceneManager().addOctreeSceneNode(m.getMesh(0))
		else:
			animModel = Device.getSceneManager().addAnimatedMeshSceneNode(m)
			animModel.setAnimationSpeed(30)
			Model = animModel
		Model.setMaterialFlag(EMF_LIGHTING, UseLight)
		Model.setMaterialFlag(EMF_NORMALIZE_NORMALS, UseLight)
		#Model.setMaterialFlag(EMF_BACK_FACE_CULLING, False)
		Model.setDebugDataVisible(EDS_OFF)

		# we need to uncheck the menu entries. would be cool to fake a menu event, but
		# that's not so simple. so we do it brute force
		menu = Device.getGUIEnvironment().getRootGUIElement().getElementFromId(GUI_ID_TOGGLE_DEBUG_INFO, True).as_IGUIContextMenu()
		if menu:
			for item in range(6):
				menu.setItemChecked(item, False)
				if (item + 2) > 6:
					break
		UpdateScaleInfo(Model)


# Finally, the third function creates a toolbox window. In this simple mesh
# viewer, this toolbox only contains a tab control with three edit boxes for
# changing the scale of the displayed model.
def createToolBox():
	global Device, Model
	# remove tool box if already there
	env = Device.getGUIEnvironment()
	root = env.getRootGUIElement()
	e = root.getElementFromId(GUI_ID_DIALOG_ROOT_WINDOW, True)
	if e:
		e.remove()
	# create the toolbox window
	wnd = env.addWindow(recti(600,45,800,480), False, "Toolset", id = GUI_ID_DIALOG_ROOT_WINDOW)
	# create tab control and tabs
	tab = env.addTabControl(recti(2,20,800-602,480-7), wnd, True, True)
	t1 = tab.addTab("Config")
	# add some edit boxes and a button to tab one
	env.addStaticText("Scale:", recti(10,20,60,45), False, False, t1)
	env.addStaticText("X:", recti(22,48,40,66), False, False, t1)
	env.addEditBox("1.0", recti(40,46,130,66), True, t1, GUI_ID_X_SCALE)
	env.addStaticText("Y:", recti(22,82,40,GUI_ID_OPEN_MODEL), False, False, t1)
	env.addEditBox("1.0", recti(40,76,130,96), True, t1, GUI_ID_Y_SCALE)
	env.addStaticText("Z:", recti(22,108,40,126), False, False, t1)
	env.addEditBox("1.0", recti(40,106,130,126), True, t1, GUI_ID_Z_SCALE)

	env.addButton(recti(10,134,85,165), t1, GUI_ID_BUTTON_SET_SCALE, "Set")

	# quick scale buttons
	env.addButton(recti(65,20,95,40), t1, GUI_ID_BUTTON_SCALE_MUL10, "* 10")
	env.addButton(recti(100,20,130,40), t1, GUI_ID_BUTTON_SCALE_DIV10, "* 0.1")

	UpdateScaleInfo(Model)

	# add transparency control
	env.addStaticText("GUI Transparency Control:", recti(10,200,150,225), True, False, t1)
	# add IGUIScrollBar
	scrollbar = env.addScrollBar(True, recti(10,225,150,240), t1, GUI_ID_SKIN_TRANSPARENCY)
	scrollbar.setMax(255)
	scrollbar.setPos(255)

	# add framerate control
	env.addStaticText("Framerate:", recti(12,240,75,265), False, False, t1)
	env.addStaticText("", recti(75,240,200,265), False, False, t1, GUI_ID_ANIMATION_INFO)
	scrollbar = env.addScrollBar(True, recti(10,265,150,280), t1, GUI_ID_SKIN_ANIMATION_FPS)
	scrollbar.setMax(MAX_FRAMERATE)
	scrollbar.setMin(-MAX_FRAMERATE)
	scrollbar.setPos(DEFAULT_FRAMERATE)
	scrollbar.setSmallStep(1)

	# bring irrlicht engine logo to front, because it
	# now may be below the newly created toolbox
	root.bringToFront(root.getElementFromId(666, True))

def updateToolBox():
	global Device, Model
	if Device and Model:
		env = Device.getGUIEnvironment()
		root = env.getRootGUIElement()
		dlg = root.getElementFromId(GUI_ID_DIALOG_ROOT_WINDOW, True)
		if dlg:
			# update the info we have about the animation of the model
			aniInfo = dlg.getElementFromId(GUI_ID_ANIMATION_INFO, True)
			if aniInfo:
				if ESNT_ANIMATED_MESH == Model.getType():
					#~ animatedModel = IAnimatedMeshSceneNode(other = Model)
					animatedModel = IAnimatedMeshSceneNode(Model)
					aniInfo.setText("%d Frame: %d" % (animatedModel.getAnimationSpeed(), animatedModel.getFrameNr()))
				else:
					aniInfo.setText("")

# To get all the events sent by the GUI Elements, we need to create an event
# receiver. This one is really simple. If an event occurs, it checks the id of
# the caller and the event type, and starts an action based on these values. For
# example, if a menu item with id GUI_ID_OPEN_MODEL was selected, if opens a file-open-dialog.
class MyEventReceiver(IEventReceiver):
	def OnEvent(self, event):
		global Device, Model
		event_type = self.GetEventType(event)
		# Escape swaps Camera Input
		if event_type == EET_KEY_INPUT_EVENT:
			Device.getLogger().log('=EET_KEY_INPUT_EVENT')
			key_event = self.GetKeyInput(event)
			if not self.KeyInput_PressedDown(key_event):
				if self.OnKeyUp(self.KeyInput_Key(key_event)):
					return True
		if (event_type == EET_GUI_EVENT) and Device:
			Device.getLogger().log('=EET_GUI_EVENT')
			gui_event = self.GetGUIEvent(event)
			gui_event_type = self.GUIEvent_EventType(gui_event)
			caller = self.GUIEvent_Caller(gui_event)
			id = caller.getID()
			env = Device.getGUIEnvironment()
			if gui_event_type == EGET_MENU_ITEM_SELECTED:
				Device.getLogger().log('=EGET_MENU_ITEM_SELECTED')
				# a menu item was clicked
				self.OnMenuItemSelected(caller.as_IGUIContextMenu())
			elif gui_event_type == EGET_FILE_SELECTED:
				Device.getLogger().log('=EGET_FILE_SELECTED')
				# load the model file, selected in the file open dialog
				dialog = caller.as_IGUIFileOpenDialog()
				loadModel(dialog.getFileName())
			if gui_event_type == EGET_SCROLL_BAR_CHANGED:
				Device.getLogger().log('=EGET_SCROLL_BAR_CHANGED')
				scroll_bar = caller.as_IGUIScrollBar()
				# control skin transparency
				if id == GUI_ID_SKIN_TRANSPARENCY:
					SetSkinTransparency(scroll_bar.getPos(), env.getSkin())
				# control animation speed
				elif id == GUI_ID_SKIN_ANIMATION_FPS:
					if ESNT_ANIMATED_MESH == Model.getType():
						Model.setAnimationSpeed(scroll_bar.getPos())
			if gui_event_type == EGET_COMBO_BOX_CHANGED:
				Device.getLogger().log('=EGET_COMBO_BOX_CHANGED')
				# control anti-aliasing/filtering
				if id == GUI_ID_TEXTUREFILTER:
					self.OnTextureFilterSelected(caller.as_IGUIComboBox())
			if gui_event_type == EGET_BUTTON_CLICKED:
				Device.getLogger().log('=EGET_BUTTON_CLICKED')
				if id == GUI_ID_BUTTON_SET_SCALE:
					# set scale
					root = env.getRootGUIElement()
					scale = vector3df()
					s = root.getElementFromId(GUI_ID_X_SCALE, True).getText()
					scale.X = float(s)
					s = root.getElementFromId(GUI_ID_Y_SCALE, True).getText()
					scale.Y = float(s)
					s = root.getElementFromId(GUI_ID_Z_SCALE, True).getText()
					scale.Z = float(s)
					if Model:
						Model.setScale(scale)
					UpdateScaleInfo(Model)
				elif id == GUI_ID_BUTTON_SCALE_MUL10:
					if Model:
						Model.setScale(Model.getScale()*10.0)
					UpdateScaleInfo(Model)
				elif id == GUI_ID_BUTTON_SCALE_DIV10:
					if Model:
						Model.setScale(Model.getScale()*0.1)
					UpdateScaleInfo(Model)
				elif id == GUI_ID_BUTTON_OPEN_MODEL:
					env.addFileOpenDialog("Please select a model file to open")
				elif id == GUI_ID_BUTTON_SHOW_ABOUT:
					showAboutText()
				elif id == GUI_ID_BUTTON_SHOW_TOOLBOX:
					createToolBox()
				elif id == GUI_ID_BUTTON_SELECT_ARCHIVE:
					env.addFileOpenDialog("Please select your game archive/directory")
		return False

	# Handle key-up events
	def OnKeyUp(self, keyCode):
		global Device, Model, UseLight
		if keyCode == KEY_ESCAPE:
			Device.getLogger().log('=KEY_ESCAPE')
			if Device:
				camera = Device.getSceneManager().getActiveCamera()
				if camera:
					camera.setInputReceiverEnabled( not camera.isInputReceiverEnabled() )
				return True
		elif keyCode == KEY_F1:
			Device.getLogger().log('=KEY_F1')
			if Device:
				elem = Device.getGUIEnvironment().getRootGUIElement().getElementFromId(GUI_ID_POSITION_TEXT)
				if elem:
					elem.setVisible(not elem.isVisible())
		elif keyCode == KEY_KEY_M:
			Device.getLogger().log('=KEY_KEY_M')
			if Device:
				Device.minimizeWindow()
		elif keyCode == KEY_KEY_L:
			Device.getLogger().log('=KEY_KEY_L')
			UseLight = not UseLight
			if Model:
				Model.setMaterialFlag(EMF_LIGHTING, UseLight)
				Model.setMaterialFlag(EMF_NORMALIZE_NORMALS, UseLight)
		return False

	# Handle "menu item clicked" events.
	def OnMenuItemSelected(self, menu):
		global Device, Model, SkyBox, Octree, Camera
		id = menu.getItemCommandId(menu.getSelectedItem())
		env = Device.getGUIEnvironment()
		if id == GUI_ID_OPEN_MODEL: # FilOnButtonSetScalinge . Open Model
			env.addFileOpenDialog("Please select a model file to open")
		elif id == GUI_ID_SET_MODEL_ARCHIVE: # File . Set Model Archive
			env.addFileOpenDialog("Please select your game archive/directory")
		elif id == GUI_ID_LOAD_AS_OCTREE: # File . LoadAsOctree
			Octree = not Octree
			menu.setItemChecked(menu.getSelectedItem(), Octree)
		elif id == GUI_ID_QUIT: # File . Quit
			Device.closeDevice()
		elif id == GUI_ID_SKY_BOX_VISIBLE: # View . Skybox
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			SkyBox.setVisible(not SkyBox.isVisible())
		elif id == GUI_ID_DEBUG_OFF: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem()+1, False)
			menu.setItemChecked(menu.getSelectedItem()+2, False)
			menu.setItemChecked(menu.getSelectedItem()+3, False)
			menu.setItemChecked(menu.getSelectedItem()+4, False)
			menu.setItemChecked(menu.getSelectedItem()+5, False)
			menu.setItemChecked(menu.getSelectedItem()+6, False)
			if Model:
				Model.setDebugDataVisible(EDS_OFF)
		elif id == GUI_ID_DEBUG_BOUNDING_BOX: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_BBOX))
		elif id == GUI_ID_DEBUG_NORMALS: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_NORMALS))
		elif id == GUI_ID_DEBUG_SKELETON: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_SKELETON))
		elif id == GUI_ID_DEBUG_WIRE_OVERLAY: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_MESH_WIRE_OVERLAY))
		elif id == GUI_ID_DEBUG_HALF_TRANSPARENT: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_HALF_TRANSPARENCY))
		elif id == GUI_ID_DEBUG_BUFFERS_BOUNDING_BOXES: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem(), not menu.isItemChecked(menu.getSelectedItem()))
			if Model:
				Model.setDebugDataVisible((E_DEBUG_SCENE_TYPE)+(Model.isDebugDataVisible()^EDS_BBOX_BUFFERS))
		elif id == GUI_ID_DEBUG_ALL: # View . Debug Information
			menu.setItemChecked(menu.getSelectedItem()-1, True)
			menu.setItemChecked(menu.getSelectedItem()-2, True)
			menu.setItemChecked(menu.getSelectedItem()-3, True)
			menu.setItemChecked(menu.getSelectedItem()-4, True)
			menu.setItemChecked(menu.getSelectedItem()-5, True)
			menu.setItemChecked(menu.getSelectedItem()-6, True)
			if Model:
				Model.setDebugDataVisible(EDS_FULL)
		elif id == GUI_ID_ABOUT: # Help.About
			showAboutText()
		elif id == GUI_ID_MODEL_MATERIAL_SOLID: # View . Material . Solid
			if Model:
				Model.setMaterialType(EMT_SOLID)
		elif id == GUI_ID_MODEL_MATERIAL_TRANSPARENT: # View . Material . Transparent
			if Model:
				Model.setMaterialType(EMT_TRANSPARENT_ADD_COLOR)
		elif id == GUI_ID_MODEL_MATERIAL_REFLECTION: # View . Material . Reflection
			if Model:
				Model.setMaterialType(EMT_SPHERE_MAP)
		elif id == GUI_ID_CAMERA_MAYA:
			setActiveCamera(Camera[0])
		elif id == GUI_ID_CAMERA_FIRST_PERSON:
			setActiveCamera(Camera[1])

	# Handle the event that one of the texture-filters was selected in the corresponding combobox.
	def OnTextureFilterSelected(self, combo):
		global Model
		if Model:
			pos = combo.getSelected()
			if pos == 0:
				Model.setMaterialFlag(EMF_BILINEAR_FILTER, False)
				Model.setMaterialFlag(EMF_TRILINEAR_FILTER, False)
				Model.setMaterialFlag(EMF_ANISOTROPIC_FILTER, False)
			elif pos == 1:
				Model.setMaterialFlag(EMF_BILINEAR_FILTER, True)
				Model.setMaterialFlag(EMF_TRILINEAR_FILTER, False)
			elif pos == 2:
				Model.setMaterialFlag(EMF_BILINEAR_FILTER, False)
				Model.setMaterialFlag(EMF_TRILINEAR_FILTER, True)
			elif pos == 3:
				Model.setMaterialFlag(EMF_ANISOTROPIC_FILTER, True)
			elif pos == 4:
				Model.setMaterialFlag(EMF_ANISOTROPIC_FILTER, False)


# Most of the hard work is done. We only need to create the Irrlicht Engine
# device and all the buttons, menus and toolbars. We start up the engine as
# usual, using createDevice(). To make our application catch events, we set our
# eventreceiver as parameter. As you can see, there is also a call to
# IrrlichtDevice::setResizeable(). This makes the render window resizeable, which
# is quite useful for a mesh viewer.
def main():
	global Device, StartUpModelFile, Caption, MessageText, SkyBox
	from sys import argv
	# create device and exit if creation failed
	#~ driverType = EDT_NULL
	#~ driverType = EDT_SOFTWARE
	#~ driverType = EDT_BURNINGSVIDEO
	#~ driverType = EDT_DIRECT3D8
	#~ driverType = EDT_DIRECT3D9
	driverType = EDT_OPENGL
	receiver = MyEventReceiver()
	Device = createDevice(driverType, dimension2du(800, 600), 16, False, False, False, receiver)
	#~ Device = createDevice(driverType, dimension2du(800, 600), 16)

	if not Device:
		#~ print('could not create selected driver.')
		return 1

	Device.setResizable(True)

	Device.setWindowCaption("Irrlicht Engine - Loading...")

	driver = Device.getVideoDriver()
	env = Device.getGUIEnvironment()
	smgr = Device.getSceneManager()
	#~ smgr.getParameters().setAttribute(COLLADA_CREATE_SCENE_INSTANCES, True)
	smgr.getParameters().setAttribute13("COLLADA_CreateSceneInstances", True)

	driver.setTextureCreationFlag(ETCF_ALWAYS_32_BIT, True)

	smgr.addLightSceneNode(0, vector3df(200,200,200), SColorf(1.0,1.0,1.0), 2000)
	smgr.setAmbientLight(SColorf(0.3,0.3,0.3))
	# add our media directory as "search path"
	if IRRLICHT_VERSION < 180:
		Device.getFileSystem().addFolderFileArchive("media/")
	else:
		Device.getFileSystem().addFileArchive("media/")

	#~ The next step is to read the configuration file. It is stored in the xml
	#~ format and looks a little bit like this:

	#~ @verbatim
	#~ <?xml version="1.0"?>
	#~ <config>
		#~ <startUpModel file="some filename" />
		#~ <messageText caption="Irrlicht Engine Mesh Viewer">
			#~ Hello!
		#~ </messageText>
	#~ </config>
	#~ @endverbatim

	#~ We need the data stored in there to be written into the global variables
	#~ StartUpModelFile, MessageText and Caption. This is now done using the
	#~ Irrlicht Engine integrated XML parser:

	# read configuration from xml file (IXMLReader)
	xml = Device.getFileSystem().createXMLReader("config.xml")
	if xml:
		while xml.read():
			switch_case = xml.getNodeType()
			if switch_case == EXN_TEXT:
				# in this xml file, the only text which occurs is the
				# messageText
				MessageText = xml.getNodeData()
			elif switch_case == EXN_ELEMENT:
				node_name = xml.getNodeName()
				if node_name == "startUpModel":
					StartUpModelFile = xml.getAttributeValue("file")
				elif node_name == "messageText":
					Caption = xml.getAttributeValue("caption")
		xml.drop() # don't forget to delete the xml reader

	if len(argv) > 1:
		StartUpModelFile = argv[1]

	# That wasn't difficult. Now we'll set a nicer font and create the Menu.
	# It is possible to create submenus for every menu item. The call
	# menu.addItem("File", -1, True, True) for example adds a new menu
	# Item with the name "File" and the id -1. The following parameter says
	# that the menu item should be enabled, and the last one says, that there
	# should be a submenu. The submenu can now be accessed with
	# menu.getSubMenu(0), because the "File" entry is the menu item with
	# index 0.

	# set a nicer font
	skin = env.getSkin()
	font = env.getFont("fonthaettenschweiler.bmp")
	if font:
		skin.setFont(font)

	# create IGUIContextMenu
	menu = env.addMenu()
	menu.addItem("File", -1, True, True)
	menu.addItem("View", -1, True, True)
	menu.addItem("Camera", -1, True, True)
	menu.addItem("Help", -1, True, True)

	submenu = menu.getSubMenu(0)
	submenu.addItem("Open Model File & Texture...", GUI_ID_OPEN_MODEL)
	submenu.addItem("Set Model Archive...", GUI_ID_SET_MODEL_ARCHIVE)
	submenu.addItem("Load as Octree", GUI_ID_LOAD_AS_OCTREE)
	submenu.addSeparator()
	submenu.addItem("Quit", GUI_ID_QUIT)

	submenu = menu.getSubMenu(1)
	submenu.addItem("sky box visible", GUI_ID_SKY_BOX_VISIBLE, True, False, True)
	submenu.addItem("toggle model debug information", GUI_ID_TOGGLE_DEBUG_INFO, True, True)
	submenu.addItem("model material", -1, True, True)

	submenu = submenu.getSubMenu(1)
	submenu.addItem("Off", GUI_ID_DEBUG_OFF)
	submenu.addItem("Bounding Box", GUI_ID_DEBUG_BOUNDING_BOX)
	submenu.addItem("Normals", GUI_ID_DEBUG_NORMALS)
	submenu.addItem("Skeleton", GUI_ID_DEBUG_SKELETON)
	submenu.addItem("Wire overlay", GUI_ID_DEBUG_WIRE_OVERLAY)
	submenu.addItem("Half-Transparent", GUI_ID_DEBUG_HALF_TRANSPARENT)
	submenu.addItem("Buffers bounding boxes", GUI_ID_DEBUG_BUFFERS_BOUNDING_BOXES)
	submenu.addItem("All", GUI_ID_DEBUG_ALL)

	submenu = menu.getSubMenu(1).getSubMenu(2)
	submenu.addItem("Solid", GUI_ID_MODEL_MATERIAL_SOLID)
	submenu.addItem("Transparent", GUI_ID_MODEL_MATERIAL_TRANSPARENT)
	submenu.addItem("Reflection", GUI_ID_MODEL_MATERIAL_REFLECTION)

	submenu = menu.getSubMenu(2)
	submenu.addItem("Maya Style", GUI_ID_CAMERA_MAYA)
	submenu.addItem("First Person", GUI_ID_CAMERA_FIRST_PERSON)

	submenu = menu.getSubMenu(3)
	submenu.addItem("About", GUI_ID_ABOUT)

	# Below the menu we want a toolbar, onto which we can place colored
	# buttons and important looking stuff like a senseless combobox.

	# create toolbar
	bar = env.addToolBar()
	image = driver.getTexture("open.png")
	bar.addButton(GUI_ID_BUTTON_OPEN_MODEL, '', "Open a model",image, None, False, True)
	image = driver.getTexture("tools.png")
	bar.addButton(GUI_ID_BUTTON_SHOW_TOOLBOX, '', "Open Toolset",image, None, False, True)
	image = driver.getTexture("zip.png")
	bar.addButton(GUI_ID_BUTTON_SELECT_ARCHIVE, '', "Set Model Archive",image, None, False, True)
	image = driver.getTexture("help.png")
	bar.addButton(GUI_ID_BUTTON_SHOW_ABOUT, '', "Open Help", image, None, False, True)

	# create a combobox with some senseless texts
	box = env.addComboBox(recti(250,4,350,23), bar, GUI_ID_TEXTUREFILTER)
	box.addItem("No filtering")
	box.addItem("Bilinear")
	box.addItem("Trilinear")
	box.addItem("Anisotropic")
	box.addItem("Isotropic")

	# To make the editor look a little bit better, we disable transparent gui
	# elements, and add an Irrlicht Engine logo. In addition, a text showing
	# the current frames per second value is created and the window caption is
	# changed.

	# disable alpha
	skin = env.getSkin()
	for i in range(EGDC_COUNT):
		col = skin.getColor(i)
		old_alpha = col.getAlpha()
		col.setAlpha(255)
		skin.setColor(i, col)

	# add a tabcontrol
	createToolBox()

	# create fps text
	fpstext = env.addStaticText("", recti(400,4,570,23), True, False, bar)
	postext = env.addStaticText("", recti(10,50,470,80),False, False, id = GUI_ID_POSITION_TEXT)
	postext.setVisible(False)

	# set window caption
	Caption += " - [" + driver.getName() + "]"
	Device.setWindowCaption(Caption)

	# That's nearly the whole application. We simply show the about message
	# box at start up, and load the first model. To make everything look
	# better, a skybox is created and a user controled camera, to make the
	# application a little bit more interactive. Finally, everything is drawn
	# in a standard drawing loop.

	# show about message box and load default model
	if len(argv) == 1:
		showAboutText()
	loadModel(StartUpModelFile)

	# add skybox
	SkyBox = smgr.addSkyBoxSceneNode(
		driver.getTexture("irrlicht2_up.jpg"),
		driver.getTexture("irrlicht2_dn.jpg"),
		driver.getTexture("irrlicht2_lf.jpg"),
		driver.getTexture("irrlicht2_rt.jpg"),
		driver.getTexture("irrlicht2_ft.jpg"),
		driver.getTexture("irrlicht2_bk.jpg"))

	# add a camera scene node
	Camera[0] = smgr.addCameraSceneNodeMaya()
	Camera[0].setFarValue(20000.0)
	# Maya cameras reposition themselves relative to their target, so target the location
	# where the mesh scene node is placed.
	Camera[0].setTarget(vector3df(0,30,0))

	Camera[1] = smgr.addCameraSceneNodeFPS()
	Camera[1].setFarValue(20000.0)
	Camera[1].setPosition(vector3df(0,0,-70))
	Camera[1].setTarget(vector3df(0,30,0))

	setActiveCamera(Camera[0])

	# load the irrlicht engine logo
	img = env.addImage(driver.getTexture("irrlichtlogo2.png"), position2di(10, driver.getScreenSize().Height - 128))

	# lock the logo's edges to the bottom left corner of the screen
	img.setAlignment(EGUIA_UPPERLEFT, EGUIA_UPPERLEFT, EGUIA_LOWERRIGHT, EGUIA_LOWERRIGHT)

	# draw everything
	while Device.run() and driver:
		if Device.isWindowActive():
			driver.beginScene(True, True, SColor(150,50,50,50))
			smgr.drawAll()
			env.drawAll()
			driver.endScene()

			str_fps = "FPS: %d" % driver.getFPS() + " Tris: %d" % driver.getPrimitiveCountDrawn()
			fpstext.setText(str_fps)

			# get ICameraSceneNode
			cam = Device.getSceneManager().getActiveCamera()
			s = "Pos: " + str(cam.getPosition().X)
			s += " " + str(cam.getPosition().Y)
			s += " " + str(cam.getPosition().Z)
			s += " Tgt: " + str(cam.getTarget().X)
			s += " " + str(cam.getTarget().Y)
			s += " " + str(cam.getTarget().Z)
			postext.setText(s)

			# update the tool dialog
			updateToolBox()

			#~ Device.sleep(10)
		else:
			Device._yield()
	Device.drop()

if __name__ == "__main__":
	main()
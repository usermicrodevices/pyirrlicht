from pyirrlicht import *

GUI_ID_QUIT_BUTTON = 101
GUI_ID_NEW_WINDOW_BUTTON = 102
GUI_ID_FILE_OPEN_BUTTON = 103
GUI_ID_TRANSPARENCY_SCROLL_BAR = 104

#~ driverType = EDT_NULL
driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
#~ driverType = EDT_OPENGL

class SAppContext:
	device = None
	counter = 0
	listbox = None

class MyEventReceiver(IEventReceiver):
	Context = SAppContext()
	def OnEvent(self, evt):
		event = SEvent(evt)
		if event.EventType == EET_GUI_EVENT:
			id = event.GUIEvent.Caller.getID()
			env = self.Context.device.getGUIEnvironment()
			if event.GUIEvent.EventType == EGET_SCROLL_BAR_CHANGED:
				if id == GUI_ID_TRANSPARENCY_SCROLL_BAR:
					pos = IGUIScrollBar(event.GUIEvent.Caller).getPos()
					for i in range(EGDC_COUNT):
						col = env.getSkin().getColor(i)
						col.setAlpha(pos)
						env.getSkin().setColor(i, col)
			elif event.GUIEvent.EventType == EGET_BUTTON_CLICKED:
				if id == GUI_ID_QUIT_BUTTON:
					self.Context.device.closeDevice()
					return True
				elif id == GUI_ID_NEW_WINDOW_BUTTON:
					self.Context.listbox.addItem("Window created")
					self.Context.counter += 30
					if self.Context.counter > 200:
						self.Context.counter = 0
					window = env.addWindow(recti(100 + self.Context.counter, 100 + self.Context.counter, 300 + self.Context.counter, 200 + self.Context.counter), False, "Test window")
					env.addStaticText("Please close me", recti(35,35,140,50), True, False, window)
					return True
				elif id == GUI_ID_FILE_OPEN_BUTTON:
					self.Context.listbox.addItem("File open")
					env.addFileOpenDialog("Please choose a file.")
					return True
				else:
					return False
		return False

def main():
	if driverType == EDT_COUNT:
		return

	device = createDevice(driverType, dimension2du(640, 480))

	if not device:
		return

	device.setWindowCaption("Irrlicht Engine - User Interface Demo")
	device.setResizable(True)

	driver = device.getVideoDriver()
	env = device.getGUIEnvironment()

	skin = env.getSkin()
	font = env.getFont("media/fonthaettenschweiler.bmp")
	if font:
		skin.setFont(font)

	skin.setFont(env.getBuiltInFont(), EGDF_TOOLTIP)

	env.addButton(recti(10,240,110,240 + 32), 0, GUI_ID_QUIT_BUTTON, "Quit", "Exits Program")
	env.addButton(recti(10,280,110,280 + 32), 0, GUI_ID_NEW_WINDOW_BUTTON, "New Window", "Launches a new Window")
	env.addButton(recti(10,320,110,320 + 32), 0, GUI_ID_FILE_OPEN_BUTTON, "File Open", "Opens a file")

	env.addStaticText("Transparent Control:", recti(150,20,350,40), True)
	scrollbar = env.addScrollBar(True, recti(150, 45, 350, 60), 0, GUI_ID_TRANSPARENCY_SCROLL_BAR)
	scrollbar.setMax(255)
	scrollbar.setPos(env.getSkin().getColor(EGDC_WINDOW).getAlpha())

	env.addStaticText("Logging ListBox:", recti(50,110,250,130), True)
	listbox = env.addListBox(recti(50, 140, 250, 210))
	env.addEditBox("Editable Text", recti(350, 80, 550, 100))

	context = SAppContext()
	context.device = device
	context.counter = 0
	context.listbox = listbox

	receiver = MyEventReceiver()
	receiver.Context = context
	device.setEventReceiver(receiver)

	env.addImage(driver.getTexture("media/irrlichtlogo2.png"), position2di(10,10))

	while device.run() and driver:
		if device.isWindowActive():
			driver.beginScene(True, True, SColor(0,200,200,200))
			env.drawAll()
			driver.endScene()

	device.drop()

	return 0


if __name__ == "__main__":
	main()

from math import fabs
from pyirrlicht import *

#~ driverType = EDT_NULL
#~ driverType = EDT_SOFTWARE
#~ driverType = EDT_BURNINGSVIDEO
#~ driverType = EDT_DIRECT3D8
#~ driverType = EDT_DIRECT3D9
driverType = EDT_OPENGL

class SMouseState:
	LeftButtonDown = False
	Position = position2di()

class MyEventReceiver(IEventReceiver):
	MouseState = SMouseState()
	JoystickState = None

	def OnEvent(self, event):
		event_type = self.GetEventType(event)
		if event_type == EET_MOUSE_INPUT_EVENT:
			mouse_event = self.GetMouseInput(event)
			mouse_event_type = self.MouseInput_EventType(mouse_event)
			if mouse_event_type == EMIE_LMOUSE_PRESSED_DOWN:
				self.MouseState.LeftButtonDown = True
			elif mouse_event_type == EMIE_LMOUSE_LEFT_UP:
				self.MouseState.LeftButtonDown = False
			elif mouse_event_type == EMIE_MOUSE_MOVED:
				self.MouseState.Position.X = self.MouseInput_X(mouse_event)
				self.MouseState.Position.Y = self.MouseInput_Y(mouse_event)
		elif event_type == EET_JOYSTICK_INPUT_EVENT:
			joystick_event = self.GetJoystickEvent(event)
			if self.JoystickEvent_Joystick(joystick_event) == 0:
				self.JoystickState = SJoystickEvent(joystick_event)
		return False

	def GetJoystickState(self):
		return self.JoystickState

	def GetMouseState(self):
		return self.MouseState

if __name__ == "__main__":
	receiver = MyEventReceiver()
	device = createDevice(driverType, dimension2du(640, 480), 16, False, False, False, receiver)
	if device:
		joystickInfo = arraySJoystickInfo()
		if device.activateJoysticks(joystickInfo):
			print ("Joystick support is enabled and %d joystick(s) are present." % joystickInfo.size())

			for joystick in range(joystickInfo.size()):
				print ("Joystick ", joystick)
				print ("\tName: '", joystickInfo[joystick].Name, "'")
				print ("\tAxes: ", joystickInfo[joystick].Axes)
				print ("\tButtons: ", joystickInfo[joystick].Buttons)

				print ("\tHat is: ")

				pov_hat = joystickInfo[joystick].PovHat
				if pov_hat == POV_HAT_PRESENT:
					print ("present")
				elif pov_hat == POV_HAT_ABSENT:
					print ("absent")
				elif pov_hat == POV_HAT_UNKNOWN:
					print ("unknown")
		else:
			print ("Joystick support is not enabled.")

		tmp = "Irrlicht Joystick Example (%d joysticks)" % joystickInfo.size()
		device.setWindowCaption(tmp)

		driver = device.getVideoDriver()
		smgr = device.getSceneManager()

		node = smgr.addMeshSceneNode(smgr.addArrowMesh('Arrow', SColor(255, 255, 0, 0), SColor(255, 0, 255, 0), 16, 16, 2.0, 1.3, 0.1, 0.6))
		node.setMaterialFlag(EMF_LIGHTING, False)

		camera = smgr.addCameraSceneNode()
		camera.setPosition(vector3df(0, 0, -10))

		then = device.getTimer().getTime()
		MOVEMENT_SPEED = 5.0

		#~ mousePosition = vector3df()
		while device.run():
			if device.isWindowActive():
				now = device.getTimer().getTime()
				frameDeltaTime = float((now - then) / 1000.0)
				then = now

				movedWithJoystick = False
				nodePosition = node.getPosition()

				if joystickInfo.size() > 0:
					moveHorizontal = 0.0
					moveVertical = 0.0

					joystickData = receiver.GetJoystickState()

					DEAD_ZONE = 0.05

					moveHorizontal = float(joystickData.Axis[AXIS_X] / 32767.0)
					if fabs(moveHorizontal) < DEAD_ZONE:
						moveHorizontal = 0.0

					moveVertical = float(joystickData.Axis[AXIS_Y] / -32767.0)
					if fabs(moveVertical) < DEAD_ZONE:
						moveVertical = 0.0

					povDegrees = joystickData.POV / 100
					if povDegrees < 360:
						if povDegrees > 0 and povDegrees < 180:
							moveHorizontal = 1.0
						elif povDegrees > 180:
							moveHorizontal -= 1.0

						if povDegrees > 90 and povDegrees < 270:
							moveVertical -= 1.0
						elif povDegrees > 270 or povDegrees < 90:
							moveVertical += 1.0

					if moveHorizontal != 0.0 or moveVertical != 0.0:
						nodePosition.X += MOVEMENT_SPEED * frameDeltaTime * moveHorizontal
						nodePosition.Y += MOVEMENT_SPEED * frameDeltaTime * moveVertical
						movedWithJoystick = True

				if not movedWithJoystick:
					ray = smgr.getSceneCollisionManager().getRayFromScreenCoordinates(receiver.GetMouseState().Position, camera)
					plane = plane3df(nodePosition, vector3df(0, 0, -1))
					mousePosition = vector3df()
					if plane.getIntersectionWithLine(ray.start, ray.getVector(), mousePosition):
						toMousePosition = mousePosition - nodePosition
						availableMovement = MOVEMENT_SPEED * frameDeltaTime
						if toMousePosition.getLength() <= availableMovement:
							nodePosition = mousePosition
						else:
							nodePosition += toMousePosition.normalize() * availableMovement

				node.setPosition(nodePosition)
				node.setMaterialFlag(EMF_LIGHTING, receiver.GetMouseState().LeftButtonDown)
				driver.beginScene(True, True, SColor(255,113,113,133))
				smgr.drawAll()
				driver.endScene()
				device.sleep(50)
			else:
				device._yield()

		device.drop()

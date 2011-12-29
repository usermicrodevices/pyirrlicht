Include "irrlicht.bmx"

Graphics3D 640,480,0,2
SetFont LoadFont("Tahoma",30)

window_size = New dimension2du(320, 240)

device = New IrrlichtDevice(EDT_DIRECT3D9, window_size, 16, False, False, False, 0)

If device

	Print "Irrlicht version: " + device.getVersion()

	device.closeDevice()

Else

	Print "ERROR : Irrlicht device not created."

EndIf

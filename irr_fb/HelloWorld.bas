#include "irrlicht.bi"
#include "resource.bi"


'~ Dim device As IrrlichtDevice = createDevice(EDT_OPENGL, Type<dimension2du>(320, 240))
'~ Dim device As IrrlichtDevice = createDevice(EDT_SOFTWARE, Type<dimension2du>(640, 480))
Dim device As IrrlichtDevice = createDevice(EDT_DIRECT3D9, Type<dimension2du>(640, 480))

device.setWindowCaption("Hello World! - Irrlicht Engine Demo")

Dim driver As IVideoDriver = device.getVideoDriver()

driver.SetIcon(IDI_ICON1)

Dim smgr As ISceneManager = device.getSceneManager()

Dim guienv As IGUIEnvironment = device.getGUIEnvironment()

guienv.addStaticText("Hello World! This is the Irrlicht Software renderer!", Type<recti>(10,10,260,22), true)

Dim mesh As IAnimatedMesh = smgr.getMesh("media/sydney.md2")

'print"+++ IAnimatedMesh", mesh

If mesh Then
	Dim node As IAnimatedMeshSceneNode = smgr.addAnimatedMeshSceneNode(@mesh)
	'Dim node As IAnimatedMeshSceneNode = smgr.addAnimatedMeshSceneNode(@mesh, 0, -1, Type<vector3df>(0.0, 0.0, 0.0), Type<vector3df>(0.0, 0.0, 0.0), Type<vector3df>(1.0, 1.0, 1.0), false)
	'print"+++ IAnimatedMeshSceneNode", node
	If node Then
		node.setMaterialFlag(EMF_LIGHTING, false)
		node.setMD2Animation(EMAT_STAND)
		node.setMaterialTexture(0, driver.getTexture("media/sydney.bmp") )
	End If
End If

smgr.addCameraSceneNode(0, Type<vector3df>(0,30,-40), Type<vector3df>(0,5,0))

Dim sc As SColor = SColor(255, 100, 100, 140)

While device.run()
	If device.isWindowActive() Then
		If driver.beginScene(true, true, @sc) Then
			smgr.drawAll()
			guienv.drawAll()
			driver.endScene()
		End If
		device.setWindowCaption("Hello World! - Irrlicht Engine Demo   fps = " & Str(driver.getFPS()))
		device.sleep(50)
	Else
		device.yield()
	End If
Wend

device.closeDevice()

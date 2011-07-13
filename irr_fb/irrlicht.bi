' object oriented implementation Irrlicht 3D SDK for FreeBASIC
' Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
' http://vosolok2008.narod.ru
' BSD license


#include once "const.bi"
#include once "irrlicht_c.bi"



Type dimension2du
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal other As Any Ptr)
	Declare Constructor()
	Declare Constructor(ByVal x As UInteger, ByVal y As UInteger)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @() As Any Ptr
	Declare Property Width() As UInteger
	Declare Property Width(ByVal value As UInteger)
	Declare Property Height() As UInteger
	Declare Property Height(ByVal value As UInteger)
End Type
Constructor dimension2du(ByVal other As Any Ptr)
	this.c_pointer = other
	this.del_ptr = False
End Constructor
Constructor dimension2du()
	this.c_pointer = dimension2du_ctor1()
End Constructor
Constructor dimension2du(ByVal x As UInteger, ByVal y As UInteger)
	this.c_pointer = dimension2du_ctor2(x, y)
End Constructor
Destructor dimension2du()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator dimension2du.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator dimension2du.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Property dimension2du.Width() As UInteger
	Width = dimension2du_get_Width(this.c_pointer)
End Property
Property dimension2du.Height() As UInteger
	Height = dimension2du_get_Height(this.c_pointer)
End Property
Property dimension2du.Width(ByVal value As UInteger)
	dimension2du_set_Width(this.c_pointer, value)
End Property
Property dimension2du.Height(ByVal value As UInteger)
	dimension2du_set_Height(this.c_pointer, value)
End Property



Type vector3df
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal d As UByte = false, ByVal other As Any Ptr = 0)
	Declare Constructor()
	Declare Constructor(ByVal x As Single, ByVal y As Single, ByVal z As Single)
	Declare Constructor(ByVal n As Single)
	Declare Constructor(ByVal other As Any Ptr)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @() As Any Ptr
	Declare Sub set_X(ByVal value As Single)
	Declare Function get_X() As Single
	Declare Sub set_Y(ByVal value As Single)
	Declare Function get_Y() As Single
	Declare Sub set_Z(ByVal value As Single)
	Declare Function get_Z() As Single
End Type
Constructor vector3df(ByVal d As UByte = false, ByVal other As Any Ptr = 0)
	this.c_pointer = other
	this.del_ptr = d
End Constructor
Constructor vector3df()
	this.c_pointer = vector3df_ctor1()
End Constructor
Constructor vector3df(ByVal x As Single, ByVal y As Single, ByVal z As Single)
	this.c_pointer = vector3df_ctor2(x, y, z)
End Constructor
Constructor vector3df(ByVal n As Single)
	this.c_pointer = vector3df_ctor3(n)
End Constructor
Constructor vector3df(ByVal other As Any Ptr)
	this.c_pointer = vector3df_ctor4(other)
End Constructor
Destructor vector3df()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator vector3df.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator vector3df.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Sub vector3df.set_X(ByVal value As Single)
	vector3df_set_X(this.c_pointer, value)
End Sub
Function vector3df.get_X() As Single
	Return vector3df_get_X(this.c_pointer)
End Function
Sub vector3df.set_Y(ByVal value As Single)
	vector3df_set_Y(this.c_pointer, value)
End Sub
Function vector3df.get_Y() As Single
	Return vector3df_get_Y(this.c_pointer)
End Function
Sub vector3df.set_Z(ByVal value As Single)
	vector3df_set_Z(this.c_pointer, value)
End Sub
Function vector3df.get_Z() As Single
	Return vector3df_get_Z(this.c_pointer)
End Function



Type IEventReceiver
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor()
	Declare Constructor(ByVal on_event_method As EVENT_METHOD)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @() As Any Ptr
	Declare Static Function OnEventMethod(ByVal _event_ As EVENT_METHOD) As UByte
End Type
Constructor IEventReceiver()
	this.c_pointer = 0
	this.del_ptr = false
End Constructor
Constructor IEventReceiver(ByVal on_event_method As EVENT_METHOD)
	this.c_pointer = IEventReceiver_ctor2(on_event_method)
	this.del_ptr = false
End Constructor
Destructor IEventReceiver()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator IEventReceiver.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator IEventReceiver.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Function IEventReceiver.OnEventMethod(ByVal _event_ As EVENT_METHOD) As UByte
	print "OnEventMethod ", _event_
	Return False
End Function


Type SExposedVideoData
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor()
	Declare Constructor(ByVal _window_ As Any Ptr)
	Declare Constructor(ByVal other As Any Ptr, ByVal del_ptr As Ubyte)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @() As Any Ptr
End Type
Constructor SExposedVideoData()
	this.c_pointer = SExposedVideoData_ctor1()
End Constructor
Constructor SExposedVideoData(ByVal _window_ As Any Ptr)
	this.c_pointer = SExposedVideoData_ctor2(_window_)
End Constructor
Constructor SExposedVideoData(ByVal other As Any Ptr, ByVal del_ptr As Ubyte)
	this.c_pointer = other
	this.del_ptr = del_ptr
End Constructor
Destructor SExposedVideoData()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator SExposedVideoData.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator SExposedVideoData.@() As Any Ptr
	Operator = this.c_pointer
End Operator



Type SColor
	As Any Ptr c_pointer
	Declare Constructor()
	Declare Constructor(ByVal a As UInteger, ByVal r As UInteger, ByVal g As UInteger, ByVal b As UInteger)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @ () As Any Ptr
End Type
Constructor SColor()
	this.c_pointer = SColor_ctor1()
End Constructor
Constructor SColor(ByVal a As UInteger, ByVal r As UInteger, ByVal g As UInteger, ByVal b As UInteger)
	this.c_pointer = SColor_ctor2(a, r, g, b)
End Constructor
Destructor SColor()
	delete_pointer(this.c_pointer)
End Destructor
Operator SColor.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator SColor.@() As Any Ptr
	Operator = this.c_pointer
End Operator



Type recti
	As Any Ptr c_pointer
	Declare Constructor()
	Declare Constructor(ByVal x As Integer, ByVal y As Integer, ByVal x2 As Integer, ByVal y2 As Integer)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
End Type
Constructor recti()
	this.c_pointer = recti_ctor1()
End Constructor
Constructor recti(ByVal x As Integer, ByVal y As Integer, ByVal x2 As Integer, ByVal y2 As Integer)
	this.c_pointer = recti_ctor2(x, y, x2, y2)
End Constructor
Destructor recti()
	delete_pointer(this.c_pointer)
End Destructor
Operator recti.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator


Type IAnimatedMesh
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal other As Any Ptr)
	Declare Destructor()
	Declare Operator Cast() As UByte
	Declare Operator Cast() As Any Ptr
	Declare Operator Cast() As String
	Declare Operator @() As Any Ptr
	Declare Function getFrameCount() As UInteger
	Declare Function getMesh(ByVal frame As Integer, ByVal detailLevel As Integer, ByVal startFrameLoop As Integer, ByVal endFrameLoop As Integer) As Any Ptr
	Declare Function getMeshType() As E_ANIMATED_MESH_TYPE
End Type
Constructor IAnimatedMesh(ByVal other As Any Ptr)
	this.c_pointer = other
	this.del_ptr = False
End Constructor
Destructor IAnimatedMesh()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator IAnimatedMesh.Cast() As UByte
	Operator = this.c_pointer <> 0
End Operator
Operator IAnimatedMesh.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator IAnimatedMesh.Cast() As String
	Operator = Str(this.c_pointer)
End Operator
Operator IAnimatedMesh.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Function IAnimatedMesh.getFrameCount() As UInteger
	Return IAnimatedMesh_getFrameCount(this.c_pointer)
End Function
Function IAnimatedMesh.getMesh(ByVal frame As Integer, ByVal detailLevel As Integer, ByVal startFrameLoop As Integer, ByVal endFrameLoop As Integer) As Any Ptr
	Return IAnimatedMesh_getMesh(this.c_pointer, frame, detailLevel, startFrameLoop, endFrameLoop)
End Function
Function IAnimatedMesh.getMeshType() As E_ANIMATED_MESH_TYPE
	Return IAnimatedMesh_getMeshType(this.c_pointer)
End Function



Type ISceneNode
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal _pointer_ As Any Ptr)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Operator @() As Any Ptr
	Declare Sub setMaterialFlag(ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	Declare Sub setMaterialTexture(ByVal textureLayer As UInteger, ByVal texture As Any Ptr)
End Type
Constructor ISceneNode(ByVal _pointer_ As Any Ptr)
	this.c_pointer = _pointer_
	this.del_ptr = False
End Constructor
Destructor ISceneNode()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator ISceneNode.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator ISceneNode.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Sub ISceneNode.setMaterialFlag(ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	ISceneNode_setMaterialFlag(this.c_pointer, flag, newvalue)
End Sub
Sub ISceneNode.setMaterialTexture(ByVal textureLayer As UInteger, ByVal texture As Any Ptr)
	ISceneNode_setMaterialTexture(this.c_pointer, textureLayer, texture)
End Sub

Type IAnimatedMeshSceneNode
	As Ubyte del_ptr = True
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal d As UByte, ByVal other As Any Ptr)
	Declare Constructor(ByVal parent As Any Ptr = 0, ByVal mgr As Any Ptr = 0, ByVal id As Integer = -1, ByVal position As Any Ptr = 0, ByVal rotation As Any Ptr = 0, ByVal scale As Any Ptr = 0)
	Declare Destructor()
	Declare Operator Cast() As UByte
	Declare Operator Cast() As Any Ptr
	Declare Operator Cast() As String
	Declare Operator @() As Any Ptr
	Declare Sub setMaterialFlag(ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	Declare Sub setMaterialTexture(ByVal textureLayer As UInteger, ByVal texture As Any Ptr)
	Declare Function setMD2Animation(ByVal anim As EMD2_ANIMATION_TYPE) As UByte
	Declare Function setMD2Animation(ByVal animationName As ZString Ptr) As UByte
End Type
Constructor IAnimatedMeshSceneNode(ByVal d As UByte, ByVal other As Any Ptr)
	this.c_pointer = other
	this.del_ptr = d
End Constructor
Constructor IAnimatedMeshSceneNode(ByVal parent As Any Ptr = 0, ByVal mgr As Any Ptr = 0, ByVal id As Integer = -1, ByVal position As Any Ptr = 0, ByVal rotation As Any Ptr = 0, ByVal scale As Any Ptr = 0)
	this.c_pointer = IAnimatedMeshSceneNode_ctor(parent, mgr, id, position, rotation, scale)
	this.del_ptr = False
End Constructor
Destructor IAnimatedMeshSceneNode()
	If this.del_ptr Then
		delete_pointer(this.c_pointer)
	End If
End Destructor
Operator IAnimatedMeshSceneNode.Cast() As UByte
	Operator = this.c_pointer <> 0
End Operator
Operator IAnimatedMeshSceneNode.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Operator IAnimatedMeshSceneNode.Cast() As String
	Operator = Str(this.c_pointer)
End Operator
Operator IAnimatedMeshSceneNode.@() As Any Ptr
	Operator = this.c_pointer
End Operator
Sub IAnimatedMeshSceneNode.setMaterialFlag(ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	ISceneNode_setMaterialFlag(this.c_pointer, flag, newvalue)
End Sub
Sub IAnimatedMeshSceneNode.setMaterialTexture(ByVal textureLayer As UInteger, ByVal texture As Any Ptr)
	ISceneNode_setMaterialTexture(this.c_pointer, textureLayer, texture)
End Sub
Function IAnimatedMeshSceneNode.setMD2Animation(ByVal anim As EMD2_ANIMATION_TYPE) As UByte
	Return IAnimatedMeshSceneNode_setMD2Animation1(this.c_pointer, anim)
End Function
Function IAnimatedMeshSceneNode.setMD2Animation(ByVal animationName As ZString Ptr) As UByte
	Return IAnimatedMeshSceneNode_setMD2Animation2(this.c_pointer, animationName)
End Function



Type IVideoDriver
	Declare Constructor(ByVal _pointer_ As Any Ptr)
	Declare Destructor()
	Declare Function beginScene Overload(ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As SColor Ptr) As UByte
	Declare Function beginScene Overload(ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As SColor Ptr, ByVal videoData As SExposedVideoData Ptr, ByVal sourceRect As recti Ptr = 0) As UByte
	Declare Function endScene() As UByte
	Declare Function getTexture(ByVal filename As ZString Ptr) As Any Ptr
	Declare Function getExposedVideoData() As SExposedVideoData
	Declare Sub SetIcon(ByVal icon_id As Integer = 32512, ByVal big_icon As UByte = False)
	Declare Function getFPS() As Integer
	Private:
		As Any Ptr c_pointer
End Type
Constructor IVideoDriver(ByVal _pointer_ As Any Ptr)
	this.c_pointer = _pointer_
End Constructor
Destructor IVideoDriver()
	'~ delete_pointer(this.c_pointer)
End Destructor
Function IVideoDriver.beginScene(ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As SColor Ptr) As UByte
	Return IVideoDriver_beginSceneDefault(this.c_pointer, backBuffer, zBuffer, _color_)
End Function
Function IVideoDriver.beginScene(ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As SColor Ptr, ByVal videoData As SExposedVideoData Ptr, ByVal sourceRect As recti Ptr = 0) As UByte
	Return IVideoDriver_beginScene(this.c_pointer, backBuffer, zBuffer, _color_, videoData, sourceRect)
End Function
Function IVideoDriver.endScene() As UByte
	Return IVideoDriver_endScene(this.c_pointer)
End Function
Function IVideoDriver.getTexture(ByVal filename As ZString Ptr) As Any Ptr
	Return IVideoDriver_getTexture1(this.c_pointer, filename)
End Function
Function IVideoDriver.getExposedVideoData() As SExposedVideoData
	Return SExposedVideoData(IVideoDriver_getExposedVideoData(this.c_pointer), False)
End Function
Sub IVideoDriver.SetIcon(ByVal icon_id As Integer = 32512, ByVal big_icon As UByte = False)
	IVideoDriver_SetIcon(this.c_pointer, icon_id, big_icon)
End Sub
Function IVideoDriver.getFPS() As Integer
	Return IVideoDriver_getFPS(this.c_pointer)
End Function



Type IFileSystem
	Declare Constructor(ByVal _pointer_ As Any Ptr)
	Declare Destructor()
	Private:
		As Any Ptr c_pointer = 0
End Type
Constructor IFileSystem(ByVal _pointer_ As Any Ptr)
	this.c_pointer = _pointer_
End Constructor
Destructor IFileSystem()
	'~ delete_pointer(this.c_pointer)
End Destructor



Type IGUIEnvironment
	As Any Ptr c_pointer = 0
	Declare Constructor(ByVal _pointer_ As Any Ptr)
	Declare Destructor()
	Declare Sub drawAll()
	Declare Function addStaticText(ByVal text_value As WString Ptr = 0, ByVal _rectangle_ As Any Ptr = 0, ByVal _border_ As UByte = 0, ByVal _wordWrap_ As UByte = 0, ByVal _parent_ As Any Ptr = 0, ByVal id_value As Integer = -1, ByVal _fillBackground_ As UByte = 0) As Any Ptr
End Type
Constructor IGUIEnvironment(ByVal _pointer_ As Any Ptr)
	this.c_pointer = _pointer_
End Constructor
Destructor IGUIEnvironment()
	'~ delete_pointer(this.c_pointer)
End Destructor
Sub IGUIEnvironment.drawAll()
	IGUIEnvironment_drawAll(this.c_pointer)
End Sub
Function IGUIEnvironment.addStaticText(ByVal text_value As WString Ptr = 0, ByVal _rectangle_ As Any Ptr = 0, ByVal _border_ As UByte = 0, ByVal _wordWrap_ As UByte = 0, ByVal _parent_ As Any Ptr = 0, ByVal id_value As Integer = -1, ByVal _fillBackground_ As UByte = 0) As Any Ptr
	Return IGUIEnvironment_addStaticText(this.c_pointer, text_value, _rectangle_, _border_, _wordWrap_, _parent_, id_value, _fillBackground_)
End Function




Type ISceneManager
	Declare Constructor(ByVal _pointer_ As Any Ptr)
	Declare Destructor()
	Declare Sub drawAll()
	Declare Function getMesh(ByVal filename As ZString Ptr) As IAnimatedMesh
	Declare Function addAnimatedMeshSceneNode(ByVal mesh As Any Ptr) As IAnimatedMeshSceneNode
	Declare Function addAnimatedMeshSceneNode(ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer = -1, ByVal position As Any Ptr = 0, ByVal rotation As Any Ptr = 0, ByVal scale As Any Ptr = 0, ByVal alsoAddIfMeshPointerZero As UByte = False) As IAnimatedMeshSceneNode
	Declare Function addCameraSceneNode(ByVal parent As Any Ptr = 0, ByVal position As Any Ptr = 0, ByVal lookat As Any Ptr = 0, ByVal id As Integer = -1) As Any Ptr
	Private:
		As Any Ptr c_pointer = 0
End Type
Constructor ISceneManager(ByVal _pointer_ As Any Ptr)
	this.c_pointer = _pointer_
End Constructor
Destructor ISceneManager()
	'~ delete_pointer(this.c_pointer)
End Destructor
Sub ISceneManager.drawAll()
	ISceneManager_drawAll(this.c_pointer)
End Sub
Function ISceneManager.getMesh(ByVal filename As ZString Ptr) As IAnimatedMesh
	Return IAnimatedMesh(ISceneManager_getMesh(this.c_pointer, filename))
End Function
Function ISceneManager.addAnimatedMeshSceneNode(ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer = -1, ByVal position As Any Ptr = 0, ByVal rotation As Any Ptr = 0, ByVal scale As Any Ptr = 0, ByVal alsoAddIfMeshPointerZero As UByte = False) As IAnimatedMeshSceneNode
	Return IAnimatedMeshSceneNode(False, ISceneManager_addAnimatedMeshSceneNode(this.c_pointer, mesh, parent, id, position, rotation, scale, alsoAddIfMeshPointerZero))
End Function
Function ISceneManager.addAnimatedMeshSceneNode(ByVal mesh As Any Ptr) As IAnimatedMeshSceneNode
	'~ Return IAnimatedMeshSceneNode(False, ISceneManager_addAnimatedMeshSceneNode(this.c_pointer, mesh, 0, -1, Type<vector3df>(0.0, 0.0, 0.0), Type<vector3df>(0.0, 0.0, 0.0), Type<vector3df>(1.0, 1.0, 1.0), False))
	Return IAnimatedMeshSceneNode(False, ISceneManager_addAnimatedMeshSceneNode2(this.c_pointer, mesh))
End Function
Function ISceneManager.addCameraSceneNode(ByVal parent As Any Ptr = 0, ByVal position As Any Ptr = 0, ByVal lookat As Any Ptr = 0, ByVal id As Integer = -1) As Any Ptr
	Return ISceneManager_addCameraSceneNode(this.c_pointer, parent, position, lookat, id)
End Function




Type IrrlichtDevice
	Declare Constructor(ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, ByVal windowSize As dimension2du Ptr = 0, ByVal bits As UInteger = 16, ByVal fullscreen As UByte = False, ByVal stencilbuffer As UByte = False, ByVal vsync As UByte = False, ByVal receiver As IEventReceiver Ptr = 0)
	Declare Destructor()
	Declare Operator Cast() As Any Ptr
	Declare Function run() As UByte
	Declare Sub yield()
	Declare Sub sleep(ByVal timeMs As UInteger, ByVal pauseTimer As UByte = False)
	Declare Function getVideoDriver() As IVideoDriver
	Declare Function getFileSystem() As IFileSystem
	Declare Function getGUIEnvironment() As IGUIEnvironment
	Declare Function getSceneManager() As ISceneManager
	Declare Sub setWindowCaption(ByVal text As WString Ptr)
	Declare Function isWindowActive() As Ubyte
	Declare Sub closeDevice()
	Declare Function getVersion() As String
	Declare Sub setEventReceiver(ByVal receiver As Any Ptr)
	Private:
		As Any Ptr c_pointer
End Type
Constructor IrrlichtDevice(ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, ByVal windowSize As dimension2du Ptr = 0, ByVal bits As UInteger = 16, ByVal fullscreen As UByte = False, ByVal stencilbuffer As UByte = False, ByVal vsync As UByte = False, ByVal receiver As IEventReceiver Ptr = 0)
	this.c_pointer = IrrlichtDevice_createDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver)
End Constructor
Destructor IrrlichtDevice()
	'~ delete_pointer(this.c_pointer)
End Destructor
Operator IrrlichtDevice.Cast() As Any Ptr
	Operator = this.c_pointer
End Operator
Function IrrlichtDevice.run() As UByte
	Return IrrlichtDevice_run(this.c_pointer)
End Function
Sub IrrlichtDevice.yield()
	IrrlichtDevice_yield(this.c_pointer)
End Sub
Sub IrrlichtDevice.sleep(ByVal timeMs As UInteger, ByVal pauseTimer As UByte = False)
	IrrlichtDevice_sleep(this.c_pointer, timeMs, pauseTimer)
End Sub
Function IrrlichtDevice.getVideoDriver() As IVideoDriver
	Return IVideoDriver(IrrlichtDevice_getVideoDriver(this.c_pointer))
End Function
Function IrrlichtDevice.getFileSystem() As IFileSystem
	Return IFileSystem(IrrlichtDevice_getFileSystem(this.c_pointer))
End Function
Function IrrlichtDevice.getGUIEnvironment() As IGUIEnvironment
	Return IGUIEnvironment(IrrlichtDevice_getGUIEnvironment(this.c_pointer))
End Function
Function IrrlichtDevice.getSceneManager() As ISceneManager
	Return ISceneManager(IrrlichtDevice_getSceneManager(this.c_pointer))
End Function
Sub IrrlichtDevice.setWindowCaption(ByVal text As WString Ptr)
	IrrlichtDevice_setWindowCaption(this.c_pointer, text)
End Sub
Function IrrlichtDevice.isWindowActive() As Ubyte
	Return IrrlichtDevice_isWindowActive(this.c_pointer)
End Function
Sub IrrlichtDevice.closeDevice()
	IrrlichtDevice_closeDevice(this.c_pointer)
End Sub
Function IrrlichtDevice.getVersion() As String
	Return *IrrlichtDevice_getVersion(this.c_pointer)
End Function
Sub IrrlichtDevice.setEventReceiver(ByVal receiver As Any Ptr)
	IrrlichtDevice_setEventReceiver(this.c_pointer, receiver)
End Sub



Declare Function createDevice( _
	ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, _
	ByVal windowSize As Any Ptr = 0, _
	ByVal bits As UInteger = 16, _
	ByVal fullscreen As UByte = False, _
	ByVal stencilbuffer As UByte = False, _
	ByVal vsync As UByte = False, _
	ByVal receiver As IEventReceiver Ptr = 0) As IrrlichtDevice

Function createDevice(ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, ByVal windowSize As Any Ptr = 0, ByVal bits As UInteger = 16, ByVal fullscreen As UByte = False, ByVal stencilbuffer As UByte = False, ByVal vsync As UByte = False, ByVal receiver As IEventReceiver Ptr = 0) As IrrlichtDevice
    Return IrrlichtDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver)
End Function

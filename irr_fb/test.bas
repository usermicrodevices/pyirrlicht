#include "irrlicht.bi"
#include "resource.bi"


'~ Dim event_method As Function(ByRef _event_ As Any Ptr) As UByte

Function event_method cdecl (ByVal _event_ As Any Ptr) As UByte
	print "+++ event_method", SEvent_GetEventType(_event_), SLogEvent_GetText(SEvent_GetSLogEvent(_event_))
	Return False
End Function
'~ Function event_method_naked Naked (ByVal _event_ As Any Ptr) As UByte
	'~ 'Asm
		'~ 'mov eax, dword ptr [_event_]
		'~ 'call SEvent_GetEventType
	'~ 'End Asm
	'~ print "+++ event_method"
	'~ Asm
		'~ 'mov byte ptr [eax], 0
		'~ mov eax, False
		'~ ret
		'~ 'mov [Function], eax
	'~ End Asm
'~ End Function

'Dim device As IrrlichtDevice = createDevice(EDT_OPENGL, Type<dimension2du>(320, 240))

Dim wsize As dimension2du = dimension2du(320, 240)

'Var wsize = New dimension2du(320, 240)

'~ Dim em As Function (As Any Ptr) As UByte = @event_method

Dim receiver As IEventReceiver = IEventReceiver(@event_method)
'~ Dim receiver As IEventReceiver = IEventReceiver(@event_method_naked)
'~ Dim receiver As IEventReceiver = IEventReceiver(ProcPtr(IEventReceiver.OnEventMethod))

'~ Dim device As IrrlichtDevice = createDevice(EDT_OPENGL, @wsize, 16, False, False, False, @receiver)
Dim device As IrrlichtDevice = createDevice(EDT_OPENGL, @wsize)

print "=== wsize = "; wsize.Width; "x"; wsize.Height

'print "wsize = "; wsize->Width; "x"; wsize->Height

'Delete wsize

print "=== getVersion = "; device.getVersion()

device.setWindowCaption("This is a test")

Dim driver As IVideoDriver = device.getVideoDriver()

driver.SetIcon(IDI_ICON1)

Dim sm As ISceneManager = device.getSceneManager()

Dim sc As SColor = SColor(255, 100, 100, 140)

device.setEventReceiver(@receiver)

While device.run()
	If device.isWindowActive() Then
		If driver.beginScene(true, true, @sc) Then
			sm.drawAll()
			driver.endScene()
		End If
		device.sleep(50)
	Else
		device.yield()
	End If
Wend

device.closeDevice()

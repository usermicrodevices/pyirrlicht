format PE GUI 4.0
entry start

include '%fasminc%/encoding/win1251.inc'
include '%fasminc%/win32w.inc'
include 'irr_inc/irrlicht.inc'

section '.text' code readable executable

start:
	cinvoke SExposedVideoData_ctor1
	mov [video_data],eax
	cinvoke dimension2du_ctor2,320,240
	mov [windowSize],eax
	cinvoke SColor_ctor2,255,100,101,140
	mov [color],eax
	cinvoke IrrlichtDevice_createDevice,EDT_SOFTWARE,[windowSize],16,FALSE,FALSE,FALSE,NULL
	mov [device],eax
	cinvoke IrrlichtDevice_setWindowCaption,[device],window_caption
	cinvoke IrrlichtDevice_setResizable,[device],TRUE
	cinvoke IrrlichtDevice_getVideoDriver,[device]
	mov [driver],eax
	cinvoke IrrlichtDevice_getSceneManager,[device]
	mov [scene_manager],eax
	cinvoke IrrlichtDevice_run,[device]
	mov [is_device_run],eax
	while is_device_run = TRUE;fix me if you know how
		cinvoke IrrlichtDevice_isWindowActive,[device]
		mov [is_window_active],eax
		if is_window_active = TRUE
			cinvoke IVideoDriver_beginScene,[driver],TRUE,TRUE,[color],[video_data],NULL
			cinvoke ISceneManager_drawAll,[scene_manager]
			cinvoke IVideoDriver_endScene,[driver]
			cinvoke IrrlichtDevice_sleep,[device],100
		else
			cinvoke IrrlichtDevice_yield,[device]
		end if
		cinvoke IrrlichtDevice_run,[device]
		mov [is_device_run],eax
		; if is_device_run = FALSE
			; break
		; end if
	end while
	cinvoke IrrlichtDevice_closeDevice,[device]
	invoke ExitProcess,0

section '.data' data readable writeable
	window_caption du 'Irrlicht Engine Window (А это русский текст ЁЖИКЪ ой)',0
	video_data dd ?
	windowSize dd ?
	color dd ?
	device dd ?
	driver dd ?
	scene_manager dd ?
	is_device_run dd ?
	is_window_active dd ?

section '.idata' import data readable writeable

	library kernel,'kernel32.dll',irrlicht_c,'irrlicht_c.dll'
	import kernel,ExitProcess,'ExitProcess'

format PE GUI 4.0
entry start

include '%fasminc%/encoding/win1251.inc'
include '%fasminc%/win32w.inc'
include 'irr_inc/irrlicht.inc'

section '.text' code readable executable

start:
	;;=======================
	; mov	[evd.D3D8.D3D8],NULL
	; mov	[evd.D3D8.D3DDev8],NULL
	; mov	[evd.D3D8.HWnd],NULL
	; mov	[evd.D3D9.D3D9],NULL
	; mov	[evd.D3D9.D3DDev9],NULL
	; mov	[evd.D3D9.HWnd],NULL
	; mov	[evd.OpenGLWin32.HDc],NULL
	; mov	[evd.OpenGLWin32.HRc],NULL
	; mov	[evd.OpenGLWin32.HWnd],NULL
	; mov	[evd.OpenGLLinux.X11Display],NULL
	; mov	[evd.OpenGLLinux.X11Context],NULL
	; mov	[evd.OpenGLLinux.X11Window],NULL
	;; =======================
	cinvoke SExposedVideoData_ctor1
	mov [video_data],eax
	;;=======================
	cinvoke dimension2du_ctor2,320,240
	mov [windowSize],eax
	; cinvoke scolor_SColor
	cinvoke SColor_ctor2,255,100,101,140
	; cinvoke SColor_ctor3,100
	mov [color],eax
	; cinvoke createDevice,EDT_SOFTWARE,[windowSize],16,FALSE,FALSE,FALSE,NULL
	cinvoke IrrlichtDevice_createDevice,EDT_SOFTWARE,[windowSize],16,FALSE,FALSE,FALSE,NULL
	mov [device],eax
	cinvoke IrrlichtDevice_setWindowCaption,[device],window_caption
	cinvoke IrrlichtDevice_setResizable,[device],TRUE
	cinvoke IrrlichtDevice_getVideoDriver,[device]
	mov [driver],eax
	cinvoke IrrlichtDevice_getSceneManager,[device]
	mov [scene_manager],eax
	cinvoke IrrlichtDevice_run,[device]
	cmp eax,FALSE
	jb IrrlichtDevice_end_loop
	jne IrrlichtDevice_run_loop
	IrrlichtDevice_run_loop:
		cinvoke IrrlichtDevice_isWindowActive,[device]
		cmp eax,TRUE
		jne draw
		jb yeld
		draw:
			cinvoke IVideoDriver_beginScene,[driver],TRUE,TRUE,[color],[video_data],NULL
			; cinvoke IVideoDriver_beginScene,[driver],TRUE,TRUE,[color],[evd],NULL
			cinvoke ISceneManager_drawAll,[scene_manager]
			cinvoke IVideoDriver_endScene,[driver]
			; cinvoke IrrlichtDevice_sleep,[device],100
		yeld:
			cinvoke IrrlichtDevice_yield,[device]
		cinvoke IrrlichtDevice_run,[device]
		cmp eax,FALSE
		jb IrrlichtDevice_end_loop
		jne IrrlichtDevice_run_loop
	IrrlichtDevice_end_loop:
		cinvoke IrrlichtDevice_closeDevice,[device]
		invoke ExitProcess,0

section '.data' data readable writeable
	window_caption du 'Irrlicht Engine Window (А это русский текст ЁЖИКЪ ой)',0
	; evd SExposedVideoData
	video_data dd ?
	windowSize dd ?
	color dd ?
	device dd ?
	driver dd ?
	scene_manager dd ?

section '.idata' import data readable writeable

	library kernel,'kernel32.dll',irrlicht_c,'irrlicht_c.dll';,irrlicht,'irrlicht.dll'
	import kernel,ExitProcess,'ExitProcess'
	; import irrlicht,createDevice,'createDevice'

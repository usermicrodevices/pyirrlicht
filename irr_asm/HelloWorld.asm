format PE GUI 4.0
entry start

include '%fasminc%/win32w.inc'
include 'irr_inc/irrlicht.inc'

section '.text' code readable executable

start:
	cinvoke SExposedVideoData_ctor1
	mov [video_data],eax
	cinvoke dimension2du_ctor2,640,480
	mov [windowSize],eax
	cinvoke SColor_ctor2,255,100,101,140
	mov [color],eax
	cinvoke IrrlichtDevice_createDevice,EDT_OPENGL,[windowSize],16,FALSE,FALSE,FALSE,NULL
	mov [device],eax
	cinvoke IrrlichtDevice_setWindowCaption,[device],window_caption
	cinvoke IrrlichtDevice_setResizable,[device],TRUE
	cinvoke IrrlichtDevice_getVideoDriver,[device]
	mov [driver],eax
	cinvoke IrrlichtDevice_getSceneManager,[device]
	mov [scene_manager],eax
	cinvoke IrrlichtDevice_getGUIEnvironment,[device]
	mov [gui_environment],eax
	cinvoke recti_ctor2,10,10,260,22
	mov [recti],eax
	cinvoke IGUIEnvironment_addStaticText,[gui_environment],static_text,[recti],TRUE,TRUE,NULL,-1,FALSE
	mov [ptrStaticText],eax
	cinvoke ISceneManager_getMesh,[scene_manager],mesh_path
	mov [i_animated_mesh],eax
	cinvoke vector3df_ctor2,0.0,0.0,0.0
	mov [position],eax
	cinvoke vector3df_ctor2,0.0,0.0,0.0
	mov [rotation],eax
	cinvoke vector3df_ctor2,1.0,1.0,1.0
	mov [scale],eax
	cinvoke ISceneManager_addAnimatedMeshSceneNode,[scene_manager],[i_animated_mesh],NULL,-1,[position],[rotation],[scale],FALSE
	mov [node],eax
	cinvoke ISceneNode_setMaterialFlag,[node],EMF_LIGHTING,FALSE
	cinvoke IAnimatedMeshSceneNode_setMD2Animation1,[node],EMAT_STAND
	cinvoke IVideoDriver_getTexture1,[driver],texture_path
	mov [texture],eax
	cinvoke ISceneNode_setMaterialTexture,[node],NULL,[texture]
	cinvoke vector3df_ctor2,0.0,30.0,-40.0
	mov [position],eax
	cinvoke vector3df_ctor2,0.0,5.0,0.0
	mov [lookat],eax
	cinvoke ISceneManager_addCameraSceneNode,[scene_manager],[node],[position],[lookat]
	mov [camera],eax
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
			cinvoke ISceneManager_drawAll,[scene_manager]
			cinvoke IGUIEnvironment_drawAll,[gui_environment]
			cinvoke IVideoDriver_endScene,[driver]
			; cinvoke IrrlichtDevice_sleep,[device],10
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
	window_caption du 'Hello World! - Irrlicht Engine Demo',0
	static_text du 'Hello World! This is the Irrlicht Software renderer!',0
	mesh_path db 'media/sydney.md2',0
	texture_path db 'media/sydney.bmp',0
	video_data dd ?
	windowSize dd ?
	color dd ?
	device dd ?
	driver dd ?
	scene_manager dd ?
	gui_environment dd ?
	recti dd ?
	ptrStaticText dd ?
	i_animated_mesh dd ?
	node dd ?
	position dd ?
	lookat dd ?
	texture dd ?
	camera dd ?
	rotation dd ?
	scale dd ?

section '.idata' import data readable writeable

	library kernel,'kernel32.dll',irrlicht_c,'irrlicht_c.dll'
	import kernel,ExitProcess,'ExitProcess'

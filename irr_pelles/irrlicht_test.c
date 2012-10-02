// Copyright(c) Maxim Kolosov 2012 pyirrlicht@gmail.com
// http://pir.sourceforge.net (http://code.google.com/p/pyirrlicht)
// BSD license

#pragma lib "irrlicht_c.lib"

#define WIN32_DEFAULT_LIBS

#include <windows.h>
#include "irrlicht_test.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	void* windowSize = dimension2du_ctor2(320, 240);
	void* color = SColor_ctor2(255, 100, 101, 140);
	void* device = IrrlichtDevice_createDevice(EDT_OPENGL, windowSize, 16, false, false, false, NULL);
	IrrlichtDevice_setWindowCaption(device, L"Irrlicht Demo");
	IrrlichtDevice_setResizable(device, true);
	void* video_driver = IrrlichtDevice_getVideoDriver(device);
	IVideoDriver_SetIcon(video_driver, IDR_ICO_MAIN, false);
	void* scene_manager = IrrlichtDevice_getSceneManager(device);
	void* gui_environment = IrrlichtDevice_getGUIEnvironment(device);
	const fschar_t mesh_path[17] = "media/sydney.md2";
	void* i_animated_mesh = ISceneManager_getMesh(scene_manager, mesh_path);
	if(i_animated_mesh)
	{
		void* position = vector3df_ctor2(0.0, 0.0, 0.0);
		void* rotation = vector3df_ctor2(0.0, 0.0, 0.0);
		void* scale = vector3df_ctor2(1.0, 1.0, 1.0);
		void* node = ISceneManager_addAnimatedMeshSceneNode(scene_manager, i_animated_mesh, NULL, -1, position, rotation, scale, false);
		if(node)
		{
			ISceneNode_setMaterialFlag(node, EMF_LIGHTING, false);
			IAnimatedMeshSceneNode_setMD2Animation1(node, EMAT_STAND);
			void* texture = IVideoDriver_getTexture1(video_driver, "media/sydney.bmp");
			ISceneNode_setMaterialTexture(node, 0, texture);
			void* position_camera = vector3df_ctor2(0.0, 30.0, -40.0);
			void* lookat = vector3df_ctor2(0.0, 5.0, 0.0);
			void* camera = ISceneManager_addCameraSceneNode(scene_manager, node, position_camera, lookat, -1);
		}
	}
	while(IrrlichtDevice_run(device))
	{
		if(IrrlichtDevice_isWindowActive(device))
		{
			IVideoDriver_beginSceneDefault(video_driver, true, true, color);
			ISceneManager_drawAll(scene_manager);
			IGUIEnvironment_drawAll(gui_environment);
			IVideoDriver_endScene(video_driver);
			IrrlichtDevice_sleep(device, 10, false);
		}
		else
			IrrlichtDevice_yield(device);
	}
	IrrlichtDevice_closeDevice(device);
	return 0;
}

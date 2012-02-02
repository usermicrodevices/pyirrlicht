// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IrrlichtDevice
//IRRLICHT_C_API IrrlichtDevice* IrrlichtDevice_createDevice(E_DRIVER_TYPE deviceType = video::EDT_SOFTWARE, const core::dimension2d<u32>& windowSize = (core::dimension2d<u32>(640,480)), u32 bits = 16, bool fullscreen = false, bool stencilbuffer = false, bool vsync = false, void* receiver = 0)
IRRLICHT_C_API IrrlichtDevice* IrrlichtDevice_createDevice(E_DRIVER_TYPE deviceType = video::EDT_SOFTWARE, const core::dimension2d<u32>& windowSize = (core::dimension2d<u32>(640,480)), u32 bits = 16, bool fullscreen = false, bool stencilbuffer = false, bool vsync = false, IEventReceiver* receiver = 0)
{
	//return createDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, (IEventReceiver*)receiver);
	return createDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver);
}
IRRLICHT_C_API IrrlichtDevice* IrrlichtDevice_createDevice2(E_DRIVER_TYPE deviceType = video::EDT_SOFTWARE, const core::dimension2d<u32>& windowSize = (core::dimension2d<u32>(640,480)), u32 bits = 16, bool fullscreen = false, bool stencilbuffer = false, bool vsync = false, bool create_receiver = false)
{
	if (create_receiver)
	{
		return createDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, new UserEventReceiver());
	}
	else
	{
		return createDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, 0);
	}
}
IRRLICHT_C_API IrrlichtDevice* IrrlichtDevice_createDeviceEx(const SIrrlichtCreationParameters& parameters){return createDeviceEx(parameters);}
IRRLICHT_C_API bool IrrlichtDevice_run(IrrlichtDevice* pointer)
{
#ifdef _MSC_VER
	__try
	{
#endif
		return pointer->run();
#ifdef _MSC_VER
	}
	//__except(filter(GetExceptionCode(), GetExceptionInformation()))
	__except(filter(_exception_code(), (struct _EXCEPTION_POINTERS *)_exception_info(), "IrrlichtDevice->run()"))
	{
		//puts("IrrlichtDevice->run() - ERROR EXECUTION");
		return false;
	}
#endif
}
IRRLICHT_C_API void IrrlichtDevice_yield(IrrlichtDevice* pointer){pointer->yield();}
IRRLICHT_C_API void IrrlichtDevice_sleep(IrrlichtDevice* pointer, u32 timeMs, bool pauseTimer=false){pointer->sleep(timeMs, pauseTimer);}
IRRLICHT_C_API IVideoDriver* IrrlichtDevice_getVideoDriver(IrrlichtDevice* pointer){return pointer->getVideoDriver();}
IRRLICHT_C_API IFileSystem* IrrlichtDevice_getFileSystem(IrrlichtDevice* pointer){return pointer->getFileSystem();}
IRRLICHT_C_API IGUIEnvironment* IrrlichtDevice_getGUIEnvironment(IrrlichtDevice* pointer){return pointer->getGUIEnvironment();}
IRRLICHT_C_API ISceneManager* IrrlichtDevice_getSceneManager(IrrlichtDevice* pointer){return pointer->getSceneManager();}
IRRLICHT_C_API ICursorControl* IrrlichtDevice_getCursorControl(IrrlichtDevice* pointer){return pointer->getCursorControl();}
IRRLICHT_C_API ILogger* IrrlichtDevice_getLogger(IrrlichtDevice* pointer){return pointer->getLogger();}
IRRLICHT_C_API IVideoModeList* IrrlichtDevice_getVideoModeList(IrrlichtDevice* pointer){return pointer->getVideoModeList();}
IRRLICHT_C_API IOSOperator* IrrlichtDevice_getOSOperator(IrrlichtDevice* pointer){return pointer->getOSOperator();}
IRRLICHT_C_API ITimer* IrrlichtDevice_getTimer(IrrlichtDevice* pointer){return pointer->getTimer();}
IRRLICHT_C_API void IrrlichtDevice_setWindowCaption(IrrlichtDevice* pointer, const wchar_t* text){pointer->setWindowCaption(text);}
IRRLICHT_C_API bool IrrlichtDevice_isWindowActive(IrrlichtDevice* pointer){return pointer->isWindowActive();}
IRRLICHT_C_API bool IrrlichtDevice_isWindowFocused(IrrlichtDevice* pointer){return pointer->isWindowFocused();}
IRRLICHT_C_API bool IrrlichtDevice_isWindowMinimized(IrrlichtDevice* pointer){return pointer->isWindowMinimized();}
IRRLICHT_C_API bool IrrlichtDevice_isFullscreen(IrrlichtDevice* pointer){return pointer->isFullscreen();}
IRRLICHT_C_API ECOLOR_FORMAT IrrlichtDevice_getColorFormat(IrrlichtDevice* pointer){return pointer->getColorFormat();}
IRRLICHT_C_API void IrrlichtDevice_closeDevice(IrrlichtDevice* pointer){pointer->closeDevice();}
IRRLICHT_C_API const c8* IrrlichtDevice_getVersion(IrrlichtDevice* pointer){return pointer->getVersion();}
IRRLICHT_C_API void IrrlichtDevice_setEventReceiver(IrrlichtDevice* pointer, IEventReceiver* receiver){pointer->setEventReceiver(receiver);}
IRRLICHT_C_API IEventReceiver* IrrlichtDevice_getEventReceiver(IrrlichtDevice* pointer){return pointer->getEventReceiver();}
IRRLICHT_C_API bool IrrlichtDevice_postEventFromUser(IrrlichtDevice* pointer, const SEvent& event){return pointer->postEventFromUser(event);}
IRRLICHT_C_API void IrrlichtDevice_setInputReceivingSceneManager(IrrlichtDevice* pointer, scene::ISceneManager* sceneManager){pointer->setInputReceivingSceneManager(sceneManager);}
IRRLICHT_C_API void IrrlichtDevice_setResizable(IrrlichtDevice* pointer, bool resize=false){pointer->setResizable(resize);}
IRRLICHT_C_API void IrrlichtDevice_minimizeWindow(IrrlichtDevice* pointer){pointer->minimizeWindow();}
IRRLICHT_C_API void IrrlichtDevice_maximizeWindow(IrrlichtDevice* pointer){pointer->maximizeWindow();}
IRRLICHT_C_API void IrrlichtDevice_restoreWindow(IrrlichtDevice* pointer){pointer->restoreWindow();}
IRRLICHT_C_API bool IrrlichtDevice_activateJoysticks(IrrlichtDevice* pointer, core::array<SJoystickInfo>& joystickInfo){return pointer->activateJoysticks(joystickInfo);}
IRRLICHT_C_API bool IrrlichtDevice_setGammaRamp(IrrlichtDevice* pointer, f32 red, f32 green, f32 blue, f32 relativebrightness, f32 relativecontrast){return pointer->setGammaRamp(red, green, blue, relativebrightness, relativecontrast);}
IRRLICHT_C_API bool IrrlichtDevice_getGammaRamp(IrrlichtDevice* pointer, f32 &red, f32 &green, f32 &blue, f32 &brightness, f32 &contrast){return pointer->getGammaRamp(red, green, blue, brightness, contrast);}
IRRLICHT_C_API E_DEVICE_TYPE IrrlichtDevice_getType(IrrlichtDevice* pointer){return pointer->getType();}
IRRLICHT_C_API bool IrrlichtDevice_isDriverSupported(IrrlichtDevice* pointer, video::E_DRIVER_TYPE driver){return pointer->isDriverSupported(driver);}

//IRRLICHT_C_API void IrrlichtDevice_SetIcon(IrrlichtDevice* pointer, int icon_id = 32512, bool big_icon = false)//ICON_SMALL,ICON_BIG
//{
//#ifdef _MSC_VER
//#include <Windows.h>
//	SendMessage(HWND(pointer->getVideoDriver()->getExposedVideoData().OpenGLWin32.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), (LPCTSTR)icon_id));
//#endif
//}

#ifdef __cplusplus
}
#endif

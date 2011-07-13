// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

// main loop helper example
class MainLoop
{
public:
	MainLoop(IrrlichtDevice* device, video::IVideoDriver* driver, scene::ISceneManager* smgr = 0, IGUIEnvironment* guienv = 0, bool backBuffer = true, bool zBuffer = true, SColor color = SColor(255,0,0,0), SExposedVideoData* videoData = 0, core::rect<s32>* sourceRect = 0, u32 time_ms = 0, bool pause_timer = false)
	{
		irrlicht_device = device;
		video_driver = driver;
		scene_manager = smgr;
		gui_environment = guienv;
		back_buffer = backBuffer;
		z_buffer = zBuffer;
		scene_color = color;
		if(videoData)
		{
			exposed_video_data = videoData;
			delete_exposed_video_data = false;
		}
		else
		{
			exposed_video_data = new SExposedVideoData();
			delete_exposed_video_data = true;
		}
		source_rect = sourceRect;
		sleep_time_ms = time_ms;
		sleep_pause_timer = pause_timer;
		execute_loop = true;
	}
	void start()
	{
		int fps = -1;
		int lastFPS = -1;
		while(irrlicht_device->run() && video_driver && execute_loop)
		{
			if(irrlicht_device->isWindowActive())
			{
				if(video_driver->beginScene(back_buffer, z_buffer, scene_color, *exposed_video_data, source_rect))
				{
					if(scene_manager)
						scene_manager->drawAll();
					if(gui_environment)
						gui_environment->drawAll();
					video_driver->endScene();
				}
				if(sleep_time_ms)
					irrlicht_device->sleep(sleep_time_ms, sleep_pause_timer);

				fps = video_driver->getFPS();

				if (lastFPS != fps)
				{
					core::stringw str = L"Irrlicht Engine [";
					str += video_driver->getName();
					str += "] FPS:";
					str += fps;

					irrlicht_device->setWindowCaption(str.c_str());
					lastFPS = fps;
				}
			}
			else
				irrlicht_device->yield();
		}
	}
	void stop()
	{
		execute_loop = false;
	}
	~MainLoop()
	{
		//irrlicht_device->closeDevice();
		//irrlicht_device->drop();
		if(delete_exposed_video_data)
			delete[] exposed_video_data;
	}
private:
	IrrlichtDevice* irrlicht_device;
	video::IVideoDriver* video_driver;
	scene::ISceneManager* scene_manager;
	IGUIEnvironment* gui_environment;
	bool back_buffer;
	bool z_buffer;
	SColor scene_color;
	irr::video::SExposedVideoData* exposed_video_data;
	bool delete_exposed_video_data;
	core::rect<s32>* source_rect;
	u32 sleep_time_ms;
	bool sleep_pause_timer;
	bool execute_loop;
};

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API MainLoop* MainLoop_ctor(IrrlichtDevice* device, video::IVideoDriver* driver, scene::ISceneManager* smgr = 0, IGUIEnvironment* guienv = 0, bool backBuffer = true, bool zBuffer = true, SColor* color = 0, SExposedVideoData* videoData = 0, core::rect<s32>* sourceRect = 0, u32 time_ms = 0, bool pause_timer = false)
{return new MainLoop(device, driver, smgr, guienv, backBuffer, zBuffer, *color, videoData, sourceRect, time_ms, pause_timer);}
IRRLICHT_C_API void MainLoop_start(MainLoop* pointer){pointer->start();}
IRRLICHT_C_API void MainLoop_stop(MainLoop* pointer){pointer->stop();}

#ifdef __cplusplus
}
#endif

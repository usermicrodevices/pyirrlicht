//~ #include <stdio.h>
#include <stdbool.h>
#include <windows.h>

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef signed short s16;
typedef signed int s32;
typedef char c8;
typedef float f32;
typedef double f64;

typedef enum
{
	EIDT_WIN32,
	EIDT_WINCE,
	EIDT_X11,
	EIDT_OSX,
	EIDT_SDL,
	EIDT_FRAMEBUFFER,
	EIDT_CONSOLE,
	EIDT_BEST
} E_DEVICE_TYPE;

typedef enum
{
	EDT_NULL,
	EDT_SOFTWARE,
	EDT_BURNINGSVIDEO,
	EDT_DIRECT3D8,
	EDT_DIRECT3D9,
	EDT_OPENGL,
	EDT_COUNT
} E_DRIVER_TYPE;

typedef enum
{
	ELL_INFORMATION,
	ELL_WARNING,
	ELL_ERROR,
	ELL_NONE
} ELOG_LEVEL;

typedef enum
{
	ECF_A1R5G5B5 = 0,
	ECF_R5G6B5,
	ECF_R8G8B8,
	ECF_A8R8G8B8,
	ECF_R16F,
	ECF_G16R16F,
	ECF_A16B16G16R16F,
	ECF_R32F,
	ECF_G32R32F,
	ECF_A32B32G32R32F,
	ECF_UNKNOWN
} ECOLOR_FORMAT;

typedef struct
{
	E_DEVICE_TYPE DeviceType;
	E_DRIVER_TYPE DriverType;
	void* WindowSize;
	u8 Bits;
	u8 ZBufferBits;
	bool Fullscreen;
	bool Stencilbuffer;
	bool Vsync;
	u8 AntiAlias;
	bool WithAlphaChannel;
	bool Doublebuffer;
	bool IgnoreInput;
	bool Stereobuffer;
	bool HighPrecisionFPU;
	void* EventReceiver;
	void* WindowId;
	ELOG_LEVEL LoggingLevel;
	const c8* const SDK_version_do_not_use;
} SIrrlichtCreationParameters;

typedef struct{u32 Width; u32 Height;} dimension2du;

typedef struct{u32 color;} SColor;

typedef struct IDirect3D9;
typedef struct IDirect3DDevice9;
typedef struct IDirect3D8;
typedef struct IDirect3DDevice8;

typedef struct
{
	union
	{
		struct
		{
			//~ IDirect3D9* D3D9;
			//~ IDirect3DDevice9* D3DDev9;
			void* HWnd;
		} D3D9;
		struct
		{
			//~ IDirect3D8* D3D8;
			//~ IDirect3DDevice8* D3DDev8;
			void* HWnd;
		} D3D8;
		struct
		{
			void* HDc;
			void* HRc;
			void* HWnd;
		} OpenGLWin32;
		struct
		{
			void* X11Display;
			void* X11Context;
			unsigned long X11Window;
		} OpenGLLinux;
	};
} SExposedVideoData;

void* createDevice(E_DRIVER_TYPE deviceType, const dimension2du* windowSize, u32 bits, bool fullscreen, bool stencilbuffer, bool vsync, void* receiver);
void* createDeviceEx(const SIrrlichtCreationParameters* parameters);

int WINAPI WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR     lpCmdLine,
	int       nCmdShow)
{
	SColor color;
	color.color = 0x0000FF;
	dimension2du windowSize;
	windowSize.Width = 320;
	windowSize.Height = 240;
	void* device = createDevice(EDT_SOFTWARE, &windowSize, 16, false, false, false, NULL);
	int* vptr_device = *(int**)device;
	//~ asm volatile ("movl %0, %%ecx;" : : "a" (device));
	//~ printf("Irrlicht version %s\n", ((const c8*(*)())vptr_device[19])());
	void* video_driver = ((void*(*)())vptr_device[3])();
	MessageBox(0, ((const c8*(*)())vptr_device[19])(), "Irrlicht version", MB_ICONINFORMATION);
	//~ int* vptr_video_driver = *(int**)video_driver;
	//~ asm volatile ("movl %0, %%ecx;" : : "a" (video_driver));
	//~ void* scene_manager = ((void*(*)())vptr_device[6])();
	//~ int* vptr_scene_manager = *(int**)scene_manager;
	//~ while (((bool(*)())vptr_device[0])())
	//~ {
		//~ ((bool(*)())vptr_video_driver[0])(true, true, color);
		//~ ((void(*)())vptr_scene_manager[45])();
		//~ ((bool(*)())vptr_video_driver[1])();
	//~ }
	//~ ((void(*)())vptr_device[18])();
	return 0;
}

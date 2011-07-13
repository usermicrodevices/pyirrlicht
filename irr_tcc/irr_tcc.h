#include <stdbool.h>

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef signed short s16;
typedef signed int s32;
typedef char c8;
typedef float f32;
typedef double f64;

#if defined(_IRR_WCHAR_FILESYSTEM)
	typedef wchar_t fschar_t;
#else
	typedef char fschar_t;
#endif

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

typedef enum
{
	EMF_WIREFRAME = 0x1,
	EMF_POINTCLOUD = 0x2,
	EMF_GOURAUD_SHADING = 0x4,
	EMF_LIGHTING = 0x8,
	EMF_ZBUFFER = 0x10,
	EMF_ZWRITE_ENABLE = 0x20,
	EMF_BACK_FACE_CULLING = 0x40,
	EMF_FRONT_FACE_CULLING = 0x80,
	EMF_BILINEAR_FILTER = 0x100,
	EMF_TRILINEAR_FILTER = 0x200,
	EMF_ANISOTROPIC_FILTER = 0x400,
	EMF_FOG_ENABLE = 0x800,
	EMF_NORMALIZE_NORMALS = 0x1000,
	EMF_TEXTURE_WRAP = 0x2000,
	EMF_ANTI_ALIASING = 0x4000,
	EMF_COLOR_MASK = 0x8000,
	EMF_COLOR_MATERIAL = 0x10000
} E_MATERIAL_FLAG;

typedef enum
{
	EMAT_STAND,
	EMAT_RUN,
	EMAT_ATTACK,
	EMAT_PAIN_A,
	EMAT_PAIN_B,
	EMAT_PAIN_C,
	EMAT_JUMP,
	EMAT_FLIP,
	EMAT_SALUTE,
	EMAT_FALLBACK,
	EMAT_WAVE,
	EMAT_POINT,
	EMAT_CROUCH_STAND,
	EMAT_CROUCH_WALK,
	EMAT_CROUCH_ATTACK,
	EMAT_CROUCH_PAIN,
	EMAT_CROUCH_DEATH,
	EMAT_DEATH_FALLBACK,
	EMAT_DEATH_FALLFORWARD,
	EMAT_DEATH_FALLBACKSLOW,
	EMAT_BOOM,
	EMAT_COUNT
} EMD2_ANIMATION_TYPE;

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

void* SColor_ctor1();
void* SColor_ctor2(u32 a, u32 r, u32 g, u32 b);
void* SColor_ctor3(u32 clr);

void* dimension2du_ctor2(u32 w, u32 h);

void* vector3df_ctor2(f32 x, f32 y, f32 z);

void ISceneNode_setMaterialFlag(void* pointer, E_MATERIAL_FLAG flag, bool newvalue);
void ISceneNode_setMaterialTexture(void* pointer, u32 textureLayer, void* texture);

bool IAnimatedMeshSceneNode_setMD2Animation1(void* pointer, EMD2_ANIMATION_TYPE anim);

bool IVideoDriver_beginScene(void* pointer, bool backBuffer, bool zBuffer, const void* color, const void* videoData, void* sourceRect);
bool IVideoDriver_beginSceneDefault(void* pointer, bool backBuffer, bool zBuffer, const void* color);
bool IVideoDriver_endScene(void* pointer);
void* IVideoDriver_getTexture1(void* pointer, const fschar_t* filename);

void* ISceneManager_getMesh(void* pointer, const fschar_t* path);
void* ISceneManager_addAnimatedMeshSceneNode();
void* ISceneManager_addAnimatedMeshSceneNode(void* pointer, void* mesh, void* parent, s32 id, const void* position, const void* rotation, const void* scale, bool alsoAddIfMeshPointerZero);
void* ISceneManager_addCameraSceneNode(void* pointer, void* parent, const void* position, const void* lookat, s32 id);
void ISceneManager_drawAll(void* pointer);

void IGUIEnvironment_drawAll(void* pointer);

void* IrrlichtDevice_createDevice(E_DRIVER_TYPE deviceType, const void* windowSize, u32 bits, bool fullscreen, bool stencilbuffer, bool vsync, void* receiver);
void* IrrlichtDevice_createDevice2(E_DRIVER_TYPE deviceType, const void* windowSize, u32 bits, bool fullscreen, bool stencilbuffer, bool vsync, bool create_receiver);
void* IrrlichtDevice_createDeviceEx(const SIrrlichtCreationParameters* parameters);
bool IrrlichtDevice_run(void* pointer);
void IrrlichtDevice_yield(void* pointer);
void IrrlichtDevice_sleep(void* pointer, u32 timeMs, bool pauseTimer);
void* IrrlichtDevice_getVideoDriver(void* pointer);
void* IrrlichtDevice_getFileSystem(void* pointer);
void* IrrlichtDevice_getGUIEnvironment(void* pointer);
void* IrrlichtDevice_getSceneManager(void* pointer);
void* IrrlichtDevice_getCursorControl(void* pointer);
void* IrrlichtDevice_getLogger(void* pointer);
void* IrrlichtDevice_getVideoModeList(void* pointer);
void* IrrlichtDevice_getOSOperator(void* pointer);
void* IrrlichtDevice_getTimer(void* pointer);
void IrrlichtDevice_setWindowCaption(void* pointer, const wchar_t* text);
bool IrrlichtDevice_isWindowActive(void* pointer);
bool IrrlichtDevice_isWindowFocused(void* pointer);
bool IrrlichtDevice_isWindowMinimized(void* pointer);
bool IrrlichtDevice_isFullscreen(void* pointer);
ECOLOR_FORMAT IrrlichtDevice_getColorFormat(void* pointer);
void IrrlichtDevice_closeDevice(void* pointer);
const c8* IrrlichtDevice_getVersion(void* pointer);
void IrrlichtDevice_setEventReceiver(void* pointer, void* receiver);
void* IrrlichtDevice_getEventReceiver(void* pointer);
//bool IrrlichtDevice_postEventFromUser(void* pointer, const SEvent& event);
void IrrlichtDevice_setInputReceivingSceneManager(void* pointer, void* sceneManager);
void IrrlichtDevice_setResizable(void* pointer, bool resize);
void IrrlichtDevice_minimizeWindow(void* pointer);
void IrrlichtDevice_maximizeWindow(void* pointer);
void IrrlichtDevice_restoreWindow(void* pointer);
//bool IrrlichtDevice_activateJoysticks(void* pointer, core::array<SJoystickInfo>& joystickInfo);
bool IrrlichtDevice_setGammaRamp(void* pointer, f32 red, f32 green, f32 blue, f32 relativebrightness, f32 relativecontrast);
bool IrrlichtDevice_getGammaRamp(void* pointer, f32 *red, f32 *green, f32 *blue, f32 *brightness, f32 *contrast);
E_DEVICE_TYPE IrrlichtDevice_getType(void* pointer);
bool IrrlichtDevice_isDriverSupported(void* pointer, E_DRIVER_TYPE driver);

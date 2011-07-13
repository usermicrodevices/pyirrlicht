// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

struct d3d8
{
	IDirect3D8* D3D8;
	IDirect3DDevice8* D3DDev8;
	void* HWnd;
} D3D8;

struct d3d9
{
	IDirect3D9* D3D9;
	IDirect3DDevice9* D3DDev9;
	void* HWnd;
} D3D9;

struct openglwin32
{
	void* HDc;
	void* HRc;
	void* HWnd;
} OpenGLWin32;

struct opengllinux
{
	void* X11Display;
	void* X11Context;
	unsigned long X11Window;
} OpenGLLinux;

//================= D3D8
IRRLICHT_C_API IDirect3D8* D3D8_get_D3D8(d3d8* pointer){return pointer->D3D8;}
IRRLICHT_C_API IDirect3DDevice8* D3D8_get_D3DDev8(d3d8* pointer){return pointer->D3DDev8;}
IRRLICHT_C_API void* D3D8_get_HWnd(d3d8* pointer){return pointer->HWnd;}
IRRLICHT_C_API void D3D8_set_D3D8(d3d8* pointer, IDirect3D8* value){pointer->D3D8 = value;}
IRRLICHT_C_API void D3D8_set_D3DDev8(d3d8* pointer, IDirect3DDevice8* value){pointer->D3DDev8 = value;}
IRRLICHT_C_API void D3D8_set_HWnd(d3d8* pointer, void* value){pointer->HWnd = value;}

//================= D3D9
IRRLICHT_C_API IDirect3D9* D3D9_get_D3D9(d3d9* pointer){return pointer->D3D9;}
IRRLICHT_C_API IDirect3DDevice9* D3D9_get_D3DDev9(d3d9* pointer){return pointer->D3DDev9;}
IRRLICHT_C_API void* D3D9_get_HWnd(d3d9* pointer){return pointer->HWnd;}
IRRLICHT_C_API void D3D9_set_D3D9(d3d9* pointer, IDirect3D9* value){pointer->D3D9 = value;}
IRRLICHT_C_API void D3D9_set_D3DDev9(d3d9* pointer, IDirect3DDevice9* value){pointer->D3DDev9 = value;}
IRRLICHT_C_API void D3D9_set_HWnd(d3d9* pointer, void* value){pointer->HWnd = value;}

//================= OpenGLWin32
IRRLICHT_C_API void* OpenGLWin32_get_HDc(openglwin32* pointer){return pointer->HDc;}
IRRLICHT_C_API void* OpenGLWin32_get_HRc(openglwin32* pointer){return pointer->HRc;}
IRRLICHT_C_API void* OpenGLWin32_get_HWnd(openglwin32* pointer){return pointer->HWnd;}
IRRLICHT_C_API void OpenGLWin32_set_HDc(openglwin32* pointer, void* value){pointer->HDc = value;}
IRRLICHT_C_API void OpenGLWin32_set_HRc(openglwin32* pointer, void* value){pointer->HRc = value;}
IRRLICHT_C_API void OpenGLWin32_set_HWnd(openglwin32* pointer, void* value){pointer->HWnd = value;}

//================= OpenGLLinux
IRRLICHT_C_API void* OpenGLLinux_get_X11Display(opengllinux* pointer){return pointer->X11Display;}
IRRLICHT_C_API void* OpenGLLinux_get_X11Context(opengllinux* pointer){return pointer->X11Context;}
IRRLICHT_C_API unsigned long OpenGLLinux_get_X11Window(opengllinux* pointer){return pointer->X11Window;}
IRRLICHT_C_API void OpenGLLinux_set_X11Display(opengllinux* pointer, void* value){pointer->X11Display = value;}
IRRLICHT_C_API void OpenGLLinux_set_X11Context(opengllinux* pointer, void* value){pointer->X11Context = value;}
IRRLICHT_C_API void OpenGLLinux_set_X11Window(opengllinux* pointer, unsigned long value){pointer->X11Window = value;}

//================= SExposedVideoData
IRRLICHT_C_API SExposedVideoData* SExposedVideoData_ctor1(){return new SExposedVideoData();}
IRRLICHT_C_API SExposedVideoData* SExposedVideoData_ctor2(void* Window){return new SExposedVideoData(Window);}
//IRRLICHT_C_API void SExposedVideoData_destructor(SExposedVideoData* pointer){delete pointer;}

IRRLICHT_C_API void* SExposedVideoData_get_D3D8(SExposedVideoData* pointer){return &pointer->D3D8;}
//IRRLICHT_C_API void SExposedVideoData_set_D3D8(SExposedVideoData* pointer, d3d8* value){&pointer->D3D8 = value;}
IRRLICHT_C_API IDirect3D8* SExposedVideoData_get_D3D8_D3D8(SExposedVideoData* pointer){return pointer->D3D8.D3D8;}
IRRLICHT_C_API IDirect3DDevice8* SExposedVideoData_get_D3D8_D3DDev8(SExposedVideoData* pointer){return pointer->D3D8.D3DDev8;}
IRRLICHT_C_API void* SExposedVideoData_get_D3D8_HWnd(SExposedVideoData* pointer){return pointer->D3D8.HWnd;}

IRRLICHT_C_API void* SExposedVideoData_get_D3D9(SExposedVideoData* pointer){return &pointer->D3D9;}
IRRLICHT_C_API IDirect3D9* SExposedVideoData_get_D3D9_D3D9(SExposedVideoData* pointer){return pointer->D3D9.D3D9;}
IRRLICHT_C_API IDirect3DDevice9* SExposedVideoData_get_D3D9_D3DDev9(SExposedVideoData* pointer){return pointer->D3D9.D3DDev9;}
IRRLICHT_C_API void* SExposedVideoData_get_D3D9_HWnd(SExposedVideoData* pointer){return pointer->D3D9.HWnd;}

IRRLICHT_C_API void* SExposedVideoData_get_OpenGLWin32(SExposedVideoData* pointer){return &pointer->OpenGLWin32;}
IRRLICHT_C_API void* SExposedVideoData_get_OpenGLWin32_HDc(SExposedVideoData* pointer){return pointer->OpenGLWin32.HDc;}
IRRLICHT_C_API void* SExposedVideoData_get_OpenGLWin32_HRc(SExposedVideoData* pointer){return pointer->OpenGLWin32.HRc;}
IRRLICHT_C_API void* SExposedVideoData_get_OpenGLWin32_HWnd(SExposedVideoData* pointer){return pointer->OpenGLWin32.HWnd;}

IRRLICHT_C_API void* SExposedVideoData_get_OpenGLLinux(SExposedVideoData* pointer){return &pointer->OpenGLLinux;}
IRRLICHT_C_API void* SExposedVideoData_get_OpenGLLinux_X11Display(SExposedVideoData* pointer){return pointer->OpenGLLinux.X11Display;}
IRRLICHT_C_API void* SExposedVideoData_get_OpenGLLinux_X11Context(SExposedVideoData* pointer){return pointer->OpenGLLinux.X11Context;}
IRRLICHT_C_API unsigned long SExposedVideoData_get_OpenGLLinux_X11Window(SExposedVideoData* pointer){return pointer->OpenGLLinux.X11Window;}

IRRLICHT_C_API void SExposedVideoData_set_D3D8_D3D8(SExposedVideoData* pointer, IDirect3D8* value){pointer->D3D8.D3D8 = value;}
IRRLICHT_C_API void SExposedVideoData_set_D3D8_D3DDev8(SExposedVideoData* pointer, IDirect3DDevice8* value){pointer->D3D8.D3DDev8 = value;}
IRRLICHT_C_API void SExposedVideoData_set_D3D8_HWnd(SExposedVideoData* pointer, void* value){pointer->D3D8.HWnd = value;}

IRRLICHT_C_API void SExposedVideoData_set_D3D9_D3D9(SExposedVideoData* pointer, IDirect3D9* value){pointer->D3D9.D3D9 = value;}
IRRLICHT_C_API void SExposedVideoData_set_D3D9_D3DDev9(SExposedVideoData* pointer, IDirect3DDevice9* value){pointer->D3D9.D3DDev9 = value;}
IRRLICHT_C_API void SExposedVideoData_set_D3D9_HWnd(SExposedVideoData* pointer, void* value){pointer->D3D9.HWnd = value;}

IRRLICHT_C_API void SExposedVideoData_set_OpenGLWin32_HDc(SExposedVideoData* pointer, void* value){pointer->OpenGLWin32.HDc = value;}
IRRLICHT_C_API void SExposedVideoData_set_OpenGLWin32_HRc(SExposedVideoData* pointer, void* value){pointer->OpenGLWin32.HRc = value;}
IRRLICHT_C_API void SExposedVideoData_set_OpenGLWin32_HWnd(SExposedVideoData* pointer, void* value){pointer->OpenGLWin32.HWnd = value;}

IRRLICHT_C_API void SExposedVideoData_set_OpenGLLinux_X11Display(SExposedVideoData* pointer, void* value){pointer->OpenGLLinux.X11Display = value;}
IRRLICHT_C_API void SExposedVideoData_set_OpenGLLinux_X11Context(SExposedVideoData* pointer, void* value){pointer->OpenGLLinux.X11Context = value;}
IRRLICHT_C_API void SExposedVideoData_set_OpenGLLinux_X11Window(SExposedVideoData* pointer, unsigned long value){pointer->OpenGLLinux.X11Window = value;}


#ifdef __cplusplus
}
#endif

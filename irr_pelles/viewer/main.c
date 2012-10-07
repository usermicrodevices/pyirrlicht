// Copyright(c) Maxim Kolosov 2012 maxkolosov@inbox.ru
// http://pir.sf.net
// BSD license

#pragma lib "irrlicht_c.lib"
// only for EDT_OPENGL driver type and wglShareLists function, else you can comment next line
#pragma lib "opengl32.lib"

#define UNICODE
#define _UNICODE
#define WIN32_DEFAULT_LIBS
#define WIN32_LEAN_AND_MEAN  /* speed up compilations */

#include <windows.h>
#include <windowsx.h>
#include <commctrl.h>
#include <commdlg.h>

//~ #include <stdio.h>
#include <tchar.h>
#include <wchar.h>

#include "main.h"

#define NELEMS(a)  (sizeof(a) / sizeof((a)[0]))

#if defined(UNICODE)
typedef wchar_t char_t;
#else
typedef char char_t;
#endif
const char_t* msgbox_caption = _T("WARNING");
const char_t* err_ofd = _T("Error open file dialog");

/** Prototypes **************************************************************/
static LRESULT WINAPI MainWndProc(HWND, UINT, WPARAM, LPARAM);
static void Main_OnEnteridle(HWND, UINT, HWND);
static void Main_OnCommand(HWND, int, HWND, UINT);
static void Main_OnDestroy(HWND);
static LRESULT WINAPI AboutDlgProc(HWND, UINT, WPARAM, LPARAM);

static void Open(HWND);
static void LoadMesh(const char_t*, const char_t* texture_path);

/** Global variables ********************************************************/

static HANDLE ghInstance;
void* videodata;
void* device;
void* video_driver;
void* scene_manager;
void* gui_environment;
void* scolor;
void* node;
void* position;
void* rotation;
void* scale;

//~ E_DRIVER_TYPE driver_type = EDT_SOFTWARE;
//~ E_DRIVER_TYPE driver_type = EDT_OPENGL;
E_DRIVER_TYPE driver_type = EDT_DIRECT3D9;

int PASCAL WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)
{
	INITCOMMONCONTROLSEX icc;
	WNDCLASS wc;
	HWND hwnd;
	MSG msg;
	void* param = SIrrlichtCreationParameters_ctor();

	ghInstance = hInstance;

	/* Initialize common controls. Also needed for MANIFEST's */
	icc.dwSize = sizeof(icc);
	icc.dwICC = ICC_WIN95_CLASSES /*|ICC_COOL_CLASSES|ICC_DATE_CLASSES|ICC_PAGESCROLLER_CLASS|ICC_USEREX_CLASSES|... */;
	InitCommonControlsEx(&icc);


	/* Register the main window class */
	wc.lpszClassName = _T("viewerClass");
	wc.lpfnWndProc = MainWndProc;
	wc.style = CS_OWNDC|CS_VREDRAW|CS_HREDRAW;
	wc.hInstance = ghInstance;
	wc.hIcon = LoadIcon(ghInstance, MAKEINTRESOURCE(IDR_ICO_MAIN));
	wc.hCursor = LoadCursor(NULL, IDC_ARROW);
	wc.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);
	wc.lpszMenuName = MAKEINTRESOURCE(IDR_MNU_MAIN);
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;
	if (!RegisterClass(&wc))
		return 1;

	/* Create the main window */
	hwnd = CreateWindowEx(WS_EX_CONTROLPARENT, wc.lpszClassName, _T("viewer"), WS_OVERLAPPEDWINDOW, 0, 0, CW_USEDEFAULT, CW_USEDEFAULT, NULL, NULL, ghInstance, NULL);
	if (!hwnd)
		return 1;

//===========================
	videodata = SExposedVideoData_ctor2(hwnd);
	SIrrlichtCreationParameters_set_DeviceType(param, EIDT_WIN32);
	SIrrlichtCreationParameters_set_DriverType(param, driver_type);
	device = IrrlichtDevice_createDeviceEx(param);
	if (device)
	{
		scolor = SColor_ctor2(255, 100, 100, 140);
		scene_manager = IrrlichtDevice_getSceneManager(device);
		video_driver = IrrlichtDevice_getVideoDriver(device);
		SetParent(IVideoDriver_GetHandle(video_driver), hwnd);
		if (driver_type == EDT_OPENGL)
		{
			HDC HDc = GetDC(hwnd);
			PIXELFORMATDESCRIPTOR pfd = {0};
			pfd.nSize = sizeof(PIXELFORMATDESCRIPTOR);
			int pf = GetPixelFormat(HDc);
			DescribePixelFormat(HDc, pf, sizeof(PIXELFORMATDESCRIPTOR), &pfd);
			pfd.dwFlags |= PFD_DOUBLEBUFFER | PFD_SUPPORT_OPENGL | PFD_DRAW_TO_WINDOW;
			pfd.cDepthBits = 16;
			pf = ChoosePixelFormat(HDc, &pfd);
			SetPixelFormat(HDc, pf, &pfd);
			SExposedVideoData_set_OpenGLWin32_HDc(videodata, HDc);
			SExposedVideoData_set_OpenGLWin32_HRc(videodata, wglCreateContext(HDc));
			void* vd = IVideoDriver_getExposedVideoData(video_driver);
			wglShareLists((HGLRC)SExposedVideoData_get_OpenGLWin32_HRc(vd), (HGLRC)SExposedVideoData_get_OpenGLWin32_HRc(videodata));
		}
		position = vector3df_ctor2(0.0, 0.0, 0.0);
		rotation = vector3df_ctor2(0.0, 0.0, 0.0);
		scale = vector3df_ctor2(1.0, 1.0, 1.0);
		const char_t mesh_path[17] = _T("media/sydney.md2");
		const char_t texture_path[17] = _T("media/sydney.bmp");
		LoadMesh(mesh_path, texture_path);
		void* camera = ISceneManager_addCameraSceneNodeMaya(scene_manager);
		ICameraSceneNode_setTarget(camera, vector3df_ctor2(0.0, 10.0, 0.0));
	}
//===========================

	/* Show and paint the main window */
	ShowWindow(hwnd, nCmdShow);
	UpdateWindow(hwnd);

    /* Pump messages until we are done */
#if 0
	/* "Politically correct" code -- SEE MICROSOFT DOCUMENTATION */
	for (;;)
	{
		BOOL fRet = GetMessage(&msg, NULL, 0, 0);
		if (fRet == -1)  /* Error */
		{
			/* TODO: handle the error from GetMessage() */
			__debugbreak();
			return -1;
		}
		else if (fRet == 0)  /* WM_QUIT */
		{
			break;
		}
		else  /* Not error or WM_QUIT */
		{
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}

		ITimer_tick(IrrlichtDevice_getTimer(device));
		if (IVideoDriver_beginScene(video_driver, true, true, scolor, videodata, NULL))
		{
			ISceneManager_drawAll(scene_manager);
			IVideoDriver_endScene(video_driver);
		}
	}
#else
	/* "Commonly seen" code */
	while (GetMessage(&msg, NULL, 0, 0))
	{
		TranslateMessage(&msg);
		DispatchMessage(&msg);

		ITimer_tick(IrrlichtDevice_getTimer(device));
		if (IVideoDriver_beginScene(video_driver, true, true, scolor, videodata, NULL))
		{
			ISceneManager_drawAll(scene_manager);
			IVideoDriver_endScene(video_driver);
		}
	}
#endif

    return msg.wParam;
}

static LRESULT CALLBACK MainWndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
	switch (msg)
	{
		HANDLE_MSG(hwnd, WM_COMMAND, Main_OnCommand);
		HANDLE_MSG(hwnd, WM_DESTROY, Main_OnDestroy);
		HANDLE_MSG(hwnd, WM_ENTERIDLE, Main_OnEnteridle);
		default:
			return DefWindowProc(hwnd, msg, wParam, lParam);
	}
}

static void Main_OnEnteridle(HWND hwnd, UINT source, HWND hwnd_source)
{
	if (device)
	{
		IrrlichtDevice_yield(device);
	}
}

static void LoadMesh(const char_t* mesh_path, const char_t* texture_path)
{
	if(video_driver && scene_manager)
	{
		void* i_animated_mesh = ISceneManager_getMesh(scene_manager, mesh_path);
		if(i_animated_mesh)
		{
			if(node)
				ISceneNode_remove(node);
			node = ISceneManager_addAnimatedMeshSceneNode(scene_manager, i_animated_mesh, NULL, -1, position, rotation, scale, false);
			if(node)
			{
				ISceneNode_setMaterialFlag(node, EMF_LIGHTING, false);
				IAnimatedMeshSceneNode_setMD2Animation1(node, EMAT_STAND);
				void* texture = IVideoDriver_getTexture1(video_driver, texture_path);
				ISceneNode_setMaterialTexture(node, 0, texture);
			}
		}
	}
}

static void Open(HWND hwnd)
{
	OPENFILENAME ofn, ofn2;
	char_t szFile[MAX_PATH], szFile2[MAX_PATH];
	char_t* szFilter = _T("All\0*.*\0Text\0*.TXT\0");
	// Initialize OPENFILENAME
	memset(&ofn, 0, sizeof(ofn));
	ofn.lStructSize = sizeof(OPENFILENAME);
	ofn.hwndOwner = hwnd;
	ofn.hInstance = ghInstance;
	ofn.lpstrFile = szFile;
	ofn.nMaxFile = MAX_PATH;
	ofn.lpstrFilter = szFilter;
	ofn.nFilterIndex = 1;
	ofn.lpstrFileTitle = NULL;
	ofn.nMaxFileTitle = MAX_PATH;
	ofn.lpstrInitialDir = NULL;
	ofn.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;
	memset(&ofn2, 0, sizeof(ofn2));
	ofn2.lStructSize = sizeof(OPENFILENAME);
	ofn2.hwndOwner = hwnd;
	ofn2.hInstance = ghInstance;
	ofn2.lpstrFile = szFile2;
	ofn2.nMaxFile = MAX_PATH;
	ofn2.lpstrFilter = szFilter;
	ofn2.nFilterIndex = 1;
	ofn2.lpstrFileTitle = NULL;
	ofn2.nMaxFileTitle = MAX_PATH;
	ofn2.lpstrInitialDir = NULL;
	ofn2.Flags = OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;
	// Display the Open dialog box.
	if (GetOpenFileName(&ofn))
	{
		if (GetOpenFileName(&ofn2))
			LoadMesh(ofn.lpstrFile, ofn2.lpstrFile);
	}
}

static void Main_OnCommand(HWND hwnd, int id, HWND hwndCtl, UINT codeNotify)
{
	switch (id)
	{
		case IDM_ABOUT:
			DialogBox(ghInstance, MAKEINTRESOURCE(DLG_ABOUT), hwnd, (DLGPROC)AboutDlgProc);
			break;
		case IDM_OPEN:
			Open(hwnd);
			break;
		default:
			break;
	}
}

static void Main_OnDestroy(HWND hwnd)
{
    PostQuitMessage(0);
	if (device)
	{
		IrrlichtDevice_closeDevice(device);
	}
}

static LRESULT CALLBACK AboutDlgProc(HWND hDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	switch (uMsg)
	{
		case WM_INITDIALOG:
			return TRUE;
		case WM_COMMAND:
			switch (wParam)
			{
				case IDOK:
				case IDCANCEL:
					EndDialog(hDlg, TRUE);
					return TRUE;
			}
			break;
	}
	return FALSE;
}

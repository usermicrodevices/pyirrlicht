// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

// for __stdcall Irrlicht.lib must be builded with _STDCALL_SUPPORTED flag

//#define _IRR_STATIC_LIB_

//#define _COMPILE_WITH_2DTTFONT_

//#define _COMPILE_WITH_3D_TEXT_

//#define _COMPILE_WITH_GRID_SCENE_NODE_

//#define _COMPILE_WITH_GUI_FILE_SELECTOR_

//#define _COMPILE_WITH_AGG_

//#define _COMPILE_WITH_IRR_SVG_AGG_

//#define _COMPILE_WITH_IRR_SVG_CAIRO_

//#define _COMPILE_WITH_CHAR_CONVERSION_FUNCTIONS_//usefull for Blitz3D wrapper

//#define _COMPILE_WITH_STREAM_FUNCTIONS_

#ifdef _MSC_VER
#define DEBUG_EVENTS
#define IRRLICHT_C_API __declspec(dllexport)
#else
#define IRRLICHT_C_API IRRLICHT_API
#endif

#include <ctime>
#include <iostream>
#include <random>
#include <chrono>

#include "irrlicht.h"
using namespace irr;
using namespace core;
using namespace gui;
using namespace io;
using namespace scene;
using namespace video;
using namespace quake3;
//#ifdef _IRR_IMPROVE_UNICODE
//using namespace unicode;
//#endif

#ifndef _MSC_VER
int _wtoi(const wchar_t* token)
{
	char* dest = 0;
	if(wcstombs(dest, token, sizeof(token)))
		return atoi(dest);
	return 0;
}
double _wtof(wchar_t* token)
{
	char* dest = 0;
	if(wcstombs(dest, token, sizeof(token)))
		return atof(dest);
	return 0;
}
double _wtof(const wchar_t* token)
{
	char* dest = 0;
	if(wcstombs(dest, token, sizeof(token)))
		return atof(dest);
	return 0;
}
#endif

#include "exception.h"

#include "_aabbox3d.h"
#include "_array.h"

#ifdef _COMPILE_WITH_GRID_SCENE_NODE_
#include "_CGridSceneNode.h"
#endif

#ifdef _COMPILE_WITH_GUI_FILE_SELECTOR_
#include "_CGUIFileSelector.h"
#endif

#include "_CDynamicMeshBuffer.h"
#include "_CMatrix4.h"
#include "_dimension2d.h"
#include "_line3d.h"
#include "_IAttributeExchangingObject.h"
#include "_IAttributes.h"
#include "_IAnimatedMesh.h"
#include "_IAnimatedMeshMD2.h"
#include "_IAnimatedMeshMD3.h"
#include "_IAnimatedMeshSceneNode.h"
#include "_IBillboardSceneNode.h"
#include "_IBillboardTextSceneNode.h"
#include "_IBoneSceneNode.h"
#include "_ICameraSceneNode.h"
#include "_ICursorControl.h"
#include "_IDummyTransformationSceneNode.h"
#include "_IDynamicMeshBuffer.h"
#include "_IEventReceiver.h"
#include "_IFileArchive.h"
#include "_IFileList.h"
#include "_IFileSystem.h"
#include "_IGUIButton.h"
#include "_IGUICheckBox.h"
#include "_IGUIColorSelectDialog.h"
#include "_IGUIComboBox.h"
#include "_IGUIContextMenu.h"
#include "_IGUIEditBox.h"
#include "_IGUIElement.h"
#include "_IGUIEnvironment.h"
#include "_IGUIFileOpenDialog.h"
#include "_IGUIFont.h"
#include "_IGUIFontBitmap.h"
#include "_IGUIImage.h"
#include "_IGUIImageList.h"
#include "_IGUIInOutFader.h"
#include "_IGUIListBox.h"
#include "_IGUIScrollBar.h"
#include "_IGUISkin.h"
#include "_IGUISpinBox.h"
#include "_IGUISpriteBank.h"
#include "_IGUIStaticText.h"
#include "_IGUITabControl.h"
#include "_IGUITable.h"
#include "_IGUIToolBar.h"
#include "_IGUITreeView.h"

#ifdef _COMPILE_WITH_2DTTFONT_
#include "_I2DTTFont.h"
#endif

#include "_IGUIWindow.h"
#include "_IGeometryCreator.h"
#include "_IImage.h"
#include "_IImageLoader.h"
#include "_IImageWriter.h"
#include "_IIndexBuffer.h"
#include "_ILightSceneNode.h"
#include "_ILogger.h"
#include "_IMesh.h"
#include "_IMeshBuffer.h"
#include "_IMeshCache.h"
#include "_IMeshManipulator.h"
#include "_IMetaTriangleSelector.h"
#include "_IMeshSceneNode.h"
#include "_IrrlichtDevice.h"
#include "_IOSOperator.h"
#include "_IParticleAffector.h"
#include "_IParticleAnimatedMeshSceneNodeEmitter.h"
#include "_IParticleAttractionAffector.h"
#include "_IParticleBoxEmitter.h"
#include "_IParticleCylinderEmitter.h"
#include "_IParticleEmitter.h"
#include "_IParticleFadeOutAffector.h"
#include "_IParticleGravityAffector.h"
#include "_IParticleMeshEmitter.h"
#include "_IParticleRingEmitter.h"
#include "_IParticleRotationAffector.h"
#include "_IParticleSphereEmitter.h"
#include "_IParticleSystemSceneNode.h"
#include "_IQ3LevelMesh.h"
#include "_IQ3Shader.h"
#include "_IReadFile.h"
#include "_IReferenceCounted.h"
#include "_ISceneCollisionManager.h"
#include "_ISceneManager.h"
#include "_ISceneNode.h"
#include "_ISceneNodeAnimator.h"
#include "_ISceneNodeAnimatorCollisionResponse.h"
#include "_ISceneNodeAnimatorFactory.h"
#include "_ISceneNodeFactory.h"
#include "_ITextSceneNode.h"
#include "_ITexture.h"
#include "_ITimer.h"
#include "_ITriangleSelector.h"
#include "_IVideoDriver.h"
#include "_IVideoModeList.h"
#include "_IVolumeLightSceneNode.h"
#include "_IWriteFile.h"
#include "_IXMLReader.h"
#include "_IXMLWriter.h"
#include "_plane3d.h"
#include "_quaternion.h"
#include "_rect.h"
#include "_S3DVertex.h"
#include "_SColor.h"
#include "_SExposedVideoData.h"
#include "_SIrrlichtCreationParameters.h"
#include "_SKeyMap.h"
#include "_SMaterial.h"
#include "_SMaterialLayer.h"
#include "_SMesh.h"
#include "_SParticle.h"
#include "_SViewFrustum.h"
#include "_triangle3d.h"
#include "_vector2d.h"
#include "_vector3d.h"

#include "MainLoop.h"

#ifdef _COMPILE_WITH_AGG_
#include "lib_agg.h"
#endif

#ifdef _COMPILE_WITH_3D_TEXT_
#include "text3d.h"
#endif

inline core::array<double> string_split_d(const wchar_t* str, u32 size = 8, const wchar_t* delimiter = L",");

class gradient
{
	stringw _id_;
	stringw _xlink_href_;
public:
	gradient(const wchar_t* id, const wchar_t* xlink_href)
	{
		_id_ = stringw(id);
		_xlink_href_ = stringw(xlink_href);
	}
	const wchar_t* id(){return _id_.c_str();}
	const wchar_t* xlink_href(){return _xlink_href_.c_str();}
};

#ifdef _COMPILE_WITH_IRR_SVG_AGG_
#include "irr_svg_agg.h"
#endif

#ifdef _COMPILE_WITH_IRR_SVG_CAIRO_
#include "irr_svg_cairo.h"
#endif

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API unsigned char _IRRLICHT_VERSION_MAJOR = IRRLICHT_VERSION_MAJOR;
IRRLICHT_C_API unsigned char _IRRLICHT_VERSION_MINOR = IRRLICHT_VERSION_MINOR;
IRRLICHT_C_API unsigned char _IRRLICHT_VERSION_REVISION = IRRLICHT_VERSION_REVISION;
IRRLICHT_C_API unsigned char _IRRLICHT_VERSION = IRRLICHT_VERSION_MAJOR*100 + IRRLICHT_VERSION_MINOR*10 + IRRLICHT_VERSION_REVISION;

#ifdef _COMPILE_WITH_3D_TEXT_
IRRLICHT_C_API bool BUILD_WITH_3D_TEXT = true;
#else
IRRLICHT_C_API bool BUILD_WITH_3D_TEXT = false;
#endif

#ifdef _COMPILE_WITH_GRID_SCENE_NODE_
IRRLICHT_C_API bool BUILD_WITH_GRID_SCENE_NODE = true;
#else
IRRLICHT_C_API bool BUILD_WITH_GRID_SCENE_NODE = false;
#endif

#ifdef _COMPILE_WITH_AGG_
IRRLICHT_C_API bool BUILD_WITH_AGG = true;
IRRLICHT_C_API void IVideoDriver_addAggSvgImageLoader(IVideoDriver* pointer)
{pointer->addExternalImageLoader(new agg_svg_loader(pointer));}
#else
IRRLICHT_C_API bool BUILD_WITH_AGG = false;
IRRLICHT_C_API void IVideoDriver_addAggSvgImageLoader(IVideoDriver* pointer){}
#endif

#ifdef _COMPILE_WITH_IRR_SVG_AGG_
IRRLICHT_C_API bool BUILD_WITH_IRR_SVG_AGG = true;
#else
IRRLICHT_C_API bool BUILD_WITH_IRR_SVG_AGG = false;
#endif

#ifdef _COMPILE_WITH_IRR_SVG_CAIRO_
IRRLICHT_C_API bool BUILD_WITH_IRR_SVG_CAIRO = true;
#else
IRRLICHT_C_API bool BUILD_WITH_IRR_SVG_CAIRO = false;
#endif

#ifdef _COMPILE_WITH_CHAR_CONVERSION_FUNCTIONS_
IRRLICHT_C_API bool BUILD_WITH_CHAR_CONVERSION_FUNCTIONS = true;
#else
IRRLICHT_C_API bool BUILD_WITH_CHAR_CONVERSION_FUNCTIONS = false;
#endif

#ifdef _COMPILE_WITH_STREAM_FUNCTIONS_
IRRLICHT_C_API bool BUILD_WITH_STREAM_FUNCTIONS = true;
#else
IRRLICHT_C_API bool BUILD_WITH_STREAM_FUNCTIONS = false;
#endif

#if defined(_IRR_WCHAR_FILESYSTEM)
	IRRLICHT_C_API bool IRR_WCHAR_FILESYSTEM = true;
#else
	IRRLICHT_C_API bool IRR_WCHAR_FILESYSTEM = false;
#endif

IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_ZIP = EFAT_ZIP;
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_GZIP = EFAT_GZIP;
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_FOLDER = EFAT_FOLDER;
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_PAK = EFAT_PAK;
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_TAR = EFAT_TAR;
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE _EFAT_UNKNOWN = EFAT_UNKNOWN;

#ifdef _IRR_IMPROVE_UNICODE
IRRLICHT_C_API bool IRR_IMPROVE_UNICODE = true;
#else
IRRLICHT_C_API bool IRR_IMPROVE_UNICODE = false;
#endif

#ifdef _IRR_USE_INPUT_METHOD
IRRLICHT_C_API bool IRR_USE_INPUT_METHOD = true;
#else
IRRLICHT_C_API bool IRR_USE_INPUT_METHOD = false;
#endif

#ifdef _COMPILE_WITH_GUI_FILE_SELECTOR_
IRRLICHT_C_API bool BUILD_WITH_GUI_FILE_SELECTOR = true;
#else
IRRLICHT_C_API bool BUILD_WITH_GUI_FILE_SELECTOR = false;
#endif

IRRLICHT_C_API IrrXMLReader* createIrrXMLReader1(const char* filename){return createIrrXMLReader(filename);}
IRRLICHT_C_API IrrXMLReader* createIrrXMLReader2(FILE* file){return createIrrXMLReader(file);}

IRRLICHT_C_API bool set_virtual_method(void* obj_pointer, bool(IRRCALLCONV* new_method)(const SEvent&), int method_index = 0)
{
#ifdef _MSC_VER
#include <Windows.h>
	LPDWORD* lpVPTR = (LPDWORD*)obj_pointer;
	MEMORY_BASIC_INFORMATION mbi;
	if(VirtualQuery((LPVOID)(lpVPTR), &mbi, sizeof(mbi)) != sizeof(mbi))
		return false;
	LPVOID lpAddress = mbi.BaseAddress;
#if defined(_WIN32)
	SIZE_T memory_region_size = 4;
#else if defined(_WIN64)
	SIZE_T memory_region_size = 8;
#endif
	PDWORD lpflOldProtect = new DWORD();
	void* result = 0;
	if(VirtualProtect(lpAddress, memory_region_size, PAGE_EXECUTE_READWRITE, lpflOldProtect))
	{
		result = memcpy((LPVOID)(lpVPTR + method_index), (LPVOID)&new_method, memory_region_size);
		delete lpflOldProtect;
		if(result)
			return true;
		else
			return false;
	}
	else
		return false;
#else
	return false;
#endif
}

IRRLICHT_C_API int tool_randrange(int rnd_min = 0, int rnd_max = RAND_MAX);

IRRLICHT_C_API ITexture* tool_texture_generator(IVideoDriver* driver, video::ECOLOR_FORMAT image_format = ECF_R8G8B8, const dimension2d<u32>& image_size = dimension2d<u32>(2, 2), const char* texture_name = "texture_01", u32 alpha_value = 128, u32 red1 = 0, u32 red2 = 255, u32 green1 = 0, u32 green2 = 255, u32 blue1 = 0, u32 blue2 = 255);

#ifdef _COMPILE_WITH_CHAR_CONVERSION_FUNCTIONS_

IRRLICHT_C_API const wchar_t* tool_char_to_wchar(const char* src_buf)
{
	wchar_t* dst_buf = 0;
	size_t src_size = strlen(src_buf) + 1;
	if (src_size > 1)
	{
		dst_buf = new wchar_t[src_size * sizeof(wchar_t)];
#ifdef _MSC_VER
		size_t NumOfCharConverted;
		errno_t res = mbstowcs_s(&NumOfCharConverted, dst_buf, src_size, src_buf, _TRUNCATE);
#else
		size_t res = mbstowcs(dst_buf, src_buf, MB_CUR_MAX);
#endif
	}
	return dst_buf;
}

#endif

#ifdef _COMPILE_WITH_STREAM_FUNCTIONS_

IRRLICHT_C_API FILE* tool_get_stdin(){return stdin;}
IRRLICHT_C_API FILE* tool_get_stdout(){return stdout;}
IRRLICHT_C_API FILE* tool_get_stderr(){return stderr;}

IRRLICHT_C_API FILE* tool_redirect_stdout_to_file(const char* file_name, const char* mode = "w")
{
	FILE *result_stream = 0;
	if (!strlen(mode))
		mode = "w";
	if( freopen_s(&result_stream, file_name, mode, stdout) != 0 )
		fprintf( stdout, "ERROR: tool_redirect_stdout_to_file\n" );
	return result_stream;
}

IRRLICHT_C_API FILE* tool_redirect_stderr_to_file(const char* file_name, const char* mode = "w")
{
	FILE *result_stream = 0;
	if (!strlen(mode))
		mode = "w";
	if( freopen_s(&result_stream, file_name, mode, stderr) != 0 )
		fprintf( stdout, "ERROR: tool_redirect_stderr_to_file\n" );
	return result_stream;
}

IRRLICHT_C_API int tool_close_stream(FILE* stream)
{
	if (stream)
		return fclose(stream);
	else
		return -2;
}

IRRLICHT_C_API int tool_close_streams(){return _fcloseall();}

#endif

IRRLICHT_C_API IMesh* tool_createEllipticalMesh(f32 radiusH, f32 radiusV, f32 Ylow, f32 Yhigh, f32 offset, u32 polyCountX, u32 polyCountY);

#ifdef __cplusplus
}
#endif

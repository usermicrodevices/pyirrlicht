// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#define _IRR_STATIC_LIB_

#define _COMPILE_WITH_2DTTFONT_

#define _COMPILE_WITH_GRID_SCENE_NODE_

#define _COMPILE_WITH_AGG_

#ifdef _MSC_VER
#define DEBUG_EVENTS
#define IRRLICHT_C_API __declspec(dllexport)
#else
#define IRRLICHT_C_API IRRLICHT_API
#endif

#include <ctime>

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

#include "exception.h"

#include "_aabbox3d.h"
#include "_array.h"

#ifdef _COMPILE_WITH_GRID_SCENE_NODE_
#include "_CGridSceneNode.h"
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

#ifdef __cplusplus
extern "C" {
#endif

#ifdef _COMPILE_WITH_AGG_
IRRLICHT_C_API void IVideoDriver_addAggSvgImageLoader(IVideoDriver* pointer)
{pointer->addExternalImageLoader(new agg_svg_loader(pointer));}
#else
IRRLICHT_C_API void IVideoDriver_addAggSvgImageLoader(IVideoDriver* pointer){}
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

IRRLICHT_C_API IrrXMLReader* createIrrXMLReader1(const char* filename){return createIrrXMLReader(filename);}
IRRLICHT_C_API IrrXMLReader* createIrrXMLReader2(FILE* file){return createIrrXMLReader(file);}
/*
IRRLICHT_C_API bool set_virtual_method(void* obj_pointer, void** new_method, int method_index = 0)
{
#ifdef _MSC_VER
#ifndef DEBUG
	size_t* vptr =  *(size_t**)obj_pointer;
	__asm{mov ecx, obj_pointer}
	vptr[method_index] = (size_t)new_method;
	//(*(size_t**)obj_pointer)[method_index] = (size_t)new_method;
	return true;
#else
	printf("set_virtual_method only for RELEASE mode, current is DEBUG!");
	return false;
#endif
#else
	obj_pointer->_vptr[method_index] = new_method;
	return true;
#endif
}
*/


//IRRLICHT_C_API bool set_virtual_method(void* obj_pointer, const void* new_method, int method_index = 0)
IRRLICHT_C_API bool set_virtual_method(void* obj_pointer, bool(IRRCALLCONV* new_method)(const SEvent&), int method_index = 0)
{
#ifdef _MSC_VER
#include <Windows.h>
	LPDWORD* lpVPTR = (LPDWORD*)obj_pointer;
	//lpVPTR = (LPDWORD*)*lpVPTR;
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
		//DWORD dw = reinterpret_cast<DWORD>(new_method);
		//result = memcpy((LPVOID)(lpVPTR + method_index), (LPVOID)&dw, memory_region_size);
		result = memcpy((LPVOID)(lpVPTR + method_index), (LPVOID)&new_method, memory_region_size);
		//result = memmove((LPVOID)(lpVPTR + method_index), (LPVOID)&new_method, memory_region_size);
		delete lpflOldProtect;
		//&(((IEventReceiver*)obj_pointer)->OnEvent) = new_method;
		//printf("++++ lpVPTR IS %d\n", lpVPTR);
		printf("++++ MEMCPY RESULT IS %d\n", result);
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

IRRLICHT_C_API void delete_pointer(void* pointer)
{
	if (pointer)
		delete pointer;
}

IRRLICHT_C_API void delete_struct_pointer(void* pointer)
{
	if (pointer)
		delete[] pointer;
}

int randrange(int rnd_min = 0, int rnd_max = RAND_MAX)
{
	return rnd_min+int((rnd_max-rnd_min+1)*rand()/(RAND_MAX + 1.0));
}

IRRLICHT_C_API int tool_randrange(int rnd_min = 0, int rnd_max = RAND_MAX)
{
	return randrange(rnd_min, rnd_max);
}

IRRLICHT_C_API ITexture* tool_texture_generator(IVideoDriver* driver, video::ECOLOR_FORMAT image_format = ECF_R8G8B8, const dimension2d<u32>& image_size = dimension2d<u32>(2, 2), char* texture_name = "texture_01", u32 alpha_value = 128, u32 red1 = 0, u32 red2 = 255, u32 green1 = 0, u32 green2 = 255, u32 blue1 = 0, u32 blue2 = 255)
{
	u32 row, column;
	IImage* image = driver->createImage(image_format, image_size);
	int alpha = 0;
	bool blend = false;
	video::ECOLOR_FORMAT color_format = image->getColorFormat();
	if (color_format == ECF_A1R5G5B5 || color_format == ECF_A8R8G8B8 || color_format == ECF_A16B16G16R16F || color_format == ECF_A32B32G32R32F)
	{
		alpha = alpha_value;
		blend = true;
	}
	srand((unsigned)time(NULL));
	for (row = 0; row < image_size.Height; row++)
	{
		for (column = 0; column < image_size.Width; column++)
			image->setPixel(row, column, SColor(alpha, randrange(red1, red2), randrange(green1, green2), randrange(blue1, blue2)), blend);
	}
	return driver->addTexture(texture_name, image);
}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//struct SOverrideMaterial
IRRLICHT_C_API SOverrideMaterial* SOverrideMaterial_ctor(){return new SOverrideMaterial();}
IRRLICHT_C_API void SOverrideMaterial_delete(SOverrideMaterial* pointer){if(pointer)delete pointer;}
IRRLICHT_C_API void SOverrideMaterial_apply(SOverrideMaterial* pointer, SMaterial* material){pointer->apply(*material);}
IRRLICHT_C_API SMaterial* SOverrideMaterial_get_Material(SOverrideMaterial* pointer){return &pointer->Material;}
IRRLICHT_C_API void SOverrideMaterial_set_Material(SOverrideMaterial* pointer, SMaterial* value){pointer->Material = *value;}
IRRLICHT_C_API u32 SOverrideMaterial_get_EnableFlags(SOverrideMaterial* pointer){return pointer->EnableFlags;}
IRRLICHT_C_API void SOverrideMaterial_set_EnableFlags(SOverrideMaterial* pointer, u32 value){pointer->EnableFlags = value;}
IRRLICHT_C_API u16 SOverrideMaterial_get_EnablePasses(SOverrideMaterial* pointer){return pointer->EnablePasses;}
IRRLICHT_C_API void SOverrideMaterial_set_EnablePasses(SOverrideMaterial* pointer, u16 value){pointer->EnablePasses = value;}
IRRLICHT_C_API bool SOverrideMaterial_get_Enabled(SOverrideMaterial* pointer){return pointer->Enabled;}
IRRLICHT_C_API void SOverrideMaterial_set_Enabled(SOverrideMaterial* pointer, bool value){pointer->Enabled = value;}

//struct IRenderTarget
#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API IRenderTarget* IRenderTarget_ctor1(ITexture* texture, E_COLOR_PLANE colorMask = ECP_ALL, E_BLEND_FACTOR blendFuncSrc = EBF_ONE, E_BLEND_FACTOR blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, bool blendEnable = false)
{return new IRenderTarget(texture, colorMask, blendFuncSrc, blendFuncDst, blendEnable);}
#else
IRRLICHT_C_API IRenderTarget* IRenderTarget_ctor1(ITexture* texture, E_COLOR_PLANE colorMask = ECP_ALL, E_BLEND_FACTOR blendFuncSrc = EBF_ONE, E_BLEND_FACTOR blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, E_BLEND_OPERATION blendOp = EBO_NONE)
{return new IRenderTarget(texture, colorMask, blendFuncSrc, blendFuncDst, blendOp);}
#endif

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API IRenderTarget* IRenderTarget_ctor2(E_RENDER_TARGET target, E_COLOR_PLANE colorMask = ECP_ALL, E_BLEND_FACTOR blendFuncSrc = EBF_ONE, E_BLEND_FACTOR blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, bool blendEnable = false)
{return new IRenderTarget(target, colorMask, blendFuncSrc, blendFuncDst, blendEnable);}
#else
IRRLICHT_C_API IRenderTarget* IRenderTarget_ctor2(E_RENDER_TARGET target, E_COLOR_PLANE colorMask = ECP_ALL, E_BLEND_FACTOR blendFuncSrc = EBF_ONE, E_BLEND_FACTOR blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, E_BLEND_OPERATION blendOp = EBO_NONE)
{return new IRenderTarget(target, colorMask, blendFuncSrc, blendFuncDst, blendOp);}
#endif

IRRLICHT_C_API void IRenderTarget_delete(IRenderTarget* pointer){if(pointer)delete pointer;}

IRRLICHT_C_API ITexture* IRenderTarget_get_RenderTexture(IRenderTarget* pointer){return pointer->RenderTexture;}
IRRLICHT_C_API void IRenderTarget_set_RenderTexture(IRenderTarget* pointer, ITexture* value){pointer->RenderTexture = value;}
IRRLICHT_C_API E_RENDER_TARGET IRenderTarget_get_TargetType(IRenderTarget* pointer){return pointer->TargetType;}
IRRLICHT_C_API void IRenderTarget_set_TargetType(IRenderTarget* pointer, E_RENDER_TARGET value){pointer->TargetType = value;}
IRRLICHT_C_API E_COLOR_PLANE IRenderTarget_get_ColorMask(IRenderTarget* pointer){return pointer->ColorMask;}
IRRLICHT_C_API void IRenderTarget_set_ColorMask(IRenderTarget* pointer, E_COLOR_PLANE value){pointer->ColorMask = value;}
IRRLICHT_C_API E_BLEND_FACTOR IRenderTarget_get_BlendFuncSrc(IRenderTarget* pointer){return pointer->BlendFuncSrc;}
IRRLICHT_C_API void IRenderTarget_set_BlendFuncSrc(IRenderTarget* pointer, E_BLEND_FACTOR value){pointer->BlendFuncSrc = value;}
IRRLICHT_C_API E_BLEND_FACTOR IRenderTarget_get_BlendFuncDst(IRenderTarget* pointer){return pointer->BlendFuncDst;}
IRRLICHT_C_API void IRenderTarget_set_BlendFuncDst(IRenderTarget* pointer, E_BLEND_FACTOR value){pointer->BlendFuncDst = value;}
#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR < 8)
IRRLICHT_C_API bool IRenderTarget_get_BlendEnable(IRenderTarget* pointer){return pointer->BlendEnable;}
IRRLICHT_C_API void IRenderTarget_set_BlendEnable(IRenderTarget* pointer, bool value){pointer->BlendEnable = value;}
#else
IRRLICHT_C_API E_BLEND_OPERATION IRenderTarget_get_BlendOp(IRenderTarget* pointer){return pointer->BlendOp;}
IRRLICHT_C_API void IRenderTarget_set_BlendOp(IRenderTarget* pointer, E_BLEND_OPERATION value){pointer->BlendOp = value;}
#endif


//class IVideoDriver : public virtual IReferenceCounted
//#if (IRRLICHT_VERSION_MAJOR == 1) && (IRRLICHT_VERSION_MINOR > 6)
IRRLICHT_C_API bool IVideoDriver_beginScene(IVideoDriver* pointer, bool backBuffer=true, bool zBuffer=true, const SColor& color=SColor(255,0,0,0), const SExposedVideoData& videoData=SExposedVideoData(), core::rect<s32>* sourceRect=0)
{return pointer->beginScene(backBuffer, zBuffer, color, videoData, sourceRect);}
IRRLICHT_C_API bool IVideoDriver_beginSceneDefault(IVideoDriver* pointer, bool backBuffer=true, bool zBuffer=true, const SColor& color=SColor(255,0,0,0))
{return pointer->beginScene(backBuffer, zBuffer, color, SExposedVideoData(), 0);}
//#else
//IRRLICHT_C_API bool IVideoDriver_beginScene(IVideoDriver* pointer, bool backBuffer=true, bool zBuffer=true, const SColor& color=SColor(255,0,0,0), void* windowId=0, core::rect<s32>* sourceRect=0)
//{return pointer->beginScene(backBuffer, zBuffer, color, videoData, sourceRect);}
//IRRLICHT_C_API bool IVideoDriver_beginSceneDefault(IVideoDriver* pointer, bool backBuffer=true, bool zBuffer=true, const SColor& color=SColor(255,0,0,0))
//{return pointer->beginScene(backBuffer, zBuffer, color, 0, 0);}
//#endif

IRRLICHT_C_API bool IVideoDriver_endScene(IVideoDriver* pointer)
{return pointer->endScene();}
IRRLICHT_C_API bool IVideoDriver_queryFeature(IVideoDriver* pointer, E_VIDEO_DRIVER_FEATURE feature)
{return pointer->queryFeature(feature);}
IRRLICHT_C_API void IVideoDriver_disableFeature(IVideoDriver* pointer, E_VIDEO_DRIVER_FEATURE feature, bool flag=true)
{pointer->disableFeature(feature, flag);}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR > 7)
IRRLICHT_C_API const io::IAttributes* IVideoDriver_getDriverAttributes(IVideoDriver* pointer)
{return &pointer->getDriverAttributes();}
#endif

IRRLICHT_C_API bool IVideoDriver_checkDriverReset(IVideoDriver* pointer)
{return pointer->checkDriverReset();}
IRRLICHT_C_API void IVideoDriver_setTransform(IVideoDriver* pointer, E_TRANSFORMATION_STATE state, const core::matrix4& mat)
{pointer->setTransform(state, mat);}
IRRLICHT_C_API const core::matrix4& IVideoDriver_getTransform(IVideoDriver* pointer, E_TRANSFORMATION_STATE state)
{return pointer->getTransform(state);}
IRRLICHT_C_API u32 IVideoDriver_getImageLoaderCount(IVideoDriver* pointer)
{return pointer->getImageLoaderCount();}
IRRLICHT_C_API IImageLoader* IVideoDriver_getImageLoader(IVideoDriver* pointer, u32 n)
{return pointer->getImageLoader(n);}
IRRLICHT_C_API u32 IVideoDriver_getImageWriterCount(IVideoDriver* pointer)
{return pointer->getImageWriterCount();}
IRRLICHT_C_API IImageWriter* IVideoDriver_getImageWriter(IVideoDriver* pointer, u32 n)
{return pointer->getImageWriter(n);}
IRRLICHT_C_API void IVideoDriver_setMaterial(IVideoDriver* pointer, const SMaterial& material)
{pointer->setMaterial(material);}
IRRLICHT_C_API ITexture* IVideoDriver_getTexture1(IVideoDriver* pointer, const fschar_t* filename)
{return pointer->getTexture(io::path(filename));}
IRRLICHT_C_API ITexture* IVideoDriver_getTexture2(IVideoDriver* pointer, io::IReadFile* file)
{return pointer->getTexture(file);}
IRRLICHT_C_API ITexture* IVideoDriver_getTextureByIndex(IVideoDriver* pointer, u32 index)
{return pointer->getTextureByIndex(index);}
IRRLICHT_C_API u32 IVideoDriver_getTextureCount(IVideoDriver* pointer)
{return pointer->getTextureCount();}
IRRLICHT_C_API void IVideoDriver_renameTexture(IVideoDriver* pointer, ITexture* texture, const fschar_t* newName)
{pointer->renameTexture(texture, newName);}
IRRLICHT_C_API ITexture* IVideoDriver_addTexture1(IVideoDriver* pointer, const core::dimension2d<u32>& size, const fschar_t* name, ECOLOR_FORMAT format = ECF_A8R8G8B8)
{return pointer->addTexture(size, name, format);}
IRRLICHT_C_API ITexture* IVideoDriver_addTexture2(IVideoDriver* pointer, const fschar_t* name, IImage* image, void* mipmapData=0)
{return pointer->addTexture(name, image, mipmapData);}
#if defined(_IRR_WCHAR_FILESYSTEM)
IRRLICHT_C_API ITexture* IVideoDriver_addRenderTargetTexture(IVideoDriver* pointer, const core::dimension2d<u32>& size, const fschar_t* name = L"rt", const ECOLOR_FORMAT format = ECF_UNKNOWN)
#else
IRRLICHT_C_API ITexture* IVideoDriver_addRenderTargetTexture(IVideoDriver* pointer, const core::dimension2d<u32>& size, const fschar_t* name = "rt", const ECOLOR_FORMAT format = ECF_UNKNOWN)
#endif
{return pointer->addRenderTargetTexture(size, name, format);}
IRRLICHT_C_API void IVideoDriver_removeTexture(IVideoDriver* pointer, ITexture* texture)
{pointer->removeTexture(texture);}
IRRLICHT_C_API void IVideoDriver_removeAllTextures(IVideoDriver* pointer)
{pointer->removeAllTextures();}
IRRLICHT_C_API void IVideoDriver_removeHardwareBuffer(IVideoDriver* pointer, const scene::IMeshBuffer* mb)
{pointer->removeHardwareBuffer(mb);}
IRRLICHT_C_API void IVideoDriver_removeAllHardwareBuffers(IVideoDriver* pointer)
{pointer->removeAllHardwareBuffers();}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR > 7)
IRRLICHT_C_API void IVideoDriver_addOcclusionQuery(IVideoDriver* pointer, scene::ISceneNode* node, const scene::IMesh* mesh = 0){pointer->addOcclusionQuery(node, mesh);}
IRRLICHT_C_API void IVideoDriver_removeOcclusionQuery(IVideoDriver* pointer, scene::ISceneNode* node){pointer->removeOcclusionQuery(node);}
IRRLICHT_C_API void IVideoDriver_removeAllOcclusionQueries(IVideoDriver* pointer){pointer->removeAllOcclusionQueries();}
IRRLICHT_C_API void IVideoDriver_runOcclusionQuery(IVideoDriver* pointer, scene::ISceneNode* node, bool visible = false){pointer->runOcclusionQuery(node, visible);}
IRRLICHT_C_API void IVideoDriver_runAllOcclusionQueries(IVideoDriver* pointer, bool visible = false){pointer->runAllOcclusionQueries(visible);}
IRRLICHT_C_API void IVideoDriver_updateOcclusionQuery(IVideoDriver* pointer, scene::ISceneNode* node, bool block = true){pointer->updateOcclusionQuery(node, block);}
IRRLICHT_C_API void IVideoDriver_updateAllOcclusionQueries(IVideoDriver* pointer, bool block = true){pointer->updateAllOcclusionQueries(block);}
IRRLICHT_C_API u32 IVideoDriver_getOcclusionQueryResult(IVideoDriver* pointer, scene::ISceneNode* node){return pointer->getOcclusionQueryResult(node);}
#endif

IRRLICHT_C_API void IVideoDriver_makeColorKeyTexture1(IVideoDriver* pointer, video::ITexture* texture, const SColor& color, bool zeroTexels = false)
{pointer->makeColorKeyTexture(texture, color, zeroTexels);}
IRRLICHT_C_API void IVideoDriver_makeColorKeyTexture2(IVideoDriver* pointer, video::ITexture* texture, const core::position2d<s32>& colorKeyPixelPos, bool zeroTexels = false)
{
	try
	{
		pointer->makeColorKeyTexture(texture, colorKeyPixelPos, zeroTexels);
	}
	catch (const std::exception& e)
	{
		std::cout << e.what() << "\n";
	}
}
IRRLICHT_C_API void IVideoDriver_makeNormalMapTexture(IVideoDriver* pointer, video::ITexture* texture, f32 amplitude=1.0f)
{pointer->makeNormalMapTexture(texture, amplitude);}
IRRLICHT_C_API bool IVideoDriver_setRenderTarget1(IVideoDriver* pointer, video::ITexture* texture, bool clearBackBuffer=true, bool clearZBuffer = true, const SColor& color = SColor(0,0,0,0))
{return pointer->setRenderTarget(texture, clearBackBuffer, clearZBuffer, color);}
IRRLICHT_C_API bool IVideoDriver_setRenderTarget2(IVideoDriver* pointer, E_RENDER_TARGET target, bool clearTarget=true, bool clearZBuffer=true, const SColor& color = SColor(0,0,0,0))
{return pointer->setRenderTarget(target, clearTarget, clearZBuffer, color);}
IRRLICHT_C_API bool IVideoDriver_setRenderTarget3(IVideoDriver* pointer, const core::array<video::IRenderTarget>& target, bool clearTarget=true, bool clearZBuffer=true, const SColor& color = SColor(0,0,0,0))
{return pointer->setRenderTarget(target, clearTarget, clearZBuffer, color);}
IRRLICHT_C_API void IVideoDriver_setViewPort(IVideoDriver* pointer, const core::rect<s32>& area)
{pointer->setViewPort(area);}
IRRLICHT_C_API const core::rect<s32>& IVideoDriver_getViewPort(IVideoDriver* pointer)
{return pointer->getViewPort();}
IRRLICHT_C_API void IVideoDriver_drawVertexPrimitiveList(IVideoDriver* pointer, const void* vertices, u32 vertexCount, const void* indexList, u32 primCount, E_VERTEX_TYPE vType=EVT_STANDARD, scene::E_PRIMITIVE_TYPE pType=scene::EPT_TRIANGLES, E_INDEX_TYPE iType=EIT_16BIT)
{pointer->drawVertexPrimitiveList(vertices, vertexCount, indexList, primCount, vType, pType, iType);}
IRRLICHT_C_API void IVideoDriver_draw2DVertexPrimitiveList(IVideoDriver* pointer, const void* vertices, u32 vertexCount, const void* indexList, u32 primCount, E_VERTEX_TYPE vType=EVT_STANDARD, scene::E_PRIMITIVE_TYPE pType=scene::EPT_TRIANGLES, E_INDEX_TYPE iType=EIT_16BIT)
{pointer->draw2DVertexPrimitiveList(vertices, vertexCount, indexList, primCount, vType, pType, iType);}
IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleList1(IVideoDriver* pointer, const S3DVertex* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
{pointer->drawIndexedTriangleList(vertices, vertexCount, indexList, triangleCount);}
IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleList2(IVideoDriver* pointer, const S3DVertex2TCoords* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
{pointer->drawIndexedTriangleList(vertices, vertexCount, indexList, triangleCount);}
IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleList3(IVideoDriver* pointer, const S3DVertexTangents* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
{pointer->drawIndexedTriangleList(vertices, vertexCount, indexList, triangleCount);}
IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleFan(IVideoDriver* pointer, const S3DVertex* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
{pointer->drawIndexedTriangleFan(vertices, vertexCount, indexList, triangleCount);}
//IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleFan1(IVideoDriver* pointer, const S3DVertex* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
//{pointer->drawIndexedTriangleFan(vertices, vertexCount, indexList, triangleCount);}
//IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleFan2(IVideoDriver* pointer, const S3DVertex2TCoords* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
//{pointer->drawIndexedTriangleFan(vertices, vertexCount, indexList, triangleCount);}
//IRRLICHT_C_API void IVideoDriver_drawIndexedTriangleFan3(IVideoDriver* pointer, const S3DVertexTangents* vertices, u32 vertexCount, const u16* indexList, u32 triangleCount)
//{pointer->drawIndexedTriangleFan(vertices, vertexCount, indexList, triangleCount);}
IRRLICHT_C_API void IVideoDriver_draw3DLine(IVideoDriver* pointer, const core::vector3df& start, const core::vector3df& end, const SColor& color = SColor(255,255,255,255))
{pointer->draw3DLine(start, end, color);}
IRRLICHT_C_API void IVideoDriver_draw3DTriangle(IVideoDriver* pointer, const core::triangle3df& triangle, const SColor& color = SColor(255,255,255,255))
{pointer->draw3DTriangle(triangle, color);}
IRRLICHT_C_API void IVideoDriver_draw3DBox(IVideoDriver* pointer, const core::aabbox3d<f32>& box, const SColor& color = SColor(255,255,255,255))
{pointer->draw3DBox(box, color);}

IRRLICHT_C_API void IVideoDriver_draw2DImage1(IVideoDriver* pointer, const video::ITexture* texture, const core::position2d<s32>* destPos)
{pointer->draw2DImage(texture, *destPos);}
IRRLICHT_C_API void IVideoDriver_draw2DImage2(IVideoDriver* pointer, const video::ITexture* texture, const core::position2d<s32>* destPos, const core::rect<s32>* sourceRect, const core::rect<s32>* clipRect = 0, const SColor& color = SColor(255,255,255,255), bool useAlphaChannelOfTexture = false)
{pointer->draw2DImage(texture, *destPos, *sourceRect, clipRect, color, useAlphaChannelOfTexture);}
IRRLICHT_C_API void IVideoDriver_draw2DImage3(IVideoDriver* pointer, const video::ITexture* texture, const core::rect<s32>* destRect, const core::rect<s32>* sourceRect, const core::rect<s32>* clipRect = 0, const video::SColor* const colors = 0, bool useAlphaChannelOfTexture = false)
{pointer->draw2DImage(texture, *destRect, *sourceRect, clipRect, colors, useAlphaChannelOfTexture);}

IRRLICHT_C_API void IVideoDriver_draw2DImageBatch1(IVideoDriver* pointer, const video::ITexture* texture, const core::position2d<s32>* pos, const core::array< core::rect<s32> >* sourceRects, const core::array<s32>* indices, s32 kerningWidth = 0, const core::rect<s32>* clipRect = 0, const SColor& color = SColor(255,255,255,255), bool useAlphaChannelOfTexture = false)
{pointer->draw2DImageBatch(texture, *pos, *sourceRects, *indices, kerningWidth, clipRect, color, useAlphaChannelOfTexture);}
IRRLICHT_C_API void IVideoDriver_draw2DImageBatch2(IVideoDriver* pointer, const video::ITexture* texture, const core::array< core::position2d<s32> >* positions, const core::array< core::rect<s32> >* sourceRects, const core::rect<s32>* clipRect = 0, const SColor& color = SColor(255,255,255,255), bool useAlphaChannelOfTexture = false)
{pointer->draw2DImageBatch(texture, *positions, *sourceRects, clipRect, color, useAlphaChannelOfTexture);}

IRRLICHT_C_API void IVideoDriver_draw2DRectangle1(IVideoDriver* pointer, SColor* color, const core::rect<s32>* pos, const core::rect<s32>* clip =0)
{pointer->draw2DRectangle(*color, *pos, clip);}
IRRLICHT_C_API void IVideoDriver_draw2DRectangle2(IVideoDriver* pointer, const core::rect<s32>* pos, const SColor* colorLeftUp, const SColor* colorRightUp, const SColor* colorLeftDown, const SColor* colorRightDown, const core::rect<s32>* clip =0)
{pointer->draw2DRectangle(*pos, *colorLeftUp, *colorRightUp, *colorLeftDown, *colorRightDown, clip);}

IRRLICHT_C_API void IVideoDriver_draw2DRectangleOutline(IVideoDriver* pointer, const core::recti* pos, const SColor& color = SColor(255,255,255,255))
{pointer->draw2DRectangleOutline(*pos, color);}
IRRLICHT_C_API void IVideoDriver_draw2DLine(IVideoDriver* pointer, const core::position2d<s32>* start, const core::position2d<s32>* end, const SColor& color = SColor(255,255,255,255))
{pointer->draw2DLine(*start, *end, color);}
IRRLICHT_C_API void IVideoDriver_drawPixel(IVideoDriver* pointer, u32 x, u32 y, const SColor* color)
{pointer->drawPixel(x, y, *color);}
IRRLICHT_C_API void IVideoDriver_draw2DPolygon(IVideoDriver* pointer, core::position2d<s32>* center, f32 radius, const SColor& color = SColor(100,255,255,255), s32 vertexCount = 10)
{pointer->draw2DPolygon(*center, radius, color, vertexCount);}

#if (IRRLICHT_VERSION_MAJOR == 1 && IRRLICHT_VERSION_MINOR > 7)
IRRLICHT_C_API void IVideoDriver_drawStencilShadowVolume(IVideoDriver* pointer, const core::array<core::vector3df>& triangles, bool zfail = true, u32 debugDataVisible = 0)
{pointer->drawStencilShadowVolume(triangles, zfail, debugDataVisible);}
#else
IRRLICHT_C_API void IVideoDriver_drawStencilShadowVolume(IVideoDriver* pointer, const core::vector3df* triangles, s32 count, bool zfail = true)
{pointer->drawStencilShadowVolume(triangles, count, zfail);}
#endif

IRRLICHT_C_API void IVideoDriver_drawStencilShadow(IVideoDriver* pointer, bool clearStencilBuffer = false, const SColor& leftUpEdge = SColor(255,0,0,0), const SColor& rightUpEdge = SColor(255,0,0,0), const SColor& leftDownEdge = SColor(255,0,0,0), const SColor& rightDownEdge = SColor(255,0,0,0))
{pointer->drawStencilShadow(clearStencilBuffer, leftUpEdge, rightUpEdge, leftDownEdge, rightDownEdge);}
IRRLICHT_C_API void IVideoDriver_drawMeshBuffer(IVideoDriver* pointer, const scene::IMeshBuffer* mb)
{pointer->drawMeshBuffer(mb);}

IRRLICHT_C_API void IVideoDriver_setFog(IVideoDriver* pointer, const SColor& color = SColor(0,255,255,255), E_FOG_TYPE fogType = EFT_FOG_LINEAR, f32 start = 50.0f, f32 end = 100.0f, f32 density = 0.01f, bool pixelFog = false, bool rangeFog = false)
{pointer->setFog(color, fogType, start, end, density, pixelFog, rangeFog);}
IRRLICHT_C_API void IVideoDriver_getFog(IVideoDriver* pointer, SColor& color, E_FOG_TYPE& fogType, f32& start, f32& end, f32& density, bool& pixelFog, bool& rangeFog)
{pointer->getFog(color, fogType, start, end, density, pixelFog, rangeFog);}

IRRLICHT_C_API ECOLOR_FORMAT IVideoDriver_getColorFormat(IVideoDriver* pointer)
{return pointer->getColorFormat();}
IRRLICHT_C_API const core::dimension2d<u32>& IVideoDriver_getScreenSize(IVideoDriver* pointer)
{return pointer->getScreenSize();}
IRRLICHT_C_API const core::dimension2d<u32>& IVideoDriver_getCurrentRenderTargetSize(IVideoDriver* pointer)
{return pointer->getCurrentRenderTargetSize();}
IRRLICHT_C_API s32 IVideoDriver_getFPS(IVideoDriver* pointer)
{return pointer->getFPS();}
IRRLICHT_C_API u32 IVideoDriver_getPrimitiveCountDrawn(IVideoDriver* pointer, u32 mode =0)
{return pointer->getPrimitiveCountDrawn(mode);}
IRRLICHT_C_API void IVideoDriver_deleteAllDynamicLights(IVideoDriver* pointer)
{pointer->deleteAllDynamicLights();}
IRRLICHT_C_API s32 IVideoDriver_addDynamicLight(IVideoDriver* pointer, const SLight* light)
{return pointer->addDynamicLight(*light);}
IRRLICHT_C_API u32 IVideoDriver_getMaximalDynamicLightAmount(IVideoDriver* pointer)
{return pointer->getMaximalDynamicLightAmount();}
IRRLICHT_C_API u32 IVideoDriver_getDynamicLightCount(IVideoDriver* pointer)
{return pointer->getDynamicLightCount();}
IRRLICHT_C_API const SLight& IVideoDriver_getDynamicLight(IVideoDriver* pointer, u32 idx)
{return pointer->getDynamicLight(idx);}
IRRLICHT_C_API void IVideoDriver_turnLightOn(IVideoDriver* pointer, s32 lightIndex, bool turnOn)
{pointer->turnLightOn(lightIndex, turnOn);}
IRRLICHT_C_API const wchar_t* IVideoDriver_getName(IVideoDriver* pointer)
{return pointer->getName();}
IRRLICHT_C_API void IVideoDriver_addExternalImageLoader(IVideoDriver* pointer, IImageLoader* loader)
{pointer->addExternalImageLoader(loader);}
IRRLICHT_C_API void IVideoDriver_addExternalImageWriter(IVideoDriver* pointer, IImageWriter* writer)
{pointer->addExternalImageWriter(writer);}
IRRLICHT_C_API u32 IVideoDriver_getMaximalPrimitiveCount(IVideoDriver* pointer)
{return pointer->getMaximalPrimitiveCount();}
IRRLICHT_C_API void IVideoDriver_setTextureCreationFlag(IVideoDriver* pointer, E_TEXTURE_CREATION_FLAG flag, bool enabled = true)
{pointer->setTextureCreationFlag(flag, enabled);}
IRRLICHT_C_API bool IVideoDriver_getTextureCreationFlag(IVideoDriver* pointer, E_TEXTURE_CREATION_FLAG flag)
{return pointer->getTextureCreationFlag(flag);}

IRRLICHT_C_API IImage* IVideoDriver_createImageFromFile1(IVideoDriver* pointer, const fschar_t* filename)
{return pointer->createImageFromFile(io::path(filename));}
IRRLICHT_C_API IImage* IVideoDriver_createImageFromFile2(IVideoDriver* pointer, io::IReadFile* file)
{return pointer->createImageFromFile(file);}

IRRLICHT_C_API bool IVideoDriver_writeImageToFile1(IVideoDriver* pointer, IImage* image, const fschar_t* filename, u32 param = 0)
{return pointer->writeImageToFile(image, io::path(filename), param);}
IRRLICHT_C_API bool IVideoDriver_writeImageToFile2(IVideoDriver* pointer, IImage* image, io::IWriteFile* file, u32 param =0)
{return pointer->writeImageToFile(image, file, param);}

IRRLICHT_C_API IImage* IVideoDriver_createImageFromData(IVideoDriver* pointer, ECOLOR_FORMAT format, const core::dimension2d<u32>* size, void* data, bool ownForeignMemory = false, bool deleteMemory = true)
{return pointer->createImageFromData(format, *size, data, ownForeignMemory, deleteMemory);}

IRRLICHT_C_API IImage* IVideoDriver_createImage1(IVideoDriver* pointer, ECOLOR_FORMAT format, const core::dimension2d<u32>* size)
{return pointer->createImage(format, *size);}
//IRRLICHT_C_API IImage* IVideoDriver_createImage2(IVideoDriver* pointer, ECOLOR_FORMAT format, IImage *imageToCopy){return pointer->createImage(format, imageToCopy);}
//IRRLICHT_C_API IImage* IVideoDriver_createImage3(IVideoDriver* pointer, IImage* imageToCopy, const core::position2d<s32>* pos, const core::dimension2d<u32>* size){return pointer->createImage(imageToCopy, *pos, *size);}
IRRLICHT_C_API IImage* IVideoDriver_createImage4(IVideoDriver* pointer, ITexture* texture, const core::position2d<s32>* pos, const core::dimension2d<u32>* size)
{return pointer->createImage(texture, *pos, *size);}

IRRLICHT_C_API void IVideoDriver_OnResize(IVideoDriver* pointer, const core::dimension2d<u32>* size)
{pointer->OnResize(*size);}
IRRLICHT_C_API s32 IVideoDriver_addMaterialRenderer(IVideoDriver* pointer, IMaterialRenderer* renderer, const c8* name = 0)
{return pointer->addMaterialRenderer(renderer, name);}
IRRLICHT_C_API IMaterialRenderer* IVideoDriver_getMaterialRenderer(IVideoDriver* pointer, u32 idx)
{return pointer->getMaterialRenderer(idx);}
IRRLICHT_C_API u32 IVideoDriver_getMaterialRendererCount(IVideoDriver* pointer)
{return pointer->getMaterialRendererCount();}
IRRLICHT_C_API const c8* IVideoDriver_getMaterialRendererName(IVideoDriver* pointer, u32 idx)
{return pointer->getMaterialRendererName(idx);}
IRRLICHT_C_API void IVideoDriver_setMaterialRendererName(IVideoDriver* pointer, s32 idx, const c8* name)
{pointer->setMaterialRendererName(idx, name);}
IRRLICHT_C_API io::IAttributes* IVideoDriver_createAttributesFromMaterial(IVideoDriver* pointer, const video::SMaterial* material)
{return pointer->createAttributesFromMaterial(*material);}
IRRLICHT_C_API void IVideoDriver_fillMaterialStructureFromAttributes(IVideoDriver* pointer, video::SMaterial* outMaterial, io::IAttributes* attributes)
{pointer->fillMaterialStructureFromAttributes(*outMaterial, attributes);}
IRRLICHT_C_API const SExposedVideoData* IVideoDriver_getExposedVideoData(IVideoDriver* pointer)
{return &pointer->getExposedVideoData();}
IRRLICHT_C_API E_DRIVER_TYPE IVideoDriver_getDriverType(IVideoDriver* pointer)
{return pointer->getDriverType();}
IRRLICHT_C_API IGPUProgrammingServices* IVideoDriver_getGPUProgrammingServices(IVideoDriver* pointer)
{return pointer->getGPUProgrammingServices();}
IRRLICHT_C_API scene::IMeshManipulator* IVideoDriver_getMeshManipulator(IVideoDriver* pointer)
{return pointer->getMeshManipulator();}
IRRLICHT_C_API void IVideoDriver_clearZBuffer(IVideoDriver* pointer)
{pointer->clearZBuffer();}
IRRLICHT_C_API IImage* IVideoDriver_createScreenShot(IVideoDriver* pointer)
{return pointer->createScreenShot();}
IRRLICHT_C_API video::ITexture* IVideoDriver_findTexture(IVideoDriver* pointer, const fschar_t* filename)
{return pointer->findTexture(io::path(filename));}
IRRLICHT_C_API bool IVideoDriver_setClipPlane(IVideoDriver* pointer, u32 index, const core::plane3df* plane, bool enable = false)
{return pointer->setClipPlane(index, *plane, enable);}
IRRLICHT_C_API void IVideoDriver_enableClipPlane(IVideoDriver* pointer, u32 index, bool enable)
{pointer->enableClipPlane(index, enable);}
IRRLICHT_C_API void IVideoDriver_setMinHardwareBufferVertexCount(IVideoDriver* pointer, u32 count)
{pointer->setMinHardwareBufferVertexCount(count);}
IRRLICHT_C_API SOverrideMaterial* IVideoDriver_getOverrideMaterial(IVideoDriver* pointer)
{return &pointer->getOverrideMaterial();}
IRRLICHT_C_API SMaterial* IVideoDriver_getMaterial2D(IVideoDriver* pointer)
{return &pointer->getMaterial2D();}
IRRLICHT_C_API void IVideoDriver_enableMaterial2D(IVideoDriver* pointer, bool enable = true)
{pointer->enableMaterial2D(enable);}
IRRLICHT_C_API const c8* IVideoDriver_getVendorInfo(IVideoDriver* pointer)
{return pointer->getVendorInfo().c_str();}
IRRLICHT_C_API void IVideoDriver_setAmbientLight(IVideoDriver* pointer, const SColorf* color)
{pointer->setAmbientLight(*color);}
IRRLICHT_C_API void IVideoDriver_setAllowZWriteOnTransparent(IVideoDriver* pointer, bool flag)
{pointer->setAllowZWriteOnTransparent(flag);}
IRRLICHT_C_API const dimension2du IVideoDriver_getMaxTextureSize(IVideoDriver* pointer)
{return pointer->getMaxTextureSize();}

#ifdef _MSC_VER
IRRLICHT_C_API void* IVideoDriver_GetHandle(IVideoDriver* pointer)
{
	switch(pointer->getDriverType())
	{
	case EDT_NULL: return GetStdHandle(STD_OUTPUT_HANDLE);
	case EDT_SOFTWARE: return FindWindow("CIrrDeviceWin32", 0);
	case EDT_BURNINGSVIDEO: return FindWindow("CIrrDeviceWin32", 0);
	case EDT_DIRECT3D8: return pointer->getExposedVideoData().D3D8.HWnd;
	case EDT_DIRECT3D9: return pointer->getExposedVideoData().D3D9.HWnd;
	case EDT_OPENGL: return pointer->getExposedVideoData().OpenGLWin32.HWnd;
	default: return NULL;
	}
}
#else
IRRLICHT_C_API unsigned long IVideoDriver_GetHandle(IVideoDriver* pointer)
{
	switch(pointer->getDriverType())
	{
	case EDT_NULL: return (unsigned long)NULL;
	default: return pointer->getExposedVideoData().OpenGLLinux.X11Window;
	}
}
#endif

//ICON_SMALL,ICON_BIG
IRRLICHT_C_API void IVideoDriver_SetIcon(IVideoDriver* pointer, int icon_id = 32512, bool big_icon = false)
{
#ifdef _MSC_VER
	switch(pointer->getDriverType())
	{
	case EDT_NULL: SendMessage(HWND(pointer->getExposedVideoData().OpenGLWin32.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	case EDT_SOFTWARE: SendMessage(HWND(pointer->getExposedVideoData().OpenGLWin32.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	case EDT_BURNINGSVIDEO: SendMessage(HWND(pointer->getExposedVideoData().OpenGLWin32.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	case EDT_DIRECT3D8: SendMessage(HWND(pointer->getExposedVideoData().D3D8.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	case EDT_DIRECT3D9: SendMessage(HWND(pointer->getExposedVideoData().D3D9.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	case EDT_OPENGL: SendMessage(HWND(pointer->getExposedVideoData().OpenGLWin32.HWnd), WM_SETICON, big_icon, (LPARAM)LoadIcon(GetModuleHandle(NULL), MAKEINTRESOURCE(icon_id)));
	}
//#else
#endif
}
// floating point analogs for 2d drawing
IRRLICHT_C_API void IVideoDriver_draw2DRectangle_f1(IVideoDriver* pointer, SColor* color, f32 pos_x1, f32 pos_y1, f32 pos_x2, f32 pos_y2)
{pointer->draw2DRectangle(*color, core::rect<s32>(pos_x1, pos_y1, pos_x2, pos_y2));}
IRRLICHT_C_API void IVideoDriver_draw2DRectangle_f2(IVideoDriver* pointer, const SColor& color, f32 pos_x1, f32 pos_y1, f32 pos_x2, f32 pos_y2, f32 clip_x1, f32 clip_y1, f32 clip_x2, f32 clip_y2)
{core::rect<s32> clip(clip_x1, clip_y1, clip_x2, clip_y2); pointer->draw2DRectangle(color, core::rect<s32>(pos_x1, pos_y1, pos_x2, pos_y2), &clip);}
IRRLICHT_C_API void IVideoDriver_draw2DRectangle_f3(IVideoDriver* pointer, f32 pos_x1, f32 pos_y1, f32 pos_x2, f32 pos_y2, const SColor* colorLeftUp, const SColor* colorRightUp, const SColor* colorLeftDown, const SColor* colorRightDown)
{pointer->draw2DRectangle(core::rect<s32>(pos_x1, pos_y1, pos_x2, pos_y2), *colorLeftUp, *colorRightUp, *colorLeftDown, *colorRightDown);}
IRRLICHT_C_API void IVideoDriver_draw2DRectangle_f4(IVideoDriver* pointer, f32 pos_x1, f32 pos_y1, f32 pos_x2, f32 pos_y2, const SColor* colorLeftUp, const SColor* colorRightUp, const SColor* colorLeftDown, const SColor* colorRightDown, f32 clip_x1, f32 clip_y1, f32 clip_x2, f32 clip_y2)
{core::rect<s32> clip(clip_x1, clip_y1, clip_x2, clip_y2); pointer->draw2DRectangle(core::rect<s32>(pos_x1, pos_y1, pos_x2, pos_y2), *colorLeftUp, *colorRightUp, *colorLeftDown, *colorRightDown, &clip);}

IRRLICHT_C_API void IVideoDriver_draw2DRectangleOutline_f(IVideoDriver* pointer, f32 x1, f32 y1, f32 x2, f32 y2, const SColor& color = SColor(255,255,255,255))
{pointer->draw2DRectangleOutline(recti(x1, y1, x2, y2), color);}
IRRLICHT_C_API void IVideoDriver_draw2DLine_f(IVideoDriver* pointer, f32 start_x, f32 start_y, f32 end_x, f32 end_y, const SColor& color = SColor(255,255,255,255))
{pointer->draw2DLine(core::position2d<s32>(start_x, start_y), core::position2d<s32>(end_x, end_y), color);}
IRRLICHT_C_API void IVideoDriver_drawPixel_f(IVideoDriver* pointer, f32 x, f32 y, const SColor* color)
{pointer->drawPixel(x, y, *color);}
IRRLICHT_C_API void IVideoDriver_draw2DPolygon_f(IVideoDriver* pointer, f32 center_x, f32 center_y, f32 radius, const SColor& color = SColor(100,255,255,255), s32 vertexCount = 10)
{pointer->draw2DPolygon(core::position2d<s32>(center_x, center_y), radius, color, vertexCount);}

IRRLICHT_C_API void IVideoDriver_draw2DLineW(IVideoDriver* pointer, const core::position2d<s32>* start, const core::position2d<s32>* end, const SColor& color = SColor(255,255,255,255), s32 width = 0)
{
	if (width < 2)
		pointer->draw2DLine(*start, *end, color);
	else
	{
		if (width%2)//3>
		{
			s32 count = (width-1)/2;
			for(s32 i = -count; i <= count; i++)
				pointer->draw2DLine(core::position2d<s32>(start->X+i, start->Y+i), core::position2d<s32>(end->X+i, end->Y+i), color);
		}
		else//2>
		{
			s32 count = width/2;
			for(s32 i = -count; i < count; i++)
				pointer->draw2DLine(core::position2d<s32>(start->X+i, start->Y+i), core::position2d<s32>(end->X+i, end->Y+i), color);
		}
	}
}

IRRLICHT_C_API void IVideoDriver_draw2DLineWf(IVideoDriver* pointer, f32 x1, f32 y1, f32 x2, f32 y2, const SColor& color = SColor(255,255,255,255), s32 width = 0)
{
	if (width < 2)
		pointer->draw2DLine(core::position2d<s32>(x1, y1), core::position2d<s32>(x2, y2), color);
	else
	{
		if (width%2)//3>
		{
			s32 count = (width-1)/2;
			for(s32 i = -count; i <= count; i++)
				pointer->draw2DLine(core::position2d<s32>(x1+i, y1+i), core::position2d<s32>(x2+i, y2+i), color);
		}
		else//2>
		{
			s32 count = width/2;
			for(s32 i = -count; i < count; i++)
				pointer->draw2DLine(core::position2d<s32>(x1+i, y1+i), core::position2d<s32>(x2+i, y2+i), color);
		}
	}
}

#ifdef __cplusplus
}
#endif

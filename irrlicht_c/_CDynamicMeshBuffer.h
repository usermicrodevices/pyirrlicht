// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class CDynamicMeshBuffer : public IDynamicMeshBuffer
IRRLICHT_C_API const std::shared_ptr<CDynamicMeshBuffer>& CDynamicMeshBuffer_ctor(video::E_VERTEX_TYPE vertexType, video::E_INDEX_TYPE indexType)
{return std::make_shared<CDynamicMeshBuffer>(vertexType, indexType);}

IRRLICHT_C_API void CDynamicMeshBuffer_delete(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{/*if(pointer)delete pointer;*/}

IRRLICHT_C_API IVertexBuffer* CDynamicMeshBuffer_getVertexBuffer(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{return &pointer->getVertexBuffer();}

IRRLICHT_C_API IIndexBuffer* CDynamicMeshBuffer_getIndexBuffer(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{return &pointer->getIndexBuffer();}

IRRLICHT_C_API void CDynamicMeshBuffer_setVertexBuffer(const std::shared_ptr<CDynamicMeshBuffer>& pointer, IVertexBuffer* newVertexBuffer)
{pointer->setVertexBuffer(newVertexBuffer);}

IRRLICHT_C_API void CDynamicMeshBuffer_setIndexBuffer(const std::shared_ptr<CDynamicMeshBuffer>& pointer, IIndexBuffer* newIndexBuffer)
{pointer->setIndexBuffer(newIndexBuffer);}

IRRLICHT_C_API const video::SMaterial* CDynamicMeshBuffer_getMaterial1(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API video::SMaterial* CDynamicMeshBuffer_getMaterial2(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API void CDynamicMeshBuffer_setMaterial(const std::shared_ptr<CDynamicMeshBuffer>& pointer, video::SMaterial* value)
{pointer->Material = *value;}

IRRLICHT_C_API const core::aabbox3d<f32>* CDynamicMeshBuffer_getBoundingBox(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{return &pointer->getBoundingBox();}

IRRLICHT_C_API void CDynamicMeshBuffer_setBoundingBox(const std::shared_ptr<CDynamicMeshBuffer>& pointer, const core::aabbox3df* box)
{pointer->setBoundingBox(*box);}

IRRLICHT_C_API void CDynamicMeshBuffer_recalculateBoundingBox(const std::shared_ptr<CDynamicMeshBuffer>& pointer)
{pointer->recalculateBoundingBox();}


#ifdef __cplusplus
}
#endif

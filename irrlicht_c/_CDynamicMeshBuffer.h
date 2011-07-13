// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class CDynamicMeshBuffer : public IDynamicMeshBuffer
IRRLICHT_C_API CDynamicMeshBuffer* CDynamicMeshBuffer_ctor(video::E_VERTEX_TYPE vertexType, video::E_INDEX_TYPE indexType)
{return new CDynamicMeshBuffer(vertexType, indexType);}

IRRLICHT_C_API IVertexBuffer* CDynamicMeshBuffer_getVertexBuffer(CDynamicMeshBuffer* pointer)
{return &pointer->getVertexBuffer();}

IRRLICHT_C_API IIndexBuffer* CDynamicMeshBuffer_getIndexBuffer(CDynamicMeshBuffer* pointer)
{return &pointer->getIndexBuffer();}

IRRLICHT_C_API void CDynamicMeshBuffer_setVertexBuffer(CDynamicMeshBuffer* pointer, IVertexBuffer* newVertexBuffer)
{pointer->setVertexBuffer(newVertexBuffer);}

IRRLICHT_C_API void CDynamicMeshBuffer_setIndexBuffer(CDynamicMeshBuffer* pointer, IIndexBuffer* newIndexBuffer)
{pointer->setIndexBuffer(newIndexBuffer);}

IRRLICHT_C_API const video::SMaterial* CDynamicMeshBuffer_getMaterial1(CDynamicMeshBuffer* pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API video::SMaterial* CDynamicMeshBuffer_getMaterial2(CDynamicMeshBuffer* pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API void CDynamicMeshBuffer_setMaterial(CDynamicMeshBuffer* pointer, video::SMaterial* value)
{pointer->Material = *value;}

IRRLICHT_C_API const core::aabbox3d<f32>* CDynamicMeshBuffer_getBoundingBox(CDynamicMeshBuffer* pointer)
{return &pointer->getBoundingBox();}

IRRLICHT_C_API void CDynamicMeshBuffer_setBoundingBox(CDynamicMeshBuffer* pointer, const core::aabbox3df* box)
{pointer->setBoundingBox(*box);}

IRRLICHT_C_API void CDynamicMeshBuffer_recalculateBoundingBox(CDynamicMeshBuffer* pointer)
{pointer->recalculateBoundingBox();}


#ifdef __cplusplus
}
#endif

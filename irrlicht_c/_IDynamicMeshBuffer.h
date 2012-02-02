// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IDynamicMeshBuffer : public IMeshBuffer
IRRLICHT_C_API IVertexBuffer* IDynamicMeshBuffer_getVertexBuffer(IDynamicMeshBuffer* pointer)
{return &pointer->getVertexBuffer();}

IRRLICHT_C_API IIndexBuffer* IDynamicMeshBuffer_getIndexBuffer(IDynamicMeshBuffer* pointer)
{return &pointer->getIndexBuffer();}

IRRLICHT_C_API void IDynamicMeshBuffer_setVertexBuffer(IDynamicMeshBuffer* pointer, IVertexBuffer *vertexBuffer)
{pointer->setVertexBuffer(vertexBuffer);}

IRRLICHT_C_API void IDynamicMeshBuffer_setIndexBuffer(IDynamicMeshBuffer* pointer, IIndexBuffer *indexBuffer)
{pointer->setIndexBuffer(indexBuffer);}

IRRLICHT_C_API video::SMaterial* IDynamicMeshBuffer_getMaterial1(IDynamicMeshBuffer* pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API const video::SMaterial* IDynamicMeshBuffer_getMaterial2(IDynamicMeshBuffer* pointer)
{return &pointer->getMaterial();}

IRRLICHT_C_API const core::aabbox3df* IDynamicMeshBuffer_getBoundingBox(IDynamicMeshBuffer* pointer)
{return &pointer->getBoundingBox();}

IRRLICHT_C_API void IDynamicMeshBuffer_setBoundingBox(IDynamicMeshBuffer* pointer, const core::aabbox3df* box)
{pointer->setBoundingBox(*box);}

IRRLICHT_C_API void IDynamicMeshBuffer_recalculateBoundingBox(IDynamicMeshBuffer* pointer)
{pointer->recalculateBoundingBox();}

IRRLICHT_C_API void IDynamicMeshBuffer_append1(IDynamicMeshBuffer* pointer, const void* const vertices, u32 numVertices, const u16* const indices, u32 numIndices)
{pointer->append(vertices, numVertices, indices, numIndices);}

IRRLICHT_C_API void IDynamicMeshBuffer_append2(IDynamicMeshBuffer* pointer, const IMeshBuffer* const other)
{pointer->append(other);}

// ------------------- To be removed? -------------------  //

IRRLICHT_C_API E_HARDWARE_MAPPING IDynamicMeshBuffer_getHardwareMappingHint_Vertex(IDynamicMeshBuffer* pointer)
{return pointer->getHardwareMappingHint_Vertex();}

IRRLICHT_C_API E_HARDWARE_MAPPING IDynamicMeshBuffer_getHardwareMappingHint_Index(IDynamicMeshBuffer* pointer)
{return pointer->getHardwareMappingHint_Index();}

IRRLICHT_C_API void IDynamicMeshBuffer_setHardwareMappingHint(IDynamicMeshBuffer* pointer, E_HARDWARE_MAPPING NewMappingHint, E_BUFFER_TYPE Buffer=EBT_VERTEX_AND_INDEX )
{pointer->setHardwareMappingHint(NewMappingHint, Buffer);}

IRRLICHT_C_API void IDynamicMeshBuffer_setDirty(IDynamicMeshBuffer* pointer, E_BUFFER_TYPE Buffer=EBT_VERTEX_AND_INDEX)
{pointer->setDirty(Buffer);}

IRRLICHT_C_API u32 IDynamicMeshBuffer_getChangedID_Vertex(IDynamicMeshBuffer* pointer)
{return pointer->getChangedID_Vertex();}

IRRLICHT_C_API u32 IDynamicMeshBuffer_getChangedID_Index(IDynamicMeshBuffer* pointer)
{return pointer->getChangedID_Index();}

// ------------------- Old interface -------------------  //

IRRLICHT_C_API video::E_VERTEX_TYPE IDynamicMeshBuffer_getVertexType(IDynamicMeshBuffer* pointer)
{return pointer->getVertexType();}

IRRLICHT_C_API const void* IDynamicMeshBuffer_getVertices1(IDynamicMeshBuffer* pointer)
{return pointer->getVertices();}

IRRLICHT_C_API void* IDynamicMeshBuffer_getVertices2(IDynamicMeshBuffer* pointer)
{return pointer->getVertices();}

IRRLICHT_C_API u32 IDynamicMeshBuffer_getVertexCount(IDynamicMeshBuffer* pointer)
{return pointer->getVertexCount();}

IRRLICHT_C_API video::E_INDEX_TYPE IDynamicMeshBuffer_getIndexType(IDynamicMeshBuffer* pointer)
{return pointer->getIndexType();}

IRRLICHT_C_API const u16* IDynamicMeshBuffer_getIndices1(IDynamicMeshBuffer* pointer)
{return pointer->getIndices();}

IRRLICHT_C_API u16* IDynamicMeshBuffer_getIndices2(IDynamicMeshBuffer* pointer)
{return pointer->getIndices();}

IRRLICHT_C_API u32 IDynamicMeshBuffer_getIndexCount(IDynamicMeshBuffer* pointer)
{return pointer->getIndexCount();}

IRRLICHT_C_API const core::vector3df* IDynamicMeshBuffer_getPosition1(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getPosition(i);}

IRRLICHT_C_API core::vector3df* IDynamicMeshBuffer_getPosition2(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getPosition(i);}

IRRLICHT_C_API const core::vector2df* IDynamicMeshBuffer_getTCoords1(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getTCoords(i);}

IRRLICHT_C_API core::vector2df* IDynamicMeshBuffer_getTCoords2(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getTCoords(i);}

IRRLICHT_C_API const core::vector3df* IDynamicMeshBuffer_getNormal1(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getNormal(i);}

IRRLICHT_C_API core::vector3df* IDynamicMeshBuffer_getNormal2(IDynamicMeshBuffer* pointer, u32 i)
{return &pointer->getNormal(i);}

#ifdef __cplusplus
}
#endif

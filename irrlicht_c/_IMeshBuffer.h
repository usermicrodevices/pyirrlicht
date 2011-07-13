// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IMeshBuffer* IMeshBuffer_ctor(){return new IMeshBuffer();}

IRRLICHT_C_API video::SMaterial* IMeshBuffer_getMaterial(IMeshBuffer* pointer){return &pointer->getMaterial();}
//IRRLICHT_C_API const video::SMaterial& IMeshBuffer_getMaterial(IMeshBuffer* pointer){return pointer->getMaterial();}
IRRLICHT_C_API video::E_VERTEX_TYPE IMeshBuffer_getVertexType(IMeshBuffer* pointer){return pointer->getVertexType();}
//IRRLICHT_C_API const void* IMeshBuffer_getVertices(IMeshBuffer* pointer){return pointer->getVertices();}
IRRLICHT_C_API void* IMeshBuffer_getVertices(IMeshBuffer* pointer){return pointer->getVertices();}
IRRLICHT_C_API u32 IMeshBuffer_getVertexCount(IMeshBuffer* pointer){return pointer->getVertexCount();}
IRRLICHT_C_API video::E_INDEX_TYPE IMeshBuffer_getIndexType(IMeshBuffer* pointer){return pointer->getIndexType();}
//IRRLICHT_C_API const u16* IMeshBuffer_getIndices(IMeshBuffer* pointer){return pointer->getIndices();}
IRRLICHT_C_API u16* IMeshBuffer_getIndices(IMeshBuffer* pointer){return pointer->getIndices();}
IRRLICHT_C_API u32 IMeshBuffer_getIndexCount(IMeshBuffer* pointer){return pointer->getIndexCount();}
IRRLICHT_C_API const core::aabbox3df& IMeshBuffer_getBoundingBox(IMeshBuffer* pointer){return pointer->getBoundingBox();}
IRRLICHT_C_API void IMeshBuffer_setBoundingBox(IMeshBuffer* pointer, const core::aabbox3df& box){pointer->setBoundingBox(box);}
IRRLICHT_C_API void IMeshBuffer_recalculateBoundingBox(IMeshBuffer* pointer){pointer->recalculateBoundingBox();}
//IRRLICHT_C_API const core::vector3df& IMeshBuffer_getPosition(IMeshBuffer* pointer, u32 i){return pointer->getPosition(i);}
IRRLICHT_C_API core::vector3df* IMeshBuffer_getPosition(IMeshBuffer* pointer, u32 i){return &pointer->getPosition(i);}
//IRRLICHT_C_API const core::vector3df& IMeshBuffer_getNormal(IMeshBuffer* pointer, u32 i){return pointer->getNormal(i);}
IRRLICHT_C_API core::vector3df* IMeshBuffer_getNormal(IMeshBuffer* pointer, u32 i){return &pointer->getNormal(i);}
//IRRLICHT_C_API const core::vector2df& IMeshBuffer_getTCoords(IMeshBuffer* pointer, u32 i){return pointer->getTCoords(i);}
IRRLICHT_C_API core::vector2df* IMeshBuffer_getTCoords(IMeshBuffer* pointer, u32 i){return &pointer->getTCoords(i);}
IRRLICHT_C_API void IMeshBuffer_append1(IMeshBuffer* pointer, const void* const vertices, u32 numVertices, const u16* const indices, u32 numIndices){pointer->append(vertices, numVertices, indices, numIndices);}
IRRLICHT_C_API void IMeshBuffer_append2(IMeshBuffer* pointer, const IMeshBuffer* const other){pointer->append(other);}
IRRLICHT_C_API E_HARDWARE_MAPPING IMeshBuffer_getHardwareMappingHint_Vertex(IMeshBuffer* pointer){return pointer->getHardwareMappingHint_Vertex();}
IRRLICHT_C_API E_HARDWARE_MAPPING IMeshBuffer_getHardwareMappingHint_Index(IMeshBuffer* pointer){return pointer->getHardwareMappingHint_Index();}
IRRLICHT_C_API void IMeshBuffer_setHardwareMappingHint(IMeshBuffer* pointer, E_HARDWARE_MAPPING newMappingHint, E_BUFFER_TYPE buffer=EBT_VERTEX_AND_INDEX){pointer->setHardwareMappingHint(newMappingHint, buffer);}
IRRLICHT_C_API void IMeshBuffer_setDirty(IMeshBuffer* pointer, E_BUFFER_TYPE buffer=EBT_VERTEX_AND_INDEX){pointer->setDirty(buffer);}
IRRLICHT_C_API u32 IMeshBuffer_getChangedID_Vertex(IMeshBuffer* pointer){return pointer->getChangedID_Vertex();}
IRRLICHT_C_API u32 IMeshBuffer_getChangedID_Index(IMeshBuffer* pointer){return pointer->getChangedID_Index();}

#ifdef __cplusplus
}
#endif

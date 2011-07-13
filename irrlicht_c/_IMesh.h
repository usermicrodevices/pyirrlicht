// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IMesh
IRRLICHT_C_API u32 IMesh_getMeshBufferCount(IMesh* pointer){return pointer->getMeshBufferCount();}
IRRLICHT_C_API IMeshBuffer* IMesh_getMeshBuffer(IMesh* pointer, u32 nr){return pointer->getMeshBuffer(nr);}
IRRLICHT_C_API IMeshBuffer* IMesh_getMeshBuffer2(IMesh* pointer, const SMaterial& material){return pointer->getMeshBuffer(material);}
IRRLICHT_C_API const aabbox3d<f32>* IMesh_getBoundingBox(IMesh* pointer){return &pointer->getBoundingBox();}
IRRLICHT_C_API void IMesh_setBoundingBox(IMesh* pointer, const aabbox3df& box){pointer->setBoundingBox(box);}
IRRLICHT_C_API void IMesh_setMaterialFlag(IMesh* pointer, E_MATERIAL_FLAG flag, bool newvalue){pointer->setMaterialFlag(flag, newvalue);}
IRRLICHT_C_API void IMesh_setHardwareMappingHint(IMesh* pointer, E_HARDWARE_MAPPING newMappingHint, E_BUFFER_TYPE buffer = EBT_VERTEX_AND_INDEX){pointer->setHardwareMappingHint(newMappingHint, buffer);}
IRRLICHT_C_API void IMesh_setDirty(IMesh* pointer, E_BUFFER_TYPE buffer = EBT_VERTEX_AND_INDEX){pointer->setDirty(buffer);}

#ifdef __cplusplus
}
#endif

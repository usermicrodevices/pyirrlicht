// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//struct SMesh : public IMesh

IRRLICHT_C_API SMesh* SMesh_ctor1(){return new SMesh();}
IRRLICHT_C_API SMesh* SMesh_ctor2(int length = 1){SMesh* pointer; pointer = new SMesh[length]; return pointer;}

IRRLICHT_C_API SMesh* SMesh_get_item(SMesh* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SMesh_set_item(SMesh* pointer, SMesh* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API const u32 SMesh_getMeshBufferCount(SMesh* pointer){return pointer->getMeshBufferCount();}
IRRLICHT_C_API const IMeshBuffer* SMesh_getMeshBuffer1(SMesh* pointer, u32 nr){return pointer->getMeshBuffer(nr);}
IRRLICHT_C_API const IMeshBuffer* SMesh_getMeshBuffer2(SMesh* pointer, const video::SMaterial* material){return pointer->getMeshBuffer(*material);}

IRRLICHT_C_API const core::aabbox3d<f32>* SMesh_getBoundingBox(SMesh* pointer){return &pointer->getBoundingBox();}
IRRLICHT_C_API void SMesh_setBoundingBox(SMesh* pointer, const core::aabbox3df* box){pointer->setBoundingBox(*box);}

IRRLICHT_C_API void SMesh_recalculateBoundingBox(SMesh* pointer){pointer->recalculateBoundingBox();}
IRRLICHT_C_API void SMesh_addMeshBuffer(SMesh* pointer, IMeshBuffer* buf){pointer->addMeshBuffer(buf);}
IRRLICHT_C_API void SMesh_setMaterialFlag(SMesh* pointer, video::E_MATERIAL_FLAG flag, bool newvalue){pointer->setMaterialFlag(flag, newvalue);}
IRRLICHT_C_API void SMesh_setHardwareMappingHint(SMesh* pointer, E_HARDWARE_MAPPING newMappingHint, E_BUFFER_TYPE buffer_type = EBT_VERTEX_AND_INDEX){pointer->setHardwareMappingHint(newMappingHint, buffer_type);}
IRRLICHT_C_API void SMesh_setDirty(SMesh* pointer, E_BUFFER_TYPE buffer_type = EBT_VERTEX_AND_INDEX){pointer->setDirty(buffer_type);}

IRRLICHT_C_API core::array<IMeshBuffer*>* SMesh_get_MeshBuffers(SMesh* pointer){return &pointer->MeshBuffers;}
IRRLICHT_C_API void SMesh_set_MeshBuffers(SMesh* pointer, core::array<IMeshBuffer*>* value){pointer->MeshBuffers = *value;}

#ifdef __cplusplus
}
#endif

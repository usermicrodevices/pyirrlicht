// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//struct SMD3AnimationInfo
IRRLICHT_C_API SMD3AnimationInfo* SMD3AnimationInfo_ctor(){return new SMD3AnimationInfo();}
IRRLICHT_C_API s32 SMD3AnimationInfo_get_first(SMD3AnimationInfo* pointer){return pointer->first;}
IRRLICHT_C_API void SMD3AnimationInfo_set_first(SMD3AnimationInfo* pointer, s32 value){pointer->first = value;}
IRRLICHT_C_API s32 SMD3AnimationInfo_get_num(SMD3AnimationInfo* pointer){return pointer->num;}
IRRLICHT_C_API void SMD3AnimationInfo_set_num(SMD3AnimationInfo* pointer, s32 value){pointer->num = value;}
IRRLICHT_C_API s32 SMD3AnimationInfo_get_looping(SMD3AnimationInfo* pointer){return pointer->looping;}
IRRLICHT_C_API void SMD3AnimationInfo_set_looping(SMD3AnimationInfo* pointer, s32 value){pointer->looping = value;}
IRRLICHT_C_API s32 SMD3AnimationInfo_get_fps(SMD3AnimationInfo* pointer){return pointer->fps;}
IRRLICHT_C_API void SMD3AnimationInfo_set_fps(SMD3AnimationInfo* pointer, s32 value){pointer->fps = value;}

//struct SMD3Header
IRRLICHT_C_API SMD3Header* SMD3Header_ctor(){return new SMD3Header();}
IRRLICHT_C_API c8* SMD3Header_get_headerID(SMD3Header* pointer){return &pointer->headerID[0];}//headerID[4]
IRRLICHT_C_API void SMD3Header_set_headerID(SMD3Header* pointer, c8* value){pointer->headerID[0] = *value;}
IRRLICHT_C_API s32 SMD3Header_get_Version(SMD3Header* pointer){return pointer->Version;}
IRRLICHT_C_API void SMD3Header_set_Version(SMD3Header* pointer, s32 value){pointer->Version = value;}
IRRLICHT_C_API s8* SMD3Header_get_fileName(SMD3Header* pointer){return &pointer->fileName[0];}//fileName[68]
IRRLICHT_C_API void SMD3Header_set_fileName(SMD3Header* pointer, s8* value){pointer->fileName[0] = *value;}
IRRLICHT_C_API s32 SMD3Header_get_numFrames(SMD3Header* pointer){return pointer->numFrames;}
IRRLICHT_C_API void SMD3Header_set_numFrames(SMD3Header* pointer, s32 value){pointer->numFrames = value;}
IRRLICHT_C_API s32 SMD3Header_get_numTags(SMD3Header* pointer){return pointer->numTags;}
IRRLICHT_C_API void SMD3Header_set_numTags(SMD3Header* pointer, s32 value){pointer->numTags = value;}
IRRLICHT_C_API s32 SMD3Header_get_numMeshes(SMD3Header* pointer){return pointer->numMeshes;}
IRRLICHT_C_API void SMD3Header_set_numMeshes(SMD3Header* pointer, s32 value){pointer->numMeshes = value;}
IRRLICHT_C_API s32 SMD3Header_get_numMaxSkins(SMD3Header* pointer){return pointer->numMaxSkins;}
IRRLICHT_C_API void SMD3Header_set_numMaxSkins(SMD3Header* pointer, s32 value){pointer->numMaxSkins = value;}
IRRLICHT_C_API s32 SMD3Header_get_frameStart(SMD3Header* pointer){return pointer->frameStart;}
IRRLICHT_C_API void SMD3Header_set_frameStart(SMD3Header* pointer, s32 value){pointer->frameStart = value;}
IRRLICHT_C_API s32 SMD3Header_get_tagStart(SMD3Header* pointer){return pointer->tagStart;}
IRRLICHT_C_API void SMD3Header_set_tagStart(SMD3Header* pointer, s32 value){pointer->tagStart = value;}
IRRLICHT_C_API s32 SMD3Header_get_tagEnd(SMD3Header* pointer){return pointer->tagEnd;}
IRRLICHT_C_API void SMD3Header_set_tagEnd(SMD3Header* pointer, s32 value){pointer->tagEnd = value;}
IRRLICHT_C_API s32 SMD3Header_get_fileSize(SMD3Header* pointer){return pointer->fileSize;}
IRRLICHT_C_API void SMD3Header_set_fileSize(SMD3Header* pointer, s32 value){pointer->fileSize = value;}

//struct SMD3MeshHeader
IRRLICHT_C_API SMD3MeshHeader* SMD3MeshHeader_ctor(){return new SMD3MeshHeader();}
IRRLICHT_C_API c8* SMD3MeshHeader_get_meshID(SMD3MeshHeader* pointer){return &pointer->meshID[0];}//meshID[4]
IRRLICHT_C_API void SMD3MeshHeader_set_meshID(SMD3MeshHeader* pointer, c8* value){pointer->meshID[0] = *value;}
IRRLICHT_C_API c8* SMD3MeshHeader_get_meshName(SMD3MeshHeader* pointer){return &pointer->meshName[0];}//meshName[68]
IRRLICHT_C_API void SMD3MeshHeader_set_meshName(SMD3MeshHeader* pointer, c8* value){pointer->meshName[0] = *value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_numFrames(SMD3MeshHeader* pointer){return pointer->numFrames;}
IRRLICHT_C_API void SMD3MeshHeader_set_numFrames(SMD3MeshHeader* pointer, s32 value){pointer->numFrames = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_numShader(SMD3MeshHeader* pointer){return pointer->numShader;}
IRRLICHT_C_API void SMD3MeshHeader_set_numShader(SMD3MeshHeader* pointer, s32 value){pointer->numShader = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_numVertices(SMD3MeshHeader* pointer){return pointer->numVertices;}
IRRLICHT_C_API void SMD3MeshHeader_set_numVertices(SMD3MeshHeader* pointer, s32 value){pointer->numVertices = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_numTriangles(SMD3MeshHeader* pointer){return pointer->numTriangles;}
IRRLICHT_C_API void SMD3MeshHeader_set_numTriangles(SMD3MeshHeader* pointer, s32 value){pointer->numTriangles = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_offset_triangles(SMD3MeshHeader* pointer){return pointer->offset_triangles;}
IRRLICHT_C_API void SMD3MeshHeader_set_offset_triangles(SMD3MeshHeader* pointer, s32 value){pointer->offset_triangles = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_offset_shaders(SMD3MeshHeader* pointer){return pointer->offset_shaders;}
IRRLICHT_C_API void SMD3MeshHeader_set_offset_shaders(SMD3MeshHeader* pointer, s32 value){pointer->offset_shaders = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_offset_st(SMD3MeshHeader* pointer){return pointer->offset_st;}
IRRLICHT_C_API void SMD3MeshHeader_set_offset_st(SMD3MeshHeader* pointer, s32 value){pointer->offset_st = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_vertexStart(SMD3MeshHeader* pointer){return pointer->vertexStart;}
IRRLICHT_C_API void SMD3MeshHeader_set_vertexStart(SMD3MeshHeader* pointer, s32 value){pointer->vertexStart = value;}
IRRLICHT_C_API s32 SMD3MeshHeader_get_offset_end(SMD3MeshHeader* pointer){return pointer->offset_end;}
IRRLICHT_C_API void SMD3MeshHeader_set_offset_end(SMD3MeshHeader* pointer, s32 value){pointer->offset_end = value;}

//struct SMD3Vertex
IRRLICHT_C_API SMD3Vertex* SMD3Vertex_ctor(){return new SMD3Vertex();}
IRRLICHT_C_API s16* SMD3Vertex_get_position(SMD3Vertex* pointer){return &pointer->position[0];}//position[3]
IRRLICHT_C_API void SMD3Vertex_set_position(SMD3Vertex* pointer, s16* value){pointer->position[0] = *value;}
IRRLICHT_C_API u8* SMD3Vertex_get_normal(SMD3Vertex* pointer){return &pointer->normal[0];}//normal[2]
IRRLICHT_C_API void SMD3Vertex_set_normal(SMD3Vertex* pointer, u8* value){pointer->normal[0] = *value;}

//struct SMD3TexCoord
IRRLICHT_C_API SMD3TexCoord* SMD3TexCoord_ctor(){return new SMD3TexCoord();}
IRRLICHT_C_API f32 SMD3TexCoord_get_u(SMD3TexCoord* pointer){return pointer->u;}
IRRLICHT_C_API void SMD3TexCoord_set_u(SMD3TexCoord* pointer, f32 value){pointer->u = value;}
IRRLICHT_C_API f32 SMD3TexCoord_get_v(SMD3TexCoord* pointer){return pointer->v;}
IRRLICHT_C_API void SMD3TexCoord_set_v(SMD3TexCoord* pointer, f32 value){pointer->v = value;}

//struct SMD3Face
IRRLICHT_C_API SMD3Face* SMD3Face_ctor(){return new SMD3Face();}
IRRLICHT_C_API s32* SMD3Face_get_Index(SMD3Face* pointer){return &pointer->Index[0];}//Index[3]
IRRLICHT_C_API void SMD3Face_set_Index(SMD3Face* pointer, s32* value){pointer->Index[0] = *value;}

//struct SMD3MeshBuffer : public IReferenceCounted
IRRLICHT_C_API SMD3MeshBuffer* SMD3MeshBuffer_ctor(){return new SMD3MeshBuffer();}
IRRLICHT_C_API SMD3MeshHeader* SMD3MeshBuffer_get_MeshHeader(SMD3MeshBuffer* pointer){return &pointer->MeshHeader;}
IRRLICHT_C_API void SMD3MeshBuffer_set_MeshHeader(SMD3MeshBuffer* pointer, SMD3MeshHeader* value){pointer->MeshHeader = *value;}
IRRLICHT_C_API const c8* SMD3MeshBuffer_get_Shader(SMD3MeshBuffer* pointer){return pointer->Shader.c_str();}
IRRLICHT_C_API void SMD3MeshBuffer_set_Shader(SMD3MeshBuffer* pointer, c8* value){pointer->Shader = core::stringc(value);}
IRRLICHT_C_API core::array<s32>* SMD3MeshBuffer_get_Indices(SMD3MeshBuffer* pointer){return &pointer->Indices;}
IRRLICHT_C_API void SMD3MeshBuffer_set_Indices(SMD3MeshBuffer* pointer, core::array<s32>* value){pointer->Indices = *value;}
IRRLICHT_C_API core::array<SMD3Vertex>* SMD3MeshBuffer_get_Vertices(SMD3MeshBuffer* pointer){return &pointer->Vertices;}
IRRLICHT_C_API void SMD3MeshBuffer_set_Vertices(SMD3MeshBuffer* pointer, core::array<SMD3Vertex>* value){pointer->Vertices = *value;}
IRRLICHT_C_API core::array<SMD3TexCoord>* SMD3MeshBuffer_get_Tex(SMD3MeshBuffer* pointer){return &pointer->Tex;}
IRRLICHT_C_API void SMD3MeshBuffer_set_Tex(SMD3MeshBuffer* pointer, core::array<SMD3TexCoord>* value){pointer->Tex = *value;}

//struct SMD3QuaternionTag
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTag_ctor1(const c8* name){return new SMD3QuaternionTag(core::stringc(name));}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTag_ctor2(const c8* name, const core::matrix4* m){return new SMD3QuaternionTag(core::stringc(name), *m);}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTag_ctor3(const core::vector3df* pos, const core::vector3df* angle){return new SMD3QuaternionTag(*pos, *angle);}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTag_ctor4(const SMD3QuaternionTag* copyMe){return new SMD3QuaternionTag(*copyMe);}
IRRLICHT_C_API void SMD3QuaternionTag_setto(SMD3QuaternionTag* pointer, core::matrix4* m){pointer->setto(*m);}
IRRLICHT_C_API const bool SMD3QuaternionTag_operator_eq(SMD3QuaternionTag* pointer, const SMD3QuaternionTag* other){return pointer->operator==(*other);}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTag_operator_set(SMD3QuaternionTag* pointer, const SMD3QuaternionTag* copyMe){return &pointer->operator=(*copyMe);}
IRRLICHT_C_API const c8* SMD3QuaternionTag_get_Name(SMD3QuaternionTag* pointer){return pointer->Name.c_str();}
IRRLICHT_C_API void SMD3QuaternionTag_set_Name(SMD3QuaternionTag* pointer, const c8* value){pointer->Name = core::stringc(value);}
IRRLICHT_C_API core::vector3df* SMD3QuaternionTag_get_position(SMD3QuaternionTag* pointer){return &pointer->position;}
IRRLICHT_C_API void SMD3QuaternionTag_set_position(SMD3QuaternionTag* pointer, core::vector3df* value){pointer->position = *value;}
IRRLICHT_C_API core::quaternion* SMD3QuaternionTag_get_rotation(SMD3QuaternionTag* pointer){return &pointer->rotation;}
IRRLICHT_C_API void SMD3QuaternionTag_set_rotation(SMD3QuaternionTag* pointer, core::quaternion* value){pointer->rotation = *value;}

//struct SMD3QuaternionTagList
IRRLICHT_C_API SMD3QuaternionTagList* SMD3QuaternionTagList_ctor1(){return new SMD3QuaternionTagList();}
IRRLICHT_C_API SMD3QuaternionTagList* SMD3QuaternionTagList_ctor2(const SMD3QuaternionTagList* copyMe){return new SMD3QuaternionTagList(*copyMe);}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTagList_get(SMD3QuaternionTagList* pointer, const c8* name){return pointer->get(core::stringc(name));}
IRRLICHT_C_API const u32 SMD3QuaternionTagList_size(SMD3QuaternionTagList* pointer){return pointer->size();}
IRRLICHT_C_API void SMD3QuaternionTagList_set_used(SMD3QuaternionTagList* pointer, u32 new_size){pointer->set_used(new_size);}
IRRLICHT_C_API const SMD3QuaternionTag* SMD3QuaternionTagList_const_operator_index(SMD3QuaternionTagList* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API SMD3QuaternionTag* SMD3QuaternionTagList_operator_index(SMD3QuaternionTagList* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API void SMD3QuaternionTagList_push_back(SMD3QuaternionTagList* pointer, const SMD3QuaternionTag* other){pointer->push_back(*other);}
IRRLICHT_C_API SMD3QuaternionTagList* SMD3QuaternionTagList_operator_set(SMD3QuaternionTagList* pointer, const SMD3QuaternionTagList* copyMe){return &pointer->operator=(*copyMe);}
IRRLICHT_C_API void SMD3QuaternionTagList_set_tag_item(SMD3QuaternionTagList* pointer, u32 index, SMD3QuaternionTag* item){pointer->operator[](index) = *item;}

//struct SMD3Mesh: public IReferenceCounted
IRRLICHT_C_API SMD3Mesh* SMD3Mesh_ctor(){return new SMD3Mesh();}
IRRLICHT_C_API const c8* SMD3Mesh_get_Name(SMD3Mesh* pointer){return pointer->Name.c_str();}
IRRLICHT_C_API void SMD3Mesh_set_Name(SMD3Mesh* pointer, c8* value){pointer->Name = core::stringc(value);}
IRRLICHT_C_API core::array<SMD3MeshBuffer*>* SMD3Mesh_get_Buffer(SMD3Mesh* pointer){return &pointer->Buffer;}
IRRLICHT_C_API void SMD3Mesh_set_Buffer(SMD3Mesh* pointer, core::array<SMD3MeshBuffer*>* value){pointer->Buffer = *value;}
IRRLICHT_C_API SMD3QuaternionTagList* SMD3Mesh_get_TagList(SMD3Mesh* pointer){return &pointer->TagList;}
IRRLICHT_C_API void SMD3Mesh_set_TagList(SMD3Mesh* pointer, SMD3QuaternionTagList* value){pointer->TagList = *value;}
IRRLICHT_C_API SMD3Header* SMD3Mesh_get_MD3Header(SMD3Mesh* pointer){return &pointer->MD3Header;}
IRRLICHT_C_API void SMD3Mesh_set_MD3Header(SMD3Mesh* pointer, SMD3Header* value){pointer->MD3Header = *value;}


//class IAnimatedMeshMD3 : public IAnimatedMesh
IRRLICHT_C_API void IAnimatedMeshMD3_setInterpolationShift(IAnimatedMeshMD3* pointer, u32 shift, u32 loopMode){pointer->setInterpolationShift(shift, loopMode);}
IRRLICHT_C_API SMD3QuaternionTagList* IAnimatedMeshMD3_getTagList(IAnimatedMeshMD3* pointer, s32 frame, s32 detailLevel, s32 startFrameLoop, s32 endFrameLoop){return pointer->getTagList(frame, detailLevel, startFrameLoop, endFrameLoop);}
IRRLICHT_C_API SMD3Mesh* IAnimatedMeshMD3_getOriginalMesh(IAnimatedMeshMD3* pointer){return pointer->getOriginalMesh();}

#ifdef __cplusplus
}
#endif

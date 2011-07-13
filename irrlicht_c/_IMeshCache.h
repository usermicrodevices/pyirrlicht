// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class IMeshCache : public virtual IReferenceCounted

IRRLICHT_C_API void IMeshCache_addMesh(IMeshCache* pointer, const fschar_t* name, IAnimatedMesh* mesh){pointer->addMesh(io::path(name), mesh);}

IRRLICHT_C_API void IMeshCache_removeMesh1(IMeshCache* pointer, const IAnimatedMesh* const mesh){pointer->removeMesh(mesh);}
IRRLICHT_C_API void IMeshCache_removeMesh2(IMeshCache* pointer, const IMesh* const mesh){pointer->removeMesh(mesh);}

IRRLICHT_C_API u32 IMeshCache_getMeshCount(IMeshCache* pointer){return pointer->getMeshCount();}

IRRLICHT_C_API s32 IMeshCache_getMeshIndex1(IMeshCache* pointer, const IAnimatedMesh* const mesh){return pointer->getMeshIndex(mesh);}
IRRLICHT_C_API s32 IMeshCache_getMeshIndex2(IMeshCache* pointer, const IMesh* const mesh){return pointer->getMeshIndex(mesh);}

IRRLICHT_C_API IAnimatedMesh* IMeshCache_getMeshByIndex(IMeshCache* pointer, u32 index){return pointer->getMeshByIndex(index);}

//_IRR_DEPRECATED_ IAnimatedMesh* getMeshByFilename(const io::path& filename)
//_IRR_DEPRECATED_ const io::path& getMeshFilename(u32 index)
//_IRR_DEPRECATED_ const io::path& getMeshFilename(const IAnimatedMesh* const mesh)
//_IRR_DEPRECATED_ const io::path& getMeshFilename(const IMesh* const mesh) const
//_IRR_DEPRECATED_ bool setMeshFilename(u32 index, const io::path& filename)
//_IRR_DEPRECATED_ bool setMeshFilename(const IAnimatedMesh* const mesh, const io::path& filename)
//_IRR_DEPRECATED_ bool setMeshFilename(const IMesh* const mesh, const io::path& filename)

IRRLICHT_C_API IAnimatedMesh* IMeshCache_getMeshByName(IMeshCache* pointer, const fschar_t* name){return pointer->getMeshByName(io::path(name));}

IRRLICHT_C_API const io::SNamedPath* IMeshCache_getMeshNameByIndex(IMeshCache* pointer, u32 index){return &pointer->getMeshName(index);}

IRRLICHT_C_API const io::SNamedPath* IMeshCache_getMeshName1(IMeshCache* pointer, const IAnimatedMesh* const mesh){return &pointer->getMeshName(mesh);}
IRRLICHT_C_API const io::SNamedPath* IMeshCache_getMeshName2(IMeshCache* pointer, const IMesh* const mesh){return &pointer->getMeshName(mesh);}

IRRLICHT_C_API bool IMeshCache_renameMeshByIndex(IMeshCache* pointer, u32 index, const fschar_t* name){return pointer->renameMesh(index, io::path(name));}

IRRLICHT_C_API bool IMeshCache_renameMesh1(IMeshCache* pointer, const IAnimatedMesh* const mesh, const fschar_t* name){return pointer->renameMesh(mesh, io::path(name));}
IRRLICHT_C_API bool IMeshCache_renameMesh2(IMeshCache* pointer, const IMesh* const mesh, const fschar_t* name){return pointer->renameMesh(mesh, io::path(name));}

IRRLICHT_C_API bool IMeshCache_isMeshLoaded(IMeshCache* pointer, const fschar_t* name){return pointer->isMeshLoaded(io::path(name));}

IRRLICHT_C_API void IMeshCache_clear(IMeshCache* pointer){pointer->clear();}

IRRLICHT_C_API void IMeshCache_clearUnusedMeshes(IMeshCache* pointer){pointer->clearUnusedMeshes();}

#ifdef __cplusplus
}
#endif

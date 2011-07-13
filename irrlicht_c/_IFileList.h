// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IFileList
IRRLICHT_C_API u32 IFileList_getFileCount(IFileList* pointer){return pointer->getFileCount();}
IRRLICHT_C_API const fschar_t* IFileList_getFileName(IFileList* pointer, u32 index){return pointer->getFileName(index).c_str();}
IRRLICHT_C_API const fschar_t* IFileList_getFullFileName(IFileList* pointer, u32 index){return pointer->getFullFileName(index).c_str();}
IRRLICHT_C_API u32 IFileList_getFileSize(IFileList* pointer, u32 index){return pointer->getFileSize(index);}
IRRLICHT_C_API u32 IFileList_getID(IFileList* pointer, u32 index){return pointer->getID(index);}
IRRLICHT_C_API bool IFileList_isDirectory(IFileList* pointer, u32 index){return pointer->isDirectory(index);}
IRRLICHT_C_API s32 IFileList_findFile(IFileList* pointer, const fschar_t* filename, bool isFolder=false){return pointer->findFile(filename, isFolder);}
IRRLICHT_C_API const fschar_t* IFileList_getPath(IFileList* pointer){return pointer->getPath().c_str();}
IRRLICHT_C_API u32 IFileList_addItem(IFileList* pointer, const fschar_t* fullPath, u32 size, bool isDirectory, u32 id=0){return pointer->addItem(io::path(fullPath), size, isDirectory, id);}
IRRLICHT_C_API void IFileList_sort(IFileList* pointer){pointer->sort();}

#ifdef __cplusplus
}
#endif

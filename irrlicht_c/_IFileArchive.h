// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IFileArchive
IRRLICHT_C_API IReadFile* IFileArchive_createAndOpenFile1(IFileArchive* pointer, const char* filename){return pointer->createAndOpenFile(*filename);}
IRRLICHT_C_API IReadFile* IFileArchive_createAndOpenFile2(IFileArchive* pointer, u32 index){return pointer->createAndOpenFile(index);}
IRRLICHT_C_API const IFileList* IFileArchive_getFileList(IFileArchive* pointer){return pointer->getFileList();}
IRRLICHT_C_API E_FILE_ARCHIVE_TYPE IFileArchive_getType(IFileArchive* pointer){return pointer->getType();}
IRRLICHT_C_API char* IFileArchive_get_Password(IFileArchive* pointer){return (char*)&pointer->Password;}
IRRLICHT_C_API void IFileArchive_set_Password(IFileArchive* pointer, char* value){pointer->Password = value;}

//================= IArchiveLoader
IRRLICHT_C_API bool IArchiveLoader_isALoadableFileFormat1(IArchiveLoader* pointer, const char* filename){return pointer->isALoadableFileFormat(irr::io::path(*filename));}
IRRLICHT_C_API bool IArchiveLoader_isALoadableFileFormat2(IArchiveLoader* pointer, io::IReadFile* file){return pointer->isALoadableFileFormat(file);}
IRRLICHT_C_API bool IArchiveLoader_isALoadableFileFormat3(IArchiveLoader* pointer, E_FILE_ARCHIVE_TYPE fileType){return pointer->isALoadableFileFormat(fileType);}
IRRLICHT_C_API IFileArchive* IArchiveLoader_createArchive1(IArchiveLoader* pointer, const char* filename, bool ignoreCase, bool ignorePaths){return pointer->createArchive(irr::io::path(*filename), ignoreCase, ignorePaths);}
IRRLICHT_C_API IFileArchive* IArchiveLoader_createArchive2(IArchiveLoader* pointer, io::IReadFile* file, bool ignoreCase, bool ignorePaths){return pointer->createArchive(file, ignoreCase, ignorePaths);}

#ifdef __cplusplus
}
#endif

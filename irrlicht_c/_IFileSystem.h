// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

#if defined(_IRR_WCHAR_FILESYSTEM)
	const fschar_t* default_root = L"/";
#else
	const fschar_t* default_root = "/";
#endif

//================= IFileSystem
IRRLICHT_C_API IReadFile* IFileSystem_createAndOpenFile(IFileSystem* pointer, const fschar_t* filename)
{return pointer->createAndOpenFile(path(filename));}

IRRLICHT_C_API IReadFile* IFileSystem_createMemoryReadFile(IFileSystem* pointer, void* memory, s32 len, const fschar_t* filename, bool deleteMemoryWhenDropped=false)
{return pointer->createMemoryReadFile(memory, len, path(filename), deleteMemoryWhenDropped);}

IRRLICHT_C_API IReadFile* IFileSystem_createLimitReadFile(IFileSystem* pointer, const fschar_t* filename, IReadFile* alreadyOpenedFile, long pos, long areaSize)
{return pointer->createLimitReadFile(path(filename), alreadyOpenedFile, pos, areaSize);}

IRRLICHT_C_API IWriteFile* IFileSystem_createMemoryWriteFile(IFileSystem* pointer, void* memory, s32 len, const fschar_t* filename, bool deleteMemoryWhenDropped=false)
{return pointer->createMemoryWriteFile(memory, len, path(filename), deleteMemoryWhenDropped);}

IRRLICHT_C_API IWriteFile* IFileSystem_createAndWriteFile(IFileSystem* pointer, const fschar_t* filename, bool append=false)
{return pointer->createAndWriteFile(path(filename), append);}

IRRLICHT_C_API bool IFileSystem_addFileArchive(IFileSystem* pointer, const fschar_t* filename, bool ignoreCase=true, bool ignorePaths=true, E_FILE_ARCHIVE_TYPE archiveType=EFAT_UNKNOWN)
{return pointer->addFileArchive(path(filename), ignoreCase, ignorePaths, archiveType);}

IRRLICHT_C_API void IFileSystem_addArchiveLoader(IFileSystem* pointer, IArchiveLoader* loader)
{pointer->addArchiveLoader(loader);}

IRRLICHT_C_API u32 IFileSystem_getFileArchiveCount(IFileSystem* pointer)
{return pointer->getFileArchiveCount();}

IRRLICHT_C_API bool IFileSystem_removeFileArchive1(IFileSystem* pointer, u32 index)
{return pointer->removeFileArchive(index);}

IRRLICHT_C_API bool IFileSystem_removeFileArchive2(IFileSystem* pointer, const fschar_t* filename)
{return pointer->removeFileArchive(path(filename));}

IRRLICHT_C_API bool IFileSystem_moveFileArchive(IFileSystem* pointer, u32 sourceIndex, s32 relative)
{return pointer->moveFileArchive(sourceIndex, relative);}

IRRLICHT_C_API IFileArchive* IFileSystem_getFileArchive(IFileSystem* pointer, u32 index)
{return pointer->getFileArchive(index);}

IRRLICHT_C_API bool IFileSystem_addZipFileArchive(IFileSystem* pointer, const c8* filename, bool ignoreCase=true, bool ignorePaths=true)
{return pointer->addZipFileArchive(filename, ignoreCase, ignorePaths);}

IRRLICHT_C_API bool IFileSystem_addFolderFileArchive(IFileSystem* pointer, const c8* filename, bool ignoreCase=true, bool ignorePaths=true)
{return pointer->addFolderFileArchive(filename, ignoreCase, ignorePaths);}

IRRLICHT_C_API bool IFileSystem_addPakFileArchive(IFileSystem* pointer, const c8* filename, bool ignoreCase=true, bool ignorePaths=true)
{return pointer->addPakFileArchive(filename, ignoreCase, ignorePaths);}

IRRLICHT_C_API const fschar_t* IFileSystem_getWorkingDirectory(IFileSystem* pointer)
{return pointer->getWorkingDirectory().c_str();}

IRRLICHT_C_API bool IFileSystem_changeWorkingDirectoryTo(IFileSystem* pointer, const fschar_t* newDirectory)
{return pointer->changeWorkingDirectoryTo(path(newDirectory));}

IRRLICHT_C_API const fschar_t* IFileSystem_getAbsolutePath(IFileSystem* pointer, const fschar_t* filename)
{return pointer->getAbsolutePath(path(filename)).c_str();}

IRRLICHT_C_API const fschar_t* IFileSystem_getFileDir(IFileSystem* pointer, const fschar_t* filename)
{return pointer->getFileDir(path(filename)).c_str();}

IRRLICHT_C_API const fschar_t* IFileSystem_getFileBasename(IFileSystem* pointer, const fschar_t* filename, bool keepExtension=true)
{return pointer->getFileBasename(path(filename), keepExtension).c_str();}

IRRLICHT_C_API const fschar_t* IFileSystem_flattenFilename(IFileSystem* pointer, const fschar_t* directory, const fschar_t* root = default_root)
{return pointer->flattenFilename(*const_cast<path*>(&path(directory)), path(root)).c_str();}

IRRLICHT_C_API IFileList* IFileSystem_createFileList(IFileSystem* pointer)
{return pointer->createFileList();}

IRRLICHT_C_API IFileList* IFileSystem_createEmptyFileList(IFileSystem* pointer, const fschar_t* _path, bool ignoreCase, bool ignorePaths)
{return pointer->createEmptyFileList(path(_path), ignoreCase, ignorePaths);}

IRRLICHT_C_API EFileSystemType IFileSystem_setFileListSystem(IFileSystem* pointer, EFileSystemType listType)
{return pointer->setFileListSystem(listType);}

IRRLICHT_C_API bool IFileSystem_existFile(IFileSystem* pointer, const fschar_t* filename)
{return pointer->existFile(path(filename));}

IRRLICHT_C_API IXMLReader* IFileSystem_createXMLReader1(IFileSystem* pointer, const fschar_t* filename)
{return pointer->createXMLReader(path(filename));}

IRRLICHT_C_API IXMLReader* IFileSystem_createXMLReader2(IFileSystem* pointer, IReadFile* file)
{return pointer->createXMLReader(file);}

IRRLICHT_C_API IXMLReaderUTF8* IFileSystem_createXMLReaderUTF8(IFileSystem* pointer, const fschar_t* filename)
{return pointer->createXMLReaderUTF8(path(filename));}

IRRLICHT_C_API IXMLReaderUTF8* IFileSystem_createXMLReaderUTF8stream(IFileSystem* pointer, IReadFile* file)
{return pointer->createXMLReaderUTF8(file);}

IRRLICHT_C_API IXMLWriter* IFileSystem_createXMLWriter1(IFileSystem* pointer, const fschar_t* filename)
{return pointer->createXMLWriter(path(filename));}

IRRLICHT_C_API IXMLWriter* IFileSystem_createXMLWriter2(IFileSystem* pointer, IWriteFile* file)
{return pointer->createXMLWriter(file);}

IRRLICHT_C_API IAttributes* IFileSystem_createEmptyAttributes(IFileSystem* pointer, video::IVideoDriver* driver=0)
{return pointer->createEmptyAttributes(driver);}

#ifdef __cplusplus
}
#endif

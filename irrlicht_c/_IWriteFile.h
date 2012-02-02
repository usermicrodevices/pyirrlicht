// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IWriteFile
IRRLICHT_C_API s32 IWriteFile_write(IWriteFile* pointer, const void* buffer, u32 sizeToWrite){return pointer->write(buffer, sizeToWrite);}
IRRLICHT_C_API bool IWriteFile_seek(IWriteFile* pointer, long finalPos, bool relativeMovement = false){return pointer->seek(finalPos, relativeMovement);}
IRRLICHT_C_API long IWriteFile_getPos(IWriteFile* pointer){return pointer->getPos();}
IRRLICHT_C_API const fschar_t* IWriteFile_getFileName(IWriteFile* pointer){return pointer->getFileName().c_str();}

#ifdef __cplusplus
}
#endif

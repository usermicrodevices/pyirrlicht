// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class IReadFile : public virtual IReferenceCounted

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API s32 IReadFile_read(IReadFile* pointer, void* buffer, u32 sizeToRead)
{return pointer->read(buffer, sizeToRead);}
IRRLICHT_C_API bool IReadFile_seek(IReadFile* pointer, long finalPos, bool relativeMovement = false)
{return pointer->seek(finalPos, relativeMovement);}
IRRLICHT_C_API long IReadFile_getSize(IReadFile* pointer)
{return pointer->getSize();}
IRRLICHT_C_API long IReadFile_getPos(IReadFile* pointer)
{return pointer->getPos();}
IRRLICHT_C_API const fschar_t* IReadFile_getFileName(IReadFile* pointer)
{return pointer->getFileName().c_str();}

#ifdef __cplusplus
}
#endif

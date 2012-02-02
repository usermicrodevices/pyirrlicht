// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class IImageLoader : public virtual IReferenceCounted

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IImageLoader* IImageLoader_ctor(){return new IImageLoader();}
IRRLICHT_C_API bool IImageLoader_isALoadableFileExtension(IImageLoader* pointer, const fschar_t* filename)
{return pointer->isALoadableFileExtension(io::path(filename));}

IRRLICHT_C_API bool IImageLoader_isALoadableFileFormat(IImageLoader* pointer, io::IReadFile* file)
{return pointer->isALoadableFileFormat(file);}

IRRLICHT_C_API IImage* IImageLoader_loadImage(IImageLoader* pointer, io::IReadFile* file)
{return pointer->loadImage(file);}


#ifdef __cplusplus
}
#endif

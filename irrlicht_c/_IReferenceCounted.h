// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IReferenceCounted
IRRLICHT_C_API IReferenceCounted* IReferenceCounted_ctor(void* pointer)
{return (IReferenceCounted*)pointer;}
//IRRLICHT_C_API void IReferenceCounted_Destructor(IReferenceCounted* pointer){delete pointer;}
IRRLICHT_C_API void IReferenceCounted_grab(IReferenceCounted* pointer)
{pointer->grab();}
IRRLICHT_C_API bool IReferenceCounted_drop(IReferenceCounted* pointer)
{return pointer->drop();}
IRRLICHT_C_API s32 IReferenceCounted_getReferenceCount(IReferenceCounted* pointer)
{return pointer->getReferenceCount();}
IRRLICHT_C_API const c8* IReferenceCounted_getDebugName(IReferenceCounted* pointer)
{return pointer->getDebugName();}
IRRLICHT_C_API bool IReferenceCounted_is_null(IReferenceCounted* pointer)
{
#ifdef _MSC_VER
	__try
	{
#endif
		return (pointer->getReferenceCount() > 0) ? false : true;
#ifdef _MSC_VER
	}
	__except(puts("EXCEPT: IReferenceCounted POINTER IS BAD"), 1)
	{
		return true;
	}
#endif
}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

//class IIndexBuffer : public IRRLICHT_C_API IReferenceCounted

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API void* IIndexBuffer_getData(IIndexBuffer* pointer)
{return pointer->getData();}

IRRLICHT_C_API video::E_INDEX_TYPE IIndexBuffer_getType(IIndexBuffer* pointer)
{return pointer->getType();}

IRRLICHT_C_API void IIndexBuffer_setType(IIndexBuffer* pointer, video::E_INDEX_TYPE IndexType)
{pointer->setType(IndexType);}

IRRLICHT_C_API u32 IIndexBuffer_stride(IIndexBuffer* pointer)
{return pointer->stride();}

IRRLICHT_C_API u32 IIndexBuffer_size(IIndexBuffer* pointer)
{return pointer->size();}

IRRLICHT_C_API void IIndexBuffer_push_back(IIndexBuffer* pointer, const u32& element)
{pointer->push_back(element);}

IRRLICHT_C_API u32 IIndexBuffer_get_item(IIndexBuffer* pointer, u32 index)
{return pointer->operator[](index);}

IRRLICHT_C_API u32 IIndexBuffer_getLast(IIndexBuffer* pointer)
{return pointer->getLast();}

IRRLICHT_C_API void IIndexBuffer_setValue(IIndexBuffer* pointer, u32 index, u32 value)
{pointer->setValue(index, value);}

IRRLICHT_C_API void IIndexBuffer_set_used(IIndexBuffer* pointer, u32 usedNow)
{pointer->set_used(usedNow);}

IRRLICHT_C_API void IIndexBuffer_reallocate(IIndexBuffer* pointer, u32 new_size)
{pointer->reallocate(new_size);}

IRRLICHT_C_API u32 IIndexBuffer_allocated_size(IIndexBuffer* pointer)
{return pointer->allocated_size();}

IRRLICHT_C_API void* IIndexBuffer_pointer(IIndexBuffer* pointer)
{return pointer->pointer();}

IRRLICHT_C_API E_HARDWARE_MAPPING IIndexBuffer_getHardwareMappingHint(IIndexBuffer* pointer)
{return pointer->getHardwareMappingHint();}

IRRLICHT_C_API void IIndexBuffer_setHardwareMappingHint(IIndexBuffer* pointer, E_HARDWARE_MAPPING NewMappingHint)
{pointer->setHardwareMappingHint(NewMappingHint);}

IRRLICHT_C_API void IIndexBuffer_setDirty(IIndexBuffer* pointer)
{pointer->setDirty();}

IRRLICHT_C_API u32 IIndexBuffer_getChangedID(IIndexBuffer* pointer)
{return pointer->getChangedID();}

#ifdef __cplusplus
}
#endif

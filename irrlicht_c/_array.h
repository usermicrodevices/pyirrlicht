// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class array
IRRLICHT_C_API core::array<void*>* array_ctor1()
{return new core::array<void*>();}

IRRLICHT_C_API core::array<void*>* array_ctor2(u32 start_count)
{return new core::array<void*>(start_count);}

IRRLICHT_C_API core::array<void*>* array_ctor3(core::array<void*>* other)
{return new core::array<void*>(*other);}

IRRLICHT_C_API void array_reallocate(core::array<void*>* pointer, u32 new_size)
{pointer->reallocate(new_size);}

IRRLICHT_C_API void array_setAllocStrategy(core::array<void*>* pointer, eAllocStrategy newStrategy = ALLOC_STRATEGY_DOUBLE)
{pointer->setAllocStrategy(newStrategy);}

IRRLICHT_C_API void array_push_back(core::array<void*>* pointer, void* element)
{pointer->push_back(*&element);}

IRRLICHT_C_API void array_push_front(core::array<void*>* pointer, void* element)
{pointer->push_front(*&element);}

IRRLICHT_C_API void array_insert(core::array<void*>* pointer, void* element, u32 index = 0)
{pointer->insert(*&element, index);}

IRRLICHT_C_API void array_clear(core::array<void*>* pointer)
{pointer->clear();}

IRRLICHT_C_API void array_set_pointer(core::array<void*>* pointer, void* newPointer, u32 size, bool _is_sorted=false, bool _free_when_destroyed=true)
{pointer->set_pointer(&newPointer, size, _is_sorted, _free_when_destroyed);}

IRRLICHT_C_API void array_set_free_when_destroyed(core::array<void*>* pointer, bool f)
{pointer->set_free_when_destroyed(f);}

IRRLICHT_C_API void array_set_used(core::array<void*>* pointer, u32 usedNow)
{pointer->set_used(usedNow);}

IRRLICHT_C_API const array<void*>* array_set(core::array<void*>* pointer, const array<void*>* other)
{return &pointer->operator=(*other);}

IRRLICHT_C_API const bool array_operator_eq(core::array<void*>* pointer, const array<void*>* other)
{return pointer->operator==(*other);}

IRRLICHT_C_API const bool array_operator_neq(core::array<void*>* pointer, const array<void*>* other)
{return pointer->operator!=(*other);}

IRRLICHT_C_API const void* array_get_item(core::array<void*>* pointer, u32 index)
{return &pointer->operator[](index);}

IRRLICHT_C_API void array_set_item(core::array<void*>* pointer, u32 index, void* element)
{pointer->operator[](index) = element;}

IRRLICHT_C_API void* array_getLast(core::array<void*>* pointer)
{return &pointer->getLast();}

IRRLICHT_C_API void* array_pointer(core::array<void*>* pointer)
{return pointer->pointer();}

IRRLICHT_C_API const void* array_const_pointer(core::array<void*>* pointer)
{return pointer->const_pointer();}

IRRLICHT_C_API irr::u32 array_size(core::array<void*>* pointer)
{return pointer->size();}

IRRLICHT_C_API irr::u32 array_allocated_size(core::array<void*>* pointer)
{return pointer->allocated_size();}

IRRLICHT_C_API const bool array_empty(core::array<void*>* pointer)
{return pointer->empty();}

IRRLICHT_C_API void array_sort(core::array<void*>* pointer)
{pointer->sort();}

IRRLICHT_C_API const s32 array_binary_search1(core::array<void*>* pointer, void* element)
{return pointer->binary_search(*&element);}

IRRLICHT_C_API const s32 array_binary_search2(core::array<void*>* pointer, void* element, s32 left, s32 right)
{return pointer->binary_search(*&element, left, right);}

IRRLICHT_C_API s32 array_binary_search_multi(core::array<void*>* pointer, void* element, s32& last)
{return pointer->binary_search_multi(*&element, last);}

IRRLICHT_C_API const s32 array_linear_search(core::array<void*>* pointer, void* element)
{return pointer->linear_search(*&element);}

IRRLICHT_C_API const s32 array_linear_reverse_search(core::array<void*>* pointer, void* element)
{return pointer->linear_reverse_search(*&element);}

IRRLICHT_C_API void array_erase1(core::array<void*>* pointer, u32 index)
{pointer->erase(index);}

IRRLICHT_C_API void array_erase2(core::array<void*>* pointer, u32 index, s32 count)
{pointer->erase(index, count);}

IRRLICHT_C_API void array_set_sorted(core::array<void*>* pointer, bool _is_sorted)
{pointer->set_sorted(_is_sorted);}

IRRLICHT_C_API void array_swap(core::array<void*>* pointer, core::array<void*>* other)
{pointer->swap(*other);}

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= rectf
IRRLICHT_C_API rectf* rectf_ctor1(){return new rectf();}
IRRLICHT_C_API rectf* rectf_ctor2(f32 x=0.0f, f32 y=0.0f, f32 x2=0.0f, f32 y2=0.0f){return new rectf(x, y, x2, y2);}
IRRLICHT_C_API rectf* rectf_ctor3(const position2df& upperLeft, const position2df& lowerRight){return new rectf(upperLeft, lowerRight);}
IRRLICHT_C_API rectf* rectf_ctor4(const position2df& pos, const dimension2df& size){return new rectf(pos, size);}
IRRLICHT_C_API rectf* rectf_add(rectf* pointer, const position2df& pos){return &pointer->operator+(pos);}
IRRLICHT_C_API rectf* rectf_add_set(rectf* pointer, const position2df& pos){return &pointer->operator+=(pos);}
IRRLICHT_C_API rectf* rectf_sub(rectf* pointer, const position2df& pos){return &pointer->operator-(pos);}
IRRLICHT_C_API rectf* rectf_sub_set(rectf* pointer, const position2df& pos){return &pointer->operator-=(pos);}
IRRLICHT_C_API bool rectf_eq(rectf* pointer, const rectf& other){return pointer->operator==(other);}
IRRLICHT_C_API bool rectf_ne(rectf* pointer, const rectf& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool rectf_le(rectf* pointer, const rectf& other){return pointer->operator<(other);}
IRRLICHT_C_API f32 rectf_getArea(rectf* pointer){return pointer->getArea();}
IRRLICHT_C_API bool rectf_isPointInside(rectf* pointer, const position2df& pos){return pointer->isPointInside(pos);}
IRRLICHT_C_API bool rectf_isRectCollided(rectf* pointer, const rectf& other){return pointer->isRectCollided(other);}
IRRLICHT_C_API void rectf_clipAgainst(rectf* pointer, const rectf& other){pointer->clipAgainst(other);}
IRRLICHT_C_API bool rectf_constrainTo(rectf* pointer, const rectf& other){return pointer->constrainTo(other);}
IRRLICHT_C_API f32 rectf_getWidth(rectf* pointer){return pointer->getWidth();}
IRRLICHT_C_API f32 rectf_getHeight(rectf* pointer){return pointer->getHeight();}
IRRLICHT_C_API void rectf_repair(rectf* pointer){pointer->repair();}
IRRLICHT_C_API bool rectf_isValid(rectf* pointer){return pointer->isValid();}
IRRLICHT_C_API position2df* rectf_getCenter(rectf* pointer){return &pointer->getCenter();}
IRRLICHT_C_API dimension2df* rectf_getSize(rectf* pointer){return &pointer->getSize();}
IRRLICHT_C_API void rectf_addInternalPoint1(rectf* pointer, const position2df& p){pointer->addInternalPoint(p);}
IRRLICHT_C_API void rectf_addInternalPoint2(rectf* pointer, f32 x, f32 y){pointer->addInternalPoint(x, y);}
IRRLICHT_C_API position2df* rectf_get_UpperLeftCorner(rectf* pointer){return &pointer->UpperLeftCorner;}
IRRLICHT_C_API void rectf_set_UpperLeftCorner(rectf* pointer, position2df* value){pointer->UpperLeftCorner = *value;}
IRRLICHT_C_API position2df* rectf_get_LowerRightCorner(rectf* pointer){return &pointer->LowerRightCorner;}
IRRLICHT_C_API void rectf_set_LowerRightCorner(rectf* pointer, position2df* value){pointer->LowerRightCorner = *value;}

//================= recti
IRRLICHT_C_API recti* recti_ctor1(){return new recti();}
IRRLICHT_C_API recti* recti_ctor2(s32 x=0, s32 y=0, s32 x2=0, s32 y2=0){return new recti(x, y, x2, y2);}
IRRLICHT_C_API recti* recti_ctor3(const position2di& upperLeft, const position2di& lowerRight){return new recti(upperLeft, lowerRight);}
IRRLICHT_C_API recti* recti_ctor4(const position2di& pos, const dimension2di& size){return new recti(pos, size);}
IRRLICHT_C_API recti* recti_add(recti* pointer, const position2di& pos){return &pointer->operator+(pos);}
IRRLICHT_C_API recti* recti_add_set(recti* pointer, const position2di& pos){return &pointer->operator+=(pos);}
IRRLICHT_C_API recti* recti_sub(recti* pointer, const position2di& pos){return &pointer->operator-(pos);}
IRRLICHT_C_API recti* recti_sub_set(recti* pointer, const position2di& pos){return &pointer->operator-=(pos);}
IRRLICHT_C_API bool recti_eq(recti* pointer, const recti& other){return pointer->operator==(other);}
IRRLICHT_C_API bool recti_ne(recti* pointer, const recti& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool recti_le(recti* pointer, const recti& other){return pointer->operator<(other);}
IRRLICHT_C_API s32 recti_getArea(recti* pointer){return pointer->getArea();}
IRRLICHT_C_API bool recti_isPointInside(recti* pointer, const position2di& pos){return pointer->isPointInside(pos);}
IRRLICHT_C_API bool recti_isRectCollided(recti* pointer, const recti& other){return pointer->isRectCollided(other);}
IRRLICHT_C_API void recti_clipAgainst(recti* pointer, const recti& other){pointer->clipAgainst(other);}
IRRLICHT_C_API bool recti_constrainTo(recti* pointer, const recti& other){return pointer->constrainTo(other);}
IRRLICHT_C_API s32 recti_getWidth(recti* pointer){return pointer->getWidth();}
IRRLICHT_C_API s32 recti_getHeight(recti* pointer){return pointer->getHeight();}
IRRLICHT_C_API void recti_repair(recti* pointer){pointer->repair();}
IRRLICHT_C_API bool recti_isValid(recti* pointer){return pointer->isValid();}
IRRLICHT_C_API position2di* recti_getCenter(recti* pointer){return &pointer->getCenter();}
IRRLICHT_C_API dimension2di* recti_getSize(recti* pointer){return &pointer->getSize();}
IRRLICHT_C_API void recti_addInternalPoint1(recti* pointer, const position2di& p){pointer->addInternalPoint(p);}
IRRLICHT_C_API void recti_addInternalPoint2(recti* pointer, s32 x, s32 y){pointer->addInternalPoint(x, y);}
IRRLICHT_C_API position2di* recti_get_UpperLeftCorner(recti* pointer){return &pointer->UpperLeftCorner;}
IRRLICHT_C_API void recti_set_UpperLeftCorner(recti* pointer, position2di* value){pointer->UpperLeftCorner = *value;}
IRRLICHT_C_API position2di* recti_get_LowerRightCorner(recti* pointer){return &pointer->LowerRightCorner;}
IRRLICHT_C_API void recti_set_LowerRightCorner(recti* pointer, position2di* value){pointer->LowerRightCorner = *value;}

//================= array<rect<s32>> (rects32array)
IRRLICHT_C_API core::array< rect<s32> >* rects32array_ctor(){return new array< rect<s32> >();}
IRRLICHT_C_API void rects32array_reallocate(core::array< rect<s32> >* pointer, u32 new_size){pointer->reallocate(new_size);}
IRRLICHT_C_API void rects32array_setAllocStrategy(core::array< rect<s32> >* pointer, eAllocStrategy newStrategy = ALLOC_STRATEGY_DOUBLE){pointer->setAllocStrategy(newStrategy);}
IRRLICHT_C_API void rects32array_push_back(core::array< rect<s32> >* pointer, rect<s32>* element){pointer->push_back(*element);}
IRRLICHT_C_API void rects32array_push_front(core::array< rect<s32> >* pointer, rect<s32>* element){pointer->push_front(*element);}
IRRLICHT_C_API void rects32array_insert(core::array< rect<s32> >* pointer, rect<s32>* element, u32 index=0){pointer->insert(*element, index);}
IRRLICHT_C_API void rects32array_clear(core::array< rect<s32> >* pointer){pointer->clear();}
IRRLICHT_C_API void rects32array_set_pointer(core::array< rect<s32> >* pointer, rect<s32>* newPointer, u32 size, bool _is_sorted=false, bool _free_when_destroyed=true){pointer->set_pointer(newPointer, size, _is_sorted, _free_when_destroyed);}
IRRLICHT_C_API void rects32array_set_free_when_destroyed(core::array< rect<s32> >* pointer, bool f){pointer->set_free_when_destroyed(f);}
IRRLICHT_C_API void rects32array_set_used(core::array< rect<s32> >* pointer, u32 usedNow){pointer->set_used(usedNow);}
IRRLICHT_C_API rect<s32>* rects32array_get_item(core::array< rect<s32> >* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API u32 rects32array_size(core::array< rect<s32> >* pointer){return pointer->size();}
IRRLICHT_C_API bool rects32array_empty(core::array< rect<s32> >* pointer){return pointer->empty();}
IRRLICHT_C_API void rects32array_sort(core::array< rect<s32> >* pointer){pointer->sort();}
IRRLICHT_C_API s32 rects32array_binary_search1(core::array< rect<s32> >* pointer, rect<s32>* element){return pointer->binary_search(*element);}
IRRLICHT_C_API s32 rects32array_binary_search2(core::array< rect<s32> >* pointer, rect<s32>* element, s32 left, s32 right){return pointer->binary_search(*element, left, right);}
IRRLICHT_C_API s32 rects32array_binary_search_multi(core::array< rect<s32> >* pointer, rect<s32>* element, s32& last){return pointer->binary_search_multi(*element, last);}
IRRLICHT_C_API s32 rects32array_linear_search(core::array< rect<s32> >* pointer, rect<s32>* element){return pointer->linear_search(*element);}
IRRLICHT_C_API s32 rects32array_linear_reverse_search(core::array< rect<s32> >* pointer, rect<s32>* element){return pointer->linear_reverse_search(*element);}
IRRLICHT_C_API void rects32array_erase1(core::array< rect<s32> >* pointer, u32 index){pointer->erase(index);}
IRRLICHT_C_API void rects32array_erase2(core::array< rect<s32> >* pointer, u32 index, s32 count){pointer->erase(index, count);}
IRRLICHT_C_API void rects32array_set_sorted(core::array< rect<s32> >* pointer, bool _is_sorted){pointer->set_sorted(_is_sorted);}
IRRLICHT_C_API void rects32array_swap(core::array< rect<s32> >* pointer, array< rect<s32> >* other){pointer->swap(*other);}

#ifdef __cplusplus
}
#endif

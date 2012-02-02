// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SGUISpriteFrame
IRRLICHT_C_API SGUISpriteFrame* SGUISpriteFrame_ctor(){return new SGUISpriteFrame();}
IRRLICHT_C_API u32 SGUISpriteFrame_get_rectNumber(SGUISpriteFrame* pointer){return pointer->rectNumber;}
IRRLICHT_C_API void SGUISpriteFrame_set_rectNumber(SGUISpriteFrame* pointer, u32 value){pointer->rectNumber = value;}
IRRLICHT_C_API u32 SGUISpriteFrame_get_textureNumber(SGUISpriteFrame* pointer){return pointer->textureNumber;}
IRRLICHT_C_API void SGUISpriteFrame_set_textureNumber(SGUISpriteFrame* pointer, u32 value){pointer->textureNumber = value;}

//================= array<SGUISpriteFrame> (SGUISpriteFrameArray)
IRRLICHT_C_API core::array<SGUISpriteFrame>* SGUISpriteFrameArray_ctor(){return new array<SGUISpriteFrame>();}
IRRLICHT_C_API void SGUISpriteFrameArray_reallocate(core::array<SGUISpriteFrame>* pointer, u32 new_size){pointer->reallocate(new_size);}
IRRLICHT_C_API void SGUISpriteFrameArray_setAllocStrategy(core::array<SGUISpriteFrame>* pointer, eAllocStrategy newStrategy = ALLOC_STRATEGY_DOUBLE){pointer->setAllocStrategy(newStrategy);}
IRRLICHT_C_API void SGUISpriteFrameArray_push_back(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element){pointer->push_back(*element);}
IRRLICHT_C_API void SGUISpriteFrameArray_push_front(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element){pointer->push_front(*element);}
IRRLICHT_C_API void SGUISpriteFrameArray_insert(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element, u32 index=0){pointer->insert(*element, index);}
IRRLICHT_C_API void SGUISpriteFrameArray_clear(core::array<SGUISpriteFrame>* pointer){pointer->clear();}
IRRLICHT_C_API void SGUISpriteFrameArray_set_pointer(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* newPointer, u32 size, bool _is_sorted=false, bool _free_when_destroyed=true){pointer->set_pointer(newPointer, size, _is_sorted, _free_when_destroyed);}
IRRLICHT_C_API void SGUISpriteFrameArray_set_free_when_destroyed(core::array<SGUISpriteFrame>* pointer, bool f){pointer->set_free_when_destroyed(f);}
IRRLICHT_C_API void SGUISpriteFrameArray_set_used(core::array<SGUISpriteFrame>* pointer, u32 usedNow){pointer->set_used(usedNow);}
IRRLICHT_C_API SGUISpriteFrame* SGUISpriteFrameArray_get_item(core::array<SGUISpriteFrame>* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API u32 SGUISpriteFrameArray_size(core::array<SGUISpriteFrame>* pointer){return pointer->size();}
IRRLICHT_C_API bool SGUISpriteFrameArray_empty(core::array<SGUISpriteFrame>* pointer){return pointer->empty();}
//IRRLICHT_C_API void SGUISpriteFrameArray_sort(core::array<SGUISpriteFrame>* pointer){pointer->sort();}
//IRRLICHT_C_API s32 SGUISpriteFrameArray_binary_search1(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element){return pointer->binary_search(*element);}
//IRRLICHT_C_API s32 SGUISpriteFrameArray_binary_search2(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element, s32 left, s32 right){return pointer->binary_search(*element, left, right);}
//IRRLICHT_C_API s32 SGUISpriteFrameArray_binary_search_multi(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element, s32& last){return pointer->binary_search_multi(*element, last);}
//IRRLICHT_C_API s32 SGUISpriteFrameArray_linear_search(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element){return pointer->linear_search(*element);}
//IRRLICHT_C_API s32 SGUISpriteFrameArray_linear_reverse_search(core::array<SGUISpriteFrame>* pointer, SGUISpriteFrame* element){return pointer->linear_reverse_search(*element);}
IRRLICHT_C_API void SGUISpriteFrameArray_erase1(core::array<SGUISpriteFrame>* pointer, u32 index){pointer->erase(index);}
IRRLICHT_C_API void SGUISpriteFrameArray_erase2(core::array<SGUISpriteFrame>* pointer, u32 index, s32 count){pointer->erase(index, count);}
IRRLICHT_C_API void SGUISpriteFrameArray_set_sorted(core::array<SGUISpriteFrame>* pointer, bool _is_sorted){pointer->set_sorted(_is_sorted);}
IRRLICHT_C_API void SGUISpriteFrameArray_swap(core::array<SGUISpriteFrame>* pointer, array<SGUISpriteFrame>* other){pointer->swap(*other);}

//================= SGUISprite
IRRLICHT_C_API SGUISprite* SGUISprite_ctor(){return new SGUISprite();}
IRRLICHT_C_API core::array<SGUISpriteFrame>* SGUISprite_get_Frames(SGUISprite* pointer){return &pointer->Frames;}
IRRLICHT_C_API void SGUISprite_set_Frames(SGUISprite* pointer, core::array<SGUISpriteFrame>* value){pointer->Frames = *value;}
IRRLICHT_C_API u32 SGUISprite_get_frameTime(SGUISprite* pointer){return pointer->frameTime;}
IRRLICHT_C_API void SGUISprite_set_frameTime(SGUISprite* pointer, u32 value){pointer->frameTime = value;}

//================= array<SGUISprite> (SGUISpriteArray)
IRRLICHT_C_API core::array<SGUISprite>* SGUISpriteArray_ctor(){return new array<SGUISprite>();}
IRRLICHT_C_API void SGUISpriteArray_reallocate(core::array<SGUISprite>* pointer, u32 new_size){pointer->reallocate(new_size);}
IRRLICHT_C_API void SGUISpriteArray_setAllocStrategy(core::array<SGUISprite>* pointer, eAllocStrategy newStrategy = ALLOC_STRATEGY_DOUBLE){pointer->setAllocStrategy(newStrategy);}
IRRLICHT_C_API void SGUISpriteArray_push_back(core::array<SGUISprite>* pointer, SGUISprite* element){pointer->push_back(*element);}
IRRLICHT_C_API void SGUISpriteArray_push_front(core::array<SGUISprite>* pointer, SGUISprite* element){pointer->push_front(*element);}
IRRLICHT_C_API void SGUISpriteArray_insert(core::array<SGUISprite>* pointer, SGUISprite* element, u32 index=0){pointer->insert(*element, index);}
IRRLICHT_C_API void SGUISpriteArray_clear(core::array<SGUISprite>* pointer){pointer->clear();}
IRRLICHT_C_API void SGUISpriteArray_set_pointer(core::array<SGUISprite>* pointer, SGUISprite* newPointer, u32 size, bool _is_sorted=false, bool _free_when_destroyed=true){pointer->set_pointer(newPointer, size, _is_sorted, _free_when_destroyed);}
IRRLICHT_C_API void SGUISpriteArray_set_free_when_destroyed(core::array<SGUISprite>* pointer, bool f){pointer->set_free_when_destroyed(f);}
IRRLICHT_C_API void SGUISpriteArray_set_used(core::array<SGUISprite>* pointer, u32 usedNow){pointer->set_used(usedNow);}
IRRLICHT_C_API SGUISprite* SGUISpriteArray_get_item(core::array<SGUISprite>* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API u32 SGUISpriteArray_size(core::array<SGUISprite>* pointer){return pointer->size();}
IRRLICHT_C_API bool SGUISpriteArray_empty(core::array<SGUISprite>* pointer){return pointer->empty();}
//IRRLICHT_C_API void SGUISpriteArray_sort(core::array<SGUISprite>* pointer){pointer->sort();}
//IRRLICHT_C_API s32 SGUISpriteArray_binary_search1(core::array<SGUISprite>* pointer, SGUISprite* element){return pointer->binary_search(*element);}
//IRRLICHT_C_API s32 SGUISpriteArray_binary_search2(core::array<SGUISprite>* pointer, SGUISprite* element, s32 left, s32 right){return pointer->binary_search(*element, left, right);}
//IRRLICHT_C_API s32 SGUISpriteArray_binary_search_multi(core::array<SGUISprite>* pointer, SGUISprite* element, s32& last){return pointer->binary_search_multi(*element, last);}
//IRRLICHT_C_API s32 SGUISpriteArray_linear_search(core::array<SGUISprite>* pointer, SGUISprite* element){return pointer->linear_search(*element);}
//IRRLICHT_C_API s32 SGUISpriteArray_linear_reverse_search(core::array<SGUISprite>* pointer, SGUISprite* element){return pointer->linear_reverse_search(*element);}
IRRLICHT_C_API void SGUISpriteArray_erase1(core::array<SGUISprite>* pointer, u32 index){pointer->erase(index);}
IRRLICHT_C_API void SGUISpriteArray_erase2(core::array<SGUISprite>* pointer, u32 index, s32 count){pointer->erase(index, count);}
IRRLICHT_C_API void SGUISpriteArray_set_sorted(core::array<SGUISprite>* pointer, bool _is_sorted){pointer->set_sorted(_is_sorted);}
IRRLICHT_C_API void SGUISpriteArray_swap(core::array<SGUISprite>* pointer, array<SGUISprite>* other){pointer->swap(*other);}

//================= IGUISpriteBank
IRRLICHT_C_API core::array< core::rect<s32> >* IGUISpriteBank_getPositions(IGUISpriteBank* pointer){return &pointer->getPositions();}
IRRLICHT_C_API core::array<SGUISprite>* IGUISpriteBank_getSprites(IGUISpriteBank* pointer){return &pointer->getSprites();}
IRRLICHT_C_API u32 IGUISpriteBank_getTextureCount(IGUISpriteBank* pointer){return pointer->getTextureCount();}
IRRLICHT_C_API video::ITexture* IGUISpriteBank_getTexture(IGUISpriteBank* pointer, u32 index){return pointer->getTexture(index);}
IRRLICHT_C_API void IGUISpriteBank_addTexture(IGUISpriteBank* pointer, video::ITexture* texture){pointer->addTexture(texture);}
IRRLICHT_C_API void IGUISpriteBank_setTexture(IGUISpriteBank* pointer, u32 index, video::ITexture* texture){pointer->setTexture(index, texture);}
IRRLICHT_C_API s32 IGUISpriteBank_addTextureAsSprite(IGUISpriteBank* pointer, video::ITexture* texture){return pointer->addTextureAsSprite(texture);}
IRRLICHT_C_API void IGUISpriteBank_clear(IGUISpriteBank* pointer){pointer->clear();}

IRRLICHT_C_API void IGUISpriteBank_draw2DSprite(IGUISpriteBank* pointer, u32 index, const core::position2di& pos, const core::rect<s32>* clip = 0, const video::SColor& color = video::SColor(255,255,255,255), u32 starttime = 0, u32 currenttime = 0, bool loop = true, bool center = false)
{pointer->draw2DSprite(index, pos, clip, color, starttime, currenttime, loop, center);}

IRRLICHT_C_API void IGUISpriteBank_draw2DSpriteBatch(IGUISpriteBank* pointer, const core::array<u32>& indices, const core::array<core::position2di>& pos, const core::rect<s32>* clip = 0, const video::SColor& color = video::SColor(255,255,255,255), u32 starttime = 0, u32 currenttime = 0, bool loop = true, bool center = false)
{pointer->draw2DSpriteBatch(indices, pos, clip, color, starttime, currenttime, loop, center);}

#ifdef __cplusplus
}
#endif

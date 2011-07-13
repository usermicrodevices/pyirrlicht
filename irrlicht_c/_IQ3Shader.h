// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//struct Q3LevelLoadParameter
IRRLICHT_C_API Q3LevelLoadParameter* Q3LevelLoadParameter_ctor1(){return new Q3LevelLoadParameter();}
IRRLICHT_C_API Q3LevelLoadParameter* Q3LevelLoadParameter_ctor2(int length = 1){Q3LevelLoadParameter* pointer; pointer = new Q3LevelLoadParameter[length]; return pointer;}

IRRLICHT_C_API Q3LevelLoadParameter* Q3LevelLoadParameter_get_item(Q3LevelLoadParameter* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void Q3LevelLoadParameter_set_item(Q3LevelLoadParameter* pointer, Q3LevelLoadParameter* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API video::E_MATERIAL_TYPE Q3LevelLoadParameter_get_defaultLightMapMaterial(Q3LevelLoadParameter* pointer){return pointer->defaultLightMapMaterial;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_defaultLightMapMaterial(Q3LevelLoadParameter* pointer, video::E_MATERIAL_TYPE value){pointer->defaultLightMapMaterial = value;}

IRRLICHT_C_API video::E_MODULATE_FUNC Q3LevelLoadParameter_get_defaultModulate(Q3LevelLoadParameter* pointer){return pointer->defaultModulate;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_defaultModulate(Q3LevelLoadParameter* pointer, video::E_MODULATE_FUNC value){pointer->defaultModulate = value;}

IRRLICHT_C_API video::E_MATERIAL_FLAG Q3LevelLoadParameter_get_defaultFilter(Q3LevelLoadParameter* pointer){return pointer->defaultFilter;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_defaultFilter(Q3LevelLoadParameter* pointer, video::E_MATERIAL_FLAG value){pointer->defaultFilter = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_patchTesselation(Q3LevelLoadParameter* pointer){return pointer->patchTesselation;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_patchTesselation(Q3LevelLoadParameter* pointer, s32 value){pointer->patchTesselation = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_verbose(Q3LevelLoadParameter* pointer){return pointer->verbose;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_verbose(Q3LevelLoadParameter* pointer, s32 value){pointer->verbose = value;}

IRRLICHT_C_API u32 Q3LevelLoadParameter_get_startTime(Q3LevelLoadParameter* pointer){return pointer->startTime;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_startTime(Q3LevelLoadParameter* pointer, u32 value){pointer->startTime = value;}

IRRLICHT_C_API u32 Q3LevelLoadParameter_get_endTime(Q3LevelLoadParameter* pointer){return pointer->endTime;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_endTime(Q3LevelLoadParameter* pointer, u32 value){pointer->endTime = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_mergeShaderBuffer(Q3LevelLoadParameter* pointer){return pointer->mergeShaderBuffer;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_mergeShaderBuffer(Q3LevelLoadParameter* pointer, s32 value){pointer->mergeShaderBuffer = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_cleanUnResolvedMeshes(Q3LevelLoadParameter* pointer){return pointer->cleanUnResolvedMeshes;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_cleanUnResolvedMeshes(Q3LevelLoadParameter* pointer, s32 value){pointer->cleanUnResolvedMeshes = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_loadAllShaders(Q3LevelLoadParameter* pointer){return pointer->loadAllShaders;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_loadAllShaders(Q3LevelLoadParameter* pointer, s32 value){pointer->loadAllShaders = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_loadSkyShader(Q3LevelLoadParameter* pointer){return pointer->loadSkyShader;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_loadSkyShader(Q3LevelLoadParameter* pointer, s32 value){pointer->loadSkyShader = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_alpharef(Q3LevelLoadParameter* pointer){return pointer->alpharef;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_alpharef(Q3LevelLoadParameter* pointer, s32 value){pointer->alpharef = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_swapLump(Q3LevelLoadParameter* pointer){return pointer->swapLump;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_swapLump(Q3LevelLoadParameter* pointer, s32 value){pointer->swapLump = value;}

IRRLICHT_C_API s32 Q3LevelLoadParameter_get_swapHeader(Q3LevelLoadParameter* pointer){return pointer->swapHeader;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_swapHeader(Q3LevelLoadParameter* pointer, s32 value){pointer->swapHeader = value;}

IRRLICHT_C_API c8* Q3LevelLoadParameter_get_scriptDir(Q3LevelLoadParameter* pointer){return pointer->scriptDir;}
IRRLICHT_C_API void Q3LevelLoadParameter_set_scriptDir(Q3LevelLoadParameter* pointer, c8 value[64]){for(int i = 0; i < 64; i++) pointer->scriptDir[i] = value[i];}

IRRLICHT_C_API unsigned int Q3LevelLoadParameter_size(Q3LevelLoadParameter* pointer){return sizeof(pointer);}


//struct SBlendFunc
IRRLICHT_C_API SBlendFunc* SBlendFunc_ctor(video::E_MODULATE_FUNC mod){return new SBlendFunc(mod);}
//IRRLICHT_C_API SBlendFunc* SBlendFunc_ctor2(int length = 1){SBlendFunc* pointer; pointer = new SBlendFunc[length]; return pointer;}

IRRLICHT_C_API SBlendFunc* SBlendFunc_get_item(SBlendFunc* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SBlendFunc_set_item(SBlendFunc* pointer, SBlendFunc* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API video::E_MATERIAL_TYPE SBlendFunc_get_type(SBlendFunc* pointer){return pointer->type;}
IRRLICHT_C_API void SBlendFunc_set_type(SBlendFunc* pointer, video::E_MATERIAL_TYPE value){pointer->type = value;}

IRRLICHT_C_API video::E_MODULATE_FUNC SBlendFunc_get_modulate(SBlendFunc* pointer){return pointer->modulate;}
IRRLICHT_C_API void SBlendFunc_set_modulate(SBlendFunc* pointer, video::E_MODULATE_FUNC value){pointer->modulate = value;}

IRRLICHT_C_API f32 SBlendFunc_get_param0(SBlendFunc* pointer){return pointer->param0;}
IRRLICHT_C_API void SBlendFunc_set_param0(SBlendFunc* pointer, f32 value){pointer->param0 = value;}

IRRLICHT_C_API u32 SBlendFunc_get_isTransparent(SBlendFunc* pointer){return pointer->isTransparent;}
IRRLICHT_C_API void SBlendFunc_set_isTransparent(SBlendFunc* pointer, u32 value){pointer->isTransparent = value;}


//struct Noiser
IRRLICHT_C_API Noiser* Noiser_ctor1(){return new Noiser();}
IRRLICHT_C_API Noiser* Noiser_ctor2(int length = 1){Noiser* pointer; pointer = new Noiser[length]; return pointer;}

IRRLICHT_C_API Noiser* Noiser_get_item(Noiser* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void Noiser_set_item(Noiser* pointer, Noiser* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API f32 Noiser_get(Noiser* pointer){return pointer->get();}


//struct SModifierFunction
IRRLICHT_C_API SModifierFunction* SModifierFunction_ctor1(){return new SModifierFunction();}
IRRLICHT_C_API SModifierFunction* SModifierFunction_ctor2(int length = 1){SModifierFunction* pointer; pointer = new SModifierFunction[length]; return pointer;}

IRRLICHT_C_API SModifierFunction* SModifierFunction_get_item(SModifierFunction* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SModifierFunction_set_item(SModifierFunction* pointer, SModifierFunction* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_masterfunc0(SModifierFunction* pointer){return pointer->masterfunc0;}
IRRLICHT_C_API void SModifierFunction_set_masterfunc0(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->masterfunc0 = value;}
IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_masterfunc1(SModifierFunction* pointer){return pointer->masterfunc1;}
IRRLICHT_C_API void SModifierFunction_set_masterfunc1(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->masterfunc1 = value;}
IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_func(SModifierFunction* pointer){return pointer->func;}
IRRLICHT_C_API void SModifierFunction_set_func(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->func = value;}
IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_tcgen(SModifierFunction* pointer){return pointer->tcgen;}
IRRLICHT_C_API void SModifierFunction_set_tcgen(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->tcgen = value;}
IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_rgbgen(SModifierFunction* pointer){return pointer->rgbgen;}
IRRLICHT_C_API void SModifierFunction_set_rgbgen(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->rgbgen = value;}
IRRLICHT_C_API eQ3ModifierFunction SModifierFunction_get_alphagen(SModifierFunction* pointer){return pointer->alphagen;}
IRRLICHT_C_API void SModifierFunction_set_alphagen(SModifierFunction* pointer, eQ3ModifierFunction value){pointer->alphagen = value;}

IRRLICHT_C_API f32 SModifierFunction_get_base(SModifierFunction* pointer){return pointer->base;}
IRRLICHT_C_API void SModifierFunction_set_base(SModifierFunction* pointer, f32 value){pointer->base = value;}
IRRLICHT_C_API f32 SModifierFunction_get_bulgewidth(SModifierFunction* pointer){return pointer->bulgewidth;}
IRRLICHT_C_API void SModifierFunction_set_bulgewidth(SModifierFunction* pointer, f32 value){pointer->bulgewidth = value;}
IRRLICHT_C_API f32 SModifierFunction_get_amp(SModifierFunction* pointer){return pointer->amp;}
IRRLICHT_C_API void SModifierFunction_set_amp(SModifierFunction* pointer, f32 value){pointer->amp = value;}
IRRLICHT_C_API f32 SModifierFunction_get_bulgeheight(SModifierFunction* pointer){return pointer->bulgeheight;}
IRRLICHT_C_API void SModifierFunction_set_bulgeheight(SModifierFunction* pointer, f32 value){pointer->bulgeheight = value;}

IRRLICHT_C_API f32 SModifierFunction_get_phase(SModifierFunction* pointer){return pointer->phase;}
IRRLICHT_C_API void SModifierFunction_set_phase(SModifierFunction* pointer, f32 value){pointer->phase = value;}

IRRLICHT_C_API f32 SModifierFunction_get_frequency(SModifierFunction* pointer){return pointer->frequency;}
IRRLICHT_C_API void SModifierFunction_set_frequency(SModifierFunction* pointer, f32 value){pointer->frequency = value;}
IRRLICHT_C_API f32 SModifierFunction_get_bulgespeed(SModifierFunction* pointer){return pointer->bulgespeed;}
IRRLICHT_C_API void SModifierFunction_set_bulgespeed(SModifierFunction* pointer, f32 value){pointer->bulgespeed = value;}
IRRLICHT_C_API f32 SModifierFunction_get_wave(SModifierFunction* pointer){return pointer->wave;}
IRRLICHT_C_API void SModifierFunction_set_wave(SModifierFunction* pointer, f32 value){pointer->wave = value;}
IRRLICHT_C_API f32 SModifierFunction_get_div(SModifierFunction* pointer){return pointer->div;}
IRRLICHT_C_API void SModifierFunction_set_div(SModifierFunction* pointer, f32 value){pointer->div = value;}

IRRLICHT_C_API f32 SModifierFunction_get_x(SModifierFunction* pointer){return pointer->x;}
IRRLICHT_C_API void SModifierFunction_set_x(SModifierFunction* pointer, f32 value){pointer->x = value;}
IRRLICHT_C_API f32 SModifierFunction_get_y(SModifierFunction* pointer){return pointer->y;}
IRRLICHT_C_API void SModifierFunction_set_y(SModifierFunction* pointer, f32 value){pointer->y = value;}
IRRLICHT_C_API f32 SModifierFunction_get_z(SModifierFunction* pointer){return pointer->z;}
IRRLICHT_C_API void SModifierFunction_set_z(SModifierFunction* pointer, f32 value){pointer->z = value;}

IRRLICHT_C_API u32 SModifierFunction_get_count(SModifierFunction* pointer){return pointer->count;}
IRRLICHT_C_API void SModifierFunction_set_count(SModifierFunction* pointer, u32 value){pointer->count = value;}

IRRLICHT_C_API const f32 SModifierFunction_evaluate(SModifierFunction* pointer, f32 dt){return pointer->evaluate(dt);}


//struct SVariable
IRRLICHT_C_API SVariable* SVariable_ctor(const c8* n, const c8* c = 0){return new SVariable(n, c);}
//IRRLICHT_C_API SVariable* SVariable_ctor2(int length = 1){SVariable* pointer; pointer = new SVariable[length]; return pointer;}

IRRLICHT_C_API SVariable* SVariable_get_item(SVariable* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SVariable_set_item(SVariable* pointer, SVariable* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API const c8* SVariable_get_name(SVariable* pointer){return pointer->name.c_str();}
IRRLICHT_C_API void SVariable_set_name(SVariable* pointer, const c8* value){pointer->name = core::stringc(value);}

IRRLICHT_C_API const c8* SVariable_get_content(SVariable* pointer){return pointer->content.c_str();}
IRRLICHT_C_API void SVariable_set_content(SVariable* pointer, const c8* value){pointer->content = core::stringc(value);}

IRRLICHT_C_API void SVariable_clear(SVariable* pointer){pointer->clear();}
IRRLICHT_C_API const s32 SVariable_isValid(SVariable* pointer){return pointer->isValid();}
IRRLICHT_C_API const bool SVariable_operator_eq(SVariable* pointer, const SVariable* other){return pointer->operator==(*other);}
IRRLICHT_C_API const bool SVariable_operator_lt(SVariable* pointer, const SVariable* other){return pointer->operator<(*other);}


//struct SVarGroup
IRRLICHT_C_API SVarGroup* SVarGroup_ctor1(){return new SVarGroup();}
IRRLICHT_C_API SVarGroup* SVarGroup_ctor2(int length = 1){SVarGroup* pointer; pointer = new SVarGroup[length]; return pointer;}

IRRLICHT_C_API SVarGroup* SVarGroup_get_item(SVarGroup* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SVarGroup_set_item(SVarGroup* pointer, SVarGroup* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API const u32 SVarGroup_isDefined(SVarGroup* pointer, const c8* name, const c8* content = 0){return pointer->isDefined(name, content);}
IRRLICHT_C_API const c8* SVarGroup_get(SVarGroup* pointer, const c8* name){return pointer->get(name).c_str();}
IRRLICHT_C_API void SVarGroup_set(SVarGroup* pointer, const c8* name, const c8* content = 0){return pointer->set(name, content);}

IRRLICHT_C_API core::array<SVariable>* SVarGroup_get_Variable(SVarGroup* pointer){return &pointer->Variable;}
IRRLICHT_C_API void SVarGroup_set_Variable(SVarGroup* pointer, core::array<SVariable>* value){pointer->Variable = *value;}



//struct SVarGroupList: public IReferenceCounted
IRRLICHT_C_API SVarGroupList* SVarGroupList_ctor1(){return new SVarGroupList();}
IRRLICHT_C_API SVarGroupList* SVarGroupList_ctor2(int length = 1){SVarGroupList* pointer; pointer = new SVarGroupList[length]; return pointer;}

IRRLICHT_C_API SVarGroupList* SVarGroupList_get_item(SVarGroupList* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void SVarGroupList_set_item(SVarGroupList* pointer, SVarGroupList* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API core::array<SVarGroup>* SVarGroupList_get_VariableGroup(SVarGroupList* pointer){return &pointer->VariableGroup;}
IRRLICHT_C_API void SVarGroupList_set_VariableGroup(SVarGroupList* pointer, core::array<SVarGroup>* value){pointer->VariableGroup = *value;}


//struct IShader
IRRLICHT_C_API IShader* IShader_ctor1(){return new IShader();}
IRRLICHT_C_API IShader* IShader_ctor2(int length = 1){IShader* pointer; pointer = new IShader[length]; return pointer;}

IRRLICHT_C_API IShader* IShader_get_item(IShader* pointer, int index = 0){return &pointer[index];}
IRRLICHT_C_API void IShader_set_item(IShader* pointer, IShader* item, int index = 0){pointer[index] = *item;}

IRRLICHT_C_API void IShader_operator_set(IShader* pointer, const IShader* other){pointer->operator=(*other);}
IRRLICHT_C_API bool IShader_operator_eq(IShader* pointer, const IShader* other){return pointer->operator==(*other);}
IRRLICHT_C_API bool IShader_operator_lt(IShader* pointer, const IShader* other){return pointer->operator<(*other);}
IRRLICHT_C_API u32 IShader_getGroupSize(IShader* pointer){return pointer->getGroupSize();}
IRRLICHT_C_API const SVarGroup* IShader_getGroup(IShader* pointer, u32 stage){return pointer->getGroup(stage);}
IRRLICHT_C_API s32 IShader_get_ID(IShader* pointer){return pointer->ID;}
IRRLICHT_C_API void IShader_set_ID(IShader* pointer, s32 value){pointer->ID = value;}
IRRLICHT_C_API SVarGroupList* IShader_get_VarGroup(IShader* pointer){return pointer->VarGroup;}
IRRLICHT_C_API void IShader_set_VarGroup(IShader* pointer, SVarGroupList* value){pointer->VarGroup = value;}
IRRLICHT_C_API const c8* IShader_get_name(IShader* pointer){return pointer->name.c_str();}
IRRLICHT_C_API void IShader_set_name(IShader* pointer, const c8* value){pointer->name = core::stringc(value);}

//================= tQ3EntityList
IRRLICHT_C_API tQ3EntityList* tQ3EntityList_ctor(){return new tQ3EntityList();}
IRRLICHT_C_API void tQ3EntityList_reallocate(tQ3EntityList* pointer, u32 new_size){pointer->reallocate(new_size);}
IRRLICHT_C_API void tQ3EntityList_setAllocStrategy(tQ3EntityList* pointer, eAllocStrategy newStrategy = ALLOC_STRATEGY_DOUBLE){pointer->setAllocStrategy(newStrategy);}
IRRLICHT_C_API void tQ3EntityList_push_back(tQ3EntityList* pointer, IEntity* element){pointer->push_back(*element);}
IRRLICHT_C_API void tQ3EntityList_push_front(tQ3EntityList* pointer, IEntity* element){pointer->push_front(*element);}
IRRLICHT_C_API void tQ3EntityList_insert(tQ3EntityList* pointer, IEntity* element, u32 index=0){pointer->insert(*element, index);}
IRRLICHT_C_API void tQ3EntityList_clear(tQ3EntityList* pointer){pointer->clear();}
IRRLICHT_C_API void tQ3EntityList_set_pointer(tQ3EntityList* pointer, IEntity* newPointer, u32 size, bool _is_sorted=false, bool _free_when_destroyed=true){pointer->set_pointer(newPointer, size, _is_sorted, _free_when_destroyed);}
IRRLICHT_C_API void tQ3EntityList_set_free_when_destroyed(tQ3EntityList* pointer, bool f){pointer->set_free_when_destroyed(f);}
IRRLICHT_C_API void tQ3EntityList_set_used(tQ3EntityList* pointer, u32 usedNow){pointer->set_used(usedNow);}
IRRLICHT_C_API IEntity* tQ3EntityList_get_item(tQ3EntityList* pointer, u32 index){return &pointer->operator[](index);}
IRRLICHT_C_API u32 tQ3EntityList_size(tQ3EntityList* pointer){return pointer->size();}
IRRLICHT_C_API bool tQ3EntityList_empty(tQ3EntityList* pointer){return pointer->empty();}
IRRLICHT_C_API void tQ3EntityList_sort(tQ3EntityList* pointer){pointer->sort();}
IRRLICHT_C_API s32 tQ3EntityList_binary_search1(tQ3EntityList* pointer, IEntity* element){return pointer->binary_search(*element);}
IRRLICHT_C_API s32 tQ3EntityList_binary_search2(tQ3EntityList* pointer, IEntity* element, s32 left, s32 right){return pointer->binary_search(*element, left, right);}
IRRLICHT_C_API s32 tQ3EntityList_binary_search_multi(tQ3EntityList* pointer, IEntity* element, s32& last){return pointer->binary_search_multi(*element, last);}
IRRLICHT_C_API s32 tQ3EntityList_linear_search(tQ3EntityList* pointer, IEntity* element){return pointer->linear_search(*element);}
IRRLICHT_C_API s32 tQ3EntityList_linear_reverse_search(tQ3EntityList* pointer, IEntity* element){return pointer->linear_reverse_search(*element);}
IRRLICHT_C_API void tQ3EntityList_erase1(tQ3EntityList* pointer, u32 index){pointer->erase(index);}
IRRLICHT_C_API void tQ3EntityList_erase2(tQ3EntityList* pointer, u32 index, s32 count){pointer->erase(index, count);}
IRRLICHT_C_API void tQ3EntityList_set_sorted(tQ3EntityList* pointer, bool _is_sorted){pointer->set_sorted(_is_sorted);}
IRRLICHT_C_API void tQ3EntityList_swap(tQ3EntityList* pointer, tQ3EntityList* other){pointer->swap(*other);}

//tools
IRRLICHT_C_API core::vector3df* tool_getAsVector3df(const c8* string, u32& pos){return &getAsVector3df(core::stringc(string), pos);}
IRRLICHT_C_API f32 tool_getAsFloat(const c8* string, u32& pos){return getAsFloat(core::stringc(string), pos);}
//IRRLICHT_C_API tTexArray* tool_getTextures(const c8* name, u32& startPos, io::IFileSystem* fileSystem, video::IVideoDriver* driver)
//{
//	tTexArray* textures = new tTexArray();
//	getTextures(*textures, core::stringc(name), startPos, fileSystem, driver);
//	return textures;
//}
IRRLICHT_C_API void tool_getTextures(tTexArray* textures, const c8* name, u32& startPos, io::IFileSystem* fileSystem, video::IVideoDriver* driver){getTextures(*textures, core::stringc(name), startPos, fileSystem, driver);}

#ifdef __cplusplus
}
#endif

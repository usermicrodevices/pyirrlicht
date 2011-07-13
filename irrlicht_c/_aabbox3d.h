// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= aabbox3df
IRRLICHT_C_API aabbox3df* aabbox3df_ctor1(){return new aabbox3df();}
IRRLICHT_C_API aabbox3df* aabbox3df_ctor2(const vector3df& min, const vector3df& max){return new aabbox3df(min, max);}
IRRLICHT_C_API aabbox3df* aabbox3df_ctor3(const vector3df& init){return new aabbox3df(init);}
IRRLICHT_C_API aabbox3df* aabbox3df_ctor4(f32 minx=0.0f, f32 miny=0.0f, f32 minz=0.0f, f32 maxx=0.0f, f32 maxy=0.0f, f32 maxz=0.0f){return new aabbox3df(minx, miny, minz, maxx, maxy, maxz);}
IRRLICHT_C_API bool aabbox3df_operator_eq(aabbox3df* pointer, const aabbox3df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool aabbox3df_operator_ne(aabbox3df* pointer, const aabbox3df& other){return pointer->operator!=(other);}
IRRLICHT_C_API void aabbox3df_reset1(aabbox3df* pointer, f32 x, f32 y, f32 z){pointer->reset(x, y, z);}
IRRLICHT_C_API void aabbox3df_reset2(aabbox3df* pointer, const aabbox3df& initValue){pointer->reset(initValue);}
IRRLICHT_C_API void aabbox3df_reset3(aabbox3df* pointer, const vector3df& initValue){pointer->reset(initValue);}
IRRLICHT_C_API void aabbox3df_addInternalBox(aabbox3df* pointer, const aabbox3df& b){pointer->addInternalBox(b);}
IRRLICHT_C_API void aabbox3df_addInternalPoint1(aabbox3df* pointer, const vector3df& p){pointer->addInternalPoint(p);}
IRRLICHT_C_API void aabbox3df_addInternalPoint2(aabbox3df* pointer, f32 x, f32 y, f32 z){pointer->addInternalPoint(x, y, z);}
IRRLICHT_C_API vector3df* aabbox3df_getCenter(aabbox3df* pointer){return &pointer->getCenter();}
IRRLICHT_C_API vector3df* aabbox3df_getExtent(aabbox3df* pointer){return &pointer->getExtent();}
IRRLICHT_C_API bool aabbox3df_isEmpty(aabbox3df* pointer){return pointer->isEmpty();}
IRRLICHT_C_API f32 aabbox3df_getVolume(aabbox3df* pointer){return pointer->getVolume();}
IRRLICHT_C_API f32 aabbox3df_getArea(aabbox3df* pointer){return pointer->getArea();}
IRRLICHT_C_API void aabbox3df_getEdges(aabbox3df* pointer, vector3df* edges){pointer->getEdges(edges);}
IRRLICHT_C_API void aabbox3df_repair(aabbox3df* pointer){pointer->repair();}
IRRLICHT_C_API aabbox3df* aabbox3df_getInterpolated(aabbox3df* pointer, const aabbox3df& other, f32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API bool aabbox3df_isPointInside(aabbox3df* pointer, const vector3df& p){return pointer->isPointInside(p);}
IRRLICHT_C_API bool aabbox3df_isPointTotalInside(aabbox3df* pointer, const vector3df& p){return pointer->isPointTotalInside(p);}
IRRLICHT_C_API bool aabbox3df_isFullInside(aabbox3df* pointer, const aabbox3df& other){return pointer->isFullInside(other);}
IRRLICHT_C_API bool aabbox3df_intersectsWithBox(aabbox3df* pointer, const aabbox3df& other){return pointer->intersectsWithBox(other);}
IRRLICHT_C_API bool aabbox3df_intersectsWithLine1(aabbox3df* pointer, const line3df& line){return pointer->intersectsWithLine(line);}
IRRLICHT_C_API bool aabbox3df_intersectsWithLine2(aabbox3df* pointer, const vector3df& linemiddle, const vector3df& linevect, f32 halflength){return pointer->intersectsWithLine(linemiddle, linevect, halflength);}
IRRLICHT_C_API EIntersectionRelation3D aabbox3df_classifyPlaneRelation(aabbox3df* pointer, const plane3df& plane){return pointer->classifyPlaneRelation(plane);}
IRRLICHT_C_API vector3df* aabbox3df_get_MinEdge(aabbox3df* pointer){return &pointer->MinEdge;}
IRRLICHT_C_API void aabbox3df_set_MinEdge(aabbox3df* pointer, const vector3df& value){pointer->MinEdge = value;}
IRRLICHT_C_API vector3df* aabbox3df_get_MaxEdge(aabbox3df* pointer){return &pointer->MaxEdge;}
IRRLICHT_C_API void aabbox3df_set_MaxEdge(aabbox3df* pointer, const vector3df& value){pointer->MaxEdge = value;}

//================= aabbox3di
IRRLICHT_C_API aabbox3di* aabbox3di_ctor1(){return new aabbox3di();}
IRRLICHT_C_API aabbox3di* aabbox3di_ctor2(const vector3di& min, const vector3di& max){return new aabbox3di(min, max);}
IRRLICHT_C_API aabbox3di* aabbox3di_ctor3(const vector3di& init){return new aabbox3di(init);}
IRRLICHT_C_API aabbox3di* aabbox3di_ctor4(s32 minx=0, s32 miny=0, s32 minz=0, s32 maxx=0, s32 maxy=0, s32 maxz=0){return new aabbox3di(minx, miny, minz, maxx, maxy, maxz);}
IRRLICHT_C_API bool aabbox3di_operator_eq(aabbox3di* pointer, const aabbox3di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool aabbox3di_operator_ne(aabbox3di* pointer, const aabbox3di& other){return pointer->operator!=(other);}
IRRLICHT_C_API void aabbox3di_reset1(aabbox3di* pointer, s32 x, s32 y, s32 z){pointer->reset(x, y, z);}
IRRLICHT_C_API void aabbox3di_reset2(aabbox3di* pointer, const aabbox3di& initValue){pointer->reset(initValue);}
IRRLICHT_C_API void aabbox3di_reset3(aabbox3di* pointer, const vector3di& initValue){pointer->reset(initValue);}
IRRLICHT_C_API void aabbox3di_addInternalBox(aabbox3di* pointer, const aabbox3di& b){pointer->addInternalBox(b);}
IRRLICHT_C_API void aabbox3di_addInternalPoint1(aabbox3di* pointer, const vector3di& p){pointer->addInternalPoint(p);}
IRRLICHT_C_API void aabbox3di_addInternalPoint2(aabbox3di* pointer, s32 x, s32 y, s32 z){pointer->addInternalPoint(x, y, z);}
IRRLICHT_C_API vector3di* aabbox3di_getCenter(aabbox3di* pointer){return &pointer->getCenter();}
IRRLICHT_C_API vector3di* aabbox3di_getExtent(aabbox3di* pointer){return &pointer->getExtent();}
IRRLICHT_C_API bool aabbox3di_isEmpty(aabbox3di* pointer){return pointer->isEmpty();}
IRRLICHT_C_API s32 aabbox3di_getVolume(aabbox3di* pointer){return pointer->getVolume();}
IRRLICHT_C_API s32 aabbox3di_getArea(aabbox3di* pointer){return pointer->getArea();}
IRRLICHT_C_API void aabbox3di_getEdges(aabbox3di* pointer, vector3di* edges){pointer->getEdges(edges);}
IRRLICHT_C_API void aabbox3di_repair(aabbox3di* pointer){pointer->repair();}
IRRLICHT_C_API aabbox3di* aabbox3di_getInterpolated(aabbox3di* pointer, const aabbox3di& other, f32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API bool aabbox3di_isPointInside(aabbox3di* pointer, const vector3di& p){return pointer->isPointInside(p);}
IRRLICHT_C_API bool aabbox3di_isPointTotalInside(aabbox3di* pointer, const vector3di& p){return pointer->isPointTotalInside(p);}
IRRLICHT_C_API bool aabbox3di_isFullInside(aabbox3di* pointer, const aabbox3di& other){return pointer->isFullInside(other);}
IRRLICHT_C_API bool aabbox3di_intersectsWithBox(aabbox3di* pointer, const aabbox3di& other){return pointer->intersectsWithBox(other);}
//IRRLICHT_C_API bool aabbox3di_intersectsWithLine1(aabbox3di* pointer, const line3di& line){return pointer->intersectsWithLine(line);}
//IRRLICHT_C_API bool aabbox3di_intersectsWithLine2(aabbox3di* pointer, const vector3di& linemiddle, const vector3di& linevect, s32 halflength){return pointer->intersectsWithLine(linemiddle, linevect, halflength);}
IRRLICHT_C_API EIntersectionRelation3D aabbox3di_classifyPlaneRelation(aabbox3di* pointer, const plane3di& plane){return pointer->classifyPlaneRelation(plane);}
IRRLICHT_C_API vector3di* aabbox3di_get_MinEdge(aabbox3di* pointer){return &pointer->MinEdge;}
IRRLICHT_C_API void aabbox3di_set_MinEdge(aabbox3di* pointer, const vector3di& value){pointer->MinEdge = value;}
IRRLICHT_C_API vector3di* aabbox3di_get_MaxEdge(aabbox3di* pointer){return &pointer->MaxEdge;}
IRRLICHT_C_API void aabbox3di_set_MaxEdge(aabbox3di* pointer, const vector3di& value){pointer->MaxEdge = value;}

#ifdef __cplusplus
}
#endif

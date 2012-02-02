// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= line3df
IRRLICHT_C_API line3df* line3df_ctor1(){return new line3df();}
IRRLICHT_C_API line3df* line3df_ctor2(f32 xa, f32 ya, f32 za, f32 xb, f32 yb, f32 zb){return new line3df(xa, ya, za, xb, yb, zb);}
IRRLICHT_C_API line3df* line3df_ctor3(const vector3d<f32>& start, const vector3d<f32>& end){return new line3df(start, end);}
IRRLICHT_C_API vector3d<f32>* line3df_get_start(line3df* pointer){return &pointer->start;}
IRRLICHT_C_API vector3d<f32>* line3df_get_end(line3df* pointer){return &pointer->end;}
IRRLICHT_C_API void line3df_set_start(line3df* pointer, const vector3d<f32>& value){pointer->start = value;}
IRRLICHT_C_API void line3df_set_end(line3df* pointer, const vector3d<f32>& value){pointer->end = value;}
// operators
IRRLICHT_C_API line3df* line3df_add(line3df* pointer, const vector3df& point){return &pointer->operator+(point);}
IRRLICHT_C_API line3df& line3df_add_set(line3df* pointer, const vector3df& point){return pointer->operator+=(point);}
IRRLICHT_C_API line3df* line3df_sub(line3df* pointer, const vector3df& point){return &pointer->operator-(point);}
IRRLICHT_C_API line3df& line3df_sub_set(line3df* pointer, const vector3df& point){return pointer->operator-=(point);}
IRRLICHT_C_API bool line3df_eq(line3df* pointer, const line3df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool line3df_ne(line3df* pointer, const line3df& other){return pointer->operator!=(other);}
// functions
IRRLICHT_C_API void line3df_setLine1(line3df* pointer, const f32& xa, const f32& ya, const f32& za, const f32& xb, const f32& yb, const f32& zb){pointer->setLine(xa, ya, za, xb, yb, zb);}
IRRLICHT_C_API void line3df_setLine2(line3df* pointer, const vector3df& nstart, const vector3df& nend){pointer->setLine(nstart, nend);}
IRRLICHT_C_API void line3df_setLine3(line3df* pointer, const line3df& line){pointer->setLine(line);}
IRRLICHT_C_API f32 line3df_getLength(line3df* pointer){return pointer->getLength();}
IRRLICHT_C_API f32 line3df_getLengthSQ(line3df* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API vector3df* line3df_getMiddle(line3df* pointer){return new core::vector3df(pointer->getMiddle());}
IRRLICHT_C_API vector3df* line3df_getVector(line3df* pointer){return new core::vector3df(pointer->getVector());}
IRRLICHT_C_API bool line3df_isPointBetweenStartAndEnd(line3df* pointer, const vector3df& point){return pointer->isPointBetweenStartAndEnd(point);}
IRRLICHT_C_API vector3df* line3df_getClosestPoint(line3df* pointer, const vector3df& point){return &pointer->getClosestPoint(point);}
IRRLICHT_C_API bool line3df_getIntersectionWithSphere(line3df* pointer, const vector3df& sorigin, f32 sradius, f64& outdistance){return pointer->getIntersectionWithSphere(sorigin, sradius, outdistance);}

//================= line3di
IRRLICHT_C_API line3di* line3di_ctor1(){return new line3di();}
IRRLICHT_C_API line3di* line3di_ctor2(s32 xa, s32 ya, s32 za, s32 xb, s32 yb, s32 zb){return new line3di(xa, ya, za, xb, yb, zb);}
IRRLICHT_C_API line3di* line3di_ctor3(const vector3d<s32>& start, const vector3d<s32>& end){return new line3di(start, end);}
IRRLICHT_C_API vector3d<s32>* line3di_get_start(line3di* pointer){return &pointer->start;}
IRRLICHT_C_API vector3d<s32>* line3di_get_end(line3di* pointer){return &pointer->end;}
IRRLICHT_C_API void line3di_set_start(line3di* pointer, const vector3d<s32>& value){pointer->start = value;}
IRRLICHT_C_API void line3di_set_end(line3di* pointer, const vector3d<s32>& value){pointer->end = value;}
// operators
IRRLICHT_C_API line3di* line3di_add(line3di* pointer, const vector3di& point){return &pointer->operator+(point);}
IRRLICHT_C_API line3di& line3di_add_set(line3di* pointer, const vector3di& point){return pointer->operator+=(point);}
IRRLICHT_C_API line3di* line3di_sub(line3di* pointer, const vector3di& point){return &pointer->operator-(point);}
IRRLICHT_C_API line3di& line3di_sub_set(line3di* pointer, const vector3di& point){return pointer->operator-=(point);}
IRRLICHT_C_API bool line3di_eq(line3di* pointer, const line3di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool line3di_ne(line3di* pointer, const line3di& other){return pointer->operator!=(other);}
// functions
IRRLICHT_C_API void line3di_setLine1(line3di* pointer, const s32& xa, const s32& ya, const s32& za, const s32& xb, const s32& yb, const s32& zb){pointer->setLine(xa, ya, za, xb, yb, zb);}
IRRLICHT_C_API void line3di_setLine2(line3di* pointer, const vector3di& nstart, const vector3di& nend){pointer->setLine(nstart, nend);}
IRRLICHT_C_API void line3di_setLine3(line3di* pointer, const line3di& line){pointer->setLine(line);}
IRRLICHT_C_API s32 line3di_getLength(line3di* pointer){return pointer->getLength();}
IRRLICHT_C_API s32 line3di_getLengthSQ(line3di* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API vector3di* line3di_getMiddle(line3di* pointer){return new vector3di(pointer->getMiddle());}
IRRLICHT_C_API vector3di* line3di_getVector(line3di* pointer){return new vector3di(pointer->getVector());}
IRRLICHT_C_API bool line3di_isPointBetweenStartAndEnd(line3di* pointer, const vector3di& point){return pointer->isPointBetweenStartAndEnd(point);}
IRRLICHT_C_API vector3di* line3di_getClosestPoint(line3di* pointer, const vector3di& point){return &pointer->getClosestPoint(point);}
IRRLICHT_C_API bool line3di_getIntersectionWithSphere(line3di* pointer, const vector3di& sorigin, s32 sradius, f64& outdistance){return pointer->getIntersectionWithSphere(sorigin, sradius, outdistance);}

#ifdef __cplusplus
}
#endif

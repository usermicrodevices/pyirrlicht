// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= vector2df
IRRLICHT_C_API vector2df* vector2df_ctor1(f32 nx=0.0f, f32 ny=0.0f){return new vector2df(nx, ny);}
IRRLICHT_C_API vector2df* vector2df_ctor2(f32 n=0.0f){return new vector2df(n);}
IRRLICHT_C_API vector2df* vector2df_ctor3(const vector2df& other){return new vector2df(other);}
IRRLICHT_C_API vector2df* vector2df_ctor4(const dimension2df& other){return new vector2df(other);}
// operators
IRRLICHT_C_API vector2df* vector2df_operator_sub(vector2df* pointer){return &pointer->operator-();}
IRRLICHT_C_API vector2df& vector2df_operator_set_other(vector2df* pointer, const vector2df& other){return pointer->operator=(other);}
IRRLICHT_C_API vector2df& vector2df_operator_set_dimension2d(vector2df* pointer, const dimension2df& other){return pointer->operator=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_add_other(vector2df* pointer, const vector2df& other){return &pointer->operator+(other);}
IRRLICHT_C_API vector2df* vector2df_operator_add_dimension2d(vector2df* pointer, const dimension2df& other){return &pointer->operator+(other);}
IRRLICHT_C_API vector2df& vector2df_operator_set_add_other(vector2df* pointer, const vector2df& other){return pointer->operator+=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_add_value(vector2df* pointer, const f32 v){return &pointer->operator+(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_add_value(vector2df* pointer, const f32 v){return pointer->operator+=(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_add_dimension2d(vector2df* pointer, const dimension2df& other){return pointer->operator+=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_sub_other(vector2df* pointer, const vector2df& other){return &pointer->operator-(other);}
IRRLICHT_C_API vector2df* vector2df_operator_sub_dimension2d(vector2df* pointer, const dimension2df& other){return &pointer->operator-(other);}
IRRLICHT_C_API vector2df& vector2df_operator_set_sub_other(vector2df* pointer, const vector2df& other){return pointer->operator-=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_sub_value(vector2df* pointer, const f32 v){return &pointer->operator-(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_sub_value(vector2df* pointer, const f32 v){return pointer->operator-=(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_sub_dimension2d(vector2df* pointer, const dimension2df& other){return pointer->operator-=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_mult_other(vector2df* pointer, const vector2df& other){return &pointer->operator*(other);}
IRRLICHT_C_API vector2df& vector2df_operator_set_mult_other(vector2df* pointer, const vector2df& other){return pointer->operator*=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_mult_value(vector2df* pointer, const f32 v){return &pointer->operator*(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_mult_value(vector2df* pointer, const f32 v){return pointer->operator*=(v);}
IRRLICHT_C_API vector2df* vector2df_operator_div_other(vector2df* pointer, const vector2df& other){return &pointer->operator/(other);}
IRRLICHT_C_API vector2df& vector2df_operator_set_div_other(vector2df* pointer, const vector2df& other){return pointer->operator/=(other);}
IRRLICHT_C_API vector2df* vector2df_operator_div_value(vector2df* pointer, const f32 v){return &pointer->operator/(v);}
IRRLICHT_C_API vector2df& vector2df_operator_set_div_value(vector2df* pointer, const f32 v){return pointer->operator/=(v);}
IRRLICHT_C_API bool vector2df_operator_le(vector2df* pointer, const vector2df& other){return pointer->operator<=(other);}
IRRLICHT_C_API bool vector2df_operator_ge(vector2df* pointer, const vector2df& other){return pointer->operator>=(other);}
IRRLICHT_C_API bool vector2df_operator_lt(vector2df* pointer, const vector2df& other){return pointer->operator<(other);}
IRRLICHT_C_API bool vector2df_operator_gt(vector2df* pointer, const vector2df& other){return pointer->operator>(other);}
IRRLICHT_C_API bool vector2df_operator_eq(vector2df* pointer, const vector2df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool vector2df_operator_ne(vector2df* pointer, const vector2df& other){return pointer->operator!=(other);}
// functions
IRRLICHT_C_API bool vector2df_equals(vector2df* pointer, const vector2df& other){return pointer->equals(other);}
IRRLICHT_C_API vector2df& vector2df_set(vector2df* pointer, f32 nx, f32 ny){return pointer->set(nx, ny);}
IRRLICHT_C_API vector2df& vector2df_set2(vector2df* pointer, const vector2df& p){return pointer->set(p);}
IRRLICHT_C_API f32 vector2df_getLength(vector2df* pointer){return pointer->getLength();}
IRRLICHT_C_API f32 vector2df_getLengthSQ(vector2df* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API f32 vector2df_dotProduct(vector2df* pointer, const vector2df& other){return pointer->dotProduct(other);}
IRRLICHT_C_API f32 vector2df_getDistanceFrom(vector2df* pointer, const vector2df& other){return pointer->getDistanceFrom(other);}
IRRLICHT_C_API f32 vector2df_getDistanceFromSQ(vector2df* pointer, const vector2df& other){return pointer->getDistanceFromSQ(other);}
IRRLICHT_C_API vector2df& vector2df_rotateBy(vector2df* pointer, f32 degrees, const vector2df& center=vector2df()){return pointer->rotateBy(degrees, center);}
IRRLICHT_C_API vector2df& vector2df_normalize(vector2df* pointer){return pointer->normalize();}
IRRLICHT_C_API f64 vector2df_getAngleTrig(vector2df* pointer){return pointer->getAngleTrig();}
IRRLICHT_C_API f64 vector2df_getAngle(vector2df* pointer){return pointer->getAngle();}
IRRLICHT_C_API f64 vector2df_getAngleWith(vector2df* pointer, const vector2df& b){return pointer->getAngleWith(b);}
IRRLICHT_C_API bool vector2df_isBetweenPoints(vector2df* pointer, const vector2df& begin, const vector2df& end){return pointer->isBetweenPoints(begin, end);}
IRRLICHT_C_API vector2df* vector2df_getInterpolated(vector2df* pointer, const vector2df& other, f32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API vector2df* vector2df_getInterpolated_quadratic(vector2df* pointer, const vector2df& v2, const vector2df& v3, f32 d){return &pointer->getInterpolated_quadratic(v2, v3, d);}
IRRLICHT_C_API vector2df& vector2df_interpolate(vector2df* pointer, const vector2df& a, const vector2df& b, f32 d){return pointer->interpolate(a, b, d);}
IRRLICHT_C_API f32 vector2df_get_X(vector2df* pointer){return pointer->X;}
IRRLICHT_C_API void vector2df_set_X(vector2df* pointer, f32 value){pointer->X = value;}
IRRLICHT_C_API f32 vector2df_get_Y(vector2df* pointer){return pointer->Y;}
IRRLICHT_C_API void vector2df_set_Y(vector2df* pointer, f32 value){pointer->Y = value;}

//================= vector2di
IRRLICHT_C_API vector2di* vector2di_ctor1(s32 nx=0, s32 ny=0){return new vector2di(nx, ny);}
IRRLICHT_C_API vector2di* vector2di_ctor2(s32 n=0){return new vector2di(n);}
IRRLICHT_C_API vector2di* vector2di_ctor3(const vector2di& other){return new vector2di(other);}
IRRLICHT_C_API vector2di* vector2di_ctor4(const dimension2di& other){return new vector2di(other);}
// operators
IRRLICHT_C_API vector2di* vector2di_operator_sub(vector2di* pointer){return &pointer->operator-();}
IRRLICHT_C_API vector2di& vector2di_operator_set_other(vector2di* pointer, const vector2di& other){return pointer->operator=(other);}
IRRLICHT_C_API vector2di& vector2di_operator_set_dimension2d(vector2di* pointer, const dimension2di& other){return pointer->operator=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_add_other(vector2di* pointer, const vector2di& other){return &pointer->operator+(other);}
IRRLICHT_C_API vector2di* vector2di_operator_add_dimension2d(vector2di* pointer, const dimension2di& other){return &pointer->operator+(other);}
IRRLICHT_C_API vector2di& vector2di_operator_set_add_other(vector2di* pointer, const vector2di& other){return pointer->operator+=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_add_value(vector2di* pointer, const s32 v){return &pointer->operator+(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_add_value(vector2di* pointer, const s32 v){return pointer->operator+=(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_add_dimension2d(vector2di* pointer, const dimension2di& other){return pointer->operator+=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_sub_other(vector2di* pointer, const vector2di& other){return &pointer->operator-(other);}
IRRLICHT_C_API vector2di* vector2di_operator_sub_dimension2d(vector2di* pointer, const dimension2di& other){return &pointer->operator-(other);}
IRRLICHT_C_API vector2di& vector2di_operator_set_sub_other(vector2di* pointer, const vector2di& other){return pointer->operator-=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_sub_value(vector2di* pointer, const s32 v){return &pointer->operator-(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_sub_value(vector2di* pointer, const s32 v){return pointer->operator-=(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_sub_dimension2d(vector2di* pointer, const dimension2di& other){return pointer->operator-=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_mult_other(vector2di* pointer, const vector2di& other){return &pointer->operator*(other);}
IRRLICHT_C_API vector2di& vector2di_operator_set_mult_other(vector2di* pointer, const vector2di& other){return pointer->operator*=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_mult_value(vector2di* pointer, const s32 v){return &pointer->operator*(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_mult_value(vector2di* pointer, const s32 v){return pointer->operator*=(v);}
IRRLICHT_C_API vector2di* vector2di_operator_div_other(vector2di* pointer, const vector2di& other){return &pointer->operator/(other);}
IRRLICHT_C_API vector2di& vector2di_operator_set_div_other(vector2di* pointer, const vector2di& other){return pointer->operator/=(other);}
IRRLICHT_C_API vector2di* vector2di_operator_div_value(vector2di* pointer, const s32 v){return &pointer->operator/(v);}
IRRLICHT_C_API vector2di& vector2di_operator_set_div_value(vector2di* pointer, const s32 v){return pointer->operator/=(v);}
IRRLICHT_C_API bool vector2di_operator_le(vector2di* pointer, const vector2di& other){return pointer->operator<=(other);}
IRRLICHT_C_API bool vector2di_operator_ge(vector2di* pointer, const vector2di& other){return pointer->operator>=(other);}
IRRLICHT_C_API bool vector2di_operator_lt(vector2di* pointer, const vector2di& other){return pointer->operator<(other);}
IRRLICHT_C_API bool vector2di_operator_gt(vector2di* pointer, const vector2di& other){return pointer->operator>(other);}
IRRLICHT_C_API bool vector2di_operator_eq(vector2di* pointer, const vector2di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool vector2di_operator_ne(vector2di* pointer, const vector2di& other){return pointer->operator!=(other);}
// functions
IRRLICHT_C_API bool vector2di_equals(vector2di* pointer, const vector2di& other){return pointer->equals(other);}
IRRLICHT_C_API vector2di& vector2di_set(vector2di* pointer, s32 nx, s32 ny){return pointer->set(nx, ny);}
IRRLICHT_C_API vector2di& vector2di_set2(vector2di* pointer, const vector2di& p){return pointer->set(p);}
IRRLICHT_C_API s32 vector2di_getLength(vector2di* pointer){return pointer->getLength();}
IRRLICHT_C_API s32 vector2di_getLengthSQ(vector2di* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API s32 vector2di_dotProduct(vector2di* pointer, const vector2di& other){return pointer->dotProduct(other);}
IRRLICHT_C_API s32 vector2di_getDistanceFrom(vector2di* pointer, const vector2di& other){return pointer->getDistanceFrom(other);}
IRRLICHT_C_API s32 vector2di_getDistanceFromSQ(vector2di* pointer, const vector2di& other){return pointer->getDistanceFromSQ(other);}
IRRLICHT_C_API vector2di& vector2di_rotateBy(vector2di* pointer, s32 degrees, const vector2di& center=vector2di()){return pointer->rotateBy(degrees, center);}
IRRLICHT_C_API vector2di& vector2di_normalize(vector2di* pointer){return pointer->normalize();}
IRRLICHT_C_API f64 vector2di_getAngleTrig(vector2di* pointer){return pointer->getAngleTrig();}
//#ifdef defined(_WIN64)
IRRLICHT_C_API f64 vector2di_getAngle(vector2di* pointer){return pointer->getAngle();}
IRRLICHT_C_API f64 vector2di_getAngleWith(vector2di* pointer, const vector2di& b){return pointer->getAngleWith(b);}
//#else
//IRRLICHT_C_API s32 vector2di_getAngle(vector2di* pointer){return (s32)pointer->getAngle();}
//IRRLICHT_C_API s32 vector2di_getAngleWith(vector2di* pointer, const vector2di& b){return (s32)pointer->getAngleWith(b);}
//#endif
IRRLICHT_C_API bool vector2di_isBetweenPoints(vector2di* pointer, const vector2di& begin, const vector2di& end){return pointer->isBetweenPoints(begin, end);}
IRRLICHT_C_API vector2di* vector2di_getInterpolated(vector2di* pointer, const vector2di& other, s32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API vector2di* vector2di_getInterpolated_quadratic(vector2di* pointer, const vector2di& v2, const vector2di& v3, s32 d){return &pointer->getInterpolated_quadratic(v2, v3, d);}
IRRLICHT_C_API vector2di& vector2di_interpolate(vector2di* pointer, const vector2di& a, const vector2di& b, s32 d){return pointer->interpolate(a, b, d);}
IRRLICHT_C_API s32 vector2di_get_X(vector2di* pointer){return pointer->X;}
IRRLICHT_C_API void vector2di_set_X(vector2di* pointer, s32 value){pointer->X = value;}
IRRLICHT_C_API s32 vector2di_get_Y(vector2di* pointer){return pointer->Y;}
IRRLICHT_C_API void vector2di_set_Y(vector2di* pointer, s32 value){pointer->Y = value;}

//================= position2df
IRRLICHT_C_API position2df* position2df_ctor1(f32 nx=0.0f, f32 ny=0.0f){return new position2df(nx, ny);}
IRRLICHT_C_API position2df* position2df_ctor2(f32 n=0.0f){return new position2df(n);}
IRRLICHT_C_API position2df* position2df_ctor3(const vector2df& other){return new position2df(other);}
IRRLICHT_C_API position2df* position2df_ctor4(const dimension2df& other){return new position2df(other);}

//================= position2di
IRRLICHT_C_API position2di* position2di_ctor1(s32 nx=0, s32 ny=0){return new position2di(nx, ny);}
IRRLICHT_C_API position2di* position2di_ctor2(s32 n=0){return new position2di(n);}
IRRLICHT_C_API position2di* position2di_ctor3(const vector2di& other){return new position2di(other);}
IRRLICHT_C_API position2di* position2di_ctor4(const dimension2di& other){return new position2di(other);}

#ifdef __cplusplus
}
#endif

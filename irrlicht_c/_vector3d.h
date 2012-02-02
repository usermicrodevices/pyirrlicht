// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= vector3df
IRRLICHT_C_API vector3df* vector3df_ctor1(){return new vector3df();}
IRRLICHT_C_API vector3df* vector3df_ctor2(f32 x = 0.0f, f32 y = 0.0f, f32 z = 0.0f){return new vector3df(x, y, z);}
IRRLICHT_C_API vector3df* vector3df_ctor3(f32 n){return new vector3df(n);}
IRRLICHT_C_API vector3df* vector3df_ctor4(const vector3df* other){return new vector3df(*other);}
IRRLICHT_C_API void vector3df_set_X(vector3df* pointer, f32 value){pointer->X = value;}
IRRLICHT_C_API f32 vector3df_get_X(const vector3df* pointer){return pointer->X;}
IRRLICHT_C_API void vector3df_set_Y(vector3df* pointer, f32 value){pointer->Y = value;}
IRRLICHT_C_API f32 vector3df_get_Y(const vector3df* pointer){return pointer->Y;}
IRRLICHT_C_API void vector3df_set_Z(vector3df* pointer, f32 value){pointer->Z = value;}
IRRLICHT_C_API f32 vector3df_get_Z(const vector3df* pointer){return pointer->Z;}
IRRLICHT_C_API vector3df* vector3df_operator_sub(const vector3df* pointer){return new vector3df(pointer->operator-());}
IRRLICHT_C_API vector3df* vector3df_operator_set(vector3df* pointer, const vector3df* other){return &pointer->operator=(*other);}

IRRLICHT_C_API vector3df* vector3df_operator_add_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator+(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_set_add_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator+=(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_add_value(vector3df* pointer, const f32 val){return new vector3df(pointer->operator+(val));}
IRRLICHT_C_API vector3df* vector3df_operator_set_add_value(vector3df* pointer, const f32 val){return new vector3df(pointer->operator+=(val));}

IRRLICHT_C_API vector3df* vector3df_operator_sub_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator-(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_set_sub_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator-=(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_sub_value(vector3df* pointer, const f32 val){return new vector3df(pointer->operator-(val));}
IRRLICHT_C_API vector3df* vector3df_operator_set_sub_value(vector3df* pointer, const f32 val){return new vector3df(pointer->operator-=(val));}

IRRLICHT_C_API vector3df* vector3df_operator_mult_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator*(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_set_mult_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator*=(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_mult_value(vector3df* pointer, const f32 v){return new vector3df(pointer->operator*(v));}
IRRLICHT_C_API vector3df* vector3df_operator_set_mult_value(vector3df* pointer, const f32 v){return new vector3df(pointer->operator*=(v));}

IRRLICHT_C_API vector3df* vector3df_operator_div_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator/(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_set_div_other(vector3df* pointer, const vector3df* other){return new vector3df(pointer->operator/=(*other));}
IRRLICHT_C_API vector3df* vector3df_operator_div_value(vector3df* pointer, const f32 v){return new vector3df(pointer->operator/(v));}
IRRLICHT_C_API vector3df* vector3df_operator_set_div_value(vector3df* pointer, const f32 v){return new vector3df(pointer->operator/=(v));}

IRRLICHT_C_API bool vector3df_operator_le(vector3df* pointer, const vector3df* other){return pointer->operator<=(*other);}
IRRLICHT_C_API bool vector3df_operator_ge(vector3df* pointer, const vector3df* other){return pointer->operator>=(*other);}
IRRLICHT_C_API bool vector3df_operator_lt(vector3df* pointer, const vector3df* other){return pointer->operator<(*other);}
IRRLICHT_C_API bool vector3df_operator_gt(vector3df* pointer, const vector3df* other){return pointer->operator>(*other);}
IRRLICHT_C_API bool vector3df_operator_eq(vector3df* pointer, const vector3df* other){return pointer->operator==(*other);}
IRRLICHT_C_API bool vector3df_operator_ne(vector3df* pointer, const vector3df* other){return pointer->operator!=(*other);}

IRRLICHT_C_API bool vector3df_equals(vector3df* pointer, const vector3df* other, const f32 tolerance = (f32)ROUNDING_ERROR_f32){return pointer->equals(*other, tolerance);}
IRRLICHT_C_API vector3df* vector3df_set1(vector3df* pointer, const f32 nx, const f32 ny, const f32 nz){return &pointer->set(nx, ny, nz);}
IRRLICHT_C_API vector3df* vector3df_set2(vector3df* pointer, const vector3df* p){return &pointer->set(*p);}
IRRLICHT_C_API f32 vector3df_getLength(vector3df* pointer){return pointer->getLength();}
IRRLICHT_C_API f32 vector3df_getLengthSQ(vector3df* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API f32 vector3df_dotProduct(vector3df* pointer, const vector3df* other){return pointer->dotProduct(*other);}
IRRLICHT_C_API f32 vector3df_getDistanceFrom(vector3df* pointer, const vector3df* other){return pointer->getDistanceFrom(*other);}
IRRLICHT_C_API f32 vector3df_getDistanceFromSQ(vector3df* pointer, const vector3df* other){return pointer->getDistanceFromSQ(*other);}
IRRLICHT_C_API vector3df* vector3df_crossProduct(vector3df* pointer, const vector3df* p){return new vector3df(pointer->crossProduct(*p));}
IRRLICHT_C_API bool vector3df_isBetweenPoints(vector3df* pointer, const vector3df* begin, const vector3df* end){return pointer->isBetweenPoints(*begin, *end);}
IRRLICHT_C_API vector3df* vector3df_normalize(vector3df* pointer){return new vector3df(pointer->normalize());}
IRRLICHT_C_API vector3df* vector3df_setLength(vector3df* pointer, f32 newlength){return new vector3df(pointer->setLength(newlength));}
IRRLICHT_C_API vector3df* vector3df_invert(vector3df* pointer){return &pointer->invert();}
IRRLICHT_C_API void vector3df_rotateXZBy(vector3df* pointer, f32 degrees, const vector3df* center){pointer->rotateXZBy(degrees, *center);}
IRRLICHT_C_API void vector3df_rotateXYBy(vector3df* pointer, f32 degrees, const vector3df* center){pointer->rotateXYBy(degrees, *center);}
IRRLICHT_C_API void vector3df_rotateYZBy(vector3df* pointer, f32 degrees, const vector3df* center){pointer->rotateYZBy(degrees, *center);}
IRRLICHT_C_API vector3df* vector3df_getInterpolated(vector3df* pointer, const vector3df* other, f32 d){return new vector3df(pointer->getInterpolated(*other, d));}
IRRLICHT_C_API vector3df* vector3df_getInterpolated_quadratic(vector3df* pointer, const vector3df* v2, const vector3df* v3, f32 d){return new vector3df(pointer->getInterpolated_quadratic(*v2, *v3, d));}
IRRLICHT_C_API vector3df* vector3df_interpolate(vector3df* pointer, const vector3df* a, const vector3df* b, f32 d){return new vector3df(pointer->interpolate(*a, *b, d));}
IRRLICHT_C_API vector3df* vector3df_getHorizontalAngle(vector3df* pointer){return new vector3df(pointer->getHorizontalAngle());}
IRRLICHT_C_API vector3df* vector3df_getSphericalCoordinateAngles(vector3df* pointer){return new vector3df(pointer->getSphericalCoordinateAngles());}
IRRLICHT_C_API vector3df* vector3df_rotationToDirection(vector3df* pointer, const vector3df& forwards = vector3df(0, 0, 1)){return new vector3df(pointer->rotationToDirection(forwards));}
IRRLICHT_C_API void vector3df_getAs4Values(vector3df* pointer, f32* array){pointer->getAs4Values(array);}


//================= vector3di
IRRLICHT_C_API vector3di* vector3di_ctor1(){return new vector3di();}
IRRLICHT_C_API vector3di* vector3di_ctor2(s32 x=0, s32 y=0, s32 z=0){return new vector3di(x, y, z);}
IRRLICHT_C_API vector3di* vector3di_ctor3(s32 n){return new vector3di(n);}
IRRLICHT_C_API vector3di* vector3di_ctor4(const vector3di* other){return new vector3di(*other);}
IRRLICHT_C_API void vector3di_set_X(vector3di* pointer, s32 value){pointer->X = value;}
IRRLICHT_C_API s32 vector3di_get_X(const vector3di* pointer){return pointer->X;}
IRRLICHT_C_API void vector3di_set_Y(vector3di* pointer, s32 value){pointer->Y = value;}
IRRLICHT_C_API s32 vector3di_get_Y(const vector3di* pointer){return pointer->Y;}
IRRLICHT_C_API void vector3di_set_Z(vector3di* pointer, s32 value){pointer->Z = value;}
IRRLICHT_C_API s32 vector3di_get_Z(const vector3di* pointer){return pointer->Z;}
IRRLICHT_C_API vector3di* vector3di_operator_sub(const vector3di* pointer){return new vector3di(pointer->operator-());}
IRRLICHT_C_API vector3di* vector3di_operator_set(vector3di* pointer, const vector3di* other){return &pointer->operator=(*other);}

IRRLICHT_C_API vector3di* vector3di_operator_add_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator+(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_set_add_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator+=(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_add_value(vector3di* pointer, const s32 val){return new vector3di(pointer->operator+(val));}
IRRLICHT_C_API vector3di* vector3di_operator_set_add_value(vector3di* pointer, const s32 val){return new vector3di(pointer->operator+=(val));}

IRRLICHT_C_API vector3di* vector3di_operator_sub_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator-(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_set_sub_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator-=(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_sub_value(vector3di* pointer, const s32 val){return new vector3di(pointer->operator-(val));}
IRRLICHT_C_API vector3di* vector3di_operator_set_sub_value(vector3di* pointer, const s32 val){return new vector3di(pointer->operator-=(val));}

IRRLICHT_C_API vector3di* vector3di_operator_mult_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator*(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_set_mult_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator*=(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_mult_value(vector3di* pointer, const s32 v){return new vector3di(pointer->operator*(v));}
IRRLICHT_C_API vector3di* vector3di_operator_set_mult_value(vector3di* pointer, const s32 v){return new vector3di(pointer->operator*=(v));}

IRRLICHT_C_API vector3di* vector3di_operator_div_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator/(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_set_div_other(vector3di* pointer, const vector3di* other){return new vector3di(pointer->operator/=(*other));}
IRRLICHT_C_API vector3di* vector3di_operator_div_value(vector3di* pointer, const s32 v){return new vector3di(pointer->operator/(v));}
IRRLICHT_C_API vector3di* vector3di_operator_set_div_value(vector3di* pointer, const s32 v){return new vector3di(pointer->operator/=(v));}

IRRLICHT_C_API bool vector3di_operator_le(vector3di* pointer, const vector3di* other){return pointer->operator<=(*other);}
IRRLICHT_C_API bool vector3di_operator_ge(vector3di* pointer, const vector3di* other){return pointer->operator>=(*other);}
IRRLICHT_C_API bool vector3di_operator_lt(vector3di* pointer, const vector3di* other){return pointer->operator<(*other);}
IRRLICHT_C_API bool vector3di_operator_gt(vector3di* pointer, const vector3di* other){return pointer->operator>(*other);}
IRRLICHT_C_API bool vector3di_operator_eq(vector3di* pointer, const vector3di* other){return pointer->operator==(*other);}
IRRLICHT_C_API bool vector3di_operator_ne(vector3di* pointer, const vector3di* other){return pointer->operator!=(*other);}

IRRLICHT_C_API bool vector3di_equals(vector3di* pointer, const vector3di* other, const s32 tolerance = (s32)ROUNDING_ERROR_S32){return pointer->equals(*other, tolerance);}
IRRLICHT_C_API vector3di* vector3di_set1(vector3di* pointer, const s32 nx, const s32 ny, const s32 nz){return new vector3di(pointer->set(nx, ny, nz));}
IRRLICHT_C_API vector3di* vector3di_set2(vector3di* pointer, const vector3di* p){return new vector3di(pointer->set(*p));}
IRRLICHT_C_API s32 vector3di_getLength(vector3di* pointer){return pointer->getLength();}
IRRLICHT_C_API s32 vector3di_getLengthSQ(vector3di* pointer){return pointer->getLengthSQ();}
IRRLICHT_C_API s32 vector3di_dotProduct(vector3di* pointer, const vector3di* other){return pointer->dotProduct(*other);}
IRRLICHT_C_API s32 vector3di_getDistanceFrom(vector3di* pointer, const vector3di* other){return pointer->getDistanceFrom(*other);}
IRRLICHT_C_API s32 vector3di_getDistanceFromSQ(vector3di* pointer, const vector3di* other){return pointer->getDistanceFromSQ(*other);}
IRRLICHT_C_API vector3di* vector3di_crossProduct(vector3di* pointer, const vector3di* p){return new vector3di(pointer->crossProduct(*p));}
IRRLICHT_C_API bool vector3di_isBetweenPoints(vector3di* pointer, const vector3di* begin, const vector3di* end){return pointer->isBetweenPoints(*begin, *end);}
IRRLICHT_C_API vector3di* vector3di_normalize(vector3di* pointer){return new vector3di(pointer->normalize());}
IRRLICHT_C_API vector3di* vector3di_setLength(vector3di* pointer, s32 newlength){return new vector3di(pointer->setLength(newlength));}
IRRLICHT_C_API vector3di* vector3di_invert(vector3di* pointer){return new vector3di(pointer->invert());}
IRRLICHT_C_API void vector3di_rotateXZBy(vector3di* pointer, s32 degrees, const vector3di* center){pointer->rotateXZBy(degrees, *center);}
IRRLICHT_C_API void vector3di_rotateXYBy(vector3di* pointer, s32 degrees, const vector3di* center){pointer->rotateXYBy(degrees, *center);}
IRRLICHT_C_API void vector3di_rotateYZBy(vector3di* pointer, s32 degrees, const vector3di* center){pointer->rotateYZBy(degrees, *center);}
IRRLICHT_C_API vector3di* vector3di_getInterpolated(vector3di* pointer, const vector3di* other, s32 d){return new vector3di(pointer->getInterpolated(*other, d));}
IRRLICHT_C_API vector3di* vector3di_getInterpolated_quadratic(vector3di* pointer, const vector3di* v2, const vector3di* v3, s32 d){return new vector3di(pointer->getInterpolated_quadratic(*v2, *v3, d));}
IRRLICHT_C_API vector3di* vector3di_interpolate(vector3di* pointer, const vector3di* a, const vector3di* b, s32 d){return new vector3di(pointer->interpolate(*a, *b, d));}
IRRLICHT_C_API vector3di* vector3di_getHorizontalAngle(vector3di* pointer){return new vector3di(pointer->getHorizontalAngle());}
IRRLICHT_C_API vector3di* vector3di_getSphericalCoordinateAngles(vector3di* pointer){return new vector3di(pointer->getSphericalCoordinateAngles());}
IRRLICHT_C_API vector3di* vector3di_rotationToDirection(vector3di* pointer, const vector3di& forwards = vector3di(0, 0, 1)){return new vector3di(pointer->rotationToDirection(forwards));}
IRRLICHT_C_API void vector3di_getAs4Values(vector3di* pointer, s32* array){pointer->getAs4Values(array);}

#ifdef __cplusplus
}
#endif

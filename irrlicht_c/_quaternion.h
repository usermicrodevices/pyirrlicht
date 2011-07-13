// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

// quaternion
IRRLICHT_C_API quaternion* quaternion_ctor1(){return new quaternion();}
IRRLICHT_C_API quaternion* quaternion_ctor2(f32 x, f32 y, f32 z, f32 w){return new quaternion(x, y, z, w);}
IRRLICHT_C_API quaternion* quaternion_ctor3(f32 x, f32 y, f32 z){return new quaternion(x, y, z);}
IRRLICHT_C_API quaternion* quaternion_ctor4(const vector3df* vec){return new quaternion(*vec);}
IRRLICHT_C_API quaternion* quaternion_ctor5(const matrix4* mat){return new quaternion(*mat);}
IRRLICHT_C_API const bool quaternion_operator_eq(quaternion* pointer, const quaternion* other){return pointer->operator==(*other);}
IRRLICHT_C_API const bool quaternion_operator_ne(quaternion* pointer, const quaternion* other){return pointer->operator!=(*other);}
IRRLICHT_C_API quaternion* quaternion_operator_set1(quaternion* pointer, const quaternion* other){return &pointer->operator=(*other);}
IRRLICHT_C_API quaternion* quaternion_operator_set2(quaternion* pointer, const matrix4* other){return &pointer->operator=(*other);}
IRRLICHT_C_API const quaternion* quaternion_operator_add(quaternion* pointer, const quaternion* other){return &pointer->operator+(*other);}
IRRLICHT_C_API const quaternion* quaternion_operator_mul1(quaternion* pointer, const quaternion* other){return &pointer->operator*(*other);}
IRRLICHT_C_API const quaternion* quaternion_operator_mul2(quaternion* pointer, f32 s){return &pointer->operator*(s);}
IRRLICHT_C_API const vector3df* quaternion_operator_mul3(quaternion* pointer, const vector3df* v){return &pointer->operator*(*v);}
IRRLICHT_C_API quaternion* quaternion_operator_mul_set1(quaternion* pointer, f32 s){return &pointer->operator*=(s);}
IRRLICHT_C_API quaternion* quaternion_operator_mul_set2(quaternion* pointer, const quaternion* other){return &pointer->operator*=(*other);}
IRRLICHT_C_API const f32 quaternion_dotProduct(quaternion* pointer, const quaternion* other){return pointer->dotProduct(*other);}
IRRLICHT_C_API quaternion* quaternion_set1(quaternion* pointer, f32 x, f32 y, f32 z, f32 w){return &pointer->set(x, y, z, w);}
IRRLICHT_C_API quaternion* quaternion_set2(quaternion* pointer, f32 x, f32 y, f32 z){return &pointer->set(x, y, z);}
IRRLICHT_C_API quaternion* quaternion_set3(quaternion* pointer, const core::vector3df* vec){return &pointer->set(*vec);}
IRRLICHT_C_API quaternion* quaternion_set4(quaternion* pointer, const core::quaternion* quat){return &pointer->set(*quat);}
IRRLICHT_C_API const bool quaternion_equals(quaternion* pointer, const quaternion* other, const f32 tolerance = ROUNDING_ERROR_f32){return pointer->equals(*other, tolerance);}
IRRLICHT_C_API quaternion* quaternion_normalize(quaternion* pointer){return &pointer->normalize();}
IRRLICHT_C_API const matrix4* quaternion_getMatrix1(quaternion* pointer){return &pointer->getMatrix();}
IRRLICHT_C_API matrix4* quaternion_getMatrix2(quaternion* pointer, const core::vector3df* translation){matrix4 dest; pointer->getMatrix(dest, *translation); return &dest;}
IRRLICHT_C_API matrix4* quaternion_getMatrixCenter(quaternion* pointer, const core::vector3df* center, const core::vector3df* translation){matrix4 dest; pointer->getMatrixCenter(dest, *center, *translation); return &dest;}
IRRLICHT_C_API matrix4* quaternion_getMatrix_transposed(quaternion* pointer){matrix4 dest; pointer->getMatrix_transposed(dest); return &dest;}
IRRLICHT_C_API quaternion* quaternion_makeInverse(quaternion* pointer){return &pointer->makeInverse();}
IRRLICHT_C_API quaternion* quaternion_slerp(quaternion* pointer, quaternion* q1, quaternion* q2, f32 interpolate){return &pointer->slerp(*q1, *q2, interpolate);}
IRRLICHT_C_API quaternion* quaternion_fromAngleAxis(quaternion* pointer, f32 angle, const vector3df* axis){return &pointer->fromAngleAxis(angle, *axis);}
IRRLICHT_C_API f32 quaternion_toAngleAxis(quaternion* pointer, core::vector3df* axis){f32 angle; pointer->toAngleAxis(angle, *axis); return angle;}
IRRLICHT_C_API vector3df* quaternion_toEuler(quaternion* pointer){vector3df euler; pointer->toEuler(euler); return &euler;}
IRRLICHT_C_API quaternion* quaternion_makeIdentity(quaternion* pointer){return &pointer->makeIdentity();}
IRRLICHT_C_API quaternion* quaternion_rotationFromTo(quaternion* pointer, const vector3df* from, const vector3df* to){return &pointer->rotationFromTo(*from, *to);}

IRRLICHT_C_API f32 quaternion_get_X(quaternion* pointer){return pointer->X;}
IRRLICHT_C_API void quaternion_set_X(quaternion* pointer, f32 value){pointer->X = value;}
IRRLICHT_C_API f32 quaternion_get_Y(quaternion* pointer){return pointer->Y;}
IRRLICHT_C_API void quaternion_set_Y(quaternion* pointer, f32 value){pointer->Y = value;}
IRRLICHT_C_API f32 quaternion_get_Z(quaternion* pointer){return pointer->Z;}
IRRLICHT_C_API void quaternion_set_Z(quaternion* pointer, f32 value){pointer->Z = value;}
IRRLICHT_C_API f32 quaternion_get_W(quaternion* pointer){return pointer->W;}
IRRLICHT_C_API void quaternion_set_W(quaternion* pointer, f32 value){pointer->W = value;}

#ifdef __cplusplus
}
#endif

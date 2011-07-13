// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= CMatrix4
IRRLICHT_C_API matrix4* matrix4_ctor1(matrix4::eConstructor constructor = matrix4::EM4CONST_IDENTITY ){return new matrix4(constructor);}
IRRLICHT_C_API matrix4* matrix4_ctor2(const matrix4* other, matrix4::eConstructor constructor = matrix4::EM4CONST_COPY){return new matrix4(*other, constructor);}
IRRLICHT_C_API f32 matrix4_operator_directly(matrix4* pointer, const s32 row, const s32 col){return pointer->operator()(row, col); }
IRRLICHT_C_API f32 matrix4_operator_linearly(matrix4* pointer, u32 index){return pointer->operator[](index); }
IRRLICHT_C_API void matrix4_set1(matrix4* pointer, const matrix4* other){pointer->operator=(*other);}
IRRLICHT_C_API void matrix4_set2(matrix4* pointer, f32 scalar){pointer->operator=(scalar);}
IRRLICHT_C_API const f32* matrix4_const_pointer(matrix4* pointer){return pointer->pointer();}
IRRLICHT_C_API f32* matrix4_pointer(matrix4* pointer){return pointer->pointer();}
IRRLICHT_C_API bool matrix4_eq(matrix4* pointer, const matrix4* other){return pointer->operator==(*other);}
IRRLICHT_C_API bool matrix4_noteq(matrix4* pointer, const matrix4* other){return pointer->operator!=(*other);}
IRRLICHT_C_API void matrix4_add(matrix4* pointer, const matrix4* other){pointer->operator+(*other);}
IRRLICHT_C_API matrix4* matrix4_get_add(matrix4* pointer, const matrix4* other){return &pointer->operator+=(*other);}
IRRLICHT_C_API void matrix4_sub(matrix4* pointer, const matrix4* other){pointer->operator-(*other);}
IRRLICHT_C_API matrix4* matrix4_get_sub(matrix4* pointer, const matrix4* other){return &pointer->operator-=(*other);}
IRRLICHT_C_API matrix4* matrix4_setbyproduct(matrix4* pointer, const matrix4* other_a, const matrix4* other_b){return &pointer->setbyproduct(*other_a, *other_b);}
IRRLICHT_C_API matrix4* matrix4_setbyproduct_nocheck(matrix4* pointer, const matrix4* other_a, const matrix4* other_b){return &pointer->setbyproduct_nocheck(*other_a, *other_b);}
IRRLICHT_C_API void matrix4_multiplication1(matrix4* pointer, const matrix4* other){pointer->operator*(*other);}
IRRLICHT_C_API void matrix4_multiplication2(matrix4* pointer, f32 scalar){pointer->operator*(scalar);}
IRRLICHT_C_API matrix4* matrix4_get_multiplication1(matrix4* pointer, const matrix4* other){return &pointer->operator*=(*other);}
IRRLICHT_C_API matrix4* matrix4_get_multiplication2(matrix4* pointer, f32 scalar){return &pointer->operator*=(scalar);}
IRRLICHT_C_API matrix4* matrix4_makeIdentity(matrix4* pointer){return &pointer->makeIdentity();}
IRRLICHT_C_API bool matrix4_isIdentity(matrix4* pointer){return pointer->isIdentity();}
IRRLICHT_C_API bool matrix4_isOrthogonal(matrix4* pointer){return pointer->isOrthogonal();}
IRRLICHT_C_API bool matrix4_isIdentity_integer_base(matrix4* pointer){return pointer->isIdentity_integer_base();}
IRRLICHT_C_API matrix4* matrix4_setTranslation(matrix4* pointer, const vector3df* translation){return &pointer->setTranslation(*translation);}
IRRLICHT_C_API vector3df* matrix4_getTranslation(matrix4* pointer){return &pointer->getTranslation();}
IRRLICHT_C_API matrix4* matrix4_setInverseTranslation(matrix4* pointer, const vector3df* translation){return &pointer->setInverseTranslation(*translation);}
IRRLICHT_C_API matrix4* matrix4_setRotationRadians(matrix4* pointer, const vector3df* rotation){return &pointer->setRotationRadians(*rotation);}
IRRLICHT_C_API matrix4* matrix4_setRotationDegrees(matrix4* pointer, const vector3df* rotation){return &pointer->setRotationDegrees(*rotation);}
IRRLICHT_C_API vector3df* matrix4_getRotationDegrees(matrix4* pointer){return &pointer->getRotationDegrees();}
IRRLICHT_C_API matrix4* matrix4_setInverseRotationRadians(matrix4* pointer, const vector3df* rotation){return &pointer->setInverseRotationRadians(*rotation);}
IRRLICHT_C_API matrix4* matrix4_setInverseRotationDegrees(matrix4* pointer, const vector3df* rotation){return &pointer->setInverseRotationDegrees(*rotation);}
IRRLICHT_C_API matrix4* matrix4_setScale1(matrix4* pointer, const vector3df* scale){return &pointer->setScale(*scale);}
IRRLICHT_C_API matrix4* matrix4_setScale2(matrix4* pointer, f32 scale){return &pointer->setScale(scale);}
IRRLICHT_C_API vector3df* matrix4_getScale(matrix4* pointer){return &pointer->getScale();}
IRRLICHT_C_API void matrix4_inverseTranslateVect(matrix4* pointer, vector3df* vect){pointer->inverseTranslateVect(*vect);}
IRRLICHT_C_API void matrix4_inverseRotateVect(matrix4* pointer, vector3df* vect){pointer->inverseRotateVect(*vect);}
IRRLICHT_C_API void matrix4_rotateVect1(matrix4* pointer, vector3df* vect){pointer->rotateVect(*vect);}
IRRLICHT_C_API void matrix4_rotateVect2(matrix4* pointer, core::vector3df* out, const vector3df* in){pointer->rotateVect(*out, *in);}
IRRLICHT_C_API void matrix4_rotateVect3(matrix4* pointer, f32* out, const vector3df* in){pointer->rotateVect(out, *in);}
IRRLICHT_C_API void matrix4_transformVect1(matrix4* pointer, vector3df* vect){pointer->transformVect(*vect);}
IRRLICHT_C_API void matrix4_transformVect2(matrix4* pointer, vector3df* out, const vector3df* in){pointer->transformVect(*out, *in);}
IRRLICHT_C_API void matrix4_transformVect3(matrix4* pointer, f32* out, const vector3df* in){pointer->transformVect(out, *in);}
IRRLICHT_C_API void matrix4_translateVect(matrix4* pointer, vector3df* vect){pointer->translateVect(*vect);}
IRRLICHT_C_API void matrix4_transformPlane1(matrix4* pointer, plane3df* plane){pointer->transformPlane(*plane);}
IRRLICHT_C_API void matrix4_transformPlane2(matrix4* pointer, const plane3df* in, plane3df* out){pointer->transformPlane(*in, *out);}
IRRLICHT_C_API void matrix4_transformBox(matrix4* pointer, aabbox3df* box){pointer->transformBox(*box);}
IRRLICHT_C_API void matrix4_transformBoxEx(matrix4* pointer, aabbox3df* box){pointer->transformBoxEx(*box);}
IRRLICHT_C_API void matrix4_multiplyWith1x4Matrix(matrix4* pointer, f32* matrix){pointer->multiplyWith1x4Matrix(matrix);}
IRRLICHT_C_API bool matrix4_makeInverse(matrix4* pointer){return pointer->makeInverse();}
IRRLICHT_C_API bool matrix4_getInversePrimitive(matrix4* pointer, matrix4* out){return pointer->getInversePrimitive(*out);}
IRRLICHT_C_API bool matrix4_getInverse(matrix4* pointer, matrix4* out){return pointer->getInverse(*out);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixPerspectiveFovRH(matrix4* pointer, f32 fieldOfViewRadians, f32 aspectRatio, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixPerspectiveFovRH(fieldOfViewRadians, aspectRatio, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixPerspectiveFovLH(matrix4* pointer, f32 fieldOfViewRadians, f32 aspectRatio, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixPerspectiveFovLH(fieldOfViewRadians, aspectRatio, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixPerspectiveRH(matrix4* pointer, f32 widthOfViewVolume, f32 heightOfViewVolume, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixPerspectiveRH(widthOfViewVolume, heightOfViewVolume, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixPerspectiveLH(matrix4* pointer, f32 widthOfViewVolume, f32 heightOfViewVolume, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixPerspectiveLH(widthOfViewVolume, heightOfViewVolume, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixOrthoLH(matrix4* pointer, f32 widthOfViewVolume, f32 heightOfViewVolume, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixOrthoLH(widthOfViewVolume, heightOfViewVolume, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildProjectionMatrixOrthoRH(matrix4* pointer, f32 widthOfViewVolume, f32 heightOfViewVolume, f32 zNear, f32 zFar){return &pointer->buildProjectionMatrixOrthoRH(widthOfViewVolume, heightOfViewVolume, zNear, zFar);}
IRRLICHT_C_API matrix4* matrix4_buildCameraLookAtMatrixLH(matrix4* pointer, const vector3df* position, const vector3df* target, const vector3df* upVector){return &pointer->buildCameraLookAtMatrixLH(*position, *target, *upVector);}
IRRLICHT_C_API matrix4* matrix4_buildCameraLookAtMatrixRH(matrix4* pointer, const vector3df* position, const vector3df* target, const vector3df* upVector){return &pointer->buildCameraLookAtMatrixRH(*position, *target, *upVector);}
IRRLICHT_C_API matrix4* matrix4_buildShadowMatrix(matrix4* pointer, const vector3df* light, const plane3df* plane, f32 point = 1.0f){return &pointer->buildShadowMatrix(*light, *plane, point);}
IRRLICHT_C_API matrix4* matrix4_buildNDCToDCMatrix(matrix4* pointer, const recti* area, f32 zScale){return &pointer->buildNDCToDCMatrix(*area, zScale);}
IRRLICHT_C_API void matrix4_interpolate(matrix4* pointer, const matrix4* b, f32 time){pointer->interpolate(*b, time);}
IRRLICHT_C_API matrix4* matrix4_getTransposed1(matrix4* pointer){return &pointer->getTransposed();}
IRRLICHT_C_API void matrix4_getTransposed2(matrix4* pointer, matrix4* dest){pointer->getTransposed(*dest);}
IRRLICHT_C_API matrix4* matrix4_buildRotateFromTo(matrix4* pointer, const vector3df* from, const vector3df* to){return &pointer->buildRotateFromTo(*from, *to);}
IRRLICHT_C_API void matrix4_setRotationCenter(matrix4* pointer, const vector3df* center, const vector3df* translate){pointer->setRotationCenter(*center, *translate);}
IRRLICHT_C_API void matrix4_buildAxisAlignedBillboard(matrix4* pointer, const vector3df* camPos, const vector3df* center, const vector3df* translation, const vector3df* axis, const vector3df* from){pointer->buildAxisAlignedBillboard(*camPos, *center, *translation, *axis, *from);}
IRRLICHT_C_API matrix4* matrix4_buildTextureTransform(matrix4* pointer, f32 rotateRad, const vector2df* rotatecenter, const vector2df* translate, const vector2df* scale){return &pointer->buildTextureTransform(rotateRad, *rotatecenter, *translate, *scale);}
IRRLICHT_C_API matrix4* matrix4_setTextureRotationCenter(matrix4* pointer, f32 radAngle){return &pointer->setTextureRotationCenter(radAngle);}
IRRLICHT_C_API matrix4* matrix4_setTextureTranslate(matrix4* pointer, f32 x, f32 y){return &pointer->setTextureTranslate(x, y);}
IRRLICHT_C_API matrix4* matrix4_setTextureTranslateTransposed(matrix4* pointer, f32 x, f32 y){return &pointer->setTextureTranslateTransposed(x, y);}
IRRLICHT_C_API matrix4* matrix4_setTextureScale(matrix4* pointer, f32 sx, f32 sy){return &pointer->setTextureScale(sx, sy);}
IRRLICHT_C_API matrix4* matrix4_setTextureScaleCenter(matrix4* pointer, f32 sx, f32 sy){return &pointer->setTextureScaleCenter(sx, sy);}
IRRLICHT_C_API matrix4* matrix4_setM(matrix4* pointer, const f32* data)
{
	//const f32 data[] = {0.f, 1.f, 2.f, 3.f, 4.f, 5.f, 6.f, 7.f, 8.f, 9.f, 10.f, 11.f, 12.f, 13.f, 14.f, 15.f};
	//for (int i = 0; i < 16; i++)
	//	printf("+++ ITEM %d = %f\n", i, data[i]);
	return &pointer->setM(data);
}
IRRLICHT_C_API void matrix4_setDefinitelyIdentityMatrix(matrix4* pointer, bool isDefinitelyIdentityMatrix){pointer->setDefinitelyIdentityMatrix(isDefinitelyIdentityMatrix);}
IRRLICHT_C_API bool matrix4_getDefinitelyIdentityMatrix(matrix4* pointer){return pointer->getDefinitelyIdentityMatrix();}

#ifdef __cplusplus
}
#endif

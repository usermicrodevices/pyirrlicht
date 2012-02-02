// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//class triangle3d
IRRLICHT_C_API triangle3df* triangle3df_ctor1(){return new triangle3df();}
IRRLICHT_C_API triangle3df* triangle3df_ctor2(vector3d<f32>* v1, vector3d<f32>* v2, vector3d<f32>* v3){return new triangle3df(*v1, *v2, *v3);}
IRRLICHT_C_API vector3df* triangle3df_get_pointA(triangle3df* pointer){return &pointer->pointA;}
IRRLICHT_C_API vector3df* triangle3df_get_pointB(triangle3df* pointer){return &pointer->pointB;}
IRRLICHT_C_API vector3df* triangle3df_get_pointC(triangle3df* pointer){return &pointer->pointC;}
IRRLICHT_C_API void triangle3df_set_pointA(triangle3df* pointer, const vector3df& value){pointer->pointA = value;}
IRRLICHT_C_API void triangle3df_set_pointB(triangle3df* pointer, const vector3df& value){pointer->pointB = value;}
IRRLICHT_C_API void triangle3df_set_pointC(triangle3df* pointer, const vector3df& value){pointer->pointC = value;}

IRRLICHT_C_API const bool triangle3df_operator_eq(triangle3d<f32>* pointer, const triangle3d<f32>* other){return pointer->operator==(*other);}
IRRLICHT_C_API const bool triangle3df_operator_ne(triangle3d<f32>* pointer, const triangle3d<f32>* other){return pointer->operator!=(*other);}
IRRLICHT_C_API const bool triangle3df_isTotalInsideBox(triangle3d<f32>* pointer, const aabbox3d<f32>* box){return pointer->isTotalInsideBox(*box);}
IRRLICHT_C_API const bool triangle3df_isTotalOutsideBox(triangle3d<f32>* pointer, const aabbox3d<f32>* box){return pointer->isTotalOutsideBox(*box);}
IRRLICHT_C_API const core::vector3d<f32>* triangle3df_closestPointOnTriangle(triangle3d<f32>* pointer, const core::vector3d<f32>* p){return &pointer->closestPointOnTriangle(*p);}
IRRLICHT_C_API const bool triangle3df_isPointInside(triangle3d<f32>* pointer, const vector3d<f32>* p){return pointer->isPointInside(*p);}
IRRLICHT_C_API const bool triangle3df_isPointInsideFast(triangle3d<f32>* pointer, const vector3d<f32>* p){return pointer->isPointInsideFast(*p);}
IRRLICHT_C_API const bool triangle3df_getIntersectionWithLimitedLine(triangle3d<f32>* pointer, const line3d<f32>* line, vector3d<f32>* outIntersection){return pointer->getIntersectionWithLimitedLine(*line, *outIntersection);}
IRRLICHT_C_API const bool triangle3df_getIntersectionWithLine(triangle3d<f32>* pointer, const vector3d<f32>* linePoint, const vector3d<f32>* lineVect, vector3d<f32>* outIntersection){return pointer->getIntersectionWithLine(*linePoint, *lineVect, *outIntersection);}
IRRLICHT_C_API const bool triangle3df_getIntersectionOfPlaneWithLine(triangle3d<f32>* pointer, const vector3d<f32>* linePoint, const vector3d<f32>* lineVect, vector3d<f32>* outIntersection){return pointer->getIntersectionOfPlaneWithLine(*linePoint, *lineVect, *outIntersection);}
IRRLICHT_C_API const vector3d<f32>* triangle3df_getNormal(triangle3d<f32>* pointer){return &pointer->getNormal();}
IRRLICHT_C_API const bool triangle3df_isFrontFacing(triangle3d<f32>* pointer, const vector3d<f32>* lookDirection){return pointer->isFrontFacing(*lookDirection);}
IRRLICHT_C_API const plane3d<f32>* triangle3df_getPlane(triangle3d<f32>* pointer){return &pointer->getPlane();}
IRRLICHT_C_API const f32 triangle3df_getArea(triangle3d<f32>* pointer){return pointer->getArea();}
IRRLICHT_C_API void triangle3df_set(triangle3d<f32>* pointer, const core::vector3d<f32>* a, const core::vector3d<f32>* b, const core::vector3d<f32>* c){pointer->set(*a, *b, *c);}


IRRLICHT_C_API triangle3di* triangle3di_ctor1(){return new triangle3di();}
IRRLICHT_C_API triangle3di* triangle3di_ctor2(vector3d<s32>* v1, vector3d<s32>* v2, vector3d<s32>* v3){return new triangle3di(*v1, *v2, *v3);}
IRRLICHT_C_API vector3di* triangle3di_get_pointA(triangle3di* pointer){return &pointer->pointA;}
IRRLICHT_C_API vector3di* triangle3di_get_pointB(triangle3di* pointer){return &pointer->pointB;}
IRRLICHT_C_API vector3di* triangle3di_get_pointC(triangle3di* pointer){return &pointer->pointC;}
IRRLICHT_C_API void triangle3di_set_pointA(triangle3di* pointer, const vector3di& value){pointer->pointA = value;}
IRRLICHT_C_API void triangle3di_set_pointB(triangle3di* pointer, const vector3di& value){pointer->pointB = value;}
IRRLICHT_C_API void triangle3di_set_pointC(triangle3di* pointer, const vector3di& value){pointer->pointC = value;}

IRRLICHT_C_API const bool triangle3di_operator_eq(triangle3d<s32>* pointer, const triangle3d<s32>* other){return pointer->operator==(*other);}
IRRLICHT_C_API const bool triangle3di_operator_ne(triangle3d<s32>* pointer, const triangle3d<s32>* other){return pointer->operator!=(*other);}
IRRLICHT_C_API const bool triangle3di_isTotalInsideBox(triangle3d<s32>* pointer, const aabbox3d<s32>* box){return pointer->isTotalInsideBox(*box);}
IRRLICHT_C_API const bool triangle3di_isTotalOutsideBox(triangle3d<s32>* pointer, const aabbox3d<s32>* box){return pointer->isTotalOutsideBox(*box);}
IRRLICHT_C_API const core::vector3d<s32>* triangle3di_closestPointOnTriangle(triangle3d<s32>* pointer, const core::vector3d<s32>* p){return &pointer->closestPointOnTriangle(*p);}
IRRLICHT_C_API const bool triangle3di_isPointInside(triangle3d<s32>* pointer, const vector3d<s32>* p){return pointer->isPointInside(*p);}
IRRLICHT_C_API const bool triangle3di_isPointInsideFast(triangle3d<s32>* pointer, const vector3d<s32>* p){return pointer->isPointInsideFast(*p);}
IRRLICHT_C_API const bool triangle3di_getIntersectionWithLimitedLine(triangle3d<s32>* pointer, const line3d<s32>* line, vector3d<s32>* outIntersection){return pointer->getIntersectionWithLimitedLine(*line, *outIntersection);}
IRRLICHT_C_API const bool triangle3di_getIntersectionWithLine(triangle3d<s32>* pointer, const vector3d<s32>* linePoint, const vector3d<s32>* lineVect, vector3d<s32>* outIntersection){return pointer->getIntersectionWithLine(*linePoint, *lineVect, *outIntersection);}
IRRLICHT_C_API const bool triangle3di_getIntersectionOfPlaneWithLine(triangle3d<s32>* pointer, const vector3d<s32>* linePoint, const vector3d<s32>* lineVect, vector3d<s32>* outIntersection){return pointer->getIntersectionOfPlaneWithLine(*linePoint, *lineVect, *outIntersection);}
IRRLICHT_C_API const vector3d<s32>* triangle3di_getNormal(triangle3d<s32>* pointer){return &pointer->getNormal();}
IRRLICHT_C_API const bool triangle3di_isFrontFacing(triangle3d<s32>* pointer, const vector3d<s32>* lookDirection){return pointer->isFrontFacing(*lookDirection);}
IRRLICHT_C_API const plane3d<s32>* triangle3di_getPlane(triangle3d<s32>* pointer){return &pointer->getPlane();}
IRRLICHT_C_API const s32 triangle3di_getArea(triangle3d<s32>* pointer){return pointer->getArea();}
IRRLICHT_C_API void triangle3di_set(triangle3d<s32>* pointer, const core::vector3d<s32>* a, const core::vector3d<s32>* b, const core::vector3d<s32>* c){pointer->set(*a, *b, *c);}

#ifdef __cplusplus
}
#endif

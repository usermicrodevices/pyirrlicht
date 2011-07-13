// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= plane3d
IRRLICHT_C_API plane3df* plane3df_ctor1(){return new plane3df();}
IRRLICHT_C_API plane3df* plane3df_ctor2(const vector3df& MPoint, const vector3df& Normal){return new plane3df(MPoint, Normal);}
IRRLICHT_C_API plane3df* plane3df_ctor3(f32 px, f32 py, f32 pz, f32 nx, f32 ny, f32 nz){return new plane3df(px, py, pz, nx, ny, nz);}
IRRLICHT_C_API plane3df* plane3df_ctor4(const vector3df& point1, const vector3df& point2, const vector3df& point3){return new plane3df(point1, point2, point3);}
IRRLICHT_C_API plane3df* plane3df_ctor5(const vector3df& normal, const f32 d){return new plane3df(normal, d);}
//IRRLICHT_C_API void plane3df_destructor(plane3df* pointer){delete pointer;}
IRRLICHT_C_API bool plane3df_operator_eq(plane3df* pointer, const plane3df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool plane3df_operator_ne(plane3df* pointer, const plane3df& other){return pointer->operator!=(other);}
IRRLICHT_C_API void plane3df_setPlane(plane3df* pointer, const vector3df& point, const vector3df& nvector){pointer->setPlane(point, nvector);}
IRRLICHT_C_API void plane3df_setPlane2(plane3df* pointer, const vector3df& nvect, f32 d){pointer->setPlane(nvect, d);}
IRRLICHT_C_API void plane3df_setPlane3(plane3df* pointer, const vector3df& point1, const vector3df& point2, const vector3df& point3){pointer->setPlane(point1, point2, point3);}
IRRLICHT_C_API bool plane3df_getIntersectionWithLine(plane3df* pointer, const vector3df& linePoint, const vector3df& lineVect, vector3df* outIntersection){return pointer->getIntersectionWithLine(linePoint, lineVect, *outIntersection);}
IRRLICHT_C_API f32 plane3df_getKnownIntersectionWithLine(plane3df* pointer, const vector3df& linePoint1, const vector3df& linePoint2){return pointer->getKnownIntersectionWithLine(linePoint1, linePoint2);}
IRRLICHT_C_API bool plane3df_getIntersectionWithLimitedLine(plane3df* pointer, const vector3df& linePoint1, const vector3df& linePoint2, vector3df& outIntersection){return pointer->getIntersectionWithLimitedLine(linePoint1, linePoint2, outIntersection);}
IRRLICHT_C_API EIntersectionRelation3D plane3df_classifyPointRelation(plane3df* pointer, const vector3df& point){return pointer->classifyPointRelation(point);}
IRRLICHT_C_API void plane3df_recalculateD(plane3df* pointer, const vector3df& MPoint){pointer->recalculateD(MPoint);}
IRRLICHT_C_API vector3df* plane3df_getMemberPoint(plane3df* pointer){return &pointer->getMemberPoint();}
IRRLICHT_C_API bool plane3df_existsIntersection(plane3df* pointer, const plane3df& other){return pointer->existsIntersection(other);}
IRRLICHT_C_API bool plane3df_getIntersectionWithPlane(plane3df* pointer, const plane3df& other, vector3df& outLinePoint, vector3df& outLineVect){return pointer->getIntersectionWithPlane(other, outLinePoint, outLineVect);}
IRRLICHT_C_API bool plane3df_getIntersectionWithPlanes(plane3df* pointer, const plane3df& o1, const plane3df& o2, vector3df& outPoint){return pointer->getIntersectionWithPlanes(o1, o2, outPoint);}
IRRLICHT_C_API bool plane3df_isFrontFacing(plane3df* pointer, const vector3df& lookDirection){return pointer->isFrontFacing(lookDirection);}
IRRLICHT_C_API f32 plane3df_getDistanceTo(plane3df* pointer, const vector3df& point){return pointer->getDistanceTo(point);}
IRRLICHT_C_API vector3df* plane3df_get_Normal(plane3df* pointer){return &pointer->Normal;}
IRRLICHT_C_API void plane3df_set_Normal(plane3df* pointer, const vector3df& value){pointer->Normal = value;}
IRRLICHT_C_API f32 plane3df_get_D(plane3df* pointer){return pointer->D;}
IRRLICHT_C_API void plane3df_set_D(plane3df* pointer, f32 value){pointer->D = value;}

IRRLICHT_C_API plane3di* plane3di_ctor1(){return new plane3di();}
IRRLICHT_C_API plane3di* plane3di_ctor2(const vector3di& MPoint, const vector3di& Normal){return new plane3di(MPoint, Normal);}
IRRLICHT_C_API plane3di* plane3di_ctor3(s32 px, s32 py, s32 pz, s32 nx, s32 ny, s32 nz){return new plane3di(px, py, pz, nx, ny, nz);}
IRRLICHT_C_API plane3di* plane3di_ctor4(const vector3di& point1, const vector3di& point2, const vector3di& point3){return new plane3di(point1, point2, point3);}
IRRLICHT_C_API plane3di* plane3di_ctor5(const vector3di& normal, const s32 d){return new plane3di(normal, d);}
//IRRLICHT_C_API void plane3di_destructor(plane3di* pointer){delete pointer;}
IRRLICHT_C_API bool plane3di_operator_eq(plane3di* pointer, const plane3di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool plane3di_operator_ne(plane3di* pointer, const plane3di& other){return pointer->operator!=(other);}
IRRLICHT_C_API void plane3di_setPlane(plane3di* pointer, const vector3di& point, const vector3di& nvector){pointer->setPlane(point, nvector);}
IRRLICHT_C_API void plane3di_setPlane2(plane3di* pointer, const vector3di& nvect, s32 d){pointer->setPlane(nvect, d);}
IRRLICHT_C_API void plane3di_setPlane3(plane3di* pointer, const vector3di& point1, const vector3di& point2, const vector3di& point3){pointer->setPlane(point1, point2, point3);}
IRRLICHT_C_API bool plane3di_getIntersectionWithLine(plane3di* pointer, const vector3di& linePoint, const vector3di& lineVect, vector3di* outIntersection){return pointer->getIntersectionWithLine(linePoint, lineVect, *outIntersection);}
IRRLICHT_C_API s32 plane3di_getKnownIntersectionWithLine(plane3di* pointer, const vector3di& linePoint1, const vector3di& linePoint2){return (s32)pointer->getKnownIntersectionWithLine(linePoint1, linePoint2);}
IRRLICHT_C_API bool plane3di_getIntersectionWithLimitedLine(plane3di* pointer, const vector3di& linePoint1, const vector3di& linePoint2, vector3di& outIntersection){return pointer->getIntersectionWithLimitedLine(linePoint1, linePoint2, outIntersection);}
IRRLICHT_C_API EIntersectionRelation3D plane3di_classifyPointRelation(plane3di* pointer, const vector3di& point){return pointer->classifyPointRelation(point);}
IRRLICHT_C_API void plane3di_recalculateD(plane3di* pointer, const vector3di& MPoint){pointer->recalculateD(MPoint);}
IRRLICHT_C_API vector3di* plane3di_getMemberPoint(plane3di* pointer){return &pointer->getMemberPoint();}
IRRLICHT_C_API bool plane3di_existsIntersection(plane3di* pointer, const plane3di& other){return pointer->existsIntersection(other);}
IRRLICHT_C_API bool plane3di_getIntersectionWithPlane(plane3di* pointer, const plane3di& other, vector3di& outLinePoint, vector3di& outLineVect){return pointer->getIntersectionWithPlane(other, outLinePoint, outLineVect);}
IRRLICHT_C_API bool plane3di_getIntersectionWithPlanes(plane3di* pointer, const plane3di& o1, const plane3di& o2, vector3di& outPoint){return pointer->getIntersectionWithPlanes(o1, o2, outPoint);}
IRRLICHT_C_API bool plane3di_isFrontFacing(plane3di* pointer, const vector3di& lookDirection){return pointer->isFrontFacing(lookDirection);}
IRRLICHT_C_API s32 plane3di_getDistanceTo(plane3di* pointer, const vector3di& point){return pointer->getDistanceTo(point);}
IRRLICHT_C_API vector3di* plane3di_get_Normal(plane3di* pointer){return &pointer->Normal;}
IRRLICHT_C_API void plane3di_set_Normal(plane3di* pointer, const vector3di& value){pointer->Normal = value;}
IRRLICHT_C_API s32 plane3di_get_D(plane3di* pointer){return pointer->D;}
IRRLICHT_C_API void plane3di_set_D(plane3di* pointer, s32 value){pointer->D = value;}

#ifdef __cplusplus
}
#endif

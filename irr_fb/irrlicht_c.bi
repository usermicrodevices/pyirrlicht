' This file was automatic generated with "h2bi" script

Type EVENT_METHOD As Function Cdecl (ByVal _event_ As Any Ptr) As UByte

#inclib "../irrlicht_c"

#include once "const.bi"

Extern "c"

	Extern _IRR_WCHAR_FILESYSTEM Alias "IRR_WCHAR_FILESYSTEM" As Integer

#if _IRR_WCHAR_FILESYSTEM
	Type fschar As WString Ptr
#else
	Type fschar As ZString Ptr
#endif

	Declare Sub delete_pointer(ByVal _pointer_ As Any Ptr)

	Declare Function IBillboardSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr) As Any Ptr
	Declare Sub IBillboardSceneNode_setSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Function IBillboardSceneNode_getSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IBillboardSceneNode_setColor(ByVal _pointer_ As Any Ptr, ByVal overallColor As Any Ptr)
	Declare Sub IBillboardSceneNode_setColor2(ByVal _pointer_ As Any Ptr, ByVal _to_pColor As Any Ptr, ByVal bottomColor As Any Ptr)
	Declare Sub IBillboardSceneNode_getColor(ByVal _pointer_ As Any Ptr, ByVal _to_pColor As Any Ptr, ByVal bottomColor As Any Ptr)
	Declare Function ICameraSceneNode_ctor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICameraSceneNode_set_func_event(ByVal _pointer_ As Any Ptr, ByVal event As Any Ptr)
	Declare Sub ICameraSceneNode_setProjectionMatrix(ByVal _pointer_ As Any Ptr, ByVal projection As Any Ptr, ByVal isOrthogonal As UByte)
	Declare Function ICameraSceneNode_getProjectionMatrix(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ICameraSceneNode_getViewMatrix(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICameraSceneNode_setViewMatrixAffector(ByVal _pointer_ As Any Ptr, ByVal affector As Any Ptr)
	Declare Function ICameraSceneNode_getViewMatrixAffector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICameraSceneNode_setTarget(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub ICameraSceneNode_setRotation(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr)
	Declare Function ICameraSceneNode_getTarget(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICameraSceneNode_setUpVector(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr)
	Declare Function ICameraSceneNode_getUpVector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ICameraSceneNode_getNearValue(ByVal _pointer_ As Any Ptr) As Single
	Declare Function ICameraSceneNode_getFarValue(ByVal _pointer_ As Any Ptr) As Single
	Declare Function ICameraSceneNode_getAspectRatio(ByVal _pointer_ As Any Ptr) As Single
	Declare Function ICameraSceneNode_getFOV(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub ICameraSceneNode_setNearValue(ByVal _pointer_ As Any Ptr, ByVal zn As Single)
	Declare Sub ICameraSceneNode_setFarValue(ByVal _pointer_ As Any Ptr, ByVal zf As Single)
	Declare Sub ICameraSceneNode_setAspectRatio(ByVal _pointer_ As Any Ptr, ByVal aspect As Single)
	Declare Sub ICameraSceneNode_setFOV(ByVal _pointer_ As Any Ptr, ByVal fovy As Single)
	Declare Function ICameraSceneNode_getViewFrustum(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICameraSceneNode_setInputReceiverEnabled(ByVal _pointer_ As Any Ptr, ByVal enabled As UByte)
	Declare Function ICameraSceneNode_isInputReceiverEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ICameraSceneNode_isOrthogonal(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ICameraSceneNode_bindTargetAndRotation(ByVal _pointer_ As Any Ptr, ByVal bound As UByte)
	Declare Function ICameraSceneNode_getTargetAndRotationBinding(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SViewFrustum_ctor1(ByVal mat As Any Ptr) As Any Ptr
	Declare Function SViewFrustum_ctor2(ByVal other As Any Ptr) As Any Ptr
	Declare Sub SViewFrustum_transform(ByVal _pointer_ As Any Ptr, ByVal mat As Any Ptr)
	Declare Function SViewFrustum_getFarLeftUp(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SViewFrustum_getFarLeftDown(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SViewFrustum_getFarRightUp(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SViewFrustum_getFarRightDown(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SViewFrustum_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SViewFrustum_recalculateBoundingBox(ByVal _pointer_ As Any Ptr)
	Declare Sub SViewFrustum_setFrom(ByVal _pointer_ As Any Ptr, ByVal mat As Any Ptr)
	Declare Function SViewFrustum_getTransform(ByVal _pointer_ As Any Ptr, ByVal state As E_TRANSFORMATION_STATE) As Any Ptr
	Declare Function SViewFrustum_clipLine(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr) As UByte
	Declare Function ILightSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr) As Any Ptr
	Declare Sub ILightSceneNode_setLightData(ByVal _pointer_ As Any Ptr, ByVal light As Any Ptr)
	Declare Function ILightSceneNode_getLightData(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ILightSceneNode_setVisible(ByVal _pointer_ As Any Ptr, ByVal _isVisible_ As UByte)
	Declare Sub ILightSceneNode_setRadius(ByVal _pointer_ As Any Ptr, ByVal radius As Single)
	Declare Function ILightSceneNode_getRadius(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub ILightSceneNode_setLightType(ByVal _pointer_ As Any Ptr, ByVal _type_ As E_LIGHT_TYPE)
	Declare Function ILightSceneNode_getLightType(ByVal _pointer_ As Any Ptr) As E_LIGHT_TYPE
	Declare Sub ILightSceneNode_enableCastShadow(ByVal _pointer_ As Any Ptr, ByVal shadow As UByte)
	Declare Function ILightSceneNode_getCastShadow(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneCollisionManager_getCollisionPoint(ByVal _pointer_ As Any Ptr, ByVal ray As Any Ptr, ByVal selector As Any Ptr, ByVal outCollisionPoint As Any Ptr, ByVal outTriangle As Any Ptr, ByVal outNode As Any Ptr) As UByte
	Declare Function ISceneCollisionManager_getCollisionResultPosition(ByVal _pointer_ As Any Ptr, ByVal selector As Any Ptr, ByVal ellipsoidPosition As Any Ptr, ByVal ellipsoidRadius As Any Ptr, ByVal ellipsoidDirectionAndSpeed As Any Ptr, ByVal triout As Any Ptr, ByVal hitPosition As Any Ptr, ByVal outFalling As UByte, ByVal outNode As Any Ptr, ByVal slidingSpeed As Single, ByVal gravityDirectionAndSpeed As Any Ptr) As Any Ptr
	Declare Function ISceneCollisionManager_getRayFromScreenCoordinates(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr, ByVal camera As Any Ptr) As Any Ptr
	Declare Function ISceneCollisionManager_getScreenCoordinatesFrom3DPosition(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr, ByVal camera As Any Ptr) As Any Ptr
	Declare Function ISceneCollisionManager_getSceneNodeFromScreenCoordinatesBB(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr, ByVal idBitMask As Integer, ByVal bNoDebugObjects As UByte, ByVal root As Any Ptr) As Any Ptr
	Declare Function ISceneCollisionManager_getSceneNodeFromRayBB(ByVal _pointer_ As Any Ptr, ByVal ray As Any Ptr, ByVal idBitMask As Integer, ByVal bNoDebugObjects As UByte, ByVal root As Any Ptr) As Any Ptr
	Declare Function ISceneCollisionManager_getSceneNodeFromCameraBB(ByVal _pointer_ As Any Ptr, ByVal camera As Any Ptr, ByVal idBitMask As Integer, ByVal bNoDebugObjects As UByte) As Any Ptr
	Declare Function ISceneCollisionManager_getSceneNodeAndCollisionPointFromRay(ByVal _pointer_ As Any Ptr, ByVal ray As Any Ptr, ByVal outCollisionPoint As Any Ptr, ByVal outTriangle As Any Ptr, ByVal idBitMask As Integer, ByVal collisionRootNode As Any Ptr, ByVal noDebugObjects As UByte) As Any Ptr
	Declare Function ICollisionCallback_ctor1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ICollisionCallback_ctor2(ByVal animator As Any Ptr) As Any Ptr
	Declare Sub ICollisionCallback_set_func_animator(ByVal _pointer_ As Any Ptr, ByVal animator As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_isFalling(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ISceneNodeAnimatorCollisionResponse_setEllipsoidRadius(ByVal _pointer_ As Any Ptr, ByVal radius As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_getEllipsoidRadius(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNodeAnimatorCollisionResponse_setGravity(ByVal _pointer_ As Any Ptr, ByVal gravity As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_getGravity(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNodeAnimatorCollisionResponse_jump(ByVal _pointer_ As Any Ptr, ByVal jumpSpeed As Single)
	Declare Sub ISceneNodeAnimatorCollisionResponse_setAnimateTarget(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function ISceneNodeAnimatorCollisionResponse_getAnimateTarget(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ISceneNodeAnimatorCollisionResponse_setEllipsoidTranslation(ByVal _pointer_ As Any Ptr, ByVal translation As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_getEllipsoidTranslation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNodeAnimatorCollisionResponse_setWorld(ByVal _pointer_ As Any Ptr, ByVal newWorld As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_getWorld(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNodeAnimatorCollisionResponse_setTargetNode(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Function ISceneNodeAnimatorCollisionResponse_getTargetNode(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorCollisionResponse_collisionOccurred(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneNodeAnimatorCollisionResponse_getCollisionPoint(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorCollisionResponse_getCollisionTriangle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorCollisionResponse_getCollisionResultPosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorCollisionResponse_getCollisionNode(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNodeAnimatorCollisionResponse_setCollisionCallback(ByVal _pointer_ As Any Ptr, ByVal callback As Any Ptr)
	Declare Function vector3df_ctor1() As Any Ptr
	Declare Function vector3df_ctor2(ByVal x As Single, ByVal y As Single, ByVal z As Single) As Any Ptr
	Declare Function vector3df_ctor3(ByVal n As Single) As Any Ptr
	Declare Function vector3df_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Sub vector3df_set_X(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function vector3df_get_X(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub vector3df_set_Y(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function vector3df_get_Y(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub vector3df_set_Z(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function vector3df_get_Z(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector3df_operator_sub(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_add_value(ByVal _pointer_ As Any Ptr, ByVal val As Single) As Any Ptr
	Declare Function vector3df_operator_set_add_value(ByVal _pointer_ As Any Ptr, ByVal val As Single) As Any Ptr
	Declare Function vector3df_operator_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_sub_value(ByVal _pointer_ As Any Ptr, ByVal val As Single) As Any Ptr
	Declare Function vector3df_operator_set_sub_value(ByVal _pointer_ As Any Ptr, ByVal val As Single) As Any Ptr
	Declare Function vector3df_operator_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_set_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector3df_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector3df_operator_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_set_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3df_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector3df_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector3df_operator_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_operator_ge(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_operator_gt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3df_equals(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal _to_lerance As Single) As UByte
	Declare Function vector3df_set1(ByVal _pointer_ As Any Ptr, ByVal nx As Single, ByVal ny As Single, ByVal nz As Single) As Any Ptr
	Declare Function vector3df_set2(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector3df_getLength(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector3df_getLengthSQ(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector3df_dotProduct(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector3df_getDistanceFrom(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector3df_getDistanceFromSQ(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector3df_crossProduct(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector3df_isBetweenPoints(ByVal _pointer_ As Any Ptr, ByVal begin As Any Ptr, ByVal _end_ As Any Ptr) As UByte
	Declare Function vector3df_normalize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3df_setLength(ByVal _pointer_ As Any Ptr, ByVal newlength As Single) As Any Ptr
	Declare Function vector3df_invert(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub vector3df_rotateXZBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Single, ByVal center As Any Ptr)
	Declare Sub vector3df_rotateXYBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Single, ByVal center As Any Ptr)
	Declare Sub vector3df_rotateYZBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Single, ByVal center As Any Ptr)
	Declare Function vector3df_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector3df_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector3df_interpolate(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector3df_getHorizontalAngle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3df_getSphericalCoordinateAngles(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3df_rotationToDirection(ByVal _pointer_ As Any Ptr, ByVal forwards As Any Ptr) As Any Ptr
	Declare Sub vector3df_getAs4Values(ByVal _pointer_ As Any Ptr, ByVal array As Any Ptr)
	Declare Function vector3di_ctor1() As Any Ptr
	Declare Function vector3di_ctor2(ByVal x As Integer, ByVal y As Integer, ByVal z As Integer) As Any Ptr
	Declare Function vector3di_ctor3(ByVal n As Integer) As Any Ptr
	Declare Function vector3di_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Sub vector3di_set_X(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function vector3di_get_X(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub vector3di_set_Y(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function vector3di_get_Y(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub vector3di_set_Z(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function vector3di_get_Z(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function vector3di_operator_sub(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_add_value(ByVal _pointer_ As Any Ptr, ByVal val As Integer) As Any Ptr
	Declare Function vector3di_operator_set_add_value(ByVal _pointer_ As Any Ptr, ByVal val As Integer) As Any Ptr
	Declare Function vector3di_operator_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_sub_value(ByVal _pointer_ As Any Ptr, ByVal val As Integer) As Any Ptr
	Declare Function vector3di_operator_set_sub_value(ByVal _pointer_ As Any Ptr, ByVal val As Integer) As Any Ptr
	Declare Function vector3di_operator_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_set_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector3di_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector3di_operator_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_set_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector3di_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector3di_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector3di_operator_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_operator_ge(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_operator_gt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector3di_equals(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal _to_lerance As Integer) As UByte
	Declare Function vector3di_set1(ByVal _pointer_ As Any Ptr, ByVal nx As Integer, ByVal ny As Integer, ByVal nz As Integer) As Any Ptr
	Declare Function vector3di_set2(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector3di_getLength(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function vector3di_getLengthSQ(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function vector3di_dotProduct(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector3di_getDistanceFrom(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector3di_getDistanceFromSQ(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector3di_crossProduct(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector3di_isBetweenPoints(ByVal _pointer_ As Any Ptr, ByVal begin As Any Ptr, ByVal _end_ As Any Ptr) As UByte
	Declare Function vector3di_normalize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3di_setLength(ByVal _pointer_ As Any Ptr, ByVal newlength As Integer) As Any Ptr
	Declare Function vector3di_invert(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub vector3di_rotateXZBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Integer, ByVal center As Any Ptr)
	Declare Sub vector3di_rotateXYBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Integer, ByVal center As Any Ptr)
	Declare Sub vector3di_rotateYZBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Integer, ByVal center As Any Ptr)
	Declare Function vector3di_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector3di_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector3di_interpolate(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector3di_getHorizontalAngle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3di_getSphericalCoordinateAngles(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector3di_rotationToDirection(ByVal _pointer_ As Any Ptr, ByVal forwards As Any Ptr) As Any Ptr
	Declare Sub vector3di_getAs4Values(ByVal _pointer_ As Any Ptr, ByVal array As Any Ptr)
	Declare Function dimension2df_ctor1() As Any Ptr
	Declare Function dimension2df_ctor2(ByVal w As Single, ByVal h As Single) As Any Ptr
	Declare Function dimension2df_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_operator_set_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_operator_eq_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2df_operator_ne_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2df_operator_eq_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2df_operator_ne_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2df_set(ByVal _pointer_ As Any Ptr, ByVal _width_ As Single, ByVal height As Single) As Any Ptr
	Declare Function dimension2df_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As Single) As Any Ptr
	Declare Function dimension2df_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As Single) As Any Ptr
	Declare Function dimension2df_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As Single) As Any Ptr
	Declare Function dimension2df_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As Single) As Any Ptr
	Declare Function dimension2df_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2df_getArea(ByVal _pointer_ As Any Ptr) As Single
	Declare Function dimension2df_getOptimalSize(ByVal _pointer_ As Any Ptr, ByVal requirePowerOfTwo As UByte, ByVal requireSquare As UByte, ByVal larger As UByte, ByVal maxValue As Single) As Any Ptr
	Declare Function dimension2df_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function dimension2df_get_Width(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub dimension2df_set_Width(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function dimension2df_get_Height(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub dimension2df_set_Height(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function dimension2du_ctor1() As Any Ptr
	Declare Function dimension2du_ctor2(ByVal w As UInteger, ByVal h As UInteger) As Any Ptr
	Declare Function dimension2du_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_operator_set_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_operator_eq_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2du_operator_ne_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2du_operator_eq_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2du_operator_ne_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2du_set(ByVal _pointer_ As Any Ptr, ByVal _width_ As UInteger, ByVal height As UInteger) As Any Ptr
	Declare Function dimension2du_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As UInteger) As Any Ptr
	Declare Function dimension2du_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As UInteger) As Any Ptr
	Declare Function dimension2du_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As UInteger) As Any Ptr
	Declare Function dimension2du_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As UInteger) As Any Ptr
	Declare Function dimension2du_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2du_getArea(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function dimension2du_getOptimalSize(ByVal _pointer_ As Any Ptr, ByVal requirePowerOfTwo As UByte, ByVal requireSquare As UByte, ByVal larger As UByte, ByVal maxValue As UInteger) As Any Ptr
	Declare Function dimension2du_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As UInteger) As Any Ptr
	Declare Function dimension2du_get_Width(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub dimension2du_set_Width(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function dimension2du_get_Height(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub dimension2du_set_Height(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function dimension2di_ctor1() As Any Ptr
	Declare Function dimension2di_ctor2(ByVal w As Integer, ByVal h As Integer) As Any Ptr
	Declare Function dimension2di_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_operator_set_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_operator_eq_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2di_operator_ne_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2di_operator_eq_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2di_operator_ne_vector2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function dimension2di_set(ByVal _pointer_ As Any Ptr, ByVal _width_ As Integer, ByVal height As Integer) As Any Ptr
	Declare Function dimension2di_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As Integer) As Any Ptr
	Declare Function dimension2di_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal scale As Integer) As Any Ptr
	Declare Function dimension2di_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As Integer) As Any Ptr
	Declare Function dimension2di_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal scale As Integer) As Any Ptr
	Declare Function dimension2di_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function dimension2di_getArea(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function dimension2di_getOptimalSize(ByVal _pointer_ As Any Ptr, ByVal requirePowerOfTwo As UByte, ByVal requireSquare As UByte, ByVal larger As UByte, ByVal maxValue As Integer) As Any Ptr
	Declare Function dimension2di_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function dimension2di_get_Width(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub dimension2di_set_Width(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function dimension2di_get_Height(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub dimension2di_set_Height(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Sub IGUIFont_draw(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal position As Any Ptr, ByVal _color_ As Any Ptr, ByVal hcenter As UByte, ByVal vcenter As UByte, ByVal clip As Any Ptr)
	Declare Function IGUIFont_getDimension(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr) As Any Ptr
	Declare Function IGUIFont_getCharacterFromPos(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal pixel_x As Integer) As Integer
	Declare Function IGUIFont_getType(ByVal _pointer_ As Any Ptr) As EGUI_FONT_TYPE
	Declare Sub IGUIFont_setKerningWidth(ByVal _pointer_ As Any Ptr, ByVal kerning As Integer)
	Declare Sub IGUIFont_setKerningHeight(ByVal _pointer_ As Any Ptr, ByVal kerning As Integer)
	Declare Function IGUIFont_getKerningWidth(ByVal _pointer_ As Any Ptr, ByVal thisLetter As WString Ptr, ByVal previousLetter As WString Ptr) As Integer
	Declare Function IGUIFont_getKerningHeight(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIFont_setInvisibleCharacters(ByVal _pointer_ As Any Ptr, ByVal s As WString Ptr)
	Declare Function vector2df_ctor1(ByVal nx As Single, ByVal ny As Single) As Any Ptr
	Declare Function vector2df_ctor2(ByVal n As Single) As Any Ptr
	Declare Function vector2df_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_sub(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_add_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_add_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_add_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_add_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_sub_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_sub_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_sub_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_sub_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_set_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2df_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Single) As Any Ptr
	Declare Function vector2df_operator_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_operator_ge(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_operator_gt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_equals(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2df_set(ByVal _pointer_ As Any Ptr, ByVal nx As Single, ByVal ny As Single) As Any Ptr
	Declare Function vector2df_set2(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector2df_getLength(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2df_getLengthSQ(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2df_dotProduct(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector2df_getDistanceFrom(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector2df_getDistanceFromSQ(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function vector2df_rotateBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Single, ByVal center As Any Ptr) As Any Ptr
	Declare Function vector2df_normalize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector2df_getAngleTrig(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2df_getAngle(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2df_getAngleWith(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As Single
	Declare Function vector2df_isBetweenPoints(ByVal _pointer_ As Any Ptr, ByVal begin As Any Ptr, ByVal _end_ As Any Ptr) As UByte
	Declare Function vector2df_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector2df_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector2df_interpolate(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function vector2df_get_X(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub vector2df_set_X(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function vector2df_get_Y(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub vector2df_set_Y(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function vector2di_ctor1(ByVal nx As Integer, ByVal ny As Integer) As Any Ptr
	Declare Function vector2di_ctor2(ByVal n As Integer) As Any Ptr
	Declare Function vector2di_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_sub(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_add_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_add_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_add_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_add_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_add_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_sub_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_sub_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_sub_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_sub_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_sub_dimension2d(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_mult_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_mult_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_set_div_other(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function vector2di_operator_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_set_div_value(ByVal _pointer_ As Any Ptr, ByVal v As Integer) As Any Ptr
	Declare Function vector2di_operator_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_operator_ge(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_operator_gt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_equals(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function vector2di_set(ByVal _pointer_ As Any Ptr, ByVal nx As Integer, ByVal ny As Integer) As Any Ptr
	Declare Function vector2di_set2(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function vector2di_getLength(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function vector2di_getLengthSQ(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function vector2di_dotProduct(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector2di_getDistanceFrom(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector2di_getDistanceFromSQ(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Integer
	Declare Function vector2di_rotateBy(ByVal _pointer_ As Any Ptr, ByVal degrees As Integer, ByVal center As Any Ptr) As Any Ptr
	Declare Function vector2di_normalize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function vector2di_getAngleTrig(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2di_getAngle(ByVal _pointer_ As Any Ptr) As Single
	Declare Function vector2di_getAngleWith(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As Single
	Declare Function vector2di_isBetweenPoints(ByVal _pointer_ As Any Ptr, ByVal begin As Any Ptr, ByVal _end_ As Any Ptr) As UByte
	Declare Function vector2di_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector2di_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector2di_interpolate(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function vector2di_get_X(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub vector2di_set_X(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function vector2di_get_Y(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub vector2di_set_Y(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function position2df_ctor1(ByVal nx As Single, ByVal ny As Single) As Any Ptr
	Declare Function position2df_ctor2(ByVal n As Single) As Any Ptr
	Declare Function position2df_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function position2df_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function position2di_ctor1(ByVal nx As Integer, ByVal ny As Integer) As Any Ptr
	Declare Function position2di_ctor2(ByVal n As Integer) As Any Ptr
	Declare Function position2di_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Function position2di_ctor4(ByVal other As Any Ptr) As Any Ptr
	Declare Function IOSOperator_getOperationSystemVersion(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Sub IOSOperator_copyToClipboard(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Function IOSOperator_getTextFromClipboard(ByVal _pointer_ As Any Ptr) As WString Ptr
	'Declare Sub IOSOperator_copyToClipboard(ByVal _pointer_ As Any Ptr, ByVal text As ZString Ptr)
	'Declare Function IOSOperator_getTextFromClipboard(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function IOSOperator_getProcessorSpeedMHz(ByVal _pointer_ As Any Ptr, ByVal MHz As Any Ptr) As UByte
	Declare Function IOSOperator_getSystemMemory(ByVal _pointer_ As Any Ptr, ByVal Total As Any Ptr, ByVal Avail As Any Ptr) As UByte
	Declare Function IGeometryCreator_createCubeMesh(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Function IGeometryCreator_createHillPlaneMesh(ByVal _pointer_ As Any Ptr, ByVal tileSize As Any Ptr, ByVal tileCount As Any Ptr, ByVal material As Any Ptr, ByVal hillHeight As Single, ByVal countHills As Any Ptr, ByVal textureRepeatCount As Any Ptr) As Any Ptr
	Declare Function IGeometryCreator_createPlaneMesh(ByVal _pointer_ As Any Ptr, ByVal tileSize As Any Ptr, ByVal tileCount As Any Ptr, ByVal material As Any Ptr, ByVal textureRepeatCount As Any Ptr) As Any Ptr
	Declare Function IGeometryCreator_createTerrainMesh(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal heightmap As Any Ptr, ByVal stretchSize As Any Ptr, ByVal maxHeight As Single, ByVal driver As Any Ptr, ByVal defaultVertexBlockSize As Any Ptr, ByVal debugBorders As UByte) As Any Ptr
	Declare Function IGeometryCreator_createArrowMesh(ByVal _pointer_ As Any Ptr, ByVal tesselationCylinder As UInteger, ByVal tesselationCone As UInteger, ByVal height As Single, ByVal cylinderHeight As Single, ByVal _width_Cylinder As Single, ByVal _width_Cone As Single, ByVal _color_Cylinder As Any Ptr, ByVal _color_Cone As Any Ptr) As Any Ptr
	Declare Function IGeometryCreator_createSphereMesh(ByVal _pointer_ As Any Ptr, ByVal radius As Single, ByVal polyCountX As UInteger, ByVal polyCountY As UInteger) As Any Ptr
	Declare Function IGeometryCreator_createCylinderMesh(ByVal _pointer_ As Any Ptr, ByVal radius As Single, ByVal _len_gth As Single, ByVal tesselation As UInteger, ByVal _color_ As Any Ptr, ByVal closeTop As UByte, ByVal oblique As Single) As Any Ptr
	Declare Function IGeometryCreator_createConeMesh(ByVal _pointer_ As Any Ptr, ByVal radius As Single, ByVal _len_gth As Single, ByVal tesselation As UInteger, ByVal _color_Top As Any Ptr, ByVal _color_Bottom As Any Ptr, ByVal oblique As Single) As Any Ptr
	Declare Function IGeometryCreator_createVolumeLightMesh(ByVal _pointer_ As Any Ptr, ByVal subdivideU As UInteger, ByVal subdivideV As UInteger, ByVal footColor As Any Ptr, ByVal tailColor As Any Ptr, ByVal lpDistance As Single, ByVal lightDim As Any Ptr) As Any Ptr
	Declare Function aabbox3df_ctor1() As Any Ptr
	Declare Function aabbox3df_ctor2(ByVal min As Any Ptr, ByVal max As Any Ptr) As Any Ptr
	Declare Function aabbox3df_ctor3(ByVal init As Any Ptr) As Any Ptr
	Declare Function aabbox3df_ctor4(ByVal minx As Single, ByVal miny As Single, ByVal minz As Single, ByVal maxx As Single, ByVal maxy As Single, ByVal maxz As Single) As Any Ptr
	Declare Function aabbox3df_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3df_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub aabbox3df_reset1(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single, ByVal z As Single)
	Declare Sub aabbox3df_reset2(ByVal _pointer_ As Any Ptr, ByVal initValue As Any Ptr)
	Declare Sub aabbox3df_reset3(ByVal _pointer_ As Any Ptr, ByVal initValue As Any Ptr)
	Declare Sub aabbox3df_addInternalBox(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr)
	Declare Sub aabbox3df_addInternalPoint1(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr)
	Declare Sub aabbox3df_addInternalPoint2(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single, ByVal z As Single)
	Declare Function aabbox3df_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function aabbox3df_getExtent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function aabbox3df_isEmpty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function aabbox3df_getVolume(ByVal _pointer_ As Any Ptr) As Single
	Declare Function aabbox3df_getArea(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub aabbox3df_getEdges(ByVal _pointer_ As Any Ptr, ByVal edges As Any Ptr)
	Declare Sub aabbox3df_repair(ByVal _pointer_ As Any Ptr)
	Declare Function aabbox3df_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function aabbox3df_isPointInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function aabbox3df_isPointTotalInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function aabbox3df_isFullInside(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3df_intersectsWithBox(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3df_intersectsWithLine1(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr) As UByte
	Declare Function aabbox3df_intersectsWithLine2(ByVal _pointer_ As Any Ptr, ByVal _line_middle As Any Ptr, ByVal _line_vect As Any Ptr, ByVal halflength As Single) As UByte
	Declare Function aabbox3df_classifyPlaneRelation(ByVal _pointer_ As Any Ptr, ByVal plane As Any Ptr) As EIntersectionRelation3D
	Declare Function aabbox3df_get_MinEdge(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub aabbox3df_set_MinEdge(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function aabbox3df_get_MaxEdge(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub aabbox3df_set_MaxEdge(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function aabbox3di_ctor1() As Any Ptr
	Declare Function aabbox3di_ctor2(ByVal min As Any Ptr, ByVal max As Any Ptr) As Any Ptr
	Declare Function aabbox3di_ctor3(ByVal init As Any Ptr) As Any Ptr
	Declare Function aabbox3di_ctor4(ByVal minx As Integer, ByVal miny As Integer, ByVal minz As Integer, ByVal maxx As Integer, ByVal maxy As Integer, ByVal maxz As Integer) As Any Ptr
	Declare Function aabbox3di_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3di_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub aabbox3di_reset1(ByVal _pointer_ As Any Ptr, ByVal x As Integer, ByVal y As Integer, ByVal z As Integer)
	Declare Sub aabbox3di_reset2(ByVal _pointer_ As Any Ptr, ByVal initValue As Any Ptr)
	Declare Sub aabbox3di_reset3(ByVal _pointer_ As Any Ptr, ByVal initValue As Any Ptr)
	Declare Sub aabbox3di_addInternalBox(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr)
	Declare Sub aabbox3di_addInternalPoint1(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr)
	Declare Sub aabbox3di_addInternalPoint2(ByVal _pointer_ As Any Ptr, ByVal x As Integer, ByVal y As Integer, ByVal z As Integer)
	Declare Function aabbox3di_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function aabbox3di_getExtent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function aabbox3di_isEmpty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function aabbox3di_getVolume(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function aabbox3di_getArea(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub aabbox3di_getEdges(ByVal _pointer_ As Any Ptr, ByVal edges As Any Ptr)
	Declare Sub aabbox3di_repair(ByVal _pointer_ As Any Ptr)
	Declare Function aabbox3di_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function aabbox3di_isPointInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function aabbox3di_isPointTotalInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function aabbox3di_isFullInside(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3di_intersectsWithBox(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function aabbox3di_classifyPlaneRelation(ByVal _pointer_ As Any Ptr, ByVal plane As Any Ptr) As EIntersectionRelation3D
	Declare Function aabbox3di_get_MinEdge(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub aabbox3di_set_MinEdge(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function aabbox3di_get_MaxEdge(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub aabbox3di_set_MaxEdge(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function IMeshBuffer_getMaterial(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IMeshBuffer_getVertexType(ByVal _pointer_ As Any Ptr) As E_VERTEX_TYPE
	Declare Function IMeshBuffer_getVertices(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IMeshBuffer_getVertexCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IMeshBuffer_getIndexType(ByVal _pointer_ As Any Ptr) As E_INDEX_TYPE
	Declare Function IMeshBuffer_getIndices(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IMeshBuffer_getIndexCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IMeshBuffer_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IMeshBuffer_setBoundingBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub IMeshBuffer_recalculateBoundingBox(ByVal _pointer_ As Any Ptr)
	Declare Function IMeshBuffer_getPosition(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IMeshBuffer_getNormal(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IMeshBuffer_getTCoords(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Sub IMeshBuffer_append1(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal numVertices As UInteger, ByVal indices As Any Ptr, ByVal numIndices As UInteger)
	Declare Sub IMeshBuffer_append2(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function IMeshBuffer_getHardwareMappingHint_Vertex(ByVal _pointer_ As Any Ptr) As E_HARDWARE_MAPPING
	Declare Function IMeshBuffer_getHardwareMappingHint_Index(ByVal _pointer_ As Any Ptr) As E_HARDWARE_MAPPING
	Declare Sub IMeshBuffer_setHardwareMappingHint(ByVal _pointer_ As Any Ptr, ByVal newMappingHint As E_HARDWARE_MAPPING, ByVal buffer As E_BUFFER_TYPE)
	Declare Sub IMeshBuffer_setDirty(ByVal _pointer_ As Any Ptr, ByVal buffer As E_BUFFER_TYPE)
	Declare Function IMeshBuffer_getChangedID_Vertex(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IMeshBuffer_getChangedID_Index(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IMetaTriangleSelector_addTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal _to_Add As Any Ptr)
	Declare Function IMetaTriangleSelector_removeTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal _to_Remove As Any Ptr) As UByte
	Declare Sub IMetaTriangleSelector_removeAllTriangleSelectors(ByVal _pointer_ As Any Ptr)
	Extern ESNT_CUBE Alias "_ESNT_CUBE" As ESCENE_NODE_TYPE
	Extern ESNT_SPHERE Alias "_ESNT_SPHERE" As ESCENE_NODE_TYPE
	Extern ESNT_TEXT Alias "_ESNT_TEXT" As ESCENE_NODE_TYPE
	Extern ESNT_WATER_SURFACE Alias "_ESNT_WATER_SURFACE" As ESCENE_NODE_TYPE
	Extern ESNT_TERRAIN Alias "_ESNT_TERRAIN" As ESCENE_NODE_TYPE
	Extern ESNT_SKY_BOX Alias "_ESNT_SKY_BOX" As ESCENE_NODE_TYPE
	Extern ESNT_SKY_DOME Alias "_ESNT_SKY_DOME" As ESCENE_NODE_TYPE
	Extern ESNT_SHADOW_VOLUME Alias "_ESNT_SHADOW_VOLUME" As ESCENE_NODE_TYPE
	Extern ESNT_OCTREE Alias "_ESNT_OCTREE" As ESCENE_NODE_TYPE
	Extern ESNT_MESH Alias "_ESNT_MESH" As ESCENE_NODE_TYPE
	Extern ESNT_LIGHT Alias "_ESNT_LIGHT" As ESCENE_NODE_TYPE
	Extern ESNT_EMPTY Alias "_ESNT_EMPTY" As ESCENE_NODE_TYPE
	Extern ESNT_DUMMY_TRANSFORMATION Alias "_ESNT_DUMMY_TRANSFORMATION" As ESCENE_NODE_TYPE
	Extern ESNT_CAMERA Alias "_ESNT_CAMERA" As ESCENE_NODE_TYPE
	Extern ESNT_BILLBOARD Alias "_ESNT_BILLBOARD" As ESCENE_NODE_TYPE
	Extern ESNT_ANIMATED_MESH Alias "_ESNT_ANIMATED_MESH" As ESCENE_NODE_TYPE
	Extern ESNT_PARTICLE_SYSTEM Alias "_ESNT_PARTICLE_SYSTEM" As ESCENE_NODE_TYPE
	Extern ESNT_Q3SHADER_SCENE_NODE Alias "_ESNT_Q3SHADER_SCENE_NODE" As ESCENE_NODE_TYPE
	Extern ESNT_MD3_SCENE_NODE Alias "_ESNT_MD3_SCENE_NODE" As ESCENE_NODE_TYPE
	Extern ESNT_VOLUME_LIGHT Alias "_ESNT_VOLUME_LIGHT" As ESCENE_NODE_TYPE
	Extern ESNT_CAMERA_MAYA Alias "_ESNT_CAMERA_MAYA" As ESCENE_NODE_TYPE
	Extern ESNT_CAMERA_FPS Alias "_ESNT_CAMERA_FPS" As ESCENE_NODE_TYPE
	Extern ESNT_UNKNOWN Alias "_ESNT_UNKNOWN" As ESCENE_NODE_TYPE
	Extern ESNT_ANY Alias "_ESNT_ANY" As ESCENE_NODE_TYPE
	Declare Function ISceneNodeAnimatorList_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub ISceneNodeAnimatorList_clear(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneNodeAnimatorList_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ISceneNodeAnimatorList_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub ISceneNodeAnimatorList_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Function ISceneNodeAnimatorList_first(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorList_current(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorList_next(ByVal _pointer_ As Any Ptr, ByVal from_first As UByte) As Any Ptr
	Declare Function ISceneNodeAnimatorList_last(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorList_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function ISceneNodeList_ctor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeList_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub ISceneNodeList_clear(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneNodeList_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ISceneNodeList_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub ISceneNodeList_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Function ISceneNodeList_first(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeList_current(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeList_next(ByVal _pointer_ As Any Ptr, ByVal from_first As UByte) As Any Ptr
	Declare Function ISceneNodeList_last(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNodeList_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function ISceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_OnRegisterSceneNode(ByVal _pointer_ As Any Ptr)
	Declare Sub ISceneNode_OnAnimate(ByVal _pointer_ As Any Ptr, ByVal timeMs As UInteger)
	Declare Sub ISceneNode_render(ByVal _pointer_ As Any Ptr, ByVal func As Any Ptr)
	Declare Function ISceneNode_getName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub ISceneNode_setName(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr)
	Declare Function ISceneNode_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNode_getTransformedBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNode_getAbsoluteTransformation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNode_getRelativeTransformation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNode_isVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneNode_isTrulyVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ISceneNode_setVisible(ByVal _pointer_ As Any Ptr, ByVal _isVisible_ As UByte)
	Declare Function ISceneNode_getID(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub ISceneNode_setID(ByVal _pointer_ As Any Ptr, ByVal id As Integer)
	Declare Sub ISceneNode_addChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr)
	Declare Function ISceneNode_removeChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr) As UByte
	Declare Sub ISceneNode_removeAll(ByVal _pointer_ As Any Ptr)
	Declare Sub ISceneNode_remove(ByVal _pointer_ As Any Ptr)
	Declare Sub ISceneNode_addAnimator(ByVal _pointer_ As Any Ptr, ByVal animator As Any Ptr)
	Declare Function ISceneNode_getAnimators(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_removeAnimator(ByVal _pointer_ As Any Ptr, ByVal animator As Any Ptr)
	Declare Sub ISceneNode_removeAnimators(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneNode_getMaterial(ByVal _pointer_ As Any Ptr, ByVal num As UInteger) As Any Ptr
	Declare Sub ISceneNode_setMaterial(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr, ByVal num As UInteger)
	Declare Function ISceneNode_getMaterialCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub ISceneNode_setMaterialFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	Declare Sub ISceneNode_setMaterialTexture(ByVal _pointer_ As Any Ptr, ByVal textureLayer As UInteger, ByVal texture As Any Ptr)
	Declare Sub ISceneNode_setMaterialType(ByVal _pointer_ As Any Ptr, ByVal newType As E_MATERIAL_TYPE)
	Declare Function ISceneNode_getScale(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setScale(ByVal _pointer_ As Any Ptr, ByVal scale As Any Ptr)
	Declare Function ISceneNode_getRotation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setRotation(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr)
	Declare Function ISceneNode_getPosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setPosition(ByVal _pointer_ As Any Ptr, ByVal newpos As Any Ptr)
	Declare Function ISceneNode_getAbsolutePosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setAutomaticCulling(ByVal _pointer_ As Any Ptr, ByVal state As E_CULLING_TYPE)
	Declare Function ISceneNode_getAutomaticCulling(ByVal _pointer_ As Any Ptr) As E_CULLING_TYPE
	Declare Sub ISceneNode_setDebugDataVisible(ByVal _pointer_ As Any Ptr, ByVal state As Integer)
	Declare Function ISceneNode_isDebugDataVisible(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub ISceneNode_setIsDebugObject(ByVal _pointer_ As Any Ptr, ByVal debugObject As UByte)
	Declare Function ISceneNode_isDebugObject(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneNode_getChildren(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setParent(ByVal _pointer_ As Any Ptr, ByVal newParent As Any Ptr)
	Declare Function ISceneNode_getTriangleSelector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneNode_setTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal selector As Any Ptr)
	Declare Sub ISceneNode_updateAbsolutePosition(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneNode_getParent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneNode_getType(ByVal _pointer_ As Any Ptr) As ESCENE_NODE_TYPE
	Declare Sub ISceneNode_serializeAttributes(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal options As Any Ptr)
	Declare Sub ISceneNode_deserializeAttributes(ByVal _pointer_ As Any Ptr, ByVal in As Any Ptr, ByVal options As Any Ptr)
	Declare Function ISceneNode_clone(ByVal _pointer_ As Any Ptr, ByVal newParent As Any Ptr, ByVal newManager As Any Ptr) As Any Ptr
	Declare Function ISceneNode_getSceneManager(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CustomSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Sub CustomSceneNode_set_OnRegisterSceneNode(ByVal _pointer_ As Any Ptr, ByVal func As Any Ptr)
	Declare Sub CustomSceneNode_set_render(ByVal _pointer_ As Any Ptr, ByVal func As Any Ptr)
	Declare Sub CustomSceneNode_set_getBoundingBox(ByVal _pointer_ As Any Ptr, ByVal func As Any Ptr)
	Declare Sub CustomSceneNode_set_getMaterial(ByVal _pointer_ As Any Ptr, ByVal funcu32 As Any Ptr)
	Declare Sub CustomSceneNode_set_getMaterialCount(ByVal _pointer_ As Any Ptr, ByVal func As Any Ptr)
	Extern MATERIAL_MAX_TEXTURES Alias "_MATERIAL_MAX_TEXTURES" As UInteger
	Declare Function SMaterial_ctor1() As Any Ptr
	Declare Function SMaterial_ctor2(ByVal other As Any Ptr) As Any Ptr
	Declare Function SMaterial_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function SMaterial_get_TextureLayer(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Function SMaterial_get_MaterialType(ByVal _pointer_ As Any Ptr) As E_MATERIAL_TYPE
	Declare Function SMaterial_get_AmbientColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMaterial_get_DiffuseColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMaterial_get_EmissiveColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMaterial_get_SpecularColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMaterial_get_Shininess(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SMaterial_get_MaterialTypeParam(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SMaterial_get_MaterialTypeParam2(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SMaterial_get_Thickness(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SMaterial_get_ZBuffer(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SMaterial_get_AntiAliasing(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SMaterial_get_ColorMask(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SMaterial_get_ColorMaterial(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SMaterial_get_Wireframe(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_PointCloud(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_GouraudShading(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_Lighting(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_ZWriteEnable(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_BackfaceCulling(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_FrontfaceCulling(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_FogEnable(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMaterial_get_NormalizeNormals(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SMaterial_set_TextureLayer(ByVal _pointer_ As Any Ptr, ByVal texture_layer As Any Ptr)
	Declare Sub SMaterial_set_MaterialType(ByVal _pointer_ As Any Ptr, ByVal value As E_MATERIAL_TYPE)
	Declare Sub SMaterial_set_AmbientColor(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SMaterial_set_DiffuseColor(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SMaterial_set_EmissiveColor(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SMaterial_set_SpecularColor(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SMaterial_set_Shininess(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SMaterial_set_MaterialTypeParam(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SMaterial_set_MaterialTypeParam2(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SMaterial_set_Thickness(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SMaterial_set_ZBuffer(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Sub SMaterial_set_AntiAliasing(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Sub SMaterial_set_ColorMask(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Sub SMaterial_set_ColorMaterial(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Sub SMaterial_set_Wireframe(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_PointCloud(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_GouraudShading(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_Lighting(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_ZWriteEnable(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_BackfaceCulling(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_FrontfaceCulling(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_FogEnable(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Sub SMaterial_set_NormalizeNormals(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SMaterial_getTextureMatrix(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Sub SMaterial_setTextureMatrix(ByVal _pointer_ As Any Ptr, ByVal i As UInteger, ByVal mat As Any Ptr)
	Declare Function SMaterial_getTexture(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Sub SMaterial_setTexture(ByVal _pointer_ As Any Ptr, ByVal i As UInteger, ByVal tex As Any Ptr)
	Declare Sub SMaterial_setFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_MATERIAL_FLAG, ByVal value As UByte)
	Declare Function SMaterial_getFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_MATERIAL_FLAG) As UByte
	Declare Function SMaterial_operator_noteq(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As UByte
	Declare Function SMaterial_operator_eq(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As UByte
	Declare Function SMaterial_isTransparent(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IImage_lock(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IImage_unlock(ByVal _pointer_ As Any Ptr)
	Declare Function IImage_getDimension(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IImage_getBitsPerPixel(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getBytesPerPixel(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getImageDataSizeInBytes(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getImageDataSizeInPixels(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getPixel(ByVal _pointer_ As Any Ptr, ByVal x As UInteger, ByVal y As UInteger) As Any Ptr
	Declare Sub IImage_setPixel(ByVal _pointer_ As Any Ptr, ByVal x As UInteger, ByVal y As UInteger, ByVal color As Any Ptr, ByVal blend As UByte)
	Declare Function IImage_getColorFormat(ByVal _pointer_ As Any Ptr) As ECOLOR_FORMAT
	Declare Function IImage_getRedMask(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getGreenMask(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getBlueMask(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getAlphaMask(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IImage_getPitch(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IImage_copyToScaling1(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr, ByVal _width_ As UInteger, ByVal height As UInteger, ByVal format As ECOLOR_FORMAT, ByVal pitch As UInteger)
	Declare Sub IImage_copyToScaling2(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr)
	Declare Sub IImage_copyTo1(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub IImage_copyTo2(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr, ByVal pos As Any Ptr, ByVal sourceRect As Any Ptr, ByVal clipRect As Any Ptr)
	Declare Sub IImage_copyToWithAlpha(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr, ByVal pos As Any Ptr, ByVal sourceRect As Any Ptr, ByVal color As Any Ptr, ByVal clipRect As Any Ptr)
	Declare Sub IImage_copyToScalingBoxFilter(ByVal _pointer_ As Any Ptr, ByVal target As Any Ptr, ByVal bias As Integer, ByVal blend As UByte)
	Declare Sub IImage_fill(ByVal _pointer_ As Any Ptr, ByVal color As Any Ptr)
	Declare Function IImage_getBitsPerPixelFromFormat(ByVal _pointer_ As Any Ptr, ByVal format As ECOLOR_FORMAT) As UInteger
	Declare Function IImage_isRenderTargetOnlyFormat(ByVal _pointer_ As Any Ptr, ByVal format As ECOLOR_FORMAT) As UByte
	Declare Function IGUIButton_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIButton_setOverrideFont(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr)
	Declare Sub IGUIButton_setImage1(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr)
	Declare Sub IGUIButton_setImage2(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub IGUIButton_setPressedImage1(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr)
	Declare Sub IGUIButton_setPressedImage2(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub IGUIButton_setSpriteBank(ByVal _pointer_ As Any Ptr, ByVal bank As Any Ptr)
	Declare Sub IGUIButton_setSprite(ByVal _pointer_ As Any Ptr, ByVal state As EGUI_BUTTON_STATE, ByVal index As Integer, ByVal _color_ As Any Ptr, ByVal _loop_ As UByte)
	Declare Sub IGUIButton_setIsPushButton(ByVal _pointer_ As Any Ptr, ByVal _isPushButton_ As UByte)
	Declare Sub IGUIButton_setPressed(ByVal _pointer_ As Any Ptr, ByVal pressed As UByte)
	Declare Function IGUIButton_isPressed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIButton_setUseAlphaChannel(ByVal _pointer_ As Any Ptr, ByVal useAlphaChannel As UByte)
	Declare Function IGUIButton_isAlphaChannelUsed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIButton_isPushButton(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIButton_setDrawBorder(ByVal _pointer_ As Any Ptr, ByVal border As UByte)
	Declare Function IGUIButton_isDrawingBorder(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIButton_setScaleImage(ByVal _pointer_ As Any Ptr, ByVal scaleImage As UByte)
	Declare Function IGUIButton_isScalingImage(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function listIGUIElementIterator_ctor() As Any Ptr
	Declare Function listIGUIElementIterator_operator_next(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function listIGUIElementIterator_operator_prev(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function listIGUIElementIterator_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function listIGUIElementIterator_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function listIGUIElementIterator_operator_add_set(ByVal _pointer_ As Any Ptr, ByVal num As Integer) As Any Ptr
	Declare Function listIGUIElementIterator_operator_add(ByVal _pointer_ As Any Ptr, ByVal num As Integer) As Any Ptr
	Declare Function listIGUIElementIterator_operator_sub(ByVal _pointer_ As Any Ptr, ByVal num As Integer) As Any Ptr
	Declare Function listIGUIElement_ctor1() As Any Ptr
	Declare Function listIGUIElement_ctor2(ByVal other As Any Ptr) As Any Ptr
	Declare Sub listIGUIElement_operator_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function listIGUIElement_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function listIGUIElement_getSize(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub listIGUIElement_clear(ByVal _pointer_ As Any Ptr)
	Declare Function listIGUIElement_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub listIGUIElement_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub listIGUIElement_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Function listIGUIElement_begin(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function listIGUIElement_end(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function listIGUIElement_getLast(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub listIGUIElement_insert_after(ByVal _pointer_ As Any Ptr, ByVal it As Any Ptr, ByVal element As Any Ptr)
	Declare Sub listIGUIElement_insert_before(ByVal _pointer_ As Any Ptr, ByVal it As Any Ptr, ByVal element As Any Ptr)
	Declare Function listIGUIElement_erase(ByVal _pointer_ As Any Ptr, ByVal it As Any Ptr) As Any Ptr
	Declare Sub listIGUIElement_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function IGUIElement_ctor(ByVal _type_ As EGUI_ELEMENT_TYPE, ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIElement_getParent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_getRelativePosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIElement_setRelativePosition1(ByVal _pointer_ As Any Ptr, ByVal r As Any Ptr)
	Declare Sub IGUIElement_setRelativePosition2(ByVal _pointer_ As Any Ptr, ByVal position As Any Ptr)
	Declare Sub IGUIElement_setRelativePositionProportional(ByVal _pointer_ As Any Ptr, ByVal r As Any Ptr)
	Declare Function IGUIElement_getAbsolutePosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_getAbsoluteClippingRect(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIElement_setNotClipped(ByVal _pointer_ As Any Ptr, ByVal noClip As UByte)
	Declare Function IGUIElement_isNotClipped(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIElement_setMaxSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Sub IGUIElement_setMinSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Sub IGUIElement_setAlignment(ByVal _pointer_ As Any Ptr, ByVal left As EGUI_ALIGNMENT, ByVal right As EGUI_ALIGNMENT, ByVal _to_p As EGUI_ALIGNMENT, ByVal bottom As EGUI_ALIGNMENT)
	Declare Sub IGUIElement_updateAbsolutePosition(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIElement_getElementFromPoint(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_isPointInside(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As UByte
	Declare Sub IGUIElement_addChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr)
	Declare Sub IGUIElement_removeChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr)
	Declare Sub IGUIElement_remove(ByVal _pointer_ As Any Ptr)
	Declare Sub IGUIElement_draw(ByVal _pointer_ As Any Ptr)
	Declare Sub IGUIElement_OnPostRender(ByVal _pointer_ As Any Ptr, ByVal timeMs As UInteger)
	Declare Sub IGUIElement_move(ByVal _pointer_ As Any Ptr, ByVal absoluteMovement As Any Ptr)
	Declare Function IGUIElement_isVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIElement_setVisible(ByVal _pointer_ As Any Ptr, ByVal visible As UByte)
	Declare Function IGUIElement_isSubElement(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIElement_setSubElement(ByVal _pointer_ As Any Ptr, ByVal subElement As UByte)
	Declare Sub IGUIElement_setTabStop(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIElement_isTabStop(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIElement_setTabOrder(ByVal _pointer_ As Any Ptr, ByVal index As Integer)
	Declare Function IGUIElement_getTabOrder(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIElement_setTabGroup(ByVal _pointer_ As Any Ptr, ByVal isGroup As UByte)
	Declare Function IGUIElement_isTabGroup(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIElement_getTabGroup(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_isEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIElement_setEnabled(ByVal _pointer_ As Any Ptr, ByVal enabled As UByte)
	Declare Sub IGUIElement_setText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Function IGUIElement_getText(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Sub IGUIElement_setToolTipText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Function IGUIElement_getToolTipText(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function IGUIElement_getID(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIElement_setID(ByVal _pointer_ As Any Ptr, ByVal id As Integer)
	Declare Function IGUIElement_bringToFront(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As UByte
	Declare Function IGUIElement_getChildren(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_getElementFromId(ByVal _pointer_ As Any Ptr, ByVal id As Integer, ByVal searchchildren As UByte) As Any Ptr
	Declare Function IGUIElement_isMyChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr) As UByte
	Declare Function IGUIElement_getNextElement(ByVal _pointer_ As Any Ptr, ByVal startOrder As Integer, ByVal reverse As UByte, ByVal group As UByte, ByVal first As Any Ptr, ByVal closest As Any Ptr, ByVal includeInvisible As UByte) As UByte
	Declare Function IGUIElement_getType(ByVal _pointer_ As Any Ptr) As EGUI_ELEMENT_TYPE
	Declare Function IGUIElement_hasType(ByVal _pointer_ As Any Ptr, ByVal _type_ As EGUI_ELEMENT_TYPE) As UByte
	Declare Function IGUIElement_getTypeName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub IGUIElement_serializeAttributes(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal options As Any Ptr)
	Declare Sub IGUIElement_deserializeAttributes(ByVal _pointer_ As Any Ptr, ByVal in As Any Ptr, ByVal options As Any Ptr)
	Declare Function IGUIElement_as_IGUIButton(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUICheckBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIColorSelectDialog(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIComboBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIContextMenu(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIEditBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIFileOpenDialog(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIFontBitmap(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIImage(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIListBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIMeshViewer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIScrollBar(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUISpinBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIStaticText(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUITab(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUITabControl(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUITable(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIToolBar(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUITreeView(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIElement_as_IGUIWindow(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIWindow_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIWindow_getCloseButton(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIWindow_getMinimizeButton(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIWindow_getMaximizeButton(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIWindow_isDraggable(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIWindow_setDraggable(ByVal _pointer_ As Any Ptr, ByVal draggable As UByte)
	Declare Sub IGUIWindow_setDrawBackground(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Function IGUIWindow_getDrawBackground(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIWindow_setDrawTitlebar(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Function IGUIWindow_getDrawTitlebar(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIWindow_getClientRect(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SGUISpriteFrame_ctor() As Any Ptr
	Declare Function SGUISpriteFrame_get_rectNumber(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SGUISpriteFrame_set_rectNumber(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SGUISpriteFrame_get_textureNumber(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SGUISpriteFrame_set_textureNumber(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SGUISpriteFrameArray_ctor() As Any Ptr
	Declare Sub SGUISpriteFrameArray_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Sub SGUISpriteFrameArray_setAllocStrategy(ByVal _pointer_ As Any Ptr, ByVal newStrategy As eAllocStrategy)
	Declare Sub SGUISpriteFrameArray_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub SGUISpriteFrameArray_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub SGUISpriteFrameArray_insert(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal index As UInteger)
	Declare Sub SGUISpriteFrameArray_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub SGUISpriteFrameArray_set_pointer(ByVal _pointer_ As Any Ptr, ByVal newPointer As Any Ptr, ByVal _size_ As UInteger, ByVal _is_sorted As UByte, ByVal _free_when_destroyed As UByte)
	Declare Sub SGUISpriteFrameArray_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub SGUISpriteFrameArray_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function SGUISpriteFrameArray_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function SGUISpriteFrameArray_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SGUISpriteFrameArray_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SGUISpriteFrameArray_erase1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub SGUISpriteFrameArray_erase2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal count As Integer)
	Declare Sub SGUISpriteFrameArray_set_sorted(ByVal _pointer_ As Any Ptr, ByVal _is_sorted As UByte)
	Declare Sub SGUISpriteFrameArray_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function SGUISprite_ctor() As Any Ptr
	Declare Function SGUISprite_get_Frames(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SGUISprite_set_Frames(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SGUISprite_get_frameTime(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SGUISprite_set_frameTime(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SGUISpriteArray_ctor() As Any Ptr
	Declare Sub SGUISpriteArray_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Sub SGUISpriteArray_setAllocStrategy(ByVal _pointer_ As Any Ptr, ByVal newStrategy As eAllocStrategy)
	Declare Sub SGUISpriteArray_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub SGUISpriteArray_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub SGUISpriteArray_insert(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal index As UInteger)
	Declare Sub SGUISpriteArray_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub SGUISpriteArray_set_pointer(ByVal _pointer_ As Any Ptr, ByVal newPointer As Any Ptr, ByVal _size_ As UInteger, ByVal _is_sorted As UByte, ByVal _free_when_destroyed As UByte)
	Declare Sub SGUISpriteArray_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub SGUISpriteArray_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function SGUISpriteArray_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function SGUISpriteArray_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SGUISpriteArray_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SGUISpriteArray_erase1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub SGUISpriteArray_erase2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal count As Integer)
	Declare Sub SGUISpriteArray_set_sorted(ByVal _pointer_ As Any Ptr, ByVal _is_sorted As UByte)
	Declare Sub SGUISpriteArray_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function IGUISpriteBank_getPositions(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUISpriteBank_getSprites(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUISpriteBank_getTextureCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUISpriteBank_getTexture(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Sub IGUISpriteBank_addTexture(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr)
	Declare Sub IGUISpriteBank_setTexture(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal texture As Any Ptr)
	Declare Function IGUISpriteBank_addTextureAsSprite(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr) As Integer
	Declare Sub IGUISpriteBank_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub IGUISpriteBank_draw2DSprite(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal pos As Any Ptr, ByVal clip As Any Ptr, ByVal _color_ As Any Ptr, ByVal starttime As UInteger, ByVal currenttime As UInteger, ByVal _loop_ As UByte, ByVal center As UByte)
	Declare Sub IGUISpriteBank_draw2DSpriteBatch(ByVal _pointer_ As Any Ptr, ByVal indices As Any Ptr, ByVal pos As Any Ptr, ByVal clip As Any Ptr, ByVal _color_ As Any Ptr, ByVal starttime As UInteger, ByVal currenttime As UInteger, ByVal _loop_ As UByte, ByVal center As UByte)
	Declare Function IGUISkin_getColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As EGUI_DEFAULT_COLOR) As Any Ptr
	Declare Sub IGUISkin_setColor(ByVal _pointer_ As Any Ptr, ByVal which As EGUI_DEFAULT_COLOR, ByVal newColor As Any Ptr)
	Declare Function IGUISkin_getSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As EGUI_DEFAULT_SIZE) As Integer
	Declare Function IGUISkin_getDefaultText(ByVal _pointer_ As Any Ptr, ByVal text As EGUI_DEFAULT_TEXT) As WString Ptr
	Declare Sub IGUISkin_setDefaultText(ByVal _pointer_ As Any Ptr, ByVal which As EGUI_DEFAULT_TEXT, ByVal newText As WString Ptr)
	Declare Sub IGUISkin_setSize(ByVal _pointer_ As Any Ptr, ByVal which As EGUI_DEFAULT_SIZE, ByVal _size_ As Integer)
	Declare Function IGUISkin_getFont(ByVal _pointer_ As Any Ptr, ByVal which As EGUI_DEFAULT_FONT) As Any Ptr
	Declare Sub IGUISkin_setFont(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr, ByVal which As EGUI_DEFAULT_FONT)
	Declare Function IGUISkin_getSpriteBank(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUISkin_setSpriteBank(ByVal _pointer_ As Any Ptr, ByVal bank As Any Ptr)
	Declare Function IGUISkin_getIcon(ByVal _pointer_ As Any Ptr, ByVal icon As EGUI_DEFAULT_ICON) As UInteger
	Declare Sub IGUISkin_setIcon(ByVal _pointer_ As Any Ptr, ByVal icon As EGUI_DEFAULT_ICON, ByVal index As UInteger)
	Declare Sub IGUISkin_draw3DButtonPaneStandard(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal rect As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IGUISkin_draw3DButtonPanePressed(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal rect As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IGUISkin_draw3DSunkenPane(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal bgcolor As Any Ptr, ByVal flat As UByte, ByVal fillBackGround As UByte, ByVal rect As Any Ptr, ByVal clip As Any Ptr)
	Declare Function IGUISkin_draw3DWindowBackground(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal _draw_TitleBar As UByte, ByVal titleBarColor As Any Ptr, ByVal rect As Any Ptr, ByVal clip As Any Ptr, ByVal checkClientArea As Any Ptr) As Any Ptr
	Declare Sub IGUISkin_draw3DMenuPane(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal rect As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IGUISkin_draw3DToolBar(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal rect As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IGUISkin_draw3DTabButton(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal active As UByte, ByVal rect As Any Ptr, ByVal clip As Any Ptr, ByVal alignment As EGUI_ALIGNMENT)
	Declare Sub IGUISkin_draw3DTabBody(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal border As UByte, ByVal background As UByte, ByVal rect As Any Ptr, ByVal clip As Any Ptr, ByVal tabHeight As Integer, ByVal alignment As EGUI_ALIGNMENT)
	Declare Sub IGUISkin_drawIcon(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal icon As EGUI_DEFAULT_ICON, ByVal position As Any Ptr, ByVal starttime As UInteger, ByVal currenttime As UInteger, ByVal _loop_ As UByte, ByVal clip As Any Ptr)
	Declare Sub IGUISkin_draw2DRectangle(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal color As Any Ptr, ByVal pos As Any Ptr, ByVal clip As Any Ptr)
	Declare Function IGUISkin_getType(ByVal _pointer_ As Any Ptr) As EGUI_SKIN_TYPE
	Declare Function IGUIStaticText_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIStaticText_setOverrideFont(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr)
	Declare Function IGUIStaticText_getOverrideFont(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIStaticText_setOverrideColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Function IGUIStaticText_getOverrideColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIStaticText_enableOverrideColor(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIStaticText_isOverrideColorEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIStaticText_setBackgroundColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IGUIStaticText_setDrawBackground(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Sub IGUIStaticText_setDrawBorder(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Sub IGUIStaticText_setTextAlignment(ByVal _pointer_ As Any Ptr, ByVal horizontal As EGUI_ALIGNMENT, ByVal vertical As EGUI_ALIGNMENT)
	Declare Sub IGUIStaticText_setWordWrap(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIStaticText_isWordWrapEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIStaticText_getTextHeight(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIStaticText_getTextWidth(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SJoystickInfo_ctor(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SJoystickInfo_get_Joystick(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SJoystickInfo_set_Joystick(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SJoystickInfo_get_Name(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SJoystickInfo_set_Name(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SJoystickInfo_get_Buttons(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SJoystickInfo_set_Buttons(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SJoystickInfo_get_Axes(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SJoystickInfo_set_Axes(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SJoystickInfo_get_PovHat(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SEvent_GetEventType(ByVal _pointer_ As Any Ptr) As EEVENT_TYPE
	Declare Function SEvent_GetSGUIEvent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SGUIEvent_GetCaller(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SGUIEvent_GetElement(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SGUIEvent_GetEventType(ByVal _pointer_ As Any Ptr) As EGUI_EVENT_TYPE
	Declare Function SEvent_GetSMouseInput(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMouseInput_GetX(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SMouseInput_GetY(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SMouseInput_GetWheel(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SMouseInput_GetShift(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMouseInput_GetControl(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMouseInput_GetButtonStates(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SMouseInput_isLeftPressed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMouseInput_isRightPressed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMouseInput_isMiddlePressed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMouseInput_GetEventType(ByVal _pointer_ As Any Ptr) As EMOUSE_INPUT_EVENT
	Declare Function SEvent_GetSKeyInput(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SKeyInput_GetChar(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function SKeyInput_GetKey(ByVal _pointer_ As Any Ptr) As EKEY_CODE
	Declare Function SKeyInput_GetPressedDown(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SKeyInput_GetShift(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SKeyInput_GetControl(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SEvent_GetSJoystickEvent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SJoystickEvent_GetButtonStates(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SJoystickEvent_GetAxis(ByVal _pointer_ As Any Ptr) As Short
	Declare Function SJoystickEvent_GetPOV(ByVal _pointer_ As Any Ptr) As UShort
	Declare Function SJoystickEvent_GetJoystick(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SJoystickEvent_IsButtonPressed(ByVal _pointer_ As Any Ptr, ByVal button As UInteger) As UByte
	Declare Function arraySJoystickInfo_ctor() As Any Ptr
	Declare Function arraySJoystickInfo_allocated_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function arraySJoystickInfo_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub arraySJoystickInfo_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub arraySJoystickInfo_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function arraySJoystickInfo_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function SEvent_GetSLogEvent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SLogEvent_GetText(ByVal _pointer_ As Any Ptr) As WString Ptr
	'Declare Function SLogEvent_GetText(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function SLogEvent_GetLevel(ByVal _pointer_ As Any Ptr) As ELOG_LEVEL
	Declare Function SEvent_GetSUserEvent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SUserEvent_GetUserData1(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SUserEvent_GetUserData2(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SEvent_GetSInputMethodEvent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SInputMethodEvent_GetHandle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SInputMethodEvent_GetChar(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function SInputMethodEvent_GetEvent(ByVal _pointer_ As Any Ptr) As EINPUT_METHOD_EVENT
	Declare Function IEventReceiver_ctor1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IEventReceiver_ctor2(ByVal _On_EventMethod As EVENT_METHOD) As Any Ptr
	Declare Sub IEventReceiver_set_func_event(ByVal _pointer_ As Any Ptr, ByVal _On_EventMethod As EVENT_METHOD)
	Declare Function IEventReceiverV_virt_ctor() As Any Ptr
	Declare Function IEventReceiverV_set_func_event(ByVal _pointer_ As Any Ptr, ByVal _On_EventMethod As Any Ptr) As UByte
	Declare Function IReferenceCounted_ctor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IReferenceCounted_grab(ByVal _pointer_ As Any Ptr)
	Declare Function IReferenceCounted_drop(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IReferenceCounted_getReferenceCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IReferenceCounted_getDebugName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function IReferenceCounted_is_null(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IrrlichtDevice_createDevice(ByVal deviceType As E_DRIVER_TYPE, ByVal windowSize As Any Ptr, ByVal bits As UInteger, ByVal fullscreen As UByte, ByVal stencilbuffer As UByte, ByVal vsync As UByte, ByVal receiver As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_createDevice2(ByVal deviceType As E_DRIVER_TYPE, ByVal windowSize As Any Ptr, ByVal bits As UInteger, ByVal fullscreen As UByte, ByVal stencilbuffer As UByte, ByVal vsync As UByte, ByVal create_receiver As UByte) As Any Ptr
	Declare Function IrrlichtDevice_createDeviceEx(ByVal parameters As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_run(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IrrlichtDevice_yield(ByVal _pointer_ As Any Ptr)
	Declare Sub IrrlichtDevice_sleep(ByVal _pointer_ As Any Ptr, ByVal timeMs As UInteger, ByVal pauseTimer As UByte)
	Declare Function IrrlichtDevice_getVideoDriver(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getFileSystem(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getGUIEnvironment(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getSceneManager(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getCursorControl(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getLogger(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getVideoModeList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getOSOperator(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_getTimer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IrrlichtDevice_setWindowCaption(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Function IrrlichtDevice_isWindowActive(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IrrlichtDevice_isWindowFocused(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IrrlichtDevice_isWindowMinimized(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IrrlichtDevice_isFullscreen(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IrrlichtDevice_getColorFormat(ByVal _pointer_ As Any Ptr) As ECOLOR_FORMAT
	Declare Sub IrrlichtDevice_closeDevice(ByVal _pointer_ As Any Ptr)
	Declare Function IrrlichtDevice_getVersion(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub IrrlichtDevice_setEventReceiver(ByVal _pointer_ As Any Ptr, ByVal receiver As Any Ptr)
	Declare Function IrrlichtDevice_getEventReceiver(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IrrlichtDevice_postEventFromUser(ByVal _pointer_ As Any Ptr, ByVal event As Any Ptr) As UByte
	Declare Sub IrrlichtDevice_setInputReceivingSceneManager(ByVal _pointer_ As Any Ptr, ByVal sceneManager As Any Ptr)
	Declare Sub IrrlichtDevice_setResizable(ByVal _pointer_ As Any Ptr, ByVal resize As UByte)
	Declare Sub IrrlichtDevice_minimizeWindow(ByVal _pointer_ As Any Ptr)
	Declare Sub IrrlichtDevice_maximizeWindow(ByVal _pointer_ As Any Ptr)
	Declare Sub IrrlichtDevice_restoreWindow(ByVal _pointer_ As Any Ptr)
	Declare Function IrrlichtDevice_activateJoysticks(ByVal _pointer_ As Any Ptr, ByVal joystickInfo As Any Ptr) As UByte
	Declare Function IrrlichtDevice_setGammaRamp(ByVal _pointer_ As Any Ptr, ByVal red As Single, ByVal green As Single, ByVal blue As Single, ByVal relativebrightness As Single, ByVal relativecontrast As Single) As UByte
	Declare Function IrrlichtDevice_getGammaRamp(ByVal _pointer_ As Any Ptr, ByVal red As Single, ByVal green As Single, ByVal blue As Single, ByVal brightness As Single, ByVal contrast As Single) As UByte
	Declare Function IrrlichtDevice_getType(ByVal _pointer_ As Any Ptr) As E_DEVICE_TYPE
	Declare Function IrrlichtDevice_isDriverSupported(ByVal _pointer_ As Any Ptr, ByVal driver As E_DRIVER_TYPE) As UByte
	Declare Function IFileSystem_createAndOpenFile(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IFileSystem_createMemoryReadFile(ByVal _pointer_ As Any Ptr, ByVal memory As Any Ptr, ByVal _len_ As Integer, ByVal filename As fschar, ByVal deleteMemoryWhenDropped As UByte) As Any Ptr
	Declare Function IFileSystem_createLimitReadFile(ByVal _pointer_ As Any Ptr, ByVal filename As fschar, ByVal alreadyOpenedFile As Any Ptr, ByVal pos As Long, ByVal areaSize As Long) As Any Ptr
	Declare Function IFileSystem_createMemoryWriteFile(ByVal _pointer_ As Any Ptr, ByVal memory As Any Ptr, ByVal _len_ As Integer, ByVal filename As fschar, ByVal deleteMemoryWhenDropped As UByte) As Any Ptr
	Declare Function IFileSystem_createAndWriteFile(ByVal _pointer_ As Any Ptr, ByVal filename As fschar, ByVal _append_ As UByte) As Any Ptr
	Declare Function IFileSystem_addFileArchive(ByVal _pointer_ As Any Ptr, ByVal filename As fschar, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte, ByVal archiveType As E_FILE_ARCHIVE_TYPE) As UByte
	Declare Sub IFileSystem_addArchiveLoader(ByVal _pointer_ As Any Ptr, ByVal loader As Any Ptr)
	Declare Function IFileSystem_getFileArchiveCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IFileSystem_removeFileArchive1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As UByte
	Declare Function IFileSystem_removeFileArchive2(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As UByte
	Declare Function IFileSystem_moveFileArchive(ByVal _pointer_ As Any Ptr, ByVal sourceIndex As UInteger, ByVal relative As Integer) As UByte
	Declare Function IFileSystem_getFileArchive(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IFileSystem_addZipFileArchive(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As UByte
	Declare Function IFileSystem_addFolderFileArchive(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As UByte
	Declare Function IFileSystem_addPakFileArchive(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As UByte
	Declare Function IFileSystem_getWorkingDirectory(ByVal _pointer_ As Any Ptr) As fschar
	Declare Function IFileSystem_changeWorkingDirectoryTo(ByVal _pointer_ As Any Ptr, ByVal newDirectory As fschar) As UByte
	Declare Function IFileSystem_getAbsolutePath(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As fschar
	Declare Function IFileSystem_getFileDir(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As fschar
	Declare Function IFileSystem_getFileBasename(ByVal _pointer_ As Any Ptr, ByVal filename As fschar, ByVal keepExtension As UByte) As fschar
	Declare Function IFileSystem_flattenFilename(ByVal _pointer_ As Any Ptr, ByVal directory As fschar, ByVal root As fschar) As fschar
	Declare Function IFileSystem_createFileList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IFileSystem_createEmptyFileList(ByVal _pointer_ As Any Ptr, ByVal _path As fschar, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As Any Ptr
	Declare Function IFileSystem_setFileListSystem(ByVal _pointer_ As Any Ptr, ByVal listType As EFileSystemType) As EFileSystemType
	Declare Function IFileSystem_existFile(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As UByte
	Declare Function IFileSystem_createXMLReader1(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IFileSystem_createXMLReader2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IFileSystem_createXMLReaderUTF8(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IFileSystem_createXMLReaderUTF8stream(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IFileSystem_createXMLWriter1(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IFileSystem_createXMLWriter2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IFileSystem_createEmptyAttributes(ByVal _pointer_ As Any Ptr, ByVal driver As Any Ptr) As Any Ptr
	Declare Sub IGUIEnvironment_drawAll(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIEnvironment_setFocus(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As UByte
	Declare Function IGUIEnvironment_getFocus(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_removeFocus(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As UByte
	Declare Function IGUIEnvironment_hasFocus(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As UByte
	Declare Function IGUIEnvironment_getVideoDriver(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_getFileSystem(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_getOSOperator(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIEnvironment_clear(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIEnvironment_postEventFromUser(ByVal _pointer_ As Any Ptr, ByVal event As Any Ptr) As UByte
	Declare Sub IGUIEnvironment_setUserEventReceiver(ByVal _pointer_ As Any Ptr, ByVal evr As Any Ptr)
	Declare Function IGUIEnvironment_getSkin(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIEnvironment_setSkin(ByVal _pointer_ As Any Ptr, ByVal skin As Any Ptr)
	Declare Function IGUIEnvironment_createSkin(ByVal _pointer_ As Any Ptr, ByVal _type_ As EGUI_SKIN_TYPE) As Any Ptr
	Declare Function IGUIEnvironment_createImageList(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal imageSize As Any Ptr, ByVal useAlphaChannel As UByte) As Any Ptr
	Declare Function IGUIEnvironment_getFont(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_getBuiltInFont(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_getSpriteBank(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addEmptySpriteBank(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_getRootGUIElement(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addButton(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr, ByVal _to_oltiptext As WString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addWindow(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal _mod_al As UByte, ByVal text As WString Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addModalScreen(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addMessageBox(ByVal _pointer_ As Any Ptr, ByVal caption As WString Ptr, ByVal text As WString Ptr, ByVal _mod_al As UByte, ByVal flags As Integer, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addScrollBar(ByVal _pointer_ As Any Ptr, ByVal horizontal As UByte, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addImage(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr, ByVal pos As Any Ptr, ByVal useAlphaChannel As UByte, ByVal parent As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addImage2(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addCheckBox(ByVal _pointer_ As Any Ptr, ByVal checked As UByte, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addListBox(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal _draw_Background As UByte) As Any Ptr
	Declare Function IGUIEnvironment_addTreeView(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal _draw_Background As UByte, ByVal scrollBarVertical As UByte, ByVal scrollBarHorizontal As UByte) As Any Ptr
	Declare Function IGUIEnvironment_addMeshViewer(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr) As Any Ptr
	Declare Function IGUIEnvironment_addFileOpenDialog(ByVal _pointer_ As Any Ptr, ByVal title As WString Ptr, ByVal _mod_al As UByte, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addColorSelectDialog(ByVal _pointer_ As Any Ptr, ByVal title As WString Ptr, ByVal _mod_al As UByte, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addStaticText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal rectangle As Any Ptr, ByVal border As UByte, ByVal wordWrap As UByte, ByVal parent As Any Ptr, ByVal id As Integer, ByVal fillBackground As UByte) As Any Ptr
	Declare Function IGUIEnvironment_addEditBox(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal rectangle As Any Ptr, ByVal border As UByte, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addSpinBox(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal rectangle As Any Ptr, ByVal border As UByte, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addInOutFader(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addTabControl(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal fillbackground As UByte, ByVal border As UByte, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addTab(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addContextMenu(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addMenu(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addToolBar(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addComboBox(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUIEnvironment_addTable(ByVal _pointer_ As Any Ptr, ByVal rectangle As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal _draw_Background As UByte) As Any Ptr
	Declare Function IGUIEnvironment_getDefaultGUIElementFactory(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIEnvironment_registerGUIElementFactory(ByVal _pointer_ As Any Ptr, ByVal factoryToAdd As Any Ptr)
	Declare Function IGUIEnvironment_getRegisteredGUIElementFactoryCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUIEnvironment_getGUIElementFactory(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IGUIEnvironment_addGUIElement(ByVal _pointer_ As Any Ptr, ByVal elementName As ZString Ptr, ByVal parent As Any Ptr) As Any Ptr
	Declare Function IGUIEnvironment_saveGUI(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal start As Any Ptr) As UByte
	Declare Function IGUIEnvironment_saveGUI2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal start As Any Ptr) As UByte
	Declare Function IGUIEnvironment_loadGUI(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal parent As Any Ptr) As UByte
	Declare Function IGUIEnvironment_loadGUI2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal parent As Any Ptr) As UByte
	Declare Sub IGUIEnvironment_serializeAttributes(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal options As Any Ptr)
	Declare Sub IGUIEnvironment_deserializeAttributes(ByVal _pointer_ As Any Ptr, ByVal in As Any Ptr, ByVal options As Any Ptr)
	Declare Sub IGUIEnvironment_writeGUIElement(ByVal _pointer_ As Any Ptr, ByVal writer As Any Ptr, ByVal node As Any Ptr)
	Declare Sub IGUIEnvironment_readGUIElement(ByVal _pointer_ As Any Ptr, ByVal reader As Any Ptr, ByVal node As Any Ptr)
	Declare Function IGUIEnvironment_getTTFont(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal fontsize As UInteger, ByVal antialias As UByte, ByVal transparency As UByte) As Any Ptr
	Declare Function ISceneManager_getMesh(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function ISceneManager_getMesh2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getMeshCache(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getVideoDriver(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getGUIEnvironment(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getFileSystem(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addVolumeLightSceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal subdivU As UInteger, ByVal subdivV As UInteger, ByVal foot As Any Ptr, ByVal tail As Any Ptr, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addCubeSceneNode(ByVal _pointer_ As Any Ptr, ByVal _size_ As Single, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addSphereSceneNode(ByVal _pointer_ As Any Ptr, ByVal radius As Single, ByVal polyCount As Integer, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addAnimatedMeshSceneNode(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addAnimatedMeshSceneNode2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addMeshSceneNode(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addWaterSurfaceSceneNode(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal waveHeight As Single, ByVal waveSpeed As Single, ByVal waveLength As Single, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addOctTreeSceneNode(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal minimalPolysPerNode As Integer, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addOctTreeSceneNode2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal minimalPolysPerNode As Integer, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addOctreeSceneNode(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal minimalPolysPerNode As Integer, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addOctreeSceneNode2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal minimalPolysPerNode As Integer, ByVal alsoAddIfMeshPointerZero As UByte) As Any Ptr
	Declare Function ISceneManager_addCameraSceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal position As Any Ptr, ByVal lookat As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addCameraSceneNodeMaya(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal rotateSpeed As Single, ByVal zoomSpeed As Single, ByVal translationSpeed As Single, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addCameraSceneNodeFPS(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal rotateSpeed As Single, ByVal moveSpeed As Single, ByVal id As Integer, ByVal keyMapArray As Any Ptr, ByVal keyMapSize As Integer, ByVal noVerticalMovement As UByte, ByVal jumpSpeed As Single, ByVal invertMouse As UByte) As Any Ptr
	Declare Function ISceneManager_addCameraSceneNodeFPS2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addLightSceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal position As Any Ptr, ByVal _color_ As Any Ptr, ByVal radius As Single, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addBillboardSceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal _size_ As Any Ptr, ByVal position As Any Ptr, ByVal id As Integer, ByVal _color_Top As Any Ptr, ByVal _color_Bottom As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addSkyBoxSceneNode(ByVal _pointer_ As Any Ptr, ByVal _to_p As Any Ptr, ByVal bottom As Any Ptr, ByVal left As Any Ptr, ByVal right As Any Ptr, ByVal front As Any Ptr, ByVal back As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addSkyDomeSceneNode(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal horiRes As UInteger, ByVal vertRes As UInteger, ByVal texturePercentage As Single, ByVal spherePercentage As Single, ByVal radius As Single, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addParticleSystemSceneNode(ByVal _pointer_ As Any Ptr, ByVal withDefaultEmitter As UByte, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addTerrainSceneNode(ByVal _pointer_ As Any Ptr, ByVal heightMapFileName As ZString Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr, ByVal vertexColor As Any Ptr, ByVal maxLOD As Integer, ByVal patchSize As E_TERRAIN_PATCH_SIZE, ByVal smoothFactor As Integer, ByVal addAlsoIfHeightmapEmpty As UByte) As Any Ptr
	Declare Function ISceneManager_addTerrainSceneNode2(ByVal _pointer_ As Any Ptr, ByVal heightMapFile As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr, ByVal vertexColor As Any Ptr, ByVal maxLOD As Integer, ByVal patchSize As E_TERRAIN_PATCH_SIZE, ByVal smoothFactor As Integer, ByVal addAlsoIfHeightmapEmpty As UByte) As Any Ptr
	Declare Function ISceneManager_addQuake3SceneNode(ByVal _pointer_ As Any Ptr, ByVal meshBuffer As Any Ptr, ByVal shader As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addEmptySceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addDummyTransformationSceneNode(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addTextSceneNode(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr, ByVal text As WString Ptr, ByVal _color_ As Any Ptr, ByVal parent As Any Ptr, ByVal position As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function ISceneManager_addBillboardTextSceneNode(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr, ByVal text As WString Ptr, ByVal parent As Any Ptr, ByVal _size_ As Any Ptr, ByVal position As Any Ptr, ByVal id As Integer, ByVal _color_Top As Any Ptr, ByVal _color_Bottom As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addHillPlaneMesh(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal tileSize As Any Ptr, ByVal tileCount As Any Ptr, ByVal material As Any Ptr, ByVal hillHeight As Single, ByVal countHills As Any Ptr, ByVal textureRepeatCount As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addTerrainMesh(ByVal _pointer_ As Any Ptr, ByVal meshname As ZString Ptr, ByVal texture As Any Ptr, ByVal heightmap As Any Ptr, ByVal stretchSize As Any Ptr, ByVal maxHeight As Single, ByVal defaultVertexBlockSize As Any Ptr) As Any Ptr
	Declare Function ISceneManager_addArrowMesh(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal vtxColor0 As Any Ptr, ByVal vtxColor1 As Any Ptr, ByVal tesselationCylinder As UInteger, ByVal tesselationCone As UInteger, ByVal height As Single, ByVal cylinderHeight As Single, ByVal _width_0 As Single, ByVal _width_1 As Single) As Any Ptr
	Declare Function ISceneManager_addSphereMesh(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal radius As Single, ByVal polyCountX As UInteger, ByVal polyCountY As UInteger) As Any Ptr
	Declare Function ISceneManager_addVolumeLightMesh(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal SubdivideU As UInteger, ByVal SubdivideV As UInteger, ByVal FootColor As Any Ptr, ByVal TailColor As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getRootSceneNode(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getSceneNodeFromId(ByVal _pointer_ As Any Ptr, ByVal id As Integer, ByVal start As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getSceneNodeFromName(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal start As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getSceneNodeFromType(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_TYPE, ByVal start As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_getSceneNodesFromType(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_TYPE, ByVal outNodes As Any Ptr, ByVal start As Any Ptr)
	Declare Function ISceneManager_getActiveCamera(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_setActiveCamera(ByVal _pointer_ As Any Ptr, ByVal camera As Any Ptr)
	Declare Sub ISceneManager_setShadowColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Function ISceneManager_getShadowColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_registerNodeForRendering(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr, ByVal pass As E_SCENE_NODE_RENDER_PASS) As UInteger
	Declare Sub ISceneManager_drawAll(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneManager_createRotationAnimator(ByVal _pointer_ As Any Ptr, ByVal rotationSpeed As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createFlyCircleAnimator(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal radius As Single, ByVal speed As Single, ByVal direction As Any Ptr, ByVal startPosition As Single, ByVal radiusEllipsoid As Single) As Any Ptr
	Declare Function ISceneManager_createFlyStraightAnimator(ByVal _pointer_ As Any Ptr, ByVal startPoint As Any Ptr, ByVal _end_Point As Any Ptr, ByVal timeForWay As UInteger, ByVal _loop_ As UByte, ByVal pingpong As UByte) As Any Ptr
	Declare Function ISceneManager_createTextureAnimator(ByVal _pointer_ As Any Ptr, ByVal textures As Any Ptr, ByVal timePerFrame As Integer, ByVal _loop_ As UByte) As Any Ptr
	Declare Function ISceneManager_createDeleteAnimator(ByVal _pointer_ As Any Ptr, ByVal timeMs As UInteger) As Any Ptr
	Declare Function ISceneManager_createCollisionResponseAnimator(ByVal _pointer_ As Any Ptr, ByVal world As Any Ptr, ByVal sceneNode As Any Ptr, ByVal ellipsoidRadius As Any Ptr, ByVal gravityPerSecond As Any Ptr, ByVal ellipsoidTranslation As Any Ptr, ByVal slidingValue As Single) As Any Ptr
	Declare Function ISceneManager_createFollowSplineAnimator(ByVal _pointer_ As Any Ptr, ByVal startTime As Integer, ByVal _point_s As Any Ptr, ByVal speed As Single, ByVal tightness As Single) As Any Ptr
	Declare Function ISceneManager_createTriangleSelector1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal node As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createTriangleSelector2(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createTriangleSelectorFromBoundingBox(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createOctTreeTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal node As Any Ptr, ByVal minimalPolysPerNode As Integer) As Any Ptr
	Declare Function ISceneManager_createOctreeTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal node As Any Ptr, ByVal minimalPolysPerNode As Integer) As Any Ptr
	Declare Function ISceneManager_createMetaTriangleSelector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createTerrainTriangleSelector(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr, ByVal LOD As Integer) As Any Ptr
	Declare Sub ISceneManager_addExternalMeshLoader(ByVal _pointer_ As Any Ptr, ByVal externalLoader As Any Ptr)
	Declare Function ISceneManager_getSceneCollisionManager(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getMeshManipulator(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_addToDeletionQueue(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Function ISceneManager_postEventFromUser(ByVal _pointer_ As Any Ptr, ByVal event As Any Ptr) As UByte
	Declare Sub ISceneManager_clear(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneManager_getParameters(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_getSceneNodeRenderPass(ByVal _pointer_ As Any Ptr) As E_SCENE_NODE_RENDER_PASS
	Declare Function ISceneManager_getDefaultSceneNodeFactory(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_registerSceneNodeFactory(ByVal _pointer_ As Any Ptr, ByVal factoryToAdd As Any Ptr)
	Declare Function ISceneManager_getRegisteredSceneNodeFactoryCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ISceneManager_getSceneNodeFactory(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function ISceneManager_getDefaultSceneNodeAnimatorFactory(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_registerSceneNodeAnimatorFactory(ByVal _pointer_ As Any Ptr, ByVal factoryToAdd As Any Ptr)
	Declare Function ISceneManager_getRegisteredSceneNodeAnimatorFactoryCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ISceneManager_getSceneNodeAnimatorFactory(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function ISceneManager_getSceneNodeTypeName(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_TYPE) As ZString Ptr
	Declare Function ISceneManager_getAnimatorTypeName(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_ANIMATOR_TYPE) As ZString Ptr
	Declare Function ISceneManager_addSceneNode(ByVal _pointer_ As Any Ptr, ByVal sceneNodeTypeName As ZString Ptr, ByVal parent As Any Ptr) As Any Ptr
	Declare Function ISceneManager_createNewSceneManager(ByVal _pointer_ As Any Ptr, ByVal cloneContent As UByte) As Any Ptr
	Declare Function ISceneManager_saveScene(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal userDataSerializer As Any Ptr) As UByte
	Declare Function ISceneManager_saveScene2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal userDataSerializer As Any Ptr) As UByte
	Declare Function ISceneManager_loadScene(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal userDataSerializer As Any Ptr) As UByte
	Declare Function ISceneManager_loadScene2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal userDataSerializer As Any Ptr) As UByte
	Declare Function ISceneManager_createMeshWriter(ByVal _pointer_ As Any Ptr, ByVal _type_ As EMESH_WRITER_TYPE) As Any Ptr
	Declare Function ISceneManager_createSkinnedMesh(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_setAmbientLight(ByVal _pointer_ As Any Ptr, ByVal ambientColor As Any Ptr)
	Declare Function ISceneManager_getAmbientLight(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ISceneManager_setLightManager(ByVal _pointer_ As Any Ptr, ByVal lightManager As Any Ptr)
	Declare Function ISceneManager_getGeometryCreator(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ISceneManager_isCulled(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr) As UByte
	Declare Function SOverrideMaterial_ctor() As Any Ptr
	Declare Sub SOverrideMaterial_apply(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr)
	Declare Function SOverrideMaterial_get_Material(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SOverrideMaterial_set_Material(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SOverrideMaterial_get_EnableFlags(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SOverrideMaterial_set_EnableFlags(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SOverrideMaterial_get_EnablePasses(ByVal _pointer_ As Any Ptr) As UShort
	Declare Sub SOverrideMaterial_set_EnablePasses(ByVal _pointer_ As Any Ptr, ByVal value As UShort)
	Declare Function SOverrideMaterial_get_Enabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SOverrideMaterial_set_Enabled(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function IRenderTarget_ctor1(ByVal texture As Any Ptr, ByVal _color_Mask As E_COLOR_PLANE, ByVal blendFuncSrc As E_BLEND_FACTOR, ByVal blendFuncDst As E_BLEND_FACTOR, ByVal blendEnable As UByte) As Any Ptr
	Declare Function IRenderTarget_ctor2(ByVal target As E_RENDER_TARGET, ByVal _color_Mask As E_COLOR_PLANE, ByVal blendFuncSrc As E_BLEND_FACTOR, ByVal blendFuncDst As E_BLEND_FACTOR, ByVal blendEnable As UByte) As Any Ptr
	Declare Function IRenderTarget_get_RenderTexture(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IRenderTarget_set_RenderTexture(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function IRenderTarget_get_TargetType(ByVal _pointer_ As Any Ptr) As E_RENDER_TARGET
	Declare Sub IRenderTarget_set_TargetType(ByVal _pointer_ As Any Ptr, ByVal value As E_RENDER_TARGET)
	Declare Function IRenderTarget_get_ColorMask(ByVal _pointer_ As Any Ptr) As E_COLOR_PLANE
	Declare Sub IRenderTarget_set_ColorMask(ByVal _pointer_ As Any Ptr, ByVal value As E_COLOR_PLANE)
	Declare Function IRenderTarget_get_BlendFuncSrc(ByVal _pointer_ As Any Ptr) As E_BLEND_FACTOR
	Declare Sub IRenderTarget_set_BlendFuncSrc(ByVal _pointer_ As Any Ptr, ByVal value As E_BLEND_FACTOR)
	Declare Function IRenderTarget_get_BlendFuncDst(ByVal _pointer_ As Any Ptr) As E_BLEND_FACTOR
	Declare Sub IRenderTarget_set_BlendFuncDst(ByVal _pointer_ As Any Ptr, ByVal value As E_BLEND_FACTOR)
	Declare Function IRenderTarget_get_BlendEnable(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IRenderTarget_set_BlendEnable(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function IVideoDriver_beginScene(ByVal _pointer_ As Any Ptr, ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As Any Ptr, ByVal videoData As Any Ptr, ByVal sourceRect As Any Ptr) As UByte
	Declare Function IVideoDriver_beginSceneDefault(ByVal _pointer_ As Any Ptr, ByVal backBuffer As UByte, ByVal zBuffer As UByte, ByVal _color_ As Any Ptr) As UByte
	Declare Function IVideoDriver_endScene(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IVideoDriver_queryFeature(ByVal _pointer_ As Any Ptr, ByVal feature As E_VIDEO_DRIVER_FEATURE) As UByte
	Declare Sub IVideoDriver_disableFeature(ByVal _pointer_ As Any Ptr, ByVal feature As E_VIDEO_DRIVER_FEATURE, ByVal flag As UByte)
	Declare Function IVideoDriver_checkDriverReset(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IVideoDriver_setTransform(ByVal _pointer_ As Any Ptr, ByVal state As E_TRANSFORMATION_STATE, ByVal mat As Any Ptr)
	Declare Function IVideoDriver_getTransform(ByVal _pointer_ As Any Ptr, ByVal state As E_TRANSFORMATION_STATE) As Any Ptr
	Declare Function IVideoDriver_getImageLoaderCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVideoDriver_getImageLoader(ByVal _pointer_ As Any Ptr, ByVal n As UInteger) As Any Ptr
	Declare Function IVideoDriver_getImageWriterCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVideoDriver_getImageWriter(ByVal _pointer_ As Any Ptr, ByVal n As UInteger) As Any Ptr
	Declare Sub IVideoDriver_setMaterial(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr)
	Declare Function IVideoDriver_getTexture1(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IVideoDriver_getTexture2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getTextureByIndex(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IVideoDriver_getTextureCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IVideoDriver_renameTexture(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal newName As fschar)
	Declare Function IVideoDriver_addTexture1(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr, ByVal _name_ As fschar, ByVal format As ECOLOR_FORMAT) As Any Ptr
	Declare Function IVideoDriver_addTexture2(ByVal _pointer_ As Any Ptr, ByVal _name_ As fschar, ByVal image As Any Ptr, ByVal mipmapData As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_addRenderTargetTexture(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr, ByVal _name_ As fschar, ByVal format As ECOLOR_FORMAT) As Any Ptr
	'Declare Function IVideoDriver_addRenderTargetTexture(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr, ByVal _name_ As fschar, ByVal format As ECOLOR_FORMAT) As Any Ptr
	Declare Sub IVideoDriver_removeTexture(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr)
	Declare Sub IVideoDriver_removeAllTextures(ByVal _pointer_ As Any Ptr)
	Declare Sub IVideoDriver_removeHardwareBuffer(ByVal _pointer_ As Any Ptr, ByVal mb As Any Ptr)
	Declare Sub IVideoDriver_removeAllHardwareBuffers(ByVal _pointer_ As Any Ptr)
	Declare Sub IVideoDriver_makeColorKeyTexture(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal _color_ As Any Ptr, ByVal zeroTexels As UByte)
	Declare Sub IVideoDriver_makeColorKeyTexture2(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal _color_KeyPixelPos As Any Ptr, ByVal zeroTexels As UByte)
	Declare Sub IVideoDriver_makeNormalMapTexture(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal amplitude As Single)
	Declare Function IVideoDriver_setRenderTarget(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal clearBackBuffer As UByte, ByVal _clearZBuffer_ As UByte, ByVal _color_ As Any Ptr) As UByte
	Declare Function IVideoDriver_setRenderTarget2(ByVal _pointer_ As Any Ptr, ByVal target As E_RENDER_TARGET, ByVal clearTarget As UByte, ByVal _clearZBuffer_ As UByte, ByVal _color_ As Any Ptr) As UByte
	Declare Sub IVideoDriver_setViewPort(ByVal _pointer_ As Any Ptr, ByVal area As Any Ptr)
	Declare Function IVideoDriver_getViewPort(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IVideoDriver_drawVertexPrimitiveList(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal primCount As UInteger, ByVal vType As E_VERTEX_TYPE, ByVal pType As E_PRIMITIVE_TYPE, ByVal iType As E_INDEX_TYPE)
	Declare Sub IVideoDriver_draw2DVertexPrimitiveList(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal primCount As UInteger, ByVal vType As E_VERTEX_TYPE, ByVal pType As E_PRIMITIVE_TYPE, ByVal iType As E_INDEX_TYPE)
	Declare Sub IVideoDriver_drawIndexedTriangleList(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal triangleCount As UInteger)
	Declare Sub IVideoDriver_drawIndexedTriangleList2(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal triangleCount As UInteger)
	Declare Sub IVideoDriver_drawIndexedTriangleList3(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal triangleCount As UInteger)
	Declare Sub IVideoDriver_drawIndexedTriangleFan(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal triangleCount As UInteger)
	Declare Sub IVideoDriver_drawIndexedTriangleFan2(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal vertexCount As UInteger, ByVal indexList As Any Ptr, ByVal triangleCount As UInteger)
	Declare Sub IVideoDriver_draw3DLine(ByVal _pointer_ As Any Ptr, ByVal start As Any Ptr, ByVal _end_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_draw3DTriangle(ByVal _pointer_ As Any Ptr, ByVal triangle As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_draw3DBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_draw2DImage1(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal destPos As Any Ptr)
	Declare Sub IVideoDriver_draw2DImage2(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal destPos As Any Ptr, ByVal sourceRect As Any Ptr, ByVal clipRect As Any Ptr, ByVal _color_ As Any Ptr, ByVal useAlphaChannelOfTexture As UByte)
	Declare Sub IVideoDriver_draw2DImage3(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal destRect As Any Ptr, ByVal sourceRect As Any Ptr, ByVal clipRect As Any Ptr, ByVal _color_s As Any Ptr, ByVal useAlphaChannelOfTexture As UByte)
	Declare Sub IVideoDriver_draw2DImageBatch1(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal pos As Any Ptr, ByVal sourceRects As Any Ptr, ByVal indices As Any Ptr, ByVal kerningWidth As Integer, ByVal clipRect As Any Ptr, ByVal _color_ As Any Ptr, ByVal useAlphaChannelOfTexture As UByte)
	Declare Sub IVideoDriver_draw2DImageBatch2(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal positions As Any Ptr, ByVal sourceRects As Any Ptr, ByVal clipRect As Any Ptr, ByVal _color_ As Any Ptr, ByVal useAlphaChannelOfTexture As UByte)
	Declare Sub IVideoDriver_draw2DRectangle1(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr, ByVal pos As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IVideoDriver_draw2DRectangle2(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr, ByVal _color_LeftUp As Any Ptr, ByVal _color_RightUp As Any Ptr, ByVal _color_LeftDown As Any Ptr, ByVal _color_RightDown As Any Ptr, ByVal clip As Any Ptr)
	Declare Sub IVideoDriver_draw2DRectangleOutline(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_draw2DLine(ByVal _pointer_ As Any Ptr, ByVal start As Any Ptr, ByVal _end_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_drawPixel(ByVal _pointer_ As Any Ptr, ByVal x As UInteger, ByVal y As UInteger, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_draw2DPolygon(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal radius As Single, ByVal _color_ As Any Ptr, ByVal vertexCount As Integer)
	Declare Sub IVideoDriver_drawStencilShadowVolume(ByVal _pointer_ As Any Ptr, ByVal triangles As Any Ptr, ByVal count As Integer, ByVal zfail As UByte)
	Declare Sub IVideoDriver_drawStencilShadow(ByVal _pointer_ As Any Ptr, ByVal clearStencilBuffer As UByte, ByVal leftUpEdge As Any Ptr, ByVal rightUpEdge As Any Ptr, ByVal leftDownEdge As Any Ptr, ByVal rightDownEdge As Any Ptr)
	Declare Sub IVideoDriver_drawMeshBuffer(ByVal _pointer_ As Any Ptr, ByVal mb As Any Ptr)
	Declare Sub IVideoDriver_setFog(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr, ByVal fogType As E_FOG_TYPE, ByVal start As Single, ByVal _end_ As Single, ByVal density As Single, ByVal pixelFog As UByte, ByVal rangeFog As UByte)
	Declare Function IVideoDriver_getColorFormat(ByVal _pointer_ As Any Ptr) As ECOLOR_FORMAT
	Declare Function IVideoDriver_getScreenSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getCurrentRenderTargetSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getFPS(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IVideoDriver_getPrimitiveCountDrawn(ByVal _pointer_ As Any Ptr, ByVal _mod_e As UInteger) As UInteger
	Declare Sub IVideoDriver_deleteAllDynamicLights(ByVal _pointer_ As Any Ptr)
	Declare Function IVideoDriver_addDynamicLight(ByVal _pointer_ As Any Ptr, ByVal light As Any Ptr) As Integer
	Declare Function IVideoDriver_getMaximalDynamicLightAmount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVideoDriver_getDynamicLightCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVideoDriver_getDynamicLight(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As Any Ptr
	Declare Sub IVideoDriver_turnLightOn(ByVal _pointer_ As Any Ptr, ByVal lightIndex As Integer, ByVal turnOn As UByte)
	Declare Function IVideoDriver_getName(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Sub IVideoDriver_addExternalImageLoader(ByVal _pointer_ As Any Ptr, ByVal loader As Any Ptr)
	Declare Sub IVideoDriver_addExternalImageWriter(ByVal _pointer_ As Any Ptr, ByVal writer As Any Ptr)
	Declare Function IVideoDriver_getMaximalPrimitiveCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IVideoDriver_setTextureCreationFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_TEXTURE_CREATION_FLAG, ByVal enabled As UByte)
	Declare Function IVideoDriver_getTextureCreationFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_TEXTURE_CREATION_FLAG) As UByte
	Declare Function IVideoDriver_createImageFromFile1(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IVideoDriver_createImageFromFile2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_writeImageToFile1(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr, ByVal filename As fschar, ByVal param As UInteger) As UByte
	Declare Function IVideoDriver_writeImageToFile2(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr, ByVal file As Any Ptr, ByVal param As UInteger) As UByte
	Declare Function IVideoDriver_createImageFromData(ByVal _pointer_ As Any Ptr, ByVal format As ECOLOR_FORMAT, ByVal _size_ As Any Ptr, ByVal _data_ As Any Ptr, ByVal ownForeignMemory As UByte, ByVal deleteMemory As UByte) As Any Ptr
	Declare Function IVideoDriver_createImage1(ByVal _pointer_ As Any Ptr, ByVal format As ECOLOR_FORMAT, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_createImage2(ByVal _pointer_ As Any Ptr, ByVal format As ECOLOR_FORMAT, ByVal imageToCopy As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_createImage3(ByVal _pointer_ As Any Ptr, ByVal imageToCopy As Any Ptr, ByVal pos As Any Ptr, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_createImage4(ByVal _pointer_ As Any Ptr, ByVal texture As Any Ptr, ByVal pos As Any Ptr, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Sub IVideoDriver_OnResize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Function IVideoDriver_addMaterialRenderer(ByVal _pointer_ As Any Ptr, ByVal renderer As Any Ptr, ByVal _name_ As ZString Ptr) As Integer
	Declare Function IVideoDriver_getMaterialRenderer(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As Any Ptr
	Declare Function IVideoDriver_getMaterialRendererCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVideoDriver_getMaterialRendererName(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As ZString Ptr
	Declare Sub IVideoDriver_setMaterialRendererName(ByVal _pointer_ As Any Ptr, ByVal idx As Integer, ByVal _name_ As ZString Ptr)
	Declare Function IVideoDriver_createAttributesFromMaterial(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr) As Any Ptr
	Declare Sub IVideoDriver_fillMaterialStructureFromAttributes(ByVal _pointer_ As Any Ptr, ByVal outMaterial As Any Ptr, ByVal attributes As Any Ptr)
	Declare Function IVideoDriver_getExposedVideoData(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getDriverType(ByVal _pointer_ As Any Ptr) As E_DRIVER_TYPE
	Declare Function IVideoDriver_getGPUProgrammingServices(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getMeshManipulator(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IVideoDriver_clearZBuffer(ByVal _pointer_ As Any Ptr)
	Declare Function IVideoDriver_createScreenShot(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_findTexture(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As Any Ptr
	Declare Function IVideoDriver_setClipPlane(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal plane As Any Ptr, ByVal enable As UByte) As UByte
	Declare Sub IVideoDriver_enableClipPlane(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal enable As UByte)
	Declare Sub IVideoDriver_setMinHardwareBufferVertexCount(ByVal _pointer_ As Any Ptr, ByVal count As UInteger)
	Declare Function IVideoDriver_getOverrideMaterial(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_getMaterial2D(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IVideoDriver_enableMaterial2D(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IVideoDriver_getVendorInfo(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub IVideoDriver_setAmbientLight(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IVideoDriver_setAllowZWriteOnTransparent(ByVal _pointer_ As Any Ptr, ByVal flag As UByte)
	Declare Function IVideoDriver_getMaxTextureSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoDriver_GetHandle(ByVal _pointer_ As Any Ptr) As Any Ptr
	'Declare Function IVideoDriver_GetHandle(ByVal _pointer_ As Any Ptr) As ULong
	Declare Sub IVideoDriver_SetIcon(ByVal _pointer_ As Any Ptr, ByVal icon_id As Integer, ByVal big_icon As UByte)
	Declare Sub ICursorControl_setVisible(ByVal _pointer_ As Any Ptr, ByVal visible As UByte)
	Declare Function ICursorControl_isVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ICursorControl_setPositionF(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub ICursorControl_setPositionF2(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single)
	Declare Sub ICursorControl_setPositionI(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr)
	Declare Sub ICursorControl_setPositionI2(ByVal _pointer_ As Any Ptr, ByVal x As Integer, ByVal y As Integer)
	Declare Function ICursorControl_getPosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ICursorControl_getRelativePosition(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub ICursorControl_setReferenceRect(ByVal _pointer_ As Any Ptr, ByVal rect As Any Ptr)
	Declare Function IAnimationEndCallBack_ctor1() As Any Ptr
	Declare Function IAnimationEndCallBack_ctor2(ByVal node As Any Ptr) As Any Ptr
	Declare Sub IAnimationEndCallBack_set_func_event(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Function IAnimationEndCallBack_UserAnimationEndCallBack(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Sub IAnimatedMeshSceneNode_setCurrentFrame(ByVal _pointer_ As Any Ptr, ByVal frame As Single)
	Declare Function IAnimatedMeshSceneNode_setFrameLoop(ByVal _pointer_ As Any Ptr, ByVal begin As Integer, ByVal _end_ As Integer) As UByte
	Declare Sub IAnimatedMeshSceneNode_setAnimationSpeed(ByVal _pointer_ As Any Ptr, ByVal framesPerSecond As Single)
	Declare Function IAnimatedMeshSceneNode_getAnimationSpeed(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IAnimatedMeshSceneNode_addShadowVolumeSceneNode(ByVal _pointer_ As Any Ptr, ByVal shadowMesh As Any Ptr, ByVal id As Integer, ByVal zfailmethod As UByte, ByVal infinity As Single) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_getJointNode1(ByVal _pointer_ As Any Ptr, ByVal jointName As ZString Ptr) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_getJointNode2(ByVal _pointer_ As Any Ptr, ByVal jointID As UInteger) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_getJointCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IAnimatedMeshSceneNode_getMS3DJointNode(ByVal _pointer_ As Any Ptr, ByVal jointName As ZString Ptr) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_getXJointNode(ByVal _pointer_ As Any Ptr, ByVal jointName As ZString Ptr) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_setMD2Animation1(ByVal _pointer_ As Any Ptr, ByVal anim As EMD2_ANIMATION_TYPE) As UByte
	Declare Function IAnimatedMeshSceneNode_setMD2Animation2(ByVal _pointer_ As Any Ptr, ByVal animationName As ZString Ptr) As UByte
	Declare Function IAnimatedMeshSceneNode_getFrameNr(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IAnimatedMeshSceneNode_getStartFrame(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IAnimatedMeshSceneNode_getEndFrame(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IAnimatedMeshSceneNode_setLoopMode(ByVal _pointer_ As Any Ptr, ByVal playAnimationLooped As UByte)
	Declare Sub IAnimatedMeshSceneNode_setAnimationEndCallback(ByVal _pointer_ As Any Ptr, ByVal callback As Any Ptr)
	Declare Sub IAnimatedMeshSceneNode_setReadOnlyMaterials(ByVal _pointer_ As Any Ptr, ByVal readonly As UByte)
	Declare Function IAnimatedMeshSceneNode_isReadOnlyMaterials(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IAnimatedMeshSceneNode_setMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Function IAnimatedMeshSceneNode_getMesh(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IAnimatedMeshSceneNode_getMD3TagTransformation(ByVal _pointer_ As Any Ptr, ByVal tagname As ZString Ptr) As Any Ptr
	Declare Sub IAnimatedMeshSceneNode_setJointMode(ByVal _pointer_ As Any Ptr, ByVal _mod_e As E_JOINT_UPDATE_ON_RENDER)
	Declare Sub IAnimatedMeshSceneNode_setTransitionTime(ByVal _pointer_ As Any Ptr, ByVal Time As Single)
	Declare Sub IAnimatedMeshSceneNode_animateJoints(ByVal _pointer_ As Any Ptr, ByVal CalculateAbsolutePositions As UByte)
	Declare Sub IAnimatedMeshSceneNode_setRenderFromIdentity(ByVal _pointer_ As Any Ptr, ByVal _On_ As UByte)
	Declare Function IAnimatedMeshSceneNode_clone(ByVal _pointer_ As Any Ptr, ByVal newParent As Any Ptr, ByVal newManager As Any Ptr) As Any Ptr
	Declare Sub IMeshSceneNode_setMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Function IMeshSceneNode_getMesh(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IMeshSceneNode_setReadOnlyMaterials(ByVal _pointer_ As Any Ptr, ByVal readonly As UByte)
	Declare Function IMeshSceneNode_isReadOnlyMaterials(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IAttributeExchangingObject_serializeAttributes(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal options As Any Ptr)
	Declare Sub IAttributeExchangingObject_deserializeAttributes(ByVal _pointer_ As Any Ptr, ByVal in As Any Ptr, ByVal options As Any Ptr)
	Declare Function IAnimatedMesh_getFrameCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IAnimatedMesh_getMesh(ByVal _pointer_ As Any Ptr, ByVal frame As Integer, ByVal detailLevel As Integer, ByVal startFrameLoop As Integer, ByVal _end_FrameLoop As Integer) As Any Ptr
	Declare Function IAnimatedMesh_getMeshType(ByVal _pointer_ As Any Ptr) As E_ANIMATED_MESH_TYPE
	Declare Function ITimer_getRealTime(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ITimer_getTime(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub ITimer_setTime(ByVal _pointer_ As Any Ptr, ByVal time As UInteger)
	Declare Sub ITimer_stop(ByVal _pointer_ As Any Ptr)
	Declare Sub ITimer_start(ByVal _pointer_ As Any Ptr)
	Declare Sub ITimer_setSpeed(ByVal _pointer_ As Any Ptr, ByVal speed As Single)
	Declare Function ITimer_getSpeed(ByVal _pointer_ As Any Ptr) As Single
	Declare Function ITimer_isStopped(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ITimer_tick(ByVal _pointer_ As Any Ptr)
	Declare Function D3D8_get_D3D8(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function D3D8_get_D3DDev8(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function D3D8_get_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub D3D8_set_D3D8(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub D3D8_set_D3DDev8(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub D3D8_set_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function D3D9_get_D3D9(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function D3D9_get_D3DDev9(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function D3D9_get_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub D3D9_set_D3D9(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub D3D9_set_D3DDev9(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub D3D9_set_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function OpenGLWin32_get_HDc(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function OpenGLWin32_get_HRc(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function OpenGLWin32_get_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub OpenGLWin32_set_HDc(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub OpenGLWin32_set_HRc(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub OpenGLWin32_set_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function OpenGLLinux_get_X11Display(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function OpenGLLinux_get_X11Context(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function OpenGLLinux_get_X11Window(ByVal _pointer_ As Any Ptr) As ULong
	Declare Sub OpenGLLinux_set_X11Display(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub OpenGLLinux_set_X11Context(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub OpenGLLinux_set_X11Window(ByVal _pointer_ As Any Ptr, ByVal value As ULong)
	Declare Function SExposedVideoData_ctor1() As Any Ptr
	Declare Function SExposedVideoData_ctor2(ByVal Window As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D8(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D8_D3D8(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D8_D3DDev8(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D8_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D9(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D9_D3D9(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D9_D3DDev9(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_D3D9_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLWin32(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLWin32_HDc(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLWin32_HRc(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLWin32_HWnd(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLLinux(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLLinux_X11Display(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLLinux_X11Context(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SExposedVideoData_get_OpenGLLinux_X11Window(ByVal _pointer_ As Any Ptr) As ULong
	Declare Sub SExposedVideoData_set_D3D8_D3D8(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_D3D8_D3DDev8(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_D3D8_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_D3D9_D3D9(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_D3D9_D3DDev9(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_D3D9_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLWin32_HDc(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLWin32_HRc(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLWin32_HWnd(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLLinux_X11Display(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLLinux_X11Context(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub SExposedVideoData_set_OpenGLLinux_X11Window(ByVal _pointer_ As Any Ptr, ByVal value As ULong)
	Declare Function matrix4_ctor1(ByVal _constructor_ As eConstructor) As Any Ptr
	Declare Function matrix4_ctor2(ByVal other As Any Ptr, ByVal _constructor_ As eConstructor) As Any Ptr
	Declare Function matrix4_operator_directly(ByVal _pointer_ As Any Ptr, ByVal row As Integer, ByVal col As Integer) As Single
	Declare Function matrix4_operator_linearly(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Single
	Declare Sub matrix4_set1(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Sub matrix4_set2(ByVal _pointer_ As Any Ptr, ByVal scalar As Single)
	Declare Function matrix4_const_pointer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function matrix4_pointer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function matrix4_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function matrix4_noteq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub matrix4_add(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function matrix4_get_add(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Sub matrix4_sub(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function matrix4_get_sub(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function matrix4_setbyproduct(ByVal _pointer_ As Any Ptr, ByVal other_a As Any Ptr, ByVal other_b As Any Ptr) As Any Ptr
	Declare Function matrix4_setbyproduct_nocheck(ByVal _pointer_ As Any Ptr, ByVal other_a As Any Ptr, ByVal other_b As Any Ptr) As Any Ptr
	Declare Sub matrix4_multiplication1(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Sub matrix4_multiplication2(ByVal _pointer_ As Any Ptr, ByVal scalar As Single)
	Declare Function matrix4_get_multiplication1(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function matrix4_get_multiplication2(ByVal _pointer_ As Any Ptr, ByVal scalar As Single) As Any Ptr
	Declare Function matrix4_makeIdentity(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function matrix4_isIdentity(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function matrix4_isOrthogonal(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function matrix4_isIdentity_integer_base(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function matrix4_setTranslation(ByVal _pointer_ As Any Ptr, ByVal translation As Any Ptr) As Any Ptr
	Declare Function matrix4_getTranslation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function matrix4_setInverseTranslation(ByVal _pointer_ As Any Ptr, ByVal translation As Any Ptr) As Any Ptr
	Declare Function matrix4_setRotationRadians(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr) As Any Ptr
	Declare Function matrix4_setRotationDegrees(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr) As Any Ptr
	Declare Function matrix4_getRotationDegrees(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function matrix4_setInverseRotationRadians(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr) As Any Ptr
	Declare Function matrix4_setInverseRotationDegrees(ByVal _pointer_ As Any Ptr, ByVal rotation As Any Ptr) As Any Ptr
	Declare Function matrix4_setScale1(ByVal _pointer_ As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function matrix4_setScale2(ByVal _pointer_ As Any Ptr, ByVal scale As Single) As Any Ptr
	Declare Function matrix4_getScale(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub matrix4_inverseTranslateVect(ByVal _pointer_ As Any Ptr, ByVal vect As Any Ptr)
	Declare Sub matrix4_inverseRotateVect(ByVal _pointer_ As Any Ptr, ByVal vect As Any Ptr)
	Declare Sub matrix4_rotateVect1(ByVal _pointer_ As Any Ptr, ByVal vect As Any Ptr)
	Declare Sub matrix4_rotateVect2(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal in As Any Ptr)
	Declare Sub matrix4_rotateVect3(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal in As Any Ptr)
	Declare Sub matrix4_transformVect1(ByVal _pointer_ As Any Ptr, ByVal vect As Any Ptr)
	Declare Sub matrix4_transformVect2(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal in As Any Ptr)
	Declare Sub matrix4_transformVect3(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr, ByVal in As Any Ptr)
	Declare Sub matrix4_translateVect(ByVal _pointer_ As Any Ptr, ByVal vect As Any Ptr)
	Declare Sub matrix4_transformPlane1(ByVal _pointer_ As Any Ptr, ByVal plane As Any Ptr)
	Declare Sub matrix4_transformPlane2(ByVal _pointer_ As Any Ptr, ByVal in As Any Ptr, ByVal out As Any Ptr)
	Declare Sub matrix4_transformBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub matrix4_transformBoxEx(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub matrix4_multiplyWith1x4Matrix(ByVal _pointer_ As Any Ptr, ByVal matrix As Any Ptr)
	Declare Function matrix4_makeInverse(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function matrix4_getInversePrimitive(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr) As UByte
	Declare Function matrix4_getInverse(ByVal _pointer_ As Any Ptr, ByVal out As Any Ptr) As UByte
	Declare Function matrix4_buildProjectionMatrixPerspectiveFovRH(ByVal _pointer_ As Any Ptr, ByVal fieldOfViewRadians As Single, ByVal aspectRatio As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildProjectionMatrixPerspectiveFovLH(ByVal _pointer_ As Any Ptr, ByVal fieldOfViewRadians As Single, ByVal aspectRatio As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildProjectionMatrixPerspectiveRH(ByVal _pointer_ As Any Ptr, ByVal _width_OfViewVolume As Single, ByVal heightOfViewVolume As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildProjectionMatrixPerspectiveLH(ByVal _pointer_ As Any Ptr, ByVal _width_OfViewVolume As Single, ByVal heightOfViewVolume As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildProjectionMatrixOrthoLH(ByVal _pointer_ As Any Ptr, ByVal _width_OfViewVolume As Single, ByVal heightOfViewVolume As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildProjectionMatrixOrthoRH(ByVal _pointer_ As Any Ptr, ByVal _width_OfViewVolume As Single, ByVal heightOfViewVolume As Single, ByVal zNear As Single, ByVal zFar As Single) As Any Ptr
	Declare Function matrix4_buildCameraLookAtMatrixLH(ByVal _pointer_ As Any Ptr, ByVal position As Any Ptr, ByVal target As Any Ptr, ByVal upVector As Any Ptr) As Any Ptr
	Declare Function matrix4_buildCameraLookAtMatrixRH(ByVal _pointer_ As Any Ptr, ByVal position As Any Ptr, ByVal target As Any Ptr, ByVal upVector As Any Ptr) As Any Ptr
	Declare Function matrix4_buildShadowMatrix(ByVal _pointer_ As Any Ptr, ByVal light As Any Ptr, ByVal plane As Any Ptr, ByVal _point_ As Single) As Any Ptr
	Declare Function matrix4_buildNDCToDCMatrix(ByVal _pointer_ As Any Ptr, ByVal area As Any Ptr, ByVal zScale As Single) As Any Ptr
	Declare Sub matrix4_interpolate(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr, ByVal time As Single)
	Declare Function matrix4_getTransposed1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub matrix4_getTransposed2(ByVal _pointer_ As Any Ptr, ByVal dest As Any Ptr)
	Declare Function matrix4_buildRotateFromTo(ByVal _pointer_ As Any Ptr, ByVal from As Any Ptr, ByVal _to_ As Any Ptr) As Any Ptr
	Declare Sub matrix4_setRotationCenter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal translate As Any Ptr)
	Declare Sub matrix4_buildAxisAlignedBillboard(ByVal _pointer_ As Any Ptr, ByVal camPos As Any Ptr, ByVal center As Any Ptr, ByVal translation As Any Ptr, ByVal axis As Any Ptr, ByVal from As Any Ptr)
	Declare Function matrix4_buildTextureTransform(ByVal _pointer_ As Any Ptr, ByVal rotateRad As Single, ByVal rotatecenter As Any Ptr, ByVal translate As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function matrix4_setTextureRotationCenter(ByVal _pointer_ As Any Ptr, ByVal radAngle As Single) As Any Ptr
	Declare Function matrix4_setTextureTranslate(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single) As Any Ptr
	Declare Function matrix4_setTextureTranslateTransposed(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single) As Any Ptr
	Declare Function matrix4_setTextureScale(ByVal _pointer_ As Any Ptr, ByVal sx As Single, ByVal sy As Single) As Any Ptr
	Declare Function matrix4_setTextureScaleCenter(ByVal _pointer_ As Any Ptr, ByVal sx As Single, ByVal sy As Single) As Any Ptr
	Declare Function matrix4_setM(ByVal _pointer_ As Any Ptr, ByVal _data_ As Any Ptr) As Any Ptr
	Declare Sub matrix4_setDefinitelyIdentityMatrix(ByVal _pointer_ As Any Ptr, ByVal isDefinitelyIdentityMatrix As UByte)
	Declare Function matrix4_getDefinitelyIdentityMatrix(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ILogger_getLogLevel(ByVal _pointer_ As Any Ptr) As ELOG_LEVEL
	Declare Sub ILogger_setLogLevel(ByVal _pointer_ As Any Ptr, ByVal ll As ELOG_LEVEL)
	Declare Sub ILogger_log(ByVal _pointer_ As Any Ptr, ByVal text As ZString Ptr, ByVal ll As ELOG_LEVEL)
	Declare Sub ILogger_log2(ByVal _pointer_ As Any Ptr, ByVal text As ZString Ptr, ByVal hint As ZString Ptr, ByVal ll As ELOG_LEVEL)
	Declare Sub ILogger_log3(ByVal _pointer_ As Any Ptr, ByVal text As ZString Ptr, ByVal hint As WString Ptr, ByVal ll As ELOG_LEVEL)
	Declare Sub ILogger_log4(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal hint As WString Ptr, ByVal ll As ELOG_LEVEL)
	Declare Sub ILogger_log5(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal ll As ELOG_LEVEL)
	Declare Function IMesh_getMeshBufferCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IMesh_getMeshBuffer(ByVal _pointer_ As Any Ptr, ByVal nr As UInteger) As Any Ptr
	Declare Function IMesh_getMeshBuffer2(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr) As Any Ptr
	Declare Function IMesh_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IMesh_setBoundingBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub IMesh_setMaterialFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	Declare Sub IMesh_setHardwareMappingHint(ByVal _pointer_ As Any Ptr, ByVal newMappingHint As E_HARDWARE_MAPPING, ByVal buffer As E_BUFFER_TYPE)
	Declare Sub IMesh_setDirty(ByVal _pointer_ As Any Ptr, ByVal buffer As E_BUFFER_TYPE)
	Declare Sub ISceneNodeAnimator_animateNode(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr, ByVal timeMs As UInteger)
	Declare Function ISceneNodeAnimator_createClone(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr, ByVal newManager As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimator_isEventReceiverEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneNodeAnimator_OnEvent(ByVal _pointer_ As Any Ptr, ByVal event As Any Ptr) As UByte
	Declare Function ISceneNodeAnimator_getType(ByVal _pointer_ As Any Ptr) As ESCENE_NODE_ANIMATOR_TYPE
	Declare Function ISceneNodeAnimator_hasFinished(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ISceneNodeAnimator_set_func_event(ByVal _pointer_ As Any Ptr, ByVal _On_EventMethodSEvent As Any Ptr) As UByte
	Declare Function ITexture_lock(ByVal _pointer_ As Any Ptr, ByVal readOnly As UByte, ByVal mipmapLevel As UInteger) As Any Ptr
	Declare Sub ITexture_unlock(ByVal _pointer_ As Any Ptr)
	Declare Function ITexture_getOriginalSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ITexture_getSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function ITexture_getDriverType(ByVal _pointer_ As Any Ptr) As E_DRIVER_TYPE
	Declare Function ITexture_getColorFormat(ByVal _pointer_ As Any Ptr) As ECOLOR_FORMAT
	Declare Function ITexture_getPitch(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ITexture_hasMipMaps(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ITexture_hasAlpha(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub ITexture_regenerateMipMapLevels(ByVal _pointer_ As Any Ptr)
	Declare Function ITexture_isRenderTarget(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function ITexture_getName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function ITriangleSelector_getTriangleCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub ITriangleSelector_getTriangles(ByVal _pointer_ As Any Ptr, ByVal triangles As Any Ptr, ByVal arraySize As Integer, ByVal outTriangleCount As Integer, ByVal transform As Any Ptr)
	Declare Sub ITriangleSelector_getTriangles2(ByVal _pointer_ As Any Ptr, ByVal triangles As Any Ptr, ByVal arraySize As Integer, ByVal outTriangleCount As Integer, ByVal box As Any Ptr, ByVal transform As Any Ptr)
	Declare Sub ITriangleSelector_getTriangles3(ByVal _pointer_ As Any Ptr, ByVal triangles As Any Ptr, ByVal arraySize As Integer, ByVal outTriangleCount As Integer, ByVal _line_ As Any Ptr, ByVal transform As Any Ptr)
	Declare Function ITriangleSelector_getSceneNodeForTriangle(ByVal _pointer_ As Any Ptr, ByVal triangleIndex As UInteger) As Any Ptr
	Declare Function IVideoModeList_getVideoModeCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IVideoModeList_getVideoModeResolution(ByVal _pointer_ As Any Ptr, ByVal _mod_eNumber As Integer) As Any Ptr
	Declare Function IVideoModeList_getVideoModeResolution2(ByVal _pointer_ As Any Ptr, ByVal minSize As Any Ptr, ByVal maxSize As Any Ptr) As Any Ptr
	Declare Function IVideoModeList_getVideoModeDepth(ByVal _pointer_ As Any Ptr, ByVal _mod_eNumber As Integer) As Integer
	Declare Function IVideoModeList_getDesktopResolution(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVideoModeList_getDesktopDepth(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function line3df_ctor1() As Any Ptr
	Declare Function line3df_ctor2(ByVal xa As Single, ByVal ya As Single, ByVal za As Single, ByVal xb As Single, ByVal yb As Single, ByVal zb As Single) As Any Ptr
	Declare Function line3df_ctor3(ByVal start As Any Ptr, ByVal _end_ As Any Ptr) As Any Ptr
	Declare Function line3df_get_start(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3df_get_end(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub line3df_set_start(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub line3df_set_end(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function line3df_add(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3df_add_set(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3df_sub(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3df_sub_set(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3df_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function line3df_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub line3df_setLine1(ByVal _pointer_ As Any Ptr, ByVal xa As Single, ByVal ya As Single, ByVal za As Single, ByVal xb As Single, ByVal yb As Single, ByVal zb As Single)
	Declare Sub line3df_setLine2(ByVal _pointer_ As Any Ptr, ByVal nstart As Any Ptr, ByVal nend As Any Ptr)
	Declare Sub line3df_setLine3(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr)
	Declare Function line3df_getLength(ByVal _pointer_ As Any Ptr) As Single
	Declare Function line3df_getLengthSQ(ByVal _pointer_ As Any Ptr) As Single
	Declare Function line3df_getMiddle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3df_getVector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3df_isPointBetweenStartAndEnd(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As UByte
	Declare Function line3df_getClosestPoint(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3df_getIntersectionWithSphere(ByVal _pointer_ As Any Ptr, ByVal sorigin As Any Ptr, ByVal sradius As Single, ByVal outdistance As Single) As UByte
	Declare Function line3di_ctor1() As Any Ptr
	Declare Function line3di_ctor2(ByVal xa As Integer, ByVal ya As Integer, ByVal za As Integer, ByVal xb As Integer, ByVal yb As Integer, ByVal zb As Integer) As Any Ptr
	Declare Function line3di_ctor3(ByVal start As Any Ptr, ByVal _end_ As Any Ptr) As Any Ptr
	Declare Function line3di_get_start(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3di_get_end(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub line3di_set_start(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub line3di_set_end(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function line3di_add(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3di_add_set(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3di_sub(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3di_sub_set(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3di_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function line3di_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub line3di_setLine1(ByVal _pointer_ As Any Ptr, ByVal xa As Integer, ByVal ya As Integer, ByVal za As Integer, ByVal xb As Integer, ByVal yb As Integer, ByVal zb As Integer)
	Declare Sub line3di_setLine2(ByVal _pointer_ As Any Ptr, ByVal nstart As Any Ptr, ByVal nend As Any Ptr)
	Declare Sub line3di_setLine3(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr)
	Declare Function line3di_getLength(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function line3di_getLengthSQ(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function line3di_getMiddle(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3di_getVector(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function line3di_isPointBetweenStartAndEnd(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As UByte
	Declare Function line3di_getClosestPoint(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Any Ptr
	Declare Function line3di_getIntersectionWithSphere(ByVal _pointer_ As Any Ptr, ByVal sorigin As Any Ptr, ByVal sradius As Integer, ByVal outdistance As Single) As UByte
	Declare Function plane3df_ctor1() As Any Ptr
	Declare Function plane3df_ctor2(ByVal MPoint As Any Ptr, ByVal Normal As Any Ptr) As Any Ptr
	Declare Function plane3df_ctor3(ByVal px As Single, ByVal py As Single, ByVal pz As Single, ByVal nx As Single, ByVal ny As Single, ByVal nz As Single) As Any Ptr
	Declare Function plane3df_ctor4(ByVal _point_1 As Any Ptr, ByVal _point_2 As Any Ptr, ByVal _point_3 As Any Ptr) As Any Ptr
	Declare Function plane3df_ctor5(ByVal normal As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function plane3df_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function plane3df_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub plane3df_setPlane(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr, ByVal nvector As Any Ptr)
	Declare Sub plane3df_setPlane2(ByVal _pointer_ As Any Ptr, ByVal nvect As Any Ptr, ByVal d As Single)
	Declare Sub plane3df_setPlane3(ByVal _pointer_ As Any Ptr, ByVal _point_1 As Any Ptr, ByVal _point_2 As Any Ptr, ByVal _point_3 As Any Ptr)
	Declare Function plane3df_getIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function plane3df_getKnownIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point1 As Any Ptr, ByVal _line_Point2 As Any Ptr) As Single
	Declare Function plane3df_getIntersectionWithLimitedLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point1 As Any Ptr, ByVal _line_Point2 As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function plane3df_classifyPointRelation(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As EIntersectionRelation3D
	Declare Sub plane3df_recalculateD(ByVal _pointer_ As Any Ptr, ByVal MPoint As Any Ptr)
	Declare Function plane3df_getMemberPoint(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function plane3df_existsIntersection(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function plane3df_getIntersectionWithPlane(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal outLinePoint As Any Ptr, ByVal outLineVect As Any Ptr) As UByte
	Declare Function plane3df_getIntersectionWithPlanes(ByVal _pointer_ As Any Ptr, ByVal o1 As Any Ptr, ByVal o2 As Any Ptr, ByVal outPoint As Any Ptr) As UByte
	Declare Function plane3df_isFrontFacing(ByVal _pointer_ As Any Ptr, ByVal lookDirection As Any Ptr) As UByte
	Declare Function plane3df_getDistanceTo(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Single
	Declare Function plane3df_get_Normal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub plane3df_set_Normal(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function plane3df_get_D(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub plane3df_set_D(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function plane3di_ctor1() As Any Ptr
	Declare Function plane3di_ctor2(ByVal MPoint As Any Ptr, ByVal Normal As Any Ptr) As Any Ptr
	Declare Function plane3di_ctor3(ByVal px As Integer, ByVal py As Integer, ByVal pz As Integer, ByVal nx As Integer, ByVal ny As Integer, ByVal nz As Integer) As Any Ptr
	Declare Function plane3di_ctor4(ByVal _point_1 As Any Ptr, ByVal _point_2 As Any Ptr, ByVal _point_3 As Any Ptr) As Any Ptr
	Declare Function plane3di_ctor5(ByVal normal As Any Ptr, ByVal d As Integer) As Any Ptr
	Declare Function plane3di_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function plane3di_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub plane3di_setPlane(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr, ByVal nvector As Any Ptr)
	Declare Sub plane3di_setPlane2(ByVal _pointer_ As Any Ptr, ByVal nvect As Any Ptr, ByVal d As Integer)
	Declare Sub plane3di_setPlane3(ByVal _pointer_ As Any Ptr, ByVal _point_1 As Any Ptr, ByVal _point_2 As Any Ptr, ByVal _point_3 As Any Ptr)
	Declare Function plane3di_getIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function plane3di_getKnownIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point1 As Any Ptr, ByVal _line_Point2 As Any Ptr) As Integer
	Declare Function plane3di_getIntersectionWithLimitedLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point1 As Any Ptr, ByVal _line_Point2 As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function plane3di_classifyPointRelation(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As EIntersectionRelation3D
	Declare Sub plane3di_recalculateD(ByVal _pointer_ As Any Ptr, ByVal MPoint As Any Ptr)
	Declare Function plane3di_getMemberPoint(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function plane3di_existsIntersection(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function plane3di_getIntersectionWithPlane(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal outLinePoint As Any Ptr, ByVal outLineVect As Any Ptr) As UByte
	Declare Function plane3di_getIntersectionWithPlanes(ByVal _pointer_ As Any Ptr, ByVal o1 As Any Ptr, ByVal o2 As Any Ptr, ByVal outPoint As Any Ptr) As UByte
	Declare Function plane3di_isFrontFacing(ByVal _pointer_ As Any Ptr, ByVal lookDirection As Any Ptr) As UByte
	Declare Function plane3di_getDistanceTo(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr) As Integer
	Declare Function plane3di_get_Normal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub plane3di_set_Normal(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function plane3di_get_D(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub plane3di_set_D(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function rectf_ctor1() As Any Ptr
	Declare Function rectf_ctor2(ByVal x As Single, ByVal y As Single, ByVal x2 As Single, ByVal y2 As Single) As Any Ptr
	Declare Function rectf_ctor3(ByVal upperLeft As Any Ptr, ByVal lowerRight As Any Ptr) As Any Ptr
	Declare Function rectf_ctor4(ByVal pos As Any Ptr, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Function rectf_add(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function rectf_add_set(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function rectf_sub(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function rectf_sub_set(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function rectf_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function rectf_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function rectf_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function rectf_getArea(ByVal _pointer_ As Any Ptr) As Single
	Declare Function rectf_isPointInside(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As UByte
	Declare Function rectf_isRectCollided(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub rectf_clipAgainst(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function rectf_constrainTo(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function rectf_getWidth(ByVal _pointer_ As Any Ptr) As Single
	Declare Function rectf_getHeight(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub rectf_repair(ByVal _pointer_ As Any Ptr)
	Declare Function rectf_isValid(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function rectf_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function rectf_getSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub rectf_addInternalPoint1(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr)
	Declare Sub rectf_addInternalPoint2(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single)
	Declare Function rectf_get_UpperLeftCorner(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub rectf_set_UpperLeftCorner(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function rectf_get_LowerRightCorner(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub rectf_set_LowerRightCorner(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function recti_ctor1() As Any Ptr
	Declare Function recti_ctor2(ByVal x As Integer, ByVal y As Integer, ByVal x2 As Integer, ByVal y2 As Integer) As Any Ptr
	Declare Function recti_ctor3(ByVal upperLeft As Any Ptr, ByVal lowerRight As Any Ptr) As Any Ptr
	Declare Function recti_ctor4(ByVal pos As Any Ptr, ByVal _size_ As Any Ptr) As Any Ptr
	Declare Function recti_add(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function recti_add_set(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function recti_sub(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function recti_sub_set(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As Any Ptr
	Declare Function recti_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function recti_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function recti_le(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function recti_getArea(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function recti_isPointInside(ByVal _pointer_ As Any Ptr, ByVal pos As Any Ptr) As UByte
	Declare Function recti_isRectCollided(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Sub recti_clipAgainst(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function recti_constrainTo(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function recti_getWidth(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function recti_getHeight(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub recti_repair(ByVal _pointer_ As Any Ptr)
	Declare Function recti_isValid(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function recti_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function recti_getSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub recti_addInternalPoint1(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr)
	Declare Sub recti_addInternalPoint2(ByVal _pointer_ As Any Ptr, ByVal x As Integer, ByVal y As Integer)
	Declare Function recti_get_UpperLeftCorner(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub recti_set_UpperLeftCorner(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function recti_get_LowerRightCorner(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub recti_set_LowerRightCorner(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function rects32array_ctor() As Any Ptr
	Declare Sub rects32array_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Sub rects32array_setAllocStrategy(ByVal _pointer_ As Any Ptr, ByVal newStrategy As eAllocStrategy)
	Declare Sub rects32array_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub rects32array_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub rects32array_insert(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal index As UInteger)
	Declare Sub rects32array_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub rects32array_set_pointer(ByVal _pointer_ As Any Ptr, ByVal newPointer As Any Ptr, ByVal _size_ As UInteger, ByVal _is_sorted As UByte, ByVal _free_when_destroyed As UByte)
	Declare Sub rects32array_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub rects32array_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function rects32array_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function rects32array_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function rects32array_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub rects32array_sort(ByVal _pointer_ As Any Ptr)
	Declare Function rects32array_binary_search1(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function rects32array_binary_search2(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal left As Integer, ByVal right As Integer) As Integer
	Declare Function rects32array_binary_search_multi(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal last As Integer) As Integer
	Declare Function rects32array_linear_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function rects32array_linear_reverse_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Sub rects32array_erase1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub rects32array_erase2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal count As Integer)
	Declare Sub rects32array_set_sorted(ByVal _pointer_ As Any Ptr, ByVal _is_sorted As UByte)
	Declare Sub rects32array_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function SColor_ctor1() As Any Ptr
	Declare Function SColor_ctor2(ByVal a As UInteger, ByVal r As UInteger, ByVal g As UInteger, ByVal b As UInteger) As Any Ptr
	Declare Function SColor_ctor3(ByVal clr As UInteger) As Any Ptr
	Declare Function SColor_getAlpha(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SColor_getRed(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SColor_getGreen(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SColor_getBlue(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SColor_getLuminance(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColor_getAverage(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SColor_setAlpha(ByVal _pointer_ As Any Ptr, ByVal a As UInteger)
	Declare Sub SColor_setRed(ByVal _pointer_ As Any Ptr, ByVal r As UInteger)
	Declare Sub SColor_setGreen(ByVal _pointer_ As Any Ptr, ByVal g As UInteger)
	Declare Sub SColor_setBlue(ByVal _pointer_ As Any Ptr, ByVal b As UInteger)
	Declare Function SColor_toA1R5G5B5(ByVal _pointer_ As Any Ptr) As UShort
	Declare Sub SColor_toOpenGLColor(ByVal _pointer_ As Any Ptr, ByVal dest As Any Ptr)
	Declare Sub SColor_set(ByVal _pointer_ As Any Ptr, ByVal a As UInteger, ByVal r As UInteger, ByVal g As UInteger, ByVal b As UInteger)
	Declare Sub SColor_set2(ByVal _pointer_ As Any Ptr, ByVal col As UInteger)
	Declare Function SColor_operator_equal(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SColor_operator_notequal(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SColor_operator_less(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SColor_operator_add(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function SColor_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function SColor_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal c1 As Any Ptr, ByVal c2 As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function SColor_color(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SColorf_ctor1() As Any Ptr
	Declare Function SColorf_ctor2(ByVal r As Single, ByVal g As Single, ByVal b As Single, ByVal a As Single) As Any Ptr
	Declare Function SColorf_ctor3(ByVal c As Any Ptr) As Any Ptr
	Declare Function SColorf_toSColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SColorf_set1(ByVal _pointer_ As Any Ptr, ByVal rr As Single, ByVal gg As Single, ByVal bb As Single)
	Declare Sub SColorf_set2(ByVal _pointer_ As Any Ptr, ByVal aa As Single, ByVal rr As Single, ByVal gg As Single, ByVal bb As Single)
	Declare Function SColorf_getInterpolated(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Function SColorf_getInterpolated_quadratic(ByVal _pointer_ As Any Ptr, ByVal c1 As Any Ptr, ByVal c2 As Any Ptr, ByVal d As Single) As Any Ptr
	Declare Sub SColorf_setColorComponentValue(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As Single)
	Declare Function SColorf_getAlpha(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColorf_getRed(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColorf_getGreen(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColorf_getBlue(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SColorf_setAlpha(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SColorf_setRed(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SColorf_setGreen(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SColorf_setBlue(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SColorHSL_ctor(ByVal h As Single, ByVal s As Single, ByVal l As Single) As Any Ptr
	Declare Sub SColorHSL_fromRGB(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub SColorHSL_toRGB(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Function SColorHSL_get_Hue(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColorHSL_get_Saturation(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SColorHSL_get_Luminance(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SColorHSL_set_Hue(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SColorHSL_set_Saturation(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Sub SColorHSL_set_Luminance(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SMaterialLayer_ctor1() As Any Ptr
	Declare Function SMaterialLayer_ctor2(ByVal other As Any Ptr) As Any Ptr
	Declare Function SMaterialLayer_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Sub SMaterialLayer_set_Texture(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMaterialLayer_get_Texture(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMaterialLayer_set_TextureWrapU(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMaterialLayer_get_TextureWrapU(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMaterialLayer_set_TextureWrapV(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMaterialLayer_get_TextureWrapV(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMaterialLayer_set_BilinearFilter(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SMaterialLayer_get_BilinearFilter(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SMaterialLayer_set_TrilinearFilter(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SMaterialLayer_get_TrilinearFilter(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SMaterialLayer_set_AnisotropicFilter(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMaterialLayer_get_AnisotropicFilter(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMaterialLayer_set_LODBias(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMaterialLayer_get_LODBias(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function SMaterialLayer_getTextureMatrix(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMaterialLayer_setTextureMatrix(ByVal _pointer_ As Any Ptr, ByVal mat As Any Ptr)
	Declare Function SMaterialLayer_operator_eq(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As UByte
	Declare Function SMaterialLayer_operator_noteq(ByVal _pointer_ As Any Ptr, ByVal b As Any Ptr) As UByte
	Declare Function triangle3df_ctor1() As Any Ptr
	Declare Function triangle3df_ctor2(ByVal v1 As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr) As Any Ptr
	Declare Function triangle3df_get_pointA(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3df_get_pointB(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3df_get_pointC(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub triangle3df_set_pointA(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub triangle3df_set_pointB(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub triangle3df_set_pointC(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function triangle3df_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function triangle3df_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function triangle3df_isTotalInsideBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr) As UByte
	Declare Function triangle3df_isTotalOutsideBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr) As UByte
	Declare Function triangle3df_closestPointOnTriangle(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function triangle3df_isPointInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function triangle3df_isPointInsideFast(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function triangle3df_getIntersectionWithLimitedLine(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3df_getIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3df_getIntersectionOfPlaneWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3df_getNormal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3df_isFrontFacing(ByVal _pointer_ As Any Ptr, ByVal lookDirection As Any Ptr) As UByte
	Declare Function triangle3df_getPlane(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3df_getArea(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub triangle3df_set(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal c As Any Ptr)
	Declare Function triangle3di_ctor1() As Any Ptr
	Declare Function triangle3di_ctor2(ByVal v1 As Any Ptr, ByVal v2 As Any Ptr, ByVal v3 As Any Ptr) As Any Ptr
	Declare Function triangle3di_get_pointA(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3di_get_pointB(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3di_get_pointC(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub triangle3di_set_pointA(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub triangle3di_set_pointB(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub triangle3di_set_pointC(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function triangle3di_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function triangle3di_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function triangle3di_isTotalInsideBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr) As UByte
	Declare Function triangle3di_isTotalOutsideBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr) As UByte
	Declare Function triangle3di_closestPointOnTriangle(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As Any Ptr
	Declare Function triangle3di_isPointInside(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function triangle3di_isPointInsideFast(ByVal _pointer_ As Any Ptr, ByVal p As Any Ptr) As UByte
	Declare Function triangle3di_getIntersectionWithLimitedLine(ByVal _pointer_ As Any Ptr, ByVal _line_ As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3di_getIntersectionWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3di_getIntersectionOfPlaneWithLine(ByVal _pointer_ As Any Ptr, ByVal _line_Point As Any Ptr, ByVal _line_Vect As Any Ptr, ByVal outIntersection As Any Ptr) As UByte
	Declare Function triangle3di_getNormal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3di_isFrontFacing(ByVal _pointer_ As Any Ptr, ByVal lookDirection As Any Ptr) As UByte
	Declare Function triangle3di_getPlane(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function triangle3di_getArea(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub triangle3di_set(ByVal _pointer_ As Any Ptr, ByVal a As Any Ptr, ByVal b As Any Ptr, ByVal c As Any Ptr)
	Declare Sub IGUIImageList_draw(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal destPos As Any Ptr, ByVal clip As Any Ptr)
	Declare Function IGUIImageList_getImageCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIImageList_getImageSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITab_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUITab_getNumber(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUITab_setDrawBackground(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Sub IGUITab_setBackgroundColor(ByVal _pointer_ As Any Ptr, ByVal c As Any Ptr)
	Declare Function IGUITab_isDrawingBackground(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUITab_getBackgroundColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUITab_setTextColor(ByVal _pointer_ As Any Ptr, ByVal c As Any Ptr)
	Declare Function IGUITab_getTextColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITabControl_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUITabControl_addTab(ByVal _pointer_ As Any Ptr, ByVal caption As WString Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IGUITabControl_getTabCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUITabControl_getTab(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As Any Ptr
	Declare Function IGUITabControl_setActiveTab1(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As UByte
	Declare Function IGUITabControl_setActiveTab2(ByVal _pointer_ As Any Ptr, ByVal tab As Any Ptr) As UByte
	Declare Function IGUITabControl_getActiveTab(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUITabControl_setTabHeight(ByVal _pointer_ As Any Ptr, ByVal height As Integer)
	Declare Function IGUITabControl_getTabHeight(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUITabControl_setTabMaxWidth(ByVal _pointer_ As Any Ptr, ByVal _width_ As Integer)
	Declare Function IGUITabControl_getTabMaxWidth(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUITabControl_setTabVerticalAlignment(ByVal _pointer_ As Any Ptr, ByVal alignment As EGUI_ALIGNMENT)
	Declare Function IGUITabControl_getTabVerticalAlignment(ByVal _pointer_ As Any Ptr) As EGUI_ALIGNMENT
	Declare Sub IGUITabControl_setTabExtraWidth(ByVal _pointer_ As Any Ptr, ByVal extraWidth As Integer)
	Declare Function IGUITabControl_getTabExtraWidth(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIToolBar_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIToolBar_addButton(ByVal _pointer_ As Any Ptr, ByVal id As Integer, ByVal text As WString Ptr, ByVal _to_oltiptext As WString Ptr, ByVal img As Any Ptr, ByVal pressedimg As Any Ptr, ByVal _isPushButton_ As UByte, ByVal useAlphaChannel As UByte) As Any Ptr
	Declare Function IGUIContextMenu_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIContextMenu_setCloseHandling(ByVal _pointer_ As Any Ptr, ByVal onClose As ECONTEXT_MENU_CLOSE)
	Declare Function IGUIContextMenu_getCloseHandling(ByVal _pointer_ As Any Ptr) As ECONTEXT_MENU_CLOSE
	Declare Function IGUIContextMenu_getItemCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUIContextMenu_addItem(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal commandId As Integer, ByVal enabled As UByte, ByVal hasSubMenu As UByte, ByVal checked As UByte, ByVal autoChecking As UByte) As UInteger
	Declare Function IGUIContextMenu_insertItem(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal text As WString Ptr, ByVal commandId As Integer, ByVal enabled As UByte, ByVal hasSubMenu As UByte, ByVal checked As UByte, ByVal autoChecking As UByte) As UInteger
	Declare Function IGUIContextMenu_findItemWithCommandId(ByVal _pointer_ As Any Ptr, ByVal commandId As Integer, ByVal idxStartSearch As UInteger) As Integer
	Declare Sub IGUIContextMenu_addSeparator(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIContextMenu_getItemText(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As WString Ptr
	Declare Sub IGUIContextMenu_setItemText(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal text As WString Ptr)
	Declare Function IGUIContextMenu_isItemEnabled(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As UByte
	Declare Sub IGUIContextMenu_setItemEnabled(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal enabled As UByte)
	Declare Sub IGUIContextMenu_setItemChecked(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal enabled As UByte)
	Declare Function IGUIContextMenu_isItemChecked(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As UByte
	Declare Sub IGUIContextMenu_removeItem(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger)
	Declare Sub IGUIContextMenu_removeAllItems(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIContextMenu_getSelectedItem(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIContextMenu_getItemCommandId(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As Integer
	Declare Sub IGUIContextMenu_setItemCommandId(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal id As Integer)
	Declare Function IGUIContextMenu_getSubMenu(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As Any Ptr
	Declare Sub IGUIContextMenu_setItemAutoChecking(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger, ByVal autoChecking As UByte)
	Declare Function IGUIContextMenu_getItemAutoChecking(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As UByte
	Declare Sub IGUIContextMenu_setEventParent(ByVal _pointer_ As Any Ptr, ByVal parent As Any Ptr)
	Declare Function IGUIInOutFader_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIInOutFader_getColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIInOutFader_setColor1(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IGUIInOutFader_setColor2(ByVal _pointer_ As Any Ptr, ByVal source As Any Ptr, ByVal dest As Any Ptr)
	Declare Sub IGUIInOutFader_fadeIn(ByVal _pointer_ As Any Ptr, ByVal time As UInteger)
	Declare Sub IGUIInOutFader_fadeOut(ByVal _pointer_ As Any Ptr, ByVal time As UInteger)
	Declare Function IGUIInOutFader_isReady(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUISpinBox_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUISpinBox_getEditBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUISpinBox_setValue(ByVal _pointer_ As Any Ptr, ByVal val As Single)
	Declare Function IGUISpinBox_getValue(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub IGUISpinBox_setRange(ByVal _pointer_ As Any Ptr, ByVal min As Single, ByVal max As Single)
	Declare Function IGUISpinBox_getMin(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IGUISpinBox_getMax(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub IGUISpinBox_setStepSize(ByVal _pointer_ As Any Ptr, ByVal step As Single)
	Declare Sub IGUISpinBox_setDecimalPlaces(ByVal _pointer_ As Any Ptr, ByVal places As Integer)
	Declare Function IGUISpinBox_getStepSize(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IAttributes_getAttributeCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IAttributes_getAttributeName(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As ZString Ptr
	Declare Function IAttributes_getAttributeType1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As E_ATTRIBUTE_TYPE
	Declare Function IAttributes_getAttributeType2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As E_ATTRIBUTE_TYPE
	Declare Function IAttributes_getAttributeTypeString1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As WString Ptr
	Declare Function IAttributes_getAttributeTypeString2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As WString Ptr
	Declare Function IAttributes_existsAttribute(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As UByte
	Declare Function IAttributes_findAttribute(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Integer
	Declare Sub IAttributes_clear(ByVal _pointer_ As Any Ptr)
	Declare Function IAttributes_read(ByVal _pointer_ As Any Ptr, ByVal reader As Any Ptr, ByVal readCurrentElementOnly As UByte, ByVal elementName As WString Ptr) As UByte
	Declare Function IAttributes_write(ByVal _pointer_ As Any Ptr, ByVal writer As Any Ptr, ByVal writeXMLHeader As UByte, ByVal elementName As WString Ptr) As UByte
	Declare Sub IAttributes_addInt(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Integer)
	Declare Sub IAttributes_setAttribute1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Integer)
	Declare Sub IAttributes_setAttribute2(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As Integer)
	Declare Sub IAttributes_setAttribute3(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Single)
	Declare Sub IAttributes_setAttribute4(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As Single)
	Declare Sub IAttributes_setAttribute5(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As ZString Ptr)
	Declare Sub IAttributes_setAttribute6(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As ZString Ptr)
	Declare Sub IAttributes_setAttribute7(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As WString Ptr)
	Declare Sub IAttributes_setAttribute8(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As WString Ptr)
	Declare Sub IAttributes_setAttribute9(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal _data_ As Any Ptr, ByVal _data_SizeInBytes As Integer)
	Declare Sub IAttributes_setAttribute10(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal _data_ As Any Ptr, ByVal _data_SizeInBytes As Integer)
	Declare Sub IAttributes_setAttribute11(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Sub IAttributes_setAttribute12(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As Any Ptr)
	Declare Sub IAttributes_setAttribute13(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As UByte)
	Declare Sub IAttributes_setAttribute14(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal value As UByte)
	Declare Sub IAttributes_setAttribute15(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal enumValue As ZString Ptr, ByVal enumerationLiterals As Any Ptr)
	Declare Sub IAttributes_setAttribute16(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal enumValue As ZString Ptr, ByVal enumerationLiterals As Any Ptr)
	Declare Sub IAttributes_setAttribute17(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IAttributes_setAttribute18(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal _color_ As Any Ptr)
	Declare Sub IAttributes_setAttribute19(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IAttributes_setAttribute20(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal _color_ As Any Ptr)
	Declare Sub IAttributes_setAttribute21(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute22(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute23(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute24(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute25(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute26(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute27(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute28(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute29(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute30(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute31(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute32(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute33(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute34(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute35(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute36(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute37(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute38(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute39(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute40(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal v As Any Ptr)
	Declare Sub IAttributes_setAttribute41(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal texture As Any Ptr)
	Declare Sub IAttributes_setAttribute42(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal texture As Any Ptr)
	Declare Sub IAttributes_setAttribute43(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal userPointer As Any Ptr)
	Declare Sub IAttributes_setAttribute44(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal userPointer As Any Ptr)
	Declare Function IAttributes_getAttributeAsInt1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Integer
	Declare Function IAttributes_getAttributeAsInt2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Integer
	Declare Sub IAttributes_addFloat(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Single)
	Declare Function IAttributes_getAttributeAsFloat1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Single
	Declare Function IAttributes_getAttributeAsFloat2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Single
	Declare Sub IAttributes_addString1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As ZString Ptr)
	Declare Sub IAttributes_addString2(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As WString Ptr)
	Declare Function IAttributes_getAttributeAsString1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As ZString Ptr
	Declare Function IAttributes_getAttributeAsString2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As ZString Ptr
	Declare Sub IAttributes_getAttributeAsString3(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal target As ZString Ptr)
	Declare Function IAttributes_getAttributeAsStringW1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As WString Ptr
	Declare Function IAttributes_getAttributeAsStringW2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As WString Ptr
	Declare Sub IAttributes_getAttributeAsStringW3(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal target As WString Ptr)
	Declare Sub IAttributes_addBinary1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal _data_ As Any Ptr, ByVal _data_SizeInBytes As Integer)
	Declare Sub IAttributes_addArray2(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Sub IAttributes_getAttributeAsBinaryData1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal outData As Any Ptr, ByVal maxSizeInBytes As Integer)
	Declare Sub IAttributes_getAttributeAsBinaryData2(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal outData As Any Ptr, ByVal maxSizeInBytes As Integer)
	Declare Function IAttributes_getAttributeAsArray1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsArray2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addBool(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As UByte)
	Declare Function IAttributes_getAttributeAsBool1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As UByte
	Declare Function IAttributes_getAttributeAsBool2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As UByte
	Declare Sub IAttributes_addEnum1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal enumValue As ZString Ptr, ByVal enumerationLiterals As Any Ptr)
	Declare Sub IAttributes_addEnum2(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal enumValue As Integer, ByVal enumerationLiterals As Any Ptr)
	Declare Function IAttributes_getAttributeAsEnumeration1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As ZString Ptr
	Declare Function IAttributes_getAttributeAsEnumeration2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As ZString Ptr
	Declare Function IAttributes_getAttributeAsEnumeration3(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal enumerationLiteralsToUse As Any Ptr) As Integer
	Declare Function IAttributes_getAttributeAsEnumeration4(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal enumerationLiteralsToUse As Any Ptr) As Integer
	Declare Sub IAttributes_getAttributeEnumerationLiteralsOfEnumeration1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal outLiterals As Any Ptr)
	Declare Sub IAttributes_getAttributeEnumerationLiteralsOfEnumeration2(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal outLiterals As Any Ptr)
	Declare Sub IAttributes_addColor(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Function IAttributes_getAttributeAsColor1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsColor2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addColorf(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Function IAttributes_getAttributeAsColorf1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsColorf2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addVector3d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Function IAttributes_getAttributeAsVector3d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsVector3d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addPosition2d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Function IAttributes_getAttributeAsPosition2d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsPosition2d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addRect(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal value As Any Ptr)
	Declare Function IAttributes_getAttributeAsRect1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsRect2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addMatrix(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsMatrix1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsMatrix2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addQuaternion(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsQuaternion1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsQuaternion2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addBox3d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsBox3d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsBox3d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addPlane3d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsPlane3d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsPlane3d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addTriangle3d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsTriangle3d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsTriangle3d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addLine2d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsLine2d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsLine2d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addLine3d(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal v As Any Ptr)
	Declare Function IAttributes_getAttributeAsLine3d1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsLine3d2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addTexture(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal texture As Any Ptr)
	Declare Function IAttributes_getAttributeAsTexture1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsTexture2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IAttributes_addUserPointer(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr, ByVal userPointer As Any Ptr)
	Declare Function IAttributes_getAttributeAsUserPointer1(ByVal _pointer_ As Any Ptr, ByVal attributeName As ZString Ptr) As Any Ptr
	Declare Function IAttributes_getAttributeAsUserPointer2(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Function CGridSceneNode_ctor(ByVal parent As Any Ptr, ByVal smgr As Any Ptr, ByVal id As Integer, ByVal spacing As UInteger, ByVal _size_ As UInteger, ByVal gridcolor As Any Ptr, ByVal accentlineoffset As UInteger, ByVal accentgridcolor As Any Ptr, ByVal axislinestate As UByte) As Any Ptr
	Declare Function CGridSceneNode_clone(ByVal _pointer_ As Any Ptr, ByVal newParent As Any Ptr, ByVal newSceneManager As Any Ptr) As Any Ptr
	Declare Sub CGridSceneNode_OnRegisterSceneNode(ByVal _pointer_ As Any Ptr)
	Declare Sub CGridSceneNode_render(ByVal _pointer_ As Any Ptr)
	Declare Function CGridSceneNode_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CGridSceneNode_getMaterialCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function CGridSceneNode_getMaterial(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Sub CGridSceneNode_RegenerateGrid(ByVal _pointer_ As Any Ptr)
	Declare Function CGridSceneNode_GetSpacing(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function CGridSceneNode_GetSize(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function CGridSceneNode_GetGridColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CGridSceneNode_GetAccentlineOffset(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function CGridSceneNode_GetAccentlineColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CGridSceneNode_AreAxisLineActive(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function CGridSceneNode_GetAxisLineXColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CGridSceneNode_GetAxisLineZColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub CGridSceneNode_SetSpacing(ByVal _pointer_ As Any Ptr, ByVal newspacing As UInteger)
	Declare Sub CGridSceneNode_SetSize(ByVal _pointer_ As Any Ptr, ByVal newsize As UInteger)
	Declare Sub CGridSceneNode_SetGridColor(ByVal _pointer_ As Any Ptr, ByVal newcolor As Any Ptr)
	Declare Sub CGridSceneNode_SetAccentlineOffset(ByVal _pointer_ As Any Ptr, ByVal newoffset As UInteger)
	Declare Sub CGridSceneNode_SetAccentlineColor(ByVal _pointer_ As Any Ptr, ByVal newcolor As Any Ptr)
	Declare Sub CGridSceneNode_SetAxisLineActive(ByVal _pointer_ As Any Ptr, ByVal active As UByte)
	Declare Sub CGridSceneNode_SetAxisLineXColor(ByVal _pointer_ As Any Ptr, ByVal XLine As Any Ptr)
	Declare Sub CGridSceneNode_SetAxisLineZColor(ByVal _pointer_ As Any Ptr, ByVal ZLine As Any Ptr)
	Declare Sub CGridSceneNode_SetMaterial(ByVal _pointer_ As Any Ptr, ByVal newMaterial As Any Ptr)
	Declare Function IBillboardTextSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr) As Any Ptr
	Declare Sub IBillboardTextSceneNode_setSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Function IBillboardTextSceneNode_getSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IBillboardTextSceneNode_setColor1(ByVal _pointer_ As Any Ptr, ByVal overallColor As Any Ptr)
	Declare Sub IBillboardTextSceneNode_setColor2(ByVal _pointer_ As Any Ptr, ByVal _to_pColor As Any Ptr, ByVal bottomColor As Any Ptr)
	Declare Sub IBillboardTextSceneNode_getColor(ByVal _pointer_ As Any Ptr, ByVal _to_pColor As Any Ptr, ByVal bottomColor As Any Ptr)
	Declare Sub IBillboardTextSceneNode_setText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Sub IBillboardTextSceneNode_setTextColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Function IDummyTransformationSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IDummyTransformationSceneNode_getRelativeTransformationMatrix(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IXMLWriter_writeXMLHeader(ByVal _pointer_ As Any Ptr)
	Declare Sub IXMLWriter_writeElement1(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr, ByVal empty As UByte, ByVal attr1Name As WString Ptr, ByVal attr1Value As WString Ptr, ByVal attr2Name As WString Ptr, ByVal attr2Value As WString Ptr, ByVal attr3Name As WString Ptr, ByVal attr3Value As WString Ptr, ByVal attr4Name As WString Ptr, ByVal attr4Value As WString Ptr, ByVal attr5Name As WString Ptr, ByVal attr5Value As WString Ptr)
	Declare Sub IXMLWriter_writeElement2(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr, ByVal empty As UByte, ByVal _name_s As Any Ptr, ByVal values As Any Ptr)
	Declare Sub IXMLWriter_writeComment(ByVal _pointer_ As Any Ptr, ByVal comment As WString Ptr)
	Declare Sub IXMLWriter_writeClosingTag(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr)
	Declare Sub IXMLWriter_writeText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Sub IXMLWriter_writeLineBreak(ByVal _pointer_ As Any Ptr)
	Declare Function IReadFile_read(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal _size_ToRead As UInteger) As Integer
	Declare Function IReadFile_seek(ByVal _pointer_ As Any Ptr, ByVal finalPos As Long, ByVal relativeMovement As UByte) As UByte
	Declare Function IReadFile_getSize(ByVal _pointer_ As Any Ptr) As Long
	Declare Function IReadFile_getPos(ByVal _pointer_ As Any Ptr) As Long
	Declare Function IReadFile_getFileName(ByVal _pointer_ As Any Ptr) As fschar
	Declare Function IXMLReader_read(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IXMLReader_getNodeType(ByVal _pointer_ As Any Ptr) As EXML_NODE
	Declare Function IXMLReader_getAttributeCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IXMLReader_getAttributeName(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As WString Ptr
	Declare Function IXMLReader_getAttributeValue1(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As WString Ptr
	Declare Function IXMLReader_getAttributeValue2(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr) As WString Ptr
	Declare Function IXMLReader_getAttributeValueSafe(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr) As WString Ptr
	Declare Function IXMLReader_getAttributeValueAsInt1(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr) As Integer
	Declare Function IXMLReader_getAttributeValueAsInt2(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As Integer
	Declare Function IXMLReader_getAttributeValueAsFloat1(ByVal _pointer_ As Any Ptr, ByVal _name_ As WString Ptr) As Single
	Declare Function IXMLReader_getAttributeValueAsFloat2(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As Single
	Declare Function IXMLReader_getNodeName(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function IXMLReader_getNodeData(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function IXMLReader_isEmptyElement(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IXMLReader_getSourceFormat(ByVal _pointer_ As Any Ptr) As ETEXT_FORMAT
	Declare Function IXMLReader_getParserFormat(ByVal _pointer_ As Any Ptr) As ETEXT_FORMAT
	Declare Function IXMLReaderUTF8_read(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IXMLReaderUTF8_getNodeType(ByVal _pointer_ As Any Ptr) As EXML_NODE
	Declare Function IXMLReaderUTF8_getAttributeCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IXMLReaderUTF8_getAttributeName(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As ZString Ptr
	Declare Function IXMLReaderUTF8_getAttributeValue1(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As ZString Ptr
	Declare Function IXMLReaderUTF8_getAttributeValue2(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As ZString Ptr
	Declare Function IXMLReaderUTF8_getAttributeValueSafe(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As ZString Ptr
	Declare Function IXMLReaderUTF8_getAttributeValueAsInt1(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As Integer
	Declare Function IXMLReaderUTF8_getAttributeValueAsInt2(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As Integer
	Declare Function IXMLReaderUTF8_getAttributeValueAsFloat1(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As Single
	Declare Function IXMLReaderUTF8_getAttributeValueAsFloat2(ByVal _pointer_ As Any Ptr, ByVal idx As Integer) As Single
	Declare Function IXMLReaderUTF8_getNodeName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function IXMLReaderUTF8_getNodeData(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function IXMLReaderUTF8_isEmptyElement(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IXMLReaderUTF8_getSourceFormat(ByVal _pointer_ As Any Ptr) As ETEXT_FORMAT
	Declare Function IXMLReaderUTF8_getParserFormat(ByVal _pointer_ As Any Ptr) As ETEXT_FORMAT
	Declare Sub ITextSceneNode_setText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Sub ITextSceneNode_setTextColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Function IFileList_getFileCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IFileList_getFileName(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As fschar
	Declare Function IFileList_getFullFileName(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As fschar
	Declare Function IFileList_getFileSize(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As UInteger
	Declare Function IFileList_getID(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As UInteger
	Declare Function IFileList_isDirectory(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As UByte
	Declare Function IFileList_findFile(ByVal _pointer_ As Any Ptr, ByVal filename As fschar, ByVal isFolder As UByte) As Integer
	Declare Function IFileList_getPath(ByVal _pointer_ As Any Ptr) As fschar
	Declare Function IFileList_addItem(ByVal _pointer_ As Any Ptr, ByVal fullPath As fschar, ByVal _size_ As UInteger, ByVal isDirectory As UByte, ByVal id As UInteger) As UInteger
	Declare Sub IFileList_sort(ByVal _pointer_ As Any Ptr)
	Declare Function CGUITTFont_ctor(ByVal env As Any Ptr, ByVal filename As fschar, ByVal _size_ As UInteger) As Any Ptr
	Declare Function CGUITTFont_as_IGUIFont(ByVal font As Any Ptr) As Any Ptr
	Declare Function CGUITTFont_createTTFont(ByVal env As Any Ptr, ByVal filename As fschar, ByVal _size_ As UInteger) As Any Ptr
	Declare Sub CGUITTFont_setBatchLoadSize(ByVal _pointer_ As Any Ptr, ByVal batch_size As UInteger)
	Declare Sub CGUITTFont_setMaxPageTextureSize(ByVal _pointer_ As Any Ptr, ByVal texture_size As Any Ptr)
	Declare Sub CGUITTFont_setTransparency(ByVal _pointer_ As Any Ptr, ByVal flag As UByte)
	Declare Sub CGUITTFont_setMonochrome(ByVal _pointer_ As Any Ptr, ByVal flag As UByte)
	Declare Sub CGUITTFont_setFontHinting(ByVal _pointer_ As Any Ptr, ByVal enable As UByte, ByVal enable_auto_hinting As UByte)
	Declare Sub CGUITTFont_draw(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal position As Any Ptr, ByVal _color_ As Any Ptr, ByVal hcenter As UByte, ByVal vcenter As UByte, ByVal clip As Any Ptr)
	Declare Function CGUITTFont_getDimension1(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr) As Any Ptr
	Declare Function CGUITTFont_getDimension2(ByVal _pointer_ As Any Ptr, ByVal text As Any Ptr) As Any Ptr
	Declare Function CGUITTFont_getCharacterFromPos1(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal pixel_x As Integer) As Integer
	Declare Function CGUITTFont_getCharacterFromPos2(ByVal _pointer_ As Any Ptr, ByVal text As Any Ptr, ByVal pixel_x As Integer) As Integer
	Declare Sub CGUITTFont_setKerningWidth(ByVal _pointer_ As Any Ptr, ByVal kerning As Integer)
	Declare Sub CGUITTFont_setKerningHeight(ByVal _pointer_ As Any Ptr, ByVal kerning As Integer)
	Declare Function CGUITTFont_getKerningWidth1(ByVal _pointer_ As Any Ptr, ByVal thisLetter As WString Ptr, ByVal previousLetter As WString Ptr) As Integer
	Declare Function CGUITTFont_getKerningWidth2(ByVal _pointer_ As Any Ptr, ByVal thisLetter As WString Ptr, ByVal previousLetter As WString Ptr) As Integer
	Declare Function CGUITTFont_getKerningHeight(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub CGUITTFont_setInvisibleCharacters1(ByVal _pointer_ As Any Ptr, ByVal s As WString Ptr)
	Declare Sub CGUITTFont_setInvisibleCharacters2(ByVal _pointer_ As Any Ptr, ByVal s As Any Ptr)
	Declare Sub CGUITTFont_forceGlyphUpdate(ByVal _pointer_ As Any Ptr)
	Declare Function IFileArchive_createAndOpenFile1(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr) As Any Ptr
	Declare Function IFileArchive_createAndOpenFile2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IFileArchive_getFileList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IFileArchive_getType(ByVal _pointer_ As Any Ptr) As E_FILE_ARCHIVE_TYPE
	Declare Function IFileArchive_get_Password(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub IFileArchive_set_Password(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function IArchiveLoader_isALoadableFileFormat1(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr) As UByte
	Declare Function IArchiveLoader_isALoadableFileFormat2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As UByte
	Declare Function IArchiveLoader_isALoadableFileFormat3(ByVal _pointer_ As Any Ptr, ByVal fileType As E_FILE_ARCHIVE_TYPE) As UByte
	Declare Function IArchiveLoader_createArchive1(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As Any Ptr
	Declare Function IArchiveLoader_createArchive2(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal ignoreCase As UByte, ByVal ignorePaths As UByte) As Any Ptr
	Declare Function IWriteFile_write(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal _size_ToWrite As UInteger) As Integer
	Declare Function IWriteFile_seek(ByVal _pointer_ As Any Ptr, ByVal finalPos As Long, ByVal relativeMovement As UByte) As UByte
	Declare Function IWriteFile_getPos(ByVal _pointer_ As Any Ptr) As Long
	Declare Function IWriteFile_getFileName(ByVal _pointer_ As Any Ptr) As fschar
	Declare Function array_ctor1() As Any Ptr
	Declare Function array_ctor2(ByVal start_count As UInteger) As Any Ptr
	Declare Function array_ctor3(ByVal other As Any Ptr) As Any Ptr
	Declare Sub array_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Sub array_setAllocStrategy(ByVal _pointer_ As Any Ptr, ByVal newStrategy As eAllocStrategy)
	Declare Sub array_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub array_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub array_insert(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal index As UInteger)
	Declare Sub array_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub array_set_pointer(ByVal _pointer_ As Any Ptr, ByVal newPointer As Any Ptr, ByVal _size_ As UInteger, ByVal _is_sorted As UByte, ByVal _free_when_destroyed As UByte)
	Declare Sub array_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub array_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function array_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function array_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function array_operator_neq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function array_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Sub array_set_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal element As Any Ptr)
	Declare Function array_getLast(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function array_pointer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function array_const_pointer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function array_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function array_allocated_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function array_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub array_sort(ByVal _pointer_ As Any Ptr)
	Declare Function array_binary_search1(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function array_binary_search2(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal left As Integer, ByVal right As Integer) As Integer
	Declare Function array_binary_search_multi(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal last As Integer) As Integer
	Declare Function array_linear_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function array_linear_reverse_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Sub array_erase1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub array_erase2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal count As Integer)
	Declare Sub array_set_sorted(ByVal _pointer_ As Any Ptr, ByVal _is_sorted As UByte)
	Declare Sub array_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function SKeyMap_ctor(ByVal _len_gth As Integer) As Any Ptr
	Declare Sub SKeyMap_set(ByVal _pointer_ As Any Ptr, ByVal index As Integer, ByVal action As EKEY_ACTION, ByVal key_code As EKEY_CODE)
	Declare Function IGUITable_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUITable_addColumn(ByVal _pointer_ As Any Ptr, ByVal caption As WString Ptr, ByVal columnIndex As Integer)
	Declare Sub IGUITable_removeColumn(ByVal _pointer_ As Any Ptr, ByVal columnIndex As UInteger)
	Declare Function IGUITable_getColumnCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUITable_setActiveColumn(ByVal _pointer_ As Any Ptr, ByVal idx As Integer, ByVal doOrder As UByte) As UByte
	Declare Function IGUITable_getActiveColumn(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUITable_getActiveColumnOrdering(ByVal _pointer_ As Any Ptr) As EGUI_ORDERING_MODE
	Declare Sub IGUITable_setColumnWidth(ByVal _pointer_ As Any Ptr, ByVal columnIndex As UInteger, ByVal _width_ As UInteger)
	Declare Sub IGUITable_setResizableColumns(ByVal _pointer_ As Any Ptr, ByVal resizable As UByte)
	Declare Function IGUITable_hasResizableColumns(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUITable_setColumnOrdering(ByVal _pointer_ As Any Ptr, ByVal columnIndex As UInteger, ByVal _mod_e As EGUI_COLUMN_ORDERING)
	Declare Function IGUITable_getSelected(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUITable_setSelected(ByVal _pointer_ As Any Ptr, ByVal index As Integer)
	Declare Function IGUITable_getRowCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUITable_addRow(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger) As UInteger
	Declare Sub IGUITable_removeRow(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger)
	Declare Sub IGUITable_clearRows(ByVal _pointer_ As Any Ptr)
	Declare Sub IGUITable_swapRows(ByVal _pointer_ As Any Ptr, ByVal rowIndexA As UInteger, ByVal rowIndexB As UInteger)
	Declare Sub IGUITable_orderRows(ByVal _pointer_ As Any Ptr, ByVal columnIndex As Integer, ByVal _mod_e As EGUI_ORDERING_MODE)
	Declare Sub IGUITable_setCellText1(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger, ByVal text As WString Ptr)
	Declare Sub IGUITable_setCellText2(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger, ByVal text As WString Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IGUITable_setCellData(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger, ByVal _data_ As Any Ptr)
	Declare Sub IGUITable_setCellColor(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger, ByVal _color_ As Any Ptr)
	Declare Function IGUITable_getCellText(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger) As WString Ptr
	Declare Function IGUITable_getCellData(ByVal _pointer_ As Any Ptr, ByVal rowIndex As UInteger, ByVal columnIndex As UInteger) As Any Ptr
	Declare Sub IGUITable_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub IGUITable_setDrawFlags(ByVal _pointer_ As Any Ptr, ByVal flags As Integer)
	Declare Function IGUITable_getDrawFlags(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIComboBox_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIComboBox_getItemCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUIComboBox_getItem(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As WString Ptr
	Declare Function IGUIComboBox_getItemData(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As UInteger
	Declare Function IGUIComboBox_getIndexForItemData(ByVal _pointer_ As Any Ptr, ByVal _data_ As UInteger) As Integer
	Declare Function IGUIComboBox_addItem(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal _data_ As UInteger) As UInteger
	Declare Sub IGUIComboBox_removeItem(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger)
	Declare Sub IGUIComboBox_clear(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIComboBox_getSelected(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIComboBox_setSelected(ByVal _pointer_ As Any Ptr, ByVal idx As Integer)
	Declare Sub IGUIComboBox_setTextAlignment(ByVal _pointer_ As Any Ptr, ByVal horizontal As EGUI_ALIGNMENT, ByVal vertical As EGUI_ALIGNMENT)
	Declare Function IGUIListBox_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIListBox_getItemCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUIListBox_getListItem(ByVal _pointer_ As Any Ptr, ByVal id As UInteger) As WString Ptr
	Declare Function IGUIListBox_addItem1(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr) As UInteger
	Declare Function IGUIListBox_addItem2(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal icon As Integer) As UInteger
	Declare Sub IGUIListBox_removeItem(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Function IGUIListBox_getIcon(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Integer
	Declare Sub IGUIListBox_setSpriteBank(ByVal _pointer_ As Any Ptr, ByVal bank As Any Ptr)
	Declare Sub IGUIListBox_clear(ByVal _pointer_ As Any Ptr)
	Declare Function IGUIListBox_getSelected(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIListBox_setSelected1(ByVal _pointer_ As Any Ptr, ByVal index As Integer)
	Declare Sub IGUIListBox_setSelected2(ByVal _pointer_ As Any Ptr, ByVal item As WString Ptr)
	Declare Sub IGUIListBox_setAutoScrollEnabled(ByVal _pointer_ As Any Ptr, ByVal scroll As UByte)
	Declare Function IGUIListBox_isAutoScrollEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIListBox_setItemOverrideColor1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _color_ As Any Ptr)
	Declare Sub IGUIListBox_setItemOverrideColor2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _color_Type As EGUI_LISTBOX_COLOR, ByVal _color_ As Any Ptr)
	Declare Sub IGUIListBox_clearItemOverrideColor1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub IGUIListBox_clearItemOverrideColor2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _color_Type As EGUI_LISTBOX_COLOR)
	Declare Function IGUIListBox_hasItemOverrideColor(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _color_Type As EGUI_LISTBOX_COLOR) As UByte
	Declare Function IGUIListBox_getItemOverrideColor(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _color_Type As EGUI_LISTBOX_COLOR) As Any Ptr
	Declare Function IGUIListBox_getItemDefaultColor(ByVal _pointer_ As Any Ptr, ByVal _color_Type As EGUI_LISTBOX_COLOR) As Any Ptr
	Declare Sub IGUIListBox_setItem(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal text As WString Ptr, ByVal icon As Integer)
	Declare Function IGUIListBox_insertItem(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal text As WString Ptr, ByVal icon As Integer) As Integer
	Declare Sub IGUIListBox_swapItems(ByVal _pointer_ As Any Ptr, ByVal index1 As UInteger, ByVal index2 As UInteger)
	Declare Sub IGUIListBox_setItemHeight(ByVal _pointer_ As Any Ptr, ByVal height As Integer)
	Declare Sub IGUIListBox_setDrawBackground(ByVal _pointer_ As Any Ptr, ByVal _draw_ As UByte)
	Declare Function IGUIScrollBar_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIScrollBar_setMax(ByVal _pointer_ As Any Ptr, ByVal max As Integer)
	Declare Function IGUIScrollBar_getMax(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIScrollBar_setMin(ByVal _pointer_ As Any Ptr, ByVal max As Integer)
	Declare Function IGUIScrollBar_getMin(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUIScrollBar_getSmallStep(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIScrollBar_setSmallStep(ByVal _pointer_ As Any Ptr, ByVal step As Integer)
	Declare Function IGUIScrollBar_getLargeStep(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIScrollBar_setLargeStep(ByVal _pointer_ As Any Ptr, ByVal step As Integer)
	Declare Function IGUIScrollBar_getPos(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IGUIScrollBar_setPos(ByVal _pointer_ As Any Ptr, ByVal pos As Integer)
	Declare Function SIrrlichtCreationParameters_ctor() As Any Ptr
	Declare Function SIrrlichtCreationParameters_get_DeviceType(ByVal _pointer_ As Any Ptr) As E_DEVICE_TYPE
	Declare Sub SIrrlichtCreationParameters_set_DeviceType(ByVal _pointer_ As Any Ptr, ByVal value As E_DEVICE_TYPE)
	Declare Function SIrrlichtCreationParameters_get_DriverType(ByVal _pointer_ As Any Ptr) As E_DRIVER_TYPE
	Declare Sub SIrrlichtCreationParameters_set_DriverType(ByVal _pointer_ As Any Ptr, ByVal value As E_DRIVER_TYPE)
	Declare Function SIrrlichtCreationParameters_get_WindowSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SIrrlichtCreationParameters_set_WindowSize(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SIrrlichtCreationParameters_get_Bits(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SIrrlichtCreationParameters_set_Bits(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SIrrlichtCreationParameters_get_ZBufferBits(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SIrrlichtCreationParameters_set_ZBufferBits(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SIrrlichtCreationParameters_get_Fullscreen(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_Fullscreen(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_Stencilbuffer(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_Stencilbuffer(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_Vsync(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_Vsync(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_AntiAlias(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SIrrlichtCreationParameters_set_AntiAlias(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SIrrlichtCreationParameters_get_WithAlphaChannel(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_WithAlphaChannel(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_Doublebuffer(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_Doublebuffer(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_IgnoreInput(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_IgnoreInput(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_Stereobuffer(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_Stereobuffer(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_HighPrecisionFPU(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub SIrrlichtCreationParameters_set_HighPrecisionFPU(ByVal _pointer_ As Any Ptr, ByVal value As UByte)
	Declare Function SIrrlichtCreationParameters_get_EventReceiver(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SIrrlichtCreationParameters_set_EventReceiver(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SIrrlichtCreationParameters_get_WindowId(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SIrrlichtCreationParameters_set_WindowId(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SIrrlichtCreationParameters_get_LoggingLevel(ByVal _pointer_ As Any Ptr) As ELOG_LEVEL
	Declare Sub SIrrlichtCreationParameters_set_LoggingLevel(ByVal _pointer_ As Any Ptr, ByVal value As ELOG_LEVEL)
	Declare Function SIrrlichtCreationParameters_get_SDK_version_do_not_use(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function Q3LevelLoadParameter_ctor1() As Any Ptr
	Declare Function Q3LevelLoadParameter_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function Q3LevelLoadParameter_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub Q3LevelLoadParameter_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function Q3LevelLoadParameter_get_defaultLightMapMaterial(ByVal _pointer_ As Any Ptr) As E_MATERIAL_TYPE
	Declare Sub Q3LevelLoadParameter_set_defaultLightMapMaterial(ByVal _pointer_ As Any Ptr, ByVal value As E_MATERIAL_TYPE)
	Declare Function Q3LevelLoadParameter_get_defaultModulate(ByVal _pointer_ As Any Ptr) As E_MODULATE_FUNC
	Declare Sub Q3LevelLoadParameter_set_defaultModulate(ByVal _pointer_ As Any Ptr, ByVal value As E_MODULATE_FUNC)
	Declare Function Q3LevelLoadParameter_get_defaultFilter(ByVal _pointer_ As Any Ptr) As E_MATERIAL_FLAG
	Declare Sub Q3LevelLoadParameter_set_defaultFilter(ByVal _pointer_ As Any Ptr, ByVal value As E_MATERIAL_FLAG)
	Declare Function Q3LevelLoadParameter_get_patchTesselation(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_patchTesselation(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_verbose(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_verbose(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_startTime(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub Q3LevelLoadParameter_set_startTime(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function Q3LevelLoadParameter_get_endTime(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub Q3LevelLoadParameter_set_endTime(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function Q3LevelLoadParameter_get_mergeShaderBuffer(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_mergeShaderBuffer(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_cleanUnResolvedMeshes(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_cleanUnResolvedMeshes(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_loadAllShaders(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_loadAllShaders(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_loadSkyShader(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_loadSkyShader(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_alpharef(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_alpharef(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_swapLump(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_swapLump(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_swapHeader(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub Q3LevelLoadParameter_set_swapHeader(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function Q3LevelLoadParameter_get_scriptDir(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub Q3LevelLoadParameter_set_scriptDir(ByVal _pointer_ As Any Ptr, ByVal value64 As ZString Ptr)
	Declare Function Q3LevelLoadParameter_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SBlendFunc_ctor(ByVal _mod_ As E_MODULATE_FUNC) As Any Ptr
	Declare Function SBlendFunc_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SBlendFunc_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SBlendFunc_get_type(ByVal _pointer_ As Any Ptr) As E_MATERIAL_TYPE
	Declare Sub SBlendFunc_set_type(ByVal _pointer_ As Any Ptr, ByVal value As E_MATERIAL_TYPE)
	Declare Function SBlendFunc_get_modulate(ByVal _pointer_ As Any Ptr) As E_MODULATE_FUNC
	Declare Sub SBlendFunc_set_modulate(ByVal _pointer_ As Any Ptr, ByVal value As E_MODULATE_FUNC)
	Declare Function SBlendFunc_get_param0(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SBlendFunc_set_param0(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SBlendFunc_get_isTransparent(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SBlendFunc_set_isTransparent(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function Noiser_ctor1() As Any Ptr
	Declare Function Noiser_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function Noiser_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub Noiser_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function Noiser_get(ByVal _pointer_ As Any Ptr) As Single
	Declare Function SModifierFunction_ctor1() As Any Ptr
	Declare Function SModifierFunction_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SModifierFunction_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SModifierFunction_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SModifierFunction_get_masterfunc0(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_masterfunc0(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_masterfunc1(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_masterfunc1(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_func(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_func(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_tcgen(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_tcgen(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_rgbgen(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_rgbgen(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_alphagen(ByVal _pointer_ As Any Ptr) As eQ3ModifierFunction
	Declare Sub SModifierFunction_set_alphagen(ByVal _pointer_ As Any Ptr, ByVal value As eQ3ModifierFunction)
	Declare Function SModifierFunction_get_base(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_base(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_bulgewidth(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_bulgewidth(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_amp(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_amp(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_bulgeheight(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_bulgeheight(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_phase(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_phase(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_frequency(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_frequency(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_bulgespeed(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_bulgespeed(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_wave(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_wave(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_div(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_div(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_x(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_x(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_y(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_y(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_z(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SModifierFunction_set_z(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SModifierFunction_get_count(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SModifierFunction_set_count(ByVal _pointer_ As Any Ptr, ByVal value As UInteger)
	Declare Function SModifierFunction_evaluate(ByVal _pointer_ As Any Ptr, ByVal dt As Single) As Single
	Declare Function SVariable_ctor(ByVal n As ZString Ptr, ByVal c As ZString Ptr) As Any Ptr
	Declare Function SVariable_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SVariable_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SVariable_get_name(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SVariable_set_name(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SVariable_get_content(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SVariable_set_content(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Sub SVariable_clear(ByVal _pointer_ As Any Ptr)
	Declare Function SVariable_isValid(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function SVariable_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SVariable_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SVarGroup_ctor1() As Any Ptr
	Declare Function SVarGroup_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SVarGroup_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SVarGroup_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SVarGroup_isDefined(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal content As ZString Ptr) As UInteger
	Declare Function SVarGroup_get(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As ZString Ptr
	Declare Sub SVarGroup_set(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal content As ZString Ptr)
	Declare Function SVarGroup_get_Variable(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SVarGroup_set_Variable(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SVarGroupList_ctor1() As Any Ptr
	Declare Function SVarGroupList_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SVarGroupList_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SVarGroupList_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SVarGroupList_get_VariableGroup(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SVarGroupList_set_VariableGroup(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function IShader_ctor1() As Any Ptr
	Declare Function IShader_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function IShader_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub IShader_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Sub IShader_operator_set(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function IShader_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function IShader_operator_lt(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function IShader_getGroupSize(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IShader_getGroup(ByVal _pointer_ As Any Ptr, ByVal stage As UInteger) As Any Ptr
	Declare Function IShader_get_ID(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IShader_set_ID(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function IShader_get_VarGroup(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IShader_set_VarGroup(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function IShader_get_name(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub IShader_set_name(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function tQ3EntityList_ctor() As Any Ptr
	Declare Sub tQ3EntityList_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Sub tQ3EntityList_setAllocStrategy(ByVal _pointer_ As Any Ptr, ByVal newStrategy As eAllocStrategy)
	Declare Sub tQ3EntityList_push_back(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub tQ3EntityList_push_front(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr)
	Declare Sub tQ3EntityList_insert(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal index As UInteger)
	Declare Sub tQ3EntityList_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub tQ3EntityList_set_pointer(ByVal _pointer_ As Any Ptr, ByVal newPointer As Any Ptr, ByVal _size_ As UInteger, ByVal _is_sorted As UByte, ByVal _free_when_destroyed As UByte)
	Declare Sub tQ3EntityList_set_free_when_destroyed(ByVal _pointer_ As Any Ptr, ByVal f As UByte)
	Declare Sub tQ3EntityList_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Function tQ3EntityList_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function tQ3EntityList_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function tQ3EntityList_empty(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub tQ3EntityList_sort(ByVal _pointer_ As Any Ptr)
	Declare Function tQ3EntityList_binary_search1(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function tQ3EntityList_binary_search2(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal left As Integer, ByVal right As Integer) As Integer
	Declare Function tQ3EntityList_binary_search_multi(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr, ByVal last As Integer) As Integer
	Declare Function tQ3EntityList_linear_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Function tQ3EntityList_linear_reverse_search(ByVal _pointer_ As Any Ptr, ByVal element As Any Ptr) As Integer
	Declare Sub tQ3EntityList_erase1(ByVal _pointer_ As Any Ptr, ByVal index As UInteger)
	Declare Sub tQ3EntityList_erase2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal count As Integer)
	Declare Sub tQ3EntityList_set_sorted(ByVal _pointer_ As Any Ptr, ByVal _is_sorted As UByte)
	Declare Sub tQ3EntityList_swap(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function tool_getAsVector3df(ByVal string As ZString Ptr, ByVal pos As UInteger) As Any Ptr
	Declare Function tool_getAsFloat(ByVal string As ZString Ptr, ByVal pos As UInteger) As Single
	Declare Sub tool_getTextures(ByVal textures As Any Ptr, ByVal _name_ As ZString Ptr, ByVal startPos As UInteger, ByVal fileSystem As Any Ptr, ByVal driver As Any Ptr)
	Declare Function IGUIEditBox_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIEditBox_setOverrideFont(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr)
	Declare Sub IGUIEditBox_setOverrideColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IGUIEditBox_enableOverrideColor(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Sub IGUIEditBox_setDrawBorder(ByVal _pointer_ As Any Ptr, ByVal border As UByte)
	Declare Sub IGUIEditBox_setTextAlignment(ByVal _pointer_ As Any Ptr, ByVal horizontal As EGUI_ALIGNMENT, ByVal vertical As EGUI_ALIGNMENT)
	Declare Sub IGUIEditBox_setWordWrap(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIEditBox_isWordWrapEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIEditBox_setMultiLine(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIEditBox_isMultiLineEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIEditBox_setAutoScroll(ByVal _pointer_ As Any Ptr, ByVal enable As UByte)
	Declare Function IGUIEditBox_isAutoScrollEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUIEditBox_setPasswordBox(ByVal _pointer_ As Any Ptr, ByVal passwordBox As UByte, ByVal passwordChar As WString Ptr)
	Declare Function IGUIEditBox_isPasswordBox(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIEditBox_getTextDimension(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUIEditBox_setMax(ByVal _pointer_ As Any Ptr, ByVal max As UInteger)
	Declare Function IGUIEditBox_getMax(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IGUITreeViewNode_getOwner(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getParent(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getText(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Sub IGUITreeViewNode_setText(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr)
	Declare Function IGUITreeViewNode_getIcon(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Sub IGUITreeViewNode_setIcon(ByVal _pointer_ As Any Ptr, ByVal icon As WString Ptr)
	Declare Function IGUITreeViewNode_getImageIndex(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IGUITreeViewNode_setImageIndex(ByVal _pointer_ As Any Ptr, ByVal imageIndex As UInteger)
	Declare Function IGUITreeViewNode_getSelectedImageIndex(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IGUITreeViewNode_setSelectedImageIndex(ByVal _pointer_ As Any Ptr, ByVal imageIndex As UInteger)
	Declare Function IGUITreeViewNode_getData(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUITreeViewNode_setData(ByVal _pointer_ As Any Ptr, ByVal _data_ As Any Ptr)
	Declare Function IGUITreeViewNode_getData2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUITreeViewNode_setData2(ByVal _pointer_ As Any Ptr, ByVal _data_ As Any Ptr)
	Declare Function IGUITreeViewNode_getChildCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IGUITreeViewNode_clearChilds(ByVal _pointer_ As Any Ptr)
	Declare Function IGUITreeViewNode_hasChilds(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUITreeViewNode_addChildBack(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal icon As WString Ptr, ByVal imageIndex As Integer, ByVal selectedImageIndex As Integer, ByVal _data_ As Any Ptr, ByVal _data_2 As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_addChildFront(ByVal _pointer_ As Any Ptr, ByVal text As WString Ptr, ByVal icon As WString Ptr, ByVal imageIndex As Integer, ByVal selectedImageIndex As Integer, ByVal _data_ As Any Ptr, ByVal _data_2 As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_insertChildAfter(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal text As WString Ptr, ByVal icon As WString Ptr, ByVal imageIndex As Integer, ByVal selectedImageIndex As Integer, ByVal _data_ As Any Ptr, ByVal _data_2 As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_insertChildBefore(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal text As WString Ptr, ByVal icon As WString Ptr, ByVal imageIndex As Integer, ByVal selectedImageIndex As Integer, ByVal _data_ As Any Ptr, ByVal _data_2 As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getFirstChild(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getLastChild(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getPrevSibling(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getNextSibling(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_getNextVisible(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeViewNode_deleteChild(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr) As UByte
	Declare Function IGUITreeViewNode_moveChildUp(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr) As UByte
	Declare Function IGUITreeViewNode_moveChildDown(ByVal _pointer_ As Any Ptr, ByVal child As Any Ptr) As UByte
	Declare Function IGUITreeViewNode_getExpanded(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUITreeViewNode_setExpanded(ByVal _pointer_ As Any Ptr, ByVal expanded As UByte)
	Declare Function IGUITreeViewNode_getSelected(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUITreeViewNode_setSelected(ByVal _pointer_ As Any Ptr, ByVal selected As UByte)
	Declare Function IGUITreeViewNode_isRoot(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUITreeViewNode_getLevel(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IGUITreeViewNode_isVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUITreeView_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUITreeView_getRoot(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeView_getSelected(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUITreeView_getLinesVisible(ByVal _pointer_ As Any Ptr) As UByte
	Declare Sub IGUITreeView_setLinesVisible(ByVal _pointer_ As Any Ptr, ByVal visible As UByte)
	Declare Sub IGUITreeView_setIconFont(ByVal _pointer_ As Any Ptr, ByVal font As Any Ptr)
	Declare Sub IGUITreeView_setImageList(ByVal _pointer_ As Any Ptr, ByVal imageList As Any Ptr)
	Declare Function IGUITreeView_getImageList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IGUITreeView_setImageLeftOfIcon(ByVal _pointer_ As Any Ptr, ByVal bLeftOf As UByte)
	Declare Function IGUITreeView_getImageLeftOfIcon(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUITreeView_getLastEventNode(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIImage_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUIImage_setImage(ByVal _pointer_ As Any Ptr, ByVal image As Any Ptr)
	Declare Sub IGUIImage_setColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IGUIImage_setScaleImage(ByVal _pointer_ As Any Ptr, ByVal scale As UByte)
	Declare Sub IGUIImage_setUseAlphaChannel(ByVal _pointer_ As Any Ptr, ByVal use As UByte)
	Declare Function IGUIImage_isImageScaled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIImage_isAlphaChannelUsed(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function SMD3AnimationInfo_ctor() As Any Ptr
	Declare Function SMD3AnimationInfo_get_first(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3AnimationInfo_set_first(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3AnimationInfo_get_num(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3AnimationInfo_set_num(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3AnimationInfo_get_looping(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3AnimationInfo_set_looping(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3AnimationInfo_get_fps(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3AnimationInfo_set_fps(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_ctor() As Any Ptr
	Declare Function SMD3Header_get_headerID(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3Header_set_headerID(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3Header_get_Version(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_Version(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_fileName(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Header_set_fileName(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3Header_get_numFrames(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_numFrames(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_numTags(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_numTags(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_numMeshes(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_numMeshes(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_numMaxSkins(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_numMaxSkins(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_frameStart(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_frameStart(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_tagStart(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_tagStart(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_tagEnd(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_tagEnd(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Header_get_fileSize(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3Header_set_fileSize(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_ctor() As Any Ptr
	Declare Function SMD3MeshHeader_get_meshID(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3MeshHeader_set_meshID(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3MeshHeader_get_meshName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3MeshHeader_set_meshName(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3MeshHeader_get_numFrames(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_numFrames(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_numShader(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_numShader(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_numVertices(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_numVertices(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_numTriangles(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_numTriangles(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_offset_triangles(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_offset_triangles(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_offset_shaders(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_offset_shaders(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_offset_st(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_offset_st(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_vertexStart(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_vertexStart(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3MeshHeader_get_offset_end(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub SMD3MeshHeader_set_offset_end(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function SMD3Vertex_ctor() As Any Ptr
	Declare Function SMD3Vertex_get_position(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Vertex_set_position(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3Vertex_get_normal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Vertex_set_normal(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3TexCoord_ctor() As Any Ptr
	Declare Function SMD3TexCoord_get_u(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SMD3TexCoord_set_u(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SMD3TexCoord_get_v(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub SMD3TexCoord_set_v(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function SMD3Face_ctor() As Any Ptr
	Declare Function SMD3Face_get_Index(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Face_set_Index(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3MeshBuffer_ctor() As Any Ptr
	Declare Function SMD3MeshBuffer_get_MeshHeader(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3MeshBuffer_set_MeshHeader(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3MeshBuffer_get_Shader(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3MeshBuffer_set_Shader(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3MeshBuffer_get_Indices(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3MeshBuffer_set_Indices(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3MeshBuffer_get_Vertices(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3MeshBuffer_set_Vertices(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3MeshBuffer_get_Tex(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3MeshBuffer_set_Tex(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3QuaternionTag_ctor1(ByVal _name_ As ZString Ptr) As Any Ptr
	Declare Function SMD3QuaternionTag_ctor2(ByVal _name_ As ZString Ptr, ByVal m As Any Ptr) As Any Ptr
	Declare Function SMD3QuaternionTag_ctor3(ByVal pos As Any Ptr, ByVal angle As Any Ptr) As Any Ptr
	Declare Function SMD3QuaternionTag_ctor4(ByVal copyMe As Any Ptr) As Any Ptr
	Declare Sub SMD3QuaternionTag_setto(ByVal _pointer_ As Any Ptr, ByVal m As Any Ptr)
	Declare Function SMD3QuaternionTag_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function SMD3QuaternionTag_operator_set(ByVal _pointer_ As Any Ptr, ByVal copyMe As Any Ptr) As Any Ptr
	Declare Function SMD3QuaternionTag_get_Name(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3QuaternionTag_set_Name(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3QuaternionTag_get_position(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3QuaternionTag_set_position(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3QuaternionTag_get_rotation(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3QuaternionTag_set_rotation(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3QuaternionTagList_ctor1() As Any Ptr
	Declare Function SMD3QuaternionTagList_ctor2(ByVal copyMe As Any Ptr) As Any Ptr
	Declare Function SMD3QuaternionTagList_get(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr) As Any Ptr
	Declare Function SMD3QuaternionTagList_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub SMD3QuaternionTagList_set_used(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Function SMD3QuaternionTagList_const_operator_index(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function SMD3QuaternionTagList_operator_index(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Sub SMD3QuaternionTagList_push_back(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function SMD3QuaternionTagList_operator_set(ByVal _pointer_ As Any Ptr, ByVal copyMe As Any Ptr) As Any Ptr
	Declare Sub SMD3QuaternionTagList_set_tag_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal item As Any Ptr)
	Declare Function SMD3Mesh_ctor() As Any Ptr
	Declare Function SMD3Mesh_get_Name(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Sub SMD3Mesh_set_Name(ByVal _pointer_ As Any Ptr, ByVal value As ZString Ptr)
	Declare Function SMD3Mesh_get_Buffer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Mesh_set_Buffer(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3Mesh_get_TagList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Mesh_set_TagList(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function SMD3Mesh_get_MD3Header(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMD3Mesh_set_MD3Header(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Sub IAnimatedMeshMD3_setInterpolationShift(ByVal _pointer_ As Any Ptr, ByVal shift As UInteger, ByVal _loop_Mode As UInteger)
	Declare Function IAnimatedMeshMD3_getTagList(ByVal _pointer_ As Any Ptr, ByVal frame As Integer, ByVal detailLevel As Integer, ByVal startFrameLoop As Integer, ByVal _end_FrameLoop As Integer) As Any Ptr
	Declare Function IAnimatedMeshMD3_getOriginalMesh(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IAnimatedMeshMD2_getFrameLoop1(ByVal _pointer_ As Any Ptr, ByVal l As EMD2_ANIMATION_TYPE, ByVal outBegin As Integer, ByVal outEnd As Integer, ByVal outFPS As Integer)
	Declare Function IAnimatedMeshMD2_getFrameLoop2(ByVal _pointer_ As Any Ptr, ByVal _name_ As ZString Ptr, ByVal outBegin As Integer, ByVal outEnd As Integer, ByVal outFPS As Integer) As UByte
	Declare Function IAnimatedMeshMD2_getAnimationCount(ByVal _pointer_ As Any Ptr) As Integer
	Declare Function IAnimatedMeshMD2_getAnimationName(ByVal _pointer_ As Any Ptr, ByVal nr As Integer) As ZString Ptr
	Declare Function IGUIColorSelectDialog_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUICheckBox_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Sub IGUICheckBox_setChecked(ByVal _pointer_ As Any Ptr, ByVal checked As UByte)
	Declare Function IGUICheckBox_isChecked(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IGUIFontBitmap_getType(ByVal _pointer_ As Any Ptr) As EGUI_FONT_TYPE
	Declare Function IGUIFontBitmap_getSpriteBank(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IGUIFontBitmap_getSpriteNoFromChar(ByVal _pointer_ As Any Ptr, ByVal c As WString Ptr) As UInteger
	Declare Function IGUIFontBitmap_getKerningWidth(ByVal _pointer_ As Any Ptr, ByVal thisLetter As WString Ptr, ByVal previousLetter As WString Ptr) As Integer
	Declare Function IGUIFileOpenDialog_ctor(ByVal environment As Any Ptr, ByVal parent As Any Ptr, ByVal id As Integer, ByVal rectangle As Any Ptr) As Any Ptr
	Declare Function IGUIFileOpenDialog_getFileName(ByVal _pointer_ As Any Ptr) As WString Ptr
	Declare Function IGUIFileOpenDialog_getDirectoryName(ByVal _pointer_ As Any Ptr) As fschar
	Declare Function IQ3LevelMesh_getShader1(ByVal _pointer_ As Any Ptr, ByVal filename As ZString Ptr, ByVal fileNameIsValid As UByte) As Any Ptr
	Declare Function IQ3LevelMesh_getShader2(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IQ3LevelMesh_getEntityList(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getVertexBuffer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getIndexBuffer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IDynamicMeshBuffer_setVertexBuffer(ByVal _pointer_ As Any Ptr, ByVal vertexBuffer As Any Ptr)
	Declare Sub IDynamicMeshBuffer_setIndexBuffer(ByVal _pointer_ As Any Ptr, ByVal indexBuffer As Any Ptr)
	Declare Function IDynamicMeshBuffer_getMaterial1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getMaterial2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IDynamicMeshBuffer_setBoundingBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub IDynamicMeshBuffer_recalculateBoundingBox(ByVal _pointer_ As Any Ptr)
	Declare Sub IDynamicMeshBuffer_append1(ByVal _pointer_ As Any Ptr, ByVal vertices As Any Ptr, ByVal numVertices As UInteger, ByVal indices As Any Ptr, ByVal numIndices As UInteger)
	Declare Sub IDynamicMeshBuffer_append2(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr)
	Declare Function IDynamicMeshBuffer_getHardwareMappingHint_Vertex(ByVal _pointer_ As Any Ptr) As E_HARDWARE_MAPPING
	Declare Function IDynamicMeshBuffer_getHardwareMappingHint_Index(ByVal _pointer_ As Any Ptr) As E_HARDWARE_MAPPING
	Declare Sub IDynamicMeshBuffer_setHardwareMappingHint(ByVal _pointer_ As Any Ptr, ByVal NewMappingHint As E_HARDWARE_MAPPING, ByVal Buffer As E_BUFFER_TYPE)
	Declare Sub IDynamicMeshBuffer_setDirty(ByVal _pointer_ As Any Ptr, ByVal Buffer As E_BUFFER_TYPE)
	Declare Function IDynamicMeshBuffer_getChangedID_Vertex(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IDynamicMeshBuffer_getChangedID_Index(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IDynamicMeshBuffer_getVertexType(ByVal _pointer_ As Any Ptr) As E_VERTEX_TYPE
	Declare Function IDynamicMeshBuffer_getVertices1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getVertices2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getVertexCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IDynamicMeshBuffer_getIndexType(ByVal _pointer_ As Any Ptr) As E_INDEX_TYPE
	Declare Function IDynamicMeshBuffer_getIndices1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getIndices2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IDynamicMeshBuffer_getIndexCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IDynamicMeshBuffer_getPosition1(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IDynamicMeshBuffer_getPosition2(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IDynamicMeshBuffer_getTCoords1(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IDynamicMeshBuffer_getTCoords2(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IDynamicMeshBuffer_getNormal1(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IDynamicMeshBuffer_getNormal2(ByVal _pointer_ As Any Ptr, ByVal i As UInteger) As Any Ptr
	Declare Function IVolumeLightSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Function IVolumeLightSceneNode_getType(ByVal _pointer_ As Any Ptr) As ESCENE_NODE_TYPE
	Declare Sub IVolumeLightSceneNode_setSubDivideU(ByVal _pointer_ As Any Ptr, ByVal inU As UInteger)
	Declare Sub IVolumeLightSceneNode_setSubDivideV(ByVal _pointer_ As Any Ptr, ByVal inV As UInteger)
	Declare Function IVolumeLightSceneNode_getSubDivideU(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IVolumeLightSceneNode_getSubDivideV(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IVolumeLightSceneNode_setFootColor(ByVal _pointer_ As Any Ptr, ByVal inColour As Any Ptr)
	Declare Sub IVolumeLightSceneNode_setTailColor(ByVal _pointer_ As Any Ptr, ByVal inColour As Any Ptr)
	Declare Function IVolumeLightSceneNode_getFootColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IVolumeLightSceneNode_getTailColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CDynamicMeshBuffer_ctor(ByVal vertexType As E_VERTEX_TYPE, ByVal indexType As E_INDEX_TYPE) As Any Ptr
	Declare Function CDynamicMeshBuffer_getVertexBuffer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CDynamicMeshBuffer_getIndexBuffer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub CDynamicMeshBuffer_setVertexBuffer(ByVal _pointer_ As Any Ptr, ByVal newVertexBuffer As Any Ptr)
	Declare Sub CDynamicMeshBuffer_setIndexBuffer(ByVal _pointer_ As Any Ptr, ByVal newIndexBuffer As Any Ptr)
	Declare Function CDynamicMeshBuffer_getMaterial1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function CDynamicMeshBuffer_getMaterial2(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub CDynamicMeshBuffer_setMaterial(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function CDynamicMeshBuffer_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub CDynamicMeshBuffer_setBoundingBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub CDynamicMeshBuffer_recalculateBoundingBox(ByVal _pointer_ As Any Ptr)
	Declare Function ISceneNodeAnimatorFactory_createSceneNodeAnimator1(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_ANIMATOR_TYPE, ByVal target As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorFactory_createSceneNodeAnimator2(ByVal _pointer_ As Any Ptr, ByVal _type_Name As ZString Ptr, ByVal target As Any Ptr) As Any Ptr
	Declare Function ISceneNodeAnimatorFactory_getCreatableSceneNodeAnimatorTypeCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorType(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As ESCENE_NODE_ANIMATOR_TYPE
	Declare Function ISceneNodeAnimatorFactory_getCreateableScNodeAnimatorTypeName1 Alias "ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1" (ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As ZString Ptr
	Declare Function ISceneNodeAnimatorFactory_getCreateableScNodeAnimatorTypeName2 Alias "ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2" (ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_ANIMATOR_TYPE) As ZString Ptr
	Declare Function ISceneNodeFactory_addSceneNode1(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_TYPE, ByVal parent As Any Ptr) As Any Ptr
	Declare Function ISceneNodeFactory_addSceneNode2(ByVal _pointer_ As Any Ptr, ByVal _type_Name As ZString Ptr, ByVal parent As Any Ptr) As Any Ptr
	Declare Function ISceneNodeFactory_getCreatableSceneNodeTypeCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function ISceneNodeFactory_getCreateableSceneNodeType(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As ESCENE_NODE_TYPE
	Declare Function ISceneNodeFactory_getCreateableSceneNodeTypeName1(ByVal _pointer_ As Any Ptr, ByVal idx As UInteger) As ZString Ptr
	Declare Function ISceneNodeFactory_getCreateableSceneNodeTypeName2(ByVal _pointer_ As Any Ptr, ByVal _type_ As ESCENE_NODE_TYPE) As ZString Ptr
	Declare Function IParticleAffector_ctor() As Any Ptr
	Declare Sub IParticleAffector_affect(ByVal _pointer_ As Any Ptr, ByVal now As UInteger, ByVal particlearray As Any Ptr, ByVal count As UInteger)
	Declare Sub IParticleAffector_setEnabled(ByVal _pointer_ As Any Ptr, ByVal enabled As UByte)
	Declare Function IParticleAffector_getEnabled(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAffector_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_AFFECTOR_TYPE
	Declare Sub IParticleAnimatedMeshSceneNodeEmitter_setAnimatedMeshSceneNode(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Sub IParticleAnimatedMeshSceneNodeEmitter_setUseNormalDirection(ByVal _pointer_ As Any Ptr, ByVal useNormalDirection As UByte)
	Declare Sub IParticleAnimatedMeshSceneNodeEmitter_setNormalDirectionModifier(ByVal _pointer_ As Any Ptr, ByVal normalDirectionModifier As Single)
	Declare Sub IParticleAnimatedMeshSceneNodeEmitter_setEveryMeshVertex(ByVal _pointer_ As Any Ptr, ByVal everyMeshVertex As UByte)
	Declare Function IParticleAnimatedMeshSceneNodeEmitter_getAnimatedMeshSceneNode(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleAnimatedMeshSceneNodeEmitter_isUsingNormalDirection(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAnimatedMeshSceneNodeEmitter_getNormalDirectionModifier(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleAnimatedMeshSceneNodeEmitter_getEveryMeshVertex(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAnimatedMeshSceneNodeEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Sub IParticleAttractionAffector_setPoint(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr)
	Declare Sub IParticleAttractionAffector_setAttract(ByVal _pointer_ As Any Ptr, ByVal attract As UByte)
	Declare Sub IParticleAttractionAffector_setAffectX(ByVal _pointer_ As Any Ptr, ByVal affect As UByte)
	Declare Sub IParticleAttractionAffector_setAffectY(ByVal _pointer_ As Any Ptr, ByVal affect As UByte)
	Declare Sub IParticleAttractionAffector_setAffectZ(ByVal _pointer_ As Any Ptr, ByVal affect As UByte)
	Declare Function IParticleAttractionAffector_getPoint(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleAttractionAffector_getAttract(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAttractionAffector_getAffectX(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAttractionAffector_getAffectY(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAttractionAffector_getAffectZ(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleAttractionAffector_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_AFFECTOR_TYPE
	Declare Sub IParticleBoxEmitter_setBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Function IParticleBoxEmitter_getBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleBoxEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Sub IParticleCylinderEmitter_setCenter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr)
	Declare Sub IParticleCylinderEmitter_setNormal(ByVal _pointer_ As Any Ptr, ByVal normal As Any Ptr)
	Declare Sub IParticleCylinderEmitter_setRadius(ByVal _pointer_ As Any Ptr, ByVal radius As Single)
	Declare Sub IParticleCylinderEmitter_setLength(ByVal _pointer_ As Any Ptr, ByVal _len_gth As Single)
	Declare Sub IParticleCylinderEmitter_setOutlineOnly(ByVal _pointer_ As Any Ptr, ByVal outlineOnly As UByte)
	Declare Function IParticleCylinderEmitter_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleCylinderEmitter_getNormal(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleCylinderEmitter_getRadius(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleCylinderEmitter_getLength(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleCylinderEmitter_getOutlineOnly(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleCylinderEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Function IParticleEmitter_emitt(ByVal _pointer_ As Any Ptr, ByVal now As UInteger, ByVal timeSinceLastCall As UInteger, ByVal outArray As Any Ptr) As Integer
	Declare Sub IParticleEmitter_setDirection(ByVal _pointer_ As Any Ptr, ByVal newDirection As Any Ptr)
	Declare Sub IParticleEmitter_setMinParticlesPerSecond(ByVal _pointer_ As Any Ptr, ByVal minPPS As UInteger)
	Declare Sub IParticleEmitter_setMaxParticlesPerSecond(ByVal _pointer_ As Any Ptr, ByVal maxPPS As UInteger)
	Declare Sub IParticleEmitter_setMinStartColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IParticleEmitter_setMaxStartColor(ByVal _pointer_ As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IParticleEmitter_setMaxStartSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Sub IParticleEmitter_setMinStartSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Function IParticleEmitter_getDirection(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleEmitter_getMinParticlesPerSecond(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IParticleEmitter_getMaxParticlesPerSecond(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IParticleEmitter_getMinStartColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleEmitter_getMaxStartColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleEmitter_getMaxStartSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleEmitter_getMinStartSize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Sub IParticleFadeOutAffector_setTargetColor(ByVal _pointer_ As Any Ptr, ByVal targetColor As Any Ptr)
	Declare Sub IParticleFadeOutAffector_setFadeOutTime(ByVal _pointer_ As Any Ptr, ByVal fadeOutTime As Single)
	Declare Function IParticleFadeOutAffector_getTargetColor(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleFadeOutAffector_getFadeOutTime(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleFadeOutAffector_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_AFFECTOR_TYPE
	Declare Sub IParticleGravityAffector_setTimeForceLost(ByVal _pointer_ As Any Ptr, ByVal timeForceLost As Single)
	Declare Sub IParticleGravityAffector_setGravity(ByVal _pointer_ As Any Ptr, ByVal gravity As Any Ptr)
	Declare Function IParticleGravityAffector_getTimeForceLost(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleGravityAffector_getGravity(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleGravityAffector_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_AFFECTOR_TYPE
	Declare Sub IParticleMeshEmitter_setMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Sub IParticleMeshEmitter_setUseNormalDirection(ByVal _pointer_ As Any Ptr, ByVal useNormalDirection As UByte)
	Declare Sub IParticleMeshEmitter_setNormalDirectionModifier(ByVal _pointer_ As Any Ptr, ByVal normalDirectionModifier As Single)
	Declare Sub IParticleMeshEmitter_setEveryMeshVertex(ByVal _pointer_ As Any Ptr, ByVal everyMeshVertex As UByte)
	Declare Function IParticleMeshEmitter_getMesh(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleMeshEmitter_isUsingNormalDirection(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleMeshEmitter_getNormalDirectionModifier(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleMeshEmitter_getEveryMeshVertex(ByVal _pointer_ As Any Ptr) As UByte
	Declare Function IParticleMeshEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Sub IParticleRingEmitter_setCenter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr)
	Declare Sub IParticleRingEmitter_setRadius(ByVal _pointer_ As Any Ptr, ByVal radius As Single)
	Declare Sub IParticleRingEmitter_setRingThickness(ByVal _pointer_ As Any Ptr, ByVal ringThickness As Single)
	Declare Function IParticleRingEmitter_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleRingEmitter_getRadius(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleRingEmitter_getRingThickness(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleRingEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Sub IParticleRotationAffector_setPivotPoint(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr)
	Declare Sub IParticleRotationAffector_setSpeed(ByVal _pointer_ As Any Ptr, ByVal speed As Any Ptr)
	Declare Function IParticleRotationAffector_getPivotPoint(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleRotationAffector_getSpeed(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleRotationAffector_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_AFFECTOR_TYPE
	Declare Sub IParticleSphereEmitter_setCenter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr)
	Declare Sub IParticleSphereEmitter_setRadius(ByVal _pointer_ As Any Ptr, ByVal radius As Single)
	Declare Function IParticleSphereEmitter_getCenter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IParticleSphereEmitter_getRadius(ByVal _pointer_ As Any Ptr) As Single
	Declare Function IParticleSphereEmitter_getType(ByVal _pointer_ As Any Ptr) As E_PARTICLE_EMITTER_TYPE
	Declare Function IParticleSystemSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer, ByVal position As Any Ptr, ByVal rotation As Any Ptr, ByVal scale As Any Ptr) As Any Ptr
	Declare Sub IParticleSystemSceneNode_setParticleSize(ByVal _pointer_ As Any Ptr, ByVal _size_ As Any Ptr)
	Declare Sub IParticleSystemSceneNode_setParticlesAreGlobal(ByVal _pointer_ As Any Ptr, ByVal global As UByte)
	Declare Function IParticleSystemSceneNode_getEmitter(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IParticleSystemSceneNode_setEmitter(ByVal _pointer_ As Any Ptr, ByVal emitter As Any Ptr)
	Declare Sub IParticleSystemSceneNode_addAffector(ByVal _pointer_ As Any Ptr, ByVal affector As Any Ptr)
	Declare Sub IParticleSystemSceneNode_removeAllAffectors(ByVal _pointer_ As Any Ptr)
	Declare Function IParticleSystemSceneNode_createAnimatedMeshSceneNodeEmitter(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr, ByVal useNormalDirection As UByte, ByVal direction As Any Ptr, ByVal normalDirectionModifier As Single, ByVal mbNumber As Integer, ByVal everyMeshVertex As UByte, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createBoxEmitter(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr, ByVal direction As Any Ptr, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createCylinderEmitter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal radius As Single, ByVal normal As Any Ptr, ByVal _len_gth As Single, ByVal outlineOnly As UByte, ByVal direction As Any Ptr, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createMeshEmitter(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal useNormalDirection As UByte, ByVal direction As Any Ptr, ByVal normalDirectionModifier As Single, ByVal mbNumber As Integer, ByVal everyMeshVertex As UByte, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createPointEmitter(ByVal _pointer_ As Any Ptr, ByVal direction As Any Ptr, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createRingEmitter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal radius As Single, ByVal ringThickness As Single, ByVal direction As Any Ptr, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createSphereEmitter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal radius As Single, ByVal direction As Any Ptr, ByVal minParticlesPerSecond As UInteger, ByVal maxParticlesPerSecond As UInteger, ByVal minStartColor As Any Ptr, ByVal maxStartColor As Any Ptr, ByVal lifeTimeMin As UInteger, ByVal lifeTimeMax As UInteger, ByVal maxAngleDegrees As Integer, ByVal minStartSize As Any Ptr, ByVal maxStartSize As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createAttractionAffector(ByVal _pointer_ As Any Ptr, ByVal _point_ As Any Ptr, ByVal speed As Single, ByVal attract As UByte, ByVal affectX As UByte, ByVal affectY As UByte, ByVal affectZ As UByte) As Any Ptr
	Declare Function IParticleSystemSceneNode_createScaleParticleAffector(ByVal _pointer_ As Any Ptr, ByVal scaleTo As Any Ptr) As Any Ptr
	Declare Function IParticleSystemSceneNode_createFadeOutParticleAffector(ByVal _pointer_ As Any Ptr, ByVal targetColor As Any Ptr, ByVal timeNeededToFadeOut As UInteger) As Any Ptr
	Declare Function IParticleSystemSceneNode_createGravityAffector(ByVal _pointer_ As Any Ptr, ByVal gravity As Any Ptr, ByVal timeForceLost As UInteger) As Any Ptr
	Declare Function IParticleSystemSceneNode_createRotationAffector(ByVal _pointer_ As Any Ptr, ByVal speed As Any Ptr, ByVal pivotPoint As Any Ptr) As Any Ptr
	Declare Sub IMeshManipulator_flipSurfaces(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Sub IMeshManipulator_setVertexColorAlpha(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal alpha As Integer)
	Declare Sub IMeshManipulator_setVertexColors(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal _color_ As Any Ptr)
	Declare Sub IMeshManipulator_recalculateNormals1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal smooth As UByte, ByVal angleWeighted As UByte)
	Declare Sub IMeshManipulator_recalculateNormals2(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal smooth As UByte, ByVal angleWeighted As UByte)
	Declare Sub IMeshManipulator_recalculateTangents(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal recalculateNormals As UByte, ByVal smooth As UByte, ByVal angleWeighted As UByte)
	Declare Sub IMeshManipulator_scale1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal factor As Any Ptr)
	Declare Sub IMeshManipulator_scale2(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal factor As Any Ptr)
	Declare Sub IMeshManipulator_scaleMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal factor As Any Ptr)
	Declare Sub IMeshManipulator_scaleTCoords1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal factor As Any Ptr, ByVal level As UInteger)
	Declare Sub IMeshManipulator_scaleTCoords2(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal factor As Any Ptr, ByVal level As UInteger)
	Declare Sub IMeshManipulator_transform1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal m As Any Ptr)
	Declare Sub IMeshManipulator_transform2(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal m As Any Ptr)
	Declare Sub IMeshManipulator_transformMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal m As Any Ptr)
	Declare Function IMeshManipulator_createMeshCopy(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Sub IMeshManipulator_makePlanarTextureMapping1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal resolution As Single)
	Declare Sub IMeshManipulator_makePlanarTextureMapping2(ByVal _pointer_ As Any Ptr, ByVal meshbuffer As Any Ptr, ByVal resolution As Single)
	Declare Sub IMeshManipulator_makePlanarTextureMapping3(ByVal _pointer_ As Any Ptr, ByVal buffer As Any Ptr, ByVal resolutionS As Single, ByVal resolutionT As Single, ByVal axis As ZString Ptr, ByVal offset As Any Ptr)
	Declare Function IMeshManipulator_createMeshWithTangents(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal recalculateNormals As UByte, ByVal smooth As UByte, ByVal angleWeighted As UByte, ByVal recalculateTangents As UByte) As Any Ptr
	Declare Function IMeshManipulator_createMeshWith2TCoords(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function IMeshManipulator_createMeshWith1TCoords(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function IMeshManipulator_createMeshUniquePrimitives(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function IMeshManipulator_createMeshWelded(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal _to_lerance As Single) As Any Ptr
	Declare Function IMeshManipulator_getPolyCount1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Integer
	Declare Function IMeshManipulator_getPolyCount2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Integer
	Declare Function IMeshManipulator_createAnimatedMesh(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal _type_ As E_ANIMATED_MESH_TYPE) As Any Ptr
	Declare Function S3DVertex_ctor1(ByVal _len_gth As Integer) As Any Ptr
	Declare Function S3DVertex_ctor2(ByVal x As Single, ByVal y As Single, ByVal z As Single, ByVal nx As Single, ByVal ny As Single, ByVal nz As Single, ByVal c As Any Ptr, ByVal tu As Single, ByVal tv As Single) As Any Ptr
	Declare Function S3DVertex_ctor3(ByVal pos As Any Ptr, ByVal normal As Any Ptr, ByVal _color_ As Any Ptr, ByVal tcoords As Any Ptr) As Any Ptr
	Declare Function S3DVertex_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub S3DVertex_set_item(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function S3DVertex_get_Pos(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub S3DVertex_set_Pos(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function S3DVertex_get_Normal(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub S3DVertex_set_Normal(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function S3DVertex_get_Color(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub S3DVertex_set_Color(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function S3DVertex_get_TCoords(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub S3DVertex_set_TCoords(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function S3DVertex_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal index As Integer) As UByte
	Declare Function S3DVertex_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal index As Integer) As UByte
	Declare Function S3DVertex_less(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal index As Integer) As UByte
	Declare Function S3DVertex_getType(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As E_VERTEX_TYPE
	Declare Function IImageLoader_isALoadableFileExtension(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As UByte
	Declare Function IImageLoader_isALoadableFileFormat(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As UByte
	Declare Function IImageLoader_loadImage(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr) As Any Ptr
	Declare Function IImageWriter_isAWriteableFileExtension(ByVal _pointer_ As Any Ptr, ByVal filename As fschar) As UByte
	Declare Function IImageWriter_writeImage(ByVal _pointer_ As Any Ptr, ByVal file As Any Ptr, ByVal image As Any Ptr, ByVal param As UInteger) As UByte
	Declare Function IIndexBuffer_getData(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IIndexBuffer_getType(ByVal _pointer_ As Any Ptr) As E_INDEX_TYPE
	Declare Sub IIndexBuffer_setType(ByVal _pointer_ As Any Ptr, ByVal IndexType As E_INDEX_TYPE)
	Declare Function IIndexBuffer_stride(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IIndexBuffer_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IIndexBuffer_push_back(ByVal _pointer_ As Any Ptr, ByVal element As UInteger)
	Declare Function IIndexBuffer_get_item(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As UInteger
	Declare Function IIndexBuffer_getLast(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub IIndexBuffer_setValue(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal value As UInteger)
	Declare Sub IIndexBuffer_set_used(ByVal _pointer_ As Any Ptr, ByVal usedNow As UInteger)
	Declare Sub IIndexBuffer_reallocate(ByVal _pointer_ As Any Ptr, ByVal new_size As UInteger)
	Declare Function IIndexBuffer_allocated_size(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IIndexBuffer_pointer(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function IIndexBuffer_getHardwareMappingHint(ByVal _pointer_ As Any Ptr) As E_HARDWARE_MAPPING
	Declare Sub IIndexBuffer_setHardwareMappingHint(ByVal _pointer_ As Any Ptr, ByVal NewMappingHint As E_HARDWARE_MAPPING)
	Declare Sub IIndexBuffer_setDirty(ByVal _pointer_ As Any Ptr)
	Declare Function IIndexBuffer_getChangedID(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Sub ILightManager_OnPreRender(ByVal _pointer_ As Any Ptr, ByVal lightList As Any Ptr)
	Declare Sub ILightManager_OnPostRender(ByVal _pointer_ As Any Ptr)
	Declare Sub ILightManager_OnRenderPassPreRender(ByVal _pointer_ As Any Ptr, ByVal renderPass As E_SCENE_NODE_RENDER_PASS)
	Declare Sub ILightManager_OnRenderPassPostRender(ByVal _pointer_ As Any Ptr, ByVal renderPass As E_SCENE_NODE_RENDER_PASS)
	Declare Sub ILightManager_OnNodePreRender(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Sub ILightManager_OnNodePostRender(ByVal _pointer_ As Any Ptr, ByVal node As Any Ptr)
	Declare Function IBoneSceneNode_ctor(ByVal parent As Any Ptr, ByVal mgr As Any Ptr, ByVal id As Integer) As Any Ptr
	Declare Function IBoneSceneNode_getBoneName(ByVal _pointer_ As Any Ptr) As ZString Ptr
	Declare Function IBoneSceneNode_getBoneIndex(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IBoneSceneNode_setAnimationMode(ByVal _pointer_ As Any Ptr, ByVal _mod_e As E_BONE_ANIMATION_MODE) As UByte
	Declare Function IBoneSceneNode_getAnimationMode(ByVal _pointer_ As Any Ptr) As E_BONE_ANIMATION_MODE
	Declare Function IBoneSceneNode_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub IBoneSceneNode_OnAnimate(ByVal _pointer_ As Any Ptr, ByVal timeMs As UInteger)
	Declare Sub IBoneSceneNode_render(ByVal _pointer_ As Any Ptr)
	Declare Sub IBoneSceneNode_setSkinningSpace(ByVal _pointer_ As Any Ptr, ByVal space As E_BONE_SKINNING_SPACE)
	Declare Function IBoneSceneNode_getSkinningSpace(ByVal _pointer_ As Any Ptr) As E_BONE_SKINNING_SPACE
	Declare Sub IBoneSceneNode_updateAbsolutePositionOfAllChildren(ByVal _pointer_ As Any Ptr)
	Declare Sub IBoneSceneNode_set_positionHint(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function IBoneSceneNode_get_positionHint(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IBoneSceneNode_set_scaleHint(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function IBoneSceneNode_get_scaleHint(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IBoneSceneNode_set_rotationHint(ByVal _pointer_ As Any Ptr, ByVal value As Integer)
	Declare Function IBoneSceneNode_get_rotationHint(ByVal _pointer_ As Any Ptr) As Integer
	Declare Sub IMeshCache_addMesh(ByVal _pointer_ As Any Ptr, ByVal _name_ As fschar, ByVal mesh As Any Ptr)
	Declare Sub IMeshCache_removeMesh1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Sub IMeshCache_removeMesh2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr)
	Declare Function IMeshCache_getMeshCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function IMeshCache_getMeshIndex1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Integer
	Declare Function IMeshCache_getMeshIndex2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Integer
	Declare Function IMeshCache_getMeshByIndex(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IMeshCache_getMeshByName(ByVal _pointer_ As Any Ptr, ByVal _name_ As fschar) As Any Ptr
	Declare Function IMeshCache_getMeshNameByIndex(ByVal _pointer_ As Any Ptr, ByVal index As UInteger) As Any Ptr
	Declare Function IMeshCache_getMeshName1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function IMeshCache_getMeshName2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr) As Any Ptr
	Declare Function IMeshCache_renameMeshByIndex(ByVal _pointer_ As Any Ptr, ByVal index As UInteger, ByVal _name_ As fschar) As UByte
	Declare Function IMeshCache_renameMesh1(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal _name_ As fschar) As UByte
	Declare Function IMeshCache_renameMesh2(ByVal _pointer_ As Any Ptr, ByVal mesh As Any Ptr, ByVal _name_ As fschar) As UByte
	Declare Function IMeshCache_isMeshLoaded(ByVal _pointer_ As Any Ptr, ByVal _name_ As fschar) As UByte
	Declare Sub IMeshCache_clear(ByVal _pointer_ As Any Ptr)
	Declare Sub IMeshCache_clearUnusedMeshes(ByVal _pointer_ As Any Ptr)
	Declare Function SParticle_ctor(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SParticle_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_item(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_pos(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_pos(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_vector(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_vector(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_startTime(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As UInteger
	Declare Sub SParticle_set_startTime(ByVal _pointer_ As Any Ptr, ByVal value As UInteger, ByVal index As Integer)
	Declare Function SParticle_get_endTime(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As UInteger
	Declare Sub SParticle_set_endTime(ByVal _pointer_ As Any Ptr, ByVal value As UInteger, ByVal index As Integer)
	Declare Function SParticle_get_color(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_color(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_startColor(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_startColor(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_startVector(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_startVector(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_size(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_size(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SParticle_get_startSize(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SParticle_set_startSize(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr, ByVal index As Integer)
	Declare Function SMesh_ctor1() As Any Ptr
	Declare Function SMesh_ctor2(ByVal _len_gth As Integer) As Any Ptr
	Declare Function SMesh_get_item(ByVal _pointer_ As Any Ptr, ByVal index As Integer) As Any Ptr
	Declare Sub SMesh_set_item(ByVal _pointer_ As Any Ptr, ByVal item As Any Ptr, ByVal index As Integer)
	Declare Function SMesh_getMeshBufferCount(ByVal _pointer_ As Any Ptr) As UInteger
	Declare Function SMesh_getMeshBuffer1(ByVal _pointer_ As Any Ptr, ByVal nr As UInteger) As Any Ptr
	Declare Function SMesh_getMeshBuffer2(ByVal _pointer_ As Any Ptr, ByVal material As Any Ptr) As Any Ptr
	Declare Function SMesh_getBoundingBox(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMesh_setBoundingBox(ByVal _pointer_ As Any Ptr, ByVal box As Any Ptr)
	Declare Sub SMesh_recalculateBoundingBox(ByVal _pointer_ As Any Ptr)
	Declare Sub SMesh_addMeshBuffer(ByVal _pointer_ As Any Ptr, ByVal buf As Any Ptr)
	Declare Sub SMesh_setMaterialFlag(ByVal _pointer_ As Any Ptr, ByVal flag As E_MATERIAL_FLAG, ByVal newvalue As UByte)
	Declare Sub SMesh_setHardwareMappingHint(ByVal _pointer_ As Any Ptr, ByVal newMappingHint As E_HARDWARE_MAPPING, ByVal buffer_type As E_BUFFER_TYPE)
	Declare Sub SMesh_setDirty(ByVal _pointer_ As Any Ptr, ByVal buffer_type As E_BUFFER_TYPE)
	Declare Function SMesh_get_MeshBuffers(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Sub SMesh_set_MeshBuffers(ByVal _pointer_ As Any Ptr, ByVal value As Any Ptr)
	Declare Function quaternion_ctor1() As Any Ptr
	Declare Function quaternion_ctor2(ByVal x As Single, ByVal y As Single, ByVal z As Single, ByVal w As Single) As Any Ptr
	Declare Function quaternion_ctor3(ByVal x As Single, ByVal y As Single, ByVal z As Single) As Any Ptr
	Declare Function quaternion_ctor4(ByVal vec As Any Ptr) As Any Ptr
	Declare Function quaternion_ctor5(ByVal mat As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_eq(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function quaternion_operator_ne(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As UByte
	Declare Function quaternion_operator_set1(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_set2(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_add(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_mul1(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_mul2(ByVal _pointer_ As Any Ptr, ByVal s As Single) As Any Ptr
	Declare Function quaternion_operator_mul3(ByVal _pointer_ As Any Ptr, ByVal v As Any Ptr) As Any Ptr
	Declare Function quaternion_operator_mul_set1(ByVal _pointer_ As Any Ptr, ByVal s As Single) As Any Ptr
	Declare Function quaternion_operator_mul_set2(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Any Ptr
	Declare Function quaternion_dotProduct(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr) As Single
	Declare Function quaternion_set1(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single, ByVal z As Single, ByVal w As Single) As Any Ptr
	Declare Function quaternion_set2(ByVal _pointer_ As Any Ptr, ByVal x As Single, ByVal y As Single, ByVal z As Single) As Any Ptr
	Declare Function quaternion_set3(ByVal _pointer_ As Any Ptr, ByVal vec As Any Ptr) As Any Ptr
	Declare Function quaternion_set4(ByVal _pointer_ As Any Ptr, ByVal quat As Any Ptr) As Any Ptr
	Declare Function quaternion_equals(ByVal _pointer_ As Any Ptr, ByVal other As Any Ptr, ByVal _to_lerance As Single) As UByte
	Declare Function quaternion_normalize(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_getMatrix1(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_getMatrix2(ByVal _pointer_ As Any Ptr, ByVal translation As Any Ptr) As Any Ptr
	Declare Function quaternion_getMatrixCenter(ByVal _pointer_ As Any Ptr, ByVal center As Any Ptr, ByVal translation As Any Ptr) As Any Ptr
	Declare Function quaternion_getMatrix_transposed(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_makeInverse(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_slerp(ByVal _pointer_ As Any Ptr, ByVal q1 As Any Ptr, ByVal q2 As Any Ptr, ByVal interpolate As Single) As Any Ptr
	Declare Function quaternion_fromAngleAxis(ByVal _pointer_ As Any Ptr, ByVal angle As Single, ByVal axis As Any Ptr) As Any Ptr
	Declare Function quaternion_toAngleAxis(ByVal _pointer_ As Any Ptr, ByVal axis As Any Ptr) As Single
	Declare Function quaternion_toEuler(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_makeIdentity(ByVal _pointer_ As Any Ptr) As Any Ptr
	Declare Function quaternion_rotationFromTo(ByVal _pointer_ As Any Ptr, ByVal from As Any Ptr, ByVal _to_ As Any Ptr) As Any Ptr
	Declare Function quaternion_get_X(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub quaternion_set_X(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function quaternion_get_Y(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub quaternion_set_Y(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function quaternion_get_Z(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub quaternion_set_Z(ByVal _pointer_ As Any Ptr, ByVal value As Single)
	Declare Function quaternion_get_W(ByVal _pointer_ As Any Ptr) As Single
	Declare Sub quaternion_set_W(ByVal _pointer_ As Any Ptr, ByVal value As Single)


End Extern

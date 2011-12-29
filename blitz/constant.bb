; constants for Irrlicht Blitz3D wrapper
; original idea by Atulos, many thanks him
; programming Maxim Kolosov

Const EDT_NULL = 0
Const EDT_SOFTWARE = 1
Const EDT_BURNINGSVIDEO = 2
Const EDT_DIRECT3D8 = 3;not supported with irrlicht_c.dll, if you want this, you must recompile dll with DirectX 8 SDK
Const EDT_DIRECT3D9 = 4
Const EDT_OPENGL = 5

Const E_MATERIAL_FLAG = $0
Const EMF_WIREFRAME = $1
Const EMF_POINTCLOUD = $2
Const EMF_GOURAUD_SHADING = $4
Const EMF_LIGHTING = $8
Const EMF_ZBUFFER = $10
Const EMF_ZWRITE_ENABLE = $20
Const EMF_BACK_FACE_CULLING = $40
Const EMF_FRONT_FACE_CULLING = $80
Const EMF_BILINEAR_FILTER = $100
Const EMF_TRILINEAR_FILTER = $200
Const EMF_ANISOTROPIC_FILTER = $400
Const EMF_FOG_ENABLE = $800
Const EMF_NORMALIZE_NORMALS = $1000
Const EMF_TEXTURE_WRAP = $2000
Const EMF_ANTI_ALIASING = $4000
Const EMF_COLOR_MASK = $8000
Const EMF_COLOR_MATERIAL = $10000

Const EMD2_ANIMATION_TYPE = 0
Const EMAT_STAND = 0
Const EMAT_RUN = 1
Const EMAT_ATTACK = 2
Const EMAT_PAIN_A = 3
Const EMAT_PAIN_B = 4
Const EMAT_PAIN_C = 5
Const EMAT_JUMP = 6
Const EMAT_FLIP = 7
Const EMAT_SALUTE = 8
Const EMAT_FALLBACK = 9
Const EMAT_WAVE = 10
Const EMAT_POINT = 11
Const EMAT_CROUCH_STAND = 12
Const EMAT_CROUCH_WALK = 13
Const EMAT_CROUCH_ATTACK = 14
Const EMAT_CROUCH_PAIN = 15
Const EMAT_CROUCH_DEATH = 16
Const EMAT_DEATH_FALLBACK = 17
Const EMAT_DEATH_FALLFORWARD = 18
Const EMAT_DEATH_FALLBACKSLOW = 19
Const EMAT_BOOM = 20
Const EMAT_COUNT = 21

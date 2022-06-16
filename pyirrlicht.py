# Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
# github.com/usermicrodevices
# BSD license

__version__ = pyirrlicht_version = '1.2.3'
__version_date__ = '2022-06-16'
__author__ = 'Maxim Kolosov'
__author_email__ = 'pyirrlicht@gmail.com'
__doc__ = '''
pyirrlicht.py - is ctypes python module for
Irrlicht Engine SDK (https://irrlicht.sourceforge.io).
'''

IRR_ENCODING = 'cp1251'

IDI_APPLICATION = 32512
IDI_HAND = 32513
IDI_QUESTION = 32514
IDI_EXCLAMATION = 32515
IDI_ASTERISK = 32516
IDI_WINLOGO = 32517
IDI_SHIELD = 32518

import ctypes
from sys import hexversion, platform

if hexversion < 0x02060000:
	ctypes.c_bool = ctypes.c_byte

class FILE(ctypes.Structure):
	pass
if hexversion >= 0x03000000:
	type_str = bytes
	type_unicode = str
else:
	type_str = str
	type_unicode = unicode

from os import environ, getcwd
c_module_name = 'irrlicht_c'
if 'IRRLICHT_C_LIBRARY' in environ:
	c_module_name = environ['IRRLICHT_C_LIBRARY']
	del environ

c_module = None
func_type = ctypes.CFUNCTYPE
if platform in ('windows', 'win32'):
	c_module = ctypes.WinDLL(c_module_name)
	func_type = ctypes.WINFUNCTYPE
else:
	c_module = ctypes.CDLL(f'{getcwd()}/{c_module_name}.so')

IRRLICHT_VERSION_MAJOR = ctypes.c_ubyte.in_dll(c_module, '_IRRLICHT_VERSION_MAJOR').value
IRRLICHT_VERSION_MINOR = ctypes.c_ubyte.in_dll(c_module, '_IRRLICHT_VERSION_MINOR').value
IRRLICHT_VERSION_REVISION = ctypes.c_ubyte.in_dll(c_module, '_IRRLICHT_VERSION_REVISION').value
IRRLICHT_VERSION = ctypes.c_ubyte.in_dll(c_module, '_IRRLICHT_VERSION').value

eAllocStrategy = 0
ALLOC_STRATEGY_SAFE = 0
ALLOC_STRATEGY_DOUBLE = 1
ALLOC_STRATEGY_SQRT = 2

IRR_WCHAR_FILESYSTEM = ctypes.c_bool.in_dll(c_module, 'IRR_WCHAR_FILESYSTEM').value
fschar_t = ctypes.c_char_p
if IRR_WCHAR_FILESYSTEM:
	fschar_t = ctypes.c_wchar_p

def fs_conv(value, encoding = IRR_ENCODING):
	if hexversion >= 0x03020000:
		if IRR_WCHAR_FILESYSTEM:
			return value
		else:
			return bytes(value, encoding)
	else:
		return value

def as_ansi(value, encoding = IRR_ENCODING):
	if hexversion >= 0x03020000:
		return bytes(value, encoding)
	else:
		return value

IRR_IMPROVE_UNICODE = ctypes.c_bool.in_dll(c_module, 'IRR_IMPROVE_UNICODE').value
IRR_USE_INPUT_METHOD = ctypes.c_bool.in_dll(c_module, 'IRR_USE_INPUT_METHOD').value

eQ3MeshIndex = 0
E_Q3_MESH_GEOMETRY = 0
E_Q3_MESH_ITEMS = 1
E_Q3_MESH_BILLBOARD = 2
E_Q3_MESH_FOG = 3
E_Q3_MESH_UNRESOLVED = 4
E_Q3_MESH_SIZE = 5

E_ANTI_ALIASING_MODE = 0
EAAM_OFF = 0
EAAM_SIMPLE = 1
EAAM_QUALITY = 3
EAAM_LINE_SMOOTH = 4
EAAM_POINT_SMOOTH = 8
EAAM_FULL_BASIC = 15
EAAM_ALPHA_TO_COVERAGE = 16

EAC_OFF = 0
EAC_BOX = 1
EAC_FRUSTUM_BOX = 2
EAC_FRUSTUM_SPHERE = 4

EAMT_UNKNOWN = 0
EAMT_MD2 = 1
EAMT_MD3 = 2
EAMT_OBJ = 3
EAMT_BSP = 4
EAMT_3DS = 5
EAMT_MY3D = 6
EAMT_LMTS = 7
EAMT_CSM = 8
EAMT_OCT = 9
EAMT_SKINNED = 10

EARWF_FOR_FILE = 0x00000001
EARWF_FOR_EDITOR = 0x00000002
EARWF_USE_RELATIVE_PATHS = 0x00000004

EAS_NONE = 0
EAS_VERTEX_COLOR = 1
EAS_TEXTURE = 2

EAT_INT = 0
EAT_FLOAT = 1
EAT_STRING = 2
EAT_BOOL = 3
EAT_ENUM = 4
EAT_COLOR = 5
EAT_COLORF = 6
EAT_VECTOR3D = 7
EAT_POSITION2D = 8
EAT_VECTOR2D = 9
EAT_RECT = 10
EAT_MATRIX = 11
EAT_QUATERNION = 12
EAT_BBOX = 13
EAT_PLANE = 14
EAT_TRIANGLE3D = 15
EAT_LINE2D = 16
EAT_LINE3D = 17
EAT_STRINGWARRAY = 18
EAT_FLOATARRAY = 19
EAT_INTARRAY = 20
EAT_BINARY = 21
EAT_TEXTURE = 22
EAT_USER_POINTER = 23
EAT_COUNT = 24
EAT_UNKNOWN = 25

E_BLEND_FACTOR = 0
EBF_ZERO = 0
EBF_ONE = 1
EBF_DST_COLOR = 2
EBF_ONE_MINUS_DST_COLOR = 3
EBF_SRC_COLOR = 4
EBF_ONE_MINUS_SRC_COLOR = 5
EBF_SRC_ALPHA = 6
EBF_ONE_MINUS_SRC_ALPHA = 7
EBF_DST_ALPHA = 8
EBF_ONE_MINUS_DST_ALPHA = 9
EBF_SRC_ALPHA_SATURATE = 10

E_BLEND_OPERATION = 0
EBO_NONE = 0		#!< No blending happens
EBO_ADD = 1			#!< Default blending adds the color values
EBO_SUBTRACT = 2	#!< This mode subtracts the color values
EBO_REVSUBTRACT = 3	#!< This modes subtracts destination from source
EBO_MIN = 4			#!< Choose minimum value of each color channel
EBO_MAX = 5			#!< Choose maximum value of each color channel
EBO_MIN_FACTOR = 6	#!< Choose minimum value of each color channel after applying blend factors, not widely supported
EBO_MAX_FACTOR = 7	#!< Choose maximum value of each color channel after applying blend factors, not widely supported
EBO_MIN_ALPHA = 8	#!< Choose minimum value of each color channel based on alpha value, not widely supported
EBO_MAX_ALPHA = 9	#!< Choose maximum value of each color channel based on alpha value, not widely supported

EBT_NONE = 0
EBT_VERTEX = 1
EBT_INDEX = 2
EBT_VERTEX_AND_INDEX = 3

ECOLOR_FORMAT = 0
ECF_A1R5G5B5 = ECOLOR_FORMAT
ECF_R5G6B5 = 1
ECF_R8G8B8 = 2
ECF_A8R8G8B8 = 3
ECF_R16F = 4
ECF_G16R16F = 5
ECF_A16B16G16R16F = 6
ECF_R32F = 7
ECF_G32R32F = 8
ECF_A32B32G32R32F = 9
ECF_UNKNOWN = 10

ECFN_NEVER = 0
ECFN_LESSEQUAL = 1
ECFN_EQUAL = 2
ECFN_LESS = 3
ECFN_NOTEQUAL = 4
ECFN_GREATEREQUAL = 5
ECFN_GREATER = 6
ECFN_ALWAYS = 7

ECM_NONE = 0
ECM_DIFFUSE = 1
ECM_AMBIENT = 2
ECM_EMISSIVE = 3
ECM_SPECULAR = 4
ECM_DIFFUSE_AND_AMBIENT = 5

ECMC_IGNORE = 0
ECMC_REMOVE = 1
ECMC_HIDE = 2

ECP_NONE = 0
ECP_ALPHA = 1
ECP_RED = 2
ECP_GREEN = 4
ECP_BLUE = 8
ECP_RGB = 14
ECP_ALL = 15

E_DEBUG_SCENE_TYPE = 0
EDS_OFF = E_DEBUG_SCENE_TYPE
EDS_BBOX = 1
EDS_NORMALS = 2
EDS_SKELETON = 4
EDS_MESH_WIRE_OVERLAY = 8
EDS_HALF_TRANSPARENCY = 16
EDS_BBOX_BUFFERS = 32
EDS_BBOX_ALL = EDS_BBOX | EDS_BBOX_BUFFERS
EDS_FULL = 0xffffffff

E_DRIVER_TYPE = 0
EDT_NULL = 0
EDT_SOFTWARE = 1
EDT_BURNINGSVIDEO = 2
EDT_DIRECT3D8 = 3
EDT_DIRECT3D9 = 4
EDT_OPENGL = 5
EDT_COUNT = 6

EET_GUI_EVENT = 0
EET_MOUSE_INPUT_EVENT = 1
EET_KEY_INPUT_EVENT = 2
EET_JOYSTICK_INPUT_EVENT = 3
EET_LOG_TEXT_EVENT = 4
EET_USER_EVENT = 5
if IRR_USE_INPUT_METHOD:
	EET_IMPUT_METHOD_EVENT = 5
	EET_USER_EVENT = 6
	EIME_CHAR_INPUT = 0
	EIME_CHANGE_POS = 1
	EIME_FORCE_32_BIT = 0x7fffffff

EGBS_BUTTON_UP = 0
EGBS_BUTTON_DOWN = 1
EGBS_BUTTON_MOUSE_OVER = 2
EGBS_BUTTON_MOUSE_OFF = 3
EGBS_BUTTON_FOCUSED = 4
EGBS_BUTTON_NOT_FOCUSED = 5
EGBS_COUNT = 6

EGDC_3D_DARK_SHADOW = 0
EGDC_3D_SHADOW = 1
EGDC_3D_FACE = 2
EGDC_3D_HIGH_LIGHT = 3
EGDC_3D_LIGHT = 4
EGDC_ACTIVE_BORDER = 5
EGDC_ACTIVE_CAPTION = 6
EGDC_APP_WORKSPACE = 7
EGDC_BUTTON_TEXT = 8
EGDC_GRAY_TEXT = 9
EGDC_HIGH_LIGHT = 10
EGDC_HIGH_LIGHT_TEXT = 11
EGDC_INACTIVE_BORDER = 12
EGDC_INACTIVE_CAPTION = 13
EGDC_TOOLTIP = 14
EGDC_TOOLTIP_BACKGROUND = 15
EGDC_SCROLLBAR = 16
EGDC_WINDOW = 17
EGDC_WINDOW_SYMBOL = 18
EGDC_ICON = 19
EGDC_ICON_HIGH_LIGHT = 20
EGDC_COUNT = 21

EGDF_DEFAULT = 0
EGDF_BUTTON = 1
EGDF_WINDOW = 2
EGDF_MENU = 3
EGDF_TOOLTIP = 4
EGDF_COUNT = 5

EGDI_WINDOW_MAXIMIZE = 0
EGDI_WINDOW_RESTORE = 1
EGDI_WINDOW_CLOSE = 2
EGDI_WINDOW_MINIMIZE = 3
EGDI_WINDOW_RESIZE = 4
EGDI_CURSOR_UP = 5
EGDI_CURSOR_DOWN = 6
EGDI_CURSOR_LEFT = 7
EGDI_CURSOR_RIGHT = 8
EGDI_MENU_MORE = 9
EGDI_CHECK_BOX_CHECKED = 10
EGDI_DROP_DOWN = 11
EGDI_SMALL_CURSOR_UP = 12
EGDI_SMALL_CURSOR_DOWN = 13
EGDI_RADIO_BUTTON_CHECKED = 14
EGDI_MORE_LEFT = 15
EGDI_MORE_RIGHT = 16
EGDI_MORE_UP = 17
EGDI_MORE_DOWN = 18
EGDI_EXPAND = 19
EGDI_COLLAPSE = 20
EGDI_FILE = 21
EGDI_DIRECTORY = 22
EGDI_COUNT = 23

EGDS_SCROLLBAR_SIZE = 0
EGDS_MENU_HEIGHT = 1
EGDS_WINDOW_BUTTON_WIDTH = 2
EGDS_CHECK_BOX_WIDTH = 3
EGDS_MESSAGE_BOX_WIDTH = 4
EGDS_MESSAGE_BOX_HEIGHT = 5
EGDS_BUTTON_WIDTH = 6
EGDS_BUTTON_HEIGHT = 7
EGDS_TEXT_DISTANCE_X = 8
EGDS_TEXT_DISTANCE_Y = 9
EGDS_TITLEBARTEXT_DISTANCE_X = 10
EGDS_TITLEBARTEXT_DISTANCE_Y = 11
EGDS_MESSAGE_BOX_GAP_SPACE = 12
EGDS_MESSAGE_BOX_MIN_TEXT_WIDTH = 13
EGDS_MESSAGE_BOX_MAX_TEST_WIDTH = 14
EGDS_MESSAGE_BOX_MIN_TEXT_HEIGHT = 15
EGDS_MESSAGE_BOX_MAX_TEXT_HEIGHT = 16
EGDS_COUNT = 17

EGDT_MSG_BOX_OK = 0
EGDT_MSG_BOX_CANCEL = 1
EGDT_MSG_BOX_YES = 2
EGDT_MSG_BOX_NO = 3
EGDT_WINDOW_CLOSE = 4
EGDT_WINDOW_MAXIMIZE = 5
EGDT_WINDOW_MINIMIZE = 6
EGDT_WINDOW_RESTORE = 7
EGDT_COUNT = 8

EGST_WINDOWS_CLASSIC = 0
EGST_WINDOWS_METALLIC = 1
EGST_BURNING_SKIN = 2
EGST_UNKNOWN = 3
EGST_COUNT = 4

EGUIET_FORCE_32_BIT = 0x7fffffff

EGUIA_UPPERLEFT = 0
EGUIA_LOWERRIGHT = 1
EGUIA_CENTER = 2
EGUIA_SCALE = 3

EGUIET_BUTTON = 0
EGUIET_CHECK_BOX = 1
EGUIET_COMBO_BOX = 2
EGUIET_CONTEXT_MENU = 3
EGUIET_MENU = 4
EGUIET_EDIT_BOX = 5
EGUIET_FILE_OPEN_DIALOG = 6
EGUIET_COLOR_SELECT_DIALOG = 7
EGUIET_IN_OUT_FADER = 8
EGUIET_IMAGE = 9
EGUIET_LIST_BOX = 10
EGUIET_MESH_VIEWER = 11
EGUIET_MESSAGE_BOX = 12
EGUIET_MODAL_SCREEN = 13
EGUIET_SCROLL_BAR = 14
EGUIET_SPIN_BOX = 15
EGUIET_STATIC_TEXT = 16
EGUIET_TAB = 17
EGUIET_TAB_CONTROL = 18
EGUIET_TABLE = 19
EGUIET_TOOL_BAR = 20
EGUIET_TREE_VIEW = 21
EGUIET_WINDOW = 22
EGUIET_ELEMENT = 23
EGUIET_COUNT = 24
EGUIET_FORCE_32_BIT = 0x7fffffff

EGUI_COLUMN_ORDERING = 0
EGCO_NONE = 0
EGCO_CUSTOM = 1
EGCO_ASCENDING = 2
EGCO_DESCENDING = 3
EGCO_FLIP_ASCENDING_DESCENDING = 4
EGCO_COUNT = 5

EGUI_ORDERING_MODE = 0
EGOM_NONE = 0
EGOM_ASCENDING = 1
EGOM_DESCENDING = 2
EGOM_COUNT = 3

EGUI_TABLE_DRAW_FLAGS = 0
EGTDF_ROWS = 1
EGTDF_COLUMNS = 2
EGTDF_ACTIVE_ROW = 4
EGTDF_COUNT = 5

# E_FILE_ARCHIVE_TYPE
EFAT_ZIP     = ctypes.c_int.in_dll(c_module, '_EFAT_ZIP').value
EFAT_GZIP    = ctypes.c_int.in_dll(c_module, '_EFAT_GZIP').value
EFAT_FOLDER  = ctypes.c_int.in_dll(c_module, '_EFAT_FOLDER').value
EFAT_PAK     = ctypes.c_int.in_dll(c_module, '_EFAT_PAK').value
EFAT_TAR     = ctypes.c_int.in_dll(c_module, '_EFAT_TAR').value
EFAT_UNKNOWN = ctypes.c_int.in_dll(c_module, '_EFAT_UNKNOWN').value

#E_FOG_TYPE
EFT_FOG_EXP = 0
EFT_FOG_LINEAR = 1
EFT_FOG_EXP2 = 2

EGET_ELEMENT_FOCUS_LOST = 0
EGET_ELEMENT_FOCUSED = 1
EGET_ELEMENT_HOVERED = 2
EGET_ELEMENT_LEFT = 3
EGET_ELEMENT_CLOSED = 4
EGET_BUTTON_CLICKED = 5
EGET_SCROLL_BAR_CHANGED = 6
EGET_CHECKBOX_CHANGED = 7
EGET_LISTBOX_CHANGED = 8
EGET_LISTBOX_SELECTED_AGAIN = 9
EGET_FILE_SELECTED = 10
EGET_DIRECTORY_SELECTED = 11
EGET_FILE_CHOOSE_DIALOG_CANCELLED = 12
EGET_MESSAGEBOX_YES = 13
EGET_MESSAGEBOX_NO = 14
EGET_MESSAGEBOX_OK = 15
EGET_MESSAGEBOX_CANCEL = 16
EGET_EDITBOX_ENTER = 17
EGET_EDITBOX_CHANGED = 18
EGET_EDITBOX_MARKING_CHANGED = 19
EGET_TAB_CHANGED = 20
EGET_MENU_ITEM_SELECTED = 21
EGET_COMBO_BOX_CHANGED = 22
EGET_SPINBOX_CHANGED = 23
EGET_TABLE_CHANGED = 24
EGET_TABLE_HEADER_CHANGED = 25
EGET_TABLE_SELECTED_AGAIN = 26
EGET_TREEVIEW_NODE_DESELECT = 27
EGET_TREEVIEW_NODE_SELECT = 28
EGET_TREEVIEW_NODE_EXPAND = 29
EGET_TREEVIEW_NODE_COLLAPS = 30
EGET_COUNT = 31

EGFT_BITMAP = 0
EGFT_VECTOR = 1
EGFT_OS = 2
EGFT_CUSTOM = 3

EHM_NEVER = 0
EHM_STATIC = 1
EHM_DYNAMIC = 2
EHM_STREAM = 3

EIDT_WIN32 = 0
EIDT_WINCE = 1
EIDT_X11 = 2
EIDT_OSX = 3
EIDT_SDL = 4
EIDT_CONSOLE = 5
EIDT_BEST = 6

EIT_16BIT = 0
EIT_32BIT = 1

EJUOR_NONE = 0
EJUOR_READ = 1
EJUOR_CONTROL = 2
EJUOR_COUNT = 3

EKA_MOVE_FORWARD = 0
EKA_MOVE_BACKWARD = 1
EKA_STRAFE_LEFT = 2
EKA_STRAFE_RIGHT = 3
EKA_JUMP_UP = 4
EKA_CROUCH = 5
EKA_COUNT = 6
EKA_FORCE_32BIT = 0x7fffffff

ELL_INFORMATION = 0
ELL_WARNING = 1
ELL_ERROR = 2
ELL_NONE = 3

#E_LOST_RESOURCE
ELR_DEVICE = 1
ELR_TEXTURES = 2
ELR_RTTS = 4
ELR_HW_BUFFERS = 8

E_LIGHT_TYPE = 0
ELT_POINT = 0
ELT_SPOT = 1
ELT_DIRECTIONAL = 2

EM4CONST_NOTHING = 0
EM4CONST_COPY = 1
EM4CONST_IDENTITY = 2
EM4CONST_TRANSPOSED = 3
EM4CONST_INVERSE = 4
EM4CONST_INVERSE_TRANSPOSED = 5

EMD2_ANIMATION_TYPE = 0
EMAT_STAND = 0
EMAT_RUN = 1
EMAT_ATTACK = 2
EMAT_PAIN_A = 3
EMAT_PAIN_B = 4
EMAT_PAIN_C = 5
EMAT_JUMP = 6
EMAT_FLIP = 7
EMAT_SALUTE = 8
EMAT_FALLBACK = 9
EMAT_WAVE = 10
EMAT_POINT = 11
EMAT_CROUCH_STAND = 12
EMAT_CROUCH_WALK = 13
EMAT_CROUCH_ATTACK = 14
EMAT_CROUCH_PAIN = 15
EMAT_CROUCH_DEATH = 16
EMAT_DEATH_FALLBACK = 17
EMAT_DEATH_FALLFORWARD = 18
EMAT_DEATH_FALLBACKSLOW = 19
EMAT_BOOM = 20
EMAT_COUNT = 21

EMBF_OK = 0x1
EMBF_CANCEL = 0x2
EMBF_YES = 0x4
EMBF_NO = 0x8
EMBF_FORCE_32BIT = 0x7fffffff

#E_MOUSE_BUTTON_STATE_MASK
EMBSM_LEFT    = 0x01
EMBSM_RIGHT   = 0x02
EMBSM_MIDDLE  = 0x04
EMBSM_EXTRA1  = 0x08
EMBSM_EXTRA2  = 0x10
EMBSM_FORCE_32_BIT = 0x7fffffff

eMD3Models = 0
EMD3_HEAD = 0
EMD3_UPPER = 1
EMD3_LOWER = 2
EMD3_WEAPON = 3
EMD3_NUMMODELS = 4

EMD3_ANIMATION_TYPE = 0
EMD3_BOTH_DEATH_1 = 0
EMD3_BOTH_DEAD_1 = 1
EMD3_BOTH_DEATH_2 = 2
EMD3_BOTH_DEAD_2 = 3
EMD3_BOTH_DEATH_3 = 4
EMD3_BOTH_DEAD_3 = 5
EMD3_TORSO_GESTURE = 6
EMD3_TORSO_ATTACK_1 = 7
EMD3_TORSO_ATTACK_2 = 8
EMD3_TORSO_DROP = 9
EMD3_TORSO_RAISE = 10
EMD3_TORSO_STAND_1 = 11
EMD3_TORSO_STAND_2 = 12
EMD3_LEGS_WALK_CROUCH = 13
EMD3_LEGS_WALK = 14
EMD3_LEGS_RUN = 15
EMD3_LEGS_BACK = 16
EMD3_LEGS_SWIM = 17
EMD3_LEGS_JUMP_1 = 18
EMD3_LEGS_LAND_1 = 19
EMD3_LEGS_JUMP_2 = 20
EMD3_LEGS_LAND_2 = 21
EMD3_LEGS_IDLE = 22
EMD3_LEGS_IDLE_CROUCH = 23
EMD3_LEGS_TURN = 24
EMD3_ANIMATION_COUNT = 25

EMF_WIREFRAME = 0x1
EMF_POINTCLOUD = 0x2
EMF_GOURAUD_SHADING = 0x4
EMF_LIGHTING = 0x8
EMF_ZBUFFER = 0x10
EMF_ZWRITE_ENABLE = 0x20
EMF_BACK_FACE_CULLING = 0x40
EMF_FRONT_FACE_CULLING = 0x80
EMF_BILINEAR_FILTER = 0x100
EMF_TRILINEAR_FILTER = 0x200
EMF_ANISOTROPIC_FILTER = 0x400
EMF_FOG_ENABLE = 0x800
EMF_NORMALIZE_NORMALS = 0x1000
EMF_TEXTURE_WRAP = 0x2000
EMF_ANTI_ALIASING = 0x4000
EMF_COLOR_MASK = 0x8000
EMF_COLOR_MATERIAL = 0x10000

E_MODULATE_FUNC = 0
EMFN_MODULATE_1X = 1
EMFN_MODULATE_2X = 2
EMFN_MODULATE_4X = 4

EMOUSE_INPUT_EVENT = 0
EMIE_LMOUSE_PRESSED_DOWN = 0
EMIE_RMOUSE_PRESSED_DOWN = 1
EMIE_MMOUSE_PRESSED_DOWN = 2
EMIE_LMOUSE_LEFT_UP = 3
EMIE_RMOUSE_LEFT_UP = 4
EMIE_MMOUSE_LEFT_UP = 5
EMIE_MOUSE_MOVED = 6
EMIE_MOUSE_WHEEL = 7
EMIE_LMOUSE_DOUBLE_CLICK = 8
EMIE_RMOUSE_DOUBLE_CLICK = 9
EMIE_MMOUSE_DOUBLE_CLICK = 10
EMIE_LMOUSE_TRIPLE_CLICK = 11
EMIE_RMOUSE_TRIPLE_CLICK = 12
EMIE_MMOUSE_TRIPLE_CLICK = 13
EMIE_COUNT = 14

EMT_SOLID = 0
EMT_SOLID_2_LAYER = 1
EMT_LIGHTMAP = 2
EMT_LIGHTMAP_ADD = 3
EMT_LIGHTMAP_M2 = 4
EMT_LIGHTMAP_M4 = 5
EMT_LIGHTMAP_LIGHTING = 6
EMT_LIGHTMAP_LIGHTING_M2 = 7
EMT_LIGHTMAP_LIGHTING_M4 = 8
EMT_DETAIL_MAP = 9
EMT_SPHERE_MAP = 10
EMT_REFLECTION_2_LAYER = 11
EMT_TRANSPARENT_ADD_COLOR = 12
EMT_TRANSPARENT_ALPHA_CHANNEL = 13
EMT_TRANSPARENT_ALPHA_CHANNEL_REF = 14
EMT_TRANSPARENT_VERTEX_ALPHA = 15
EMT_TRANSPARENT_REFLECTION_2_LAYER = 16
EMT_NORMAL_MAP_SOLID = 17
EMT_NORMAL_MAP_TRANSPARENT_ADD_COLOR = 18
EMT_NORMAL_MAP_TRANSPARENT_VERTEX_ALPHA = 19
EMT_PARALLAX_MAP_SOLID = 20
EMT_PARALLAX_MAP_TRANSPARENT_ADD_COLOR = 21
EMT_PARALLAX_MAP_TRANSPARENT_VERTEX_ALPHA = 22
EMT_ONETEXTURE_BLEND = 23
EMT_FORCE_32BIT = 0x7fffffff

E_PARTICLE_AFFECTOR_TYPE = 0
EPAT_NONE = E_PARTICLE_AFFECTOR_TYPE
EPAT_ATTRACT = 1
EPAT_FADE_OUT = 2
EPAT_GRAVITY = 3
EPAT_ROTATE = 4
EPAT_SCALE = 5
EPAT_COUNT = 6

E_PARTICLE_EMITTER_TYPE = 0
EPET_POINT = E_PARTICLE_EMITTER_TYPE
EPET_ANIMATED_MESH = 1
EPET_BOX = 2
EPET_CYLINDER = 3
EPET_MESH = 4
EPET_RING = 5
EPET_SPHERE = 6
EPET_COUNT = 7

EPT_POINTS = 0
EPT_LINE_STRIP = 1
EPT_LINE_LOOP = 2
EPT_LINES = 3
EPT_TRIANGLE_STRIP = 4
EPT_TRIANGLE_FAN = 5
EPT_TRIANGLES = 6
EPT_QUAD_STRIP = 7
EPT_QUADS = 8
EPT_POLYGON = 9
EPT_POINT_SPRITES = 10

eQ3ModifierFunction = 0
TCMOD				= 0
DEFORMVERTEXES		= 1
RGBGEN				= 2
TCGEN				= 3
MAP					= 4
ALPHAGEN			= 5
FUNCTION2			= 0x10
SCROLL				= FUNCTION2 + 1
SCALE				= FUNCTION2 + 2
ROTATE				= FUNCTION2 + 3
STRETCH				= FUNCTION2 + 4
TURBULENCE			= FUNCTION2 + 5
WAVE				= FUNCTION2 + 6
IDENTITY			= FUNCTION2 + 7
VERTEX				= FUNCTION2 + 8
TEXTURE				= FUNCTION2 + 9
LIGHTMAP			= FUNCTION2 + 10
ENVIRONMENT			= FUNCTION2 + 11
DOLLAR_LIGHTMAP		= FUNCTION2 + 12
BULGE				= FUNCTION2 + 13
AUTOSPRITE			= FUNCTION2 + 14
AUTOSPRITE2			= FUNCTION2 + 15
TRANSFORM			= FUNCTION2 + 16
EXACTVERTEX			= FUNCTION2 + 17
CONSTANT			= FUNCTION2 + 18
LIGHTINGSPECULAR	= FUNCTION2 + 19
MOVE				= FUNCTION2 + 20
NORMAL				= FUNCTION2 + 21
IDENTITYLIGHTING	= FUNCTION2 + 22
WAVE_MODIFIER_FUNCTION	= 0x30
SINUS				= WAVE_MODIFIER_FUNCTION + 1
COSINUS				= WAVE_MODIFIER_FUNCTION + 2
SQUARE				= WAVE_MODIFIER_FUNCTION + 3
TRIANGLE			= WAVE_MODIFIER_FUNCTION + 4
SAWTOOTH			= WAVE_MODIFIER_FUNCTION + 5
SAWTOOTH_INVERSE	= WAVE_MODIFIER_FUNCTION + 6
NOISE				= WAVE_MODIFIER_FUNCTION + 7
UNKNOWN				= -2

#E_RENDER_TARGET
ERT_FRAME_BUFFER = 0
ERT_RENDER_TEXTURE = 1
ERT_MULTI_RENDER_TEXTURES = 2
ERT_STEREO_LEFT_BUFFER = 3
ERT_STEREO_RIGHT_BUFFER = 4
ERT_STEREO_BOTH_BUFFERS = 5
ERT_AUX_BUFFER0 = 6
ERT_AUX_BUFFER1 = 7
ERT_AUX_BUFFER2 = 8
ERT_AUX_BUFFER3 = 9
ERT_AUX_BUFFER4 = 10

ESCENE_NODE_ANIMATOR_TYPE = 0
ESNAT_FLY_CIRCLE = 0
ESNAT_FLY_STRAIGHT = 1
ESNAT_FOLLOW_SPLINE = 2
ESNAT_ROTATION = 3
ESNAT_TEXTURE = 4
ESNAT_DELETION = 5
ESNAT_COLLISION_RESPONSE = 6
ESNAT_CAMERA_FPS = 7
ESNAT_CAMERA_MAYA = 8
ESNAT_COUNT = 9
ESNAT_UNKNOWN = 10
ESNAT_FORCE_32_BIT = 0x7fffffff

ESNRP_NONE = 0
ESNRP_CAMERA = 1
ESNRP_LIGHT = 2
ESNRP_SKY_BOX = 4
ESNRP_AUTOMATIC = 24
ESNRP_SOLID = 8
ESNRP_TRANSPARENT = 16
ESNRP_TRANSPARENT_EFFECT = 32
ESNRP_SHADOW = 64

ESNT_CUBE = ctypes.c_int.in_dll(c_module, '_ESNT_CUBE').value
ESNT_SPHERE = ctypes.c_int.in_dll(c_module, '_ESNT_SPHERE').value
ESNT_TEXT = ctypes.c_int.in_dll(c_module, '_ESNT_TEXT').value
ESNT_WATER_SURFACE = ctypes.c_int.in_dll(c_module, '_ESNT_WATER_SURFACE').value
ESNT_TERRAIN = ctypes.c_int.in_dll(c_module, '_ESNT_TERRAIN').value
ESNT_SKY_BOX = ctypes.c_int.in_dll(c_module, '_ESNT_SKY_BOX').value
ESNT_SKY_DOME = ctypes.c_int.in_dll(c_module, '_ESNT_SKY_DOME').value
ESNT_SHADOW_VOLUME = ctypes.c_int.in_dll(c_module, '_ESNT_SHADOW_VOLUME').value
ESNT_OCTREE = ctypes.c_int.in_dll(c_module, '_ESNT_OCTREE').value
ESNT_MESH = ctypes.c_int.in_dll(c_module, '_ESNT_MESH').value
ESNT_LIGHT = ctypes.c_int.in_dll(c_module, '_ESNT_LIGHT').value
ESNT_EMPTY = ctypes.c_int.in_dll(c_module, '_ESNT_EMPTY').value
ESNT_DUMMY_TRANSFORMATION = ctypes.c_int.in_dll(c_module, '_ESNT_DUMMY_TRANSFORMATION').value
ESNT_CAMERA = ctypes.c_int.in_dll(c_module, '_ESNT_CAMERA').value
ESNT_BILLBOARD = ctypes.c_int.in_dll(c_module, '_ESNT_BILLBOARD').value
ESNT_ANIMATED_MESH = ctypes.c_int.in_dll(c_module, '_ESNT_ANIMATED_MESH').value
ESNT_PARTICLE_SYSTEM = ctypes.c_int.in_dll(c_module, '_ESNT_PARTICLE_SYSTEM').value
ESNT_Q3SHADER_SCENE_NODE = ctypes.c_int.in_dll(c_module, '_ESNT_Q3SHADER_SCENE_NODE').value
ESNT_MD3_SCENE_NODE = ctypes.c_int.in_dll(c_module, '_ESNT_MD3_SCENE_NODE').value
ESNT_VOLUME_LIGHT = ctypes.c_int.in_dll(c_module, '_ESNT_VOLUME_LIGHT').value
ESNT_CAMERA_MAYA = ctypes.c_int.in_dll(c_module, '_ESNT_CAMERA_MAYA').value
ESNT_CAMERA_FPS = ctypes.c_int.in_dll(c_module, '_ESNT_CAMERA_FPS').value
ESNT_UNKNOWN = ctypes.c_int.in_dll(c_module, '_ESNT_UNKNOWN').value
ESNT_ANY = ctypes.c_int.in_dll(c_module, '_ESNT_ANY').value

ETC_REPEAT = 0
ETC_CLAMP = 1
ETC_CLAMP_TO_EDGE = 2
ETC_CLAMP_TO_BORDER = 3
ETC_MIRROR = 4

ETCF_ALWAYS_16_BIT = 0x00000001
ETCF_ALWAYS_32_BIT = 0x00000002
ETCF_OPTIMIZED_FOR_QUALITY = 0x00000004
ETCF_OPTIMIZED_FOR_SPEED = 0x00000008
ETCF_CREATE_MIP_MAPS = 0x00000010
ETCF_NO_ALPHA_CHANNEL = 0x00000020
ETCF_ALLOW_NON_POWER_2 = 0x00000040
ETCF_FORCE_32_BIT_DO_NOT_USE = 0x7fffffff

ETF_ASCII = 0
ETF_UTF8 = 1
ETF_UTF16_BE = 2
ETF_UTF16_LE = 3
ETF_UTF32_BE = 4
ETF_UTF32_LE = 5

E_TEXTURE_LOCK_MODE = 0
ETLM_READ_WRITE = 0
ETLM_READ_ONLY = 1
ETLM_WRITE_ONLY = 2

ETPS_9 = 9
ETPS_17 = 17
ETPS_33 = 33
ETPS_65 = 65
ETPS_129 = 129

E_TRANSFORMATION_STATE = 0
ETS_VIEW = E_TRANSFORMATION_STATE
ETS_WORLD = 1
ETS_PROJECTION = 2
ETS_TEXTURE_0 = 3
ETS_TEXTURE_1 = 4
ETS_TEXTURE_2 = 5
ETS_TEXTURE_3 = 6
ETS_TEXTURE_4 = 7
ETS_TEXTURE_5 = 8
ETS_TEXTURE_6 = 9
ETS_TEXTURE_7 = 10
ETS_COUNT = 11

#~ ETS_VIEW = 0
#~ ETS_PROJECTION = 1
ETS_COUNT_FRUSTUM = 2

EVDF_RENDER_TO_TARGET = 0
EVDF_HARDWARE_TL = 1
EVDF_MULTITEXTURE = 2
EVDF_BILINEAR_FILTER = 3
EVDF_MIP_MAP = 4
EVDF_MIP_MAP_AUTO_UPDATE = 5
EVDF_STENCIL_BUFFER = 6
EVDF_VERTEX_SHADER_1_1 = 7
EVDF_VERTEX_SHADER_2_0 = 8
EVDF_VERTEX_SHADER_3_0 = 9
EVDF_PIXEL_SHADER_1_1 = 10
EVDF_PIXEL_SHADER_1_2 = 11
EVDF_PIXEL_SHADER_1_3 = 12
EVDF_PIXEL_SHADER_1_4 = 13
EVDF_PIXEL_SHADER_2_0 = 14
EVDF_PIXEL_SHADER_3_0 = 15
EVDF_ARB_VERTEX_PROGRAM_1 = 16
EVDF_ARB_FRAGMENT_PROGRAM_1 = 17
EVDF_ARB_GLSL = 18
EVDF_HLSL = 19
EVDF_TEXTURE_NSQUARE = 20
EVDF_TEXTURE_NPOT = 21
EVDF_FRAMEBUFFER_OBJECT = 22
EVDF_VERTEX_BUFFER_OBJECT = 23
EVDF_ALPHA_TO_COVERAGE = 24
EVDF_COLOR_MASK = 25
EVDF_COUNT = 26

E_VERTEX_TYPE = 0
EVT_STANDARD = 0
EVT_2TCOORDS = 1
EVT_TANGENTS = 2

EXN_NONE = 0
EXN_ELEMENT = 1
EXN_ELEMENT_END = 2
EXN_TEXT = 3
EXN_COMMENT = 4
EXN_CDATA = 5
EXN_UNKNOWN = 6

EFileSystemType = 0
FILESYSTEM_NATIVE = 0
FILESYSTEM_VIRTUAL = 1

ISREL3D_FRONT = 0
ISREL3D_BACK = 1
ISREL3D_PLANAR = 2
ISREL3D_SPANNING = 3
ISREL3D_CLIPPED = 4

KEY_LBUTTON          = 0x01# Left mouse button
KEY_RBUTTON          = 0x02# Right mouse button
KEY_CANCEL           = 0x03# Control-break processing
KEY_MBUTTON          = 0x04# Middle mouse button (three-button mouse)
KEY_XBUTTON1         = 0x05# Windows 2000/XP: X1 mouse button
KEY_XBUTTON2         = 0x06# Windows 2000/XP: X2 mouse button
KEY_BACK             = 0x08# BACKSPACE key
KEY_TAB              = 0x09# TAB key
KEY_CLEAR            = 0x0C# CLEAR key
KEY_RETURN           = 0x0D# ENTER key
KEY_SHIFT            = 0x10# SHIFT key
KEY_CONTROL          = 0x11# CTRL key
KEY_MENU             = 0x12# ALT key
KEY_PAUSE            = 0x13# PAUSE key
KEY_CAPITAL          = 0x14# CAPS LOCK key
KEY_KANA             = 0x15# IME Kana mode
KEY_HANGUEL          = 0x15# IME Hanguel mode (maintained for compatibility use KEY_HANGUL)
KEY_HANGUL           = 0x15# IME Hangul mode
KEY_JUNJA            = 0x17# IME Junja mode
KEY_FINAL            = 0x18# IME final mode
KEY_HANJA            = 0x19# IME Hanja mode
KEY_KANJI            = 0x19# IME Kanji mode
KEY_ESCAPE           = 0x1B# ESC key
KEY_CONVERT          = 0x1C# IME convert
KEY_NONCONVERT       = 0x1D# IME nonconvert
KEY_ACCEPT           = 0x1E# IME accept
KEY_MODECHANGE       = 0x1F# IME mode change request
KEY_SPACE            = 0x20# SPACEBAR
KEY_PRIOR            = 0x21# PAGE UP key
KEY_NEXT             = 0x22# PAGE DOWN key
KEY_END              = 0x23# END key
KEY_HOME             = 0x24# HOME key
KEY_LEFT             = 0x25# LEFT ARROW key
KEY_UP               = 0x26# UP ARROW key
KEY_RIGHT            = 0x27# RIGHT ARROW key
KEY_DOWN             = 0x28# DOWN ARROW key
KEY_SELECT           = 0x29# SELECT key
KEY_PRINT            = 0x2A# PRINT key
KEY_EXECUT           = 0x2B# EXECUTE key
KEY_SNAPSHOT         = 0x2C# PRINT SCREEN key
KEY_INSERT           = 0x2D# INS key
KEY_DELETE           = 0x2E# DEL key
KEY_HELP             = 0x2F# HELP key
KEY_KEY_0            = 0x30# 0 key
KEY_KEY_1            = 0x31# 1 key
KEY_KEY_2            = 0x32# 2 key
KEY_KEY_3            = 0x33# 3 key
KEY_KEY_4            = 0x34# 4 key
KEY_KEY_5            = 0x35# 5 key
KEY_KEY_6            = 0x36# 6 key
KEY_KEY_7            = 0x37# 7 key
KEY_KEY_8            = 0x38# 8 key
KEY_KEY_9            = 0x39# 9 key
KEY_KEY_A            = 0x41# A key
KEY_KEY_B            = 0x42# B key
KEY_KEY_C            = 0x43# C key
KEY_KEY_D            = 0x44# D key
KEY_KEY_E            = 0x45# E key
KEY_KEY_F            = 0x46# F key
KEY_KEY_G            = 0x47# G key
KEY_KEY_H            = 0x48# H key
KEY_KEY_I            = 0x49# I key
KEY_KEY_J            = 0x4A# J key
KEY_KEY_K            = 0x4B# K key
KEY_KEY_L            = 0x4C# L key
KEY_KEY_M            = 0x4D# M key
KEY_KEY_N            = 0x4E# N key
KEY_KEY_O            = 0x4F# O key
KEY_KEY_P            = 0x50# P key
KEY_KEY_Q            = 0x51# Q key
KEY_KEY_R            = 0x52# R key
KEY_KEY_S            = 0x53# S key
KEY_KEY_T            = 0x54# T key
KEY_KEY_U            = 0x55# U key
KEY_KEY_V            = 0x56# V key
KEY_KEY_W            = 0x57# W key
KEY_KEY_X            = 0x58# X key
KEY_KEY_Y            = 0x59# Y key
KEY_KEY_Z            = 0x5A# Z key
KEY_LWIN             = 0x5B# Left Windows key (Microsoft Natural keyboard)
KEY_RWIN             = 0x5C# Right Windows key (Natural keyboard)
KEY_APPS             = 0x5D# Applications key (Natural keyboard)
KEY_SLEEP            = 0x5F# Computer Sleep key
KEY_NUMPAD0          = 0x60# Numeric keypad 0 key
KEY_NUMPAD1          = 0x61# Numeric keypad 1 key
KEY_NUMPAD2          = 0x62# Numeric keypad 2 key
KEY_NUMPAD3          = 0x63# Numeric keypad 3 key
KEY_NUMPAD4          = 0x64# Numeric keypad 4 key
KEY_NUMPAD5          = 0x65# Numeric keypad 5 key
KEY_NUMPAD6          = 0x66# Numeric keypad 6 key
KEY_NUMPAD7          = 0x67# Numeric keypad 7 key
KEY_NUMPAD8          = 0x68# Numeric keypad 8 key
KEY_NUMPAD9          = 0x69# Numeric keypad 9 key
KEY_MULTIPLY         = 0x6A# Multiply key
KEY_ADD              = 0x6B# Add key
KEY_SEPARATOR        = 0x6C# Separator key
KEY_SUBTRACT         = 0x6D# Subtract key
KEY_DECIMAL          = 0x6E# Decimal key
KEY_DIVIDE           = 0x6F# Divide key
KEY_F1               = 0x70# F1 key
KEY_F2               = 0x71# F2 key
KEY_F3               = 0x72# F3 key
KEY_F4               = 0x73# F4 key
KEY_F5               = 0x74# F5 key
KEY_F6               = 0x75# F6 key
KEY_F7               = 0x76# F7 key
KEY_F8               = 0x77# F8 key
KEY_F9               = 0x78# F9 key
KEY_F10              = 0x79# F10 key
KEY_F11              = 0x7A# F11 key
KEY_F12              = 0x7B# F12 key
KEY_F13              = 0x7C# F13 key
KEY_F14              = 0x7D# F14 key
KEY_F15              = 0x7E# F15 key
KEY_F16              = 0x7F# F16 key
KEY_F17              = 0x80# F17 key
KEY_F18              = 0x81# F18 key
KEY_F19              = 0x82# F19 key
KEY_F20              = 0x83# F20 key
KEY_F21              = 0x84# F21 key
KEY_F22              = 0x85# F22 key
KEY_F23              = 0x86# F23 key
KEY_F24              = 0x87# F24 key
KEY_NUMLOCK          = 0x90# NUM LOCK key
KEY_SCROLL           = 0x91# SCROLL LOCK key
KEY_LSHIFT           = 0xA0# Left SHIFT key
KEY_RSHIFT           = 0xA1# Right SHIFT key
KEY_LCONTROL         = 0xA2# Left CONTROL key
KEY_RCONTROL         = 0xA3# Right CONTROL key
KEY_LMENU            = 0xA4# Left MENU key
KEY_RMENU            = 0xA5# Right MENU key
KEY_PLUS             = 0xBB# Plus Key   (+)
KEY_COMMA            = 0xBC# Comma Key  (,)
KEY_MINUS            = 0xBD# Minus Key  (-)
KEY_PERIOD           = 0xBE# Period Key (.)
KEY_ATTN             = 0xF6# Attn key
KEY_CRSEL            = 0xF7# CrSel key
KEY_EXSEL            = 0xF8# ExSel key
KEY_EREOF            = 0xF9# Erase EOF key
KEY_PLAY             = 0xFA# Play key
KEY_ZOOM             = 0xFB# Zoom key
KEY_PA1              = 0xFD# PA1 key
KEY_OEM_CLEAR        = 0xFE# Clear key
KEY_KEY_CODES_COUNT  = 0xFF# this is not a key, but the amount of keycodes there are.

MATERIAL_MAX_TEXTURES = ctypes.c_uint.in_dll(c_module, '_MATERIAL_MAX_TEXTURES').value

POV_HAT_PRESENT = 0
POV_HAT_ABSENT = 1
POV_HAT_UNKNOWN = 2

VF_FAR_PLANE = 0
VF_NEAR_PLANE = 1
VF_LEFT_PLANE = 2
VF_RIGHT_PLANE = 3
VF_BOTTOM_PLANE = 4
VF_TOP_PLANE = 5
VF_PLANE_COUNT = 6

ROUNDING_ERROR_S32 = 0
ROUNDING_ERROR_f32 = 0.000001
ROUNDING_ERROR_f64 = 0.00000001

ALLOW_ZWRITE_ON_TRANSPARENT = "Allow_ZWrite_On_Transparent"
CSM_TEXTURE_PATH = "CSM_TexturePath"
LMTS_TEXTURE_PATH = "LMTS_TexturePath"
MY3D_TEXTURE_PATH = "MY3D_TexturePath"
COLLADA_CREATE_SCENE_INSTANCES = "COLLADA_CreateSceneInstances"
DMF_TEXTURE_PATH = "DMF_TexturePath"
DMF_IGNORE_MATERIALS_DIRS = "DMF_IgnoreMaterialsDir"
DMF_ALPHA_CHANNEL_REF = "DMF_AlphaRef"
DMF_FLIP_ALPHA_TEXTURES = "DMF_FlipAlpha"
OBJ_TEXTURE_PATH = "OBJ_TexturePath"
OBJ_LOADER_IGNORE_GROUPS = "OBJ_IgnoreGroups"
OBJ_LOADER_IGNORE_MATERIAL_FILES = "OBJ_IgnoreMaterialFiles"
B3D_LOADER_IGNORE_MIPMAP_FLAG = "B3D_IgnoreMipmapFlag"
B3D_TEXTURE_PATH = "B3D_TexturePath"
IRR_SCENE_MANAGER_IS_EDITOR = "IRR_Editor"
DEBUG_NORMAL_LENGTH = "DEBUG_Normal_Length"
DEBUG_NORMAL_COLOR = "DEBUG_Normal_Color"

#================= SKeyMap
# extended methods for SKeyMap
SKeyMap_ctor = func_type(ctypes.c_void_p, ctypes.c_int)(('SKeyMap_ctor', c_module))
SKeyMap_delete = func_type(None, ctypes.c_void_p)(('SKeyMap_delete', c_module))
SKeyMap_set = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('SKeyMap_set', c_module))
class SKeyMap:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.length = 0
		if len(args) > 0:
			self.length = args[0]
			self.c_pointer = SKeyMap_ctor(self.length)
	def __del__(self):
		if self.c_pointer:
			try:
				SKeyMap_delete(self.c_pointer)
			except:
				pass
	def set(self, index, action, key_code):
		SKeyMap_set(self.c_pointer, index, action, key_code)

class SAttributeReadWriteOptions(ctypes.Structure):
	_fields_ = [('Flags', ctypes.c_int),
				('Filename', ctypes.c_char_p)
				]

NUMBER_OF_BUTTONS = 32
AXIS_X = 0
AXIS_Y = 1
AXIS_Z = 2
AXIS_R = 3
AXIS_U = 4
AXIS_V = 5
NUMBER_OF_AXES = 6

class SLight(ctypes.Structure):
	_fields_ = [('AmbientColor', ctypes.c_void_p),# SColorf
				('DiffuseColor', ctypes.c_void_p),# SColorf
				('SpecularColor', ctypes.c_void_p),# SColorf
				('Attenuation', ctypes.c_void_p),# vector3df
				('OuterCone', ctypes.c_float),
				('InnerCone', ctypes.c_float),
				('Falloff', ctypes.c_float),
				('Position', ctypes.c_void_p),# vector3df
				('Direction', ctypes.c_void_p),# vector3df
				('Radius', ctypes.c_float),
				('Type', ctypes.c_int),
				('CastShadows', ctypes.c_bool)
				]

#delete_pointer = func_type(None, ctypes.c_void_p)(('delete_pointer', c_module))
#delete_struct_pointer = func_type(None, ctypes.c_void_p)(('delete_struct_pointer', c_module))

tool_randrange = func_type(ctypes.c_int, ctypes.c_int, ctypes.c_int)(('tool_randrange', c_module))
tool_texture_generator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)(('tool_texture_generator', c_module))
tool_getAsVector3df = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('tool_getAsVector3df', c_module))
tool_getAsFloat = func_type(ctypes.c_float, ctypes.c_char_p, ctypes.c_void_p)(('tool_getAsFloat', c_module))
#~ tool_getTextures = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('tool_getTextures', c_module))
tool_getTextures = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('tool_getTextures', c_module))

# tool_char_to_wchar mainly used with Blitz3D wrapper
BUILD_WITH_CHAR_CONVERSION_FUNCTIONS = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_CHAR_CONVERSION_FUNCTIONS').value
if BUILD_WITH_CHAR_CONVERSION_FUNCTIONS:
	tool_char_to_wchar = func_type(ctypes.c_wchar_p, ctypes.c_char_p)(('tool_char_to_wchar', c_module))

# stream functions
BUILD_WITH_STREAM_FUNCTIONS = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_STREAM_FUNCTIONS').value
if BUILD_WITH_STREAM_FUNCTIONS:
	tool_get_stdin = func_type(ctypes.c_void_p)(('tool_get_stdin', c_module))
	tool_get_stdout = func_type(ctypes.c_void_p)(('tool_get_stdout', c_module))
	tool_redirect_stdout_to_file = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('tool_redirect_stdout_to_file', c_module))
	tool_redirect_stderr_to_file = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('tool_redirect_stderr_to_file', c_module))
	tool_close_stream = func_type(ctypes.c_int, ctypes.c_void_p)(('tool_close_stream', c_module))
	tool_close_streams = func_type(ctypes.c_int)(('tool_close_streams', c_module))

# agg functions
BUILD_WITH_AGG = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_AGG').value
if BUILD_WITH_AGG:
	tool_texture_from_svg = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint)(('tool_texture_from_svg', c_module))
	tool_texture_from_test_vectors = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint)(('tool_texture_from_test_vectors', c_module))
	agg_svg_path = func_type(ctypes.c_void_p, fschar_t)(('agg_svg_path', c_module))
	agg_svg_path_from_string = func_type(ctypes.c_void_p, ctypes.c_char_p)(('agg_svg_path_from_string', c_module))
	agg_svg_IImage = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_uint, ctypes.c_int)(('agg_svg_IImage', c_module))
	agg_svg_ITexture = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int, ctypes.c_uint, ctypes.c_int)(('agg_svg_ITexture', c_module))

	#=== agg_svg_loader
	agg_svg_loader_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('agg_svg_loader_ctor', c_module))

	# svg_viewer helper example
	svg_viewer_ctor = func_type(ctypes.c_void_p)(('svg_viewer_ctor', c_module))
	svg_viewer_set_video_driver = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('svg_viewer_set_video_driver', c_module))
	svg_viewer_scale = func_type(None, ctypes.c_void_p, ctypes.c_double)(('svg_viewer_scale', c_module))
	svg_viewer_get_texture = func_type(ctypes.c_void_p, ctypes.c_void_p)(('svg_viewer_get_texture', c_module))

# svg_agg_image
BUILD_WITH_IRR_SVG_AGG = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_IRR_SVG_AGG').value
if BUILD_WITH_IRR_SVG_AGG:
	svg_agg_image_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_uint, ctypes.c_int, ctypes.c_int)(('svg_agg_image_ctor1', c_module))
	svg_agg_image_parse = func_type(None, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_uint, ctypes.c_int, ctypes.c_int)(('svg_agg_image_parse', c_module))
	svg_agg_image_scale = func_type(None, ctypes.c_void_p, ctypes.c_double, ctypes.c_double)(('svg_agg_image_scale', c_module))
	svg_agg_image_scale_rateably = func_type(None, ctypes.c_void_p, ctypes.c_double)(('svg_agg_image_scale_rateably', c_module))
	#~ svg_agg_image_render = func_type(ctypes.c_void_p, ctypes.c_void_p)(('svg_agg_image_render', c_module))
	svg_agg_image_get_image = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('svg_agg_image_get_image', c_module))
	svg_agg_image_get_texture = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('svg_agg_image_get_texture', c_module))
	#~ svg_agg_image_drop = func_type(ctypes.c_bool, ctypes.c_void_p)(('svg_agg_image_drop', c_module))
	#~ svg_agg_image_get_size = func_type(ctypes.c_void_p, ctypes.c_void_p)(('svg_agg_image_get_size', c_module))
	svg_agg_image_get_width = func_type(ctypes.c_double, ctypes.c_void_p)(('svg_agg_image_get_width', c_module))
	svg_agg_image_get_width_u32 = func_type(ctypes.c_uint, ctypes.c_void_p)(('svg_agg_image_get_width_u32', c_module))
	svg_agg_image_get_height = func_type(ctypes.c_double, ctypes.c_void_p)(('svg_agg_image_get_height', c_module))
	svg_agg_image_get_height_u32 = func_type(ctypes.c_uint, ctypes.c_void_p)(('svg_agg_image_get_height_u32', c_module))

# svg_cairo_image
BUILD_WITH_IRR_SVG_CAIRO = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_IRR_SVG_CAIRO').value
if BUILD_WITH_IRR_SVG_CAIRO:
	CAIRO_ANTIALIAS_DEFAULT = 0
	CAIRO_ANTIALIAS_NONE = 1
	CAIRO_ANTIALIAS_GRAY = 2
	CAIRO_ANTIALIAS_SUBPIXEL = 3

	cairo_version = func_type(ctypes.c_int)(('tool_cairo_version', c_module))
	cairo_version_string = func_type(ctypes.c_char_p)(('tool_cairo_version_string', c_module))

	svg_cairo_image_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double)(('svg_cairo_image_ctor1', c_module))
	svg_cairo_image_parse = func_type(None, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_double, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double)(('svg_cairo_image_parse', c_module))
	svg_cairo_image_scale = func_type(None, ctypes.c_void_p, ctypes.c_double, ctypes.c_double)(('svg_cairo_image_scale', c_module))
	svg_cairo_image_get_image = func_type(ctypes.c_void_p, ctypes.c_void_p)(('svg_cairo_image_get_image', c_module))
	svg_cairo_image_get_texture = func_type(ctypes.c_void_p, ctypes.c_void_p)(('svg_cairo_image_get_texture', c_module))
	svg_cairo_image_get_width = func_type(ctypes.c_double, ctypes.c_void_p)(('svg_cairo_image_get_width', c_module))
	svg_cairo_image_get_width_u32 = func_type(ctypes.c_uint, ctypes.c_void_p)(('svg_cairo_image_get_width_u32', c_module))
	svg_cairo_image_get_height = func_type(ctypes.c_double, ctypes.c_void_p)(('svg_cairo_image_get_height', c_module))
	svg_cairo_image_get_height_u32 = func_type(ctypes.c_uint, ctypes.c_void_p)(('svg_cairo_image_get_height_u32', c_module))

# MainLoop main loop helper example
MainLoop_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('MainLoop_ctor', c_module))
MainLoop_start = func_type(None, ctypes.c_void_p)(('MainLoop_start', c_module))
MainLoop_stop = func_type(None, ctypes.c_void_p)(('MainLoop_stop', c_module))

#class array
array_ctor1 = func_type(ctypes.c_void_p)(('array_ctor1', c_module))
array_ctor2 = func_type(ctypes.c_void_p, ctypes.c_uint)(('array_ctor2', c_module))
array_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('array_ctor3', c_module))
array_delete = func_type(None, ctypes.c_void_p)(('array_delete', c_module))
array_reallocate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('array_reallocate', c_module))
array_setAllocStrategy = func_type(None, ctypes.c_void_p, ctypes.c_int)(('array_setAllocStrategy', c_module))
array_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('array_push_back', c_module))
array_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('array_push_front', c_module))
array_insert = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('array_insert', c_module))
array_clear = func_type(None, ctypes.c_void_p)(('array_clear', c_module))
array_set_pointer = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('array_set_pointer', c_module))
array_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('array_set_free_when_destroyed', c_module))
array_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('array_set_used', c_module))
array_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('array_set', c_module))
array_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('array_operator_eq', c_module))
array_operator_neq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('array_operator_neq', c_module))
array_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('array_get_item', c_module))
array_set_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('array_set_item', c_module))
array_getLast = func_type(ctypes.c_void_p, ctypes.c_void_p)(('array_getLast', c_module))
array_pointer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('array_pointer', c_module))
array_const_pointer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('array_const_pointer', c_module))
array_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('array_size', c_module))
array_allocated_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('array_allocated_size', c_module))
array_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('array_empty', c_module))
array_sort = func_type(None, ctypes.c_void_p)(('array_sort', c_module))
array_binary_search1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('array_binary_search1', c_module))
array_binary_search2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('array_binary_search2', c_module))
array_binary_search_multi = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('array_binary_search_multi', c_module))
array_linear_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('array_linear_search', c_module))
array_linear_reverse_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('array_linear_reverse_search', c_module))
array_erase1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('array_erase1', c_module))
array_erase2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('array_erase2', c_module))
array_set_sorted = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('array_set_sorted', c_module))
array_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('array_swap', c_module))

#================= SJoystickInfo
SJoystickInfo_ctor = func_type(ctypes.c_void_p, ctypes.c_int)(('SJoystickInfo_ctor', c_module))
SJoystickInfo_delete = func_type(None, ctypes.c_void_p)(('SJoystickInfo_delete', c_module))
SJoystickInfo_get_Joystick = func_type(ctypes.c_ubyte, ctypes.c_void_p)(('SJoystickInfo_get_Joystick', c_module))
SJoystickInfo_set_Joystick = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SJoystickInfo_set_Joystick', c_module))
SJoystickInfo_get_Name = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SJoystickInfo_get_Name', c_module))
SJoystickInfo_set_Name = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SJoystickInfo_set_Name', c_module))
SJoystickInfo_get_Buttons = func_type(ctypes.c_uint, ctypes.c_void_p)(('SJoystickInfo_get_Buttons', c_module))
SJoystickInfo_set_Buttons = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SJoystickInfo_set_Buttons', c_module))
SJoystickInfo_get_Axes = func_type(ctypes.c_uint, ctypes.c_void_p)(('SJoystickInfo_get_Axes', c_module))
SJoystickInfo_set_Axes = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SJoystickInfo_set_Axes', c_module))
SJoystickInfo_get_PovHat = func_type(ctypes.c_int, ctypes.c_void_p)(('SJoystickInfo_get_PovHat', c_module))

# functions for class arraySJoystickInfo
arraySJoystickInfo_ctor = func_type(ctypes.c_void_p)(('arraySJoystickInfo_ctor', c_module))
arraySJoystickInfo_delete = func_type(None, ctypes.c_void_p)(('arraySJoystickInfo_delete', c_module))
arraySJoystickInfo_allocated_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('arraySJoystickInfo_allocated_size', c_module))
arraySJoystickInfo_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('arraySJoystickInfo_size', c_module))
arraySJoystickInfo_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('arraySJoystickInfo_set_free_when_destroyed', c_module))
arraySJoystickInfo_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('arraySJoystickInfo_set_used', c_module))
arraySJoystickInfo_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('arraySJoystickInfo_get_item', c_module))
#~ arraySJoystickInfo_get_item = func_type(ctypes.POINTER(SJoystickInfo), ctypes.c_void_p, ctypes.c_uint)(('arraySJoystickInfo_get_item', c_module))

# functions for class CGridSceneNode
BUILD_WITH_GRID_SCENE_NODE = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_GRID_SCENE_NODE').value
if BUILD_WITH_GRID_SCENE_NODE:
	CGridSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_bool)(('CGridSceneNode_ctor', c_module))
	CGridSceneNode_delete = func_type(None, ctypes.c_void_p)(('CGridSceneNode_delete', c_module))
	CGridSceneNode_clone = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_clone', c_module))
	CGridSceneNode_OnRegisterSceneNode = func_type(None, ctypes.c_void_p)(('CGridSceneNode_OnRegisterSceneNode', c_module))
	CGridSceneNode_render = func_type(None, ctypes.c_void_p)(('CGridSceneNode_render', c_module))
	CGridSceneNode_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_getBoundingBox', c_module))
	CGridSceneNode_getMaterialCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('CGridSceneNode_getMaterialCount', c_module))
	CGridSceneNode_getMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('CGridSceneNode_getMaterial', c_module))
	CGridSceneNode_RegenerateGrid = func_type(None, ctypes.c_void_p)(('CGridSceneNode_RegenerateGrid', c_module))
	CGridSceneNode_GetSpacing = func_type(ctypes.c_uint, ctypes.c_void_p)(('CGridSceneNode_GetSpacing', c_module))
	CGridSceneNode_GetSize = func_type(ctypes.c_uint, ctypes.c_void_p)(('CGridSceneNode_GetSize', c_module))
	CGridSceneNode_GetGridColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_GetGridColor', c_module))
	CGridSceneNode_GetAccentlineOffset = func_type(ctypes.c_uint, ctypes.c_void_p)(('CGridSceneNode_GetAccentlineOffset', c_module))
	CGridSceneNode_GetAccentlineColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_GetAccentlineColor', c_module))
	CGridSceneNode_AreAxisLineActive = func_type(ctypes.c_bool, ctypes.c_void_p)(('CGridSceneNode_AreAxisLineActive', c_module))
	CGridSceneNode_GetAxisLineXColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_GetAxisLineXColor', c_module))
	CGridSceneNode_GetAxisLineZColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_GetAxisLineZColor', c_module))
	CGridSceneNode_SetSpacing = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('CGridSceneNode_SetSpacing', c_module))
	CGridSceneNode_SetSize = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('CGridSceneNode_SetSize', c_module))
	CGridSceneNode_SetGridColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_SetGridColor', c_module))
	CGridSceneNode_SetAccentlineOffset = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('CGridSceneNode_SetAccentlineOffset', c_module))
	CGridSceneNode_SetAccentlineColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_SetAccentlineColor', c_module))
	CGridSceneNode_SetAxisLineActive = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('CGridSceneNode_SetAxisLineActive', c_module))
	CGridSceneNode_SetAxisLineXColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_SetAxisLineXColor', c_module))
	CGridSceneNode_SetAxisLineZColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_SetAxisLineZColor', c_module))
	CGridSceneNode_SetMaterial = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGridSceneNode_SetMaterial', c_module))

#class CGUIFileSelector : public IGUIFileOpenDialog
BUILD_WITH_GUI_FILE_SELECTOR = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_GUI_FILE_SELECTOR').value
if BUILD_WITH_GUI_FILE_SELECTOR:
	E_FILESELECTOR_TYPE = 0
	EFST_OPEN_DIALOG = 0#<! For opening files
	EFST_SAVE_DIALOG = 1#<! For saving files
	EFST_NUM_TYPES = 2#<! Not used, just specifies how many possible types there are
	CGUIFileSelector_ctor = func_type(ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('CGUIFileSelector_ctor', c_module))
	CGUIFileSelector_getFileName = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('CGUIFileSelector_getFileName', c_module))
	CGUIFileSelector_delete = func_type(None, ctypes.c_void_p)(('CGUIFileSelector_delete', c_module))
	CGUIFileSelector_getDirectoryName = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGUIFileSelector_getDirectoryName', c_module))
	CGUIFileSelector_getFileFilter = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('CGUIFileSelector_getFileFilter', c_module))
	CGUIFileSelector_getDialogType = func_type(ctypes.c_int, ctypes.c_void_p)(('CGUIFileSelector_getDialogType', c_module))
	CGUIFileSelector_addFileFilter = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_void_p)(('CGUIFileSelector_addFileFilter', c_module))
	CGUIFileSelector_setCustomFileIcon = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGUIFileSelector_setCustomFileIcon', c_module))
	CGUIFileSelector_setCustomDirectoryIcon = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGUIFileSelector_setCustomDirectoryIcon', c_module))
	CGUIFileSelector_setDirectoryChoosable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('CGUIFileSelector_setDirectoryChoosable', c_module))

# functions for Structure class SViewFrustum
SViewFrustum_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_ctor1', c_module))
SViewFrustum_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_ctor2', c_module))
SViewFrustum_transform = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_transform', c_module))
SViewFrustum_getFarLeftUp = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_getFarLeftUp', c_module))
SViewFrustum_getFarLeftDown = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_getFarLeftDown', c_module))
SViewFrustum_getFarRightUp = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_getFarRightUp', c_module))
SViewFrustum_getFarRightDown = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_getFarRightDown', c_module))
SViewFrustum_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_getBoundingBox', c_module))
SViewFrustum_recalculateBoundingBox = func_type(None, ctypes.c_void_p)(('SViewFrustum_recalculateBoundingBox', c_module))
SViewFrustum_setFrom = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_setFrom', c_module))
SViewFrustum_getTransform = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SViewFrustum_getTransform', c_module))
SViewFrustum_clipLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SViewFrustum_clipLine', c_module))

# functions for class IEventReceiver
#~ SEvent_GetEventType = func_type(ctypes.c_int, ctypes.POINTER(SEvent))(('SEvent_GetEventType', c_module))
SEvent_GetEventType = func_type(ctypes.c_int, ctypes.c_void_p)(('SEvent_GetEventType', c_module))

#~ SEvent_GetSGUIEvent = func_type(ctypes.POINTER(SGUIEvent), ctypes.POINTER(SEvent))(('SEvent_GetSGUIEvent', c_module))
#~ SGUIEvent_GetCaller = func_type(ctypes.c_void_p, ctypes.POINTER(SGUIEvent))(('SGUIEvent_GetCaller', c_module))
#~ SGUIEvent_GetElement = func_type(ctypes.c_void_p, ctypes.POINTER(SGUIEvent))(('SGUIEvent_GetElement', c_module))
#~ SGUIEvent_GetEventType = func_type(ctypes.c_int, ctypes.POINTER(SGUIEvent))(('SGUIEvent_GetEventType', c_module))
SEvent_GetSGUIEvent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSGUIEvent', c_module))
SGUIEvent_GetCaller = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SGUIEvent_GetCaller', c_module))
SGUIEvent_GetElement = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SGUIEvent_GetElement', c_module))
SGUIEvent_GetEventType = func_type(ctypes.c_int, ctypes.c_void_p)(('SGUIEvent_GetEventType', c_module))

#~ SEvent_GetSMouseInput = func_type(ctypes.POINTER(SMouseInput), ctypes.POINTER(SEvent))(('SEvent_GetSMouseInput', c_module))
#~ SMouseInput_GetX = func_type(ctypes.c_int, ctypes.POINTER(SMouseInput))(('SMouseInput_GetX', c_module))
#~ SMouseInput_GetY = func_type(ctypes.c_int, ctypes.POINTER(SMouseInput))(('SMouseInput_GetY', c_module))
#~ SMouseInput_GetWheel = func_type(ctypes.c_float, ctypes.POINTER(SMouseInput))(('SMouseInput_GetWheel', c_module))
#~ SMouseInput_GetShift = func_type(ctypes.c_bool, ctypes.POINTER(SMouseInput))(('SMouseInput_GetShift', c_module))
#~ SMouseInput_GetControl = func_type(ctypes.c_bool, ctypes.POINTER(SMouseInput))(('SMouseInput_GetControl', c_module))
#~ SMouseInput_GetButtonStates = func_type(ctypes.c_uint, ctypes.POINTER(SMouseInput))(('SMouseInput_GetButtonStates', c_module))
#~ SMouseInput_isLeftPressed = func_type(ctypes.c_bool, ctypes.POINTER(SMouseInput))(('SMouseInput_isLeftPressed', c_module))
#~ SMouseInput_isRightPressed = func_type(ctypes.c_bool, ctypes.POINTER(SMouseInput))(('SMouseInput_isRightPressed', c_module))
#~ SMouseInput_isMiddlePressed = func_type(ctypes.c_bool, ctypes.POINTER(SMouseInput))(('SMouseInput_isMiddlePressed', c_module))
#~ SMouseInput_GetEventType = func_type(ctypes.c_int, ctypes.POINTER(SMouseInput))(('SMouseInput_GetEventType', c_module))
SEvent_GetSMouseInput = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSMouseInput', c_module))
SMouseInput_GetX = func_type(ctypes.c_int, ctypes.c_void_p)(('SMouseInput_GetX', c_module))
SMouseInput_GetY = func_type(ctypes.c_int, ctypes.c_void_p)(('SMouseInput_GetY', c_module))
SMouseInput_GetWheel = func_type(ctypes.c_float, ctypes.c_void_p)(('SMouseInput_GetWheel', c_module))
SMouseInput_GetShift = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMouseInput_GetShift', c_module))
SMouseInput_GetControl = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMouseInput_GetControl', c_module))
SMouseInput_GetButtonStates = func_type(ctypes.c_uint, ctypes.c_void_p)(('SMouseInput_GetButtonStates', c_module))
SMouseInput_isLeftPressed = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMouseInput_isLeftPressed', c_module))
SMouseInput_isRightPressed = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMouseInput_isRightPressed', c_module))
SMouseInput_isMiddlePressed = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMouseInput_isMiddlePressed', c_module))
SMouseInput_GetEventType = func_type(ctypes.c_int, ctypes.c_void_p)(('SMouseInput_GetEventType', c_module))

#~ SEvent_GetSKeyInput = func_type(ctypes.POINTER(SKeyInput), ctypes.POINTER(SEvent))(('SEvent_GetSKeyInput', c_module))
#~ SKeyInput_GetChar = func_type(ctypes.c_wchar, ctypes.POINTER(SKeyInput))(('SKeyInput_GetChar', c_module))
#~ SKeyInput_GetKey = func_type(ctypes.c_int, ctypes.POINTER(SKeyInput))(('SKeyInput_GetKey', c_module))
#~ SKeyInput_GetPressedDown = func_type(ctypes.c_bool, ctypes.POINTER(SKeyInput))(('SKeyInput_GetPressedDown', c_module))
#~ SKeyInput_GetShift = func_type(ctypes.c_bool, ctypes.POINTER(SKeyInput))(('SKeyInput_GetShift', c_module))
#~ SKeyInput_GetControl = func_type(ctypes.c_bool, ctypes.POINTER(SKeyInput))(('SKeyInput_GetControl', c_module))
SEvent_GetSKeyInput = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSKeyInput', c_module))
SKeyInput_GetChar = func_type(ctypes.c_wchar, ctypes.c_void_p)(('SKeyInput_GetChar', c_module))
SKeyInput_GetKey = func_type(ctypes.c_int, ctypes.c_void_p)(('SKeyInput_GetKey', c_module))
SKeyInput_GetPressedDown = func_type(ctypes.c_bool, ctypes.c_void_p)(('SKeyInput_GetPressedDown', c_module))
SKeyInput_GetShift = func_type(ctypes.c_bool, ctypes.c_void_p)(('SKeyInput_GetShift', c_module))
SKeyInput_GetControl = func_type(ctypes.c_bool, ctypes.c_void_p)(('SKeyInput_GetControl', c_module))

#~ SEvent_GetSJoystickEvent = func_type(ctypes.POINTER(SJoystickEvent), ctypes.POINTER(SEvent))(('SEvent_GetSJoystickEvent', c_module))
#~ SJoystickEvent_GetButtonStates = func_type(ctypes.c_uint, ctypes.POINTER(SJoystickEvent))(('SJoystickEvent_GetButtonStates', c_module))
#~ SJoystickEvent_GetAxis = func_type(ctypes.c_short * NUMBER_OF_AXES, ctypes.POINTER(SJoystickEvent))(('SJoystickEvent_GetAxis', c_module))
#~ SJoystickEvent_GetPOV = func_type(ctypes.c_ushort, ctypes.POINTER(SJoystickEvent))(('SJoystickEvent_GetPOV', c_module))
#~ SJoystickEvent_GetJoystick = func_type(ctypes.c_ubyte, ctypes.POINTER(SJoystickEvent))(('SJoystickEvent_GetJoystick', c_module))
#~ SJoystickEvent_IsButtonPressed = func_type(ctypes.c_bool, ctypes.POINTER(SJoystickEvent), ctypes.c_uint)(('SJoystickEvent_IsButtonPressed', c_module))
SEvent_GetSJoystickEvent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSJoystickEvent', c_module))
SJoystickEvent_GetButtonStates = func_type(ctypes.c_uint, ctypes.c_void_p)(('SJoystickEvent_GetButtonStates', c_module))
SJoystickEvent_GetAxis = func_type(ctypes.c_short * NUMBER_OF_AXES, ctypes.c_void_p)(('SJoystickEvent_GetAxis', c_module))
SJoystickEvent_GetPOV = func_type(ctypes.c_ushort, ctypes.c_void_p)(('SJoystickEvent_GetPOV', c_module))
SJoystickEvent_GetJoystick = func_type(ctypes.c_ubyte, ctypes.c_void_p)(('SJoystickEvent_GetJoystick', c_module))
SJoystickEvent_IsButtonPressed = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('SJoystickEvent_IsButtonPressed', c_module))

#~ SEvent_GetSLogEvent = func_type(ctypes.POINTER(SLogEvent), ctypes.POINTER(SEvent))(('SEvent_GetSLogEvent', c_module))
#~ SLogEvent_GetText = func_type(ctypes.c_char_p, ctypes.POINTER(SLogEvent))(('SLogEvent_GetText', c_module))
#~ if IRR_IMPROVE_UNICODE:
	#~ SLogEvent_GetText = func_type(ctypes.c_wchar_p, ctypes.POINTER(SLogEvent))(('SLogEvent_GetText', c_module))
#~ SLogEvent_GetLevel = func_type(ctypes.c_int, ctypes.POINTER(SLogEvent))(('SLogEvent_GetLevel', c_module))
SEvent_GetSLogEvent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSLogEvent', c_module))
if IRR_IMPROVE_UNICODE or hexversion >= 0x03000000:# hexversion only if use english text with log
	SLogEvent_GetText = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('SLogEvent_GetText', c_module))
else:
	SLogEvent_GetText = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SLogEvent_GetText', c_module))
SLogEvent_GetLevel = func_type(ctypes.c_int, ctypes.c_void_p)(('SLogEvent_GetLevel', c_module))

#~ SEvent_GetSUserEvent = func_type(ctypes.POINTER(SUserEvent), ctypes.POINTER(SEvent))(('SEvent_GetSUserEvent', c_module))
#~ SUserEvent_GetUserData1 = func_type(ctypes.c_int, ctypes.POINTER(SUserEvent))(('SUserEvent_GetUserData1', c_module))
#~ SUserEvent_GetUserData2 = func_type(ctypes.c_int, ctypes.POINTER(SUserEvent))(('SUserEvent_GetUserData2', c_module))
SEvent_GetSUserEvent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSUserEvent', c_module))
SUserEvent_GetUserData1 = func_type(ctypes.c_int, ctypes.c_void_p)(('SUserEvent_GetUserData1', c_module))
SUserEvent_GetUserData2 = func_type(ctypes.c_int, ctypes.c_void_p)(('SUserEvent_GetUserData2', c_module))

if IRR_USE_INPUT_METHOD:
	#~ SEvent_GetSInputMethodEvent = func_type(ctypes.POINTER(SInputMethodEvent), ctypes.POINTER(SEvent))(('SEvent_GetSInputMethodEvent', c_module))
	#~ SInputMethodEvent_GetHandle = func_type(ctypes.c_void_p, ctypes.POINTER(SInputMethodEvent))(('SInputMethodEvent_GetHandle', c_module))
	#~ SInputMethodEvent_GetChar = func_type(ctypes.c_wchar, ctypes.POINTER(SInputMethodEvent))(('SInputMethodEvent_GetChar', c_module))
	#~ SInputMethodEvent_GetEvent = func_type(ctypes.c_int, ctypes.POINTER(SInputMethodEvent))(('SInputMethodEvent_GetEvent', c_module))
	SEvent_GetSInputMethodEvent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SEvent_GetSInputMethodEvent', c_module))
	SInputMethodEvent_GetHandle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SInputMethodEvent_GetHandle', c_module))
	SInputMethodEvent_GetChar = func_type(ctypes.c_wchar, ctypes.c_void_p)(('SInputMethodEvent_GetChar', c_module))
	SInputMethodEvent_GetEvent = func_type(ctypes.c_int, ctypes.c_void_p)(('SInputMethodEvent_GetEvent', c_module))

#~ OnEventFunc = func_type(ctypes.c_bool, ctypes.POINTER(SEvent))
OnEventFunc = func_type(ctypes.c_bool, ctypes.c_void_p)
#~ OnEventFunc = ctypes.PYFUNCTYPE(ctypes.c_bool, ctypes.POINTER(SEvent))
#~ OnEventFunc = func_type(ctypes.c_bool, SEvent)
IEventReceiver_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IEventReceiver_ctor1', c_module))
IEventReceiver_ctor2 = func_type(ctypes.c_void_p, OnEventFunc)(('IEventReceiver_ctor2', c_module))
IEventReceiver_delete = func_type(None, ctypes.c_void_p)(('IEventReceiver_delete', c_module))
IEventReceiver_set_func_event = func_type(None, ctypes.c_void_p, OnEventFunc)(('IEventReceiver_set_func_event', c_module))

# functions for class IFileSystem
IFileSystem_createAndOpenFile = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('IFileSystem_createAndOpenFile', c_module))
IFileSystem_createMemoryReadFile = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, fschar_t, ctypes.c_bool)(('IFileSystem_createMemoryReadFile', c_module))
IFileSystem_createLimitReadFile = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_void_p, ctypes.c_long, ctypes.c_long)(('IFileSystem_createLimitReadFile', c_module))
IFileSystem_createMemoryWriteFile = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, fschar_t, ctypes.c_bool)(('IFileSystem_createMemoryWriteFile', c_module))
IFileSystem_createAndWriteFile = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool)(('IFileSystem_createAndWriteFile', c_module))
IFileSystem_addFileArchive = func_type(ctypes.c_bool, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_bool, ctypes.c_int)(('IFileSystem_addFileArchive', c_module))
IFileSystem_addArchiveLoader = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_addArchiveLoader', c_module))
IFileSystem_getFileArchiveCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IFileSystem_getFileArchiveCount', c_module))
IFileSystem_removeFileArchive1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('IFileSystem_removeFileArchive1', c_module))
IFileSystem_removeFileArchive2 = func_type(ctypes.c_bool, ctypes.c_void_p, fschar_t)(('IFileSystem_removeFileArchive2', c_module))
IFileSystem_moveFileArchive = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IFileSystem_moveFileArchive', c_module))
IFileSystem_getFileArchive = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IFileSystem_getFileArchive', c_module))
if IRRLICHT_VERSION < 180:
	IFileSystem_addZipFileArchive = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool)(('IFileSystem_addZipFileArchive', c_module))
	IFileSystem_addFolderFileArchive = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool)(('IFileSystem_addFolderFileArchive', c_module))
	IFileSystem_addPakFileArchive = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool)(('IFileSystem_addPakFileArchive', c_module))
IFileSystem_getWorkingDirectory = func_type(fschar_t, ctypes.c_void_p)(('IFileSystem_getWorkingDirectory', c_module))
IFileSystem_changeWorkingDirectoryTo = func_type(ctypes.c_bool, ctypes.c_void_p, fschar_t)(('IFileSystem_changeWorkingDirectoryTo', c_module))
IFileSystem_getAbsolutePath = func_type(fschar_t, ctypes.c_void_p, fschar_t)(('IFileSystem_getAbsolutePath', c_module))
IFileSystem_getFileDir = func_type(fschar_t, ctypes.c_void_p, fschar_t)(('IFileSystem_getFileDir', c_module))
IFileSystem_getFileBasename = func_type(fschar_t, ctypes.c_void_p, fschar_t, ctypes.c_bool)(('IFileSystem_getFileBasename', c_module))
IFileSystem_flattenFilename = func_type(fschar_t, ctypes.c_void_p, fschar_t, fschar_t)(('IFileSystem_flattenFilename', c_module))
IFileSystem_createFileList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_createFileList', c_module))
IFileSystem_createEmptyFileList = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_bool, ctypes.c_bool)(('IFileSystem_createEmptyFileList', c_module))
IFileSystem_setFileListSystem = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IFileSystem_setFileListSystem', c_module))
IFileSystem_existFile = func_type(ctypes.c_bool, ctypes.c_void_p, fschar_t)(('IFileSystem_existFile', c_module))
IFileSystem_createXMLReader1 = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('IFileSystem_createXMLReader1', c_module))
IFileSystem_createXMLReader2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_createXMLReader2', c_module))
IFileSystem_createXMLReaderUTF8 = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('IFileSystem_createXMLReaderUTF8', c_module))
IFileSystem_createXMLReaderUTF8stream = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_createXMLReaderUTF8stream', c_module))
IFileSystem_createXMLWriter1 = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('IFileSystem_createXMLWriter1', c_module))
IFileSystem_createXMLWriter2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_createXMLWriter2', c_module))
IFileSystem_createEmptyAttributes = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IFileSystem_createEmptyAttributes', c_module))

# matrix4
matrix4_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_ctor1', c_module))
matrix4_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_ctor2', c_module))
matrix4_delete = func_type(None, ctypes.c_void_p)(('matrix4_delete', c_module))
matrix4_operator_directly = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('matrix4_operator_directly', c_module))
matrix4_operator_linearly = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_uint)(('matrix4_operator_linearly', c_module))
matrix4_set1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_set1', c_module))
matrix4_set2 = func_type(None, ctypes.c_void_p, ctypes.c_float)(('matrix4_set2', c_module))
matrix4_const_pointer = func_type(ctypes.c_float*16, ctypes.c_void_p)(('matrix4_const_pointer', c_module))
matrix4_pointer = func_type(ctypes.c_float*16, ctypes.c_void_p)(('matrix4_pointer', c_module))
matrix4_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_eq', c_module))
matrix4_noteq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_noteq', c_module))
matrix4_add = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_add', c_module))
matrix4_get_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_get_add', c_module))
matrix4_sub = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_sub', c_module))
matrix4_get_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_get_sub', c_module))
matrix4_setbyproduct = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setbyproduct', c_module))
matrix4_setbyproduct_nocheck = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setbyproduct_nocheck', c_module))
matrix4_multiplication1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_multiplication1', c_module))
matrix4_multiplication2 = func_type(None, ctypes.c_void_p, ctypes.c_float)(('matrix4_multiplication2', c_module))
matrix4_get_multiplication1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_get_multiplication1', c_module))
matrix4_get_multiplication2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_get_multiplication2', c_module))
matrix4_makeIdentity = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_makeIdentity', c_module))
matrix4_isIdentity = func_type(ctypes.c_bool, ctypes.c_void_p)(('matrix4_isIdentity', c_module))
matrix4_isOrthogonal = func_type(ctypes.c_bool, ctypes.c_void_p)(('matrix4_isOrthogonal', c_module))
matrix4_isIdentity_integer_base = func_type(ctypes.c_bool, ctypes.c_void_p)(('matrix4_isIdentity_integer_base', c_module))
matrix4_setTranslation = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setTranslation', c_module))
matrix4_getTranslation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getTranslation', c_module))
matrix4_setInverseTranslation = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setInverseTranslation', c_module))
matrix4_setRotationRadians = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setRotationRadians', c_module))
matrix4_setRotationDegrees = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setRotationDegrees', c_module))
matrix4_getRotationDegrees = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getRotationDegrees', c_module))
matrix4_setInverseRotationRadians = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setInverseRotationRadians', c_module))
matrix4_setInverseRotationDegrees = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setInverseRotationDegrees', c_module))
matrix4_setScale1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setScale1', c_module))
matrix4_setScale2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_setScale2', c_module))
matrix4_getScale = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getScale', c_module))
matrix4_inverseTranslateVect = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_inverseTranslateVect', c_module))
matrix4_inverseRotateVect = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_inverseRotateVect', c_module))
matrix4_rotateVect1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_rotateVect1', c_module))
matrix4_rotateVect2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_rotateVect2', c_module))
matrix4_rotateVect3 = func_type(None, ctypes.c_void_p, ctypes.c_float*3, ctypes.c_void_p)(('matrix4_rotateVect3', c_module))
matrix4_transformVect1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformVect1', c_module))
matrix4_transformVect2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformVect2', c_module))
matrix4_transformVect3 = func_type(None, ctypes.c_void_p, ctypes.c_float*4, ctypes.c_void_p)(('matrix4_transformVect3', c_module))
matrix4_translateVect = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_translateVect', c_module))
matrix4_transformPlane1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformPlane1', c_module))
matrix4_transformPlane2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformPlane2', c_module))
#matrix4_transformBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformBox', c_module))
matrix4_transformBoxEx = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_transformBoxEx', c_module))
matrix4_multiplyWith1x4Matrix = func_type(None, ctypes.c_void_p, ctypes.c_float*4)(('matrix4_multiplyWith1x4Matrix', c_module))
matrix4_makeInverse = func_type(ctypes.c_bool, ctypes.c_void_p)(('matrix4_makeInverse', c_module))
matrix4_getInversePrimitive = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getInversePrimitive', c_module))
matrix4_getInverse = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getInverse', c_module))
matrix4_buildProjectionMatrixPerspectiveFovRH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixPerspectiveFovRH', c_module))
matrix4_buildProjectionMatrixPerspectiveFovLH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixPerspectiveFovLH', c_module))
matrix4_buildProjectionMatrixPerspectiveRH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixPerspectiveRH', c_module))
matrix4_buildProjectionMatrixPerspectiveLH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixPerspectiveLH', c_module))
matrix4_buildProjectionMatrixOrthoLH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixOrthoLH', c_module))
matrix4_buildProjectionMatrixOrthoRH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('matrix4_buildProjectionMatrixOrthoRH', c_module))
matrix4_buildCameraLookAtMatrixLH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_buildCameraLookAtMatrixLH', c_module))
matrix4_buildCameraLookAtMatrixRH = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_buildCameraLookAtMatrixRH', c_module))
matrix4_buildShadowMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_buildShadowMatrix', c_module))
matrix4_buildNDCToDCMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_buildNDCToDCMatrix', c_module))
matrix4_interpolate = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_interpolate', c_module))
matrix4_getTransposed1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getTransposed1', c_module))
matrix4_getTransposed2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_getTransposed2', c_module))
matrix4_buildRotateFromTo = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_buildRotateFromTo', c_module))
matrix4_setRotationCenter = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setRotationCenter', c_module))
matrix4_buildAxisAlignedBillboard = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_buildAxisAlignedBillboard', c_module))
matrix4_buildTextureTransform = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_buildTextureTransform', c_module))
matrix4_setTextureRotationCenter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('matrix4_setTextureRotationCenter', c_module))
matrix4_setTextureTranslate = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('matrix4_setTextureTranslate', c_module))
matrix4_setTextureTranslateTransposed = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('matrix4_setTextureTranslateTransposed', c_module))
matrix4_setTextureScale = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('matrix4_setTextureScale', c_module))
matrix4_setTextureScaleCenter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('matrix4_setTextureScaleCenter', c_module))
matrix4_setM = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float*16)(('matrix4_setM', c_module))
#~ matrix4_setM = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('matrix4_setM', c_module))
matrix4_setDefinitelyIdentityMatrix = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('matrix4_setDefinitelyIdentityMatrix', c_module))
matrix4_getDefinitelyIdentityMatrix = func_type(ctypes.c_bool, ctypes.c_void_p)(('matrix4_getDefinitelyIdentityMatrix', c_module))

# functions for class vector2df
vector2df_ctor1 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('vector2df_ctor1', c_module))
vector2df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float)(('vector2df_ctor2', c_module))
vector2df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2df_ctor3', c_module))
vector2df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2df_ctor4', c_module))
vector2df_delete = func_type(None, ctypes.c_void_p)(('vector2df_delete', c_module))
vector2df_operator_sub = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_sub', c_module))
vector2df_operator_set_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_other', c_module))
vector2df_operator_set_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_dimension2d', c_module))
vector2df_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_add_other', c_module))
vector2df_operator_add_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_add_dimension2d', c_module))
vector2df_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_add_other', c_module))
vector2df_operator_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_add_value', c_module))
vector2df_operator_set_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_set_add_value', c_module))
vector2df_operator_set_add_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_add_dimension2d', c_module))
vector2df_operator_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_sub_other', c_module))
vector2df_operator_sub_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_sub_dimension2d', c_module))
vector2df_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_sub_other', c_module))
vector2df_operator_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_sub_value', c_module))
vector2df_operator_set_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_set_sub_value', c_module))
vector2df_operator_set_sub_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_sub_dimension2d', c_module))
vector2df_operator_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_mult_other', c_module))
vector2df_operator_set_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_mult_other', c_module))
vector2df_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_mult_value', c_module))
vector2df_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_set_mult_value', c_module))
vector2df_operator_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_div_other', c_module))
vector2df_operator_set_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_set_div_other', c_module))
vector2df_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_div_value', c_module))
vector2df_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_operator_set_div_value', c_module))
vector2df_operator_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_le', c_module))
vector2df_operator_ge = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_ge', c_module))
vector2df_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_lt', c_module))
vector2df_operator_gt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_gt', c_module))
vector2df_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_eq', c_module))
vector2df_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_operator_ne', c_module))
vector2df_equals = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_equals', c_module))
vector2df_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('vector2df_set', c_module))
vector2df_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_set2', c_module))
vector2df_getLength = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_getLength', c_module))
vector2df_getLengthSQ = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_getLengthSQ', c_module))
vector2df_dotProduct = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_dotProduct', c_module))
vector2df_getDistanceFrom = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_getDistanceFrom', c_module))
vector2df_getDistanceFromSQ = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_getDistanceFromSQ', c_module))
vector2df_rotateBy = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('vector2df_rotateBy', c_module))
vector2df_normalize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2df_normalize', c_module))
vector2df_getAngleTrig = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_getAngleTrig', c_module))
vector2df_getAngle = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_getAngle', c_module))
vector2df_getAngleWith = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_getAngleWith', c_module))
vector2df_isBetweenPoints = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2df_isBetweenPoints', c_module))
vector2df_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_getInterpolated', c_module))
vector2df_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_getInterpolated_quadratic', c_module))
vector2df_interpolate = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector2df_interpolate', c_module))
vector2df_get_X = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_get_X', c_module))
vector2df_set_X = func_type(None, ctypes.c_void_p, ctypes.c_float)(('vector2df_set_X', c_module))
vector2df_get_Y = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2df_get_Y', c_module))
vector2df_set_Y = func_type(None, ctypes.c_void_p, ctypes.c_float)(('vector2df_set_Y', c_module))

# functions for class vector2di
vector2di_ctor1 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('vector2di_ctor1', c_module))
vector2di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('vector2di_ctor2', c_module))
vector2di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2di_ctor3', c_module))
vector2di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2di_ctor4', c_module))
vector2di_delete = func_type(None, ctypes.c_void_p)(('vector2di_delete', c_module))
vector2di_operator_sub = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_sub', c_module))
vector2di_operator_set_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_other', c_module))
vector2di_operator_set_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_dimension2d', c_module))
vector2di_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_add_other', c_module))
vector2di_operator_add_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_add_dimension2d', c_module))
vector2di_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_add_other', c_module))
vector2di_operator_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_add_value', c_module))
vector2di_operator_set_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_set_add_value', c_module))
vector2di_operator_set_add_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_add_dimension2d', c_module))
vector2di_operator_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_sub_other', c_module))
vector2di_operator_sub_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_sub_dimension2d', c_module))
vector2di_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_sub_other', c_module))
vector2di_operator_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_sub_value', c_module))
vector2di_operator_set_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_set_sub_value', c_module))
vector2di_operator_set_sub_dimension2d = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_sub_dimension2d', c_module))
vector2di_operator_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_mult_other', c_module))
vector2di_operator_set_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_mult_other', c_module))
vector2di_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_mult_value', c_module))
vector2di_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_set_mult_value', c_module))
vector2di_operator_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_div_other', c_module))
vector2di_operator_set_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_set_div_other', c_module))
vector2di_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_div_value', c_module))
vector2di_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_operator_set_div_value', c_module))
vector2di_operator_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_le', c_module))
vector2di_operator_ge = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_ge', c_module))
vector2di_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_lt', c_module))
vector2di_operator_gt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_gt', c_module))
vector2di_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_eq', c_module))
vector2di_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_operator_ne', c_module))
vector2di_equals = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_equals', c_module))
vector2di_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('vector2di_set', c_module))
vector2di_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_set2', c_module))
vector2di_getLength = func_type(ctypes.c_int, ctypes.c_void_p)(('vector2di_getLength', c_module))
vector2di_getLengthSQ = func_type(ctypes.c_int, ctypes.c_void_p)(('vector2di_getLengthSQ', c_module))
vector2di_dotProduct = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_dotProduct', c_module))
vector2di_getDistanceFrom = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_getDistanceFrom', c_module))
vector2di_getDistanceFromSQ = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_getDistanceFromSQ', c_module))
vector2di_rotateBy = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('vector2di_rotateBy', c_module))
vector2di_normalize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector2di_normalize', c_module))
vector2di_getAngleTrig = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2di_getAngleTrig', c_module))
vector2di_getAngle = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2di_getAngle', c_module))
vector2di_getAngleWith = func_type(ctypes.c_float, ctypes.c_void_p)(('vector2di_getAngleWith', c_module))
vector2di_isBetweenPoints = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector2di_isBetweenPoints', c_module))
vector2di_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_getInterpolated', c_module))
vector2di_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_getInterpolated_quadratic', c_module))
vector2di_interpolate = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector2di_interpolate', c_module))
vector2di_get_X = func_type(ctypes.c_int, ctypes.c_void_p)(('vector2di_get_X', c_module))
vector2di_set_X = func_type(None, ctypes.c_void_p, ctypes.c_int)(('vector2di_set_X', c_module))
vector2di_get_Y = func_type(ctypes.c_int, ctypes.c_void_p)(('vector2di_get_Y', c_module))
vector2di_set_Y = func_type(None, ctypes.c_void_p, ctypes.c_int)(('vector2di_set_Y', c_module))

# functions for class position2df
position2df_ctor1 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('position2df_ctor1', c_module), ((1, 'nx', 0.0), (1, 'ny', 0.0)))
position2df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float)(('position2df_ctor2', c_module), ((1, 'n', 0), ))
position2df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('position2df_ctor3', c_module))
position2df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('position2df_ctor4', c_module))

# functions for class position2di
position2di_ctor1 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('position2di_ctor1', c_module), ((1, 'nx', 0), (1, 'ny', 0)))
position2di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('position2di_ctor2', c_module), ((1, 'n', 0), ))
position2di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('position2di_ctor3', c_module))
position2di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('position2di_ctor4', c_module))

# functions for class dimension2df
dimension2df_ctor1 = func_type(ctypes.c_void_p)(('dimension2df_ctor1', c_module))
dimension2df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('dimension2df_ctor2', c_module))
dimension2df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_ctor3', c_module))
dimension2df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_ctor4', c_module))
dimension2df_delete = func_type(None, ctypes.c_void_p)(('dimension2df_delete', c_module))
dimension2df_operator_set_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_set_other', c_module))
dimension2df_operator_eq_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_eq_other', c_module))
dimension2df_operator_ne_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_ne_other', c_module))
dimension2df_operator_eq_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_eq_vector2d', c_module))
dimension2df_operator_ne_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_ne_vector2d', c_module))
dimension2df_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('dimension2df_set', c_module))
dimension2df_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('dimension2df_operator_set_div_value', c_module))
dimension2df_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('dimension2df_operator_div_value', c_module))
dimension2df_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('dimension2df_operator_set_mult_value', c_module))
dimension2df_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('dimension2df_operator_mult_value', c_module))
dimension2df_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_set_add_other', c_module))
dimension2df_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_set_sub_other', c_module))
dimension2df_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2df_operator_add_other', c_module))
dimension2df_getArea = func_type(ctypes.c_float, ctypes.c_void_p)(('dimension2df_getArea', c_module))
dimension2df_getOptimalSize = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_float)(('dimension2df_getOptimalSize', c_module))
dimension2df_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('dimension2df_getInterpolated', c_module))
dimension2df_get_Width = func_type(ctypes.c_float, ctypes.c_void_p)(('dimension2df_get_Width', c_module))
dimension2df_set_Width = func_type(None, ctypes.c_void_p, ctypes.c_float)(('dimension2df_set_Width', c_module))
dimension2df_get_Height = func_type(ctypes.c_float, ctypes.c_void_p)(('dimension2df_get_Height', c_module))
dimension2df_set_Height = func_type(None, ctypes.c_void_p, ctypes.c_float)(('dimension2df_set_Height', c_module))

# functions for class dimension2du
dimension2du_ctor1 = func_type(ctypes.c_void_p)(('dimension2du_ctor1', c_module))
dimension2du_ctor2 = func_type(ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('dimension2du_ctor2', c_module))
dimension2du_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_ctor3', c_module))
dimension2du_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_ctor4', c_module))
dimension2du_delete = func_type(None, ctypes.c_void_p)(('dimension2du_delete', c_module))
dimension2du_operator_set_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_set_other', c_module))
dimension2du_operator_eq_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_eq_other', c_module))
dimension2du_operator_ne_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_ne_other', c_module))
dimension2du_operator_eq_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_eq_vector2d', c_module))
dimension2du_operator_ne_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_ne_vector2d', c_module))
dimension2du_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('dimension2du_set', c_module))
dimension2du_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_operator_set_div_value', c_module))
dimension2du_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_operator_div_value', c_module))
dimension2du_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_operator_set_mult_value', c_module))
dimension2du_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_operator_mult_value', c_module))
dimension2du_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_set_add_other', c_module))
dimension2du_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_set_sub_other', c_module))
dimension2du_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2du_operator_add_other', c_module))
dimension2du_getArea = func_type(ctypes.c_uint, ctypes.c_void_p)(('dimension2du_getArea', c_module))
dimension2du_getOptimalSize = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_uint)(('dimension2du_getOptimalSize', c_module))
dimension2du_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_getInterpolated', c_module))
dimension2du_get_Width = func_type(ctypes.c_uint, ctypes.c_void_p)(('dimension2du_get_Width', c_module))
dimension2du_set_Width = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_set_Width', c_module))
dimension2du_get_Height = func_type(ctypes.c_uint, ctypes.c_void_p)(('dimension2du_get_Height', c_module))
dimension2du_set_Height = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('dimension2du_set_Height', c_module))

# functions for class dimension2di
dimension2di_ctor1 = func_type(ctypes.c_void_p)(('dimension2di_ctor1', c_module))
dimension2di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('dimension2di_ctor2', c_module))
dimension2di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_ctor3', c_module))
dimension2di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_ctor4', c_module))
dimension2di_delete = func_type(None, ctypes.c_void_p)(('dimension2di_delete', c_module))
dimension2di_operator_set_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_set_other', c_module))
dimension2di_operator_eq_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_eq_other', c_module))
dimension2di_operator_ne_other = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_ne_other', c_module))
dimension2di_operator_eq_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_eq_vector2d', c_module))
dimension2di_operator_ne_vector2d = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_ne_vector2d', c_module))
dimension2di_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('dimension2di_set', c_module))
dimension2di_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('dimension2di_operator_set_div_value', c_module))
dimension2di_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('dimension2di_operator_div_value', c_module))
dimension2di_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('dimension2di_operator_set_mult_value', c_module))
dimension2di_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('dimension2di_operator_mult_value', c_module))
dimension2di_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_set_add_other', c_module))
dimension2di_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_set_sub_other', c_module))
dimension2di_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('dimension2di_operator_add_other', c_module))
dimension2di_getArea = func_type(ctypes.c_int, ctypes.c_void_p)(('dimension2di_getArea', c_module))
dimension2di_getOptimalSize = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_int)(('dimension2di_getOptimalSize', c_module))
dimension2di_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('dimension2di_getInterpolated', c_module))
dimension2di_get_Width = func_type(ctypes.c_int, ctypes.c_void_p)(('dimension2di_get_Width', c_module))
dimension2di_set_Width = func_type(None, ctypes.c_void_p, ctypes.c_int)(('dimension2di_set_Width', c_module))
dimension2di_get_Height = func_type(ctypes.c_int, ctypes.c_void_p)(('dimension2di_get_Height', c_module))
dimension2di_set_Height = func_type(None, ctypes.c_void_p, ctypes.c_int)(('dimension2di_set_Height', c_module))

# functions for class rectf
rectf_ctor1 = func_type(ctypes.c_void_p)(('rectf_ctor1', c_module))
rectf_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('rectf_ctor2', c_module))
rectf_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_ctor3', c_module))
rectf_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_ctor4', c_module))
rectf_delete = func_type(None, ctypes.c_void_p)(('rectf_delete', c_module))
rectf_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_add', c_module))
rectf_add_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_add_set', c_module))
rectf_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_sub', c_module))
rectf_sub_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rectf_sub_set', c_module))
rectf_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_eq', c_module))
rectf_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_ne', c_module))
rectf_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_le', c_module))
rectf_getArea = func_type(ctypes.c_float, ctypes.c_void_p)(('rectf_getArea', c_module))
rectf_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_isPointInside', c_module))
rectf_isRectCollided = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_isRectCollided', c_module))
rectf_clipAgainst = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rectf_clipAgainst', c_module))
rectf_constrainTo = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('rectf_constrainTo', c_module))
rectf_getWidth = func_type(ctypes.c_float, ctypes.c_void_p)(('rectf_getWidth', c_module))
rectf_getHeight = func_type(ctypes.c_float, ctypes.c_void_p)(('rectf_getHeight', c_module))
rectf_repair = func_type(None, ctypes.c_void_p)(('rectf_repair', c_module))
rectf_isValid = func_type(ctypes.c_bool, ctypes.c_void_p)(('rectf_isValid', c_module))
rectf_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('rectf_getCenter', c_module))
rectf_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('rectf_getSize', c_module))
rectf_addInternalPoint1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rectf_addInternalPoint1', c_module))
rectf_addInternalPoint2 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('rectf_addInternalPoint2', c_module))
rectf_get_UpperLeftCorner = func_type(ctypes.c_void_p, ctypes.c_void_p)(('rectf_get_UpperLeftCorner', c_module))
rectf_set_UpperLeftCorner = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rectf_set_UpperLeftCorner', c_module))
rectf_get_LowerRightCorner = func_type(ctypes.c_void_p, ctypes.c_void_p)(('rectf_get_LowerRightCorner', c_module))
rectf_set_LowerRightCorner = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rectf_set_LowerRightCorner', c_module))

# functions for class recti
recti_ctor1 = func_type(ctypes.c_void_p)(('recti_ctor1', c_module))
recti_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('recti_ctor2', c_module))
recti_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_ctor3', c_module))
recti_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_ctor4', c_module))
recti_delete = func_type(None, ctypes.c_void_p)(('recti_delete', c_module))
recti_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_add', c_module))
recti_add_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_add_set', c_module))
recti_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_sub', c_module))
recti_sub_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('recti_sub_set', c_module))
recti_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_eq', c_module))
recti_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_ne', c_module))
recti_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_le', c_module))
recti_getArea = func_type(ctypes.c_int, ctypes.c_void_p)(('recti_getArea', c_module))
recti_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_isPointInside', c_module))
recti_isRectCollided = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_isRectCollided', c_module))
recti_clipAgainst = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('recti_clipAgainst', c_module))
recti_constrainTo = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('recti_constrainTo', c_module))
recti_getWidth = func_type(ctypes.c_int, ctypes.c_void_p)(('recti_getWidth', c_module))
recti_getHeight = func_type(ctypes.c_int, ctypes.c_void_p)(('recti_getHeight', c_module))
recti_repair = func_type(None, ctypes.c_void_p)(('recti_repair', c_module))
recti_isValid = func_type(ctypes.c_bool, ctypes.c_void_p)(('recti_isValid', c_module))
recti_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('recti_getCenter', c_module))
recti_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('recti_getSize', c_module))
recti_addInternalPoint1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('recti_addInternalPoint1', c_module))
recti_addInternalPoint2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('recti_addInternalPoint2', c_module))
recti_get_UpperLeftCorner = func_type(ctypes.c_void_p, ctypes.c_void_p)(('recti_get_UpperLeftCorner', c_module))
recti_set_UpperLeftCorner = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('recti_set_UpperLeftCorner', c_module))
recti_get_LowerRightCorner = func_type(ctypes.c_void_p, ctypes.c_void_p)(('recti_get_LowerRightCorner', c_module))
recti_set_LowerRightCorner = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('recti_set_LowerRightCorner', c_module))

# functions for class vector3df
vector3df_ctor1 = func_type(ctypes.c_void_p)(('vector3df_ctor1', c_module))
vector3df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('vector3df_ctor2', c_module))
vector3df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_float)(('vector3df_ctor3', c_module))
vector3df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_ctor4', c_module))
vector3df_delete = func_type(None, ctypes.c_float)(('vector3df_delete', c_module))
vector3df_set_X = func_type(None, ctypes.c_void_p, ctypes.c_float)(('vector3df_set_X', c_module), ((1, 'pointer', 0), (1, 'value', 0.0)))
vector3df_get_X = func_type(ctypes.c_float, ctypes.c_void_p)(('vector3df_get_X', c_module))
vector3df_set_Y = func_type(None, ctypes.c_void_p, ctypes.c_float)(('vector3df_set_Y', c_module), ((1, 'pointer', 0), (1, 'value', 0.0)))
vector3df_get_Y = func_type(ctypes.c_float, ctypes.c_void_p)(('vector3df_get_Y', c_module))
vector3df_set_Z = func_type(None, ctypes.c_void_p, ctypes.c_float)(('vector3df_set_Z', c_module), ((1, 'pointer', 0), (1, 'value', 0.0)))
vector3df_get_Z = func_type(ctypes.c_float, ctypes.c_void_p)(('vector3df_get_Z', c_module))
vector3df_operator_sub = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_sub', c_module))
vector3df_operator_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_set', c_module))
vector3df_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_add_other', c_module))
vector3df_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_set_add_other', c_module))
vector3df_operator_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_add_value', c_module))
vector3df_operator_set_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_set_add_value', c_module))
vector3df_operator_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_sub_other', c_module))
vector3df_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_set_sub_other', c_module))
vector3df_operator_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_sub_value', c_module))
vector3df_operator_set_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_set_sub_value', c_module))
vector3df_operator_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_mult_other', c_module))
vector3df_operator_set_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_set_mult_other', c_module))
vector3df_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_mult_value', c_module))
vector3df_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_set_mult_value', c_module))
vector3df_operator_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_div_other', c_module))
vector3df_operator_set_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_set_div_other', c_module))
vector3df_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_div_value', c_module))
vector3df_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_operator_set_div_value', c_module))
vector3df_operator_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_le', c_module))
vector3df_operator_ge = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_ge', c_module))
vector3df_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_lt', c_module))
vector3df_operator_gt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_gt', c_module))
vector3df_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_eq', c_module))
vector3df_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_ne', c_module))
vector3df_equals = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_equals', c_module))
vector3df_set1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('vector3df_set1', c_module))
vector3df_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_set2', c_module))
vector3df_getLength = func_type(ctypes.c_float, ctypes.c_void_p)(('vector3df_getLength', c_module))
vector3df_getLengthSQ = func_type(ctypes.c_float, ctypes.c_void_p)(('vector3df_getLengthSQ', c_module))
vector3df_dotProduct = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_dotProduct', c_module))
vector3df_getDistanceFrom = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_getDistanceFrom', c_module))
vector3df_getDistanceFromSQ = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_getDistanceFromSQ', c_module))
vector3df_crossProduct = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_crossProduct', c_module))
vector3df_isBetweenPoints = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_isBetweenPoints', c_module))
vector3df_normalize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_normalize', c_module))
vector3df_setLength = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_setLength', c_module))
vector3df_invert = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_invert', c_module))
vector3df_rotateXZBy = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('vector3df_rotateXZBy', c_module))
vector3df_rotateXYBy = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('vector3df_rotateXYBy', c_module))
vector3df_rotateYZBy = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('vector3df_rotateYZBy', c_module))
vector3df_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_getInterpolated', c_module))
vector3df_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_getInterpolated_quadratic', c_module))
vector3df_interpolate = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('vector3df_interpolate', c_module))
vector3df_getHorizontalAngle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_getHorizontalAngle', c_module))
vector3df_getSphericalCoordinateAngles = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_getSphericalCoordinateAngles', c_module))
vector3df_rotationToDirection = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_rotationToDirection', c_module))
vector3df_getAs4Values = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('vector3df_getAs4Values', c_module))

# functions for class vector3di
vector3di_ctor1 = func_type(ctypes.c_void_p)(('vector3di_ctor1', c_module))
vector3di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('vector3di_ctor2', c_module))
vector3di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_int)(('vector3di_ctor3', c_module))
vector3di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3di_ctor4', c_module))
vector3di_delete = func_type(None, ctypes.c_float)(('vector3di_delete', c_module))
vector3di_set_X = func_type(None, ctypes.c_void_p, ctypes.c_int)(('vector3di_set_X', c_module), ((1, 'pointer', 0), (1, 'value', 0)))
vector3di_get_X = func_type(ctypes.c_int, ctypes.c_void_p)(('vector3di_get_X', c_module))
vector3di_set_Y = func_type(None, ctypes.c_void_p, ctypes.c_int)(('vector3di_set_Y', c_module), ((1, 'pointer', 0), (1, 'value', 0)))
vector3di_get_Y = func_type(ctypes.c_int, ctypes.c_void_p)(('vector3di_get_Y', c_module))
vector3di_set_Z = func_type(None, ctypes.c_void_p, ctypes.c_int)(('vector3di_set_Z', c_module), ((1, 'pointer', 0), (1, 'value', 0)))
vector3di_get_Z = func_type(ctypes.c_int, ctypes.c_void_p)(('vector3di_get_Z', c_module))
vector3di_operator_sub = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3df_operator_sub', c_module))
vector3di_operator_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_set', c_module))
vector3di_operator_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_add_other', c_module))
vector3di_operator_set_add_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_set_add_other', c_module))
vector3di_operator_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_add_value', c_module))
vector3di_operator_set_add_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_set_add_value', c_module))
vector3di_operator_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_sub_other', c_module))
vector3di_operator_set_sub_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_set_sub_other', c_module))
vector3di_operator_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_sub_value', c_module))
vector3di_operator_set_sub_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_set_sub_value', c_module))
vector3di_operator_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_mult_other', c_module))
vector3di_operator_set_mult_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_set_mult_other', c_module))
vector3di_operator_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_mult_value', c_module))
vector3di_operator_set_mult_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_set_mult_value', c_module))
vector3di_operator_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_div_other', c_module))
vector3di_operator_set_div_other = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_set_div_other', c_module))
vector3di_operator_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_div_value', c_module))
vector3di_operator_set_div_value = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_operator_set_div_value', c_module))
vector3di_operator_le = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_le', c_module))
vector3di_operator_ge = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_ge', c_module))
vector3di_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_lt', c_module))
vector3di_operator_gt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_gt', c_module))
vector3di_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_eq', c_module))
vector3di_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_operator_ne', c_module))
vector3di_equals = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_equals', c_module))
vector3di_set1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('vector3di_set1', c_module))
vector3di_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_set2', c_module))
vector3di_getLength = func_type(ctypes.c_int, ctypes.c_void_p)(('vector3di_getLength', c_module))
vector3di_getLengthSQ = func_type(ctypes.c_int, ctypes.c_void_p)(('vector3di_getLengthSQ', c_module))
vector3di_dotProduct = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_dotProduct', c_module))
vector3di_getDistanceFrom = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_getDistanceFrom', c_module))
vector3di_getDistanceFromSQ = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_getDistanceFromSQ', c_module))
vector3di_crossProduct = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_crossProduct', c_module))
vector3di_isBetweenPoints = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_isBetweenPoints', c_module))
vector3di_normalize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3di_normalize', c_module))
vector3di_setLength = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_setLength', c_module))
vector3di_invert = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3di_invert', c_module))
vector3di_rotateXZBy = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('vector3di_rotateXZBy', c_module))
vector3di_rotateXYBy = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('vector3di_rotateXYBy', c_module))
vector3di_rotateYZBy = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('vector3di_rotateYZBy', c_module))
vector3di_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_getInterpolated', c_module))
vector3di_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_getInterpolated_quadratic', c_module))
vector3di_interpolate = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('vector3di_interpolate', c_module))
vector3di_getHorizontalAngle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3di_getHorizontalAngle', c_module))
vector3di_getSphericalCoordinateAngles = func_type(ctypes.c_void_p, ctypes.c_void_p)(('vector3di_getSphericalCoordinateAngles', c_module))
vector3di_rotationToDirection = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_rotationToDirection', c_module))
vector3di_getAs4Values = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('vector3di_getAs4Values', c_module))

# functions for class aabbox3df
aabbox3df_ctor1 = func_type(ctypes.c_void_p)(('aabbox3df_ctor1', c_module))
aabbox3df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_ctor2', c_module), ((1, 'min', vector3df_ctor2(-1.0, -1.0, -1.0)), (1, 'max', vector3df_ctor2(1.0, 1.0, 1.0))))
aabbox3df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_ctor3', c_module), ((1, 'init', vector3df_ctor2(-1.0, -1.0, -1.0)), ))
aabbox3df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('aabbox3df_ctor4', c_module), ((1, 'minx', -1.0), (1, 'miny', -1.0), (1, 'minz', -1.0), (1, 'maxx', 1.0), (1, 'maxy', 1.0), (1, 'maxz', 1.0)))
aabbox3df_delete = func_type(None, ctypes.c_void_p)(('aabbox3df_delete', c_module))
aabbox3df_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_operator_eq', c_module))
aabbox3df_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_operator_ne', c_module))
aabbox3df_reset1 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('aabbox3df_reset1', c_module))
aabbox3df_reset2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_reset2', c_module))
aabbox3df_reset3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_reset3', c_module))
aabbox3df_addInternalBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_addInternalBox', c_module))
aabbox3df_addInternalPoint1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_addInternalPoint1', c_module))
aabbox3df_addInternalPoint2 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('aabbox3df_addInternalPoint2', c_module))
aabbox3df_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_getCenter', c_module))
aabbox3df_getExtent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_getExtent', c_module))
aabbox3df_isEmpty = func_type(ctypes.c_bool, ctypes.c_void_p)(('aabbox3df_isEmpty', c_module))
aabbox3df_getVolume = func_type(ctypes.c_float, ctypes.c_void_p)(('aabbox3df_getVolume', c_module))
aabbox3df_getArea = func_type(ctypes.c_float, ctypes.c_void_p)(('aabbox3df_getArea', c_module))
aabbox3df_getEdges = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_getEdges', c_module))
aabbox3df_repair = func_type(None, ctypes.c_void_p)(('aabbox3df_repair', c_module))
aabbox3df_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('aabbox3df_getInterpolated', c_module))
aabbox3df_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_isPointInside', c_module))
aabbox3df_isPointTotalInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_isPointTotalInside', c_module))
aabbox3df_isFullInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_isFullInside', c_module))
aabbox3df_intersectsWithBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_intersectsWithBox', c_module))
aabbox3df_intersectsWithLine1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_intersectsWithLine1', c_module))
aabbox3df_intersectsWithLine2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('aabbox3df_intersectsWithLine2', c_module))
aabbox3df_classifyPlaneRelation = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_classifyPlaneRelation', c_module))
aabbox3df_get_MinEdge = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_get_MinEdge', c_module))
aabbox3df_set_MinEdge = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_set_MinEdge', c_module))
aabbox3df_get_MaxEdge = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_get_MaxEdge', c_module))
aabbox3df_set_MaxEdge = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3df_set_MaxEdge', c_module))

# functions for class aabbox3di
aabbox3di_ctor1 = func_type(ctypes.c_void_p)(('aabbox3di_ctor1', c_module))
aabbox3di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_ctor2', c_module), ((1, 'min', vector3di_ctor2(-1, -1, -1)), (1, 'max', vector3di_ctor2(1, 1, 1))))
aabbox3di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_ctor3', c_module), ((1, 'init', vector3di_ctor2(-1, -1, -1)), ))
aabbox3di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('aabbox3di_ctor4', c_module), ((1, 'minx', -1), (1, 'miny', -1), (1, 'minz', -1), (1, 'maxx', 1), (1, 'maxy', 1), (1, 'maxz', 1)))
aabbox3di_delete = func_type(None, ctypes.c_void_p)(('aabbox3di_delete', c_module))
aabbox3di_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_operator_eq', c_module))
aabbox3di_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_operator_ne', c_module))
aabbox3di_reset1 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('aabbox3di_reset1', c_module))
aabbox3di_reset2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_reset2', c_module))
aabbox3di_reset3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_reset3', c_module))
aabbox3di_addInternalBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_addInternalBox', c_module))
aabbox3di_addInternalPoint1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_addInternalPoint1', c_module))
aabbox3di_addInternalPoint2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('aabbox3di_addInternalPoint2', c_module))
aabbox3di_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_getCenter', c_module))
aabbox3di_getExtent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_getExtent', c_module))
aabbox3di_isEmpty = func_type(ctypes.c_bool, ctypes.c_void_p)(('aabbox3di_isEmpty', c_module))
aabbox3di_getVolume = func_type(ctypes.c_int, ctypes.c_void_p)(('aabbox3di_getVolume', c_module))
aabbox3di_getArea = func_type(ctypes.c_int, ctypes.c_void_p)(('aabbox3di_getArea', c_module))
aabbox3di_getEdges = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_getEdges', c_module))
aabbox3di_repair = func_type(None, ctypes.c_void_p)(('aabbox3di_repair', c_module))
aabbox3di_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('aabbox3di_getInterpolated', c_module))
aabbox3di_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_isPointInside', c_module))
aabbox3di_isPointTotalInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_isPointTotalInside', c_module))
aabbox3di_isFullInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_isFullInside', c_module))
aabbox3di_intersectsWithBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_intersectsWithBox', c_module))
#~ aabbox3di_intersectsWithLine1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_intersectsWithLine1', c_module))
#~ aabbox3di_intersectsWithLine2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('aabbox3di_intersectsWithLine2', c_module))
aabbox3di_classifyPlaneRelation = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_classifyPlaneRelation', c_module))
aabbox3di_get_MinEdge = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_get_MinEdge', c_module))
aabbox3di_set_MinEdge = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_set_MinEdge', c_module))
aabbox3di_get_MaxEdge = func_type(ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_get_MaxEdge', c_module))
aabbox3di_set_MaxEdge = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('aabbox3di_set_MaxEdge', c_module))

#class CDynamicMeshBuffer
CDynamicMeshBuffer_ctor = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('CDynamicMeshBuffer_ctor', c_module))
CDynamicMeshBuffer_delete = func_type(None, ctypes.c_void_p)(('CDynamicMeshBuffer_delete', c_module))
CDynamicMeshBuffer_getVertexBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_getVertexBuffer', c_module))
CDynamicMeshBuffer_getIndexBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_getIndexBuffer', c_module))
CDynamicMeshBuffer_setVertexBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_setVertexBuffer', c_module))
CDynamicMeshBuffer_setIndexBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_setIndexBuffer', c_module))
CDynamicMeshBuffer_getMaterial1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_getMaterial1', c_module))
CDynamicMeshBuffer_getMaterial2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_getMaterial2', c_module))
CDynamicMeshBuffer_setMaterial = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_setMaterial', c_module))
CDynamicMeshBuffer_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_getBoundingBox', c_module))
CDynamicMeshBuffer_setBoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CDynamicMeshBuffer_setBoundingBox', c_module))
CDynamicMeshBuffer_recalculateBoundingBox = func_type(None, ctypes.c_void_p)(('CDynamicMeshBuffer_recalculateBoundingBox', c_module))

# functions for class line3df
line3df_ctor1 = func_type(ctypes.c_void_p)(('line3df_ctor1', c_module))
line3df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('line3df_ctor2', c_module))
line3df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_ctor3', c_module))
line3df_delete = func_type(ctypes.c_void_p)(('line3df_delete', c_module))
line3df_get_start = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3df_get_start', c_module))
line3df_get_end = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3df_get_end', c_module))
line3df_set_start = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3df_set_start', c_module))
line3df_set_end = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3df_set_end', c_module))
line3df_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_add', c_module))
line3df_add_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_add_set', c_module))
line3df_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_sub', c_module))
line3df_sub_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_sub_set', c_module))
line3df_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3df_eq', c_module))
line3df_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3df_ne', c_module))
line3df_setLine1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_setLine1', c_module))
line3df_setLine2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_setLine2', c_module))
line3df_setLine3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3df_setLine3', c_module))
line3df_getLength = func_type(ctypes.c_float, ctypes.c_void_p)(('line3df_getLength', c_module))
line3df_getLengthSQ = func_type(ctypes.c_float, ctypes.c_void_p)(('line3df_getLengthSQ', c_module))
line3df_getMiddle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3df_getMiddle', c_module))
line3df_getVector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3df_getVector', c_module))
line3df_isPointBetweenStartAndEnd = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3df_isPointBetweenStartAndEnd', c_module))
line3df_getClosestPoint = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3df_getClosestPoint', c_module))
line3df_getIntersectionWithSphere = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('line3df_getIntersectionWithSphere', c_module))

# functions for class line3di
line3di_ctor1 = func_type(ctypes.c_void_p)(('line3di_ctor1', c_module))
line3di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('line3di_ctor2', c_module))
line3di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_ctor3', c_module))
line3di_delete = func_type(ctypes.c_void_p)(('line3di_delete', c_module))
line3di_get_start = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3di_get_start', c_module))
line3di_get_end = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3di_get_end', c_module))
line3di_set_start = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3di_set_start', c_module))
line3di_set_end = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3di_set_end', c_module))
line3di_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_add', c_module))
line3di_add_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_add_set', c_module))
line3di_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_sub', c_module))
line3di_sub_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_sub_set', c_module))
line3di_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3di_eq', c_module))
line3di_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3di_ne', c_module))
line3di_setLine1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_setLine1', c_module))
line3di_setLine2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_setLine2', c_module))
line3di_setLine3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('line3di_setLine3', c_module))
line3di_getLength = func_type(ctypes.c_int, ctypes.c_void_p)(('line3di_getLength', c_module))
line3di_getLengthSQ = func_type(ctypes.c_int, ctypes.c_void_p)(('line3di_getLengthSQ', c_module))
line3di_getMiddle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3di_getMiddle', c_module))
line3di_getVector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('line3di_getVector', c_module))
line3di_isPointBetweenStartAndEnd = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('line3di_isPointBetweenStartAndEnd', c_module))
line3di_getClosestPoint = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('line3di_getClosestPoint', c_module))
line3di_getIntersectionWithSphere = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('line3di_getIntersectionWithSphere', c_module))

# triangle3d
triangle3df_ctor1 = func_type(ctypes.c_void_p)(('triangle3df_ctor1', c_module))
triangle3df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_ctor2', c_module))
triangle3df_delete = func_type(ctypes.c_void_p)(('triangle3df_delete', c_module))
triangle3df_get_pointA = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_get_pointA', c_module))
triangle3df_get_pointB = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_get_pointB', c_module))
triangle3df_get_pointC = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_get_pointC', c_module))
triangle3df_set_pointA = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_set_pointA', c_module))
triangle3df_set_pointB = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_set_pointB', c_module))
triangle3df_set_pointC = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_set_pointC', c_module))
triangle3df_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_operator_eq', c_module))
triangle3df_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_operator_ne', c_module))
triangle3df_isTotalInsideBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_isTotalInsideBox', c_module))
triangle3df_isTotalOutsideBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_isTotalOutsideBox', c_module))
triangle3df_closestPointOnTriangle = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_closestPointOnTriangle', c_module))
triangle3df_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_isPointInside', c_module))
triangle3df_isPointInsideFast = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_isPointInsideFast', c_module))
triangle3df_getIntersectionWithLimitedLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_getIntersectionWithLimitedLine', c_module))
triangle3df_getIntersectionWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_getIntersectionWithLine', c_module))
triangle3df_getIntersectionOfPlaneWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_getIntersectionOfPlaneWithLine', c_module))
triangle3df_getNormal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_getNormal', c_module))
triangle3df_isFrontFacing = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_isFrontFacing', c_module))
triangle3df_getPlane = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_getPlane', c_module))
triangle3df_getArea = func_type(ctypes.c_float, ctypes.c_void_p)(('triangle3df_getArea', c_module))
triangle3df_set = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3df_set', c_module))

triangle3di_ctor1 = func_type(ctypes.c_void_p)(('triangle3di_ctor1', c_module))
triangle3di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_ctor2', c_module))
triangle3di_delete = func_type(ctypes.c_void_p)(('triangle3di_delete', c_module))
triangle3di_get_pointA = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_get_pointA', c_module))
triangle3di_get_pointB = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_get_pointB', c_module))
triangle3di_get_pointC = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_get_pointC', c_module))
triangle3di_set_pointA = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_set_pointA', c_module))
triangle3di_set_pointB = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_set_pointB', c_module))
triangle3di_set_pointC = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_set_pointC', c_module))
triangle3di_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_operator_eq', c_module))
triangle3di_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_operator_ne', c_module))
triangle3di_isTotalInsideBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_isTotalInsideBox', c_module))
triangle3di_isTotalOutsideBox = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_isTotalOutsideBox', c_module))
triangle3di_closestPointOnTriangle = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_closestPointOnTriangle', c_module))
triangle3di_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_isPointInside', c_module))
triangle3di_isPointInsideFast = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_isPointInsideFast', c_module))
triangle3di_getIntersectionWithLimitedLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_getIntersectionWithLimitedLine', c_module))
triangle3di_getIntersectionWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_getIntersectionWithLine', c_module))
triangle3di_getIntersectionOfPlaneWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_getIntersectionOfPlaneWithLine', c_module))
triangle3di_getNormal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_getNormal', c_module))
triangle3di_isFrontFacing = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_isFrontFacing', c_module))
triangle3di_getPlane = func_type(ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_getPlane', c_module))
triangle3di_getArea = func_type(ctypes.c_int, ctypes.c_void_p)(('triangle3di_getArea', c_module))
triangle3di_set = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('triangle3di_set', c_module))

#================= S3DVertex
getVertexPitchFromType = func_type(ctypes.c_uint, ctypes.c_int)(('tool_getVertexPitchFromType', c_module))
S3DVertex_ctor1 = func_type(ctypes.c_void_p, ctypes.c_int)(('S3DVertex_ctor1', c_module))
S3DVertex_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('S3DVertex_ctor2', c_module))
S3DVertex_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertex_ctor3', c_module))
S3DVertex_get_item = func_type(ctypes.c_void_p, ctypes.c_int)(('S3DVertex_get_item', c_module))
S3DVertex_set_item = func_type(None, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_set_item', c_module))
S3DVertex_get_Pos = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_get_Pos', c_module))
S3DVertex_set_Pos = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_set_Pos', c_module))
S3DVertex_get_Normal = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_get_Normal', c_module))
S3DVertex_set_Normal = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_set_Normal', c_module))
S3DVertex_get_Color = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_get_Color', c_module))
S3DVertex_set_Color = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_set_Color', c_module))
S3DVertex_get_TCoords = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_get_TCoords', c_module))
S3DVertex_set_TCoords = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_set_TCoords', c_module))
S3DVertex_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_eq', c_module))
S3DVertex_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_ne', c_module))
S3DVertex_less = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_less', c_module))
S3DVertex_getType = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('S3DVertex_getType', c_module))
if IRRLICHT_VERSION >= 180:
	S3DVertex_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_int)(('S3DVertex_getInterpolated', c_module))

#struct S3DVertex2TCoords : public S3DVertex
S3DVertex2TCoords_ctor1 = func_type(ctypes.c_void_p, ctypes.c_int)(('S3DVertex2TCoords_ctor1', c_module))
S3DVertex2TCoords_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('S3DVertex2TCoords_ctor2', c_module))
S3DVertex2TCoords_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertex2TCoords_ctor3', c_module))
S3DVertex2TCoords_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertex2TCoords_ctor4', c_module))
S3DVertex2TCoords_ctor5 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('S3DVertex2TCoords_ctor5', c_module))
S3DVertex2TCoords_ctor6 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('S3DVertex2TCoords_ctor6', c_module))
S3DVertex2TCoords_ctor7 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertex2TCoords_ctor7', c_module))
S3DVertex2TCoords_ctor8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('S3DVertex2TCoords_ctor8', c_module))
S3DVertex2TCoords_get_TCoords2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex2TCoords_get_TCoords2', c_module))
S3DVertex2TCoords_set_TCoords2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertex2TCoords_set_TCoords2', c_module))

#struct S3DVertexTangents : public S3DVertex
S3DVertexTangents_ctor1 = func_type(ctypes.c_void_p, ctypes.c_int)(('S3DVertexTangents_ctor1', c_module))
S3DVertexTangents_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('S3DVertexTangents_ctor2', c_module))
S3DVertexTangents_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertexTangents_ctor3', c_module))
S3DVertexTangents_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('S3DVertexTangents_ctor4', c_module))
S3DVertexTangents_get_Tangent = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertexTangents_get_Tangent', c_module))
S3DVertexTangents_set_Tangent = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertexTangents_set_Tangent', c_module))
S3DVertexTangents_get_Binormal = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertexTangents_get_Binormal', c_module))
S3DVertexTangents_set_Binormal = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('S3DVertexTangents_set_Binormal', c_module))

# functions for class SColor
SColor_ctor1 = func_type(ctypes.c_void_p)(('SColor_ctor1', c_module))
SColor_ctor2 = func_type(ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)(('SColor_ctor2', c_module))
SColor_ctor3 = func_type(ctypes.c_void_p, ctypes.c_uint)(('SColor_ctor3', c_module))
SColor_delete = func_type(None, ctypes.c_void_p)(('SColor_delete', c_module))
SColor_getAlpha = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_getAlpha', c_module))
SColor_getRed = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_getRed', c_module))
SColor_getGreen = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_getGreen', c_module))
SColor_getBlue = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_getBlue', c_module))
SColor_getLuminance = func_type(ctypes.c_float, ctypes.c_void_p)(('SColor_getLuminance', c_module))
SColor_getAverage = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_getAverage', c_module))
SColor_setAlpha = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SColor_setAlpha', c_module))
SColor_setRed = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SColor_setRed', c_module))
SColor_setGreen = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SColor_setGreen', c_module))
SColor_setBlue = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SColor_setBlue', c_module))
SColor_toA1R5G5B5 = func_type(ctypes.c_ushort, ctypes.c_void_p)(('SColor_toA1R5G5B5', c_module))
SColor_toOpenGLColor = func_type(None, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ubyte))(('SColor_toOpenGLColor', c_module))
SColor_set = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint)(('SColor_set', c_module))
SColor_set2 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SColor_set2', c_module))
SColor_operator_equal = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SColor_operator_equal', c_module))
SColor_operator_notequal = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SColor_operator_notequal', c_module))
SColor_operator_less = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SColor_operator_less', c_module))
SColor_operator_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SColor_operator_add', c_module))
SColor_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('SColor_getInterpolated', c_module))
SColor_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('SColor_getInterpolated_quadratic', c_module))
SColor_color = func_type(ctypes.c_uint, ctypes.c_void_p)(('SColor_color', c_module))

# functions for class SColorf
SColorf_ctor1 = func_type(ctypes.c_void_p)(('SColorf_ctor1', c_module))
SColorf_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('SColorf_ctor2', c_module))
SColorf_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SColorf_ctor3', c_module))
SColorf_delete = func_type(None, ctypes.c_void_p)(('SColorf_delete', c_module))
SColorf_toSColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SColorf_toSColor', c_module))
SColorf_set1 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('SColorf_set1', c_module))
SColorf_set2 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('SColorf_set2', c_module))
SColorf_getInterpolated = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('SColorf_getInterpolated', c_module))
SColorf_getInterpolated_quadratic = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('SColorf_getInterpolated_quadratic', c_module))
SColorf_setColorComponentValue = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_float)(('SColorf_setColorComponentValue', c_module))
SColorf_getAlpha = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorf_getAlpha', c_module))
SColorf_getRed = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorf_getRed', c_module))
SColorf_getGreen = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorf_getGreen', c_module))
SColorf_getBlue = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorf_getBlue', c_module))
SColorf_setAlpha = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorf_setAlpha', c_module))
SColorf_setRed = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorf_setRed', c_module))
SColorf_setGreen = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorf_setGreen', c_module))
SColorf_setBlue = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorf_setBlue', c_module))

#================= SColorHSL
SColorHSL_ctor = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('SColorHSL_ctor', c_module))
SColorHSL_delete = func_type(None, ctypes.c_void_p)(('SColorHSL_delete', c_module))
SColorHSL_fromRGB = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SColorHSL_fromRGB', c_module))
SColorHSL_toRGB = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SColorHSL_toRGB', c_module))
SColorHSL_get_Hue = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorHSL_get_Hue', c_module))
SColorHSL_get_Saturation = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorHSL_get_Saturation', c_module))
SColorHSL_get_Luminance = func_type(ctypes.c_float, ctypes.c_void_p)(('SColorHSL_get_Luminance', c_module))
SColorHSL_set_Hue = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorHSL_set_Hue', c_module))
SColorHSL_set_Saturation = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorHSL_set_Saturation', c_module))
SColorHSL_set_Luminance = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SColorHSL_set_Luminance', c_module))

# functions for class IReferenceCounted
IReferenceCounted_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IReferenceCounted_ctor', c_module))
#~ IReferenceCounted_Destructor = func_type(None, ctypes.c_void_p)(('IReferenceCounted_Destructor', c_module))
IReferenceCounted_grab = func_type(None, ctypes.c_void_p)(('IReferenceCounted_grab', c_module))
IReferenceCounted_drop = func_type(ctypes.c_bool, ctypes.c_void_p)(('IReferenceCounted_drop', c_module))
IReferenceCounted_getReferenceCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IReferenceCounted_getReferenceCount', c_module))
IReferenceCounted_getDebugName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IReferenceCounted_getDebugName', c_module))
IReferenceCounted_is_null = func_type(ctypes.c_bool, ctypes.c_void_p)(('IReferenceCounted_is_null', c_module))

# functions for class IAttributes
IAttributes_getAttributeCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IAttributes_getAttributeCount', c_module))
IAttributes_getAttributeName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeName', c_module))
IAttributes_getAttributeType1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeType1', c_module))
IAttributes_getAttributeType2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeType2', c_module))
IAttributes_getAttributeTypeString1 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeTypeString1', c_module))
IAttributes_getAttributeTypeString2 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeTypeString2', c_module))
IAttributes_existsAttribute = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_existsAttribute', c_module))
IAttributes_findAttribute = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_findAttribute', c_module))
IAttributes_clear = func_type(None, ctypes.c_void_p)(('IAttributes_clear', c_module))
IAttributes_read = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p)(('IAttributes_read', c_module))
IAttributes_write = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p)(('IAttributes_write', c_module))
IAttributes_addInt = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)(('IAttributes_addInt', c_module))
IAttributes_setAttribute1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)(('IAttributes_setAttribute1', c_module))
IAttributes_setAttribute2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IAttributes_setAttribute2', c_module))
IAttributes_setAttribute3 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float)(('IAttributes_setAttribute3', c_module))
IAttributes_setAttribute4 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_float)(('IAttributes_setAttribute4', c_module))
IAttributes_setAttribute5 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('IAttributes_setAttribute5', c_module))
IAttributes_setAttribute6 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p)(('IAttributes_setAttribute6', c_module))
IAttributes_setAttribute7 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_wchar_p)(('IAttributes_setAttribute7', c_module))
IAttributes_setAttribute8 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IAttributes_setAttribute8', c_module))
IAttributes_setAttribute9 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_setAttribute9', c_module))
IAttributes_setAttribute10 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IAttributes_setAttribute10', c_module))
IAttributes_setAttribute11 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute11', c_module))
IAttributes_setAttribute12 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute12', c_module))
IAttributes_setAttribute13 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool)(('IAttributes_setAttribute13', c_module))
IAttributes_setAttribute14 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IAttributes_setAttribute14', c_module))
IAttributes_setAttribute15 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute15', c_module))
IAttributes_setAttribute16 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute16', c_module))
IAttributes_setAttribute17 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute17', c_module))
IAttributes_setAttribute18 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute18', c_module))
IAttributes_setAttribute19 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute19', c_module))
IAttributes_setAttribute20 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute20', c_module))
IAttributes_setAttribute21 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute21', c_module))
IAttributes_setAttribute22 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute22', c_module))
IAttributes_setAttribute23 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute23', c_module))
IAttributes_setAttribute24 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute24', c_module))
IAttributes_setAttribute25 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute25', c_module))
IAttributes_setAttribute26 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute26', c_module))
IAttributes_setAttribute27 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute27', c_module))
IAttributes_setAttribute28 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute28', c_module))
IAttributes_setAttribute29 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute29', c_module))
IAttributes_setAttribute30 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute30', c_module))
IAttributes_setAttribute31 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute31', c_module))
IAttributes_setAttribute32 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute32', c_module))
IAttributes_setAttribute33 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute33', c_module))
IAttributes_setAttribute34 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute34', c_module))
IAttributes_setAttribute35 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute35', c_module))
IAttributes_setAttribute36 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute36', c_module))
IAttributes_setAttribute37 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute37', c_module))
IAttributes_setAttribute38 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute38', c_module))
IAttributes_setAttribute39 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute39', c_module))
IAttributes_setAttribute40 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute40', c_module))
IAttributes_setAttribute41 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute41', c_module))
IAttributes_setAttribute42 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute42', c_module))
IAttributes_setAttribute43 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_setAttribute43', c_module))
IAttributes_setAttribute44 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_setAttribute44', c_module))
IAttributes_getAttributeAsInt1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsInt1', c_module))
IAttributes_getAttributeAsInt2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsInt2', c_module))
IAttributes_addFloat = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_float)(('IAttributes_addFloat', c_module))
IAttributes_getAttributeAsFloat1 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsFloat1', c_module))
IAttributes_getAttributeAsFloat2 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsFloat2', c_module))
IAttributes_addString1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('IAttributes_addString1', c_module))
IAttributes_addString2 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_wchar_p)(('IAttributes_addString2', c_module))
IAttributes_getAttributeAsString1 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsString1', c_module))
IAttributes_getAttributeAsString2 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsString2', c_module))
IAttributes_getAttributeAsString3 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('IAttributes_getAttributeAsString3', c_module))
IAttributes_getAttributeAsStringW1 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsStringW1', c_module))
IAttributes_getAttributeAsStringW2 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsStringW2', c_module))
IAttributes_getAttributeAsStringW3 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_wchar_p)(('IAttributes_getAttributeAsStringW3', c_module))
IAttributes_addBinary1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_addBinary1', c_module))
IAttributes_addArray2 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addArray2', c_module))
IAttributes_getAttributeAsBinaryData1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsBinaryData1', c_module))
IAttributes_getAttributeAsBinaryData2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsBinaryData2', c_module))
IAttributes_getAttributeAsArray1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsArray1', c_module))
IAttributes_getAttributeAsArray2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsArray2', c_module))
IAttributes_addBool = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool)(('IAttributes_addBool', c_module))
IAttributes_getAttributeAsBool1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsBool1', c_module))
IAttributes_getAttributeAsBool2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsBool2', c_module))
IAttributes_addEnum1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addEnum1', c_module))
IAttributes_addEnum2 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_addEnum2', c_module))
IAttributes_getAttributeAsEnumeration1 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsEnumeration1', c_module))
IAttributes_getAttributeAsEnumeration2 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsEnumeration2', c_module))
IAttributes_getAttributeAsEnumeration3 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_getAttributeAsEnumeration3', c_module))
IAttributes_getAttributeAsEnumeration4 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_getAttributeAsEnumeration4', c_module))
IAttributes_getAttributeEnumerationLiteralsOfEnumeration1 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_getAttributeEnumerationLiteralsOfEnumeration1', c_module))
IAttributes_getAttributeEnumerationLiteralsOfEnumeration2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IAttributes_getAttributeEnumerationLiteralsOfEnumeration2', c_module))
IAttributes_addColor = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addColor', c_module))
IAttributes_getAttributeAsColor1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsColor1', c_module))
IAttributes_getAttributeAsColor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsColor2', c_module))
IAttributes_addColorf = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addColorf', c_module))
IAttributes_getAttributeAsColorf1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsColorf1', c_module))
IAttributes_getAttributeAsColorf2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsColorf2', c_module))
IAttributes_addVector3d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addVector3d', c_module))
IAttributes_getAttributeAsVector3d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsVector3d1', c_module))
IAttributes_getAttributeAsVector3d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsVector3d2', c_module))
IAttributes_addPosition2d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addPosition2d', c_module))
IAttributes_getAttributeAsPosition2d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsPosition2d1', c_module))
IAttributes_getAttributeAsPosition2d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsPosition2d2', c_module))
IAttributes_addRect = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addRect', c_module))
IAttributes_getAttributeAsRect1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsRect1', c_module))
IAttributes_getAttributeAsRect2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsRect2', c_module))
IAttributes_addMatrix = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addMatrix', c_module))
IAttributes_getAttributeAsMatrix1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsMatrix1', c_module))
IAttributes_getAttributeAsMatrix2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsMatrix2', c_module))
IAttributes_addQuaternion = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addQuaternion', c_module))
IAttributes_getAttributeAsQuaternion1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsQuaternion1', c_module))
IAttributes_getAttributeAsQuaternion2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsQuaternion2', c_module))
IAttributes_addBox3d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addBox3d', c_module))
IAttributes_getAttributeAsBox3d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsBox3d1', c_module))
IAttributes_getAttributeAsBox3d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsBox3d2', c_module))
IAttributes_addPlane3d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addPlane3d', c_module))
IAttributes_getAttributeAsPlane3d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsPlane3d1', c_module))
IAttributes_getAttributeAsPlane3d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsPlane3d2', c_module))
IAttributes_addTriangle3d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addTriangle3d', c_module))
IAttributes_getAttributeAsTriangle3d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsTriangle3d1', c_module))
IAttributes_getAttributeAsTriangle3d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsTriangle3d2', c_module))
IAttributes_addLine2d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addLine2d', c_module))
IAttributes_getAttributeAsLine2d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsLine2d1', c_module))
IAttributes_getAttributeAsLine2d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsLine2d2', c_module))
IAttributes_addLine3d = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addLine3d', c_module))
IAttributes_getAttributeAsLine3d1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsLine3d1', c_module))
IAttributes_getAttributeAsLine3d2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsLine3d2', c_module))
IAttributes_addTexture = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addTexture', c_module))
IAttributes_getAttributeAsTexture1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsTexture1', c_module))
IAttributes_getAttributeAsTexture2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsTexture2', c_module))
IAttributes_addUserPointer = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IAttributes_addUserPointer', c_module))
IAttributes_getAttributeAsUserPointer1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAttributes_getAttributeAsUserPointer1', c_module))
IAttributes_getAttributeAsUserPointer2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IAttributes_getAttributeAsUserPointer2', c_module))

#class IBoneSceneNode : public ISceneNode
IBoneSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_ctor', c_module))
if IRRLICHT_VERSION < 180:
	IBoneSceneNode_getBoneName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IBoneSceneNode_getBoneName', c_module))
IBoneSceneNode_getBoneIndex = func_type(ctypes.c_uint, ctypes.c_void_p)(('IBoneSceneNode_getBoneIndex', c_module))
IBoneSceneNode_setAnimationMode = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_setAnimationMode', c_module))
IBoneSceneNode_getAnimationMode = func_type(ctypes.c_int, ctypes.c_void_p)(('IBoneSceneNode_getAnimationMode', c_module))
IBoneSceneNode_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IBoneSceneNode_getBoundingBox', c_module))
IBoneSceneNode_OnAnimate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IBoneSceneNode_OnAnimate', c_module))
IBoneSceneNode_render = func_type(None, ctypes.c_void_p)(('IBoneSceneNode_render', c_module))
IBoneSceneNode_setSkinningSpace = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_setSkinningSpace', c_module))
IBoneSceneNode_getSkinningSpace = func_type(ctypes.c_int, ctypes.c_void_p)(('IBoneSceneNode_getSkinningSpace', c_module))
IBoneSceneNode_updateAbsolutePositionOfAllChildren = func_type(None, ctypes.c_void_p)(('IBoneSceneNode_updateAbsolutePositionOfAllChildren', c_module))
IBoneSceneNode_set_positionHint = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_set_positionHint', c_module))
IBoneSceneNode_get_positionHint = func_type(ctypes.c_int, ctypes.c_void_p)(('IBoneSceneNode_get_positionHint', c_module))
IBoneSceneNode_set_scaleHint = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_set_scaleHint', c_module))
IBoneSceneNode_get_scaleHint = func_type(ctypes.c_int, ctypes.c_void_p)(('IBoneSceneNode_get_scaleHint', c_module))
IBoneSceneNode_set_rotationHint = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IBoneSceneNode_set_rotationHint', c_module))
IBoneSceneNode_get_rotationHint = func_type(ctypes.c_int, ctypes.c_void_p)(('IBoneSceneNode_get_rotationHint', c_module))

#================= IDynamicMeshBuffer
IDynamicMeshBuffer_getVertexBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getVertexBuffer', c_module))
IDynamicMeshBuffer_getIndexBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getIndexBuffer', c_module))
IDynamicMeshBuffer_setVertexBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_setVertexBuffer', c_module))
IDynamicMeshBuffer_setIndexBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_setIndexBuffer', c_module))
IDynamicMeshBuffer_getMaterial1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getMaterial1', c_module))
IDynamicMeshBuffer_getMaterial2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getMaterial2', c_module))
IDynamicMeshBuffer_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getBoundingBox', c_module))
IDynamicMeshBuffer_setBoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_setBoundingBox', c_module))
IDynamicMeshBuffer_recalculateBoundingBox = func_type(None, ctypes.c_void_p)(('IDynamicMeshBuffer_recalculateBoundingBox', c_module))
IDynamicMeshBuffer_append1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_append1', c_module))
IDynamicMeshBuffer_append2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_append2', c_module))
IDynamicMeshBuffer_getHardwareMappingHint_Vertex = func_type(ctypes.c_int, ctypes.c_void_p)(('IDynamicMeshBuffer_getHardwareMappingHint_Vertex', c_module))
IDynamicMeshBuffer_getHardwareMappingHint_Index = func_type(ctypes.c_int, ctypes.c_void_p)(('IDynamicMeshBuffer_getHardwareMappingHint_Index', c_module))
IDynamicMeshBuffer_setHardwareMappingHint = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IDynamicMeshBuffer_setHardwareMappingHint', c_module))
IDynamicMeshBuffer_setDirty = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IDynamicMeshBuffer_setDirty', c_module))
IDynamicMeshBuffer_getChangedID_Vertex = func_type(ctypes.c_uint, ctypes.c_void_p)(('IDynamicMeshBuffer_getChangedID_Vertex', c_module))
IDynamicMeshBuffer_getChangedID_Index = func_type(ctypes.c_uint, ctypes.c_void_p)(('IDynamicMeshBuffer_getChangedID_Index', c_module))
IDynamicMeshBuffer_getVertexType = func_type(ctypes.c_int, ctypes.c_void_p)(('IDynamicMeshBuffer_getVertexType', c_module))
IDynamicMeshBuffer_getVertices1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getVertices1', c_module))
IDynamicMeshBuffer_getVertices2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getVertices2', c_module))
IDynamicMeshBuffer_getVertexCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IDynamicMeshBuffer_getVertexCount', c_module))
IDynamicMeshBuffer_getIndexType = func_type(ctypes.c_int, ctypes.c_void_p)(('IDynamicMeshBuffer_getIndexType', c_module))
IDynamicMeshBuffer_getIndices1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getIndices1', c_module))
IDynamicMeshBuffer_getIndices2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IDynamicMeshBuffer_getIndices2', c_module))
IDynamicMeshBuffer_getIndexCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IDynamicMeshBuffer_getIndexCount', c_module))
IDynamicMeshBuffer_getPosition1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getPosition1', c_module))
IDynamicMeshBuffer_getPosition2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getPosition2', c_module))
IDynamicMeshBuffer_getTCoords1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getTCoords1', c_module))
IDynamicMeshBuffer_getTCoords2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getTCoords2', c_module))
IDynamicMeshBuffer_getNormal1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getNormal1', c_module))
IDynamicMeshBuffer_getNormal2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IDynamicMeshBuffer_getNormal2', c_module))

# functions for class IDummyTransformationSceneNode
IDummyTransformationSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IDummyTransformationSceneNode_ctor', c_module))
IDummyTransformationSceneNode_getRelativeTransformationMatrix = func_type(ctypes.c_void_p)(('IDummyTransformationSceneNode_getRelativeTransformationMatrix', c_module))

#================= IFileArchive
IFileArchive_createAndOpenFile1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IFileArchive_createAndOpenFile1', c_module))
IFileArchive_createAndOpenFile2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IFileArchive_createAndOpenFile2', c_module))
IFileArchive_getFileList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IFileArchive_getFileList', c_module))
IFileArchive_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IFileArchive_getType', c_module))
IFileArchive_get_Password = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IFileArchive_get_Password', c_module))
IFileArchive_set_Password = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('IFileArchive_set_Password', c_module))

#================= IArchiveLoader
IArchiveLoader_isALoadableFileFormat1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)(('IArchiveLoader_isALoadableFileFormat1', c_module))
IArchiveLoader_isALoadableFileFormat2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IArchiveLoader_isALoadableFileFormat2', c_module))
IArchiveLoader_isALoadableFileFormat3 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IArchiveLoader_isALoadableFileFormat3', c_module))
IArchiveLoader_createArchive1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_bool)(('IArchiveLoader_createArchive1', c_module))
IArchiveLoader_createArchive2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('IArchiveLoader_createArchive2', c_module))

#================= IFileList
IFileList_getFileCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IFileList_getFileCount', c_module))
IFileList_getFileSize = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IFileList_getFileSize', c_module))
IFileList_getID = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IFileList_getID', c_module))
IFileList_isDirectory = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('IFileList_isDirectory', c_module))
IFileList_sort = func_type(None, ctypes.c_void_p)(('IFileList_sort', c_module))

IFileList_getFileName = func_type(fschar_t, ctypes.c_void_p, ctypes.c_uint)(('IFileList_getFileName', c_module))
IFileList_getFullFileName = func_type(fschar_t, ctypes.c_void_p, ctypes.c_uint)(('IFileList_getFullFileName', c_module))
IFileList_findFile = func_type(ctypes.c_int, ctypes.c_void_p, fschar_t, ctypes.c_bool)(('IFileList_findFile', c_module))
IFileList_getPath = func_type(fschar_t, ctypes.c_void_p)(('IFileList_getPath', c_module))
if IRRLICHT_VERSION < 180:
	IFileList_addItem = func_type(ctypes.c_uint, ctypes.c_void_p, fschar_t, ctypes.c_uint, ctypes.c_bool, ctypes.c_uint)(('IFileList_addItem', c_module))
else:
	IFileList_addItem = func_type(ctypes.c_uint, ctypes.c_void_p, fschar_t, ctypes.c_uint, ctypes.c_uint, ctypes.c_bool, ctypes.c_uint)(('IFileList_addItem', c_module))

# functions for class IImage
IImage_lock = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IImage_lock', c_module))
IImage_unlock = func_type(None, ctypes.c_void_p)(('IImage_unlock', c_module))
IImage_getDimension = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IImage_getDimension', c_module))
IImage_getBitsPerPixel = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getBitsPerPixel', c_module))
IImage_getBytesPerPixel = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getBytesPerPixel', c_module))
IImage_getImageDataSizeInBytes = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getImageDataSizeInBytes', c_module))
IImage_getImageDataSizeInPixels = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getImageDataSizeInPixels', c_module))
IImage_getPixel = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IImage_getPixel', c_module))
IImage_setPixel = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_bool)(('IImage_setPixel', c_module))
IImage_getColorFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IImage_getColorFormat', c_module))
IImage_getRedMask = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getRedMask', c_module))
IImage_getGreenMask = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getGreenMask', c_module))
IImage_getBlueMask = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getBlueMask', c_module))
IImage_getAlphaMask = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getAlphaMask', c_module))
IImage_getPitch = func_type(ctypes.c_uint, ctypes.c_void_p)(('IImage_getPitch', c_module))
IImage_copyToScaling1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_uint)(('IImage_copyToScaling1', c_module))
IImage_copyToScaling2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IImage_copyToScaling2', c_module))
IImage_copyTo1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IImage_copyTo1', c_module))
IImage_copyTo2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IImage_copyTo2', c_module))
IImage_copyToWithAlpha = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IImage_copyToWithAlpha', c_module))
IImage_copyToScalingBoxFilter = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IImage_copyToScalingBoxFilter', c_module))
IImage_fill = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IImage_fill', c_module))
IImage_getBitsPerPixelFromFormat = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_int)(('IImage_getBitsPerPixelFromFormat', c_module))
IImage_isRenderTargetOnlyFormat = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IImage_isRenderTargetOnlyFormat', c_module))

#===== IImageLoader
IImageLoader_isALoadableFileExtension = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IImageLoader_isALoadableFileExtension', c_module))
IImageLoader_isALoadableFileFormat = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IImageLoader_isALoadableFileFormat', c_module))
IImageLoader_loadImage = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IImageLoader_loadImage', c_module))

#=== IImageWriter
IImageWriter_isAWriteableFileExtension = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IImageWriter_isAWriteableFileExtension', c_module))
IImageWriter_writeImage = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IImageWriter_writeImage', c_module))

# functions for class ITriangleSelector
#~ ITriangleSelector_Destructor = func_type(None, ctypes.c_void_p)(('ITriangleSelector_Destructor', c_module))
ITriangleSelector_getTriangleCount = func_type(ctypes.c_int, ctypes.c_void_p)(('ITriangleSelector_getTriangleCount', c_module))
ITriangleSelector_getTriangles = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)(('ITriangleSelector_getTriangles', c_module))
ITriangleSelector_getTriangles2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('ITriangleSelector_getTriangles2', c_module))
ITriangleSelector_getTriangles3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('ITriangleSelector_getTriangles3', c_module))
ITriangleSelector_getSceneNodeForTriangle = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ITriangleSelector_getSceneNodeForTriangle', c_module))

# functions for class IMetaTriangleSelector
IMetaTriangleSelector_addTriangleSelector = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMetaTriangleSelector_addTriangleSelector', c_module))
IMetaTriangleSelector_removeTriangleSelector = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IMetaTriangleSelector_removeTriangleSelector', c_module))
IMetaTriangleSelector_removeAllTriangleSelectors = func_type(None, ctypes.c_void_p)(('IMetaTriangleSelector_removeAllTriangleSelectors', c_module))

# functions for class IAttributeExchangingObject
IAttributeExchangingObject_serializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(SAttributeReadWriteOptions))(('IAttributeExchangingObject_serializeAttributes', c_module))
IAttributeExchangingObject_deserializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(SAttributeReadWriteOptions))(('IAttributeExchangingObject_deserializeAttributes', c_module))

# functions for class listIGUIElementIterator
listIGUIElementIterator_ctor = func_type(ctypes.c_void_p)(('listIGUIElementIterator_ctor', c_module))
listIGUIElementIterator_delete = func_type(None, ctypes.c_void_p)(('listIGUIElementIterator_delete', c_module))
listIGUIElementIterator_operator_next = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElementIterator_operator_next', c_module))
listIGUIElementIterator_operator_prev = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElementIterator_operator_prev', c_module))
listIGUIElementIterator_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElementIterator_operator_eq', c_module))
listIGUIElementIterator_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElementIterator_operator_ne', c_module))
listIGUIElementIterator_operator_add_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('listIGUIElementIterator_operator_add_set', c_module))
listIGUIElementIterator_operator_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('listIGUIElementIterator_operator_add', c_module))
listIGUIElementIterator_operator_sub = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('listIGUIElementIterator_operator_sub', c_module))

# functions for class listIGUIElement
listIGUIElement_ctor1 = func_type(ctypes.c_void_p)(('listIGUIElement_ctor1', c_module))
listIGUIElement_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_ctor2', c_module))
listIGUIElement_delete = func_type(None, ctypes.c_void_p)(('listIGUIElement_delete', c_module))
listIGUIElement_operator_set = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_operator_set', c_module))
listIGUIElement_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('listIGUIElement_size', c_module))
listIGUIElement_getSize = func_type(ctypes.c_uint, ctypes.c_void_p)(('listIGUIElement_getSize', c_module))
listIGUIElement_clear = func_type(None, ctypes.c_void_p)(('listIGUIElement_clear', c_module))
listIGUIElement_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('listIGUIElement_empty', c_module))
listIGUIElement_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_push_back', c_module))
listIGUIElement_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_push_front', c_module))
listIGUIElement_begin = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_begin', c_module))
listIGUIElement_end = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_end', c_module))
listIGUIElement_getLast = func_type(ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_getLast', c_module))
listIGUIElement_insert_after = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_insert_after', c_module))
listIGUIElement_insert_before = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_insert_before', c_module))
listIGUIElement_erase = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_erase', c_module))
listIGUIElement_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('listIGUIElement_swap', c_module))

# functions for class IGUIButton
IGUIButton_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIButton_ctor', c_module))
IGUIButton_setOverrideFont = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setOverrideFont', c_module))
IGUIButton_setImage1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setImage1', c_module))
IGUIButton_setImage2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setImage2', c_module))
IGUIButton_setPressedImage1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setPressedImage1', c_module))
IGUIButton_setPressedImage2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setPressedImage2', c_module))
IGUIButton_setSpriteBank = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIButton_setSpriteBank', c_module))
IGUIButton_setSprite = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setSprite', c_module))
IGUIButton_setIsPushButton = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setIsPushButton', c_module))
IGUIButton_setPressed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setPressed', c_module))
IGUIButton_isPressed = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIButton_isPressed', c_module))
IGUIButton_setUseAlphaChannel = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setUseAlphaChannel', c_module))
IGUIButton_isAlphaChannelUsed = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIButton_isAlphaChannelUsed', c_module))
IGUIButton_isPushButton = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIButton_isPushButton', c_module))
IGUIButton_setDrawBorder = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setDrawBorder', c_module))
IGUIButton_isDrawingBorder = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIButton_isDrawingBorder', c_module))
IGUIButton_setScaleImage = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIButton_setScaleImage', c_module))
IGUIButton_isScalingImage = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIButton_isScalingImage', c_module))

# functions for class IGUICheckBox
IGUICheckBox_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUICheckBox_ctor', c_module))
IGUICheckBox_delete = func_type(None, ctypes.c_void_p)(('IGUICheckBox_delete', c_module))
IGUICheckBox_setChecked = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUICheckBox_setChecked', c_module))
IGUICheckBox_isChecked = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUICheckBox_isChecked', c_module))

# functions for class IGUIColorSelectDialog
IGUIColorSelectDialog_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIColorSelectDialog_ctor', c_module))
IGUIColorSelectDialog_delete = func_type(None, ctypes.c_void_p)(('IGUIColorSelectDialog_delete', c_module))

# functions for class IGUIComboBox
IGUIComboBox_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIComboBox_ctor', c_module))
IGUIComboBox_getItemCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUIComboBox_getItemCount', c_module))
IGUIComboBox_getItem = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint)(('IGUIComboBox_getItem', c_module))
IGUIComboBox_getItemData = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IGUIComboBox_getItemData', c_module))
IGUIComboBox_getIndexForItemData = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)(('IGUIComboBox_getIndexForItemData', c_module))
IGUIComboBox_addItem = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p)(('IGUIComboBox_addItem', c_module))
IGUIComboBox_removeItem = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIComboBox_removeItem', c_module))
IGUIComboBox_clear = func_type(None, ctypes.c_void_p)(('IGUIComboBox_clear', c_module))
IGUIComboBox_getSelected = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIComboBox_getSelected', c_module))
IGUIComboBox_setSelected = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIComboBox_setSelected', c_module))
IGUIComboBox_setTextAlignment = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUIComboBox_setTextAlignment', c_module))

# functions for class IGUIContextMenu
IGUIContextMenu_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIContextMenu_ctor', c_module))
IGUIContextMenu_setCloseHandling = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIContextMenu_setCloseHandling', c_module))
IGUIContextMenu_getCloseHandling = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIContextMenu_getCloseHandling', c_module))
IGUIContextMenu_getItemCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUIContextMenu_getItemCount', c_module))
IGUIContextMenu_addItem = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IGUIContextMenu_addItem', c_module))
IGUIContextMenu_insertItem = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IGUIContextMenu_insertItem', c_module))
IGUIContextMenu_findItemWithCommandId = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint)(('IGUIContextMenu_findItemWithCommandId', c_module))
IGUIContextMenu_addSeparator = func_type(None, ctypes.c_void_p)(('IGUIContextMenu_addSeparator', c_module))
IGUIContextMenu_getItemText = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_getItemText', c_module))
IGUIContextMenu_setItemText = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p)(('IGUIContextMenu_setItemText', c_module))
IGUIContextMenu_isItemEnabled = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_isItemEnabled', c_module))
IGUIContextMenu_setItemEnabled = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('IGUIContextMenu_setItemEnabled', c_module))
IGUIContextMenu_setItemChecked = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('IGUIContextMenu_setItemChecked', c_module))
IGUIContextMenu_isItemChecked = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_isItemChecked', c_module))
IGUIContextMenu_removeItem = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_removeItem', c_module))
IGUIContextMenu_removeAllItems = func_type(None, ctypes.c_void_p)(('IGUIContextMenu_removeAllItems', c_module))
IGUIContextMenu_getSelectedItem = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIContextMenu_getSelectedItem', c_module))
IGUIContextMenu_getItemCommandId = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_getItemCommandId', c_module))
IGUIContextMenu_setItemCommandId = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IGUIContextMenu_setItemCommandId', c_module))
IGUIContextMenu_getSubMenu = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_getSubMenu', c_module))
IGUIContextMenu_setItemAutoChecking = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('IGUIContextMenu_setItemAutoChecking', c_module))
IGUIContextMenu_getItemAutoChecking = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint)(('IGUIContextMenu_getItemAutoChecking', c_module))
IGUIContextMenu_setEventParent = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIContextMenu_setEventParent', c_module))

# functions for class IGUIEditBox
IGUIEditBox_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIEditBox_ctor', c_module))
IGUIEditBox_setOverrideFont = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEditBox_setOverrideFont', c_module))
IGUIEditBox_setOverrideColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEditBox_setOverrideColor', c_module))
IGUIEditBox_enableOverrideColor = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIEditBox_enableOverrideColor', c_module))
IGUIEditBox_setDrawBorder = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIEditBox_setDrawBorder', c_module))
IGUIEditBox_setTextAlignment = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUIEditBox_setTextAlignment', c_module))
IGUIEditBox_setWordWrap = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIEditBox_setWordWrap', c_module))
IGUIEditBox_isWordWrapEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIEditBox_isWordWrapEnabled', c_module))
IGUIEditBox_setMultiLine = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIEditBox_setMultiLine', c_module))
IGUIEditBox_isMultiLineEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIEditBox_isMultiLineEnabled', c_module))
IGUIEditBox_setAutoScroll = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIEditBox_setAutoScroll', c_module))
IGUIEditBox_isAutoScrollEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIEditBox_isAutoScrollEnabled', c_module))
IGUIEditBox_setPasswordBox = func_type(None, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p)(('IGUIEditBox_setPasswordBox', c_module))
IGUIEditBox_isPasswordBox = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIEditBox_isPasswordBox', c_module))
IGUIEditBox_getTextDimension = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEditBox_getTextDimension', c_module))
IGUIEditBox_setMax = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIEditBox_setMax', c_module))
IGUIEditBox_getMax = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUIEditBox_getMax', c_module))

# functions for class IGUIElement
IGUIElement_ctor = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIElement_ctor', c_module))
IGUIElement_delete = func_type(None, ctypes.c_void_p)(('IGUIElement_delete', c_module))
IGUIElement_getParent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getParent', c_module))
IGUIElement_getRelativePosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getRelativePosition', c_module))
IGUIElement_setRelativePosition1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_setRelativePosition1', c_module))
IGUIElement_setRelativePosition2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_setRelativePosition2', c_module))
IGUIElement_setRelativePositionProportional = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_setRelativePositionProportional', c_module))
IGUIElement_getAbsolutePosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getAbsolutePosition', c_module))
IGUIElement_getAbsoluteClippingRect = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getAbsoluteClippingRect', c_module))
IGUIElement_setNotClipped = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setNotClipped', c_module))
IGUIElement_isNotClipped = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isNotClipped', c_module))
IGUIElement_setMaxSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_setMaxSize', c_module))
IGUIElement_setMinSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_setMinSize', c_module))
IGUIElement_setAlignment = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IGUIElement_setAlignment', c_module))
IGUIElement_updateAbsolutePosition = func_type(None, ctypes.c_void_p)(('IGUIElement_updateAbsolutePosition', c_module))
IGUIElement_getElementFromPoint = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getElementFromPoint', c_module))
IGUIElement_isPointInside = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_isPointInside', c_module))
IGUIElement_addChild = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_addChild', c_module))
IGUIElement_removeChild = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_removeChild', c_module))
IGUIElement_remove = func_type(None, ctypes.c_void_p)(('IGUIElement_remove', c_module))
IGUIElement_draw = func_type(None, ctypes.c_void_p)(('IGUIElement_draw', c_module))
IGUIElement_OnPostRender = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIElement_OnPostRender', c_module))
IGUIElement_move = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_move', c_module))
IGUIElement_isVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isVisible', c_module))
IGUIElement_setVisible = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setVisible', c_module))
IGUIElement_isSubElement = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isSubElement', c_module))
IGUIElement_setSubElement = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setSubElement', c_module))
IGUIElement_setTabStop = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setTabStop', c_module))
IGUIElement_isTabStop = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isTabStop', c_module))
IGUIElement_setTabOrder = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIElement_setTabOrder', c_module))
IGUIElement_getTabOrder = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIElement_getTabOrder', c_module))
IGUIElement_setTabGroup = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setTabGroup', c_module))
IGUIElement_isTabGroup = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isTabGroup', c_module))
IGUIElement_getTabGroup = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getTabGroup', c_module))
IGUIElement_isEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIElement_isEnabled', c_module))
IGUIElement_setEnabled = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_setEnabled', c_module))
IGUIElement_setText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIElement_setText', c_module))
IGUIElement_getText = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IGUIElement_getText', c_module))
IGUIElement_setToolTipText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIElement_setToolTipText', c_module))
IGUIElement_getToolTipText = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IGUIElement_getToolTipText', c_module))
IGUIElement_getID = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIElement_getID', c_module))
IGUIElement_setID = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIElement_setID', c_module))
IGUIElement_bringToFront = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_bringToFront', c_module))
IGUIElement_getChildren = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_getChildren', c_module))
IGUIElement_getElementFromId = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IGUIElement_getElementFromId', c_module))
IGUIElement_isMyChild = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_isMyChild', c_module))
IGUIElement_getNextElement = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IGUIElement_getNextElement', c_module))
IGUIElement_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIElement_getType', c_module))
IGUIElement_hasType = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUIElement_hasType', c_module))
IGUIElement_getTypeName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IGUIElement_getTypeName', c_module))
IGUIElement_serializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_serializeAttributes', c_module))
IGUIElement_deserializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_deserializeAttributes', c_module))
#extended methods for compatibility with swig project
IGUIElement_as_IGUIButton = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIButton', c_module))
IGUIElement_as_IGUICheckBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUICheckBox', c_module))
IGUIElement_as_IGUIColorSelectDialog = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIColorSelectDialog', c_module))
IGUIElement_as_IGUIComboBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIComboBox', c_module))
IGUIElement_as_IGUIContextMenu = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIContextMenu', c_module))
IGUIElement_as_IGUIEditBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIEditBox', c_module))
IGUIElement_as_IGUIFileOpenDialog = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIFileOpenDialog', c_module))
IGUIElement_as_IGUIFontBitmap = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIFontBitmap', c_module))
IGUIElement_as_IGUIImage = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIImage', c_module))
IGUIElement_as_IGUIListBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIListBox', c_module))
IGUIElement_as_IGUIMeshViewer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIMeshViewer', c_module))
IGUIElement_as_IGUIScrollBar = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIScrollBar', c_module))
IGUIElement_as_IGUISpinBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUISpinBox', c_module))
IGUIElement_as_IGUIStaticText = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIStaticText', c_module))
IGUIElement_as_IGUITab = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUITab', c_module))
IGUIElement_as_IGUITabControl = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUITabControl', c_module))
IGUIElement_as_IGUITable = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUITable', c_module))
IGUIElement_as_IGUIToolBar = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIToolBar', c_module))
IGUIElement_as_IGUITreeView = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUITreeView', c_module))
IGUIElement_as_IGUIWindow = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIElement_as_IGUIWindow', c_module))

# functions for class IGUIFileOpenDialog
IGUIFileOpenDialog_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIFileOpenDialog_ctor', c_module))
IGUIFileOpenDialog_getFileName = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IGUIFileOpenDialog_getFileName', c_module))
IGUIFileOpenDialog_getDirectoryName = func_type(fschar_t, ctypes.c_void_p)(('IGUIFileOpenDialog_getDirectoryName', c_module))

# functions for class IGUIFontBitmap
IGUIFontBitmap_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIFontBitmap_getType', c_module))
IGUIFontBitmap_getSpriteBank = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIFontBitmap_getSpriteBank', c_module))
IGUIFontBitmap_getSpriteNoFromChar = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_wchar)(('IGUIFontBitmap_getSpriteNoFromChar', c_module))
IGUIFontBitmap_getKerningWidth = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p)(('IGUIFontBitmap_getKerningWidth', c_module))

# functions for class IGUIImage
IGUIImage_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIImage_ctor', c_module))
IGUIImage_setImage = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIImage_setImage', c_module))
IGUIImage_setColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIImage_setColor', c_module))
IGUIImage_setScaleImage = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIImage_setScaleImage', c_module))
IGUIImage_setUseAlphaChannel = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIImage_setUseAlphaChannel', c_module))
IGUIImage_isImageScaled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIImage_isImageScaled', c_module))
IGUIImage_isAlphaChannelUsed = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIImage_isAlphaChannelUsed', c_module))

# functions for class IGUIImageList
IGUIImageList_draw = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUIImageList_draw', c_module))
IGUIImageList_getImageCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIImageList_getImageCount', c_module))
IGUIImageList_getImageSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIImageList_getImageSize', c_module))

# functions for class IGUIInOutFader
IGUIInOutFader_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIInOutFader_ctor', c_module))
IGUIInOutFader_getColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIInOutFader_getColor', c_module))
IGUIInOutFader_setColor1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIInOutFader_setColor1', c_module))
IGUIInOutFader_setColor2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIInOutFader_setColor2', c_module))
IGUIInOutFader_fadeIn = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIInOutFader_fadeIn', c_module))
IGUIInOutFader_fadeOut = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIInOutFader_fadeOut', c_module))
IGUIInOutFader_isReady = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIInOutFader_isReady', c_module))

# functions for class CGUITTFont
CGUITTFont_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_uint)(('CGUITTFont_ctor', c_module))
CGUITTFont_as_IGUIFont = func_type(ctypes.c_void_p, ctypes.c_void_p)(('CGUITTFont_as_IGUIFont', c_module))
CGUITTFont_createTTFont = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_uint)(('CGUITTFont_createTTFont', c_module))
CGUITTFont_setBatchLoadSize = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('CGUITTFont_setBatchLoadSize', c_module))
CGUITTFont_setMaxPageTextureSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGUITTFont_setMaxPageTextureSize', c_module))
CGUITTFont_setTransparency = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('CGUITTFont_setTransparency', c_module))
CGUITTFont_setMonochrome = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('CGUITTFont_setMonochrome', c_module))
CGUITTFont_setFontHinting = func_type(None, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p)(('CGUITTFont_setFontHinting', c_module))
CGUITTFont_draw = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('CGUITTFont_draw', c_module))
CGUITTFont_getDimension1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p)(('CGUITTFont_getDimension1', c_module))
CGUITTFont_getDimension2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_ushort))(('CGUITTFont_getDimension2', c_module))
CGUITTFont_getCharacterFromPos1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('CGUITTFont_getCharacterFromPos1', c_module))
CGUITTFont_getCharacterFromPos2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('CGUITTFont_getCharacterFromPos2', c_module))
CGUITTFont_setKerningWidth = func_type(None, ctypes.c_void_p, ctypes.c_int)(('CGUITTFont_setKerningWidth', c_module))
CGUITTFont_setKerningHeight = func_type(None, ctypes.c_void_p, ctypes.c_int)(('CGUITTFont_setKerningHeight', c_module))
CGUITTFont_getKerningWidth1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p)(('CGUITTFont_getKerningWidth1', c_module))
CGUITTFont_getKerningWidth2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('CGUITTFont_getKerningWidth2', c_module))
CGUITTFont_getKerningHeight = func_type(ctypes.c_int, ctypes.c_void_p)(('CGUITTFont_getKerningHeight', c_module))
CGUITTFont_setInvisibleCharacters1 = func_type(None, ctypes.c_void_p, ctypes.c_wchar)(('CGUITTFont_setInvisibleCharacters1', c_module))
CGUITTFont_setInvisibleCharacters2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CGUITTFont_setInvisibleCharacters2', c_module))
CGUITTFont_forceGlyphUpdate = func_type(None, ctypes.c_void_p)(('CGUITTFont_forceGlyphUpdate', c_module))

#functions for class IGUITab
IGUITab_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUITab_ctor', c_module))
IGUITab_getNumber = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITab_getNumber', c_module))
IGUITab_setDrawBackground = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITab_setDrawBackground', c_module))
IGUITab_setBackgroundColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUITab_setBackgroundColor', c_module))
IGUITab_isDrawingBackground = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITab_isDrawingBackground', c_module))
IGUITab_getBackgroundColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITab_getBackgroundColor', c_module))
IGUITab_setTextColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUITab_setTextColor', c_module))
IGUITab_getTextColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITab_getTextColor', c_module))

#functions for class IGUITabControl
IGUITabControl_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_ctor', c_module))
IGUITabControl_addTab = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('IGUITabControl_addTab', c_module))
IGUITabControl_getTabCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_getTabCount', c_module))
IGUITabControl_getTab = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUITabControl_getTab', c_module))
IGUITabControl_setActiveTab1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUITabControl_setActiveTab1', c_module))
IGUITabControl_setActiveTab2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUITabControl_setActiveTab2', c_module))
IGUITabControl_getActiveTab = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_getActiveTab', c_module))
IGUITabControl_setTabHeight = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUITabControl_setTabHeight', c_module))
IGUITabControl_getTabHeight = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_getTabHeight', c_module))
IGUITabControl_setTabMaxWidth = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUITabControl_setTabMaxWidth', c_module))
IGUITabControl_getTabMaxWidth = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_getTabMaxWidth', c_module))
IGUITabControl_setTabVerticalAlignment = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUITabControl_setTabVerticalAlignment', c_module))
IGUITabControl_getTabVerticalAlignment = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITabControl_getTabVerticalAlignment', c_module))
IGUITabControl_setTabExtraWidth = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUITabControl_setTabExtraWidth', c_module))
IGUITabControl_getTabExtraWidth = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITabControl_getTabExtraWidth', c_module))

#functions for class IGUIToolBar
IGUIToolBar_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIToolBar_ctor', c_module))
IGUIToolBar_addButton = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('IGUIToolBar_addButton', c_module))

#================= IGUITreeViewNode
IGUITreeViewNode_getOwner = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getOwner', c_module))
IGUITreeViewNode_getParent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getParent', c_module))
IGUITreeViewNode_getText = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IGUITreeViewNode_getText', c_module))
IGUITreeViewNode_setText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUITreeViewNode_setText', c_module))
IGUITreeViewNode_getIcon = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IGUITreeViewNode_getIcon', c_module))
IGUITreeViewNode_setIcon = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUITreeViewNode_setIcon', c_module))
IGUITreeViewNode_getImageIndex = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUITreeViewNode_getImageIndex', c_module))
IGUITreeViewNode_setImageIndex = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUITreeViewNode_setImageIndex', c_module))
IGUITreeViewNode_getSelectedImageIndex = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUITreeViewNode_getSelectedImageIndex', c_module))
IGUITreeViewNode_setSelectedImageIndex = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUITreeViewNode_setSelectedImageIndex', c_module))
IGUITreeViewNode_getData = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getData', c_module))
IGUITreeViewNode_setData = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_setData', c_module))
IGUITreeViewNode_getData2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getData2', c_module))
IGUITreeViewNode_setData2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_setData2', c_module))
IGUITreeViewNode_getChildCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUITreeViewNode_getChildCount', c_module))
if IRRLICHT_VERSION < 180:
	IGUITreeViewNode_clearChilds = func_type(None, ctypes.c_void_p)(('IGUITreeViewNode_clearChilds', c_module))
	IGUITreeViewNode_hasChilds = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeViewNode_hasChilds', c_module))
IGUITreeViewNode_addChildBack = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_addChildBack', c_module))
IGUITreeViewNode_addChildFront = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_addChildFront', c_module))
IGUITreeViewNode_insertChildAfter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_insertChildAfter', c_module))
IGUITreeViewNode_insertChildBefore = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_insertChildBefore', c_module))
IGUITreeViewNode_getFirstChild = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getFirstChild', c_module))
IGUITreeViewNode_getLastChild = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getLastChild', c_module))
IGUITreeViewNode_getPrevSibling = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getPrevSibling', c_module))
IGUITreeViewNode_getNextSibling = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getNextSibling', c_module))
IGUITreeViewNode_getNextVisible = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_getNextVisible', c_module))
IGUITreeViewNode_deleteChild = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_deleteChild', c_module))
IGUITreeViewNode_moveChildUp = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_moveChildUp', c_module))
IGUITreeViewNode_moveChildDown = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeViewNode_moveChildDown', c_module))
IGUITreeViewNode_getExpanded = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeViewNode_getExpanded', c_module))
IGUITreeViewNode_setExpanded = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITreeViewNode_setExpanded', c_module))
IGUITreeViewNode_getSelected = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeViewNode_getSelected', c_module))
IGUITreeViewNode_setSelected = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITreeViewNode_setSelected', c_module))
IGUITreeViewNode_isRoot = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeViewNode_isRoot', c_module))
IGUITreeViewNode_getLevel = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITreeViewNode_getLevel', c_module))
IGUITreeViewNode_isVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeViewNode_isVisible', c_module))

#================= IGUITreeView
IGUITreeView_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUITreeView_ctor', c_module))
IGUITreeView_getRoot = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_getRoot', c_module))
IGUITreeView_getSelected = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_getSelected', c_module))
IGUITreeView_getLinesVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeView_getLinesVisible', c_module))
IGUITreeView_setLinesVisible = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITreeView_setLinesVisible', c_module))
IGUITreeView_setIconFont = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_setIconFont', c_module))
IGUITreeView_setImageList = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_setImageList', c_module))
IGUITreeView_getImageList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_getImageList', c_module))
IGUITreeView_setImageLeftOfIcon = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITreeView_setImageLeftOfIcon', c_module))
IGUITreeView_getImageLeftOfIcon = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITreeView_getImageLeftOfIcon', c_module))
IGUITreeView_getLastEventNode = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUITreeView_getLastEventNode', c_module))

# functions for class IGUIScrollBar
IGUIScrollBar_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_ctor', c_module))
IGUIScrollBar_setMax = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIScrollBar_setMax', c_module))
IGUIScrollBar_getMax = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_getMax', c_module))
IGUIScrollBar_setMin = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIScrollBar_setMin', c_module))
IGUIScrollBar_getMin = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_getMin', c_module))
IGUIScrollBar_getSmallStep = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_getSmallStep', c_module))
IGUIScrollBar_setSmallStep = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIScrollBar_setSmallStep', c_module))
IGUIScrollBar_getLargeStep = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_getLargeStep', c_module))
IGUIScrollBar_setLargeStep = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIScrollBar_setLargeStep', c_module))
IGUIScrollBar_getPos = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIScrollBar_getPos', c_module))
IGUIScrollBar_setPos = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIScrollBar_setPos', c_module))

# functions for class IGUISkin
IGUISkin_getColor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_getColor', c_module))
IGUISkin_setColor = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUISkin_setColor', c_module))
IGUISkin_getSize = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_getSize', c_module))
IGUISkin_getDefaultText = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_getDefaultText', c_module))
IGUISkin_setDefaultText = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IGUISkin_setDefaultText', c_module))
IGUISkin_setSize = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUISkin_setSize', c_module))
IGUISkin_getFont = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_getFont', c_module))
IGUISkin_setFont = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_setFont', c_module))
IGUISkin_getSpriteBank = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_getSpriteBank', c_module))
IGUISkin_setSpriteBank = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_setSpriteBank', c_module))
IGUISkin_getIcon = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_getIcon', c_module))
IGUISkin_setIcon = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUISkin_setIcon', c_module))
IGUISkin_draw3DButtonPaneStandard = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DButtonPaneStandard', c_module))
IGUISkin_draw3DButtonPanePressed = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DButtonPanePressed', c_module))
IGUISkin_draw3DSunkenPane = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DSunkenPane', c_module))
IGUISkin_draw3DWindowBackground = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DWindowBackground', c_module))
IGUISkin_draw3DMenuPane = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DMenuPane', c_module))
IGUISkin_draw3DToolBar = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw3DToolBar', c_module))
IGUISkin_draw3DTabButton = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUISkin_draw3DTabButton', c_module))
IGUISkin_draw3DTabBody = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUISkin_draw3DTabBody', c_module))
IGUISkin_drawIcon = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_bool, ctypes.c_void_p)(('IGUISkin_drawIcon', c_module))
IGUISkin_draw2DRectangle = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUISkin_draw2DRectangle', c_module))
IGUISkin_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUISkin_getType', c_module))

# functions for class IGUISpinBox
IGUISpinBox_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUISpinBox_ctor', c_module))
IGUISpinBox_getEditBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUISpinBox_getEditBox', c_module))
IGUISpinBox_setValue = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IGUISpinBox_setValue', c_module))
IGUISpinBox_getValue = func_type(ctypes.c_float, ctypes.c_void_p)(('IGUISpinBox_getValue', c_module))
IGUISpinBox_setRange = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('IGUISpinBox_setRange', c_module))
IGUISpinBox_getMin = func_type(ctypes.c_float, ctypes.c_void_p)(('IGUISpinBox_getMin', c_module))
IGUISpinBox_getMax = func_type(ctypes.c_float, ctypes.c_void_p)(('IGUISpinBox_getMax', c_module))
IGUISpinBox_setStepSize = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IGUISpinBox_setStepSize', c_module))
IGUISpinBox_setDecimalPlaces = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUISpinBox_setDecimalPlaces', c_module))
IGUISpinBox_getStepSize = func_type(ctypes.c_float, ctypes.c_void_p)(('IGUISpinBox_getStepSize', c_module))

#================= array<rect<s32>> (rects32array)
rects32array_ctor = func_type(ctypes.c_void_p)(('rects32array_ctor', c_module))
rects32array_delete = func_type(None, ctypes.c_void_p)(('rects32array_delete', c_module))
rects32array_reallocate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('rects32array_reallocate', c_module))
rects32array_setAllocStrategy = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_setAllocStrategy', c_module))
rects32array_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_push_back', c_module))
rects32array_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_push_front', c_module))
rects32array_insert = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('rects32array_insert', c_module))
rects32array_clear = func_type(None, ctypes.c_void_p)(('rects32array_clear', c_module))
rects32array_set_pointer = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('rects32array_set_pointer', c_module))
rects32array_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('rects32array_set_free_when_destroyed', c_module))
rects32array_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('rects32array_set_used', c_module))
rects32array_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('rects32array_get_item', c_module))
rects32array_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('rects32array_size', c_module))
rects32array_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('rects32array_empty', c_module))
rects32array_sort = func_type(None, ctypes.c_void_p)(('rects32array_sort', c_module))
rects32array_binary_search1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_binary_search1', c_module))
rects32array_binary_search2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('rects32array_binary_search2', c_module))
rects32array_binary_search_multi = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_binary_search_multi', c_module))
rects32array_linear_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_linear_search', c_module))
rects32array_linear_reverse_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_linear_reverse_search', c_module))
rects32array_erase1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('rects32array_erase1', c_module))
rects32array_erase2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('rects32array_erase2', c_module))
rects32array_set_sorted = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('rects32array_set_sorted', c_module))
rects32array_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('rects32array_swap', c_module))

#================= SGUISpriteFrame
SGUISpriteFrame_ctor = func_type(ctypes.c_void_p)(('SGUISpriteFrame_ctor', c_module))
SGUISpriteFrame_get_rectNumber = func_type(ctypes.c_uint, ctypes.c_void_p)(('SGUISpriteFrame_get_rectNumber', c_module))
SGUISpriteFrame_set_rectNumber = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrame_set_rectNumber', c_module))
SGUISpriteFrame_get_textureNumber = func_type(ctypes.c_uint, ctypes.c_void_p)(('SGUISpriteFrame_get_textureNumber', c_module))
SGUISpriteFrame_set_textureNumber = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrame_set_textureNumber', c_module))

#================= array<SGUISpriteFrame> (SGUISpriteFrameArray)
SGUISpriteFrameArray_ctor = func_type(ctypes.c_void_p)(('SGUISpriteFrameArray_ctor', c_module))
SGUISpriteFrameArray_reallocate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrameArray_reallocate', c_module))
SGUISpriteFrameArray_setAllocStrategy = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteFrameArray_setAllocStrategy', c_module))
SGUISpriteFrameArray_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteFrameArray_push_back', c_module))
SGUISpriteFrameArray_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteFrameArray_push_front', c_module))
SGUISpriteFrameArray_insert = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrameArray_insert', c_module))
SGUISpriteFrameArray_clear = func_type(None, ctypes.c_void_p)(('SGUISpriteFrameArray_clear', c_module))
SGUISpriteFrameArray_set_pointer = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('SGUISpriteFrameArray_set_pointer', c_module))
SGUISpriteFrameArray_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SGUISpriteFrameArray_set_free_when_destroyed', c_module))
SGUISpriteFrameArray_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrameArray_set_used', c_module))
SGUISpriteFrameArray_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrameArray_get_item', c_module))
SGUISpriteFrameArray_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('SGUISpriteFrameArray_size', c_module))
SGUISpriteFrameArray_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('SGUISpriteFrameArray_empty', c_module))
SGUISpriteFrameArray_erase1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteFrameArray_erase1', c_module))
SGUISpriteFrameArray_erase2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('SGUISpriteFrameArray_erase2', c_module))
SGUISpriteFrameArray_set_sorted = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SGUISpriteFrameArray_set_sorted', c_module))
SGUISpriteFrameArray_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteFrameArray_swap', c_module))

#================= SGUISprite
SGUISprite_ctor = func_type(ctypes.c_void_p)(('SGUISprite_ctor', c_module))
SGUISprite_get_Frames = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SGUISprite_get_Frames', c_module))
SGUISprite_set_Frames = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISprite_set_Frames', c_module))
SGUISprite_get_frameTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('SGUISprite_get_frameTime', c_module))
SGUISprite_set_frameTime = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISprite_set_frameTime', c_module))

#================= array<SGUISprite> (SGUISpriteArray)
SGUISpriteArray_ctor = func_type(ctypes.c_void_p)(('SGUISpriteArray_ctor', c_module))
SGUISpriteArray_reallocate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteArray_reallocate', c_module))
SGUISpriteArray_setAllocStrategy = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteArray_setAllocStrategy', c_module))
SGUISpriteArray_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteArray_push_back', c_module))
SGUISpriteArray_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteArray_push_front', c_module))
SGUISpriteArray_insert = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteArray_insert', c_module))
SGUISpriteArray_clear = func_type(None, ctypes.c_void_p)(('SGUISpriteArray_clear', c_module))
SGUISpriteArray_set_pointer = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('SGUISpriteArray_set_pointer', c_module))
SGUISpriteArray_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SGUISpriteArray_set_free_when_destroyed', c_module))
SGUISpriteArray_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteArray_set_used', c_module))
SGUISpriteArray_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteArray_get_item', c_module))
SGUISpriteArray_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('SGUISpriteArray_size', c_module))
SGUISpriteArray_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('SGUISpriteArray_empty', c_module))
SGUISpriteArray_erase1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SGUISpriteArray_erase1', c_module))
SGUISpriteArray_erase2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('SGUISpriteArray_erase2', c_module))
SGUISpriteArray_set_sorted = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SGUISpriteArray_set_sorted', c_module))
SGUISpriteArray_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SGUISpriteArray_swap', c_module))

# functions for class IGUISpriteBank
IGUISpriteBank_getPositions = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUISpriteBank_getPositions', c_module))
IGUISpriteBank_getSprites = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUISpriteBank_getSprites', c_module))
IGUISpriteBank_getTextureCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUISpriteBank_getTextureCount', c_module))
IGUISpriteBank_getTexture = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IGUISpriteBank_getTexture', c_module))
IGUISpriteBank_addTexture = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUISpriteBank_addTexture', c_module))
IGUISpriteBank_setTexture = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('IGUISpriteBank_setTexture', c_module))
IGUISpriteBank_addTextureAsSprite = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IGUISpriteBank_addTextureAsSprite', c_module))
IGUISpriteBank_clear = func_type(None, ctypes.c_void_p)(('IGUISpriteBank_clear', c_module))
IGUISpriteBank_draw2DSprite = func_type(None, ctypes.c_void_p)(('IGUISpriteBank_draw2DSprite', c_module))
IGUISpriteBank_draw2DSpriteBatch = func_type(None, ctypes.c_void_p)(('IGUISpriteBank_draw2DSpriteBatch', c_module))

# functions for class IGUIStaticText
IGUIStaticText_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIStaticText_ctor', c_module))
IGUIStaticText_setOverrideFont = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIStaticText_setOverrideFont', c_module))
IGUIStaticText_getOverrideFont = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIStaticText_getOverrideFont', c_module))
IGUIStaticText_setOverrideColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIStaticText_setOverrideColor', c_module))
IGUIStaticText_getOverrideColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIStaticText_getOverrideColor', c_module))
IGUIStaticText_enableOverrideColor = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIStaticText_enableOverrideColor', c_module))
IGUIStaticText_isOverrideColorEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIStaticText_isOverrideColorEnabled', c_module))
IGUIStaticText_setBackgroundColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIStaticText_setBackgroundColor', c_module))
IGUIStaticText_setDrawBackground = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIStaticText_setDrawBackground', c_module))
IGUIStaticText_setDrawBorder = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIStaticText_setDrawBorder', c_module))
IGUIStaticText_setTextAlignment = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUIStaticText_setTextAlignment', c_module))
IGUIStaticText_setWordWrap = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIStaticText_setWordWrap', c_module))
IGUIStaticText_isWordWrapEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIStaticText_isWordWrapEnabled', c_module))
IGUIStaticText_getTextHeight = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIStaticText_getTextHeight', c_module))
IGUIStaticText_getTextWidth = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIStaticText_getTextWidth', c_module))

# functions for class IGUIWindow
IGUIWindow_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIWindow_ctor', c_module))
IGUIWindow_getCloseButton = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIWindow_getCloseButton', c_module))
IGUIWindow_getMinimizeButton = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIWindow_getMinimizeButton', c_module))
IGUIWindow_getMaximizeButton = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIWindow_getMaximizeButton', c_module))
IGUIWindow_isDraggable = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIWindow_isDraggable', c_module))
IGUIWindow_setDraggable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIWindow_setDraggable', c_module))
IGUIWindow_setDrawBackground = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIWindow_setDrawBackground', c_module))
IGUIWindow_getDrawBackground = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIWindow_getDrawBackground', c_module))
IGUIWindow_setDrawTitlebar = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIWindow_setDrawTitlebar', c_module))
IGUIWindow_getDrawTitlebar = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIWindow_getDrawTitlebar', c_module))
IGUIWindow_getClientRect = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIWindow_getClientRect', c_module))

#class IMeshCache
IMeshCache_addMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_addMesh', c_module))
IMeshCache_removeMesh1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_removeMesh1', c_module))
IMeshCache_removeMesh2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_removeMesh2', c_module))
IMeshCache_getMeshCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMeshCache_getMeshCount', c_module))
IMeshCache_getMeshIndex1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_getMeshIndex1', c_module))
IMeshCache_getMeshIndex2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_getMeshIndex2', c_module))
IMeshCache_getMeshByIndex = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshCache_getMeshByIndex', c_module))
IMeshCache_getMeshByName = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_getMeshByName', c_module))
IMeshCache_getMeshNameByIndex = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshCache_getMeshNameByIndex', c_module))
IMeshCache_getMeshName1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_getMeshName1', c_module))
IMeshCache_getMeshName2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_getMeshName2', c_module))
IMeshCache_renameMeshByIndex = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('IMeshCache_renameMeshByIndex', c_module))
IMeshCache_renameMesh1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_renameMesh1', c_module))
IMeshCache_renameMesh2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_renameMesh2', c_module))
IMeshCache_isMeshLoaded = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IMeshCache_isMeshLoaded', c_module))
IMeshCache_clear = func_type(None, ctypes.c_void_p)(('IMeshCache_clear', c_module))
IMeshCache_clearUnusedMeshes = func_type(None, ctypes.c_void_p)(('IMeshCache_clearUnusedMeshes', c_module))

#class IMeshManipulator
IMeshManipulator_flipSurfaces = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_flipSurfaces', c_module))
IMeshManipulator_setVertexColorAlpha = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IMeshManipulator_setVertexColorAlpha', c_module))
IMeshManipulator_setVertexColors = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_setVertexColors', c_module))
IMeshManipulator_recalculateNormals1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('IMeshManipulator_recalculateNormals1', c_module))
IMeshManipulator_recalculateNormals2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('IMeshManipulator_recalculateNormals2', c_module))
IMeshManipulator_recalculateTangents = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IMeshManipulator_recalculateTangents', c_module))
IMeshManipulator_scale1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_scale1', c_module))
IMeshManipulator_scale2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_scale2', c_module))
if IRRLICHT_VERSION < 180:
	IMeshManipulator_scaleMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_scaleMesh', c_module))
	IMeshManipulator_transformMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_transformMesh', c_module))
IMeshManipulator_scaleTCoords1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshManipulator_scaleTCoords1', c_module))
IMeshManipulator_scaleTCoords2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshManipulator_scaleTCoords2', c_module))
IMeshManipulator_transform1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_transform1', c_module))
IMeshManipulator_transform2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_transform2', c_module))
IMeshManipulator_createMeshCopy = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_createMeshCopy', c_module))
IMeshManipulator_makePlanarTextureMapping1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('IMeshManipulator_makePlanarTextureMapping1', c_module))
IMeshManipulator_makePlanarTextureMapping2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('IMeshManipulator_makePlanarTextureMapping2', c_module))
IMeshManipulator_makePlanarTextureMapping3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_ubyte, ctypes.c_void_p)(('IMeshManipulator_makePlanarTextureMapping3', c_module))
IMeshManipulator_createMeshWithTangents = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IMeshManipulator_createMeshWithTangents', c_module))
IMeshManipulator_createMeshWith2TCoords = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_createMeshWith2TCoords', c_module))
IMeshManipulator_createMeshWith1TCoords = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_createMeshWith1TCoords', c_module))
IMeshManipulator_createMeshUniquePrimitives = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_createMeshUniquePrimitives', c_module))
IMeshManipulator_createMeshWelded = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('IMeshManipulator_createMeshWelded', c_module))
IMeshManipulator_getPolyCount1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_getPolyCount1', c_module))
IMeshManipulator_getPolyCount2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IMeshManipulator_getPolyCount2', c_module))
IMeshManipulator_createAnimatedMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IMeshManipulator_createAnimatedMesh', c_module))

#class IParticleAffector
IParticleAffector_ctor = func_type(ctypes.c_void_p)(('IParticleAffector_ctor', c_module))
IParticleAffector_affect = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IParticleAffector_affect', c_module))
IParticleAffector_setEnabled = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAffector_setEnabled', c_module))
IParticleAffector_getEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAffector_getEnabled', c_module))
IParticleAffector_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleAffector_getType', c_module))

#class IParticleAnimatedMeshSceneNodeEmitter : public IParticleEmitter
IParticleAnimatedMeshSceneNodeEmitter_setAnimatedMeshSceneNode = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_setAnimatedMeshSceneNode', c_module))
IParticleAnimatedMeshSceneNodeEmitter_setUseNormalDirection = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAnimatedMeshSceneNodeEmitter_setUseNormalDirection', c_module))
IParticleAnimatedMeshSceneNodeEmitter_setNormalDirectionModifier = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleAnimatedMeshSceneNodeEmitter_setNormalDirectionModifier', c_module))
IParticleAnimatedMeshSceneNodeEmitter_setEveryMeshVertex = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAnimatedMeshSceneNodeEmitter_setEveryMeshVertex', c_module))
IParticleAnimatedMeshSceneNodeEmitter_getAnimatedMeshSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_getAnimatedMeshSceneNode', c_module))
IParticleAnimatedMeshSceneNodeEmitter_isUsingNormalDirection = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_isUsingNormalDirection', c_module))
IParticleAnimatedMeshSceneNodeEmitter_getNormalDirectionModifier = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_getNormalDirectionModifier', c_module))
IParticleAnimatedMeshSceneNodeEmitter_getEveryMeshVertex = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_getEveryMeshVertex', c_module))
IParticleAnimatedMeshSceneNodeEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleAnimatedMeshSceneNodeEmitter_getType', c_module))

#class IParticleAttractionAffector : public IParticleAffector
IParticleAttractionAffector_setPoint = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleAttractionAffector_setPoint', c_module))
IParticleAttractionAffector_setAttract = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAttractionAffector_setAttract', c_module))
IParticleAttractionAffector_setAffectX = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAttractionAffector_setAffectX', c_module))
IParticleAttractionAffector_setAffectY = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAttractionAffector_setAffectY', c_module))
IParticleAttractionAffector_setAffectZ = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleAttractionAffector_setAffectZ', c_module))
IParticleAttractionAffector_getPoint = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleAttractionAffector_getPoint', c_module))
IParticleAttractionAffector_getAttract = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAttractionAffector_getAttract', c_module))
IParticleAttractionAffector_getAffectX = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAttractionAffector_getAffectX', c_module))
IParticleAttractionAffector_getAffectY = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAttractionAffector_getAffectY', c_module))
IParticleAttractionAffector_getAffectZ = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleAttractionAffector_getAffectZ', c_module))
IParticleAttractionAffector_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleAttractionAffector_getType', c_module))

#class IParticleBoxEmitter : public IParticleEmitter
IParticleBoxEmitter_setBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleBoxEmitter_setBox', c_module))
IParticleBoxEmitter_getBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleBoxEmitter_getBox', c_module))
IParticleBoxEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleBoxEmitter_getType', c_module))

#class IParticleCylinderEmitter : public IParticleEmitter
IParticleCylinderEmitter_setCenter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleCylinderEmitter_setCenter', c_module))
IParticleCylinderEmitter_setNormal = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleCylinderEmitter_setNormal', c_module))
IParticleCylinderEmitter_setRadius = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleCylinderEmitter_setRadius', c_module))
IParticleCylinderEmitter_setLength = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleCylinderEmitter_setLength', c_module))
IParticleCylinderEmitter_setOutlineOnly = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleCylinderEmitter_setOutlineOnly', c_module))
IParticleCylinderEmitter_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleCylinderEmitter_getCenter', c_module))
IParticleCylinderEmitter_getNormal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleCylinderEmitter_getNormal', c_module))
IParticleCylinderEmitter_getRadius = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleCylinderEmitter_getRadius', c_module))
IParticleCylinderEmitter_getLength = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleCylinderEmitter_getLength', c_module))
IParticleCylinderEmitter_getOutlineOnly = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleCylinderEmitter_getOutlineOnly', c_module))
IParticleCylinderEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleCylinderEmitter_getType', c_module))

#class IParticleEmitter
IParticleEmitter_emitt = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)(('IParticleEmitter_emitt', c_module))
IParticleEmitter_setDirection = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_setDirection', c_module))
IParticleEmitter_setMinParticlesPerSecond = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IParticleEmitter_setMinParticlesPerSecond', c_module))
IParticleEmitter_setMaxParticlesPerSecond = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IParticleEmitter_setMaxParticlesPerSecond', c_module))
IParticleEmitter_setMinStartColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_setMinStartColor', c_module))
IParticleEmitter_setMaxStartColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_setMaxStartColor', c_module))
IParticleEmitter_setMaxStartSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_setMaxStartSize', c_module))
IParticleEmitter_setMinStartSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_setMinStartSize', c_module))
IParticleEmitter_getDirection = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_getDirection', c_module))
IParticleEmitter_getMinParticlesPerSecond = func_type(ctypes.c_uint, ctypes.c_void_p)(('IParticleEmitter_getMinParticlesPerSecond', c_module))
IParticleEmitter_getMaxParticlesPerSecond = func_type(ctypes.c_uint, ctypes.c_void_p)(('IParticleEmitter_getMaxParticlesPerSecond', c_module))
IParticleEmitter_getMinStartColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_getMinStartColor', c_module))
IParticleEmitter_getMaxStartColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_getMaxStartColor', c_module))
IParticleEmitter_getMaxStartSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_getMaxStartSize', c_module))
IParticleEmitter_getMinStartSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleEmitter_getMinStartSize', c_module))
IParticleEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleEmitter_getType', c_module))

#class IParticleFadeOutAffector : public IParticleAffector
IParticleFadeOutAffector_setTargetColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleFadeOutAffector_setTargetColor', c_module))
if IRRLICHT_VERSION < 180:
	IParticleFadeOutAffector_setFadeOutTime = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleFadeOutAffector_setFadeOutTime', c_module))
	IParticleFadeOutAffector_getFadeOutTime = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleFadeOutAffector_getFadeOutTime', c_module))
else:
	IParticleFadeOutAffector_setFadeOutTime = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IParticleFadeOutAffector_setFadeOutTime', c_module))
	IParticleFadeOutAffector_getFadeOutTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('IParticleFadeOutAffector_getFadeOutTime', c_module))
IParticleFadeOutAffector_getTargetColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleFadeOutAffector_getTargetColor', c_module))
IParticleFadeOutAffector_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleFadeOutAffector_getType', c_module))

#class IParticleGravityAffector : public IParticleAffector
IParticleGravityAffector_setTimeForceLost = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleGravityAffector_setTimeForceLost', c_module))
IParticleGravityAffector_setGravity = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleGravityAffector_setGravity', c_module))
IParticleGravityAffector_getTimeForceLost = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleGravityAffector_getTimeForceLost', c_module))
IParticleGravityAffector_getGravity = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleGravityAffector_getGravity', c_module))
IParticleGravityAffector_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleGravityAffector_getType', c_module))

#class IParticleMeshEmitter : public IParticleEmitter
IParticleMeshEmitter_setMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleMeshEmitter_setMesh', c_module))
IParticleMeshEmitter_setUseNormalDirection = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleMeshEmitter_setUseNormalDirection', c_module))
IParticleMeshEmitter_setNormalDirectionModifier = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleMeshEmitter_setNormalDirectionModifier', c_module))
IParticleMeshEmitter_setEveryMeshVertex = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleMeshEmitter_setEveryMeshVertex', c_module))
IParticleMeshEmitter_getMesh = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleMeshEmitter_getMesh', c_module))
IParticleMeshEmitter_isUsingNormalDirection = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleMeshEmitter_isUsingNormalDirection', c_module))
IParticleMeshEmitter_getNormalDirectionModifier = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleMeshEmitter_getNormalDirectionModifier', c_module))
IParticleMeshEmitter_getEveryMeshVertex = func_type(ctypes.c_bool, ctypes.c_void_p)(('IParticleMeshEmitter_getEveryMeshVertex', c_module))
IParticleMeshEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleMeshEmitter_getType', c_module))

#class IParticleRingEmitter : public IParticleEmitter
IParticleRingEmitter_setCenter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleRingEmitter_setCenter', c_module))
IParticleRingEmitter_setRadius = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleRingEmitter_setRadius', c_module))
IParticleRingEmitter_setRingThickness = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleRingEmitter_setRingThickness', c_module))
IParticleRingEmitter_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleRingEmitter_getCenter', c_module))
IParticleRingEmitter_getRadius = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleRingEmitter_getRadius', c_module))
IParticleRingEmitter_getRingThickness = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleRingEmitter_getRingThickness', c_module))
IParticleRingEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleRingEmitter_getType', c_module))

#class IParticleRotationAffector : public IParticleAffector
IParticleRotationAffector_setPivotPoint = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleRotationAffector_setPivotPoint', c_module))
IParticleRotationAffector_setSpeed = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleRotationAffector_setSpeed', c_module))
IParticleRotationAffector_getPivotPoint = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleRotationAffector_getPivotPoint', c_module))
IParticleRotationAffector_getSpeed = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleRotationAffector_getSpeed', c_module))
IParticleRotationAffector_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleRotationAffector_getType', c_module))

#class IParticleSphereEmitter : public IParticleEmitter
IParticleSphereEmitter_setCenter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSphereEmitter_setCenter', c_module))
IParticleSphereEmitter_setRadius = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IParticleSphereEmitter_setRadius', c_module))
IParticleSphereEmitter_getCenter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleSphereEmitter_getCenter', c_module))
IParticleSphereEmitter_getRadius = func_type(ctypes.c_float, ctypes.c_void_p)(('IParticleSphereEmitter_getRadius', c_module))
IParticleSphereEmitter_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IParticleSphereEmitter_getType', c_module))

#class IParticleSystemSceneNode : public ISceneNode
IParticleSystemSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_ctor', c_module))
IParticleSystemSceneNode_setParticleSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_setParticleSize', c_module))
IParticleSystemSceneNode_setParticlesAreGlobal = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IParticleSystemSceneNode_setParticlesAreGlobal', c_module))
IParticleSystemSceneNode_getEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_getEmitter', c_module))
IParticleSystemSceneNode_setEmitter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_setEmitter', c_module))
IParticleSystemSceneNode_addAffector = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_addAffector', c_module))
IParticleSystemSceneNode_removeAllAffectors = func_type(None, ctypes.c_void_p)(('IParticleSystemSceneNode_removeAllAffectors', c_module))
IParticleSystemSceneNode_createAnimatedMeshSceneNodeEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_float, ctypes.c_int, ctypes.c_bool, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createAnimatedMeshSceneNodeEmitter', c_module))
IParticleSystemSceneNode_createBoxEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createBoxEmitter', c_module))
IParticleSystemSceneNode_createCylinderEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createCylinderEmitter', c_module))
IParticleSystemSceneNode_createMeshEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_float, ctypes.c_int, ctypes.c_bool, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createMeshEmitter', c_module))
IParticleSystemSceneNode_createPointEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createPointEmitter', c_module))
IParticleSystemSceneNode_createRingEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createRingEmitter', c_module))
IParticleSystemSceneNode_createSphereEmitter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createSphereEmitter', c_module))
IParticleSystemSceneNode_createAttractionAffector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IParticleSystemSceneNode_createAttractionAffector', c_module))
IParticleSystemSceneNode_createScaleParticleAffector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createScaleParticleAffector', c_module))
IParticleSystemSceneNode_createFadeOutParticleAffector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IParticleSystemSceneNode_createFadeOutParticleAffector', c_module))
IParticleSystemSceneNode_createGravityAffector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IParticleSystemSceneNode_createGravityAffector', c_module))
IParticleSystemSceneNode_createRotationAffector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IParticleSystemSceneNode_createRotationAffector', c_module))

#================= list<ISceneNodeAnimator*> (ISceneNodeAnimatorList)
ISceneNodeAnimatorList_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNodeAnimatorList_size', c_module))
ISceneNodeAnimatorList_clear = func_type(None, ctypes.c_void_p)(('ISceneNodeAnimatorList_clear', c_module))
ISceneNodeAnimatorList_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimatorList_empty', c_module))
ISceneNodeAnimatorList_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorList_push_back', c_module))
ISceneNodeAnimatorList_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorList_push_front', c_module))
ISceneNodeAnimatorList_first = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorList_first', c_module))
ISceneNodeAnimatorList_current = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorList_current', c_module))
ISceneNodeAnimatorList_next = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ISceneNodeAnimatorList_next', c_module))
ISceneNodeAnimatorList_last = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorList_last', c_module))
ISceneNodeAnimatorList_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeAnimatorList_get_item', c_module))

# list<ISceneNode*> (ISceneNodeList)
ISceneNodeList_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeList_ctor', c_module))
ISceneNodeList_delete = func_type(None, ctypes.c_void_p)(('ISceneNodeList_delete', c_module))
ISceneNodeList_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNodeList_size', c_module))
ISceneNodeList_clear = func_type(None, ctypes.c_void_p)(('ISceneNodeList_clear', c_module))
ISceneNodeList_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeList_empty', c_module))
ISceneNodeList_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeList_push_back', c_module))
ISceneNodeList_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeList_push_front', c_module))
ISceneNodeList_first = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeList_first', c_module))
ISceneNodeList_next = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ISceneNodeList_next', c_module))
ISceneNodeList_last = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeList_last', c_module))
ISceneNodeList_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeList_get_item', c_module))

# functions for class ISceneNode
ISceneNode_OnRegisterSceneNode = func_type(None, ctypes.c_void_p)(('ISceneNode_OnRegisterSceneNode', c_module))
ISceneNode_OnAnimate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('ISceneNode_OnAnimate', c_module))
ISceneNode_render = func_type(None, ctypes.c_void_p)(('ISceneNode_render', c_module))
ISceneNode_getName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('ISceneNode_getName', c_module))
ISceneNode_setName = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('ISceneNode_setName', c_module))
ISceneNode_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getBoundingBox', c_module))
ISceneNode_getTransformedBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getTransformedBoundingBox', c_module))
ISceneNode_getAbsoluteTransformation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getAbsoluteTransformation', c_module))
ISceneNode_getRelativeTransformation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getRelativeTransformation', c_module))
ISceneNode_isVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNode_isVisible', c_module))
ISceneNode_isTrulyVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNode_isTrulyVisible', c_module))
ISceneNode_setVisible = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ISceneNode_setVisible', c_module))
ISceneNode_getID = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneNode_getID', c_module))
ISceneNode_setID = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ISceneNode_setID', c_module))
ISceneNode_addChild = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_addChild', c_module))
ISceneNode_removeChild = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_removeChild', c_module))
ISceneNode_removeAll = func_type(None, ctypes.c_void_p)(('ISceneNode_removeAll', c_module))
ISceneNode_remove = func_type(None, ctypes.c_void_p)(('ISceneNode_remove', c_module))
ISceneNode_addAnimator = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_addAnimator', c_module))
ISceneNode_getAnimators = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getAnimators', c_module))
ISceneNode_removeAnimator = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_removeAnimator', c_module))
ISceneNode_removeAnimators = func_type(None, ctypes.c_void_p)(('ISceneNode_removeAnimators', c_module))
ISceneNode_getMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNode_getMaterial', c_module))
ISceneNode_setMaterial = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNode_setMaterial', c_module))
ISceneNode_getMaterialCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNode_getMaterialCount', c_module))
ISceneNode_setMaterialFlag = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('ISceneNode_setMaterialFlag', c_module))
ISceneNode_setMaterialTexture = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('ISceneNode_setMaterialTexture', c_module))
ISceneNode_setMaterialType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ISceneNode_setMaterialType', c_module))
ISceneNode_getScale = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getScale', c_module))
ISceneNode_setScale = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_setScale', c_module))
ISceneNode_getRotation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getRotation', c_module))
ISceneNode_setRotation = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_setRotation', c_module))
ISceneNode_getPosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getPosition', c_module))
ISceneNode_setPosition = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_setPosition', c_module))
ISceneNode_getAbsolutePosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getAbsolutePosition', c_module))
if IRRLICHT_VERSION < 180:
	ISceneNode_setAutomaticCulling = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ISceneNode_setAutomaticCulling', c_module))
	ISceneNode_getAutomaticCulling = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneNode_getAutomaticCulling', c_module))
else:
	ISceneNode_setAutomaticCulling = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('ISceneNode_setAutomaticCulling', c_module))
	ISceneNode_getAutomaticCulling = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNode_getAutomaticCulling', c_module))
ISceneNode_setDebugDataVisible = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ISceneNode_setDebugDataVisible', c_module))
ISceneNode_isDebugDataVisible = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneNode_isDebugDataVisible', c_module))
ISceneNode_setIsDebugObject = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ISceneNode_setIsDebugObject', c_module))
ISceneNode_isDebugObject = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNode_isDebugObject', c_module))
ISceneNode_getChildren = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getChildren', c_module))
ISceneNode_setParent = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_setParent', c_module))
ISceneNode_getTriangleSelector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getTriangleSelector', c_module))
ISceneNode_setTriangleSelector = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_setTriangleSelector', c_module))
ISceneNode_updateAbsolutePosition = func_type(None, ctypes.c_void_p)(('ISceneNode_updateAbsolutePosition', c_module))
ISceneNode_getParent = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getParent', c_module))
ISceneNode_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneNode_getType', c_module))
ISceneNode_serializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_serializeAttributes', c_module))
ISceneNode_deserializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_deserializeAttributes', c_module))
ISceneNode_clone = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_clone', c_module))
ISceneNode_getSceneManager = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNode_getSceneManager', c_module))

# functions for class CustomSceneNode
func_OnRegisterSceneNode = func_type(None)
func_render = func_type(None)
func_getBoundingBox = func_type(ctypes.c_void_p)
func_getMaterial = func_type(ctypes.c_void_p, ctypes.c_uint)
func_getMaterialCount = func_type(ctypes.c_uint)
CustomSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('CustomSceneNode_ctor', c_module))
CustomSceneNode_delete = func_type(None, ctypes.c_void_p)(('CustomSceneNode_delete', c_module))
CustomSceneNode_set_OnRegisterSceneNode = func_type(None, ctypes.c_void_p, func_OnRegisterSceneNode)(('CustomSceneNode_set_OnRegisterSceneNode', c_module))
CustomSceneNode_set_render = func_type(None, ctypes.c_void_p, func_render)(('CustomSceneNode_set_render', c_module))
CustomSceneNode_set_getBoundingBox = func_type(None, ctypes.c_void_p, func_getBoundingBox)(('CustomSceneNode_set_getBoundingBox', c_module))
CustomSceneNode_set_getMaterial = func_type(None, ctypes.c_void_p, func_getMaterial)(('CustomSceneNode_set_getMaterial', c_module))
CustomSceneNode_set_getMaterialCount = func_type(None, ctypes.c_void_p, func_getMaterialCount)(('CustomSceneNode_set_getMaterialCount', c_module))
#~ CustomSceneNode_set_BoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CustomSceneNode_set_BoundingBox', c_module))
#~ CustomSceneNode_set_Vertices = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CustomSceneNode_set_Vertices', c_module))
#~ CustomSceneNode_set_Material = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('CustomSceneNode_set_Material', c_module))

# functions for class ISceneNodeAnimator
ISceneNodeAnimator_animateNode = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeAnimator_animateNode', c_module))
ISceneNodeAnimator_createClone = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimator_createClone', c_module))
ISceneNodeAnimator_isEventReceiverEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimator_isEventReceiverEnabled', c_module))
ISceneNodeAnimator_OnEvent = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimator_OnEvent', c_module))
ISceneNodeAnimator_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneNodeAnimator_getType', c_module))
ISceneNodeAnimator_hasFinished = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimator_hasFinished', c_module))
ISceneNodeAnimator_set_func_event = func_type(ctypes.c_bool, ctypes.c_void_p, OnEventFunc)(('ISceneNodeAnimator_set_func_event', c_module))

# functions for class ITexture
ITexture_delete = func_type(None, ctypes.c_void_p)(('ITexture_delete', c_module))
if IRRLICHT_VERSION < 180:
	ITexture_lock = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_uint)(('ITexture_lock', c_module))
else:
	ITexture_lock = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint)(('ITexture_lock', c_module))
ITexture_unlock = func_type(None, ctypes.c_void_p)(('ITexture_unlock', c_module))
ITexture_getOriginalSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ITexture_getOriginalSize', c_module))
ITexture_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ITexture_getSize', c_module))
ITexture_getDriverType = func_type(ctypes.c_int, ctypes.c_void_p)(('ITexture_getDriverType', c_module))
ITexture_getColorFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('ITexture_getColorFormat', c_module))
ITexture_getPitch = func_type(ctypes.c_uint, ctypes.c_void_p)(('ITexture_getPitch', c_module))
ITexture_hasMipMaps = func_type(ctypes.c_bool, ctypes.c_void_p)(('ITexture_hasMipMaps', c_module))
ITexture_hasAlpha = func_type(ctypes.c_bool, ctypes.c_void_p)(('ITexture_hasAlpha', c_module))
ITexture_regenerateMipMapLevels = func_type(None, ctypes.c_void_p)(('ITexture_regenerateMipMapLevels', c_module))
ITexture_isRenderTarget = func_type(ctypes.c_bool, ctypes.c_void_p)(('ITexture_isRenderTarget', c_module))
ITexture_getName = func_type(fschar_t, ctypes.c_void_p)(('ITexture_getName', c_module))

# functions for class ITextSceneNode
ITextSceneNode_setText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('ITextSceneNode_setText', c_module))
ITextSceneNode_setTextColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ITextSceneNode_setTextColor', c_module))

# functions for class IMesh
IMesh_getMeshBufferCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMesh_getMeshBufferCount', c_module))
IMesh_getMeshBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMesh_getMeshBuffer', c_module))
IMesh_getMeshBuffer2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IMesh_getMeshBuffer2', c_module))
IMesh_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMesh_getBoundingBox', c_module))
IMesh_setBoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMesh_setBoundingBox', c_module))
IMesh_setMaterialFlag = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IMesh_setMaterialFlag', c_module))
IMesh_setHardwareMappingHint = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IMesh_setHardwareMappingHint', c_module))
IMesh_setDirty = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IMesh_setDirty', c_module))

# functions for class IMeshBuffer
IMeshBuffer_getMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_getMaterial', c_module))
IMeshBuffer_getVertexType = func_type(ctypes.c_int, ctypes.c_void_p)(('IMeshBuffer_getVertexType', c_module))
IMeshBuffer_getVertices = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_getVertices', c_module))
IMeshBuffer_getVertexCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMeshBuffer_getVertexCount', c_module))
IMeshBuffer_getIndexType = func_type(ctypes.c_int, ctypes.c_void_p)(('IMeshBuffer_getIndexType', c_module))
IMeshBuffer_getIndices = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_getIndices', c_module))
IMeshBuffer_getIndexCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMeshBuffer_getIndexCount', c_module))
IMeshBuffer_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_getBoundingBox', c_module))
IMeshBuffer_setBoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_setBoundingBox', c_module))
IMeshBuffer_recalculateBoundingBox = func_type(None, ctypes.c_void_p)(('IMeshBuffer_recalculateBoundingBox', c_module))
IMeshBuffer_getPosition = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshBuffer_getPosition', c_module))
IMeshBuffer_getNormal = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshBuffer_getNormal', c_module))
IMeshBuffer_getTCoords = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IMeshBuffer_getTCoords', c_module))
IMeshBuffer_append1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IMeshBuffer_append1', c_module))
IMeshBuffer_append2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshBuffer_append2', c_module))
IMeshBuffer_getHardwareMappingHint_Vertex = func_type(ctypes.c_int, ctypes.c_void_p)(('IMeshBuffer_getHardwareMappingHint_Vertex', c_module))
IMeshBuffer_getHardwareMappingHint_Index = func_type(ctypes.c_int, ctypes.c_void_p)(('IMeshBuffer_getHardwareMappingHint_Index', c_module))
IMeshBuffer_setHardwareMappingHint = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IMeshBuffer_setHardwareMappingHint', c_module))
IMeshBuffer_setDirty = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IMeshBuffer_setDirty', c_module))
IMeshBuffer_getChangedID_Vertex = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMeshBuffer_getChangedID_Vertex', c_module))
IMeshBuffer_getChangedID_Index = func_type(ctypes.c_uint, ctypes.c_void_p)(('IMeshBuffer_getChangedID_Index', c_module))

# functions for class IAnimatedMesh
IAnimatedMesh_getFrameCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IAnimatedMesh_getFrameCount', c_module))
IAnimatedMesh_getMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IAnimatedMesh_getMesh', c_module))
IAnimatedMesh_getMeshType = func_type(ctypes.c_int, ctypes.c_void_p)(('IAnimatedMesh_getMeshType', c_module))

# IAnimatedMeshMD2
IAnimatedMeshMD2_getFrameLoop1 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshMD2_getFrameLoop1', c_module))
IAnimatedMeshMD2_getFrameLoop2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshMD2_getFrameLoop2', c_module))
IAnimatedMeshMD2_getAnimationCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IAnimatedMeshMD2_getAnimationCount', c_module))
IAnimatedMeshMD2_getAnimationName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IAnimatedMeshMD2_getAnimationName', c_module))

#class IAnimatedMeshMD3 : public IAnimatedMesh
IAnimatedMeshMD3_setInterpolationShift = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IAnimatedMeshMD3_setInterpolationShift', c_module))
IAnimatedMeshMD3_getTagList = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IAnimatedMeshMD3_getTagList', c_module))
IAnimatedMeshMD3_getOriginalMesh = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshMD3_getOriginalMesh', c_module))

# functions for class IAnimationEndCallBack
OnAnimationEndFunc = func_type(None, ctypes.c_void_p)
IAnimationEndCallBack_ctor1 = func_type(ctypes.c_void_p)(('IAnimationEndCallBack_ctor1', c_module))
IAnimationEndCallBack_ctor2 = func_type(ctypes.c_void_p, OnAnimationEndFunc)(('IAnimationEndCallBack_ctor2', c_module))
IAnimationEndCallBack_delete = func_type(None, ctypes.c_void_p)(('IAnimationEndCallBack_delete', c_module))
IAnimationEndCallBack_set_func_event = func_type(None, ctypes.c_void_p, OnAnimationEndFunc)(('IAnimationEndCallBack_set_func_event', c_module))
IAnimationEndCallBack_UserAnimationEndCallBack = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IAnimationEndCallBack_UserAnimationEndCallBack', c_module))

# functions for class IAnimatedMeshSceneNode
IAnimatedMeshSceneNode_delete = func_type(None, ctypes.c_void_p)(('IAnimatedMeshSceneNode_delete', c_module))
IAnimatedMeshSceneNode_setCurrentFrame = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IAnimatedMeshSceneNode_setCurrentFrame', c_module))
IAnimatedMeshSceneNode_setFrameLoop = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IAnimatedMeshSceneNode_setFrameLoop', c_module))
IAnimatedMeshSceneNode_setAnimationSpeed = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IAnimatedMeshSceneNode_setAnimationSpeed', c_module))
IAnimatedMeshSceneNode_getAnimationSpeed = func_type(ctypes.c_float, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getAnimationSpeed', c_module))
IAnimatedMeshSceneNode_addShadowVolumeSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_float)(('IAnimatedMeshSceneNode_addShadowVolumeSceneNode', c_module))
IAnimatedMeshSceneNode_getJointNode1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAnimatedMeshSceneNode_getJointNode1', c_module))
IAnimatedMeshSceneNode_getJointNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IAnimatedMeshSceneNode_getJointNode2', c_module))
IAnimatedMeshSceneNode_getJointCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getJointCount', c_module))
# IAnimatedMeshSceneNode_getMS3DJointNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAnimatedMeshSceneNode_getMS3DJointNode', c_module))
# IAnimatedMeshSceneNode_getXJointNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAnimatedMeshSceneNode_getXJointNode', c_module))
IAnimatedMeshSceneNode_setMD2Animation1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IAnimatedMeshSceneNode_setMD2Animation1', c_module))
IAnimatedMeshSceneNode_setMD2Animation2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p)(('IAnimatedMeshSceneNode_setMD2Animation2', c_module))
IAnimatedMeshSceneNode_getFrameNr = func_type(ctypes.c_float, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getFrameNr', c_module))
IAnimatedMeshSceneNode_getStartFrame = func_type(ctypes.c_int, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getStartFrame', c_module))
IAnimatedMeshSceneNode_getEndFrame = func_type(ctypes.c_int, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getEndFrame', c_module))
IAnimatedMeshSceneNode_setLoopMode = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IAnimatedMeshSceneNode_setLoopMode', c_module))
IAnimatedMeshSceneNode_setAnimationEndCallback = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshSceneNode_setAnimationEndCallback', c_module))
IAnimatedMeshSceneNode_setReadOnlyMaterials = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IAnimatedMeshSceneNode_setReadOnlyMaterials', c_module))
IAnimatedMeshSceneNode_isReadOnlyMaterials = func_type(ctypes.c_bool, ctypes.c_void_p)(('IAnimatedMeshSceneNode_isReadOnlyMaterials', c_module))
IAnimatedMeshSceneNode_setMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshSceneNode_setMesh', c_module))
IAnimatedMeshSceneNode_getMesh = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshSceneNode_getMesh', c_module))
IAnimatedMeshSceneNode_getMD3TagTransformation = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IAnimatedMeshSceneNode_getMD3TagTransformation', c_module))
IAnimatedMeshSceneNode_setJointMode = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IAnimatedMeshSceneNode_setJointMode', c_module))
IAnimatedMeshSceneNode_setTransitionTime = func_type(None, ctypes.c_void_p, ctypes.c_float)(('IAnimatedMeshSceneNode_setTransitionTime', c_module))
IAnimatedMeshSceneNode_animateJoints = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IAnimatedMeshSceneNode_animateJoints', c_module))
IAnimatedMeshSceneNode_setRenderFromIdentity = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IAnimatedMeshSceneNode_setRenderFromIdentity', c_module))
IAnimatedMeshSceneNode_clone = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IAnimatedMeshSceneNode_clone', c_module))

# functions for class IBillboardSceneNode
IBillboardSceneNode_setSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardSceneNode_setSize', c_module))
IBillboardSceneNode_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IBillboardSceneNode_getSize', c_module))
IBillboardSceneNode_setColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardSceneNode_setColor', c_module))
IBillboardSceneNode_setColor2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardSceneNode_setColor2', c_module))
IBillboardSceneNode_getColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardSceneNode_getColor', c_module))

# functions for class IBillboardTextSceneNode
IBillboardTextSceneNode_setSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_setSize', c_module))
IBillboardTextSceneNode_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_getSize', c_module))
IBillboardTextSceneNode_setColor1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_setColor1', c_module))
IBillboardTextSceneNode_setColor2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_setColor2', c_module))
IBillboardTextSceneNode_getColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_getColor', c_module))
IBillboardTextSceneNode_setText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IBillboardTextSceneNode_setText', c_module))
IBillboardTextSceneNode_setTextColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IBillboardTextSceneNode_setTextColor', c_module))

# functions for class ILightSceneNode
ILightSceneNode_setLightData = func_type(None, ctypes.c_void_p, ctypes.POINTER(SLight))(('ILightSceneNode_setLightData', c_module))
ILightSceneNode_getLightData = func_type(ctypes.POINTER(SLight), ctypes.c_void_p)(('ILightSceneNode_getLightData', c_module))
ILightSceneNode_setVisible = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ILightSceneNode_setVisible', c_module))
ILightSceneNode_setRadius = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ILightSceneNode_setRadius', c_module))
ILightSceneNode_getRadius = func_type(ctypes.c_float, ctypes.c_void_p)(('ILightSceneNode_getRadius', c_module))
ILightSceneNode_setLightType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ILightSceneNode_setLightType', c_module))
ILightSceneNode_getLightType = func_type(ctypes.c_int, ctypes.c_void_p)(('ILightSceneNode_getLightType', c_module))
ILightSceneNode_enableCastShadow = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ILightSceneNode_enableCastShadow', c_module))
ILightSceneNode_getCastShadow = func_type(ctypes.c_bool, ctypes.c_void_p)(('ILightSceneNode_getCastShadow', c_module))

# functions for class ICameraSceneNode
ICameraSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_ctor', c_module))
#~ ICameraSceneNode_Destructor = func_type(None, ctypes.c_void_p)(('ICameraSceneNode_Destructor', c_module))
ICameraSceneNode_set_func_event = func_type(None, ctypes.c_void_p, OnEventFunc)(('ICameraSceneNode_set_func_event', c_module))
ICameraSceneNode_setProjectionMatrix = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ICameraSceneNode_setProjectionMatrix', c_module))
ICameraSceneNode_getProjectionMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getProjectionMatrix', c_module))
ICameraSceneNode_getViewMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getViewMatrix', c_module))
ICameraSceneNode_setViewMatrixAffector = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_setViewMatrixAffector', c_module))
ICameraSceneNode_getViewMatrixAffector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getViewMatrixAffector', c_module))
ICameraSceneNode_setTarget = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_setTarget', c_module))
ICameraSceneNode_setRotation = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_setRotation', c_module))
ICameraSceneNode_getTarget = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getTarget', c_module))
ICameraSceneNode_setUpVector = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_setUpVector', c_module))
ICameraSceneNode_getUpVector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getUpVector', c_module))
ICameraSceneNode_getNearValue = func_type(ctypes.c_float, ctypes.c_void_p)(('ICameraSceneNode_getNearValue', c_module))
ICameraSceneNode_getFarValue = func_type(ctypes.c_float, ctypes.c_void_p)(('ICameraSceneNode_getFarValue', c_module))
ICameraSceneNode_getAspectRatio = func_type(ctypes.c_float, ctypes.c_void_p)(('ICameraSceneNode_getAspectRatio', c_module))
ICameraSceneNode_getFOV = func_type(ctypes.c_float, ctypes.c_void_p)(('ICameraSceneNode_getFOV', c_module))
ICameraSceneNode_setNearValue = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ICameraSceneNode_setNearValue', c_module))
ICameraSceneNode_setFarValue = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ICameraSceneNode_setFarValue', c_module))
ICameraSceneNode_setAspectRatio = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ICameraSceneNode_setAspectRatio', c_module))
ICameraSceneNode_setFOV = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ICameraSceneNode_setFOV', c_module))
ICameraSceneNode_getViewFrustum = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICameraSceneNode_getViewFrustum', c_module))
ICameraSceneNode_setInputReceiverEnabled = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ICameraSceneNode_setInputReceiverEnabled', c_module))
ICameraSceneNode_isInputReceiverEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('ICameraSceneNode_isInputReceiverEnabled', c_module))
ICameraSceneNode_isOrthogonal = func_type(ctypes.c_bool, ctypes.c_void_p)(('ICameraSceneNode_isOrthogonal', c_module))
ICameraSceneNode_bindTargetAndRotation = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ICameraSceneNode_bindTargetAndRotation', c_module))
ICameraSceneNode_getTargetAndRotationBinding = func_type(ctypes.c_bool, ctypes.c_void_p)(('ICameraSceneNode_getTargetAndRotationBinding', c_module))

# functions for class ICollisionCallback
onCollisionFunc = func_type(ctypes.c_bool, ctypes.c_void_p) 
ICollisionCallback_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICollisionCallback_ctor1', c_module))
ICollisionCallback_ctor2 = func_type(ctypes.c_void_p, onCollisionFunc)(('ICollisionCallback_ctor2', c_module))
#~ ICollisionCallback_Destructor = func_type(None, ctypes.c_void_p)(('ICollisionCallback_Destructor', c_module))
ICollisionCallback_set_func_animator = func_type(None, ctypes.c_void_p, onCollisionFunc)(('ICollisionCallback_set_func_animator', c_module))

# functions for class IGeometryCreator
IGeometryCreator_createCubeMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGeometryCreator_createCubeMesh', c_module))
IGeometryCreator_createHillPlaneMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('IGeometryCreator_createHillPlaneMesh', c_module))
IGeometryCreator_createPlaneMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGeometryCreator_createPlaneMesh', c_module))
IGeometryCreator_createTerrainMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IGeometryCreator_createTerrainMesh', c_module))
IGeometryCreator_createArrowMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('IGeometryCreator_createArrowMesh', c_module))
IGeometryCreator_createSphereMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_uint, ctypes.c_uint)(('IGeometryCreator_createSphereMesh', c_module))
IGeometryCreator_createCylinderMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_uint, ctypes.c_void_p, ctypes.c_bool, ctypes.c_float)(('IGeometryCreator_createCylinderMesh', c_module))
IGeometryCreator_createConeMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('IGeometryCreator_createConeMesh', c_module))
IGeometryCreator_createVolumeLightMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('IGeometryCreator_createVolumeLightMesh', c_module))

# functions for class IGUIFont
IGUIFont_draw = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IGUIFont_draw', c_module))
IGUIFont_getDimension = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIFont_getDimension', c_module))
IGUIFont_getCharacterFromPos = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('IGUIFont_getCharacterFromPos', c_module))
IGUIFont_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIFont_getType', c_module))
IGUIFont_setKerningWidth = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIFont_setKerningWidth', c_module))
IGUIFont_setKerningHeight = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIFont_setKerningHeight', c_module))
IGUIFont_getKerningWidth = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p)(('IGUIFont_getKerningWidth', c_module))
IGUIFont_getKerningHeight = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIFont_getKerningHeight', c_module))
IGUIFont_setInvisibleCharacters = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIFont_setInvisibleCharacters', c_module))

#================= IGUIListBox
IGUIListBox_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUIListBox_ctor', c_module))
IGUIListBox_getItemCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUIListBox_getItemCount', c_module))
IGUIListBox_getListItem = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint)(('IGUIListBox_getListItem', c_module))
IGUIListBox_addItem1 = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIListBox_addItem1', c_module))
IGUIListBox_addItem2 = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('IGUIListBox_addItem2', c_module))
IGUIListBox_removeItem = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIListBox_removeItem', c_module))
IGUIListBox_getIcon = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)(('IGUIListBox_getIcon', c_module))
IGUIListBox_setSpriteBank = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIListBox_setSpriteBank', c_module))
IGUIListBox_clear = func_type(None, ctypes.c_void_p)(('IGUIListBox_clear', c_module))
IGUIListBox_getSelected = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUIListBox_getSelected', c_module))
IGUIListBox_setSelected1 = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIListBox_setSelected1', c_module))
IGUIListBox_setSelected2 = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IGUIListBox_setSelected2', c_module))
IGUIListBox_setAutoScrollEnabled = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIListBox_setAutoScrollEnabled', c_module))
IGUIListBox_isAutoScrollEnabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUIListBox_isAutoScrollEnabled', c_module))
IGUIListBox_setItemOverrideColor1 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('IGUIListBox_setItemOverrideColor1', c_module))
IGUIListBox_setItemOverrideColor2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_void_p)(('IGUIListBox_setItemOverrideColor2', c_module))
IGUIListBox_clearItemOverrideColor1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUIListBox_clearItemOverrideColor1', c_module))
IGUIListBox_clearItemOverrideColor2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IGUIListBox_clearItemOverrideColor2', c_module))
IGUIListBox_hasItemOverrideColor = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IGUIListBox_hasItemOverrideColor', c_module))
IGUIListBox_getItemOverrideColor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IGUIListBox_getItemOverrideColor', c_module))
IGUIListBox_getItemDefaultColor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIListBox_getItemDefaultColor', c_module))
IGUIListBox_setItem = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_int)(('IGUIListBox_setItem', c_module))
IGUIListBox_insertItem = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_int)(('IGUIListBox_insertItem', c_module))
IGUIListBox_swapItems = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IGUIListBox_swapItems', c_module))
IGUIListBox_setItemHeight = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUIListBox_setItemHeight', c_module))
IGUIListBox_setDrawBackground = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUIListBox_setDrawBackground', c_module))

#================= IGUITable
IGUITable_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IGUITable_ctor', c_module))
IGUITable_addColumn = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('IGUITable_addColumn', c_module))
IGUITable_removeColumn = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUITable_removeColumn', c_module))
IGUITable_getColumnCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getColumnCount', c_module))
IGUITable_setActiveColumn = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IGUITable_setActiveColumn', c_module))
IGUITable_getActiveColumn = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getActiveColumn', c_module))
IGUITable_getActiveColumnOrdering = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getActiveColumnOrdering', c_module))
IGUITable_setColumnWidth = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IGUITable_setColumnWidth', c_module))
IGUITable_setResizableColumns = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IGUITable_setResizableColumns', c_module))
IGUITable_hasResizableColumns = func_type(ctypes.c_bool, ctypes.c_void_p)(('IGUITable_hasResizableColumns', c_module))
IGUITable_setColumnOrdering = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('IGUITable_setColumnOrdering', c_module))
IGUITable_getSelected = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getSelected', c_module))
IGUITable_setSelected = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUITable_setSelected', c_module))
IGUITable_getRowCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getRowCount', c_module))
IGUITable_addRow = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IGUITable_addRow', c_module))
IGUITable_removeRow = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IGUITable_removeRow', c_module))
IGUITable_clearRows = func_type(None, ctypes.c_void_p)(('IGUITable_clearRows', c_module))
IGUITable_swapRows = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IGUITable_swapRows', c_module))
IGUITable_orderRows = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('IGUITable_orderRows', c_module))
IGUITable_setCellText1 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_wchar_p)(('IGUITable_setCellText1', c_module))
IGUITable_setCellText2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_wchar_p, ctypes.c_void_p)(('IGUITable_setCellText2', c_module))
IGUITable_setCellData = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)(('IGUITable_setCellData', c_module))
IGUITable_setCellColor = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)(('IGUITable_setCellColor', c_module))
IGUITable_getCellText = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IGUITable_getCellText', c_module))
IGUITable_getCellData = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint)(('IGUITable_getCellData', c_module))
IGUITable_clear = func_type(None, ctypes.c_void_p)(('IGUITable_clear', c_module))
IGUITable_setDrawFlags = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IGUITable_setDrawFlags', c_module))
IGUITable_getDrawFlags = func_type(ctypes.c_int, ctypes.c_void_p)(('IGUITable_getDrawFlags', c_module))

# functions for class ISceneCollisionManager
ISceneCollisionManager_getCollisionPoint = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneCollisionManager_getCollisionPoint', c_module))
ISceneCollisionManager_getCollisionResultPosition = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('ISceneCollisionManager_getCollisionResultPosition', c_module))
ISceneCollisionManager_getRayFromScreenCoordinates = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneCollisionManager_getRayFromScreenCoordinates', c_module))
ISceneCollisionManager_getScreenCoordinatesFrom3DPosition = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneCollisionManager_getScreenCoordinatesFrom3DPosition', c_module))
ISceneCollisionManager_getSceneNodeFromScreenCoordinatesBB = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_void_p)(('ISceneCollisionManager_getSceneNodeFromScreenCoordinatesBB', c_module))
ISceneCollisionManager_getSceneNodeFromRayBB = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_void_p)(('ISceneCollisionManager_getSceneNodeFromRayBB', c_module))
ISceneCollisionManager_getSceneNodeFromCameraBB = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('ISceneCollisionManager_getSceneNodeFromCameraBB', c_module))
ISceneCollisionManager_getSceneNodeAndCollisionPointFromRay = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_bool)(('ISceneCollisionManager_getSceneNodeAndCollisionPointFromRay', c_module))

# functions for class ISceneNodeAnimatorCollisionResponse
#~ ISceneNodeAnimatorCollisionResponse_Destructor = func_type(None, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_Destructor', c_module))
ISceneNodeAnimatorCollisionResponse_isFalling = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_isFalling', c_module))
ISceneNodeAnimatorCollisionResponse_setEllipsoidRadius = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setEllipsoidRadius', c_module))
ISceneNodeAnimatorCollisionResponse_getEllipsoidRadius = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getEllipsoidRadius', c_module))
ISceneNodeAnimatorCollisionResponse_setGravity = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setGravity', c_module))
ISceneNodeAnimatorCollisionResponse_getGravity = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getGravity', c_module))
ISceneNodeAnimatorCollisionResponse_jump = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ISceneNodeAnimatorCollisionResponse_jump', c_module))
ISceneNodeAnimatorCollisionResponse_setAnimateTarget = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ISceneNodeAnimatorCollisionResponse_setAnimateTarget', c_module))
ISceneNodeAnimatorCollisionResponse_getAnimateTarget = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getAnimateTarget', c_module))
ISceneNodeAnimatorCollisionResponse_setEllipsoidTranslation = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setEllipsoidTranslation', c_module))
ISceneNodeAnimatorCollisionResponse_getEllipsoidTranslation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getEllipsoidTranslation', c_module))
ISceneNodeAnimatorCollisionResponse_setWorld = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setWorld', c_module))
ISceneNodeAnimatorCollisionResponse_getWorld = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getWorld', c_module))
ISceneNodeAnimatorCollisionResponse_setTargetNode = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setTargetNode', c_module))
ISceneNodeAnimatorCollisionResponse_getTargetNode = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getTargetNode', c_module))
ISceneNodeAnimatorCollisionResponse_collisionOccurred = func_type(ctypes.c_bool, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_collisionOccurred', c_module))
ISceneNodeAnimatorCollisionResponse_getCollisionPoint = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getCollisionPoint', c_module))
ISceneNodeAnimatorCollisionResponse_getCollisionTriangle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getCollisionTriangle', c_module))
ISceneNodeAnimatorCollisionResponse_getCollisionResultPosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getCollisionResultPosition', c_module))
ISceneNodeAnimatorCollisionResponse_getCollisionNode = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_getCollisionNode', c_module))
ISceneNodeAnimatorCollisionResponse_setCollisionCallback = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneNodeAnimatorCollisionResponse_setCollisionCallback', c_module))

#class ISceneNodeAnimatorFactory : public IReferenceCounted
ISceneNodeAnimatorFactory_createSceneNodeAnimator1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('ISceneNodeAnimatorFactory_createSceneNodeAnimator1', c_module))
ISceneNodeAnimatorFactory_createSceneNodeAnimator2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneNodeAnimatorFactory_createSceneNodeAnimator2', c_module))
ISceneNodeAnimatorFactory_getCreatableSceneNodeAnimatorTypeCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNodeAnimatorFactory_getCreatableSceneNodeAnimatorTypeCount', c_module))
ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorType = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorType', c_module))
ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1', c_module))
ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2', c_module))

#class ISceneNodeFactory : public IReferenceCounted
ISceneNodeFactory_addSceneNode1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('ISceneNodeFactory_addSceneNode1', c_module))
ISceneNodeFactory_addSceneNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneNodeFactory_addSceneNode2', c_module))
ISceneNodeFactory_getCreatableSceneNodeTypeCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneNodeFactory_getCreatableSceneNodeTypeCount', c_module))
ISceneNodeFactory_getCreateableSceneNodeType = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeFactory_getCreateableSceneNodeType', c_module))
ISceneNodeFactory_getCreateableSceneNodeTypeName1 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneNodeFactory_getCreateableSceneNodeTypeName1', c_module))
ISceneNodeFactory_getCreateableSceneNodeTypeName2 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('ISceneNodeFactory_getCreateableSceneNodeTypeName2', c_module))

# functions for class IVideoDriver
if IRRLICHT_VERSION < 170:
	IVideoDriver_beginScene = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_beginScene', c_module))
else:
	IVideoDriver_beginScene = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_beginScene', c_module))
IVideoDriver_beginSceneDefault = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_beginSceneDefault', c_module))
IVideoDriver_endScene = func_type(ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_endScene', c_module))
IVideoDriver_queryFeature = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_queryFeature', c_module))
IVideoDriver_disableFeature = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IVideoDriver_disableFeature', c_module))
if IRRLICHT_VERSION >= 180:
	IVideoDriver_getDriverAttributes = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getDriverAttributes', c_module))
IVideoDriver_checkDriverReset = func_type(ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_checkDriverReset', c_module))
IVideoDriver_setTransform = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_setTransform', c_module))
IVideoDriver_getTransform = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_getTransform', c_module))
IVideoDriver_getImageLoaderCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getImageLoaderCount', c_module))
IVideoDriver_getImageLoader = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getImageLoader', c_module))
IVideoDriver_getImageWriterCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getImageWriterCount', c_module))
IVideoDriver_getImageWriter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getImageWriter', c_module))
IVideoDriver_setMaterial = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_setMaterial', c_module))
IVideoDriver_getTexture1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IVideoDriver_getTexture1', c_module))
IVideoDriver_getTexture2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getTexture2', c_module))
IVideoDriver_getTextureByIndex = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getTextureByIndex', c_module))
IVideoDriver_getTextureCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getTextureCount', c_module))
IVideoDriver_renameTexture = func_type(None, ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('IVideoDriver_renameTexture', c_module))
IVideoDriver_addTexture1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_int)(('IVideoDriver_addTexture1', c_module))
IVideoDriver_addTexture2 = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_addTexture2', c_module))
IVideoDriver_addRenderTargetTexture = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_int)(('IVideoDriver_addRenderTargetTexture', c_module))
IVideoDriver_removeTexture = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_removeTexture', c_module))
IVideoDriver_removeAllTextures = func_type(None, ctypes.c_void_p)(('IVideoDriver_removeAllTextures', c_module))
IVideoDriver_removeHardwareBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_removeHardwareBuffer', c_module))
IVideoDriver_removeAllHardwareBuffers = func_type(None, ctypes.c_void_p)(('IVideoDriver_removeAllHardwareBuffers', c_module))
if IRRLICHT_VERSION >= 180:
	IVideoDriver_addOcclusionQuery = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_addOcclusionQuery', c_module))
	IVideoDriver_removeOcclusionQuery = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_removeOcclusionQuery', c_module))
	IVideoDriver_removeAllOcclusionQueries = func_type(None, ctypes.c_void_p)(('IVideoDriver_removeAllOcclusionQueries', c_module))
	IVideoDriver_runOcclusionQuery = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_runOcclusionQuery', c_module))
	IVideoDriver_runAllOcclusionQueries = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_runAllOcclusionQueries', c_module))
	IVideoDriver_updateOcclusionQuery = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_updateOcclusionQuery', c_module))
	IVideoDriver_updateAllOcclusionQueries = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_updateAllOcclusionQueries', c_module))
	IVideoDriver_getOcclusionQueryResult = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getOcclusionQueryResult', c_module))
IVideoDriver_makeColorKeyTexture1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_makeColorKeyTexture1', c_module))
IVideoDriver_makeColorKeyTexture2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_makeColorKeyTexture2', c_module))
IVideoDriver_makeNormalMapTexture = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('IVideoDriver_makeNormalMapTexture', c_module))
IVideoDriver_setRenderTarget1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_setRenderTarget1', c_module))
IVideoDriver_setRenderTarget2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_setRenderTarget2', c_module))
IVideoDriver_setRenderTarget3 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IVideoDriver_setRenderTarget3', c_module))
IVideoDriver_setViewPort = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_setViewPort', c_module))
IVideoDriver_getViewPort = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_getViewPort', c_module))
IVideoDriver_drawVertexPrimitiveList = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IVideoDriver_drawVertexPrimitiveList', c_module))
IVideoDriver_draw2DVertexPrimitiveList = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IVideoDriver_draw2DVertexPrimitiveList', c_module))
IVideoDriver_drawIndexedTriangleList1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleList1', c_module))
IVideoDriver_drawIndexedTriangleList2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleList2', c_module))
IVideoDriver_drawIndexedTriangleList3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleList3', c_module))
IVideoDriver_drawIndexedTriangleFan = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleFan', c_module))
#~ IVideoDriver_drawIndexedTriangleFan1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleFan1', c_module))
#~ IVideoDriver_drawIndexedTriangleFan2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint16, ctypes.c_uint)(('IVideoDriver_drawIndexedTriangleFan2', c_module))
IVideoDriver_draw3DLine = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw3DLine', c_module))
IVideoDriver_draw3DTriangle = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw3DTriangle', c_module))
IVideoDriver_draw3DBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw3DBox', c_module))
IVideoDriver_draw2DImage1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DImage1', c_module))
IVideoDriver_draw2DImage2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_draw2DImage2', c_module))
IVideoDriver_draw2DImage3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_draw2DImage3', c_module))
IVideoDriver_draw2DImageBatch1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_draw2DImageBatch1', c_module))
IVideoDriver_draw2DImageBatch2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_draw2DImageBatch2', c_module))
IVideoDriver_draw2DRectangle1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DRectangle1', c_module))
IVideoDriver_draw2DRectangle2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DRectangle2', c_module))
IVideoDriver_draw2DRectangleOutline = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DRectangleOutline', c_module))
IVideoDriver_draw2DLine = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DLine', c_module))
IVideoDriver_drawPixel = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_drawPixel', c_module))
IVideoDriver_draw2DPolygon = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_draw2DPolygon', c_module))
if IRRLICHT_VERSION < 180:
	IVideoDriver_drawStencilShadowVolume = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IVideoDriver_drawStencilShadowVolume', c_module))
else:
	IVideoDriver_drawStencilShadowVolume = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_uint)(('IVideoDriver_drawStencilShadowVolume', c_module))
IVideoDriver_drawStencilShadow = func_type(None, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_drawStencilShadow', c_module))
IVideoDriver_drawMeshBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_drawMeshBuffer', c_module))
IVideoDriver_setFog = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_bool, ctypes.c_bool)(('IVideoDriver_setFog', c_module))
IVideoDriver_getFog = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getFog', c_module))
IVideoDriver_getColorFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_getColorFormat', c_module))
IVideoDriver_getScreenSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getScreenSize', c_module))
IVideoDriver_getCurrentRenderTargetSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getCurrentRenderTargetSize', c_module))
IVideoDriver_getFPS = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_getFPS', c_module))
IVideoDriver_getPrimitiveCountDrawn = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getPrimitiveCountDrawn', c_module))
IVideoDriver_deleteAllDynamicLights = func_type(None, ctypes.c_void_p)(('IVideoDriver_deleteAllDynamicLights', c_module))
IVideoDriver_addDynamicLight = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_addDynamicLight', c_module))
IVideoDriver_getMaximalDynamicLightAmount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getMaximalDynamicLightAmount', c_module))
IVideoDriver_getDynamicLightCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getDynamicLightCount', c_module))
IVideoDriver_getDynamicLight = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getDynamicLight', c_module))
IVideoDriver_turnLightOn = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_turnLightOn', c_module))
IVideoDriver_getName = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IVideoDriver_getName', c_module))
IVideoDriver_addExternalImageLoader = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_addExternalImageLoader', c_module))
IVideoDriver_addExternalImageWriter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_addExternalImageWriter', c_module))
IVideoDriver_getMaximalPrimitiveCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getMaximalPrimitiveCount', c_module))
IVideoDriver_setTextureCreationFlag = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IVideoDriver_setTextureCreationFlag', c_module))
IVideoDriver_getTextureCreationFlag = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_getTextureCreationFlag', c_module))
IVideoDriver_createImageFromFile1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IVideoDriver_createImageFromFile1', c_module))
IVideoDriver_createImageFromFile2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_createImageFromFile2', c_module))
if hexversion >= 0x03000000:
	IVideoDriver_writeImageToFile1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_uint)(('IVideoDriver_writeImageToFile1', c_module))
else:
	IVideoDriver_writeImageToFile1 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint)(('IVideoDriver_writeImageToFile1', c_module))
IVideoDriver_writeImageToFile2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_writeImageToFile2', c_module))
IVideoDriver_createImageFromData = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool)(('IVideoDriver_createImageFromData', c_module))
IVideoDriver_createImage1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_createImage1', c_module))
if IRRLICHT_VERSION < 180:
	IVideoDriver_createImage2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_createImage2', c_module))
	IVideoDriver_createImage3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_createImage3', c_module))
IVideoDriver_createImage4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_createImage4', c_module))
IVideoDriver_OnResize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_OnResize', c_module))
IVideoDriver_addMaterialRenderer = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IVideoDriver_addMaterialRenderer', c_module))
IVideoDriver_getMaterialRenderer = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getMaterialRenderer', c_module))
IVideoDriver_getMaterialRendererCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVideoDriver_getMaterialRendererCount', c_module))
IVideoDriver_getMaterialRendererName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_getMaterialRendererName', c_module))
IVideoDriver_setMaterialRendererName = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p)(('IVideoDriver_setMaterialRendererName', c_module))
IVideoDriver_createAttributesFromMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_createAttributesFromMaterial', c_module))
IVideoDriver_fillMaterialStructureFromAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_fillMaterialStructureFromAttributes', c_module))
#~ IVideoDriver_getExposedVideoData = func_type(ctypes.POINTER(SExposedVideoData), ctypes.c_void_p)(('IVideoDriver_getExposedVideoData', c_module))
IVideoDriver_getExposedVideoData = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getExposedVideoData', c_module))
IVideoDriver_getDriverType = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoDriver_getDriverType', c_module))
IVideoDriver_getGPUProgrammingServices = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getGPUProgrammingServices', c_module))
IVideoDriver_getMeshManipulator = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getMeshManipulator', c_module))
IVideoDriver_clearZBuffer = func_type(None, ctypes.c_void_p)(('IVideoDriver_clearZBuffer', c_module))
IVideoDriver_createScreenShot = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_createScreenShot', c_module))
IVideoDriver_findTexture = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_findTexture', c_module))
IVideoDriver_setClipPlane = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_setClipPlane', c_module))
IVideoDriver_enableClipPlane = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('IVideoDriver_enableClipPlane', c_module))
IVideoDriver_setMinHardwareBufferVertexCount = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IVideoDriver_setMinHardwareBufferVertexCount', c_module))
IVideoDriver_getOverrideMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getOverrideMaterial', c_module))
IVideoDriver_getMaterial2D = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getMaterial2D', c_module))
IVideoDriver_enableMaterial2D = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_enableMaterial2D', c_module))
IVideoDriver_getVendorInfo = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getVendorInfo', c_module))
IVideoDriver_setAmbientLight = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_setAmbientLight', c_module))
IVideoDriver_setAllowZWriteOnTransparent = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IVideoDriver_setAllowZWriteOnTransparent', c_module))
IVideoDriver_getMaxTextureSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_getMaxTextureSize', c_module))
if 'win' in platform:
	IVideoDriver_GetHandle = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_GetHandle', c_module))
else:
	IVideoDriver_GetHandle = func_type(ctypes.c_ulong, ctypes.c_void_p)(('IVideoDriver_GetHandle', c_module))
IVideoDriver_SetIcon = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IVideoDriver_SetIcon', c_module))
IVideoDriver_addAggSvgImageLoader = func_type(None, ctypes.c_void_p)(('IVideoDriver_addAggSvgImageLoader', c_module))
# draw 2d primitives with simple coords as floating numbers
IVideoDriver_draw2DRectangle_f1 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('IVideoDriver_draw2DRectangle_f1', c_module))
IVideoDriver_draw2DRectangle_f2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('IVideoDriver_draw2DRectangle_f2', c_module))
IVideoDriver_draw2DRectangle_f3 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoDriver_draw2DRectangle_f3', c_module))
IVideoDriver_draw2DRectangle_f4 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('IVideoDriver_draw2DRectangle_f4', c_module))
IVideoDriver_draw2DRectangleOutline_f = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p)(('IVideoDriver_draw2DRectangleOutline_f', c_module))
IVideoDriver_draw2DLine_f = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p)(('IVideoDriver_draw2DLine_f', c_module))
IVideoDriver_drawPixel_f = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_void_p)(('IVideoDriver_drawPixel_f', c_module))
IVideoDriver_draw2DPolygon_f = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_draw2DPolygon_f', c_module))
# extended draw 2d lines
IVideoDriver_draw2DLineW = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_draw2DLineW', c_module))
IVideoDriver_draw2DLineWf = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IVideoDriver_draw2DLineWf', c_module))

# functions for class ISceneManager
ISceneManager_getMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t)(('ISceneManager_getMesh', c_module))
ISceneManager_getMesh2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getMesh2', c_module))
ISceneManager_getMeshCache = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getMeshCache', c_module))
ISceneManager_getVideoDriver = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getVideoDriver', c_module))
ISceneManager_getGUIEnvironment = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getGUIEnvironment', c_module))
ISceneManager_getFileSystem = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getFileSystem', c_module))
ISceneManager_addVolumeLightSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addVolumeLightSceneNode', c_module))
ISceneManager_addCubeSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addCubeSceneNode', c_module))
ISceneManager_addSphereSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addSphereSceneNode', c_module))
ISceneManager_addAnimatedMeshSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ISceneManager_addAnimatedMeshSceneNode', c_module))
ISceneManager_addAnimatedMeshSceneNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addAnimatedMeshSceneNode2', c_module))
ISceneManager_addMeshSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ISceneManager_addMeshSceneNode', c_module))
ISceneManager_addWaterSurfaceSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addWaterSurfaceSceneNode', c_module))
if IRRLICHT_VERSION < 180:
	ISceneManager_addOctTreeSceneNode1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addOctTreeSceneNode1', c_module))
	ISceneManager_addOctTreeSceneNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addOctTreeSceneNode2', c_module))
	ISceneManager_addCameraSceneNodeMaya = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int)(('ISceneManager_addCameraSceneNodeMaya', c_module))
	ISceneManager_createOctTreeTriangleSelector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_createOctTreeTriangleSelector', c_module))
else:
	ISceneManager_addCameraSceneNodeMaya = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_float, ctypes.c_bool)(('ISceneManager_addCameraSceneNodeMaya', c_module))
ISceneManager_addOctreeSceneNode1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addOctreeSceneNode1', c_module))
ISceneManager_addOctreeSceneNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addOctreeSceneNode2', c_module))
ISceneManager_addCameraSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addCameraSceneNode', c_module))
ISceneManager_addCameraSceneNodeFPS = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_float, ctypes.c_bool)(('ISceneManager_addCameraSceneNodeFPS', c_module))
ISceneManager_addLightSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_int)(('ISceneManager_addLightSceneNode', c_module))
ISceneManager_addBillboardSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addBillboardSceneNode', c_module))
ISceneManager_addSkyBoxSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addSkyBoxSceneNode', c_module))
ISceneManager_addSkyDomeSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addSkyDomeSceneNode', c_module))
ISceneManager_addParticleSystemSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addParticleSystemSceneNode', c_module))
ISceneManager_addTerrainSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addTerrainSceneNode', c_module))
ISceneManager_addTerrainSceneNode2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('ISceneManager_addTerrainSceneNode2', c_module))
ISceneManager_addQuake3SceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addQuake3SceneNode', c_module))
ISceneManager_addEmptySceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addEmptySceneNode', c_module))
ISceneManager_addDummyTransformationSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addDummyTransformationSceneNode', c_module))
ISceneManager_addTextSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_addTextSceneNode', c_module))
ISceneManager_addBillboardTextSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addBillboardTextSceneNode', c_module))
ISceneManager_addHillPlaneMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addHillPlaneMesh', c_module))
ISceneManager_addTerrainMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('ISceneManager_addTerrainMesh', c_module))
ISceneManager_addArrowMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('ISceneManager_addArrowMesh', c_module))
ISceneManager_addSphereMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_float, ctypes.c_uint, ctypes.c_uint)(('ISceneManager_addSphereMesh', c_module))
ISceneManager_addVolumeLightMesh = func_type(ctypes.c_void_p, ctypes.c_void_p, fschar_t, ctypes.c_uint, ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addVolumeLightMesh', c_module))
ISceneManager_getRootSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, )(('ISceneManager_getRootSceneNode', c_module))
ISceneManager_getSceneNodeFromId = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('ISceneManager_getSceneNodeFromId', c_module))
ISceneManager_getSceneNodeFromName = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneManager_getSceneNodeFromName', c_module))
ISceneManager_getSceneNodeFromType = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('ISceneManager_getSceneNodeFromType', c_module))
ISceneManager_getSceneNodesFromType = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getSceneNodesFromType', c_module))
ISceneManager_getActiveCamera = func_type(ctypes.c_void_p, ctypes.c_void_p, )(('ISceneManager_getActiveCamera', c_module))
ISceneManager_setActiveCamera = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_setActiveCamera', c_module))
ISceneManager_setShadowColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_setShadowColor', c_module))
ISceneManager_getShadowColor = func_type(ctypes.c_void_p, ctypes.c_void_p, )(('ISceneManager_getShadowColor', c_module))
ISceneManager_registerNodeForRendering = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_registerNodeForRendering', c_module))
ISceneManager_drawAll = func_type(None, ctypes.c_void_p)(('ISceneManager_drawAll', c_module))
ISceneManager_createRotationAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createRotationAnimator', c_module))
ISceneManager_createFlyCircleAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('ISceneManager_createFlyCircleAnimator', c_module))
ISceneManager_createFlyStraightAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('ISceneManager_createFlyStraightAnimator', c_module))
ISceneManager_createTextureAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('ISceneManager_createTextureAnimator', c_module))
ISceneManager_createDeleteAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneManager_createDeleteAnimator', c_module))
ISceneManager_createCollisionResponseAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('ISceneManager_createCollisionResponseAnimator', c_module))
ISceneManager_createFollowSplineAnimator = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('ISceneManager_createFollowSplineAnimator', c_module))
ISceneManager_createTriangleSelector1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createTriangleSelector1', c_module))
ISceneManager_createTriangleSelector2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createTriangleSelector2', c_module))
ISceneManager_createTriangleSelectorFromBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createTriangleSelectorFromBoundingBox', c_module))
ISceneManager_createOctreeTriangleSelector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_createOctreeTriangleSelector', c_module))
ISceneManager_createMetaTriangleSelector = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createMetaTriangleSelector', c_module))
ISceneManager_createTerrainTriangleSelector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_createTerrainTriangleSelector', c_module))
ISceneManager_addExternalMeshLoader = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addExternalMeshLoader', c_module))
ISceneManager_getSceneCollisionManager = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getSceneCollisionManager', c_module))
ISceneManager_getMeshManipulator = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getMeshManipulator', c_module))
ISceneManager_addToDeletionQueue = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_addToDeletionQueue', c_module))
ISceneManager_postEventFromUser = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_postEventFromUser', c_module))
ISceneManager_clear = func_type(None, ctypes.c_void_p)(('ISceneManager_clear', c_module))
ISceneManager_getParameters = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getParameters', c_module))
ISceneManager_getSceneNodeRenderPass = func_type(ctypes.c_int, ctypes.c_void_p)(('ISceneManager_getSceneNodeRenderPass', c_module))
ISceneManager_getDefaultSceneNodeFactory = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getDefaultSceneNodeFactory', c_module))
ISceneManager_registerSceneNodeFactory = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_registerSceneNodeFactory', c_module))
ISceneManager_getRegisteredSceneNodeFactoryCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneManager_getRegisteredSceneNodeFactoryCount', c_module))
ISceneManager_getSceneNodeFactory = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneManager_getSceneNodeFactory', c_module))
ISceneManager_getDefaultSceneNodeAnimatorFactory = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getDefaultSceneNodeAnimatorFactory', c_module))
ISceneManager_registerSceneNodeAnimatorFactory = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_registerSceneNodeAnimatorFactory', c_module))
ISceneManager_getRegisteredSceneNodeAnimatorFactoryCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('ISceneManager_getRegisteredSceneNodeAnimatorFactoryCount', c_module))
ISceneManager_getSceneNodeAnimatorFactory = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('ISceneManager_getSceneNodeAnimatorFactory', c_module))
ISceneManager_getSceneNodeTypeName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_getSceneNodeTypeName', c_module))
ISceneManager_getAnimatorTypeName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_getAnimatorTypeName', c_module))
ISceneManager_addSceneNode = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneManager_addSceneNode', c_module))
ISceneManager_createNewSceneManager = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('ISceneManager_createNewSceneManager', c_module))
ISceneManager_saveScene = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneManager_saveScene', c_module))
ISceneManager_saveScene2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_saveScene2', c_module))
ISceneManager_loadScene = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('ISceneManager_loadScene', c_module))
ISceneManager_loadScene2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_loadScene2', c_module))
ISceneManager_createMeshWriter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('ISceneManager_createMeshWriter', c_module))
ISceneManager_createSkinnedMesh = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_createSkinnedMesh', c_module))
ISceneManager_setAmbientLight = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_setAmbientLight', c_module))
ISceneManager_getAmbientLight = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getAmbientLight', c_module))
ISceneManager_setLightManager = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_setLightManager', c_module))
ISceneManager_getGeometryCreator = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_getGeometryCreator', c_module))
ISceneManager_isCulled = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('ISceneManager_isCulled', c_module))

# functions for class IGUIEnvironment
IGUIEnvironment_drawAll = func_type(None, ctypes.c_void_p)(('IGUIEnvironment_drawAll', c_module))
IGUIEnvironment_setFocus = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_setFocus', c_module))
IGUIEnvironment_getFocus = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getFocus', c_module))
IGUIEnvironment_removeFocus = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_removeFocus', c_module))
IGUIEnvironment_hasFocus = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_hasFocus', c_module))
IGUIEnvironment_getVideoDriver = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getVideoDriver', c_module))
IGUIEnvironment_getFileSystem = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getFileSystem', c_module))
IGUIEnvironment_getOSOperator = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getOSOperator', c_module))
IGUIEnvironment_clear = func_type(None, ctypes.c_void_p)(('IGUIEnvironment_clear', c_module))
IGUIEnvironment_postEventFromUser = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_postEventFromUser', c_module))
IGUIEnvironment_setUserEventReceiver = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_setUserEventReceiver', c_module))
IGUIEnvironment_getSkin = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getSkin', c_module))
IGUIEnvironment_setSkin = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_setSkin', c_module))
IGUIEnvironment_createSkin = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_createSkin', c_module))
IGUIEnvironment_createImageList = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IGUIEnvironment_createImageList', c_module))
IGUIEnvironment_getFont = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IGUIEnvironment_getFont', c_module))
IGUIEnvironment_getBuiltInFont = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getBuiltInFont', c_module))
IGUIEnvironment_getSpriteBank = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IGUIEnvironment_getSpriteBank', c_module))
IGUIEnvironment_addEmptySpriteBank = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('IGUIEnvironment_addEmptySpriteBank', c_module))
IGUIEnvironment_getRootGUIElement = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getRootGUIElement', c_module))
IGUIEnvironment_addButton = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_wchar_p)(('IGUIEnvironment_addButton', c_module))
IGUIEnvironment_addWindow = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addWindow', c_module))
IGUIEnvironment_addModalScreen = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_addModalScreen', c_module))
IGUIEnvironment_addMessageBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addMessageBox', c_module))
IGUIEnvironment_addScrollBar = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addScrollBar', c_module))
IGUIEnvironment_addImage = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IGUIEnvironment_addImage', c_module))
IGUIEnvironment_addImage2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IGUIEnvironment_addImage2', c_module))
IGUIEnvironment_addCheckBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IGUIEnvironment_addCheckBox', c_module))
IGUIEnvironment_addListBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IGUIEnvironment_addListBox', c_module))
IGUIEnvironment_addTreeView = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IGUIEnvironment_addTreeView', c_module))
IGUIEnvironment_addMeshViewer = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_wchar_p)(('IGUIEnvironment_addMeshViewer', c_module))
if IRRLICHT_VERSION < 180:
	IGUIEnvironment_addFileOpenDialog = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addFileOpenDialog', c_module))
else:
	IGUIEnvironment_addFileOpenDialog = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool, fschar_t)(('IGUIEnvironment_addFileOpenDialog', c_module))
if BUILD_WITH_GUI_FILE_SELECTOR:
	IGUIEnvironment_addFileSelectorDialog = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addFileSelectorDialog', c_module))
IGUIEnvironment_addColorSelectDialog = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addColorSelectDialog', c_module))
IGUIEnvironment_addStaticText = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IGUIEnvironment_addStaticText', c_module))
IGUIEnvironment_addEditBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addEditBox', c_module))
IGUIEnvironment_addSpinBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addSpinBox', c_module))
IGUIEnvironment_addInOutFader = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addInOutFader', c_module))
IGUIEnvironment_addTabControl = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool, ctypes.c_int)(('IGUIEnvironment_addTabControl', c_module))
IGUIEnvironment_addTab = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addTab', c_module))
IGUIEnvironment_addContextMenu = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addContextMenu', c_module))
IGUIEnvironment_addMenu = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addMenu', c_module))
IGUIEnvironment_addToolBar = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addToolBar', c_module))
IGUIEnvironment_addComboBox = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IGUIEnvironment_addComboBox', c_module))
IGUIEnvironment_addTable = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('IGUIEnvironment_addTable', c_module))
IGUIEnvironment_getDefaultGUIElementFactory = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_getDefaultGUIElementFactory', c_module))
IGUIEnvironment_registerGUIElementFactory = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_registerGUIElementFactory', c_module))
IGUIEnvironment_getRegisteredGUIElementFactoryCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('IGUIEnvironment_getRegisteredGUIElementFactoryCount', c_module))
IGUIEnvironment_getGUIElementFactory = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IGUIEnvironment_getGUIElementFactory', c_module))
IGUIEnvironment_addGUIElement = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IGUIEnvironment_addGUIElement', c_module))
IGUIEnvironment_saveGUI = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IGUIEnvironment_saveGUI', c_module))
IGUIEnvironment_saveGUI2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_saveGUI2', c_module))
IGUIEnvironment_loadGUI = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('IGUIEnvironment_loadGUI', c_module))
IGUIEnvironment_loadGUI2 = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_loadGUI2', c_module))
IGUIEnvironment_serializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_serializeAttributes', c_module))
IGUIEnvironment_deserializeAttributes = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_deserializeAttributes', c_module))
IGUIEnvironment_writeGUIElement = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_writeGUIElement', c_module))
IGUIEnvironment_readGUIElement = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IGUIEnvironment_readGUIElement', c_module))

# functions for class IReadFile
IReadFile_read = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IReadFile_read', c_module))
IReadFile_seek = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IReadFile_seek', c_module))
IReadFile_getSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IReadFile_getSize', c_module))
IReadFile_getPos = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IReadFile_getPos', c_module))
IReadFile_getFileName = func_type(fschar_t, ctypes.c_void_p)(('IReadFile_getFileName', c_module))

#================= IWriteFile
IWriteFile_write = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IWriteFile_write', c_module))
IWriteFile_seek = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool)(('IWriteFile_seek', c_module))
IWriteFile_getPos = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IWriteFile_getPos', c_module))
IWriteFile_getFileName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IWriteFile_getFileName', c_module))

# functions for class IXMLReader
IXMLReader_read = func_type(ctypes.c_bool, ctypes.c_void_p)(('IXMLReader_read', c_module))
IXMLReader_getNodeType = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReader_getNodeType', c_module))
IXMLReader_getAttributeCount = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IXMLReader_getAttributeCount', c_module))
IXMLReader_getAttributeName = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IXMLReader_getAttributeName', c_module))
IXMLReader_getAttributeValue1 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_int)(('IXMLReader_getAttributeValue1', c_module))
IXMLReader_getAttributeValue2 = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLReader_getAttributeValue2', c_module))
IXMLReader_getAttributeValueSafe = func_type(ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLReader_getAttributeValueSafe', c_module))
IXMLReader_getAttributeValueAsInt1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLReader_getAttributeValueAsInt1', c_module))
IXMLReader_getAttributeValueAsInt2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IXMLReader_getAttributeValueAsInt2', c_module))
IXMLReader_getAttributeValueAsFloat1 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLReader_getAttributeValueAsFloat1', c_module))
IXMLReader_getAttributeValueAsFloat2 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IXMLReader_getAttributeValueAsFloat2', c_module))
IXMLReader_getNodeName = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IXMLReader_getNodeName', c_module))
IXMLReader_getNodeData = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IXMLReader_getNodeData', c_module))
IXMLReader_isEmptyElement = func_type(ctypes.c_bool, ctypes.c_void_p)(('IXMLReader_isEmptyElement', c_module))
IXMLReader_getSourceFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReader_getSourceFormat', c_module))
IXMLReader_getParserFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReader_getParserFormat', c_module))

# functions for class IXMLReaderUTF8
IXMLReaderUTF8_read = func_type(ctypes.c_bool, ctypes.c_void_p)(('IXMLReaderUTF8_read', c_module))
IXMLReaderUTF8_getNodeType = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReaderUTF8_getNodeType', c_module))
IXMLReaderUTF8_getAttributeCount = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IXMLReaderUTF8_getAttributeCount', c_module))
IXMLReaderUTF8_getAttributeName = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IXMLReaderUTF8_getAttributeName', c_module))
IXMLReaderUTF8_getAttributeValue1 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_int)(('IXMLReaderUTF8_getAttributeValue1', c_module))
IXMLReaderUTF8_getAttributeValue2 = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p)(('IXMLReaderUTF8_getAttributeValue2', c_module))
IXMLReaderUTF8_getAttributeValueSafe = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p)(('IXMLReaderUTF8_getAttributeValueSafe', c_module))
IXMLReaderUTF8_getAttributeValueAsInt1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_char_p)(('IXMLReaderUTF8_getAttributeValueAsInt1', c_module))
IXMLReaderUTF8_getAttributeValueAsInt2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IXMLReaderUTF8_getAttributeValueAsInt2', c_module))
IXMLReaderUTF8_getAttributeValueAsFloat1 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_char_p)(('IXMLReaderUTF8_getAttributeValueAsFloat1', c_module))
IXMLReaderUTF8_getAttributeValueAsFloat2 = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_int)(('IXMLReaderUTF8_getAttributeValueAsFloat2', c_module))
IXMLReaderUTF8_getNodeName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IXMLReaderUTF8_getNodeName', c_module))
IXMLReaderUTF8_getNodeData = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IXMLReaderUTF8_getNodeData', c_module))
IXMLReaderUTF8_isEmptyElement = func_type(ctypes.c_bool, ctypes.c_void_p)(('IXMLReaderUTF8_isEmptyElement', c_module))
IXMLReaderUTF8_getSourceFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReaderUTF8_getSourceFormat', c_module))
IXMLReaderUTF8_getParserFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IXMLReaderUTF8_getParserFormat', c_module))

#================= IXMLWriter
#~ IXMLWriter_Destructor = func_type(None, ctypes.c_void_p)(('IXMLWriter_Destructor', c_module))
IXMLWriter_writeXMLHeader = func_type(None, ctypes.c_void_p)(('IXMLWriter_writeXMLHeader', c_module))
IXMLWriter_writeElement1 = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p)(('IXMLWriter_writeElement1', c_module))
IXMLWriter_writeElement2 = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IXMLWriter_writeElement2', c_module))
IXMLWriter_writeComment = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLWriter_writeComment', c_module))
IXMLWriter_writeClosingTag = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLWriter_writeClosingTag', c_module))
IXMLWriter_writeText = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IXMLWriter_writeText', c_module))
IXMLWriter_writeLineBreak = func_type(None, ctypes.c_void_p)(('IXMLWriter_writeLineBreak', c_module))

# functions for class plane3df
plane3df_ctor1 = func_type(ctypes.c_void_p)(('plane3df_ctor1', c_module))
plane3df_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_ctor2', c_module))
plane3df_ctor3 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('plane3df_ctor3', c_module))
plane3df_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_ctor4', c_module))
plane3df_ctor5 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('plane3df_ctor5', c_module))
plane3df_delete = func_type(None, ctypes.c_void_p)(('plane3df_delete', c_module))
plane3df_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_operator_eq', c_module))
plane3df_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_operator_ne', c_module))
plane3df_setPlane = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_setPlane', c_module))
plane3df_setPlane2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('plane3df_setPlane2', c_module))
plane3df_setPlane3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_setPlane3', c_module))
plane3df_getIntersectionWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getIntersectionWithLine', c_module))
plane3df_getKnownIntersectionWithLine = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getKnownIntersectionWithLine', c_module))
plane3df_getIntersectionWithLimitedLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getIntersectionWithLimitedLine', c_module))
plane3df_classifyPointRelation = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_classifyPointRelation', c_module))
plane3df_recalculateD = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_recalculateD', c_module))
plane3df_getMemberPoint = func_type(ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getMemberPoint', c_module))
plane3df_existsIntersection = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_existsIntersection', c_module))
plane3df_getIntersectionWithPlane = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getIntersectionWithPlane', c_module))
plane3df_getIntersectionWithPlanes = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getIntersectionWithPlanes', c_module))
plane3df_isFrontFacing = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_isFrontFacing', c_module))
plane3df_getDistanceTo = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_getDistanceTo', c_module))
plane3df_get_Normal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('plane3df_get_Normal', c_module))
plane3df_set_Normal = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('plane3df_set_Normal', c_module))
plane3df_get_D = func_type(ctypes.c_float, ctypes.c_void_p)(('plane3df_get_D', c_module))
plane3df_set_D = func_type(None, ctypes.c_void_p, ctypes.c_float)(('plane3df_set_D', c_module))

# functions for class plane3di
plane3di_ctor1 = func_type(ctypes.c_void_p)(('plane3di_ctor1', c_module))
plane3di_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_ctor2', c_module))
plane3di_ctor3 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('plane3di_ctor3', c_module))
plane3di_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_ctor4', c_module))
plane3di_ctor5 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('plane3di_ctor5', c_module))
plane3di_delete = func_type(None, ctypes.c_void_p)(('plane3di_delete', c_module))
plane3di_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_operator_eq', c_module))
plane3di_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_operator_ne', c_module))
plane3di_setPlane = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_setPlane', c_module))
plane3di_setPlane2 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('plane3di_setPlane2', c_module))
plane3di_setPlane3 = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_setPlane3', c_module))
plane3di_getIntersectionWithLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getIntersectionWithLine', c_module))
plane3di_getKnownIntersectionWithLine = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getKnownIntersectionWithLine', c_module))
plane3di_getIntersectionWithLimitedLine = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getIntersectionWithLimitedLine', c_module))
plane3di_classifyPointRelation = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_classifyPointRelation', c_module))
plane3di_recalculateD = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_recalculateD', c_module))
plane3di_getMemberPoint = func_type(ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getMemberPoint', c_module))
plane3di_existsIntersection = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_existsIntersection', c_module))
plane3di_getIntersectionWithPlane = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getIntersectionWithPlane', c_module))
plane3di_getIntersectionWithPlanes = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getIntersectionWithPlanes', c_module))
plane3di_isFrontFacing = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_isFrontFacing', c_module))
plane3di_getDistanceTo = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_getDistanceTo', c_module))
plane3di_get_Normal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('plane3di_get_Normal', c_module))
plane3di_set_Normal = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('plane3di_set_Normal', c_module))
plane3di_get_D = func_type(ctypes.c_int, ctypes.c_void_p)(('plane3di_get_D', c_module))
plane3di_set_D = func_type(None, ctypes.c_void_p, ctypes.c_int)(('plane3di_set_D', c_module))

# quaternion
quaternion_ctor1 = func_type(ctypes.c_void_p)(('quaternion_ctor1', c_module))
quaternion_ctor2 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('quaternion_ctor2', c_module))
quaternion_ctor3 = func_type(ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('quaternion_ctor3', c_module))
quaternion_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_ctor4', c_module))
quaternion_ctor5 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_ctor5', c_module))
quaternion_delete = func_type(None, ctypes.c_void_p)(('quaternion_delete', c_module))
quaternion_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_eq', c_module))
quaternion_operator_ne = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_ne', c_module))
quaternion_operator_set1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_set1', c_module))
quaternion_operator_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_set2', c_module))
quaternion_operator_add = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_add', c_module))
quaternion_operator_mul1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_mul1', c_module))
quaternion_operator_mul2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('quaternion_operator_mul2', c_module))
quaternion_operator_mul3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_mul3', c_module))
quaternion_operator_mul_set1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('quaternion_operator_mul_set1', c_module))
quaternion_operator_mul_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_operator_mul_set2', c_module))
quaternion_dotProduct = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_dotProduct', c_module))
quaternion_set1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('quaternion_set1', c_module))
quaternion_set2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('quaternion_set2', c_module))
quaternion_set3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_set3', c_module))
quaternion_set4 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_set4', c_module))
quaternion_equals = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('quaternion_equals', c_module))
quaternion_normalize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_normalize', c_module))
quaternion_getMatrix1 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_getMatrix1', c_module))
quaternion_getMatrix2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_getMatrix2', c_module))
quaternion_getMatrixCenter = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_getMatrixCenter', c_module))
quaternion_getMatrix_transposed = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_getMatrix_transposed', c_module))
quaternion_makeInverse = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_makeInverse', c_module))
quaternion_slerp = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float)(('quaternion_slerp', c_module))
quaternion_fromAngleAxis = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_void_p)(('quaternion_fromAngleAxis', c_module))
quaternion_toAngleAxis = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_toAngleAxis', c_module))
quaternion_toEuler = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_toEuler', c_module))
quaternion_makeIdentity = func_type(ctypes.c_void_p, ctypes.c_void_p)(('quaternion_makeIdentity', c_module))
quaternion_rotationFromTo = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('quaternion_rotationFromTo', c_module))
quaternion_get_X = func_type(ctypes.c_float, ctypes.c_void_p)(('quaternion_get_X', c_module))
quaternion_set_X = func_type(None, ctypes.c_void_p, ctypes.c_float)(('quaternion_set_X', c_module))
quaternion_get_Y = func_type(ctypes.c_float, ctypes.c_void_p)(('quaternion_get_Y', c_module))
quaternion_set_Y = func_type(None, ctypes.c_void_p, ctypes.c_float)(('quaternion_set_Y', c_module))
quaternion_get_Z = func_type(ctypes.c_float, ctypes.c_void_p)(('quaternion_get_Z', c_module))
quaternion_set_Z = func_type(None, ctypes.c_void_p, ctypes.c_float)(('quaternion_set_Z', c_module))
quaternion_get_W = func_type(ctypes.c_float, ctypes.c_void_p)(('quaternion_get_W', c_module))
quaternion_set_W = func_type(None, ctypes.c_void_p, ctypes.c_float)(('quaternion_set_W', c_module))

# functions for class ICursorControl
ICursorControl_setVisible = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('ICursorControl_setVisible', c_module))
ICursorControl_isVisible = func_type(ctypes.c_bool, ctypes.c_void_p)(('ICursorControl_isVisible', c_module))
ICursorControl_setPositionF = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICursorControl_setPositionF', c_module))
ICursorControl_setPositionF2 = func_type(None, ctypes.c_void_p, ctypes.c_float, ctypes.c_float)(('ICursorControl_setPositionF2', c_module))
ICursorControl_setPositionI = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICursorControl_setPositionI', c_module))
ICursorControl_setPositionI2 = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('ICursorControl_setPositionI2', c_module))
ICursorControl_getPosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICursorControl_getPosition', c_module))
ICursorControl_getRelativePosition = func_type(ctypes.c_void_p, ctypes.c_void_p)(('ICursorControl_getRelativePosition', c_module))
ICursorControl_setReferenceRect = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('ICursorControl_setReferenceRect', c_module))

# functions for class ILogger
#~ ILogger_Destructor = func_type(None, ctypes.c_void_p)(('ILogger_Destructor', c_module))
ILogger_getLogLevel = func_type(ctypes.c_int, ctypes.c_void_p)(('ILogger_getLogLevel', c_module))
ILogger_setLogLevel = func_type(None, ctypes.c_void_p, ctypes.c_int)(('ILogger_setLogLevel', c_module))
ILogger_log = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)(('ILogger_log', c_module))
ILogger_log2 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int)(('ILogger_log2', c_module))
ILogger_log3 = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_wchar_p, ctypes.c_int)(('ILogger_log3', c_module))
ILogger_log4 = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_int)(('ILogger_log4', c_module))
ILogger_log5 = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int)(('ILogger_log5', c_module))

# functions for class IMeshSceneNode
IMeshSceneNode_setMesh = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IMeshSceneNode_setMesh', c_module))
IMeshSceneNode_getMesh = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IMeshSceneNode_getMesh', c_module))
IMeshSceneNode_setReadOnlyMaterials = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IMeshSceneNode_setReadOnlyMaterials', c_module))
IMeshSceneNode_isReadOnlyMaterials = func_type(ctypes.c_bool, ctypes.c_void_p)(('IMeshSceneNode_isReadOnlyMaterials', c_module))

# functions for class IVideoModeList
IVideoModeList_getVideoModeCount = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoModeList_getVideoModeCount', c_module))
IVideoModeList_getVideoModeResolution = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IVideoModeList_getVideoModeResolution', c_module))
IVideoModeList_getVideoModeResolution2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVideoModeList_getVideoModeResolution2', c_module))
IVideoModeList_getVideoModeDepth = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('IVideoModeList_getVideoModeDepth', c_module))
IVideoModeList_getDesktopResolution = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVideoModeList_getDesktopResolution', c_module))
IVideoModeList_getDesktopDepth = func_type(ctypes.c_int, ctypes.c_void_p)(('IVideoModeList_getDesktopDepth', c_module))

# IVolumeLightSceneNode
IVolumeLightSceneNode_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IVolumeLightSceneNode_ctor', c_module))
IVolumeLightSceneNode_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IVolumeLightSceneNode_getType', c_module))
IVolumeLightSceneNode_setSubDivideU = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IVolumeLightSceneNode_setSubDivideU', c_module))
IVolumeLightSceneNode_setSubDivideV = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('IVolumeLightSceneNode_setSubDivideV', c_module))
IVolumeLightSceneNode_getSubDivideU = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVolumeLightSceneNode_getSubDivideU', c_module))
IVolumeLightSceneNode_getSubDivideV = func_type(ctypes.c_uint, ctypes.c_void_p)(('IVolumeLightSceneNode_getSubDivideV', c_module))
IVolumeLightSceneNode_setFootColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVolumeLightSceneNode_setFootColor', c_module))
IVolumeLightSceneNode_setTailColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IVolumeLightSceneNode_setTailColor', c_module))
IVolumeLightSceneNode_getFootColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVolumeLightSceneNode_getFootColor', c_module))
IVolumeLightSceneNode_getTailColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IVolumeLightSceneNode_getTailColor', c_module))

# functions for class IOSOperator
if IRRLICHT_VERSION < 180:
	IOSOperator_getOperationSystemVersion = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IOSOperator_getOperationSystemVersion', c_module))
if IRR_IMPROVE_UNICODE:
	IOSOperator_copyToClipboard = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IOSOperator_copyToClipboard', c_module))
	IOSOperator_getTextFromClipboard = func_type(ctypes.c_wchar_p, ctypes.c_void_p)(('IOSOperator_getTextFromClipboard', c_module))
else:
	IOSOperator_copyToClipboard = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('IOSOperator_copyToClipboard', c_module))
	IOSOperator_getTextFromClipboard = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IOSOperator_getTextFromClipboard', c_module))
#~ IOSOperator_getProcessorSpeedMHz = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint))(('IOSOperator_getProcessorSpeedMHz', c_module))
#~ IOSOperator_getSystemMemory = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint))(('IOSOperator_getSystemMemory', c_module))
IOSOperator_getProcessorSpeedMHz = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IOSOperator_getProcessorSpeedMHz', c_module))
IOSOperator_getSystemMemory = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('IOSOperator_getSystemMemory', c_module))

#struct Q3LevelLoadParameter
Q3LevelLoadParameter_ctor1 = func_type(ctypes.c_void_p)(('Q3LevelLoadParameter_ctor1', c_module))
Q3LevelLoadParameter_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_ctor2', c_module))
Q3LevelLoadParameter_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_get_item', c_module))
Q3LevelLoadParameter_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_item', c_module))
Q3LevelLoadParameter_get_defaultLightMapMaterial = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_defaultLightMapMaterial', c_module))
Q3LevelLoadParameter_set_defaultLightMapMaterial = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_defaultLightMapMaterial', c_module))
Q3LevelLoadParameter_get_defaultModulate = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_defaultModulate', c_module))
Q3LevelLoadParameter_set_defaultModulate = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_defaultModulate', c_module))
Q3LevelLoadParameter_get_defaultFilter = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_defaultFilter', c_module))
Q3LevelLoadParameter_set_defaultFilter = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_defaultFilter', c_module))
Q3LevelLoadParameter_get_patchTesselation = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_patchTesselation', c_module))
Q3LevelLoadParameter_set_patchTesselation = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_patchTesselation', c_module))
Q3LevelLoadParameter_get_verbose = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_verbose', c_module))
Q3LevelLoadParameter_set_verbose = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_verbose', c_module))
Q3LevelLoadParameter_get_startTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('Q3LevelLoadParameter_get_startTime', c_module))
Q3LevelLoadParameter_set_startTime = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('Q3LevelLoadParameter_set_startTime', c_module))
Q3LevelLoadParameter_get_endTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('Q3LevelLoadParameter_get_endTime', c_module))
Q3LevelLoadParameter_set_endTime = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('Q3LevelLoadParameter_set_endTime', c_module))
Q3LevelLoadParameter_get_mergeShaderBuffer = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_mergeShaderBuffer', c_module))
Q3LevelLoadParameter_set_mergeShaderBuffer = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_mergeShaderBuffer', c_module))
Q3LevelLoadParameter_get_cleanUnResolvedMeshes = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_cleanUnResolvedMeshes', c_module))
Q3LevelLoadParameter_set_cleanUnResolvedMeshes = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_cleanUnResolvedMeshes', c_module))
Q3LevelLoadParameter_get_loadAllShaders = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_loadAllShaders', c_module))
Q3LevelLoadParameter_set_loadAllShaders = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_loadAllShaders', c_module))
Q3LevelLoadParameter_get_loadSkyShader = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_loadSkyShader', c_module))
Q3LevelLoadParameter_set_loadSkyShader = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_loadSkyShader', c_module))
Q3LevelLoadParameter_get_alpharef = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_alpharef', c_module))
Q3LevelLoadParameter_set_alpharef = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_alpharef', c_module))
Q3LevelLoadParameter_get_swapLump = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_swapLump', c_module))
Q3LevelLoadParameter_set_swapLump = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_swapLump', c_module))
Q3LevelLoadParameter_get_swapHeader = func_type(ctypes.c_int, ctypes.c_void_p)(('Q3LevelLoadParameter_get_swapHeader', c_module))
Q3LevelLoadParameter_set_swapHeader = func_type(None, ctypes.c_void_p, ctypes.c_int)(('Q3LevelLoadParameter_set_swapHeader', c_module))
Q3LevelLoadParameter_get_scriptDir = func_type(ctypes.c_char_p, ctypes.c_void_p)(('Q3LevelLoadParameter_get_scriptDir', c_module))
Q3LevelLoadParameter_set_scriptDir = func_type(None, ctypes.c_void_p, ctypes.c_char * 64)(('Q3LevelLoadParameter_set_scriptDir', c_module))
Q3LevelLoadParameter_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('Q3LevelLoadParameter_size', c_module))

# IQ3LevelMesh
IQ3LevelMesh_getShader1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool)(('IQ3LevelMesh_getShader1', c_module))
IQ3LevelMesh_getShader2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IQ3LevelMesh_getShader2', c_module))
IQ3LevelMesh_getEntityList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IQ3LevelMesh_getEntityList', c_module))

#struct SBlendFunc
SBlendFunc_ctor = func_type(ctypes.c_void_p, ctypes.c_int)(('SBlendFunc_ctor', c_module))
SBlendFunc_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SBlendFunc_get_item', c_module))
SBlendFunc_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SBlendFunc_set_item', c_module))
SBlendFunc_get_type = func_type(ctypes.c_int, ctypes.c_void_p)(('SBlendFunc_get_type', c_module))
SBlendFunc_set_type = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SBlendFunc_set_type', c_module))
SBlendFunc_get_modulate = func_type(ctypes.c_int, ctypes.c_void_p)(('SBlendFunc_get_modulate', c_module))
SBlendFunc_set_modulate = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SBlendFunc_set_modulate', c_module))
SBlendFunc_get_param0 = func_type(ctypes.c_float, ctypes.c_void_p)(('SBlendFunc_get_param0', c_module))
SBlendFunc_set_param0 = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SBlendFunc_set_param0', c_module))
SBlendFunc_get_isTransparent = func_type(ctypes.c_uint, ctypes.c_void_p)(('SBlendFunc_get_isTransparent', c_module))
SBlendFunc_set_isTransparent = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SBlendFunc_set_isTransparent', c_module))

#struct Noiser
Noiser_ctor1 = func_type(ctypes.c_void_p)(('Noiser_ctor1', c_module))
Noiser_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('Noiser_ctor2', c_module))
Noiser_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('Noiser_get_item', c_module))
Noiser_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('Noiser_set_item', c_module))
Noiser_get = func_type(ctypes.c_float, ctypes.c_void_p)(('Noiser_get', c_module))

#struct SModifierFunction
SModifierFunction_ctor1 = func_type(ctypes.c_void_p)(('SModifierFunction_ctor1', c_module))
SModifierFunction_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_ctor2', c_module))
SModifierFunction_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_get_item', c_module))
SModifierFunction_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_item', c_module))
SModifierFunction_get_masterfunc0 = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_masterfunc0', c_module))
SModifierFunction_set_masterfunc0 = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_masterfunc0', c_module))
SModifierFunction_get_masterfunc1 = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_masterfunc1', c_module))
SModifierFunction_set_masterfunc1 = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_masterfunc1', c_module))
SModifierFunction_get_func = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_func', c_module))
SModifierFunction_set_func = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_func', c_module))
SModifierFunction_get_tcgen = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_tcgen', c_module))
SModifierFunction_set_tcgen = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_tcgen', c_module))
SModifierFunction_get_rgbgen = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_rgbgen', c_module))
SModifierFunction_set_rgbgen = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_rgbgen', c_module))
SModifierFunction_get_alphagen = func_type(ctypes.c_int, ctypes.c_void_p)(('SModifierFunction_get_alphagen', c_module))
SModifierFunction_set_alphagen = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SModifierFunction_set_alphagen', c_module))
SModifierFunction_get_base = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_base', c_module))
SModifierFunction_set_base = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_base', c_module))
SModifierFunction_get_bulgewidth = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_bulgewidth', c_module))
SModifierFunction_set_bulgewidth = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_bulgewidth', c_module))
SModifierFunction_get_amp = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_amp', c_module))
SModifierFunction_set_amp = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_amp', c_module))
SModifierFunction_get_bulgeheight = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_bulgeheight', c_module))
SModifierFunction_set_bulgeheight = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_bulgeheight', c_module))
SModifierFunction_get_phase = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_phase', c_module))
SModifierFunction_set_phase = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_phase', c_module))
SModifierFunction_get_frequency = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_frequency', c_module))
SModifierFunction_set_frequency = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_frequency', c_module))
SModifierFunction_get_bulgespeed = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_bulgespeed', c_module))
SModifierFunction_set_bulgespeed = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_bulgespeed', c_module))
SModifierFunction_get_wave = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_wave', c_module))
SModifierFunction_set_wave = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_wave', c_module))
SModifierFunction_get_div = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_div', c_module))
SModifierFunction_set_div = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_div', c_module))
SModifierFunction_get_x = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_x', c_module))
SModifierFunction_set_x = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_x', c_module))
SModifierFunction_get_y = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_y', c_module))
SModifierFunction_set_y = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_y', c_module))
SModifierFunction_get_z = func_type(ctypes.c_float, ctypes.c_void_p)(('SModifierFunction_get_z', c_module))
SModifierFunction_set_z = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_set_z', c_module))
SModifierFunction_get_count = func_type(ctypes.c_uint, ctypes.c_void_p)(('SModifierFunction_get_count', c_module))
SModifierFunction_set_count = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SModifierFunction_set_count', c_module))
SModifierFunction_evaluate = func_type(ctypes.c_float, ctypes.c_void_p, ctypes.c_float)(('SModifierFunction_evaluate', c_module))

#struct SVariable
SVariable_ctor = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('SVariable_ctor', c_module))
SVariable_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVariable_get_item', c_module))
SVariable_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVariable_set_item', c_module))
SVariable_get_name = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SVariable_get_name', c_module))
SVariable_set_name = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SVariable_set_name', c_module))
SVariable_get_content = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SVariable_get_content', c_module))
SVariable_set_content = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SVariable_set_content', c_module))
SVariable_clear = func_type(None, ctypes.c_void_p)(('SVariable_clear', c_module))
SVariable_isValid = func_type(ctypes.c_int, ctypes.c_void_p)(('SVariable_isValid', c_module))
SVariable_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SVariable_operator_eq', c_module))
SVariable_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SVariable_operator_lt', c_module))

#struct SVarGroup
SVarGroup_ctor1 = func_type(ctypes.c_void_p)(('SVarGroup_ctor1', c_module))
SVarGroup_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('SVarGroup_ctor2', c_module))
SVarGroup_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVarGroup_get_item', c_module))
SVarGroup_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVarGroup_set_item', c_module))
SVarGroup_isDefined = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('SVarGroup_isDefined', c_module))
SVarGroup_get = func_type(ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p)(('SVarGroup_get', c_module))
SVarGroup_set = func_type(None, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)(('SVarGroup_set', c_module))
SVarGroup_get_Variable = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SVarGroup_get_Variable', c_module))
SVarGroup_set_Variable = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SVarGroup_set_Variable', c_module))

#struct SVarGroupList: public IReferenceCounted
SVarGroupList_ctor1 = func_type(ctypes.c_void_p)(('SVarGroupList_ctor1', c_module))
SVarGroupList_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('SVarGroupList_ctor2', c_module))
SVarGroupList_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVarGroupList_get_item', c_module))
SVarGroupList_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SVarGroupList_set_item', c_module))
SVarGroupList_get_VariableGroup = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SVarGroupList_get_VariableGroup', c_module))
SVarGroupList_set_VariableGroup = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SVarGroupList_set_VariableGroup', c_module))

#struct IShader
IShader_ctor1 = func_type(ctypes.c_void_p)(('IShader_ctor1', c_module))
IShader_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('IShader_ctor2', c_module))
IShader_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IShader_get_item', c_module))
IShader_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IShader_set_item', c_module))
IShader_operator_set = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IShader_operator_set', c_module))
IShader_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IShader_operator_eq', c_module))
IShader_operator_lt = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IShader_operator_lt', c_module))
IShader_getGroupSize = func_type(ctypes.c_uint, ctypes.c_void_p)(('IShader_getGroupSize', c_module))
IShader_getGroup = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('IShader_getGroup', c_module))
IShader_get_ID = func_type(ctypes.c_int, ctypes.c_void_p)(('IShader_get_ID', c_module))
IShader_set_ID = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IShader_set_ID', c_module))
IShader_get_VarGroup = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IShader_get_VarGroup', c_module))
IShader_set_VarGroup = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IShader_set_VarGroup', c_module))
IShader_get_name = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IShader_get_name', c_module))
IShader_set_name = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('IShader_set_name', c_module))

# tQ3EntityList
tQ3EntityList_ctor = func_type(ctypes.c_void_p)(('tQ3EntityList_ctor', c_module))
tQ3EntityList_reallocate = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('tQ3EntityList_reallocate', c_module))
tQ3EntityList_setAllocStrategy = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_setAllocStrategy', c_module))
tQ3EntityList_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_push_back', c_module))
tQ3EntityList_push_front = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_push_front', c_module))
tQ3EntityList_insert = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('tQ3EntityList_insert', c_module))
tQ3EntityList_clear = func_type(None, ctypes.c_void_p)(('tQ3EntityList_clear', c_module))
tQ3EntityList_set_pointer = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool, ctypes.c_bool)(('tQ3EntityList_set_pointer', c_module))
tQ3EntityList_set_free_when_destroyed = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('tQ3EntityList_set_free_when_destroyed', c_module))
tQ3EntityList_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('tQ3EntityList_set_used', c_module))
tQ3EntityList_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('tQ3EntityList_get_item', c_module))
tQ3EntityList_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('tQ3EntityList_size', c_module))
tQ3EntityList_empty = func_type(ctypes.c_bool, ctypes.c_void_p)(('tQ3EntityList_empty', c_module))
tQ3EntityList_sort = func_type(None, ctypes.c_void_p)(('tQ3EntityList_sort', c_module))
tQ3EntityList_binary_search1 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_binary_search1', c_module))
tQ3EntityList_binary_search2 = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('tQ3EntityList_binary_search2', c_module))
tQ3EntityList_binary_search_multi = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_binary_search_multi', c_module))
tQ3EntityList_linear_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_linear_search', c_module))
tQ3EntityList_linear_reverse_search = func_type(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_linear_reverse_search', c_module))
tQ3EntityList_erase1 = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('tQ3EntityList_erase1', c_module))
tQ3EntityList_erase2 = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('tQ3EntityList_erase2', c_module))
tQ3EntityList_set_sorted = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('tQ3EntityList_set_sorted', c_module))
tQ3EntityList_swap = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('tQ3EntityList_swap', c_module))

# functions for class ITimer
ITimer_getRealTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('ITimer_getRealTime', c_module))
if IRRLICHT_VERSION >= 180:
	# EWeekday
	EWD_SUNDAY = 0
	EWD_MONDAY = 1
	EWD_TUESDAY = 2
	EWD_WEDNESDAY = 3
	EWD_THURSDAY = 4
	EWD_FRIDAY = 5
	EWD_SATURDAY = 6
	class RealTimeDate(ctypes.Structure):
		_fields_ = [('Hour', ctypes.c_int),
					('Minute', ctypes.c_int),
					('Second', ctypes.c_int),
					('Year', ctypes.c_int),
					('Month', ctypes.c_int),
					('Day', ctypes.c_int),
					('Weekday', ctypes.c_int),
					('Yearday', ctypes.c_uint),
					('IsDST', ctypes.c_bool)
					]
	#ITimer_getRealTimeAndDate = func_type(ctypes.POINTER(RealTimeDate), ctypes.c_void_p)(('ITimer_getRealTimeAndDate', c_module))
ITimer_getTime = func_type(ctypes.c_uint, ctypes.c_void_p)(('ITimer_getTime', c_module))
ITimer_setTime = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('ITimer_setTime', c_module))
ITimer_stop = func_type(None, ctypes.c_void_p)(('ITimer_stop', c_module))
ITimer_start = func_type(None, ctypes.c_void_p)(('ITimer_start', c_module))
ITimer_setSpeed = func_type(None, ctypes.c_void_p, ctypes.c_float)(('ITimer_setSpeed', c_module))
ITimer_getSpeed = func_type(ctypes.c_float, ctypes.c_void_p)(('ITimer_getSpeed', c_module))
ITimer_isStopped = func_type(ctypes.c_bool, ctypes.c_void_p)(('ITimer_isStopped', c_module))
ITimer_tick = func_type(None, ctypes.c_void_p)(('ITimer_tick', c_module))

#struct IRenderTarget
if IRRLICHT_VERSION < 180:
	IRenderTarget_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('IRenderTarget_ctor1', c_module))
	IRenderTarget_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('IRenderTarget_ctor2', c_module))
else:
	IRenderTarget_ctor1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IRenderTarget_ctor1', c_module))
	IRenderTarget_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IRenderTarget_ctor2', c_module))
IRenderTarget_delete = func_type(None, ctypes.c_void_p)(('IRenderTarget_delete', c_module))
IRenderTarget_get_RenderTexture = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IRenderTarget_get_RenderTexture', c_module))
IRenderTarget_set_RenderTexture = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IRenderTarget_set_RenderTexture', c_module))
IRenderTarget_get_TargetType = func_type(ctypes.c_int, ctypes.c_void_p)(('IRenderTarget_get_TargetType', c_module))
IRenderTarget_set_TargetType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IRenderTarget_set_TargetType', c_module))
IRenderTarget_get_ColorMask = func_type(ctypes.c_int, ctypes.c_void_p)(('IRenderTarget_get_ColorMask', c_module))
IRenderTarget_set_ColorMask = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IRenderTarget_set_ColorMask', c_module))
IRenderTarget_get_BlendFuncSrc = func_type(ctypes.c_int, ctypes.c_void_p)(('IRenderTarget_get_BlendFuncSrc', c_module))
IRenderTarget_set_BlendFuncSrc = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IRenderTarget_set_BlendFuncSrc', c_module))
IRenderTarget_get_BlendFuncDst = func_type(ctypes.c_int, ctypes.c_void_p)(('IRenderTarget_get_BlendFuncDst', c_module))
IRenderTarget_set_BlendFuncDst = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IRenderTarget_set_BlendFuncDst', c_module))
if IRRLICHT_VERSION < 180:
	IRenderTarget_get_BlendEnable = func_type(ctypes.c_bool, ctypes.c_void_p)(('IRenderTarget_get_BlendEnable', c_module))
	IRenderTarget_set_BlendEnable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IRenderTarget_set_BlendEnable', c_module))
else:
	IRenderTarget_get_BlendOp = func_type(ctypes.c_int, ctypes.c_void_p)(('IRenderTarget_get_BlendOp', c_module))
	IRenderTarget_set_BlendOp = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IRenderTarget_set_BlendOp', c_module))

# functions for class IrrlichtDevice
IrrlichtDevice_createDevice = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_createDevice', c_module))#, ((1, 'deviceType', EDT_SOFTWARE), (1, 'windowSize', dimension2du_dimension2du(640, 480)), (1, 'bits', 16), (1, 'fullscreen', False), (1, 'stencilbuffer', False), (1, 'vsync', False), (1, 'receiver', 0)))
IrrlichtDevice_createDevice2 = func_type(ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool)(('IrrlichtDevice_createDevice2', c_module))#, ((1, 'deviceType', EDT_SOFTWARE), (1, 'windowSize', dimension2du_dimension2du(640, 480)), (1, 'bits', 16), (1, 'fullscreen', False), (1, 'stencilbuffer', False), (1, 'vsync', False), (1, 'create_receiver', False)))
#~ IrrlichtDevice_createDeviceEx = func_type(ctypes.c_void_p, ctypes.POINTER(SIrrlichtCreationParameters))(('IrrlichtDevice_createDeviceEx', c_module))
IrrlichtDevice_createDeviceEx = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_createDeviceEx', c_module))
IrrlichtDevice_run = func_type(ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_run', c_module))
IrrlichtDevice_yield = func_type(None, ctypes.c_void_p)(('IrrlichtDevice_yield', c_module))
IrrlichtDevice_sleep = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_bool)(('IrrlichtDevice_sleep', c_module))
IrrlichtDevice_getVideoDriver = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getVideoDriver', c_module))
IrrlichtDevice_getFileSystem = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getFileSystem', c_module))
IrrlichtDevice_getGUIEnvironment = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getGUIEnvironment', c_module))
IrrlichtDevice_getSceneManager = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getSceneManager', c_module))
IrrlichtDevice_getCursorControl = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getCursorControl', c_module))
IrrlichtDevice_getLogger = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getLogger', c_module))
IrrlichtDevice_getVideoModeList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getVideoModeList', c_module))
IrrlichtDevice_getOSOperator = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getOSOperator', c_module))
IrrlichtDevice_getTimer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getTimer', c_module))
IrrlichtDevice_setWindowCaption = func_type(None, ctypes.c_void_p, ctypes.c_wchar_p)(('IrrlichtDevice_setWindowCaption', c_module))
IrrlichtDevice_isWindowActive = func_type(ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_isWindowActive', c_module))
IrrlichtDevice_isWindowFocused = func_type(ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_isWindowFocused', c_module))
IrrlichtDevice_isWindowMinimized = func_type(ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_isWindowMinimized', c_module))
IrrlichtDevice_isFullscreen = func_type(ctypes.c_bool, ctypes.c_void_p)(('IrrlichtDevice_isFullscreen', c_module))
IrrlichtDevice_getColorFormat = func_type(ctypes.c_int, ctypes.c_void_p)(('IrrlichtDevice_getColorFormat', c_module))
IrrlichtDevice_closeDevice = func_type(None, ctypes.c_void_p)(('IrrlichtDevice_closeDevice', c_module))
IrrlichtDevice_getVersion = func_type(ctypes.c_char_p, ctypes.c_void_p)(('IrrlichtDevice_getVersion', c_module))
IrrlichtDevice_setEventReceiver = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_setEventReceiver', c_module))
IrrlichtDevice_getEventReceiver = func_type(ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_getEventReceiver', c_module))
IrrlichtDevice_postEventFromUser = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_postEventFromUser', c_module))
IrrlichtDevice_setInputReceivingSceneManager = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_setInputReceivingSceneManager', c_module))
IrrlichtDevice_setResizable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('IrrlichtDevice_setResizable', c_module))
IrrlichtDevice_minimizeWindow = func_type(None, ctypes.c_void_p)(('IrrlichtDevice_minimizeWindow', c_module))
IrrlichtDevice_maximizeWindow = func_type(None, ctypes.c_void_p)(('IrrlichtDevice_maximizeWindow', c_module))
IrrlichtDevice_restoreWindow = func_type(None, ctypes.c_void_p)(('IrrlichtDevice_restoreWindow', c_module))
#~ IrrlichtDevice_activateJoysticks = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.POINTER(SJoystickInfo))(('IrrlichtDevice_activateJoysticks', c_module))
IrrlichtDevice_activateJoysticks = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('IrrlichtDevice_activateJoysticks', c_module))
IrrlichtDevice_setGammaRamp = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('IrrlichtDevice_setGammaRamp', c_module))
IrrlichtDevice_getGammaRamp = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float)(('IrrlichtDevice_getGammaRamp', c_module))
IrrlichtDevice_getType = func_type(ctypes.c_int, ctypes.c_void_p)(('IrrlichtDevice_getType', c_module))
IrrlichtDevice_isDriverSupported = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('IrrlichtDevice_isDriverSupported', c_module))

#struct SOverrideMaterial
SOverrideMaterial_ctor = func_type(ctypes.c_void_p)(('SOverrideMaterial_ctor', c_module))
SOverrideMaterial_delete = func_type(None, ctypes.c_void_p)(('SOverrideMaterial_delete', c_module))
SOverrideMaterial_apply = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SOverrideMaterial_apply', c_module))
SOverrideMaterial_get_Material = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SOverrideMaterial_get_Material', c_module))
SOverrideMaterial_set_Material = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SOverrideMaterial_set_Material', c_module))
SOverrideMaterial_get_EnableFlags = func_type(ctypes.c_uint, ctypes.c_void_p)(('SOverrideMaterial_get_EnableFlags', c_module))
SOverrideMaterial_set_EnableFlags = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SOverrideMaterial_set_EnableFlags', c_module))
SOverrideMaterial_get_EnablePasses = func_type(ctypes.c_ushort, ctypes.c_void_p)(('SOverrideMaterial_get_EnablePasses', c_module))
SOverrideMaterial_set_EnablePasses = func_type(None, ctypes.c_void_p, ctypes.c_ushort)(('SOverrideMaterial_set_EnablePasses', c_module))
SOverrideMaterial_get_Enabled = func_type(ctypes.c_bool, ctypes.c_void_p)(('SOverrideMaterial_get_Enabled', c_module))
SOverrideMaterial_set_Enabled = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SOverrideMaterial_set_Enabled', c_module))

# functions for class SMaterial
SMaterial_ctor1 = func_type(ctypes.c_void_p)(('SMaterial_ctor1', c_module))
SMaterial_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_ctor2', c_module))
SMaterial_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set', c_module))
SMaterial_delete = func_type(None, ctypes.c_void_p)(('SMaterial_delete', c_module))
SMaterial_get_TextureLayer = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SMaterial_get_TextureLayer', c_module))
SMaterial_get_MaterialType = func_type(ctypes.c_int, ctypes.c_void_p)(('SMaterial_get_MaterialType', c_module))
SMaterial_get_AmbientColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_AmbientColor', c_module))
SMaterial_get_DiffuseColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_DiffuseColor', c_module))
SMaterial_get_EmissiveColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_EmissiveColor', c_module))
SMaterial_get_SpecularColor = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_SpecularColor', c_module))
SMaterial_get_Shininess = func_type(ctypes.c_float, ctypes.c_void_p)(('SMaterial_get_Shininess', c_module))
SMaterial_get_MaterialTypeParam = func_type(ctypes.c_float, ctypes.c_void_p)(('SMaterial_get_MaterialTypeParam', c_module))
SMaterial_get_MaterialTypeParam2 = func_type(ctypes.c_float, ctypes.c_void_p)(('SMaterial_get_MaterialTypeParam2', c_module))
SMaterial_get_Thickness = func_type(ctypes.c_float, ctypes.c_void_p)(('SMaterial_get_Thickness', c_module))
SMaterial_get_ZBuffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_ZBuffer', c_module))
SMaterial_get_AntiAliasing = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_AntiAliasing', c_module))
SMaterial_get_ColorMask = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_ColorMask', c_module))
SMaterial_get_ColorMaterial = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_get_ColorMaterial', c_module))
SMaterial_get_Wireframe = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_Wireframe', c_module))
SMaterial_get_PointCloud = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_PointCloud', c_module))
SMaterial_get_GouraudShading = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_GouraudShading', c_module))
SMaterial_get_Lighting = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_Lighting', c_module))
SMaterial_get_ZWriteEnable = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_ZWriteEnable', c_module))
SMaterial_get_BackfaceCulling = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_BackfaceCulling', c_module))
SMaterial_get_FrontfaceCulling = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_FrontfaceCulling', c_module))
SMaterial_get_FogEnable = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_FogEnable', c_module))
SMaterial_get_NormalizeNormals = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_get_NormalizeNormals', c_module))
SMaterial_set_TextureLayer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set_TextureLayer', c_module))
SMaterial_set_MaterialType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMaterial_set_MaterialType', c_module))
SMaterial_set_AmbientColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set_AmbientColor', c_module))
SMaterial_set_DiffuseColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set_DiffuseColor', c_module))
SMaterial_set_EmissiveColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set_EmissiveColor', c_module))
SMaterial_set_SpecularColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_set_SpecularColor', c_module))
SMaterial_set_Shininess = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMaterial_set_Shininess', c_module))
SMaterial_set_MaterialTypeParam = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMaterial_set_MaterialTypeParam', c_module))
SMaterial_set_MaterialTypeParam2 = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMaterial_set_MaterialTypeParam2', c_module))
SMaterial_set_Thickness = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMaterial_set_Thickness', c_module))
SMaterial_set_ZBuffer = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SMaterial_set_ZBuffer', c_module))
SMaterial_set_AntiAliasing = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SMaterial_set_AntiAliasing', c_module))
SMaterial_set_ColorMask = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SMaterial_set_ColorMask', c_module))
SMaterial_set_ColorMaterial = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SMaterial_set_ColorMaterial', c_module))
SMaterial_set_Wireframe = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_Wireframe', c_module))
SMaterial_set_PointCloud = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_PointCloud', c_module))
SMaterial_set_GouraudShading = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_GouraudShading', c_module))
SMaterial_set_Lighting = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_Lighting', c_module))
SMaterial_set_ZWriteEnable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_ZWriteEnable', c_module))
SMaterial_set_BackfaceCulling = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_BackfaceCulling', c_module))
SMaterial_set_FrontfaceCulling = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_FrontfaceCulling', c_module))
SMaterial_set_FogEnable = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_FogEnable', c_module))
SMaterial_set_NormalizeNormals = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterial_set_NormalizeNormals', c_module))
SMaterial_getTextureMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SMaterial_getTextureMatrix', c_module))
SMaterial_setTextureMatrix = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('SMaterial_setTextureMatrix', c_module))
SMaterial_getTexture = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SMaterial_getTexture', c_module))
SMaterial_setTexture = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('SMaterial_setTexture', c_module))
SMaterial_setFlag = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('SMaterial_setFlag', c_module))
SMaterial_getFlag = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int)(('SMaterial_getFlag', c_module))
SMaterial_operator_noteq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_operator_noteq', c_module))
SMaterial_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SMaterial_operator_eq', c_module))
SMaterial_isTransparent = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterial_isTransparent', c_module))

# functions for class SMaterialLayer
SMaterialLayer_ctor1 = func_type(ctypes.c_void_p)(('SMaterialLayer_ctor1', c_module))
SMaterialLayer_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_ctor2', c_module))
SMaterialLayer_delete = func_type(None, ctypes.c_void_p)(('SMaterialLayer_delete', c_module))
SMaterialLayer_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set', c_module))
SMaterialLayer_set_Texture = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set_Texture', c_module))
SMaterialLayer_get_Texture = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_get_Texture', c_module))
SMaterialLayer_set_TextureWrapU = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set_TextureWrapU', c_module))
SMaterialLayer_get_TextureWrapU = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_get_TextureWrapU', c_module))
SMaterialLayer_set_TextureWrapV = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set_TextureWrapV', c_module))
SMaterialLayer_get_TextureWrapV = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_get_TextureWrapV', c_module))
SMaterialLayer_set_BilinearFilter = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterialLayer_set_BilinearFilter', c_module))
SMaterialLayer_get_BilinearFilter = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterialLayer_get_BilinearFilter', c_module))
SMaterialLayer_set_TrilinearFilter = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SMaterialLayer_set_TrilinearFilter', c_module))
SMaterialLayer_get_TrilinearFilter = func_type(ctypes.c_bool, ctypes.c_void_p)(('SMaterialLayer_get_TrilinearFilter', c_module))
SMaterialLayer_set_AnisotropicFilter = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set_AnisotropicFilter', c_module))
SMaterialLayer_get_AnisotropicFilter = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_get_AnisotropicFilter', c_module))
SMaterialLayer_set_LODBias = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_set_LODBias', c_module))
SMaterialLayer_get_LODBias = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_get_LODBias', c_module))
SMaterialLayer_getTextureMatrix = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_getTextureMatrix', c_module))
SMaterialLayer_setTextureMatrix = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_setTextureMatrix', c_module))
SMaterialLayer_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_operator_eq', c_module))
SMaterialLayer_operator_noteq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SMaterialLayer_operator_noteq', c_module))

#struct SMD3AnimationInfo
SMD3AnimationInfo_ctor = func_type(ctypes.c_void_p)(('SMD3AnimationInfo_ctor', c_module))
SMD3AnimationInfo_delete = func_type(None, ctypes.c_void_p)(('SMD3AnimationInfo_delete', c_module))
SMD3AnimationInfo_get_first = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3AnimationInfo_get_first', c_module))
SMD3AnimationInfo_set_first = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3AnimationInfo_set_first', c_module))
SMD3AnimationInfo_get_num = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3AnimationInfo_get_num', c_module))
SMD3AnimationInfo_set_num = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3AnimationInfo_set_num', c_module))
SMD3AnimationInfo_get_looping = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3AnimationInfo_get_looping', c_module))
SMD3AnimationInfo_set_looping = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3AnimationInfo_set_looping', c_module))
SMD3AnimationInfo_get_fps = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3AnimationInfo_get_fps', c_module))
SMD3AnimationInfo_set_fps = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3AnimationInfo_set_fps', c_module))

#struct SMD3Header
SMD3Header_ctor = func_type(ctypes.c_void_p)(('SMD3Header_ctor', c_module))
SMD3Header_delete = func_type(None, ctypes.c_void_p)(('SMD3Header_delete', c_module))
SMD3Header_get_headerID = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3Header_get_headerID', c_module))
SMD3Header_set_headerID = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3Header_set_headerID', c_module))
SMD3Header_get_Version = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_Version', c_module))
SMD3Header_set_Version = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_Version', c_module))
SMD3Header_get_fileName = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Header_get_fileName', c_module))
SMD3Header_set_fileName = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Header_set_fileName', c_module))
SMD3Header_get_numFrames = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_numFrames', c_module))
SMD3Header_set_numFrames = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_numFrames', c_module))
SMD3Header_get_numTags = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_numTags', c_module))
SMD3Header_set_numTags = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_numTags', c_module))
SMD3Header_get_numMeshes = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_numMeshes', c_module))
SMD3Header_set_numMeshes = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_numMeshes', c_module))
SMD3Header_get_numMaxSkins = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_numMaxSkins', c_module))
SMD3Header_set_numMaxSkins = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_numMaxSkins', c_module))
SMD3Header_get_frameStart = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_frameStart', c_module))
SMD3Header_set_frameStart = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_frameStart', c_module))
SMD3Header_get_tagStart = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_tagStart', c_module))
SMD3Header_set_tagStart = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_tagStart', c_module))
SMD3Header_get_tagEnd = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_tagEnd', c_module))
SMD3Header_set_tagEnd = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_tagEnd', c_module))
SMD3Header_get_fileSize = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3Header_get_fileSize', c_module))
SMD3Header_set_fileSize = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3Header_set_fileSize', c_module))

#struct SMD3MeshHeader
SMD3MeshHeader_ctor = func_type(ctypes.c_void_p)(('SMD3MeshHeader_ctor', c_module))
SMD3MeshHeader_delete = func_type(None, ctypes.c_void_p)(('SMD3MeshHeader_delete', c_module))
SMD3MeshHeader_get_meshID = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3MeshHeader_get_meshID', c_module))
SMD3MeshHeader_set_meshID = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3MeshHeader_set_meshID', c_module))
SMD3MeshHeader_get_meshName = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3MeshHeader_get_meshName', c_module))
SMD3MeshHeader_set_meshName = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3MeshHeader_set_meshName', c_module))
SMD3MeshHeader_get_numFrames = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_numFrames', c_module))
SMD3MeshHeader_set_numFrames = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_numFrames', c_module))
SMD3MeshHeader_get_numShader = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_numShader', c_module))
SMD3MeshHeader_set_numShader = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_numShader', c_module))
SMD3MeshHeader_get_numVertices = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_numVertices', c_module))
SMD3MeshHeader_set_numVertices = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_numVertices', c_module))
SMD3MeshHeader_get_numTriangles = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_numTriangles', c_module))
SMD3MeshHeader_set_numTriangles = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_numTriangles', c_module))
SMD3MeshHeader_get_offset_triangles = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_offset_triangles', c_module))
SMD3MeshHeader_set_offset_triangles = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_offset_triangles', c_module))
SMD3MeshHeader_get_offset_shaders = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_offset_shaders', c_module))
SMD3MeshHeader_set_offset_shaders = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_offset_shaders', c_module))
SMD3MeshHeader_get_offset_st = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_offset_st', c_module))
SMD3MeshHeader_set_offset_st = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_offset_st', c_module))
SMD3MeshHeader_get_vertexStart = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_vertexStart', c_module))
SMD3MeshHeader_set_vertexStart = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_vertexStart', c_module))
SMD3MeshHeader_get_offset_end = func_type(ctypes.c_int, ctypes.c_void_p)(('SMD3MeshHeader_get_offset_end', c_module))
SMD3MeshHeader_set_offset_end = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMD3MeshHeader_set_offset_end', c_module))

#struct SMD3Vertex
SMD3Vertex_ctor = func_type(ctypes.c_void_p)(('SMD3Vertex_ctor', c_module))
SMD3Vertex_delete = func_type(None, ctypes.c_void_p)(('SMD3Vertex_delete', c_module))
SMD3Vertex_get_position = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Vertex_get_position', c_module))
SMD3Vertex_set_position = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Vertex_set_position', c_module))
SMD3Vertex_get_normal = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Vertex_get_normal', c_module))
SMD3Vertex_set_normal = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Vertex_set_normal', c_module))

#struct SMD3TexCoord
SMD3TexCoord_ctor = func_type(ctypes.c_void_p)(('SMD3TexCoord_ctor', c_module))
SMD3TexCoord_delete = func_type(None, ctypes.c_void_p)(('SMD3TexCoord_delete', c_module))
SMD3TexCoord_get_u = func_type(ctypes.c_float, ctypes.c_void_p)(('SMD3TexCoord_get_u', c_module))
SMD3TexCoord_set_u = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMD3TexCoord_set_u', c_module))
SMD3TexCoord_get_v = func_type(ctypes.c_float, ctypes.c_void_p)(('SMD3TexCoord_get_v', c_module))
SMD3TexCoord_set_v = func_type(None, ctypes.c_void_p, ctypes.c_float)(('SMD3TexCoord_set_v', c_module))

#struct SMD3Face
SMD3Face_ctor = func_type(ctypes.c_void_p)(('SMD3Face_ctor', c_module))
SMD3Face_delete = func_type(None, ctypes.c_void_p)(('SMD3Face_delete', c_module))
SMD3Face_get_Index = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Face_get_Index', c_module))
SMD3Face_set_Index = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Face_set_Index', c_module))

#struct SMD3MeshBuffer : public IReferenceCounted
SMD3MeshBuffer_ctor = func_type(ctypes.c_void_p)(('SMD3MeshBuffer_ctor', c_module))
SMD3MeshBuffer_delete = func_type(None, ctypes.c_void_p)(('SMD3MeshBuffer_delete', c_module))
SMD3MeshBuffer_get_MeshHeader = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_get_MeshHeader', c_module))
SMD3MeshBuffer_set_MeshHeader = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_set_MeshHeader', c_module))
SMD3MeshBuffer_get_Shader = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3MeshBuffer_get_Shader', c_module))
SMD3MeshBuffer_set_Shader = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3MeshBuffer_set_Shader', c_module))
SMD3MeshBuffer_get_Indices = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_get_Indices', c_module))
SMD3MeshBuffer_set_Indices = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_set_Indices', c_module))
SMD3MeshBuffer_get_Vertices = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_get_Vertices', c_module))
SMD3MeshBuffer_set_Vertices = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_set_Vertices', c_module))
SMD3MeshBuffer_get_Tex = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_get_Tex', c_module))
SMD3MeshBuffer_set_Tex = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3MeshBuffer_set_Tex', c_module))

#struct SMD3QuaternionTag
SMD3QuaternionTag_ctor1 = func_type(ctypes.c_void_p, ctypes.c_char_p)(('SMD3QuaternionTag_ctor1', c_module))
SMD3QuaternionTag_delete = func_type(None, ctypes.c_void_p)(('SMD3QuaternionTag_delete', c_module))
SMD3QuaternionTag_ctor2 = func_type(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p)(('SMD3QuaternionTag_ctor2', c_module))
SMD3QuaternionTag_ctor3 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_ctor3', c_module))
SMD3QuaternionTag_ctor4 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_ctor4', c_module))
SMD3QuaternionTag_setto = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_setto', c_module))
SMD3QuaternionTag_operator_eq = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_operator_eq', c_module))
SMD3QuaternionTag_operator_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_operator_set', c_module))
SMD3QuaternionTag_get_Name = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3QuaternionTag_get_Name', c_module))
SMD3QuaternionTag_set_Name = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3QuaternionTag_set_Name', c_module))
SMD3QuaternionTag_get_position = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_get_position', c_module))
SMD3QuaternionTag_set_position = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_set_position', c_module))
SMD3QuaternionTag_get_rotation = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_get_rotation', c_module))
SMD3QuaternionTag_set_rotation = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTag_set_rotation', c_module))

#struct SMD3QuaternionTagList
SMD3QuaternionTagList_ctor1 = func_type(ctypes.c_void_p)(('SMD3QuaternionTagList_ctor1', c_module))
SMD3QuaternionTagList_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTagList_ctor2', c_module))
SMD3QuaternionTagList_delete = func_type(None, ctypes.c_void_p)(('SMD3QuaternionTagList_delete', c_module))
SMD3QuaternionTagList_get = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)(('SMD3QuaternionTagList_get', c_module))
SMD3QuaternionTagList_size = func_type(ctypes.c_uint, ctypes.c_void_p)(('SMD3QuaternionTagList_size', c_module))
SMD3QuaternionTagList_set_used = func_type(None, ctypes.c_void_p, ctypes.c_uint)(('SMD3QuaternionTagList_set_used', c_module))
SMD3QuaternionTagList_const_operator_index = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SMD3QuaternionTagList_const_operator_index', c_module))
SMD3QuaternionTagList_operator_index = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SMD3QuaternionTagList_operator_index', c_module))
SMD3QuaternionTagList_push_back = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTagList_push_back', c_module))
SMD3QuaternionTagList_operator_set = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMD3QuaternionTagList_operator_set', c_module))
SMD3QuaternionTagList_set_tag_item = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_void_p)(('SMD3QuaternionTagList_set_tag_item', c_module))

#struct SMD3Mesh: public IReferenceCounted
SMD3Mesh_ctor = func_type(ctypes.c_void_p)(('SMD3Mesh_ctor', c_module))
SMD3Mesh_delete = func_type(None, ctypes.c_void_p)(('SMD3Mesh_delete', c_module))
SMD3Mesh_get_Name = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SMD3Mesh_get_Name', c_module))
SMD3Mesh_set_Name = func_type(None, ctypes.c_void_p, ctypes.c_char_p)(('SMD3Mesh_set_Name', c_module))
SMD3Mesh_get_Buffer = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_get_Buffer', c_module))
SMD3Mesh_set_Buffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_set_Buffer', c_module))
SMD3Mesh_get_TagList = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_get_TagList', c_module))
SMD3Mesh_set_TagList = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_set_TagList', c_module))
SMD3Mesh_get_MD3Header = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_get_MD3Header', c_module))
SMD3Mesh_set_MD3Header = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMD3Mesh_set_MD3Header', c_module))

# SMesh
SMesh_ctor1 = func_type(ctypes.c_void_p)(('SMesh_ctor1', c_module))
SMesh_ctor2 = func_type(ctypes.c_void_p, ctypes.c_int)(('SMesh_ctor2', c_module))
SMesh_delete = func_type(None, ctypes.c_void_p)(('SMesh_delete', c_module))
SMesh_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SMesh_get_item', c_module))
SMesh_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SMesh_set_item', c_module))
SMesh_getMeshBufferCount = func_type(ctypes.c_uint, ctypes.c_void_p)(('SMesh_getMeshBufferCount', c_module))
SMesh_getMeshBuffer1 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('SMesh_getMeshBuffer1', c_module))
SMesh_getMeshBuffer2 = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)(('SMesh_getMeshBuffer2', c_module))
SMesh_getBoundingBox = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMesh_getBoundingBox', c_module))
SMesh_setBoundingBox = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMesh_setBoundingBox', c_module))
SMesh_recalculateBoundingBox = func_type(None, ctypes.c_void_p)(('SMesh_recalculateBoundingBox', c_module))
SMesh_addMeshBuffer = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMesh_addMeshBuffer', c_module))
SMesh_setMaterialFlag = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_bool)(('SMesh_setMaterialFlag', c_module))
SMesh_setHardwareMappingHint = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int)(('SMesh_setHardwareMappingHint', c_module))
SMesh_setDirty = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SMesh_setDirty', c_module))
SMesh_get_MeshBuffers = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SMesh_get_MeshBuffers', c_module))
SMesh_set_MeshBuffers = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SMesh_set_MeshBuffers', c_module))

# SParticle
SParticle_ctor = func_type(ctypes.c_void_p, ctypes.c_int)(('SParticle_ctor', c_module))
SParticle_get_item = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_item', c_module))
SParticle_set_item = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_item', c_module))
SParticle_get_pos = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_pos', c_module))
SParticle_set_pos = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_pos', c_module))
SParticle_get_vector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_vector', c_module))
SParticle_set_vector = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_vector', c_module))
SParticle_get_startTime = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_startTime', c_module))
SParticle_set_startTime = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('SParticle_set_startTime', c_module))
SParticle_get_endTime = func_type(ctypes.c_uint, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_endTime', c_module))
SParticle_set_endTime = func_type(None, ctypes.c_void_p, ctypes.c_uint, ctypes.c_int)(('SParticle_set_endTime', c_module))
SParticle_get_color = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_color', c_module))
SParticle_set_color = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_color', c_module))
SParticle_get_startColor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_startColor', c_module))
SParticle_set_startColor = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_startColor', c_module))
SParticle_get_startVector = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_startVector', c_module))
SParticle_set_startVector = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_startVector', c_module))
SParticle_get_size = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_size', c_module))
SParticle_set_size = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_size', c_module))
SParticle_get_startSize = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_get_startSize', c_module))
SParticle_set_startSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('SParticle_set_startSize', c_module))

#================= SIrrlichtCreationParameters
SIrrlichtCreationParameters_ctor = func_type(ctypes.c_void_p)(('SIrrlichtCreationParameters_ctor', c_module))
SIrrlichtCreationParameters_get_DeviceType = func_type(ctypes.c_int, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_DeviceType', c_module))
SIrrlichtCreationParameters_set_DeviceType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SIrrlichtCreationParameters_set_DeviceType', c_module))
SIrrlichtCreationParameters_get_DriverType = func_type(ctypes.c_int, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_DriverType', c_module))
SIrrlichtCreationParameters_set_DriverType = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SIrrlichtCreationParameters_set_DriverType', c_module))
SIrrlichtCreationParameters_get_WindowSize = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_WindowSize', c_module))
SIrrlichtCreationParameters_set_WindowSize = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_set_WindowSize', c_module))
SIrrlichtCreationParameters_get_Bits = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Bits', c_module))
SIrrlichtCreationParameters_set_Bits = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_set_Bits', c_module))
SIrrlichtCreationParameters_get_ZBufferBits = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_ZBufferBits', c_module))
SIrrlichtCreationParameters_set_ZBufferBits = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_set_ZBufferBits', c_module))
SIrrlichtCreationParameters_get_Fullscreen = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Fullscreen', c_module))
SIrrlichtCreationParameters_set_Fullscreen = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_Fullscreen', c_module))
SIrrlichtCreationParameters_get_Stencilbuffer = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Stencilbuffer', c_module))
SIrrlichtCreationParameters_set_Stencilbuffer = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_Stencilbuffer', c_module))
SIrrlichtCreationParameters_get_Vsync = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Vsync', c_module))
SIrrlichtCreationParameters_set_Vsync = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_Vsync', c_module))
SIrrlichtCreationParameters_get_AntiAlias = func_type(ctypes.c_ubyte, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_AntiAlias', c_module))
SIrrlichtCreationParameters_set_AntiAlias = func_type(None, ctypes.c_void_p, ctypes.c_ubyte)(('SIrrlichtCreationParameters_set_AntiAlias', c_module))
SIrrlichtCreationParameters_get_WithAlphaChannel = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_WithAlphaChannel', c_module))
SIrrlichtCreationParameters_set_WithAlphaChannel = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_WithAlphaChannel', c_module))
SIrrlichtCreationParameters_get_Doublebuffer = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Doublebuffer', c_module))
SIrrlichtCreationParameters_set_Doublebuffer = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_Doublebuffer', c_module))
SIrrlichtCreationParameters_get_IgnoreInput = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_IgnoreInput', c_module))
SIrrlichtCreationParameters_set_IgnoreInput = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_IgnoreInput', c_module))
SIrrlichtCreationParameters_get_Stereobuffer = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_Stereobuffer', c_module))
SIrrlichtCreationParameters_set_Stereobuffer = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_Stereobuffer', c_module))
SIrrlichtCreationParameters_get_HighPrecisionFPU = func_type(ctypes.c_bool, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_HighPrecisionFPU', c_module))
SIrrlichtCreationParameters_set_HighPrecisionFPU = func_type(None, ctypes.c_void_p, ctypes.c_bool)(('SIrrlichtCreationParameters_set_HighPrecisionFPU', c_module))
SIrrlichtCreationParameters_get_EventReceiver = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_EventReceiver', c_module))
SIrrlichtCreationParameters_set_EventReceiver = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_set_EventReceiver', c_module))
SIrrlichtCreationParameters_get_WindowId = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_WindowId', c_module))
SIrrlichtCreationParameters_set_WindowId = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_set_WindowId', c_module))
SIrrlichtCreationParameters_get_LoggingLevel = func_type(ctypes.c_int, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_LoggingLevel', c_module))
SIrrlichtCreationParameters_set_LoggingLevel = func_type(None, ctypes.c_void_p, ctypes.c_int)(('SIrrlichtCreationParameters_set_LoggingLevel', c_module))
SIrrlichtCreationParameters_get_SDK_version_do_not_use = func_type(ctypes.c_char_p, ctypes.c_void_p)(('SIrrlichtCreationParameters_get_SDK_version_do_not_use', c_module))

#================= D3D8
D3D8_get_D3D8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D8_get_D3D8', c_module))
D3D8_get_D3DDev8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D8_get_D3DDev8', c_module))
D3D8_get_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D8_get_HWnd', c_module))
D3D8_set_D3D8 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D8_set_D3D8', c_module))
D3D8_set_D3DDev8 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D8_set_D3DDev8', c_module))
D3D8_set_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D8_set_HWnd', c_module))

#================= D3D9
D3D9_get_D3D9 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D9_get_D3D9', c_module))
D3D9_get_D3DDev9 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D9_get_D3DDev9', c_module))
D3D9_get_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('D3D9_get_HWnd', c_module))
D3D9_set_D3D9 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D9_set_D3D9', c_module))
D3D9_set_D3DDev9 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D9_set_D3DDev9', c_module))
D3D9_set_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('D3D9_set_HWnd', c_module))

#================= OpenGLWin32
OpenGLWin32_get_HDc = func_type(ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_get_HDc', c_module))
OpenGLWin32_get_HRc = func_type(ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_get_HRc', c_module))
OpenGLWin32_get_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_get_HWnd', c_module))
OpenGLWin32_set_HDc = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_set_HDc', c_module))
OpenGLWin32_set_HRc = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_set_HRc', c_module))
OpenGLWin32_set_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('OpenGLWin32_set_HWnd', c_module))

#================= OpenGLLinux
OpenGLLinux_get_X11Display = func_type(ctypes.c_void_p, ctypes.c_void_p)(('OpenGLLinux_get_X11Display', c_module))
OpenGLLinux_get_X11Context = func_type(ctypes.c_void_p, ctypes.c_void_p)(('OpenGLLinux_get_X11Context', c_module))
OpenGLLinux_get_X11Window = func_type(ctypes.c_ulong, ctypes.c_void_p)(('OpenGLLinux_get_X11Window', c_module))
OpenGLLinux_set_X11Display = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('OpenGLLinux_set_X11Display', c_module))
OpenGLLinux_set_X11Context = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('OpenGLLinux_set_X11Context', c_module))
OpenGLLinux_set_X11Window = func_type(None, ctypes.c_void_p, ctypes.c_ulong)(('OpenGLLinux_set_X11Window', c_module))

#================= SExposedVideoData
SExposedVideoData_ctor1 = func_type(ctypes.c_void_p)(('SExposedVideoData_ctor1', c_module))
SExposedVideoData_ctor2 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_ctor2', c_module))
#~ SExposedVideoData_destructor = func_type(None, ctypes.c_void_p)(('SExposedVideoData_destructor', c_module))
SExposedVideoData_get_D3D8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D8', c_module))
SExposedVideoData_get_D3D8_D3D8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D8_D3D8', c_module))
SExposedVideoData_get_D3D8_D3DDev8 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D8_D3DDev8', c_module))
SExposedVideoData_get_D3D8_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D8_HWnd', c_module))
SExposedVideoData_get_D3D9 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D9', c_module))
SExposedVideoData_get_D3D9_D3D9 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D9_D3D9', c_module))
SExposedVideoData_get_D3D9_D3DDev9 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D9_D3DDev9', c_module))
SExposedVideoData_get_D3D9_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_D3D9_HWnd', c_module))
SExposedVideoData_get_OpenGLWin32 = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLWin32', c_module))
SExposedVideoData_get_OpenGLWin32_HDc = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLWin32_HDc', c_module))
SExposedVideoData_get_OpenGLWin32_HRc = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLWin32_HRc', c_module))
SExposedVideoData_get_OpenGLWin32_HWnd = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLWin32_HWnd', c_module))
SExposedVideoData_get_OpenGLLinux = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLLinux', c_module))
SExposedVideoData_get_OpenGLLinux_X11Display = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLLinux_X11Display', c_module))
SExposedVideoData_get_OpenGLLinux_X11Context = func_type(ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLLinux_X11Context', c_module))
SExposedVideoData_get_OpenGLLinux_X11Window = func_type(ctypes.c_ulong, ctypes.c_void_p)(('SExposedVideoData_get_OpenGLLinux_X11Window', c_module))
SExposedVideoData_set_D3D8_D3D8 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D8_D3D8', c_module))
SExposedVideoData_set_D3D8_D3DDev8 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D8_D3DDev8', c_module))
SExposedVideoData_set_D3D8_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D8_HWnd', c_module))
SExposedVideoData_set_D3D9_D3D9 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D9_D3D9', c_module))
SExposedVideoData_set_D3D9_D3DDev9 = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D9_D3DDev9', c_module))
SExposedVideoData_set_D3D9_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_D3D9_HWnd', c_module))
SExposedVideoData_set_OpenGLWin32_HDc = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_OpenGLWin32_HDc', c_module))
SExposedVideoData_set_OpenGLWin32_HRc = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_OpenGLWin32_HRc', c_module))
SExposedVideoData_set_OpenGLWin32_HWnd = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_OpenGLWin32_HWnd', c_module))
SExposedVideoData_set_OpenGLLinux_X11Display = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_OpenGLLinux_X11Display', c_module))
SExposedVideoData_set_OpenGLLinux_X11Context = func_type(None, ctypes.c_void_p, ctypes.c_void_p)(('SExposedVideoData_set_OpenGLLinux_X11Context', c_module))
SExposedVideoData_set_OpenGLLinux_X11Window = func_type(None, ctypes.c_void_p, ctypes.c_ulong)(('SExposedVideoData_set_OpenGLLinux_X11Window', c_module))

#================= I3DText
BUILD_WITH_3D_TEXT = ctypes.c_bool.in_dll(c_module, 'BUILD_WITH_3D_TEXT').value
if BUILD_WITH_3D_TEXT:
	E_RCC_TYPE = 0
	RCC_NO = 0#NOT USED RANDOM COLORS
	RCC_AUTO = 1#USED RANDOM COLORS WITH AUTO CHANGES
	RCC_CUSTOM = 2#USED RANDOM COLORS WITH CUSTOM CHANGES

	E_ABSV_TYPE = 0
	ABSV_INTERLEAVE = 0#INTERLEAVE Z VALUE FOR ONE PASS, RESULT IS CURVE
	ABSV_INTERLEAVE_TWO_PASS = 1#RESULT IS TWO MIXED CURVE
	ABSV_LINEAR = 2#ONE PASS Z=0, LIKE FLAT TEXT, BUT AS 3D OBJECT
	ABSV_LINEAR_TWO_PASS = 3#FIRST PASS Z=0, SECOND PASS Z=DEPTH
	ABSV_PRIMITIVES = 4#VERTICES FOR DRAWING AS PRIMITIVES

	E_DAF_TYPE = 0
	DAF_NO = 0#NOT DRAW AS FIGURES
	DAF_CUBE = 1#DRAW AS CUBES
	DAF_SPHERE = 2#DRAW AS SPHERES
	DAF_CYLINDER = 3#DRAW AS CYLINDERS
	DAF_MIXED = 4#DRAW AS FIGURES WITH PRIMITIVES

	IText3DSimple_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IText3DSimple_ctor', c_module))
	IText3DSimple_setText = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_wchar_p, fschar_t, ctypes.c_uint, ctypes.c_float, ctypes.c_int, ctypes.c_int)(('IText3DSimple_setText', c_module))

	IText3D_ctor = func_type(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)(('IText3D_ctor', c_module))
	IText3D_setText = func_type(ctypes.c_bool, ctypes.c_void_p, ctypes.c_wchar_p, fschar_t, ctypes.c_uint, ctypes.c_float, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('IText3D_setText', c_module))
	IText3D_get_color_random_type = func_type(ctypes.c_int, ctypes.c_void_p)(('IText3D_get_color_random_type', c_module))
	IText3D_set_color_random_type = func_type(None, ctypes.c_void_p, ctypes.c_int)(('IText3D_set_color_random_type', c_module))
	IText3D_set_auto_emissive_color = func_type(None, ctypes.c_void_p)(('IText3D_set_auto_emissive_color', c_module))
	IText3D_get_draw_as_figures = func_type(ctypes.c_int, ctypes.c_void_p)(('IText3D_get_draw_as_figures', c_module))
	IText3D_set_draw_as_figures = func_type(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)(('IText3D_set_draw_as_figures', c_module))


# ============== Python classes

class array:
	def __init__(self, *args, **kwargs):
		self.c_pointer = array_ctor1()
		self.delete_c_pointer = True
		self._type_ = None
		if len(args) > 0:
			if isinstance(args[0], int):
				self.c_pointer = array_ctor2(args[0])
			elif hasattr(args[0], 'c_pointer') and isinstance(args[0], array):
				self.c_pointer = array_ctor3(args[0].c_pointer)
			#~ elif hasattr(args[0], '__name__'):
			elif callable(args[0]):
				self._type_ = args[0]
			else:
				self.c_pointer = array_ctor3(args[0])
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
		if '_type_' in kwargs:
			type_name = kwargs.pop('_type_', None)
			if callable(type_name):
				self._type_ = type_name
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				array_delete(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self.size()
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(key, value)
	def __delitem__(self, key):
		self.erase1(key)
	def __iter__(self):
		pass
	def __repr__(self):
		if self._type_:
			return '%s(%s)' % (self.__class__.__name__, self._type_.__name__)
		else:
			return '%s(unknown type)' % self.__class__.__name__
	def __str__(self):
		return self.__repr__()
	def reallocate(self, new_size):
		array_reallocate(self.c_pointer, new_size)
	def setAllocStrategy(self, newStrategy = ALLOC_STRATEGY_DOUBLE):
		array_setAllocStrategy(self.c_pointer, newStrategy)
	def push_back(self, element):
		if hasattr(element, 'c_pointer'):
			array_push_back(self.c_pointer, element.c_pointer)
		else:
			array_push_back(self.c_pointer, element)
	def push_front(self, element):
		if hasattr(element, 'c_pointer'):
			array_push_front(self.c_pointer, element.c_pointer)
		else:
			array_push_front(self.c_pointer, element)
	def insert(self, element, index = 0):
		if hasattr(element, 'c_pointer'):
			array_insert(self.c_pointer, element.c_pointer, index)
		else:
			array_insert(self.c_pointer, element, index)
	def clear(self):
		array_clear(self.c_pointer)
	def set_pointer(self, newPointer, size, _is_sorted = False, _free_when_destroyed = True):
		array_set_pointer(self.c_pointer, newPointer, size, _is_sorted, _free_when_destroyed)
	def set_free_when_destroyed(self, f):
		array_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		array_set_used(self.c_pointer, usedNow)
	def set(self, other):
		return array_set(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return array_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return array_operator_neq(self.c_pointer, other.c_pointer)
	def get_item(self, index = 0):
		if self._type_:
			return self._type_(array_get_item(self.c_pointer, index))
		else:
			return array_get_item(self.c_pointer, index)
	def set_item(self, index, element):
		if hasattr(element, 'c_pointer'):
			return array_set_item(self.c_pointer, index, element.c_pointer)
		else:
			return array_set_item(self.c_pointer, index, element)
	def getLast(self):
		return array_getLast(self.c_pointer)
	def pointer(self):
		return array_pointer(self.c_pointer)
	def const_pointer(self):
		return array_const_pointer(self.c_pointer)
	def size(self):
		return array_size(self.c_pointer)
	def allocated_size(self):
		return array_allocated_size(self.c_pointer)
	def empty(self):
		return array_empty(self.c_pointer)
	def sort(self):
		array_sort(self.c_pointer)
	def binary_search1(self, element):
		if hasattr(element, 'c_pointer'):
			return array_binary_search1(self.c_pointer, element.c_pointer)
		else:
			return array_binary_search1(self.c_pointer, element)
	def binary_search2(self, element, left, right):
		if hasattr(element, 'c_pointer'):
			return array_binary_search2(self.c_pointer, element.c_pointer, left, right)
		else:
			return array_binary_search2(self.c_pointer, element, left, right)
	def binary_search(self, *args):
		if len(args) == 1:
			return self.binary_search1(*args)
		else:
			return self.binary_search2(*args)
	def binary_search_multi(self, element, last):
		if hasattr(element, 'c_pointer'):
			return array_binary_search_multi(self.c_pointer, element.c_pointer, last)
		else:
			return array_binary_search_multi(self.c_pointer, element, last)
	def linear_search(self, element):
		if hasattr(element, 'c_pointer'):
			return array_linear_search(self.c_pointer, element.c_pointer)
		else:
			return array_linear_search(self.c_pointer, element)
	def linear_reverse_search(self, element):
		if hasattr(element, 'c_pointer'):
			return array_linear_reverse_search(self.c_pointer, element.c_pointer)
		else:
			return array_linear_reverse_search(self.c_pointer, element)
	def erase1(self, index):
		array_erase1(self.c_pointer, index)
	def erase2(self, index, count):
		array_erase2(self.c_pointer, index, count)
	def erase(self, *args):
		if len(args) == 1:
			self.erase1(*args)
		else:
			self.erase2(*args)
	def set_sorted(self, _is_sorted):
		array_set_sorted(self.c_pointer, _is_sorted)
	def swap(self, other):
		array_swap(self.c_pointer, other.c_pointer)
	def append(self, element):#extend like list method
		self.push_back(element)

class SJoystickInfo(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.length = 0
		self.delete_c_pointer = True
		if len(args) > 0:
			self.length = args[0]
			self.c_pointer = self.ctor(self.length)
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __len__(self):
		return self.length
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SJoystickInfo_delete(self.c_pointer)
			except:
				pass
	def ctor(self, length = 1):
		return SJoystickInfo_ctor(length)
	def get_Joystick(self):
		return SJoystickInfo_get_Joystick(self.c_pointer)
	def set_Joystick(self, value):
		SJoystickInfo_set_Joystick(self.c_pointer, value)
	def get_Name(self):
		return SJoystickInfo_get_Name(self.c_pointer)
	def set_Name(self, value):
		SJoystickInfo_set_Name(self.c_pointer, value)
	def get_Buttons(self):
		return SJoystickInfo_get_Buttons(self.c_pointer)
	def set_Buttons(self, value):
		SJoystickInfo_set_Buttons(self.c_pointer, value)
	def get_Axes(self):
		return SJoystickInfo_get_Axes(self.c_pointer)
	def set_Axes(self, value):
		SJoystickInfo_set_Axes(self.c_pointer, value)
	def get_PovHat(self):
		return SJoystickInfo_get_PovHat(self.c_pointer)
	Joystick = property(get_Joystick, set_Joystick)
	Name = property(get_Name, set_Name)
	Buttons = property(get_Buttons, set_Buttons)
	Axes = property(get_Axes, set_Axes)
	PovHat = property(get_PovHat)

class arraySJoystickInfo:
	def __init__(self):
		self.c_pointer = arraySJoystickInfo_ctor()
	def __del__(self):
		if self.c_pointer:
			try:
				arraySJoystickInfo_delete(self.c_pointer)
			except:
				pass
	def allocated_size(self):
		return arraySJoystickInfo_allocated_size(self.c_pointer)
	def size(self):
		return arraySJoystickInfo_size(self.c_pointer)
	def set_free_when_destroyed(self, f):
		arraySJoystickInfo_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		arraySJoystickInfo_set_used(self.c_pointer, usedNow)
	def get_item(self, index):
		return SJoystickInfo(c_pointer = arraySJoystickInfo_get_item(self.c_pointer, index))
	def __len__(self):
		return self.size()
	def __getitem__(self, index):
		return self.get_item(index)

class SViewFrustum(ctypes.Structure):
	_fields_ = [('cameraPosition', ctypes.c_void_p),
				('planes', ctypes.c_void_p),
				('boundingBox', ctypes.c_void_p)
				]
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
		elif 'matrix4' in kwargs:
			self.c_pointer = SMaterialLayer_ctor1(kwargs.pop('matrix4'))
		elif 'other' in kwargs:
			self.c_pointer = SMaterialLayer_ctor2(kwargs.pop('other'))
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def transform(self, mat):
		SViewFrustum_transform(self.c_pointer, mat)
	def getFarLeftUp(self):
		return SViewFrustum_getFarLeftUp(self.c_pointer)
	def getFarLeftDown(self):
		return SViewFrustum_getFarLeftDown(self.c_pointer)
	def getFarRightUp(self):
		return SViewFrustum_getFarRightUp(self.c_pointer)
	def getFarRightDown(self):
		return SViewFrustum_getFarRightDown(self.c_pointer)
	def getBoundingBox(self):
		return aabbox3df(SViewFrustum_getBoundingBox(self.c_pointer))
	def recalculateBoundingBox(self):
		SViewFrustum_recalculateBoundingBox(self.c_pointer)
	def setFrom(self, mat):
		SViewFrustum_setFrom(self.c_pointer, mat)
	def getTransform(self, state):
		return SViewFrustum_getTransform(self.c_pointer, state)
	def clipLine(self, line):
		return SViewFrustum_clipLine(self.c_pointer, line)

class IGUIElement: pass

class SGUIEvent(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetCaller(self):
		return IGUIElement(SGUIEvent_GetCaller(self.c_pointer))
	def GetElement(self):
		return IGUIElement(SGUIEvent_GetElement(self.c_pointer))
	def GetEventType(self):
		return SGUIEvent_GetEventType(self.c_pointer)
	Caller = property(GetCaller)
	Element = property(GetElement)
	EventType = property(GetEventType)

class SMouseInput(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetX(self):
		return SMouseInput_GetX(self.c_pointer)
	def GetY(self):
		return SMouseInput_GetY(self.c_pointer)
	def GetWheel(self):
		return SMouseInput_GetWheel(self.c_pointer)
	def GetShift(self):
		return SMouseInput_GetShift(self.c_pointer)
	def GetControl(self):
		return SMouseInput_GetControl(self.c_pointer)
	def GetButtonStates(self):
		return SMouseInput_GetButtonStates(self.c_pointer)
	def isLeftPressed(self):
		return SMouseInput_isLeftPressed(self.c_pointer)
	def isRightPressed(self):
		return SMouseInput_isRightPressed(self.c_pointer)
	def isMiddlePressed(self):
		return SMouseInput_isMiddlePressed(self.c_pointer)
	def GetEventType(self):
		return SMouseInput_GetEventType(self.c_pointer)
	def GetEvent(self):
		'for c++ compatibility'
		return SMouseInput_GetEventType(self.c_pointer)
	X = property(GetX)
	Y = property(GetY)
	Wheel = property(GetWheel)
	Shift = property(GetShift)
	Control = property(GetControl)
	ButtonStates = property(GetButtonStates)
	EventType = property(GetEventType)
	Event = property(GetEvent)

class SKeyInput(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetChar(self):
		return SKeyInput_GetChar(self.c_pointer)
	def GetKey(self):
		return SKeyInput_GetKey(self.c_pointer)
	def GetPressedDown(self):
		return SKeyInput_GetPressedDown(self.c_pointer)
	def GetShift(self):
		return SKeyInput_GetShift(self.c_pointer)
	def GetControl(self):
		return SKeyInput_GetControl(self.c_pointer)
	Char = property(GetChar)
	Key = property(GetKey)
	PressedDown = property(GetPressedDown)
	Shift = property(GetShift)
	Control = property(GetControl)

class SJoystickEvent(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetButtonStates(self):
		return SJoystickEvent_GetButtonStates(self.c_pointer)
	def GetAxis(self):
		return SJoystickEvent_GetAxis(self.c_pointer)
	def GetPOV(self):
		return SJoystickEvent_GetPOV(self.c_pointer)
	def GetJoystick(self):
		return SJoystickEvent_GetJoystick(self.c_pointer)
	def IsButtonPressed(self):
		return SJoystickEvent_IsButtonPressed(self.c_pointer)
	ButtonStates = property(GetButtonStates)
	Axis = property(GetAxis)
	POV = property(GetPOV)
	Joystick = property(GetJoystick)

class SLogEvent(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetText(self):
		return SLogEvent_GetText(self.c_pointer)
	def GetLevel(self):
		return SLogEvent_GetLevel(self.c_pointer)
	Text = property(GetText)
	Level = property(GetLevel)

class SUserEvent(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetUserData1(self):
		return SUserEvent_GetUserData1(self.c_pointer)
	def GetUserData2(self):
		return SUserEvent_GetUserData2(self.c_pointer)
	UserData1 = property(GetUserData1)
	UserData2 = property(GetUserData2)

if IRR_USE_INPUT_METHOD:
	class SInputMethodEvent(object):
		def __init__(self, *args, **kwargs):
			self.c_pointer = args[0]
		def GetHandle(self):
			return SInputMethodEvent_GetHandle(self.c_pointer)
		def GetChar(self):
			return SInputMethodEvent_GetChar(self.c_pointer)
		def GetEvent(self):
			return SInputMethodEvent_GetEvent(self.c_pointer)
		Handle = property(GetHandle)
		Char = property(GetChar)
		Event = property(GetEvent)

class SEvent(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def GetGUIEvent(self):
		return SGUIEvent(SEvent_GetSGUIEvent(self.c_pointer))
	def GetMouseInput(self):
		return SMouseInput(SEvent_GetSMouseInput(self.c_pointer))
	def GetKeyInput(self):
		return SKeyInput(SEvent_GetSKeyInput(self.c_pointer))
	def GetJoystickEvent(self):
		return SJoystickEvent(SEvent_GetSJoystickEvent(self.c_pointer))
	def GetLogEvent(self):
		return SLogEvent(SEvent_GetSLogEvent(self.c_pointer))
	def GetUserEvent(self):
		return SUserEvent(SEvent_GetSUserEvent(self.c_pointer))
	def GetEventType(self):
		return SEvent_GetEventType(self.c_pointer)
	GUIEvent = property(GetGUIEvent)
	MouseInput = property(GetMouseInput)
	KeyInput = property(GetKeyInput)
	JoystickEvent = property(GetJoystickEvent)
	LogEvent = property(GetLogEvent)
	UserEvent = property(GetUserEvent)
	EventType = property(GetEventType)
	if IRR_USE_INPUT_METHOD:
		def GetInputMethodEvent(self):
			return SInputMethodEvent(SEvent_GetSInputMethodEvent(self.c_pointer))
		InputMethodEvent = property(GetInputMethodEvent)


class IEventReceiver:
	set_virtual_method = func_type(ctypes.c_bool, ctypes.c_void_p, OnEventFunc, ctypes.c_int)(('set_virtual_method', c_module))
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		self.callback = OnEventFunc(self.OnEvent)
		if len(args) > 0:
			self.c_pointer = IEventReceiver_ctor1(args[0])
			self.delete_c_pointer = False
		else:
			self.c_pointer = IEventReceiver_ctor2(self.callback)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				IEventReceiver_delete(self.c_pointer)
			except:
				pass
	def set_virt_method(self, new_method, method_index = 0):
		return self.set_virtual_method(self.c_pointer, OnEventFunc(new_method), method_index)
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def set_func_event(self, event_func):
		IEventReceiver_set_func_event(self.c_pointer, event_func)
	def OnEvent(self, event):
		'''OnEvent must be replaced with custom IEventReceiver class.
		for access to event as class doing next,
		event_class = SEvent(event)'''
		print(self.OnEvent.__doc__)
		return False
	def convert_pointer(self):
		self.c_pointer = IEventReceiver_ctor1(self.c_pointer)
	def GetEventType(self, event_pointer):
		return SEvent_GetEventType(event_pointer)
	def GetGUIEvent(self, event_pointer):
		return SEvent_GetSGUIEvent(event_pointer)
	def GUIEvent_Caller(self, event_pointer):
		return IGUIElement(SGUIEvent_GetCaller(event_pointer))
	def GUIEvent_Element(self, event_pointer):
		return IGUIElement(SGUIEvent_GetElement(event_pointer))
	def GUIEvent_EventType(self, event_pointer):
		return SGUIEvent_GetEventType(event_pointer)
	def GetMouseInput(self, event_pointer):
		return SEvent_GetSMouseInput(event_pointer)
	def MouseInput_X(self, event_pointer):
		return SMouseInput_GetX(event_pointer)
	def MouseInput_Y(self, event_pointer):
		return SMouseInput_GetY(event_pointer)
	def MouseInput_Wheel(self, event_pointer):
		return SMouseInput_GetWheel(event_pointer)
	def MouseInput_Shift(self, event_pointer):
		return SMouseInput_GetShift(event_pointer)
	def MouseInput_Control(self, event_pointer):
		return SMouseInput_GetControl(event_pointer)
	def MouseInput_ButtonStates(self, event_pointer):
		return SMouseInput_GetButtonStates(event_pointer)
	def MouseInput_isLeftPressed(self, event_pointer):
		return SMouseInput_isLeftPressed(event_pointer)
	def MouseInput_isRightPressed(self, event_pointer):
		return SMouseInput_isRightPressed(event_pointer)
	def MouseInput_isMiddlePressed(self, event_pointer):
		return SMouseInput_isMiddlePressed(event_pointer)
	def MouseInput_EventType(self, event_pointer):
		return SMouseInput_GetEventType(event_pointer)
	def GetKeyInput(self, event_pointer):
		return SEvent_GetSKeyInput(event_pointer)
	def KeyInput_Char(self, event_pointer):
		return SKeyInput_GetChar(event_pointer)
	def KeyInput_Key(self, event_pointer):
		return SKeyInput_GetKey(event_pointer)
	def KeyInput_PressedDown(self, event_pointer):
		return SKeyInput_GetPressedDown(event_pointer)
	def KeyInput_Shift(self, event_pointer):
		return SKeyInput_GetShift(event_pointer)
	def KeyInput_Control(self, event_pointer):
		return SKeyInput_GetControl(event_pointer)
	def GetJoystickEvent(self, event_pointer):
		return SEvent_GetSJoystickEvent(event_pointer)
	def JoystickEvent_ButtonStates(self, event_pointer):
		return SJoystickEvent_GetButtonStates(event_pointer)
	def JoystickEvent_Axis(self, event_pointer):
		return SJoystickEvent_GetAxis(event_pointer)
	def JoystickEvent_POV(self, event_pointer):
		return SJoystickEvent_GetPOV(event_pointer)
	def JoystickEvent_Joystick(self, event_pointer):
		return SJoystickEvent_GetJoystick(event_pointer)
	def JoystickEvent_IsButtonPressed(self, event_pointer):
		return SJoystickEvent_IsButtonPressed(event_pointer)
	def GetLogEvent(self, event_pointer):
		return SEvent_GetSLogEvent(event_pointer)
	def LogEvent_Text(self, event_pointer):
		return SLogEvent_GetText(event_pointer)
	def LogEvent_Level(self, event_pointer):
		return SLogEvent_GetLevel(event_pointer)
	def GetUserEvent(self, event_pointer):
		return SEvent_GetSUserEvent(event_pointer)
	def UserEvent_UserData1(self, event_pointer):
		return SUserEvent_GetUserData1(event_pointer)
	def UserEvent_UserData2(self, event_pointer):
		return SUserEvent_GetUserData2(event_pointer)
	#~ def set_event_attributes(self, e, gui_event = False, mouse_event = False, key_event = False, joystick_event = False, log_event = False, user_event = False, input_method_event = False):
		#~ e.EventType = SEvent_GetEventType(e)
		#~ if gui_event:
			#~ e.GUIEvent = SEvent_GetSGUIEvent(e)
			#~ e.GUIEvent.Caller = IGUIElement(SGUIEvent_GetCaller(e.GUIEvent))
			#~ e.GUIEvent.Element = IGUIElement(SGUIEvent_GetElement(e.GUIEvent))
			#~ e.GUIEvent.EventType = SGUIEvent_GetEventType(e.GUIEvent)
		#~ if mouse_event:
			#~ e.MouseInput = SEvent_GetSMouseInput(e)
			#~ e.MouseInput.X = SMouseInput_GetX(e.MouseInput)
			#~ e.MouseInput.Y = SMouseInput_GetY(e.MouseInput)
			#~ e.MouseInput.Wheel = SMouseInput_GetWheel(e.MouseInput)
			#~ e.MouseInput.Shift = SMouseInput_GetShift(e.MouseInput)
			#~ e.MouseInput.Control = SMouseInput_GetControl(e.MouseInput)
			#~ e.MouseInput.ButtonStates = SMouseInput_GetButtonStates(e.MouseInput)
			#~ e.MouseInput.isLeftPressed = lambda : SMouseInput_isLeftPressed(e.MouseInput)
			#~ e.MouseInput.isRightPressed = lambda : SMouseInput_isRightPressed(e.MouseInput)
			#~ e.MouseInput.isMiddlePressed = lambda : SMouseInput_isMiddlePressed(e.MouseInput)
			#~ e.MouseInput.EventType = SMouseInput_GetEventType(e.MouseInput)
		#~ if key_event:
			#~ e.KeyInput = SEvent_GetSKeyInput(e)
			#~ e.KeyInput.Char = SKeyInput_GetChar(e.KeyInput)
			#~ e.KeyInput.Key = SKeyInput_GetKey(e.KeyInput)
			#~ e.KeyInput.PressedDown = SKeyInput_GetPressedDown(e.KeyInput)
			#~ e.KeyInput.Shift = SKeyInput_GetShift(e.KeyInput)
			#~ e.KeyInput.Control = SKeyInput_GetControl(e.KeyInput)
		#~ if joystick_event:
			#~ e.JoystickEvent = SEvent_GetSJoystickEvent(e)
			#~ e.JoystickEvent.ButtonStates = SJoystickEvent_GetButtonStates(e.JoystickEvent)
			#~ e.JoystickEvent.Axis = SJoystickEvent_GetAxis(e.JoystickEvent)
			#~ e.JoystickEvent.POV = SJoystickEvent_GetPOV(e.JoystickEvent)
			#~ e.JoystickEvent.Joystick = SJoystickEvent_GetJoystick(e.JoystickEvent)
			#~ e.JoystickEvent.IsButtonPressed = lambda button: SJoystickEvent_IsButtonPressed(e.JoystickEvent, button)
		#~ if log_event:
			#~ e.LogEvent = SEvent_GetSLogEvent(e)
			#~ try:
				#~ e.LogEvent.Text = SLogEvent_GetText(e.LogEvent)
			#~ except:
				#~ e.LogEvent.Text = ''
			#~ e.LogEvent.Level = SLogEvent_GetLevel(e.LogEvent)
		#~ if user_event:
			#~ e.UserEvent = SEvent_GetSUserEvent(e)
			#~ e.UserEvent.UserData1 = SUserEvent_GetUserData1(e.UserEvent)
			#~ e.UserEvent.UserData2 = SUserEvent_GetUserData2(e.UserEvent)
		#~ if input_method_event and IRR_USE_INPUT_METHOD:
			#~ e.InputMethodEvent = SEvent_GetSInputMethodEvent(e)
			#~ e.InputMethodEvent.Handle = SInputMethodEvent_GetHandle(e)
			#~ e.InputMethodEvent.Char = SInputMethodEvent_GetChar(e)
			#~ e.InputMethodEvent.Event = SInputMethodEvent_GetEvent(e)
	#~ def _set_event_attributes(self, e, gui_event = False, mouse_event = False, key_event = False, joystick_event = False, log_event = False, user_event = False, input_method_event = False):
		#~ _SEvent_ = ctypes.py_object(e)
		#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('EventType'), ctypes.py_object(SEvent_GetEventType(e)))
		#~ if gui_event:
			#~ _SGUIEvent = SEvent_GetSGUIEvent(e)
			#~ _SGUIEvent_ = ctypes.py_object(_SGUIEvent)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('GUIEvent'), _SGUIEvent_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SGUIEvent_, ctypes.py_object('Caller'), ctypes.py_object(SGUIEvent_GetCaller(_SGUIEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SGUIEvent_, ctypes.py_object('Element'), ctypes.py_object(SGUIEvent_GetElement(_SGUIEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SGUIEvent_, ctypes.py_object('EventType'), ctypes.py_object(SGUIEvent_GetEventType(_SGUIEvent)))
		#~ if mouse_event:
			#~ _SMouseInput = SEvent_GetSMouseInput(e)
			#~ _SMouseInput_ = ctypes.py_object(_SMouseInput)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('MouseInput'), _SMouseInput_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('X'), ctypes.py_object(SMouseInput_GetX(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('Y'), ctypes.py_object(SMouseInput_GetY(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('Wheel'), ctypes.py_object(SMouseInput_GetWheel(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('Shift'), ctypes.py_object(SMouseInput_GetShift(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('Control'), ctypes.py_object(SMouseInput_GetControl(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('ButtonStates'), ctypes.py_object(SMouseInput_GetButtonStates(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('isLeftPressed'), ctypes.py_object(lambda : SMouseInput_isLeftPressed(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('isRightPressed'), ctypes.py_object(lambda : SMouseInput_isRightPressed(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('isMiddlePressed'), ctypes.py_object(lambda : SMouseInput_isMiddlePressed(_SMouseInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SMouseInput_, ctypes.py_object('EventType'), ctypes.py_object(SMouseInput_GetEventType(_SMouseInput)))
		#~ if key_event:
			#~ _SKeyInput = SEvent_GetSKeyInput(e)
			#~ _SKeyInput_ = ctypes.py_object(_SKeyInput)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('KeyInput'), _SKeyInput_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SKeyInput_, ctypes.py_object('Char'), ctypes.py_object(SKeyInput_GetChar(_SKeyInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SKeyInput_, ctypes.py_object('Key'), ctypes.py_object(SKeyInput_GetKey(_SKeyInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SKeyInput_, ctypes.py_object('PressedDown'), ctypes.py_object(SKeyInput_GetPressedDown(_SKeyInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SKeyInput_, ctypes.py_object('Shift'), ctypes.py_object(SKeyInput_GetShift(_SKeyInput)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SKeyInput_, ctypes.py_object('Control'), ctypes.py_object(SKeyInput_GetControl(_SKeyInput)))
		#~ if joystick_event:
			#~ _SJoystickEvent = SEvent_GetSJoystickEvent(e)
			#~ _SJoystickEvent_ = ctypes.py_object(_SJoystickEvent)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('JoystickEvent'), _SJoystickEvent_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SJoystickEvent_, ctypes.py_object('ButtonStates'), ctypes.py_object(SJoystickEvent_GetButtonStates(_SJoystickEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SJoystickEvent_, ctypes.py_object('Axis'), ctypes.py_object(SJoystickEvent_GetAxis(_SJoystickEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SJoystickEvent_, ctypes.py_object('POV'), ctypes.py_object(SJoystickEvent_GetPOV(_SJoystickEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SJoystickEvent_, ctypes.py_object('Joystick'), ctypes.py_object(SJoystickEvent_GetJoystick(_SJoystickEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SJoystickEvent_, ctypes.py_object('IsButtonPressed'), ctypes.py_object(lambda button: SJoystickEvent_IsButtonPressed(_SJoystickEvent, button)))
		#~ if log_event:
			#~ _SLogEvent = SEvent_GetSLogEvent(e)
			#~ _SLogEvent_ = ctypes.py_object(_SLogEvent)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('LogEvent'), _SLogEvent_)
			#~ try:
				#~ ctypes.pythonapi.PyObject_SetAttr(_SLogEvent_, ctypes.py_object('Text'), ctypes.py_object(SLogEvent_GetText(_SLogEvent)))
			#~ except:
				#~ ctypes.pythonapi.PyObject_SetAttr(_SLogEvent_, ctypes.py_object('Text'), ctypes.py_object(''))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SLogEvent_, ctypes.py_object('Level'), ctypes.py_object(SLogEvent_GetLevel(_SLogEvent)))
		#~ if user_event:
			#~ _SUserEvent = SEvent_GetSUserEvent(e)
			#~ _SUserEvent_ = ctypes.py_object(_SUserEvent)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('UserEvent'), _SUserEvent_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SUserEvent_, ctypes.py_object('UserData1'), ctypes.py_object(SUserEvent_GetUserData1(_SUserEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SUserEvent_, ctypes.py_object('UserData2'), ctypes.py_object(SUserEvent_GetUserData2(_SUserEvent)))
		#~ if input_method_event and IRR_USE_INPUT_METHOD:
			#~ _SInputMethodEvent = SEvent_GetSInputMethodEvent(e)
			#~ _SInputMethodEvent_ = ctypes.py_object(_SInputMethodEvent)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SEvent_, ctypes.py_object('InputMethodEvent'), _SInputMethodEvent_)
			#~ ctypes.pythonapi.PyObject_SetAttr(_SInputMethodEvent_, ctypes.py_object('Handle'), ctypes.py_object(SInputMethodEvent_GetHandle(_SInputMethodEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SInputMethodEvent_, ctypes.py_object('Char'), ctypes.py_object(SInputMethodEvent_GetChar(_SInputMethodEvent)))
			#~ ctypes.pythonapi.PyObject_SetAttr(_SInputMethodEvent_, ctypes.py_object('Event'), ctypes.py_object(SInputMethodEvent_GetEvent(_SInputMethodEvent)))

class vector2df:
	def __init__(self, *args, **kwargs):
		pass
class vector2di:
	def __init__(self, *args, **kwargs):
		pass
class dimension2df:
	def __init__(self, *args, **kwargs):
		pass
class dimension2du:
	def __init__(self, *args, **kwargs):
		pass
class dimension2di:
	def __init__(self, *args, **kwargs):
		pass

class vector2df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 2:
			self.c_pointer = vector2df_ctor1(*args)
		elif len(args) == 1:
			if isinstance(args[0], float):
				self.c_pointer = vector2df_ctor2(args[0])
			elif isinstance(args[0], vector2df):
				self.c_pointer = vector2df_ctor3(args[0].c_pointer)
			elif hasattr(args[0], 'c_pointer'):
				self.c_pointer = vector2df_ctor4(args[0].c_pointer)
			else:
				self.c_pointer = args[0]
				self.delete_c_pointer = False
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				vector2df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def operator_sub(self):
		return vector2df(vector2df_operator_sub(self.c_pointer))
	def operator_set_other(self, other):
		return vector2df(vector2df_operator_set_other(self.c_pointer, other.c_pointer))
	def operator_set_dimension2d(self, other):
		return vector2df(vector2df_operator_set_dimension2d(self.c_pointer, other.c_pointer))
	def __add__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_add_value(self.c_pointer, value))
		elif isinstance(value, dimension2df):
			return vector2df(vector2df_operator_add_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2df(vector2df_operator_add_other(self.c_pointer, value.c_pointer))
	def __iadd__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_set_add_value(self.c_pointer, value))
		elif isinstance(value, dimension2df):
			return vector2df(vector2df_operator_set_add_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2df(vector2df_operator_set_add_other(self.c_pointer, value.c_pointer))
	def __sub__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_sub_value(self.c_pointer, value))
		elif isinstance(value, dimension2df):
			return vector2df(vector2df_operator_sub_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2df(vector2df_operator_sub_other(self.c_pointer, value.c_pointer))
	def __sub__(self, value):
		if isinstance(value, float):
			return vector2df((self.c_pointer, value))
		elif isinstance(value, dimension2df):
			return vector2df((self.c_pointer, value.c_pointer))
		else:
			return vector2df((self.c_pointer, value.c_pointer))
	def __isub__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_set_sub_value(self.c_pointer, value))
		elif isinstance(value, dimension2df):
			return vector2df(vector2df_operator_set_sub_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2df(vector2df_operator_set_sub_other(self.c_pointer, value.c_pointer))
	def __mul__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_mult_value(self.c_pointer, value))
		else:
			return vector2df(vector2df_operator_mult_other(self.c_pointer, value.c_pointer))
	def __imul__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_set_mult_value(self.c_pointer, value))
		else:
			return vector2df(vector2df_operator_set_mult_other(self.c_pointer, value.c_pointer))
	def __div__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_div_value(self.c_pointer, value))
		else:
			return vector2df(vector2df_operator_div_other(self.c_pointer, value.c_pointer))
	def __idiv__(self, value):
		if isinstance(value, float):
			return vector2df(vector2df_operator_set_div_value(self.c_pointer, value))
		else:
			return vector2df(vector2df_operator_set_div_other(self.c_pointer, value.c_pointer))
	def __le__(self, other):
		return vector2df_operator_le(self.c_pointer, other.c_pointer)
	def __ge__(self, other):
		return vector2df_operator_ge(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return vector2df_operator_lt(self.c_pointer, other.c_pointer)
	def __gt__(self, other):
		return vector2df_operator_gt(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return vector2df_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return vector2df_operator_ne(self.c_pointer, other.c_pointer)
	def equals(self, other):
		return vector2df_equals(self.c_pointer, other.c_pointer)
	def set(self, *args):
		if len(args) == 2:
			return vector2df(vector2df_set(self.c_pointer, *args))
		else:
			return vector2df(vector2df_set2(self.c_pointer, args[0].c_pointer))
	def set1(self, nx, ny):
		return vector2df(vector2df_set(self.c_pointer, nx, ny))
	def set2(self, p):
		return vector2df(vector2df_set2(self.c_pointer, p.c_pointer))
	def getLength(self):
		return vector2df_getLength(self.c_pointer)
	def getLengthSQ(self):
		return vector2df_getLengthSQ(self.c_pointer)
	def dotProduct(self, other):
		return vector2df_dotProduct(self.c_pointer, other.c_pointer)
	def getDistanceFrom(self, other):
		return vector2df_getDistanceFrom(self.c_pointer, other.c_pointer)
	def getDistanceFromSQ(self, other):
		return vector2df_getDistanceFromSQ(self.c_pointer, other.c_pointer)
	def rotateBy(self, degrees, center):
		return vector2df(vector2df_rotateBy(self.c_pointer, degrees, center.c_pointer))
	def normalize(self):
		return vector2df(vector2df_normalize(self.c_pointer))
	def getAngleTrig(self, other):
		return vector2df_getAngleTrig(self.c_pointer)
	def getAngle(self):
		return vector2df_getAngle(self.c_pointer)
	def getAngleWith(self, b):
		return vector2df_getAngleWith(self.c_pointer, b.c_pointer)
	def isBetweenPoints(self, begin, end):
		return vector2df_isBetweenPoints(self.c_pointer, begin.c_pointer, end.c_pointer)
	def getInterpolated(self, other, d):
		return vector2df(vector2df_getInterpolated(self.c_pointer, other.c_pointer, d))
	def getInterpolated_quadratic(self, v2, v3, d):
		return vector2df(vector2df_getInterpolated_quadratic(self.c_pointer, v2.c_pointer, v3.c_pointer, d))
	def interpolate(self, a, b, d):
		return vector2df(vector2df_interpolate(self.c_pointer, a.c_pointer, b.c_pointer, d))
	def get_X(self):
		return vector2df_get_X(self.c_pointer)
	def set_X(self, value):
		vector2df_set_X(self.c_pointer, value)
	def get_Y(self):
		return vector2df_get_Y(self.c_pointer)
	def set_Y(self, value):
		vector2df_set_Y(self.c_pointer, value)
	X = property(get_X, set_X)
	Y = property(get_Y, set_Y)
	def __repr__(self):
		return '%s(%f, %f)' % (self.__class__.__name__, self.X, self.Y)
	def __str__(self):
		return self.__repr__()
	def get_XY(self):
		return (vector2df_get_X(self.c_pointer), vector2df_get_Y(self.c_pointer))

class vector2di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = False
		if len(args) == 2:
			self.c_pointer = vector2di_ctor1(*args)
			self.delete_c_pointer = True
		elif len(args) == 1:
			if isinstance(args[0], int):
				self.c_pointer = vector2di_ctor2(args[0])
			elif isinstance(args[0], vector2di):
				self.c_pointer = vector2di_ctor3(args[0].c_pointer)
			elif hasattr(args[0], 'c_pointer'):
				self.c_pointer = vector2di_ctor4(args[0].c_pointer)
			self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				vector2di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def operator_sub(self):
		return vector2di(vector2di_operator_sub(self.c_pointer))
	def operator_set_other(self, other):
		return vector2di(vector2di_operator_set_other(self.c_pointer, other.c_pointer))
	def operator_set_dimension2d(self, other):
		return vector2di(vector2di_operator_set_dimension2d(self.c_pointer, other.c_pointer))
	def __add__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_add_value(self.c_pointer, value))
		elif isinstance(value, dimension2di):
			return vector2di(vector2di_operator_add_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2di(vector2di_operator_add_other(self.c_pointer, value.c_pointer))
	def __iadd__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_set_add_value(self.c_pointer, value))
		elif isinstance(value, dimension2di):
			return vector2di(vector2di_operator_set_add_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2di(vector2di_operator_set_add_other(self.c_pointer, value.c_pointer))
	def __sub__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_sub_value(self.c_pointer, value))
		elif isinstance(value, dimension2di):
			return vector2di(vector2di_operator_sub_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2di(vector2di_operator_sub_other(self.c_pointer, value.c_pointer))
	def __sub__(self, value):
		if isinstance(value, int):
			return vector2di((self.c_pointer, value))
		elif isinstance(value, dimension2di):
			return vector2di((self.c_pointer, value.c_pointer))
		else:
			return vector2di((self.c_pointer, value.c_pointer))
	def __isub__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_set_sub_value(self.c_pointer, value))
		elif isinstance(value, dimension2di):
			return vector2di(vector2di_operator_set_sub_dimension2d(self.c_pointer, value.c_pointer))
		else:
			return vector2di(vector2di_operator_set_sub_other(self.c_pointer, value.c_pointer))
	def __mul__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_mult_value(self.c_pointer, value))
		else:
			return vector2di(vector2di_operator_mult_other(self.c_pointer, value.c_pointer))
	def __imul__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_set_mult_value(self.c_pointer, value))
		else:
			return vector2di(vector2di_operator_set_mult_other(self.c_pointer, value.c_pointer))
	def __div__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_div_value(self.c_pointer, value))
		else:
			return vector2di(vector2di_operator_div_other(self.c_pointer, value.c_pointer))
	def __idiv__(self, value):
		if isinstance(value, int):
			return vector2di(vector2di_operator_set_div_value(self.c_pointer, value))
		else:
			return vector2di(vector2di_operator_set_div_other(self.c_pointer, value.c_pointer))
	def __le__(self, other):
		return vector2di_operator_le(self.c_pointer, other.c_pointer)
	def __ge__(self, other):
		return vector2di_operator_ge(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return vector2di_operator_lt(self.c_pointer, other.c_pointer)
	def __gt__(self, other):
		return vector2di_operator_gt(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return vector2di_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return vector2di_operator_ne(self.c_pointer, other.c_pointer)
	def equals(self, other):
		return vector2di_equals(self.c_pointer, other.c_pointer)
	def set(self, *args):
		if len(args) == 2:
			return vector2di(vector2di_set(self.c_pointer, *args))
		else:
			return vector2di(vector2di_set2(self.c_pointer, args[0].c_pointer))
	def set1(self, nx, ny):
		return vector2di(vector2di_set(self.c_pointer, nx, ny))
	def set2(self, p):
		return vector2di(vector2di_set2(self.c_pointer, p.c_pointer))
	def getLength(self):
		return vector2di_getLength(self.c_pointer)
	def getLengthSQ(self):
		return vector2di_getLengthSQ(self.c_pointer)
	def dotProduct(self, other):
		return vector2di_dotProduct(self.c_pointer, other.c_pointer)
	def getDistanceFrom(self, other):
		return vector2di_getDistanceFrom(self.c_pointer, other.c_pointer)
	def getDistanceFromSQ(self, other):
		return vector2di_getDistanceFromSQ(self.c_pointer, other.c_pointer)
	def rotateBy(self, degrees, center):
		return vector2di(vector2di_rotateBy(self.c_pointer, degrees, center.c_pointer))
	def normalize(self):
		return vector2di(vector2di_normalize(self.c_pointer))
	#~ def getAngleTrig(self, other):
		#~ return vector2di_getAngleTrig(self.c_pointer)
	def getAngle(self):
		return vector2di_getAngle(self.c_pointer)
	def getAngleWith(self, b):
		return vector2di_getAngleWith(self.c_pointer, b.c_pointer)
	def isBetweenPoints(self, begin, end):
		return vector2di_isBetweenPoints(self.c_pointer, begin.c_pointer, end.c_pointer)
	def getInterpolated(self, other, d):
		return vector2di(vector2di_getInterpolated(self.c_pointer, other.c_pointer, d))
	def getInterpolated_quadratic(self, v2, v3, d):
		return vector2di(vector2di_getInterpolated_quadratic(self.c_pointer, v2.c_pointer, v3.c_pointer, d))
	def interpolate(self, a, b, d):
		return vector2di(vector2di_interpolate(self.c_pointer, a.c_pointer, b.c_pointer, d))
	def get_X(self):
		return vector2di_get_X(self.c_pointer)
	def set_X(self, value):
		vector2di_set_X(self.c_pointer, value)
	def get_Y(self):
		return vector2di_get_Y(self.c_pointer)
	def set_Y(self, value):
		vector2di_set_Y(self.c_pointer, value)
	X = property(get_X, set_X)
	Y = property(get_Y, set_Y)
	def __repr__(self):
		return '%s(%d, %d)' % (self.__class__.__name__, self.X, self.Y)
	def __str__(self):
		return self.__repr__()
	def get_XY(self):
		return (vector2di_get_X(self.c_pointer), vector2di_get_Y(self.c_pointer))

class vector2du(vector2di):
	pass

class position2df(vector2df):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = position2df_ctor2(0)
			self.delete_c_pointer = True
		elif len(args) == 1:
			if isinstance(args[0], float):
				self.c_pointer = position2df_ctor2(args[0])
			elif isinstance(args[0], vector2df):
				self.c_pointer = position2df_ctor3(args[0].c_pointer)
			elif hasattr(args[0], 'c_pointer'):
				self.c_pointer = position2df_ctor4(args[0].c_pointer)
			self.delete_c_pointer = True
		elif len(args) == 2:
			self.c_pointer = position2df_ctor1(*args)
			self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)

class position2di(vector2di):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = position2di_ctor2(0)
			self.delete_c_pointer = True
		elif len(args) == 1:
			if isinstance(args[0], int):
				self.c_pointer = position2di_ctor2(args[0])
			elif isinstance(args[0], vector2di):
				self.c_pointer = position2di_ctor3(args[0].c_pointer)
			elif hasattr(args[0], 'c_pointer'):
				self.c_pointer = position2di_ctor4(args[0].c_pointer)
			self.delete_c_pointer = True
		elif len(args) == 2:
			self.c_pointer = position2di_ctor1(args[0], args[1])
			self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
				self.c_pointer = kwargs.pop('c_pointer', None)
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)

class dimension2df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = dimension2df_ctor1()
		elif len(args) == 2:
			self.c_pointer = dimension2df_ctor2(*args)
		elif len(args) == 1:
			if isinstance(args[0], int):
				self.c_pointer = args[0]
				self.delete_c_pointer = False
			elif isinstance(args[0], vector2df):
				self.c_pointer = dimension2df_ctor4(args[0].c_pointer)
			else:
				if hasattr(args[0], 'c_pointer'):
					self.c_pointer = dimension2df_ctor3(args[0].c_pointer)
				else:
					self.c_pointer = dimension2df_ctor1()
		elif 'pointer' in kwargs:
			self.c_pointer = kwargs.pop('pointer')
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				dimension2df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def operator_set_other(self, other):
		return dimension2df(dimension2df_operator_set_other(self.c_pointer, other.c_pointer))
	def __eq__(self, other):
		if isinstance(other, vector2df):
			return dimension2df_operator_eq_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2df_operator_eq_other(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		if isinstance(other, vector2df):
			return dimension2df_operator_ne_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2df_operator_ne_other(self.c_pointer, other.c_pointer)
	def set(self, width, height):
		return dimension2df(dimension2df_set(self.c_pointer, width, height))
	def __idiv__(self, value):
		return dimension2df(dimension2df_operator_set_div_value(self.c_pointer, value))
	def __div__(self, value):
		return dimension2df(dimension2df_operator_div_value(self.c_pointer, value))
	def __imul__(self, value):
		return dimension2df(dimension2df_operator_set_mult_value(self.c_pointer, value))
	def __mul__(self, value):
		return dimension2df(dimension2df_operator_mult_value(self.c_pointer, value))
	def __iadd__(self, other):
		return dimension2df(dimension2df_operator_set_add_other(self.c_pointer, other.c_pointer))
	def __isub__(self, other):
		return dimension2df(dimension2df_operator_set_sub_other(self.c_pointer, other.c_pointer))
	def __add__(self, other):
		return dimension2df(dimension2df_operator_add_other(self.c_pointer, other.c_pointer))
	def getArea(self):
		return dimension2df_getArea(self.c_pointer)
	def getOptimalSize(self, requirePowerOfTwo = True, requireSquare = False, larger = True, maxValue = 0.0):
		return dimension2df(dimension2df_getOptimalSize(self.c_pointer, requirePowerOfTwo, requireSquare, larger, maxValue))
	def getInterpolated(self, other, d):
		return dimension2df(dimension2df_getInterpolated(self.c_pointer, other.c_pointer, d))
	def get_Width(self):
		return dimension2df_get_Width(self.c_pointer)
	def set_Width(self, value):
		dimension2df_set_Width(self.c_pointer, value)
	def get_Height(self):
		return dimension2df_get_Height(self.c_pointer)
	def set_Height(self, value):
		dimension2df_set_Height(self.c_pointer, value)
	X = Width = property(get_Width, set_Width)
	Y = Height = property(get_Height, set_Height)
	def __repr__(self):
		return '%s(%f, %f)' % (self.__class__.__name__, self.Width, self.Height)
	def __str__(self):
		return self.__repr__()

class dimension2du(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = dimension2du_ctor1()
		elif len(args) == 2:
			self.c_pointer = dimension2du_ctor2(*args)
		elif len(args) == 1:
			if isinstance(args[0], int):
				self.c_pointer = args[0]
				self.delete_c_pointer = False
			elif isinstance(args[0], vector2du):
				self.c_pointer = dimension2du_ctor4(args[0].c_pointer)
			else:
				if hasattr(args[0], 'c_pointer'):
					self.c_pointer = dimension2du_ctor3(args[0].c_pointer)
				else:
					self.c_pointer = dimension2du_ctor1()
		elif 'pointer' in kwargs:
			self.c_pointer = kwargs.pop('pointer', None)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				dimension2du_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def operator_set_other(self, other):
		return dimension2du(pointer = dimension2du_operator_set_other(self.c_pointer, other.c_pointer))
	def __eq__(self, other):
		if isinstance(other, vector2du):
			return dimension2du_operator_eq_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2du_operator_eq_other(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		if isinstance(other, vector2du):
			return dimension2du_operator_ne_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2du_operator_ne_other(self.c_pointer, other.c_pointer)
	def set(self, width, height):
		return dimension2du(pointer = dimension2du_set(self.c_pointer, width, height))
	def __idiv__(self, value):
		return dimension2du(pointer = dimension2du_operator_set_div_value(self.c_pointer, value))
	def __div__(self, value):
		return dimension2du(pointer = dimension2du_operator_div_value(self.c_pointer, value))
	def __imul__(self, value):
		return dimension2du(pointer = dimension2du_operator_set_mult_value(self.c_pointer, value))
	def __mul__(self, value):
		return dimension2du(pointer = dimension2du_operator_mult_value(self.c_pointer, value))
	def __iadd__(self, other):
		return dimension2du(pointer = dimension2du_operator_set_add_other(self.c_pointer, other.c_pointer))
	def __isub__(self, other):
		return dimension2du(pointer = dimension2du_operator_set_sub_other(self.c_pointer, other.c_pointer))
	def __add__(self, other):
		return dimension2du(pointer = dimension2du_operator_add_other(self.c_pointer, other.c_pointer))
	def getArea(self):
		return dimension2du_getArea(self.c_pointer)
	def getOptimalSize(self, requirePowerOfTwo = True, requireSquare = False, larger = True, maxValue = 0):
		return dimension2du(pointer = dimension2du_getOptimalSize(self.c_pointer, requirePowerOfTwo, requireSquare, larger, maxValue))
	def getInterpolated(self, other, d):
		return dimension2du(pointer = dimension2du_getInterpolated(self.c_pointer, other.c_pointer, d))
	def get_Width(self):
		return dimension2du_get_Width(self.c_pointer)
	def set_Width(self, value):
		dimension2du_set_Width(self.c_pointer, value)
	def get_Height(self):
		return dimension2du_get_Height(self.c_pointer)
	def set_Height(self, value):
		dimension2du_set_Height(self.c_pointer, value)
	X = Width = property(get_Width, set_Width)
	Y = Height = property(get_Height, set_Height)
	def __repr__(self):
		return '%s(%d, %d)' % (self.__class__.__name__, self.Width, self.Height)
	def __str__(self):
		return self.__repr__()

class dimension2di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = dimension2di_ctor1()
		elif len(args) == 2:
			self.c_pointer = dimension2di_ctor2(*args)
		elif len(args) == 1:
			if isinstance(args[0], int):
				self.c_pointer = args[0]
				self.delete_c_pointer = False
			elif isinstance(args[0], vector2di):
				self.c_pointer = dimension2di_ctor4(args[0].c_pointer)
			else:
				if hasattr(args[0], 'c_pointer'):
					self.c_pointer = dimension2di_ctor3(args[0].c_pointer)
				else:
					self.c_pointer = dimension2di_ctor1()
		elif 'pointer' in kwargs:
			self.c_pointer = kwargs.pop('pointer')
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				dimension2di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def operator_set_other(self, other):
		return dimension2di(dimension2di_operator_set_other(self.c_pointer, other.c_pointer))
	def __eq__(self, other):
		if isinstance(other, vector2di):
			return dimension2di_operator_eq_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2di_operator_eq_other(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		if isinstance(other, vector2di):
			return dimension2di_operator_ne_vector2d(self.c_pointer, other.c_pointer)
		else:
			return dimension2di_operator_ne_other(self.c_pointer, other.c_pointer)
	def set(self, width, height):
		return dimension2di(dimension2di_set(self.c_pointer, width, height))
	def __idiv__(self, value):
		return dimension2di(dimension2di_operator_set_div_value(self.c_pointer, value))
	def __div__(self, value):
		return dimension2di(dimension2di_operator_div_value(self.c_pointer, value))
	def __imul__(self, value):
		return dimension2di(dimension2di_operator_set_mult_value(self.c_pointer, value))
	def __mul__(self, value):
		return dimension2di(dimension2di_operator_mult_value(self.c_pointer, value))
	def __iadd__(self, other):
		return dimension2di(dimension2di_operator_set_add_other(self.c_pointer, other.c_pointer))
	def __isub__(self, other):
		return dimension2di(dimension2di_operator_set_sub_other(self.c_pointer, other.c_pointer))
	def __add__(self, other):
		return dimension2di(dimension2di_operator_add_other(self.c_pointer, other.c_pointer))
	def getArea(self):
		return dimension2di_getArea(self.c_pointer)
	def getOptimalSize(self, requirePowerOfTwo = True, requireSquare = False, larger = True, maxValue = 0):
		return dimension2di(dimension2di_getOptimalSize(self.c_pointer, requirePowerOfTwo, requireSquare, larger, maxValue))
	def getInterpolated(self, other, d):
		return dimension2di(dimension2di_getInterpolated(self.c_pointer, other.c_pointer, d))
	def get_Width(self):
		return dimension2di_get_Width(self.c_pointer)
	def set_Width(self, value):
		dimension2di_set_Width(self.c_pointer, value)
	def get_Height(self):
		return dimension2di_get_Height(self.c_pointer)
	def set_Height(self, value):
		dimension2di_set_Height(self.c_pointer, value)
	X = Width = property(get_Width, set_Width)
	Y = Height = property(get_Height, set_Height)
	def __repr__(self):
		return '%s(%d, %d)' % (self.__class__.__name__, self.Width, self.Height)
	def __str__(self):
		return self.__repr__()

class rectf(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 4 or 'x' in kwargs or 'y' in kwargs or 'x2' in kwargs or 'y2' in kwargs:
			self.ctor2(*args, **kwargs)
		elif len(args) == 2:
			if isinstance(args[1], dimension2df):
				self.ctor4(*args, **kwargs)
			else:
				self.ctor3(*args, **kwargs)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				rectf_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(%f, %f, %f, %f)' % (self.__class__.__name__, self.UpperLeftCorner.X, self.UpperLeftCorner.Y, self.LowerRightCorner.X, self.LowerRightCorner.Y)
	def __str__(self):
		return self.__repr__()
	def ctor1(self):
		self.c_pointer = rectf_ctor1()
	def ctor2(self, x = 0.0, y = 0.0, x2 = 0.0, y2 = 0.0):
		self.c_pointer = rectf_ctor2(x, y, x2, y2)
	def ctor3(self, upperLeft, lowerRight):
		self.c_pointer = rectf_ctor3(upperLeft.c_pointer, lowerRight.c_pointer)
	def ctor4(self, pos, size):
		self.c_pointer = rectf_ctor4(pos.c_pointer, size.c_pointer)
	def add(self, pos):
		return rectf_add(self.c_pointer, pos.c_pointer)
	def add_set(self, pos):
		return rectf_add_set(self.c_pointer, pos.c_pointer)
	def sub(self, pos):
		return rectf_sub(self.c_pointer, pos.c_pointer)
	def sub_set(self, pos):
		return rectf_sub_set(self.c_pointer, pos.c_pointer)
	def eq(self, other):
		return rectf_eq(self.c_pointer, other.c_pointer)
	def ne(self, other):
		return rectf_ne(self.c_pointer, other.c_pointer)
	def le(self, other):
		return rectf_le(self.c_pointer, other.c_pointer)
	def getArea(self):
		return rectf_getArea(self.c_pointer)
	def isPointInside(self, pos):
		return rectf_isPointInside(self.c_pointer, pos.c_pointer)
	def isRectCollided(self, other):
		return rectf_isRectCollided(self.c_pointer, other.c_pointer)
	def clipAgainst(self, other):
		rectf_clipAgainst(self.c_pointer, other.c_pointer)
	def constrainTo(self, other):
		return rectf_constrainTo(self.c_pointer, other.c_pointer)
	def getWidth(self):
		return rectf_getWidth(self.c_pointer)
	def getHeight(self):
		return rectf_getHeight(self.c_pointer)
	def repair(self):
		rectf_repair(self.c_pointer)
	def isValid(self):
		return rectf_isValid(self.c_pointer)
	def getCenter(self):
		return position2df(c_pointer = rectf_getCenter(self.c_pointer))
	def getSize(self):
		return dimension2df(rectf_getSize(self.c_pointer))
	def addInternalPoint1(self, p):
		rectf_addInternalPoint1(self.c_pointer, p.c_pointer)
	def addInternalPoint2(self, x, y):
		rectf_addInternalPoint2(self.c_pointer, x, y)
	def addInternalPoint(self, *args):
		if len(args) == 1:
			self.addInternalPoint1(*args)
		else:
			self.addInternalPoint2(*args)
	def get_UpperLeftCorner(self):
		return position2df(c_pointer = rectf_get_UpperLeftCorner(self.c_pointer))
	def set_UpperLeftCorner(self, value):
		rectf_set_UpperLeftCorner(self.c_pointer, value.c_pointer)
	def get_LowerRightCorner(self):
		return position2df(c_pointer = rectf_get_LowerRightCorner(self.c_pointer))
	def set_LowerRightCorner(self, value):
		rectf_set_LowerRightCorner(self.c_pointer, value.c_pointer)
	UpperLeftCorner = property(get_UpperLeftCorner, set_UpperLeftCorner)
	LowerRightCorner = property(get_LowerRightCorner, set_LowerRightCorner)

class recti(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = recti_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 4 or 'x' in kwargs or 'y' in kwargs or 'x2' in kwargs or 'y2' in kwargs:
			self.ctor2(*args, **kwargs)
		elif len(args) == 2:
			if isinstance(args[1], dimension2di):
				self.ctor4(*args, **kwargs)
			else:
				self.ctor3(*args, **kwargs)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				recti_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(%d, %d, %d, %d)' % (self.__class__.__name__, self.UpperLeftCorner.X, self.UpperLeftCorner.Y, self.LowerRightCorner.X, self.LowerRightCorner.Y)
	def __str__(self):
		return self.__repr__()
	def ctor1(self):
		self.c_pointer = recti_ctor1()
	def ctor2(self, x = 0, y = 0, x2 = 0, y2 = 0):
		self.c_pointer = recti_ctor2(x, y, x2, y2)
	def ctor3(self, upperLeft, lowerRight):
		self.c_pointer = recti_ctor3(upperLeft.c_pointer, lowerRight.c_pointer)
	def ctor4(self, pos, size):
		self.c_pointer = recti_ctor4(pos.c_pointer, size.c_pointer)
	def add(self, pos):
		return recti_add(self.c_pointer, pos.c_pointer)
	def add_set(self, pos):
		return recti_add_set(self.c_pointer, pos.c_pointer)
	def sub(self, pos):
		return recti_sub(self.c_pointer, pos.c_pointer)
	def sub_set(self, pos):
		return recti_sub_set(self.c_pointer, pos.c_pointer)
	def eq(self, other):
		return recti_eq(self.c_pointer, other.c_pointer)
	def ne(self, other):
		return recti_ne(self.c_pointer, other.c_pointer)
	def le(self, other):
		return recti_le(self.c_pointer, other.c_pointer)
	def getArea(self):
		return recti_getArea(self.c_pointer)
	def isPointInside(self, pos):
		return recti_isPointInside(self.c_pointer, pos.c_pointer)
	def isRectCollided(self, other):
		return recti_isRectCollided(self.c_pointer, other.c_pointer)
	def clipAgainst(self, other):
		recti_clipAgainst(self.c_pointer, other.c_pointer)
	def constrainTo(self, other):
		return recti_constrainTo(self.c_pointer, other.c_pointer)
	def getWidth(self):
		return recti_getWidth(self.c_pointer)
	def getHeight(self):
		return recti_getHeight(self.c_pointer)
	def repair(self):
		recti_repair(self.c_pointer)
	def isValid(self):
		return recti_isValid(self.c_pointer)
	def getCenter(self):
		return position2di(c_pointer = recti_getCenter(self.c_pointer))
	def getSize(self):
		return dimension2di(recti_getSize(self.c_pointer))
	def addInternalPoint1(self, p):
		recti_addInternalPoint1(self.c_pointer, p.c_pointer)
	def addInternalPoint2(self, x, y):
		recti_addInternalPoint2(self.c_pointer, x, y)
	def addInternalPoint(self, *args):
		if len(args) == 1:
			self.addInternalPoint1(*args)
		else:
			self.addInternalPoint2(*args)
	def get_UpperLeftCorner(self):
		return position2di(c_pointer = recti_get_UpperLeftCorner(self.c_pointer))
	def set_UpperLeftCorner(self, value):
		recti_set_UpperLeftCorner(self.c_pointer, value.c_pointer)
	def get_LowerRightCorner(self):
		return position2di(c_pointer = recti_get_LowerRightCorner(self.c_pointer))
	def set_LowerRightCorner(self, value):
		recti_set_LowerRightCorner(self.c_pointer, value.c_pointer)
	UpperLeftCorner = property(get_UpperLeftCorner, set_UpperLeftCorner)
	LowerRightCorner = property(get_LowerRightCorner, set_LowerRightCorner)

class rects32array:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = rects32array_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				rects32array_delete(self.c_pointer)
			except:
				pass
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return self.get_item(key)
	def reallocate(self, new_size):
		rects32array_reallocate(self.c_pointer, new_size)
	def setAllocStrategy(self, newStrategy = ALLOC_STRATEGY_DOUBLE):
		rects32array_setAllocStrategy(self.c_pointer, newStrategy)
	def push_back(self, element):
		rects32array_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		rects32array_push_front(self.c_pointer, element.c_pointer)
	def insert(self, element, index = 0):
		rects32array_insert(self.c_pointer, element.c_pointer, index)
	def clear(self):
		rects32array_clear(self.c_pointer)
	def set_pointer(self, newPointer, size, _is_sorted = False, _free_when_destroyed = True):
		rects32array_set_pointer(self.c_pointer, newPointer.c_pointer, size, _is_sorted, _free_when_destroyed)
	def set_free_when_destroyed(self, f):
		rects32array_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		rects32array_set_used(self.c_pointer, usedNow)
	def get_item(self, index):
		return recti(rects32array_get_item(self.c_pointer, index))
	def size(self):
		return rects32array_size(self.c_pointer)
	def empty(self):
		return rects32array_empty(self.c_pointer)
	def sort(self):
		rects32array_sort(self.c_pointer)
	def binary_search1(self, element):
		return rects32array_binary_search1(self.c_pointer, element.c_pointer)
	def binary_search2(self, element, left, right):
		return rects32array_binary_search2(self.c_pointer, element.c_pointer, left, right)
	def binary_search(self, *args):
		if len(args) == 1:
			return self.binary_search1(*args)
		else:
			return self.binary_search2(*args)
	def binary_search_multi(self, element, last):
		return rects32array_binary_search_multi(self.c_pointer, element.c_pointer, last)
	def linear_search(self, element):
		return rects32array_linear_search(self.c_pointer, element.c_pointer)
	def linear_reverse_search(self, element):
		return rects32array_linear_reverse_search(self.c_pointer, element.c_pointer)
	def erase1(self, index):
		rects32array_erase1(self.c_pointer, index)
	def erase2(self, index, count):
		rects32array_erase2(self.c_pointer, index, count)
	def erase(self, *args):
		if len(args) == 1:
			self.erase1(*args)
		else:
			self.erase2(*args)
	def set_sorted(self, is_sorted):
		rects32array_set_sorted(self.c_pointer, is_sorted)
	def swap(self, other):
		rects32array_swap(self.c_pointer, other.c_pointer)

class vector3df:
	def __init__(self, *args, **kwargs):
		pass
class vector3di:
	def __init__(self, *args, **kwargs):
		pass

class vector3df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = vector3df_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 2:
			self.c_pointer, self.delete_c_pointer = args
		elif len(args) == 3:
			self.c_pointer = vector3df_ctor2(*args)
		elif 'n' in kwargs:
			self.c_pointer = vector3df_ctor3(kwargs.pop('n', 0.0))
		elif 'other' in kwargs:
			self.c_pointer = vector3df_ctor4(kwargs.pop('other'))
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				vector3df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def set_X(self, value):
		vector3df_set_X(self.c_pointer, value)
	def get_X(self):
		return vector3df_get_X(self.c_pointer)
	def set_Y(self, value):
		vector3df_set_Y(self.c_pointer, value)
	def get_Y(self):
		return vector3df_get_Y(self.c_pointer)
	def set_Z(self, value):
		vector3df_set_Z(self.c_pointer, value)
	def get_Z(self):
		return vector3df_get_Z(self.c_pointer)
	X = property(get_X, set_X)
	Y = property(get_Y, set_Y)
	Z = property(get_Z, set_Z)
	def __repr__(self):
		return '%s(%f, %f, %f)' % (self.__class__.__name__, self.X, self.Y, self.Z)
	def __str__(self):
		return self.__repr__()
	def __neg__(self):
		return vector3df(vector3df_operator_sub(self.c_pointer), True)
	def operator_set(self, other):
		return vector3df(vector3df_operator_set(self.c_pointer, other.c_pointer))
	def __add__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_add_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_add_value(self.c_pointer, other), True)
	def __iadd__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_set_add_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_set_add_value(self.c_pointer, other), True)
	def __sub__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_sub_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_sub_value(self.c_pointer, other), True)
	def __isub__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_set_sub_other(self.c_pointer, other.c_pointer))
		else:
			return vector3df(vector3df_operator_set_sub_value(self.c_pointer, other))
	def __mul__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_mult_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_mult_value(self.c_pointer, other), True)
	def __imul__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_set_mult_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_set_mult_value(self.c_pointer, other), True)
	def __div__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_div_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_div_value(self.c_pointer, other), True)
	def __idiv__(self, other):
		if isinstance(other, vector3df):
			return vector3df(vector3df_operator_set_div_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3df(vector3df_operator_set_div_value(self.c_pointer, other), True)
	def __le__(self, other):
		return vector3df_operator_le(self.c_pointer, other.c_pointer)
	def __ge__(self, other):
		return vector3df_operator_ge(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return vector3df_operator_lt(self.c_pointer, other.c_pointer)
	def __gt__(self, other):
		return vector3df_operator_gt(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return vector3df_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return vector3df_operator_ne(self.c_pointer, other.c_pointer)
	def equals(self, other, tolerance = ROUNDING_ERROR_f32):
		return vector3df_equals(self.c_pointer, other.c_pointer, tolerance)
	def set(self, *args):
		if len(args) == 3:
			return self.set1(*args)
		else:
			return self.set2(*args)
	def set1(self, nx, ny, nz):
		return vector3df(vector3df_set1(self.c_pointer, nx, ny, nz), True)
	def set2(self, p):
		return vector3df(vector3df_set2(self.c_pointer, p.c_pointer), True)
	def getLength(self):
		return vector3df_getLength(self.c_pointer)
	def getLengthSQ(self):
		return vector3df_getLengthSQ(self.c_pointer)
	def dotProduct(self, other):
		return vector3df_dotProduct(self.c_pointer, other.c_pointer)
	def getDistanceFrom(self, other):
		return vector3df_getDistanceFrom(self.c_pointer, other.c_pointer)
	def getDistanceFromSQ(self, other):
		return vector3df_getDistanceFromSQ(self.c_pointer, other.c_pointer)
	def crossProduct(self, p):
		return vector3df(vector3df_crossProduct(self.c_pointer, p.c_pointer), True)
	def isBetweenPoints(self, begin, end):
		return vector3df_isBetweenPoints(self.c_pointer, begin.c_pointer, end.c_pointer)
	def normalize(self):
		return vector3df(vector3df_normalize(self.c_pointer), True)
	def setLength(self, newlength):
		return vector3df(vector3df_setLength(self.c_pointer, newlength), True)
	def invert(self):
		return vector3df(vector3df_invert(self.c_pointer), True)
	def rotateXZBy(self, degrees, center = vector3df()):
		vector3df_rotateXZBy(self.c_pointer, degrees, center.c_pointer)
	def rotateXYBy(self, degrees, center = vector3df()):
		vector3df_rotateXYBy(self.c_pointer, degrees, center.c_pointer)
	def rotateYZBy(self, degrees, center = vector3df()):
		vector3df_rotateYZBy(self.c_pointer, degrees, center.c_pointer)
	def getInterpolated(self, other, d):
		return vector3df(vector3df_getInterpolated(self.c_pointer, other.c_pointer, d), True)
	def getInterpolated_quadratic(self, v2, v3, d):
		return vector3df(vector3df_getInterpolated_quadratic(self.c_pointer, v2.c_pointer, v3.c_pointer, d), True)
	def interpolate(self, a, b, d):
		return vector3df(vector3df_interpolate(self.c_pointer, a.c_pointer, b.c_pointer, d), True)
	def getHorizontalAngle(self):
		return vector3df(vector3df_getHorizontalAngle(self.c_pointer), True)
	def getSphericalCoordinateAngles(self):
		return vector3df(vector3df_getSphericalCoordinateAngles(self.c_pointer), True)
	def rotationToDirection(self, forwards = vector3df(0, 0, 1)):
		return vector3df(vector3df_rotationToDirection(self.c_pointer, forwards.c_pointer), True)
	def getAs4Values(self, pointer_array):
		vector3df_getAs4Values(self.c_pointer, pointer_array)

class vector3di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = vector3di_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 2:
			self.c_pointer, self.delete_c_pointer = args
		elif len(args) == 3:
			self.c_pointer = vector3di_ctor2(*args)
		elif 'n' in kwargs:
			self.c_pointer = vector3di_ctor3(kwargs.pop('n', 0))
		elif 'other' in kwargs:
			self.c_pointer = vector3di_ctor4(kwargs.pop('other'))
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				vector3di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def set_X(self, value):
		vector3di_set_X(self.c_pointer, value)
	def get_X(self):
		return vector3di_get_X(self.c_pointer)
	def set_Y(self, value):
		vector3di_set_Y(self.c_pointer, value)
	def get_Y(self):
		return vector3di_get_Y(self.c_pointer)
	def set_Z(self, value):
		vector3di_set_Z(self.c_pointer, value)
	def get_Z(self):
		return vector3di_get_Z(self.c_pointer)
	X = property(get_X, set_X)
	Y = property(get_Y, set_Y)
	Z = property(get_Z, set_Z)
	def __repr__(self):
		return '%s(%d, %d, %d)' % (self.__class__.__name__, self.X, self.Y, self.Z)
	def __str__(self):
		return self.__repr__()
	def __neg__(self):
		return vector3di(vector3di_operator_sub(self.c_pointer), True)
	def operator_set(self, other):
		return vector3di(vector3di_operator_set(self.c_pointer, other.c_pointer), True)
	def __add__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_add_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_add_value(self.c_pointer, other), True)
	def __iadd__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_set_add_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_set_add_value(self.c_pointer, other), True)
	def __sub__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_sub_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_sub_value(self.c_pointer, other), True)
	def __isub__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_set_sub_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_set_sub_value(self.c_pointer, other), True)
	def __mul__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_mult_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_mult_value(self.c_pointer, other), True)
	def __imul__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_set_mult_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_set_mult_value(self.c_pointer, other), True)
	def __idiv__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_div_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_div_value(self.c_pointer, other), True)
	def __idiv__(self, other):
		if isinstance(other, vector3di):
			return vector3di(vector3di_operator_set_div_other(self.c_pointer, other.c_pointer), True)
		else:
			return vector3di(vector3di_operator_set_div_value(self.c_pointer, other), True)
	def __le__(self, other):
		return vector3di_operator_le(self.c_pointer, other.c_pointer)
	def __ge__(self, other):
		return vector3di_operator_ge(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return vector3di_operator_lt(self.c_pointer, other.c_pointer)
	def __gt__(self, other):
		return vector3di_operator_gt(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return vector3di_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return vector3di_operator_ne(self.c_pointer, other.c_pointer)
	def equals(self, other, tolerance = ROUNDING_ERROR_S32):
		return vector3di_equals(self.c_pointer, other.c_pointer, tolerance)
	def set(self, *args):
		if len(args) == 3:
			return self.set1(*args)
		else:
			return self.set2(*args)
	def set1(self, nx, ny, nz):
		return vector3di(vector3di_set1(self.c_pointer, nx, ny, nz), True)
	def set2(self, p):
		return vector3di(vector3di_set2(self.c_pointer, p.c_pointer), True)
	def getLength(self):
		return vector3di_getLength(self.c_pointer)
	def getLengthSQ(self):
		return vector3di_getLengthSQ(self.c_pointer)
	def dotProduct(self, other):
		return vector3di_dotProduct(self.c_pointer, other.c_pointer)
	def getDistanceFrom(self, other):
		return vector3di_getDistanceFrom(self.c_pointer, other.c_pointer)
	def getDistanceFromSQ(self, other):
		return vector3di_getDistanceFromSQ(self.c_pointer, other.c_pointer)
	def crossProduct(self, p):
		return vector3di(vector3di_crossProduct(self.c_pointer, p.c_pointer), True)
	def isBetweenPoints(self, begin, end):
		return vector3di_isBetweenPoints(self.c_pointer, begin.c_pointer, end.c_pointer)
	def normalize(self):
		return vector3di(vector3di_normalize(self.c_pointer), True)
	def setLength(self, newlength):
		return vector3di(vector3di_setLength(self.c_pointer, newlength), True)
	def invert(self):
		return vector3di(vector3di_invert(self.c_pointer), True)
	def rotateXZBy(self, degrees, center = vector3di()):
		vector3di_rotateXZBy(self.c_pointer, degrees, center.c_pointer)
	def rotateXYBy(self, degrees, center = vector3di()):
		vector3di_rotateXYBy(self.c_pointer, degrees, center.c_pointer)
	def rotateYZBy(self, degrees, center = vector3di()):
		vector3di_rotateYZBy(self.c_pointer, degrees, center.c_pointer)
	def getInterpolated(self, other, d):
		return vector3di(vector3di_getInterpolated(self.c_pointer, other.c_pointer, d), True)
	def getInterpolated_quadratic(self, v2, v3, d):
		return vector3di(vector3di_getInterpolated_quadratic(self.c_pointer, v2.c_pointer, v3.c_pointer, d), True)
	def interpolate(self, a, b, d):
		return vector3di(vector3di_interpolate(self.c_pointer, a.c_pointer, b.c_pointer, d), True)
	def getHorizontalAngle(self):
		return vector3di(vector3di_getHorizontalAngle(self.c_pointer), True)
	def getSphericalCoordinateAngles(self):
		return vector3di(vector3di_getSphericalCoordinateAngles(self.c_pointer), True)
	def rotationToDirection(self, forwards = vector3di(0, 0, 1)):
		return vector3di(vector3di_rotationToDirection(self.c_pointer, forwards.c_pointer), True)
	def getAs4Values(self, pointer_array):
		vector3di_getAs4Values(self.c_pointer, pointer_array)

class aabbox3df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = aabbox3df_ctor1()
		elif len(args) == 2:
			if isinstance(args[0], vector3df) and isinstance(args[1], vector3df):
				self.c_pointer = aabbox3df_ctor2(args[0].c_pointer, args[1].c_pointer)
			else:
				self.c_pointer = aabbox3df_ctor2(*args, **kwargs)
		elif len(args) == 1:
			if isinstance(args[0], vector3df):
				self.c_pointer = aabbox3df_ctor3(args[0].c_pointer)
			else:
				self.c_pointer = args[0]
				self.delete_c_pointer = False
		elif len(args) == 6:
			self.c_pointer = aabbox3df_ctor4(*args, **kwargs)
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', 0)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				aabbox3df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __eq__(self, other):
		return aabbox3df_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return aabbox3df_operator_ne(self.c_pointer, other.c_pointer)
	def reset(self, *args):
		if len(args) == 3:
			aabbox3df_reset1(self.c_pointer, *args)
		else:
			if isinstance(args[0], aabbox3df):
				aabbox3df_reset2(self.c_pointer, args[0].c_pointer)
			else:
				aabbox3df_reset3(self.c_pointer, args[0].c_pointer)
	def reset1(self, x, y, z):
		aabbox3df_reset1(self.c_pointer, x, y, z)
	def reset2(self, initValue):
		aabbox3df_reset2(self.c_pointer, initValue.c_pointer)
	def reset3(self, initValue):
		aabbox3df_reset3(self.c_pointer, initValue.c_pointer)
	def addInternalBox(self, b):
		aabbox3df_addInternalBox(self.c_pointer, b.c_pointer)
	def addInternalPoint(self, *args):
		if len(args) == 3:
			aabbox3df_addInternalPoint2(self.c_pointer, *args)
		else:
			aabbox3df_addInternalPoint1(self.c_pointer, args[0].c_pointer)
	def addInternalPoint1(self, p):
		aabbox3df_addInternalPoint1(self.c_pointer, p.c_pointer)
	def addInternalPoint2(self, x, y, z):
		aabbox3df_addInternalPoint2(self.c_pointer, x, y, z)
	def getCenter(self):
		return vector3df(aabbox3df_getCenter(self.c_pointer))
	def getExtent(self):
		return vector3df(aabbox3df_getExtent(self.c_pointer))
	def isEmpty(self):
		return aabbox3df_isEmpty(self.c_pointer)
	def getVolume(self):
		return aabbox3df_getVolume(self.c_pointer)
	def getArea(self):
		return aabbox3df_getArea(self.c_pointer)
	def getEdges(self, edges):
		aabbox3df_getEdges(self.c_pointer, edges.c_pointer)
	def repair(self):
		aabbox3df_repair(self.c_pointer)
	def getInterpolated(self, other, d):
		return aabbox3df(aabbox3df_getInterpolated(self.c_pointer, other.c_pointer, d))
	def isPointInside(self, p):
		return aabbox3df_isPointInside(self.c_pointer, p.c_pointer)
	def isPointTotalInside(self, p):
		return aabbox3df_isPointTotalInside(self.c_pointer, p.c_pointer)
	def isFullInside(self, other):
		return aabbox3df_isFullInside(self.c_pointer, other.c_pointer)
	def intersectsWithBox(self, other):
		return aabbox3df_intersectsWithBox(self.c_pointer, other.c_pointer)
	def intersectsWithLine(self, *args):
		if len(args) == 1:
			return aabbox3df_intersectsWithLine1(self.c_pointer, args[0].c_pointer)
		else:
			return aabbox3df_intersectsWithLine2(self.c_pointer, args[0].c_pointer, args[1].c_pointer, args[2])
	def intersectsWithLine1(self, line):
		return aabbox3df_intersectsWithLine1(self.c_pointer, line.c_pointer)
	def intersectsWithLine2(self, linemiddle, linevect, halflength):
		return aabbox3df_intersectsWithLine2(self.c_pointer, linemiddle.c_pointer, linevect.c_pointer, halflength)
	def classifyPlaneRelation(self, plane):
		return aabbox3df_classifyPlaneRelation(self.c_pointer, plane.c_pointer)
	def get_MinEdge(self):
		return vector3df(aabbox3df_get_MinEdge(self.c_pointer))
	def set_MinEdge(self, value):
		aabbox3df_set_MinEdge(self.c_pointer, value.c_pointer)
	def get_MaxEdge(self):
		return vector3df(aabbox3df_get_MaxEdge(self.c_pointer))
	def set_MaxEdge(self, value):
		aabbox3df_set_MaxEdge(self.c_pointer, value.c_pointer)
	MinEdge = property(get_MinEdge, set_MinEdge)
	MaxEdge = property(get_MaxEdge, set_MaxEdge)
	def __repr__(self):
		min_edge = self.MinEdge
		max_edge = self.MaxEdge
		return '%s(%s(%f, %f, %f), %s(%f, %f, %f))' % (self.__class__.__name__, min_edge.__class__.__name__, min_edge.X, min_edge.Y, min_edge.Z, max_edge.__class__.__name__, max_edge.X, max_edge.Y, max_edge.Z)
	def __str__(self):
		return self.__repr__()

class aabbox3di:
	def __init__(self, *args, **kwargs):
		pass
class aabbox3di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = aabbox3di_ctor1()
		elif len(args) == 2:
			if isinstance(args[0], vector3di) and isinstance(args[1], vector3di):
				self.c_pointer = aabbox3di_ctor2(args[0].c_pointer, args[1].c_pointer)
			else:
				self.c_pointer = aabbox3di_ctor2(*args, **kwargs)
		elif len(args) == 1:
			if isinstance(args[0], vector3di):
				self.c_pointer = aabbox3di_ctor3(args[0].c_pointer)
			else:
				self.c_pointer = args[0]
				self.delete_c_pointer = False
		elif len(args) == 6:
			self.c_pointer = aabbox3di_ctor4(*args, **kwargs)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				aabbox3di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __eq__(self, other):
		return aabbox3di_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return aabbox3di_operator_ne(self.c_pointer, other.c_pointer)
	def reset(self, *args):
		if len(args) == 3:
			aabbox3di_reset1(self.c_pointer, *args)
		else:
			if isinstance(args[0], aabbox3di):
				aabbox3di_reset2(self.c_pointer, args[0].c_pointer)
			else:
				aabbox3di_reset3(self.c_pointer, args[0].c_pointer)
	def reset1(self, x, y, z):
		aabbox3di_reset1(self.c_pointer, x, y, z)
	def reset2(self, initValue):
		aabbox3di_reset2(self.c_pointer, initValue.c_pointer)
	def reset3(self, initValue):
		aabbox3di_reset3(self.c_pointer, initValue.c_pointer)
	def addInternalBox(self, b):
		aabbox3di_addInternalBox(self.c_pointer, b.c_pointer)
	def addInternalPoint(self, *args):
		if len(args) == 3:
			aabbox3di_addInternalPoint2(self.c_pointer, *args)
		else:
			aabbox3di_addInternalPoint1(self.c_pointer, args[0].c_pointer)
	def addInternalPoint1(self, p):
		aabbox3di_addInternalPoint1(self.c_pointer, p.c_pointer)
	def addInternalPoint2(self, x, y, z):
		aabbox3di_addInternalPoint2(self.c_pointer, x, y, z)
	def getCenter(self):
		return vector3di(aabbox3di_getCenter(self.c_pointer))
	def getExtent(self):
		return vector3di(aabbox3di_getExtent(self.c_pointer))
	def isEmpty(self):
		return aabbox3di_isEmpty(self.c_pointer)
	def getVolume(self):
		return aabbox3di_getVolume(self.c_pointer)
	def getArea(self):
		return aabbox3di_getArea(self.c_pointer)
	def getEdges(self, edges):
		aabbox3di_getEdges(self.c_pointer, edges.c_pointer)
	def repair(self):
		aabbox3di_repair(self.c_pointer)
	def getInterpolated(self, other, d):
		return aabbox3di(aabbox3di_getInterpolated(self.c_pointer, other.c_pointer, d))
	def isPointInside(self, p):
		return aabbox3di_isPointInside(self.c_pointer, p.c_pointer)
	def isPointTotalInside(self, p):
		return aabbox3di_isPointTotalInside(self.c_pointer, p.c_pointer)
	def isFullInside(self, other):
		return aabbox3di_isFullInside(self.c_pointer, other.c_pointer)
	def intersectsWithBox(self, other):
		return aabbox3di_intersectsWithBox(self.c_pointer, other.c_pointer)
	#~ def intersectsWithLine(self, *args):
		#~ if len(args) == 1:
			#~ return aabbox3di_intersectsWithLine1(self.c_pointer, args[0].c_pointer)
		#~ else:
			#~ return aabbox3di_intersectsWithLine2(self.c_pointer, args[0].c_pointer, args[1].c_pointer, args[2])
	#~ def intersectsWithLine1(self, line):
		#~ return aabbox3di_intersectsWithLine1(self.c_pointer, line.c_pointer)
	#~ def intersectsWithLine2(self, linemiddle, linevect, halflength):
		#~ return aabbox3di_intersectsWithLine2(self.c_pointer, linemiddle.c_pointer, linevect.c_pointer, halflength)
	def classifyPlaneRelation(self, plane):
		return aabbox3di_classifyPlaneRelation(self.c_pointer, plane.c_pointer)
	def get_MinEdge(self):
		return vector3di(aabbox3di_get_MinEdge(self.c_pointer))
	def set_MinEdge(self, value):
		aabbox3di_set_MinEdge(self.c_pointer, value.c_pointer)
	def get_MaxEdge(self):
		return vector3di(aabbox3di_get_MaxEdge(self.c_pointer))
	def set_MaxEdge(self, value):
		aabbox3di_set_MaxEdge(self.c_pointer, value.c_pointer)
	MinEdge = property(get_MinEdge, set_MinEdge)
	MaxEdge = property(get_MaxEdge, set_MaxEdge)
	def __repr__(self):
		min_edge = self.MinEdge
		max_edge = self.MaxEdge
		return '%s(%s(%f, %f, %f), %s(%f, %f, %f))' % (self.__class__.__name__, min_edge.__class__.__name__, min_edge.X, min_edge.Y, min_edge.Z, max_edge.__class__.__name__, max_edge.X, max_edge.Y, max_edge.Z)
	def __str__(self):
		return self.__repr__()

class plane3df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = plane3df_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 2:
			if isinstance(args[0], vector3df) and isinstance(args[1], vector3df):
				self.c_pointer = plane3df_ctor2(args[0].c_pointer, args[1].c_pointer)
			elif isinstance(args[0], vector3df) and isinstance(args[1], float):
				self.c_pointer = plane3df_ctor5(args[0].c_pointer, args[1])
		elif len(args) == 3:
			self.c_pointer = plane3df_ctor4(args[0].c_pointer, args[1].c_pointer, args[2].c_pointer)
		elif len(args) == 6:
			self.c_pointer = plane3df_ctor4(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				plane3df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	#~ def destructor(self):
		#~ plane3df_destructor(self.c_pointer)
	def __eq__(self, other):
		return plane3df_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return plane3df_operator_ne(self.c_pointer, other.c_pointer)
	def setPlane(self, point, nvector):
		plane3df_setPlane(self.c_pointer, point.c_pointer, nvector.c_pointer)
	def setPlane2(self, nvect, d):
		plane3df_setPlane2(self.c_pointer, nvect.c_pointer, d)
	def setPlane3(self, point1, point2, point3):
		plane3df_setPlane3(self.c_pointer, point1.c_pointer, point2.c_pointer, point3.c_pointer)
	def getIntersectionWithLine(self, linePoint, lineVect, outIntersection):
		#~ return plane3df_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, ctypes.byref(ctypes.c_long(outIntersection.c_pointer)))
		#~ return plane3df_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, ctypes.addressof(ctypes.c_long(outIntersection.c_pointer)))
		return plane3df_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getKnownIntersectionWithLine(self, linePoint1, linePoint2):
		return plane3df_getKnownIntersectionWithLine(self.c_pointer, linePoint1, linePoint2)
	def getIntersectionWithLimitedLine(self, linePoint1, linePoint2, outIntersection):
		return plane3df_getIntersectionWithLimitedLine(self.c_pointer, linePoint1.c_pointer, linePoint2.c_pointer, outIntersection.c_pointer)
	def classifyPointRelation(self, point):
		return plane3df_classifyPointRelation(self.c_pointer, point.c_pointer)
	def recalculateD(self, MPoint):
		plane3df_recalculateD(self.c_pointer, MPoint.c_pointer)
	def getMemberPoint(self):
		return plane3df_getMemberPoint(self.c_pointer)
	def existsIntersection(self, other):
		return plane3df_existsIntersection(self.c_pointer, other.c_pointer)
	def getIntersectionWithPlane(self, other, outLinePoint, outLineVect):
		return plane3df_getIntersectionWithPlane(self.c_pointer, other.c_pointer, outLinePoint.c_pointer, outLineVect.c_pointer)
	def getIntersectionWithPlanes(self, o1, o2, outPoint):
		return plane3df_getIntersectionWithPlanes(self.c_pointer, o1.c_pointer, o2.c_pointer, outPoint.c_pointer)
	def isFrontFacing(self, lookDirection):
		return plane3df_isFrontFacing(self.c_pointer, lookDirection)
	def getDistanceTo(self, point):
		return plane3df_getDistanceTo(self.c_pointer, point.c_pointer)
	def get_Normal(self):
		return plane3df_get_Normal(self.c_pointer)
	def set_Normal(self, value):
		plane3df_set_Normal(self.c_pointer, value.c_pointer)
	def get_D(self):
		return plane3df_get_D(self.c_pointer)
	def set_D(self, value):
		plane3df_set_D(self.c_pointer, value)
	Normal = property(get_Normal, set_Normal)
	D = property(get_D, set_D)
	def __repr__(self):
		return '%s(%s, %f)' % (self.__class__.__name__, str(self.X), self.D)
	def __str__(self):
		return self.__repr__()

class plane3di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = plane3di_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 2:
			if isinstance(args[0], vector3di) and isinstance(args[1], vector3di):
				self.c_pointer = plane3di_ctor2(args[0].c_pointer, args[1].c_pointer)
			elif isinstance(args[0], vector3di) and isinstance(args[1], int):
				self.c_pointer = plane3di_ctor5(args[0].c_pointer, args[1])
		elif len(args) == 3:
			self.c_pointer = plane3di_ctor4(args[0].c_pointer, args[1].c_pointer, args[2].c_pointer)
		elif len(args) == 6:
			self.c_pointer = plane3di_ctor4(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				plane3di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	#~ def destructor(self):
		#~ plane3di_destructor(self.c_pointer)
	def __eq__(self, other):
		return plane3di_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return plane3di_operator_ne(self.c_pointer, other.c_pointer)
	def setPlane(self, point, nvector):
		plane3di_setPlane(self.c_pointer, point.c_pointer, nvector.c_pointer)
	def setPlane2(self, nvect, d):
		plane3di_setPlane2(self.c_pointer, nvect.c_pointer, d)
	def setPlane3(self, point1, point2, point3):
		plane3di_setPlane3(self.c_pointer, point1.c_pointer, point2.c_pointer, point3.c_pointer)
	def getIntersectionWithLine(self, linePoint, lineVect, outIntersection):
		return plane3di_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getKnownIntersectionWithLine(self, linePoint1, linePoint2):
		return plane3di_getKnownIntersectionWithLine(self.c_pointer, linePoint1.c_pointer, linePoint2.c_pointer)
	def getIntersectionWithLimitedLine(self, linePoint1, linePoint2, outIntersection):
		return plane3di_getIntersectionWithLimitedLine(self.c_pointer, linePoint1.c_pointer, linePoint2.c_pointer, outIntersection.c_pointer)
	def classifyPointRelation(self, point):
		return plane3di_classifyPointRelation(self.c_pointer, point.c_pointer)
	def recalculateD(self, MPoint):
		plane3di_recalculateD(self.c_pointer, MPoint.c_pointer)
	def getMemberPoint(self):
		return plane3di_getMemberPoint(self.c_pointer)
	def existsIntersection(self, other):
		return plane3di_existsIntersection(self.c_pointer, other.c_pointer)
	def getIntersectionWithPlane(self, other, outLinePoint, outLineVect):
		return plane3di_getIntersectionWithPlane(self.c_pointer, other.c_pointer, outLinePoint.c_pointer, outLineVect.c_pointer)
	def getIntersectionWithPlanes(self, o1, o2, outPoint):
		return plane3di_getIntersectionWithPlanes(self.c_pointer, o1.c_pointer, o2.c_pointer, outPoint.c_pointer)
	def isFrontFacing(self, lookDirection):
		return plane3di_isFrontFacing(self.c_pointer, lookDirection)
	def getDistanceTo(self, point):
		return plane3di_getDistanceTo(self.c_pointer, point.c_pointer)
	def get_Normal(self):
		return plane3di_get_Normal(self.c_pointer)
	def set_Normal(self, value):
		plane3di_set_Normal(self.c_pointer, value.c_pointer)
	def get_D(self):
		return plane3di_get_D(self.c_pointer)
	def set_D(self, value):
		plane3di_set_D(self.c_pointer, value)
	Normal = property(get_Normal, set_Normal)
	D = property(get_D, set_D)
	def __repr__(self):
		return '%s(%s, %d)' % (self.__class__.__name__, str(self.X), self.D)
	def __str__(self):
		return self.__repr__()

class line3df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = line3df_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 6:
			self.c_pointer = line3df_ctor2(*args)
		elif len(args) == 2:
			self.c_pointer = line3df_ctor3(args[0].c_pointer, args[1].c_pointer)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				line3df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def get_start(self):
		return vector3df(line3df_get_start(self.c_pointer))
	def get_end(self):
		return vector3df(line3df_get_end(self.c_pointer))
	def set_start(self, value):
		line3df_set_start(self.c_pointer, value.c_pointer)
	def set_end(self, value):
		line3df_set_end(self.c_pointer, value.c_pointer)
	start = property(get_start, set_start) 
	end = property(get_end, set_end) 
	def __repr__(self):
		return '%s(%s, %s)' % (self.__class__.__name__, str(self.start), str(self.end))
	def __str__(self):
		return self.__repr__()
	def __add__(self, point):
		return line3df(line3df_add(self.c_pointer, point.c_pointer))
	def __iadd__(self, point):
		return line3df(line3df_add_set(self.c_pointer, point.c_pointer))
	def __sub__(self, point):
		return line3df(line3df_sub(self.c_pointer, point.c_pointer))
	def __isub__(self, point):
		return line3df(line3df_sub_set(self.c_pointer, point.c_pointer))
	def __eq__(self, other):
		return line3df_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return line3df_neq(self.c_pointer, other.c_pointer)
	def setLine1(self, xa, ya, za, xb, yb, zb):
		line3df_setLine1(self.c_pointer, xa, ya, za, xb, yb, zb)
	def setLine2(self, nstart, nend):
		line3df_setLine2(self.c_pointer, nstart.c_pointer, nend.c_pointer)
	def setLine3(self, line):
		line3df_setLine3(self.c_pointer, line.c_pointer)
	def getLength(self):
		return line3df_getLength(self.c_pointer)
	def getLengthSQ(self):
		return line3df_getLengthSQ(self.c_pointer)
	def getMiddle(self):
		return line3df_getMiddle(self.c_pointer)
	def getVector(self):
		return vector3df(line3df_getVector(self.c_pointer))
	def isPointBetweenStartAndEnd(self, point):
		return line3df_isPointBetweenStartAndEnd(self.c_pointer, point.c_pointer)
	def getClosestPoint(self, point):
		return line3df_getClosestPoint(self.c_pointer, point.c_pointer)
	def getIntersectionWithSphere(self, sorigin, sradius, outdistance):
		return line3df_getIntersectionWithSphere(self.c_pointer, sorigin.c_pointer, sradius, ctypes.byref(outdistance))

class line3di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = line3di_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 6:
			self.c_pointer = line3di_ctor2(*args)
		elif len(args) == 2:
			self.c_pointer = line3di_ctor3(args[0].c_pointer, args[1].c_pointer)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				line3di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def get_start(self):
		return vector3di(line3di_get_start(self.c_pointer))
	def get_end(self):
		return vector3di(line3di_get_end(self.c_pointer))
	def set_start(self, value):
		line3di_set_start(self.c_pointer, value.c_pointer)
	def set_end(self, value):
		line3di_set_end(self.c_pointer, value.c_pointer)
	start = property(get_start, set_start) 
	end = property(get_end, set_end) 
	def __repr__(self):
		return '%s(%s, %s)' % (self.__class__.__name__, str(self.start), str(self.end))
	def __str__(self):
		return self.__repr__()
	def __add__(self, point):
		return line3di(line3di_add(self.c_pointer, point.c_pointer))
	def __iadd__(self, point):
		return line3di(line3di_add_set(self.c_pointer, point.c_pointer))
	def __sub__(self, point):
		return line3di(line3di_sub(self.c_pointer, point.c_pointer))
	def __isub__(self, point):
		return line3di(line3di_sub_set(self.c_pointer, point.c_pointer))
	def __eq__(self, other):
		return line3di_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return line3di_neq(self.c_pointer, other.c_pointer)
	def setLine1(self, xa, ya, za, xb, yb, zb):
		line3di_setLine1(self.c_pointer, xa, ya, za, xb, yb, zb)
	def setLine2(self, nstart, nend):
		line3di_setLine2(self.c_pointer, nstart.c_pointer, nend.c_pointer)
	def setLine3(self, line):
		line3di_setLine3(self.c_pointer, line.c_pointer)
	def getLength(self):
		return line3di_getLength(self.c_pointer)
	def getLengthSQ(self):
		return line3di_getLengthSQ(self.c_pointer)
	def getMiddle(self):
		return line3di_getMiddle(self.c_pointer)
	def getVector(self):
		return vector3di(line3di_getVector(self.c_pointer))
	def isPointBetweenStartAndEnd(self, point):
		return line3di_isPointBetweenStartAndEnd(self.c_pointer, point.c_pointer)
	def getClosestPoint(self, point):
		return line3di_getClosestPoint(self.c_pointer, point.c_pointer)
	def getIntersectionWithSphere(self, sorigin, sradius, outdistance):
		return line3di_getIntersectionWithSphere(self.c_pointer, sorigin.c_pointer, sradius, ctypes.byref(outdistance))

class triangle3df(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = triangle3df_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 3:
			self.c_pointer = triangle3df_ctor2(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				triangle3df_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(%s, %s, %s)' % (self.__class__.__name__, str(self.pointA), str(self.pointB), str(self.pointC))
	def __str__(self):
		return self.__repr__()
	def __eq__(self, other):
		return triangle3df_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return triangle3df_operator_ne(self.c_pointer, other.c_pointer)
	def isTotalInsideBox(self, box):
		return triangle3df_isTotalInsideBox(self.c_pointer, box.c_pointer)
	def isTotalOutsideBox(self, box):
		return triangle3df_isTotalOutsideBox(self.c_pointer, box.c_pointer)
	def closestPointOnTriangle(self, p):
		return vector3df(triangle3df_closestPointOnTriangle(self.c_pointer, p.c_pointer))
	def isPointInside(self, p):
		return triangle3df_isPointInside(self.c_pointer, p.c_pointer)
	def isPointInsideFast(self, p):
		return triangle3df_isPointInsideFast(self.c_pointer, p.c_pointer)
	def getIntersectionWithLimitedLine(self, line, outIntersection):
		return triangle3df_getIntersectionWithLimitedLine(self.c_pointer, line.c_pointer, outIntersection.c_pointer)
	def getIntersectionWithLine(self, linePoint, lineVect, outIntersection):
		return triangle3df_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getIntersectionOfPlaneWithLine(self, linePoint, lineVect, outIntersection):
		return triangle3df_getIntersectionOfPlaneWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getNormal(self):
		return vector3df(triangle3df_getNormal(self.c_pointer))
	def isFrontFacing(self, lookDirection):
		return triangle3df_isFrontFacing(self.c_pointer, lookDirection.c_pointer)
	def getPlane(self):
		return plane3df(triangle3df_getPlane(self.c_pointer))
	def getArea(self):
		return triangle3df_getArea(self.c_pointer)
	def set(self, a, b, c):
		triangle3df_set(self.c_pointer, a.c_pointer, b.c_pointer, c.c_pointer)
	def get_pointA(self):
		return vector3df(triangle3df_get_pointA(self.c_pointer))
	def get_pointB(self):
		return vector3df(triangle3df_get_pointB(self.c_pointer))
	def get_pointC(self):
		return vector3df(triangle3df_get_pointC(self.c_pointer))
	def set_pointA(self, value):
		triangle3df_set_pointA(self.c_pointer, value.c_pointer)
	def set_pointB(self, value):
		triangle3df_set_pointB(self.c_pointer, value.c_pointer)
	def set_pointC(self, value):
		triangle3df_set_pointC(self.c_pointer, value.c_pointer)
	pointA = property(get_pointA, set_pointA) 
	pointB = property(get_pointB, set_pointB) 
	pointC = property(get_pointC, set_pointC) 

class triangle3di(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = triangle3di_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 3:
			self.c_pointer = triangle3di_ctor2(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				triangle3di_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __eq__(self, other):
		return triangle3di_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return triangle3di_operator_ne(self.c_pointer, other.c_pointer)
	def isTotalInsideBox(self, box):
		return triangle3di_isTotalInsideBox(self.c_pointer, box.c_pointer)
	def isTotalOutsideBox(self, box):
		return triangle3di_isTotalOutsideBox(self.c_pointer, box.c_pointer)
	def closestPointOnTriangle(self, p):
		return vector3di(triangle3di_closestPointOnTriangle(self.c_pointer, p.c_pointer))
	def isPointInside(self, p):
		return triangle3di_isPointInside(self.c_pointer, p.c_pointer)
	def isPointInsideFast(self, p):
		return triangle3di_isPointInsideFast(self.c_pointer, p.c_pointer)
	def getIntersectionWithLimitedLine(self, line, outIntersection):
		return triangle3di_getIntersectionWithLimitedLine(self.c_pointer, line.c_pointer, outIntersection.c_pointer)
	def getIntersectionWithLine(self, linePoint, lineVect, outIntersection):
		return triangle3di_getIntersectionWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getIntersectionOfPlaneWithLine(self, linePoint, lineVect, outIntersection):
		return triangle3di_getIntersectionOfPlaneWithLine(self.c_pointer, linePoint.c_pointer, lineVect.c_pointer, outIntersection.c_pointer)
	def getNormal(self):
		return vector3di(triangle3di_getNormal(self.c_pointer))
	def isFrontFacing(self, lookDirection):
		return triangle3di_isFrontFacing(self.c_pointer, lookDirection.c_pointer)
	def getPlane(self):
		return plane3di(triangle3di_getPlane(self.c_pointer))
	def getArea(self):
		return triangle3di_getArea(self.c_pointer)
	def set(self, a, b, c):
		triangle3di_set(self.c_pointer, a.c_pointer, b.c_pointer, c.c_pointer)
	def get_pointA(self):
		return vector3di(triangle3di_get_pointA(self.c_pointer))
	def get_pointB(self):
		return vector3di(triangle3di_get_pointB(self.c_pointer))
	def get_pointC(self):
		return vector3di(triangle3di_get_pointC(self.c_pointer))
	def set_pointA(self, value):
		triangle3di_set_pointA(self.c_pointer, value.c_pointer)
	def set_pointB(self, value):
		triangle3di_set_pointB(self.c_pointer, value.c_pointer)
	def set_pointC(self, value):
		triangle3di_set_pointC(self.c_pointer, value.c_pointer)
	pointA = property(get_pointA, set_pointA) 
	pointB = property(get_pointB, set_pointB) 
	pointC = property(get_pointC, set_pointC) 

class S3DVertex(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
			self.delete_c_pointer = False
		elif len(args) == 0:
			self.c_pointer = self.ctor1()
		elif len(args) == 1:
			if isinstance(args[0], (int, long)):
				self.c_pointer = self.ctor1(args[0])
			elif isinstance(args[0], (tuple, list)):
				idx = 0
				self.c_pointer = self.ctor1(len(args[0]))
				for it in args[0]:
					self.set_item(it.c_pointer, idx)
					idx = idx + 1
		elif len(args) == 4:
			self.c_pointer = self.ctor3(*args)
		elif len(args) == 9:
			self.c_pointer = self.ctor2(*args)
	def ctor1(self, length = 1):
		return S3DVertex_ctor1(length)
	def ctor2(self, x, y, z, nx, ny, nz, c, tu, tv):
		return S3DVertex_ctor2(x, y, z, nx, ny, nz, c.c_pointer, tu, tv)
	def ctor3(self, pos, normal, color, tcoords):
		return S3DVertex_ctor3(pos.c_pointer, normal.c_pointer, color.c_pointer, tcoords.c_pointer)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(%s, %s, %s, %s)' % (self.__class__.__name__, str(self.Pos), str(self.Normal), str(self.Color), str(self.TCoords))
	def __str__(self):
		return self.__repr__()
	def __eq__(self, other):
		return self.eq(other.c_pointer)
	def __ne__(self, other):
		return self.ne(other.c_pointer)
	def __le__(self, other):
		return self.less(other.c_pointer)
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, item):
		return self.set_item(item, key)
	def get_item(self, index = 0):
		return S3DVertex(c_pointer = S3DVertex_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		S3DVertex_set_item(self.c_pointer, item.c_pointer, index)
	def get_Pos(self, index = 0):
		return vector3df(S3DVertex_get_Pos(self.c_pointer, index))
	def set_Pos(self, value, index = 0):
		S3DVertex_set_Pos(self.c_pointer, value.c_pointer, index)
	def get_Normal(self, index = 0):
		return vector3df(S3DVertex_get_Normal(self.c_pointer, index))
	def set_Normal(self, value, index = 0):
		S3DVertex_set_Normal(self.c_pointer, value.c_pointer, index)
	def get_Color(self, index = 0):
		return SColor(S3DVertex_get_Color(self.c_pointer, index))
	def set_Color(self, value, index = 0):
		S3DVertex_set_Color(self.c_pointer, value.c_pointer, index)
	def get_TCoords(self, index = 0):
		return vector2df(S3DVertex_get_TCoords(self.c_pointer, index))
	def set_TCoords(self, value, index = 0):
		S3DVertex_set_TCoords(self.c_pointer, value.c_pointer, index)
	def eq(self, other, index = 0):
		return S3DVertex_eq(self.c_pointer, other.c_pointer, index)
	def ne(self, other, index = 0):
		return S3DVertex_ne(self.c_pointer, other.c_pointer, index)
	def less(self, other, index = 0):
		return S3DVertex_less(self.c_pointer, other.c_pointer, index)
	def getType(self, index = 0):
		return S3DVertex_getType(self.c_pointer, index)
	Pos = property(get_Pos, set_Pos) 
	Normal = property(get_Normal, set_Normal) 
	Color = property(get_Color, set_Color) 
	TCoords = property(get_TCoords, set_TCoords) 
	if IRRLICHT_VERSION >= 180:
		def S3DVertex_getInterpolated(self, other, d, index = 0):
			return S3DVertex(c_pointer = S3DVertex_getInterpolated(self.c_pointer, other.c_pointer, d, index))

class S3DVertex2TCoords(S3DVertex):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
			self.delete_c_pointer = False
		elif len(args) == 0:
			self.c_pointer = self.ctor1()
		elif len(args) == 1:
			if isinstance(args[0], (int, long)):
				self.c_pointer = self.ctor1(args[0])
			elif hasattr(args[0], 'c_pointer'):
				self.c_pointer = self.ctor8(args[0])
			elif isinstance(args[0], (tuple, list)):
				idx = 0
				self.c_pointer = self.ctor1(len(args[0]))
				for it in args[0]:
					self.set_item(it.c_pointer, idx)
					idx = idx + 1
		elif len(args) == 4:
			if isinstance(args[0], SColor):
				self.c_pointer = self.ctor3(*args)
			else:
				self.c_pointer = self.ctor7(*args)
		elif len(args) == 5:
			self.c_pointer = self.ctor4(*args)
		elif len(args) == 8:
			self.c_pointer = self.ctor2(*args)
		elif len(args) == 9:
			self.c_pointer = self.ctor6(*args)
		elif len(args) == 11:
			self.c_pointer = self.ctor5(*args)
	def ctor1(self, length = 1):
		return S3DVertex2TCoords_ctor1(length)
	def ctor2(self, x, y, z, c, tu, tv, tu2, tv2):
		return S3DVertex2TCoords_ctor2(x, y, z, c.c_pointer, tu, tv, tu2, tv2)
	def ctor3(self, pos, color, tcoords, tcoords2):
		return S3DVertex2TCoords_ctor3(pos.c_pointer, color.c_pointer, tcoords.c_pointer, tcoords2.c_pointer)
	def ctor4(self, pos, normal, color, tcoords, tcoords2):
		return S3DVertex2TCoords_ctor4(pos.c_pointer, normal.c_pointer, color.c_pointer, tcoords.c_pointer, tcoords2.c_pointer)
	def ctor5(self, x, y, z, nx, ny, nz, c, tu, tv, tu2, tv2):
		return S3DVertex2TCoords_ctor5(x, y, z, nx, ny, nz, c.c_pointer, tu, tv, tu2, tv2)
	def ctor6(self, x, y, z, nx, ny, nz, c, tu, tv):
		return S3DVertex2TCoords_ctor6(x, y, z, nx, ny, nz, c.c_pointer, tu, tv)
	def ctor7(self, pos, normal, color, tcoords):
		return S3DVertex2TCoords_ctor7(pos.c_pointer, normal.c_pointer, color.c_pointer, tcoords.c_pointer)
	def ctor8(self, other):
		return S3DVertex2TCoords_ctor8(other.c_pointer)
	def get_TCoords2(self, index = 0):
		return vector2df(S3DVertex_get_TCoords2(self.c_pointer, index))
	def set_TCoords2(self, value, index = 0):
		S3DVertex_set_TCoords2(self.c_pointer, value.c_pointer, index)
	TCoords2 = property(get_TCoords2, set_TCoords2) 
	def __repr__(self):
		return '%s(%s, %s, %s, %s, %s)' % (self.__class__.__name__, str(self.Pos), str(self.Normal), str(self.Color), str(self.TCoords), str(self.TCoords2))

class S3DVertexTangents(S3DVertex):
	class SColor(object):
		'Dummy class of original, used for default parameters'
		def __init__(self, *args, **kwargs):
			self.c_pointer = None
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
			self.delete_c_pointer = False
		elif len(args) == 0:
			self.c_pointer = self.ctor1()
		elif len(args) == 1:
			if isinstance(args[0], (int, long)):
				self.c_pointer = self.ctor1(args[0])
	def ctor1(self, length = 1):
		return S3DVertex2TCoords_ctor1(length)
	def ctor2(self, x, y, z, nx = 0.0, ny = 0.0, nz = 0.0, c = SColor(255, 255, 255, 255), tu = 0.0, tv = 0.0, tanx = 0.0, tany = 0.0, tanz = 0.0, bx = 0.0, by = 0.0, bz = 0.0):
		return S3DVertexTangents_ctor2(x, y, z, nx, ny, nz, c.c_pointer, tu, tv, tanx, tany, tanz, bx, by, bz)
	def ctor3(self, pos, c, tcoords):
		return S3DVertexTangents_ctor3(pos.c_pointer, c.c_pointer, tcoords.c_pointer)
	def ctor4(self, pos, normal, c, tcoords, tangent = vector3df(), binormal = vector3df()):
		return S3DVertexTangents_ctor4(pos.c_pointer, normal.c_pointer, c.c_pointer, tcoords.c_pointer, tangent.c_pointer, binormal.c_pointer)
	def get_Tangent(self, index):
		return S3DVertexTangents_get_Tangent(self.c_pointer, index)
	def set_Tangent(self, value, index):
		S3DVertexTangents_set_Tangent(self.c_pointer, value.c_pointer, index)
	Tangent = property(get_Tangent, set_Tangent) 
	def get_Binormal(self, index):
		return S3DVertexTangents_get_Binormal(self.c_pointer, index)
	def set_Binormal(self, value, index):
		S3DVertexTangents_set_Binormal(self.c_pointer, value.c_pointer, index)
	Binormal = property(get_Binormal, set_Binormal) 
	def __repr__(self):
		return '%s(%s, %s, %s, %s, %s, %s)' % (self.__class__.__name__, str(self.Pos), str(self.Normal), str(self.Color), str(self.TCoords), str(self.Tangent), str(self.Binormal))

class SColor(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
		elif len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SColor_ctor1()
		elif len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 4:
			self.c_pointer = SColor_ctor2(*args)
		elif 'color' in kwargs:
			self.c_pointer = SColor_ctor3(kwargs.pop('color', 0))
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SColor_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def getAlpha(self):
		return SColor_getAlpha(self.c_pointer)
	def getRed(self):
		return SColor_getRed(self.c_pointer)
	def getGreen(self):
		return SColor_getGreen(self.c_pointer)
	def getBlue(self):
		return SColor_getBlue(self.c_pointer)
	def getLuminance(self):
		return SColor_getLuminance(self.c_pointer)
	def getAverage(self):
		return SColor_getAverage(self.c_pointer)
	def setAlpha(self, a):
		return SColor_setAlpha(self.c_pointer, a)
	def setRed(self, r):
		return SColor_setRed(self.c_pointer, r)
	def setGreen(self, g):
		return SColor_setGreen(self.c_pointer, g)
	def setBlue(self, b):
		return SColor_setBlue(self.c_pointer, b)
	def toA1R5G5B5(self):
		return SColor_toA1R5G5B5(self.c_pointer)
	def toOpenGLColor(self, dest):
		SColor_toOpenGLColor(self.c_pointer, dest)
	def set(self, a, r, g, b):
		SColor_set(self.c_pointer, a, r, g, b)
	def set2(self, col):
		SColor_set2(self.c_pointer, col)
	def operator_equal(self, other):
		return SColor_operator_equal(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return SColor_operator_equal(self.c_pointer, other.c_pointer)
	def operator_notequal(self, other):
		return SColor_operator_notequal(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return SColor_operator_notequal(self.c_pointer, other.c_pointer)
	def operator_less(self, other):
		return SColor_operator_less(self.c_pointer, other.c_pointer)
	def __le__(self, other):
		return SColor_operator_less(self.c_pointer, other.c_pointer)
	def operator_add(self, other):
		return SColor_operator_add(self.c_pointer, other.c_pointer)
	def __add__(self, other):
		return SColor_operator_add(self.c_pointer, other.c_pointer)
	def getInterpolated(self, other, d):
		return SColor_getInterpolated(self.c_pointer, other.c_pointer, d)
	def getInterpolated_quadratic(self, c1, c2, d):
		return SColor_getInterpolated_quadratic(self.c_pointer, c1, c2, d)
	def color(self):
		return SColor_color(self.c_pointer)
	a = property(getAlpha, setAlpha) 
	r = property(getRed, setRed) 
	g = property(getGreen, setGreen) 
	b = property(getBlue, setBlue) 
	def __repr__(self):
		return '%s(%d, %d, %d, %d)' % (self.__class__.__name__, self.a, self.r, self.g, self.b)
	def __str__(self):
		return self.__repr__()

class SColorf(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
		elif len(args) == 0:
			self.c_pointer = SColorf_ctor1()
		elif len(args) == 1:
			if isinstance(args[0], SColor):
				self.c_pointer = SColorf_ctor3(args[0].c_pointer)
			else:
				self.c_pointer = args[0]
				self.delete_c_pointer = False
		elif len(args) == 3:
			self.c_pointer = SColorf_ctor2(args[0], args[1], args[2], 1.0)
		elif len(args) == 4:
			self.c_pointer = SColorf_ctor2(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SColorf_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(%f, %f, %f, %f)' % (self.__class__.__name__, self.a, self.r, self.g, self.b)
	def __str__(self):
		return self.__repr__()
	def toSColor(self):
		return SColor(SColorf_toSColor(self.c_pointer))
	def set1(self, rr, gg, bb):
		SColorf_set1(self.c_pointer, rr, gg, bb)
	def set2(self, aa, rr, gg, bb):
		SColorf_set2(self.c_pointer, aa, rr, gg, bb)
	def set(self, *args):
		if len(args) > 3:
			self.set2(*args)
		else:
			self.set1(*args)
	def getInterpolated(self, other, d):
		return SColorf(SColorf_getInterpolated(self.c_pointer, other.c_pointer, d))
	def getInterpolated_quadratic(self, c1, c2, d):
		return SColorf(SColorf_getInterpolated_quadratic(self.c_pointer, c1.c_pointer, c2.c_pointer, d))
	def setColorComponentValue(self, index, value):
		SColorf_setColorComponentValue(self.c_pointer, index, value)
	def getAlpha(self):
		return SColorf_getAlpha(self.c_pointer)
	def getRed(self):
		return SColorf_getRed(self.c_pointer)
	def getGreen(self):
		return SColorf_getGreen(self.c_pointer)
	def getBlue(self):
		return SColorf_getBlue(self.c_pointer)
	def setAlpha(self, value):
		SColorf_setAlpha(self.c_pointer, value)
	def setRed(self, value):
		SColorf_setRed(self.c_pointer, value)
	def setGreen(self, value):
		SColorf_setGreen(self.c_pointer, value)
	def setBlue(self, value):
		SColorf_setBlue(self.c_pointer, value)
	a = property(getAlpha, setAlpha) 
	r = property(getRed, setRed) 
	g = property(getGreen, setGreen) 
	b = property(getBlue, setBlue) 

class SColorHSL(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif len(args) == 3:
			self.c_pointer = SColorHSL_ctor(*args)
	def ctor(self, h = 0.0, s = 0.0, l = 0.0):
		self.c_pointer = SColorHSL_ctor(h, s, l)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SColorHSL_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __repr__(self):
		return '%s(Hue = %f, Saturation = %f, Luminance = %f)' % (self.__class__.__name__, self.Hue, self.Saturation, self.Luminance)
	def __str__(self):
		return self.__repr__()
	def fromRGB(self, color):
		SColorHSL_fromRGB(self.c_pointer, color.c_pointer)
	def toRGB(self, color):
		SColorHSL_toRGB(self.c_pointer, color.c_pointer)
	def get_Hue(self):
		return SColorHSL_get_Hue(self.c_pointer)
	def get_Saturation(self):
		return SColorHSL_get_Saturation(self.c_pointer)
	def get_Luminance(self):
		return SColorHSL_get_Luminance(self.c_pointer)
	def set_Hue(self, value):
		SColorHSL_set_Hue(self.c_pointer, value)
	def set_Saturation(self, value):
		SColorHSL_set_Saturation(self.c_pointer, value)
	def set_Luminance(self, value):
		SColorHSL_set_Luminance(self.c_pointer, value)
	Hue = property(get_Hue, set_Hue) 
	Saturation = property(get_Saturation, set_Saturation) 
	Luminance = property(get_Luminance, set_Luminance) 

class matrix4:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 1:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer')
		elif 'other' in kwargs:
			self.c_pointer = matrix4_ctor2(kwargs.pop('other').c_pointer, EM4CONST_COPY)
		elif 'other' in kwargs and 'constructor' in kwargs:
			self.c_pointer = matrix4_ctor2(kwargs.pop('other').c_pointer, kwargs.pop('constructor', EM4CONST_COPY))
		elif 'constructor' in kwargs:
			self.c_pointer = matrix4_ctor1(kwargs.pop('constructor', EM4CONST_IDENTITY))
		else:
			self.c_pointer = matrix4_ctor1(EM4CONST_IDENTITY)
	def __repr__(self):
		return '%s(%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f)' % (self.__class__.__name__, self[0], self[1], self[2], self[3], self[4], self[5], self[6], self[7], self[8], self[9], self[10], self[11], self[12], self[13], self[14], self[15])
	def __str__(self):
		return self.__repr__()
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				matrix4_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __getslice__(self, row, col):
		return matrix4_operator_directly(self.c_pointer, row, col)
	def __getitem__(self, index):
		return matrix4_operator_linearly(self.c_pointer, index)
	def set1(self, other):
		matrix4_set1(self.c_pointer, other.c_pointer)
	def set2(self, scalar):
		matrix4_set2(self.c_pointer, scalar)
	def const_pointer(self):
		return matrix4_const_pointer(self.c_pointer)
	def pointer(self):
		return matrix4_pointer(self.c_pointer)
	def __eq__(self, other):
		return matrix4_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return matrix4_noteq(self.c_pointer, other.c_pointer)
	def __add__(self, other):
		matrix4_add(self.c_pointer, other.c_pointer)
	def __iadd__(self, other):
		return matrix4(matrix4_get_add(self.c_pointer, other.c_pointer))
	def __sub__(self, other):
		matrix4_sub(self.c_pointer, other.c_pointer)
	def __isub__(self, other):
		return matrix4(matrix4_get_sub(self.c_pointer, other.c_pointer))
	def setbyproduct(self, other_a, other_b):
		return matrix4_setbyproduct(self.c_pointer, other_a.c_pointer, other_b.c_pointer)
	def setbyproduct_nocheck(self, other_a, other_b):
		return matrix4_setbyproduct_nocheck(self.c_pointer, other_a.c_pointer, other_b.c_pointer)
	def __mul__(self, arg):
		if hasattr(arg, 'c_pointer'):
			self.multiplication1(arg)
		else:
			self.multiplication2(arg)
	def multiplication1(self, other):
		matrix4_multiplication1(self.c_pointer, other.c_pointer)
	def multiplication2(self, scalar):
		matrix4_multiplication2(self.c_pointer, scalar)
	def __imul__(self, arg):
		if hasattr(arg, 'c_pointer'):
			return self.get_multiplication1(arg)
		else:
			return self.get_multiplication2(arg)
	def get_multiplication1(self, other):
		return matrix4(matrix4_get_multiplication1(self.c_pointer, other.c_pointer))
	def get_multiplication2(self, scalar):
		return matrix4(matrix4_get_multiplication2(self.c_pointer, scalar))
	def makeIdentity(self):
		return matrix4_makeIdentity(self.c_pointer)
	def isIdentity(self):
		return matrix4_isIdentity(self.c_pointer)
	def isOrthogonal(self):
		return matrix4_isOrthogonal(self.c_pointer)
	def isIdentity_integer_base(self):
		return matrix4_isIdentity_integer_base(self.c_pointer)
	def setTranslation(self, translation):
		return matrix4_setTranslation(self.c_pointer, translation.c_pointer)
	def getTranslation(self):
		return vector3df(matrix4_getTranslation(self.c_pointer))
	def setInverseTranslation(self, translation):
		return matrix4_setInverseTranslation(self.c_pointer, translation.c_pointer)
	def setRotationRadians(self, rotation):
		return matrix4_setRotationRadians(self.c_pointer, rotation.c_pointer)
	def setRotationDegrees(self, rotation):
		return matrix4_setRotationDegrees(self.c_pointer, rotation.c_pointer)
	def getRotationDegrees(self):
		return vector3df(matrix4_getRotationDegrees(self.c_pointer))
	def setInverseRotationRadians(self, rotation):
		return matrix4_setInverseRotationRadians(self.c_pointer, rotation.c_pointer)
	def setInverseRotationDegrees(self, rotation):
		return matrix4_setInverseRotationDegrees(self.c_pointer, rotation.c_pointer)
	def setScale1(self, scale):
		return matrix4_setScale1(self.c_pointer, scale.c_pointer)
	def setScale2(self, scale):
		return matrix4_setScale2(self.c_pointer, scale)
	def setScale(self, scale):
		if hasattr(scale, 'c_pointer'):
			return self.setScale1(scale)
		else:
			return self.setScale2(scale)
	def getScale(self):
		return vector3df(matrix4_getScale(self.c_pointer))
	def inverseTranslateVect(self, vect):
		matrix4_inverseTranslateVect(self.c_pointer, vect.c_pointer)
	def inverseRotateVect(self, vect):
		matrix4_inverseRotateVect(self.c_pointer, vect.c_pointer)
	def rotateVect1(self, vect):
		matrix4_rotateVect1(self.c_pointer, vect.c_pointer)
	def rotateVect2(self, out, inp):
		matrix4_rotateVect2(self.c_pointer, out.c_pointer, inp.c_pointer)
	def rotateVect3(self, out, inp):
		matrix4_rotateVect3(self.c_pointer, out, inp.c_pointer)
	def rotateVect(self, *args):
		if len(args) == 1:
			self.rotateVect1(*args)
		elif hasattr(args[0], 'c_pointer'):
			self.rotateVect2(*args)
		else:
			self.rotateVect3(*args)
	def transformVect1(self, vect):
		matrix4_transformVect1(self.c_pointer, vect.c_pointer)
	def transformVect2(self, out, inp):
		matrix4_transformVect2(self.c_pointer, out.c_pointer, inp.c_pointer)
	def transformVect3(self, out, inp):
		matrix4_transformVect3(self.c_pointer, out, inp.c_pointer)
	def transformVect(self, *args):
		if len(args) == 1:
			self.transformVect1(*args)
		elif hasattr(args[0], 'c_pointer'):
			self.transformVect2(*args)
		else:
			self.transformVect3(*args)
	def translateVect(self, vect):
		matrix4_translateVect(self.c_pointer, vect.c_pointer)
	def transformPlane1(self, plane):
		matrix4_transformPlane1(self.c_pointer, plane.c_pointer)
	def transformPlane2(self, inp, out):
		matrix4_transformPlane2(self.c_pointer, inp.c_pointer, out.c_pointer)
	def transformPlane(self, *args):
		if len(args) == 1:
			self.transformPlane1(*args)
		else:
			self.transformPlane2(*args)
	#def transformBox(self, box):
		#matrix4_transformBox(self.c_pointer, box.c_pointer)
	def transformBoxEx(self, box):
		matrix4_transformBoxEx(self.c_pointer, box.c_pointer)
	def multiplyWith1x4Matrix(self, matrix):
		matrix4_multiplyWith1x4Matrix(self.c_pointer, matrix)
	def makeInverse(self):
		return matrix4_makeInverse(self.c_pointer)
	def getInversePrimitive(self, out):
		return matrix4_getInversePrimitive(self.c_pointer, out.c_pointer)
	def getInverse(self, out):
		return matrix4_getInverse(self.c_pointer, out.c_pointer)
	def buildProjectionMatrixPerspectiveFovRH(self, fieldOfViewRadians, aspectRatio, zNear, zFar):
		return matrix4_buildProjectionMatrixPerspectiveFovRH(self.c_pointer, fieldOfViewRadians, aspectRatio, zNear, zFar)
	def buildProjectionMatrixPerspectiveFovLH(self, fieldOfViewRadians, aspectRatio, zNear, zFar):
		return matrix4_buildProjectionMatrixPerspectiveFovLH(self.c_pointer, fieldOfViewRadians, aspectRatio, zNear, zFar)
	def buildProjectionMatrixPerspectiveRH(self, widthOfViewVolume, heightOfViewVolume, zNear, zFar):
		return matrix4_buildProjectionMatrixPerspectiveRH(self.c_pointer, widthOfViewVolume, heightOfViewVolume, zNear, zFar)
	def buildProjectionMatrixPerspectiveLH(self, widthOfViewVolume, heightOfViewVolume, zNear, zFar):
		return matrix4_buildProjectionMatrixPerspectiveLH(self.c_pointer, widthOfViewVolume, heightOfViewVolume, zNear, zFar)
	def buildProjectionMatrixOrthoLH(self, widthOfViewVolume, heightOfViewVolume, zNear, zFar):
		return matrix4_buildProjectionMatrixOrthoLH(self.c_pointer, widthOfViewVolume, heightOfViewVolume, zNear, zFar)
	def buildProjectionMatrixOrthoRH(self, widthOfViewVolume, heightOfViewVolume, zNear, zFar):
		return matrix4_buildProjectionMatrixOrthoRH(self.c_pointer, widthOfViewVolume, heightOfViewVolume, zNear, zFar)
	def buildCameraLookAtMatrixLH(self, position, target, upVector):
		return matrix4_buildCameraLookAtMatrixLH(self.c_pointer, position.c_pointer, target.c_pointer, upVector.c_pointer)
	def buildCameraLookAtMatrixRH(self, position, target, upVector):
		return matrix4_buildCameraLookAtMatrixRH(self.c_pointer, position.c_pointer, target.c_pointer, upVector.c_pointer)
	def buildShadowMatrix(self, light, plane, point=1.0):
		return matrix4_buildShadowMatrix(self.c_pointer, light.c_pointer, plane.c_pointer, point)
	def buildNDCToDCMatrix(self, area, zScale):
		return matrix4_buildNDCToDCMatrix(self.c_pointer, area.c_pointer, zScale)
	def interpolate(self, b, time):
		matrix4_interpolate(self.c_pointer, b.c_pointer, time)
	def getTransposed1(self):
		return matrix4(matrix4_getTransposed1(self.c_pointer))
	def getTransposed2(self, dest):
		matrix4_getTransposed2(self.c_pointer, dest.c_pointer)
	def getTransposed(self, *args):
		if len(args) == 0:
			return self.getTransposed1()
		else:
			self.getTransposed2(*args)
	def buildRotateFromTo(self, from_vector3df, to_vector3df):
		return matrix4(matrix4_buildRotateFromTo(self.c_pointer, from_vector3df.c_pointer, to_vector3df.c_pointer))
	def setRotationCenter(self, center, translate):
		matrix4_setRotationCenter(self.c_pointer, center.c_pointer, translate.c_pointer)
	def buildAxisAlignedBillboard(self, v_camPos, v_center, v_translation, v_axis, v_from):
		matrix4_buildAxisAlignedBillboard(self.c_pointer, v_camPos.c_pointer, v_center.c_pointer, v_translation.c_pointer, v_axis.c_pointer, v_from.c_pointer)
	def buildTextureTransform(self, rotateRad, rotatecenter, translate, scale):
		return matrix4(matrix4_buildTextureTransform(self.c_pointer, rotateRad, rotatecenter.c_pointer, translate.c_pointer, scale.c_pointer))
	def setTextureRotationCenter(self, radAngle):
		return matrix4(matrix4_setTextureRotationCenter(self.c_pointer, radAngle))
	def setTextureTranslate(self, x, y):
		return matrix4(matrix4_setTextureTranslate(self.c_pointer, x, y))
	def setTextureTranslateTransposed(self, x, y):
		return matrix4(matrix4_setTextureTranslateTransposed(self.c_pointer, x, y))
	def setTextureScale(self, sx, sy):
		return matrix4(matrix4_setTextureScale(self.c_pointer, sx, sy))
	def setTextureScaleCenter(self, sx, sy):
		return matrix4(matrix4_setTextureScaleCenter(self.c_pointer, sx, sy))
	def setM(self, data):
		return matrix4(matrix4_setM(self.c_pointer, data))
	def setDefinitelyIdentityMatrix(self, isDefinitelyIdentityMatrix):
		matrix4_setDefinitelyIdentityMatrix(self.c_pointer, isDefinitelyIdentityMatrix)
	def getDefinitelyIdentityMatrix(self):
		return matrix4_getDefinitelyIdentityMatrix(self.c_pointer)

class quaternion(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor1()
		elif len(args) == 1:
			if isinstance(args[0], vector3df):
				self.c_pointer = self.ctor4(*args)
			elif isinstance(args[0], matrix4):
				self.c_pointer = self.ctor5(*args)
			else:
				self.c_pointer = args[0]
				self.delete_c_pointer = False
		elif len(args) == 4:
			self.c_pointer = self.ctor2(*args)
		elif len(args) == 3:
			self.c_pointer = self.ctor3(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				quaternion_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def ctor1(self):
		return quaternion_ctor1()
	def ctor2(self, x, y, z, w):
		return quaternion_ctor2(x, y, z, w)
	def ctor3(self, x, y, z):
		return quaternion_ctor3(x, y, z)
	def ctor4(self, vec):
		return quaternion_ctor4(vec.c_pointer)
	def ctor5(self, mat):
		return quaternion_ctor5(mat.c_pointer)
	def __eq__(self, other):
		return quaternion_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return quaternion_operator_ne(self.c_pointer, other.c_pointer)
	def operator_set1(self, other):
		return quaternion(quaternion_operator_set1(self.c_pointer, other.c_pointer))
	def operator_set2(self, other):
		return quaternion(quaternion_operator_set2(self.c_pointer, other.c_pointer))
	def operator_add(self, other):
		return quaternion(quaternion_operator_add(self.c_pointer, other.c_pointer))
	def operator_mul1(self, other):
		return quaternion(quaternion_operator_mul1(self.c_pointer, other.c_pointer))
	def operator_mul2(self, s):
		return quaternion(quaternion_operator_mul2(self.c_pointer, s))
	def operator_mul3(self, v):
		return vector3df(quaternion_operator_mul3(self.c_pointer, v.c_pointer))
	def operator_mul_set1(self, s):
		return quaternion(quaternion_operator_mul_set1(self.c_pointer, s))
	def operator_mul_set2(self, other):
		return quaternion(quaternion_operator_mul_set2(self.c_pointer, other.c_pointer))
	def dotProduct(self, other):
		return quaternion_dotProduct(self.c_pointer, other.c_pointer)
	def set1(self, x, y, z, w):
		return quaternion(quaternion_set1(self.c_pointer, x, y, z, w))
	def set2(self, x, y, z):
		return quaternion(quaternion_set2(self.c_pointer, x, y, z))
	def set3(self, vec):
		return quaternion(quaternion_set3(self.c_pointer, vec.c_pointer))
	def set4(self, quat):
		return quaternion(quaternion_set4(self.c_pointer, quat.c_pointer))
	def equals(self, other, tolerance = ROUNDING_ERROR_f32):
		return quaternion_equals(self.c_pointer, other.c_pointer, tolerance)
	def normalize(self):
		return quaternion(quaternion_normalize(self.c_pointer))
	def getMatrix1(self):
		return matrix4(quaternion_getMatrix1(self.c_pointer))
	def getMatrix2(self, translation):
		return matrix4(quaternion_getMatrix2(self.c_pointer, translation.c_pointer))
	def getMatrixCenter(self, center, translation):
		return matrix4(quaternion_getMatrixCenter(self.c_pointer, center.c_pointer, translation.c_pointer))
	def getMatrix_transposed(self):
		return matrix4(quaternion_getMatrix_transposed(self.c_pointer))
	def makeInverse(self):
		return quaternion(quaternion_makeInverse(self.c_pointer))
	def slerp(self, q1, q2, interpolate):
		return quaternion(quaternion_slerp(self.c_pointer, q1.c_pointer, q2.c_pointer, interpolate))
	def fromAngleAxis(self, angle, axis):
		return quaternion(quaternion_fromAngleAxis(self.c_pointer, angle, axis.c_pointer))
	def toAngleAxis(self, axis):
		return quaternion_toAngleAxis(self.c_pointer, axis.c_pointer)
	def toEuler(self):
		return vector3df(quaternion_toEuler(self.c_pointer))
	def makeIdentity(self):
		return quaternion(quaternion_makeIdentity(self.c_pointer))
	def rotationFromTo(self, from_value, to_value):
		return quaternion(quaternion_rotationFromTo(self.c_pointer, from_value.c_pointer, to_value.c_pointer))
	def get_X(self):
		return quaternion_get_X(self.c_pointer)
	def set_X(self, value):
		quaternion_set_X(self.c_pointer, value)
	X = property(get_X, set_X) 
	def get_Y(self):
		return quaternion_get_Y(self.c_pointer)
	def set_Y(self, value):
		quaternion_set_Y(self.c_pointer, value)
	Y = property(get_Y, set_Y) 
	def get_Z(self):
		return quaternion_get_Z(self.c_pointer)
	def set_Z(self, value):
		quaternion_set_Z(self.c_pointer, value)
	Z = property(get_Z, set_Z) 
	def get_W(self):
		return quaternion_get_W(self.c_pointer)
	def set_W(self, value):
		quaternion_set_W(self.c_pointer, value)
	W = property(get_W, set_W) 

class SMaterialLayer(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) > 0:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
		elif 'other' in kwargs:
			self.c_pointer = SMaterialLayer_ctor2(kwargs.pop('other').c_pointer, None)
		else:
			self.c_pointer = SMaterialLayer_ctor1()
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SMaterialLayer_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	#~ def Destructor(self):
		#~ SMaterialLayer_Destructor(self.c_pointer)
	def set(self, other):
		return SMaterialLayer_set(self.c_pointer, other.c_pointer)
	def set_Texture(self, value):
		SMaterialLayer_set_Texture(self.c_pointer, value.c_pointer)
	def get_Texture(self):
		return SMaterialLayer_get_Texture(self.c_pointer)
	Texture = property(get_Texture, set_Texture) 
	def set_TextureWrapU(self, value):
		SMaterialLayer_set_TextureWrapU(self.c_pointer, value)
	def get_TextureWrapU(self):
		return SMaterialLayer_get_TextureWrapU(self.c_pointer)
	TextureWrapU = property(get_TextureWrapU, set_TextureWrapU) 
	def set_TextureWrapV(self, value):
		SMaterialLayer_set_TextureWrapV(self.c_pointer, value)
	def get_TextureWrapV(self):
		return SMaterialLayer_get_TextureWrapV(self.c_pointer)
	TextureWrapV = property(get_TextureWrapV, set_TextureWrapV) 
	def set_BilinearFilter(self, value):
		SMaterialLayer_set_BilinearFilter(self.c_pointer, value)
	def get_BilinearFilter(self):
		return SMaterialLayer_get_BilinearFilter(self.c_pointer)
	BilinearFilter = property(get_BilinearFilter, set_BilinearFilter) 
	def set_TrilinearFilter(self, value):
		SMaterialLayer_set_TrilinearFilter(self.c_pointer, value)
	def get_TrilinearFilter(self):
		return SMaterialLayer_get_TrilinearFilter(self.c_pointer)
	TrilinearFilter = property(get_TrilinearFilter, set_TrilinearFilter) 
	def set_AnisotropicFilter(self, value):
		SMaterialLayer_set_AnisotropicFilter(self.c_pointer, value)
	def get_AnisotropicFilter(self):
		return SMaterialLayer_get_AnisotropicFilter(self.c_pointer)
	AnisotropicFilter = property(get_AnisotropicFilter, set_AnisotropicFilter) 
	def set_LODBias(self, value):
		SMaterialLayer_set_LODBias(self.c_pointer, value)
	def get_LODBias(self):
		return SMaterialLayer_get_LODBias(self.c_pointer)
	LODBias = property(get_LODBias, set_LODBias) 
	def getTextureMatrix(self):
		return matrix4(SMaterialLayer_getTextureMatrix(self.c_pointer))
	def setTextureMatrix(self, mat):
		SMaterialLayer_setTextureMatrix(self.c_pointer, mat.c_pointer)
	TextureMatrix = property(getTextureMatrix, setTextureMatrix) 
	def __eq__(self, other):
		return SMaterialLayer_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return SMaterialLayer_operator_noteq(self.c_pointer, other.c_pointer)

class SMaterial(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) > 0:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
		elif 'other' in kwargs:
			self.c_pointer = SMaterial_ctor2(kwargs.pop('other').c_pointer, None)
		else:
			self.c_pointer = SMaterial_ctor1()
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SMaterial_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def set(self, other):
		return SMaterial(SMaterial_set(self.c_pointer, other.c_pointer))
	def get_TextureLayer(self, index = 0):
		return SMaterialLayer(SMaterial_get_TextureLayer(self.c_pointer, index))
	def get_MaterialType(self):
		return SMaterial_get_MaterialType(self.c_pointer)
	def get_AmbientColor(self):
		return SColor(SMaterial_get_AmbientColor(self.c_pointer))
	def get_DiffuseColor(self):
		return SColor(SMaterial_get_DiffuseColor(self.c_pointer))
	def get_EmissiveColor(self):
		return SColor(SMaterial_get_EmissiveColor(self.c_pointer))
	def get_SpecularColor(self):
		return SColor(SMaterial_get_SpecularColor(self.c_pointer))
	def get_Shininess(self):
		return SMaterial_get_Shininess(self.c_pointer)
	def get_MaterialTypeParam(self):
		return SMaterial_get_MaterialTypeParam(self.c_pointer)
	def get_MaterialTypeParam2(self):
		return SMaterial_get_MaterialTypeParam2(self.c_pointer)
	def get_Thickness(self):
		return SMaterial_get_Thickness(self.c_pointer)
	def get_ZBuffer(self):
		return SMaterial_get_ZBuffer(self.c_pointer)
	def get_AntiAliasing(self):
		return SMaterial_get_AntiAliasing(self.c_pointer)
	def get_ColorMask(self):
		return SMaterial_get_ColorMask(self.c_pointer)
	def get_ColorMaterial(self):
		return SMaterial_get_ColorMaterial(self.c_pointer)
	def get_Wireframe(self):
		return SMaterial_get_Wireframe(self.c_pointer)
	def get_PointCloud(self):
		return SMaterial_get_PointCloud(self.c_pointer)
	def get_GouraudShading(self):
		return SMaterial_get_GouraudShading(self.c_pointer)
	def get_Lighting(self):
		return SMaterial_get_Lighting(self.c_pointer)
	def get_ZWriteEnable(self):
		return SMaterial_get_ZWriteEnable(self.c_pointer)
	def get_BackfaceCulling(self):
		return SMaterial_get_BackfaceCulling(self.c_pointer)
	def get_FrontfaceCulling(self):
		return SMaterial_get_FrontfaceCulling(self.c_pointer)
	def get_FogEnable(self):
		return SMaterial_get_FogEnable(self.c_pointer)
	def get_NormalizeNormals(self):
		return SMaterial_get_NormalizeNormals(self.c_pointer)
	def set_TextureLayer(self, texture_layer):
		SMaterial_set_TextureLayer(self.c_pointer, texture_layer.c_pointer)
	TextureLayer = property(get_TextureLayer, set_TextureLayer) 
	def set_MaterialType(self, value):
		SMaterial_set_MaterialType(self.c_pointer, value)
	MaterialType = property(get_MaterialType, set_MaterialType) 
	def set_AmbientColor(self, value):
		SMaterial_set_AmbientColor(self.c_pointer, value.c_pointer)
	AmbientColor = property(get_AmbientColor, set_AmbientColor) 
	def set_DiffuseColor(self, value):
		SMaterial_set_DiffuseColor(self.c_pointer, value.c_pointer)
	DiffuseColor = property(get_DiffuseColor, set_DiffuseColor) 
	def set_EmissiveColor(self, value):
		SMaterial_set_EmissiveColor(self.c_pointer, value.c_pointer)
	EmissiveColor = property(get_EmissiveColor, set_EmissiveColor) 
	def set_SpecularColor(self, value):
		SMaterial_set_SpecularColor(self.c_pointer, value.c_pointer)
	SpecularColor = property(get_SpecularColor, set_SpecularColor) 
	def set_Shininess(self, value):
		SMaterial_set_Shininess(self.c_pointer, value)
	Shininess = property(get_Shininess, set_Shininess) 
	def set_MaterialTypeParam(self, value):
		SMaterial_set_MaterialTypeParam(self.c_pointer, value)
	MaterialTypeParam = property(get_MaterialTypeParam, set_MaterialTypeParam) 
	def set_MaterialTypeParam2(self, value):
		SMaterial_set_MaterialTypeParam2(self.c_pointer, value)
	MaterialTypeParam2 = property(get_MaterialTypeParam2, set_MaterialTypeParam2) 
	def set_Thickness(self, value):
		SMaterial_set_Thickness(self.c_pointer, value)
	Thickness = property(get_Thickness, set_Thickness) 
	def set_ZBuffer(self, value):
		SMaterial_set_ZBuffer(self.c_pointer, value)
	ZBuffer = property(get_ZBuffer, set_ZBuffer) 
	def set_AntiAliasing(self, value):
		SMaterial_set_AntiAliasing(self.c_pointer, value)
	AntiAliasing = property(get_AntiAliasing, set_AntiAliasing) 
	def set_ColorMask(self, value):
		SMaterial_set_ColorMask(self.c_pointer, value)
	ColorMask = property(get_ColorMask, set_ColorMask) 
	def set_ColorMaterial(self, value):
		SMaterial_set_ColorMaterial(self.c_pointer, value)
	ColorMaterial = property(get_ColorMaterial, set_ColorMaterial) 
	def set_Wireframe(self, value):
		SMaterial_set_Wireframe(self.c_pointer, value)
	Wireframe = property(get_Wireframe, set_Wireframe) 
	def set_PointCloud(self, value):
		SMaterial_set_PointCloud(self.c_pointer, value)
	PointCloud = property(get_PointCloud, set_PointCloud) 
	def set_GouraudShading(self, value):
		SMaterial_set_GouraudShading(self.c_pointer, value)
	GouraudShading = property(get_GouraudShading, set_GouraudShading) 
	def set_Lighting(self, value):
		SMaterial_set_Lighting(self.c_pointer, value)
	Lighting = property(get_Lighting, set_Lighting) 
	def set_ZWriteEnable(self, value):
		SMaterial_set_ZWriteEnable(self.c_pointer, value)
	ZWriteEnable = property(get_ZWriteEnable, set_ZWriteEnable) 
	def set_BackfaceCulling(self, value):
		SMaterial_set_BackfaceCulling(self.c_pointer, value)
	BackfaceCulling = property(get_BackfaceCulling, set_BackfaceCulling) 
	def set_FrontfaceCulling(self, value):
		SMaterial_set_FrontfaceCulling(self.c_pointer, value)
	FrontfaceCulling = property(get_FrontfaceCulling, set_FrontfaceCulling) 
	def set_FogEnable(self, value):
		SMaterial_set_FogEnable(self.c_pointer, value)
	FogEnable = property(get_FogEnable, set_FogEnable) 
	def set_NormalizeNormals(self, value):
		SMaterial_set_NormalizeNormals(self.c_pointer, value)
	NormalizeNormals = property(get_NormalizeNormals, set_NormalizeNormals) 
	def getTextureMatrix(self, i):
		return matrix4(SMaterial_getTextureMatrix(self.c_pointer, i))
	def setTextureMatrix(self, i, mat):
		SMaterial_setTextureMatrix(self.c_pointer, i, mat.c_pointer)
	def getTexture(self, i):
		return ITexture(SMaterial_getTexture(self.c_pointer, i))
	def setTexture(self, i, tex):
		SMaterial_setTexture(self.c_pointer, i, tex.c_pointer)
	def setFlag(self, flag, value):
		SMaterial_setFlag(self.c_pointer, flag, value)
	def getFlag(self, flag):
		return SMaterial_getFlag(self.c_pointer, flag)
	def __ne__(self, other):
		return SMaterial_operator_noteq(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return SMaterial_operator_eq(self.c_pointer, other.c_pointer)
	def isTransparent(self):
		return SMaterial_isTransparent(self.c_pointer)

class SOverrideMaterial(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
		else:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				SOverrideMaterial_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def ctor(self):
		return SOverrideMaterial_ctor()
	def apply(self, material):
		SOverrideMaterial_apply(self.c_pointer, material.c_pointer)
	def get_Material(self):
		return SMaterial(SOverrideMaterial_get_Material(self.c_pointer))
	def set_Material(self, value):
		SOverrideMaterial_set_Material(self.c_pointer, value.c_pointer)
	Material = property(get_Material, set_Material) 
	def get_EnableFlags(self):
		return SOverrideMaterial_get_EnableFlags(self.c_pointer)
	def set_EnableFlags(self, value):
		SOverrideMaterial_set_EnableFlags(self.c_pointer, value)
	EnableFlags = property(get_EnableFlags, set_EnableFlags) 
	def get_EnablePasses(self):
		return SOverrideMaterial_get_EnablePasses(self.c_pointer)
	def set_EnablePasses(self, value):
		SOverrideMaterial_set_EnablePasses(self.c_pointer, value)
	EnablePasses = property(get_EnablePasses, set_EnablePasses) 
	def get_Enabled(self):
		return SOverrideMaterial_get_Enabled(self.c_pointer)
	def set_Enabled(self, value):
		SOverrideMaterial_set_Enabled(self.c_pointer, value)
	Enabled = property(get_Enabled, set_Enabled) 

class IRenderTarget(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) > 0:
			if isinstance(args[0], ITexture):
				self.c_pointer = self.ctor1(*args, **kwargs)
			else:
				self.c_pointer = self.ctor2(*args, **kwargs)
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				IRenderTarget_delete(self.c_pointer)
			except:
				pass
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	if IRRLICHT_VERSION < 180:
		def ctor1(self, texture, colorMask = ECP_ALL, blendFuncSrc = EBF_ONE, blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, blendEnable = False):
			return IRenderTarget_ctor1(texture.c_pointer, colorMask, blendFuncSrc, blendFuncDst, blendEnable)
		def ctor2(self, target, colorMask = ECP_ALL, blendFuncSrc = EBF_ONE, blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, blendEnable = False):
			return IRenderTarget_ctor2(target, colorMask, blendFuncSrc, blendFuncDst, blendEnable)
	else:
		def ctor1(self, texture, colorMask = ECP_ALL, blendFuncSrc = EBF_ONE, blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, blendOp = EBO_NONE):
			return IRenderTarget_ctor1(texture.c_pointer, colorMask, blendFuncSrc, blendFuncDst, blendEnable)
		def ctor2(self, target, colorMask = ECP_ALL, blendFuncSrc = EBF_ONE, blendFuncDst = EBF_ONE_MINUS_SRC_ALPHA, blendOp = EBO_NONE):
			return IRenderTarget_ctor2(target, colorMask, blendFuncSrc, blendFuncDst, blendEnable)
	def get_RenderTexture(self):
		return ITexture(IRenderTarget_get_RenderTexture(self.c_pointer))
	def set_RenderTexture(self, value):
		IRenderTarget_set_RenderTexture(self.c_pointer, value)
	RenderTexture = property(get_RenderTexture, set_RenderTexture) 
	def get_TargetType(self):
		return IRenderTarget_get_TargetType(self.c_pointer)
	def set_TargetType(self, value):
		IRenderTarget_set_TargetType(self.c_pointer, value)
	TargetType = property(get_TargetType, set_TargetType) 
	def get_ColorMask(self):
		return IRenderTarget_get_ColorMask(self.c_pointer)
	def set_ColorMask(self, value):
		IRenderTarget_set_ColorMask(self.c_pointer, value)
	ColorMask = property(get_ColorMask, set_ColorMask) 
	def get_BlendFuncSrc(self):
		return IRenderTarget_get_BlendFuncSrc(self.c_pointer)
	def set_BlendFuncSrc(self, value):
		IRenderTarget_set_BlendFuncSrc(self.c_pointer, value)
	BlendFuncSrc = property(get_BlendFuncSrc, set_BlendFuncSrc) 
	def get_BlendFuncDst(self):
		return IRenderTarget_get_BlendFuncDst(self.c_pointer)
	def set_BlendFuncDst(self, value):
		IRenderTarget_set_BlendFuncDst(self.c_pointer, value)
	BlendFuncDst = property(get_BlendFuncDst, set_BlendFuncDst) 
	if IRRLICHT_VERSION < 180:
		def get_BlendEnable(self):
			return IRenderTarget_get_BlendEnable(self.c_pointer)
		def set_BlendEnable(self, value):
			IRenderTarget_set_BlendEnable(self.c_pointer, value)
		BlendEnable = property(get_BlendEnable, set_BlendEnable)
	else:
		def get_BlendOp(self):
			return IRenderTarget_get_BlendOp(self.c_pointer)
		def set_BlendOp(self, value):
			IRenderTarget_set_BlendOp(self.c_pointer, value)
		BlendOp = property(get_BlendOp, set_BlendOp)

class ISceneUserDataSerializer:
	def __init__(self, *args, **kwargs):
		self.c_pointer = 0
		if len(args) > 0:
			self.c_pointer = args[0]
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)

class IReferenceCounted:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
		#~ ctypes.pythonapi.Py_IncRef(ctypes.py_object(self))
	#~ def __del__(self):
		#~ IReferenceCounted_Destructor(self.c_pointer)
		#~ ctypes.pythonapi.Py_DecRef(ctypes.py_object(self))
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	#~ def Destructor(self):
		#~ IReferenceCounted_Destructor(self.c_pointer)
	def grab(self):
		IReferenceCounted_grab(self.c_pointer)
	def drop(self):
		return IReferenceCounted_drop(self.c_pointer)
	def getReferenceCount(self):
		return IReferenceCounted_getReferenceCount(self.c_pointer)
	def getDebugName(self):
		return IReferenceCounted_getDebugName(self.c_pointer)
	def IsNull(self):
		return IReferenceCounted_is_null(self.c_pointer)
	def __eq__(self, other):
		if hasattr(other, 'c_pointer'):
			return self.c_pointer == other.c_pointer
		else:
			return False
	def __ne__(self, other):
		if hasattr(other, 'c_pointer'):
			return self.c_pointer != other.c_pointer
		else:
			return False

#~ class ICollisionCallback(IReferenceCounted, class_thread):
class ICollisionCallback(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.callback = onCollisionFunc(self.onCollision)
		if len(args) > 0:
			self.c_pointer = ICollisionCallback_ctor1(args[0])
		else:
			self.c_pointer = ICollisionCallback_ctor2(self.callback)
		#~ class_thread.__init__(self)
		#~ self.setDaemon(True)
		#~ self.start()
	#~ def Destructor(self):
		#~ ICollisionCallback_Destructor(self.c_pointer)
	def set_func_animator(self, animator_func):
		ICollisionCallback_set_func_animator(self.c_pointer, animator_func)
	def onCollision(self, animator):
		'must be replaced with custom ICollisionCallback class'
		return False
	def convert_pointer(self):
		self.c_pointer = ICollisionCallback_ctor1(self.c_pointer)

class IFileList(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getFileCount(self):
		return IFileList_getFileCount(self.c_pointer)
	def getFileName(self, index):
		return IFileList_getFileName(self.c_pointer, index)
	def getFullFileName(self, index):
		return IFileList_getFullFileName(self.c_pointer, index)
	def getFileSize(self, index):
		return IFileList_getFileSize(self.c_pointer, index)
	def getID(self, index):
		return IFileList_getID(self.c_pointer, index)
	def isDirectory(self, index):
		return IFileList_isDirectory(self.c_pointer, index)
	def findFile(self, filename, isFolder = False):
		return IFileList_findFile(self.c_pointer, filename, isFolder)
	def getPath(self):
		return IFileList_getPath(self.c_pointer)
	if IRRLICHT_VERSION < 180:
		def addItem(self, fullPath, size, isDirectory, id = 0):
			return IFileList_addItem(self.c_pointer, fullPath, size, isDirectory, id)
	else:
		def addItem(self, fullPath, offset, size, isDirectory, id = 0):
			return IFileList_addItem(self.c_pointer, fullPath, offset, size, isDirectory, id)
	def sort(self):
		IFileList_sort(self.c_pointer)

class IFileArchive(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def createAndOpenFile1(self, filename):
		return IReadFile(IFileArchive_createAndOpenFile1(self.c_pointer, filename))
	def createAndOpenFile2(self, index):
		return IReadFile(IFileArchive_createAndOpenFile2(self.c_pointer, index))
	def createAndOpenFile(self, filename_or_index):
		if isinstance(filename_or_index, type_str):
			return self.createAndOpenFile1(filename_or_index)
		elif isinstance(filename_or_index, int):
			return self.createAndOpenFile2(filename_or_index)
		else:
			print('ERROR in IFileArchive::createAndOpenFile, unsupported argument type', filename_or_index)
			return None
	def getFileList(self):
		return IFileList(IFileArchive_getFileList(self.c_pointer))
	def getType(self):
		return IFileArchive_getType(self.c_pointer)
	def get_Password(self):
		return IFileArchive_get_Password(self.c_pointer)
	def set_Password(self, value):
		IFileArchive_set_Password(self.c_pointer, value)
	Password = property(get_Password, set_Password)

class IArchiveLoader(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def isALoadableFileFormat1(self, filename):
		return IArchiveLoader_isALoadableFileFormat1(self.c_pointer, filename)
	def isALoadableFileFormat2(self, file):
		return IArchiveLoader_isALoadableFileFormat2(self.c_pointer, file.c_pointer)
	def isALoadableFileFormat3(self, fileType):
		return IArchiveLoader_isALoadableFileFormat3(self.c_pointer, fileType)
	def isALoadableFileFormat(self, name_or_file_or_type):
		if isinstance(name_or_file_or_type, type_str):
			return self.isALoadableFileFormat1(name_or_file_or_type)
		elif isinstance(name_or_file_or_type, IReadFile):
			return self.isALoadableFileFormat2(name_or_file_or_type)
		elif isinstance(name_or_file_or_type, int):
			return self.isALoadableFileFormat3(name_or_file_or_type)
		else:
			print('ERROR in IArchiveLoader::isALoadableFileFormat, unsupported argument type', name_or_file_or_type)
			return False
	def createArchive1(self, filename, ignoreCase, ignorePaths):
		return IFileArchive(IArchiveLoader_createArchive1(self.c_pointer, filename, ignoreCase, ignorePaths))
	def createArchive2(self, file, ignoreCase, ignorePaths):
		return IFileArchive(IArchiveLoader_createArchive2(self.c_pointer, file.c_pointer, ignoreCase, ignorePaths))
	def createArchive(self, name_or_file, ignoreCase, ignorePaths):
		if isinstance(name_or_file, type_str):
			return self.createArchive1(name_or_file, ignoreCase, ignorePaths)
		elif isinstance(name_or_file, IFileArchive):
			return self.createArchive2(name_or_file, ignoreCase, ignorePaths)
		else:
			print('ERROR in IArchiveLoader::createArchive, unsupported argument type', name_or_file)
			return None

class SMD3AnimationInfo(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3AnimationInfo_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3AnimationInfo_ctor()
	def get_first(self):
		return SMD3AnimationInfo_get_first(self.c_pointer)
	def set_first(self, value):
		SMD3AnimationInfo_set_first(self.c_pointer, value)
	first = property(get_first, set_first)
	def get_num(self):
		return SMD3AnimationInfo_get_num(self.c_pointer)
	def set_num(self, value):
		SMD3AnimationInfo_set_num(self.c_pointer, value)
	num = property(get_num, set_num)
	def get_looping(self):
		return SMD3AnimationInfo_get_looping(self.c_pointer)
	def set_looping(self, value):
		SMD3AnimationInfo_set_looping(self.c_pointer, value)
	looping = property(get_looping, set_looping)
	def get_fps(self):
		return SMD3AnimationInfo_get_fps(self.c_pointer)
	def set_fps(self, value):
		SMD3AnimationInfo_set_fps(self.c_pointer, value)
	fps = property(get_fps, set_fps)

class SMD3Header(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3Header_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3Header_ctor()
	def get_headerID(self):
		return SMD3Header_get_headerID(self.c_pointer)
	def set_headerID(self, value):
		SMD3Header_set_headerID(self.c_pointer, value)
	headerID = property(get_headerID, set_headerID)
	def get_Version(self):
		return SMD3Header_get_Version(self.c_pointer)
	def set_Version(self, value):
		SMD3Header_set_Version(self.c_pointer, value)
	Version = property(get_Version, set_Version)
	def get_fileName(self):
		return SMD3Header_get_fileName(self.c_pointer)
	def set_fileName(self, value):
		SMD3Header_set_fileName(self.c_pointer, value)
	fileName = property(get_fileName, set_fileName)
	def get_numFrames(self):
		return SMD3Header_get_numFrames(self.c_pointer)
	def set_numFrames(self, value):
		SMD3Header_set_numFrames(self.c_pointer, value)
	numFrames = property(get_numFrames, set_numFrames)
	def get_numTags(self):
		return SMD3Header_get_numTags(self.c_pointer)
	def set_numTags(self, value):
		SMD3Header_set_numTags(self.c_pointer, value)
	numTags = property(get_numTags, set_numTags)
	def get_numMeshes(self):
		return SMD3Header_get_numMeshes(self.c_pointer)
	def set_numMeshes(self, value):
		SMD3Header_set_numMeshes(self.c_pointer, value)
	numMeshes = property(get_numMeshes, set_numMeshes)
	def get_numMaxSkins(self):
		return SMD3Header_get_numMaxSkins(self.c_pointer)
	def set_numMaxSkins(self, value):
		SMD3Header_set_numMaxSkins(self.c_pointer, value)
	numMaxSkins = property(get_numMaxSkins, set_numMaxSkins)
	def get_frameStart(self):
		return SMD3Header_get_frameStart(self.c_pointer)
	def set_frameStart(self, value):
		SMD3Header_set_frameStart(self.c_pointer, value)
	frameStart = property(get_frameStart, set_frameStart)
	def get_tagStart(self):
		return SMD3Header_get_tagStart(self.c_pointer)
	def set_tagStart(self, value):
		SMD3Header_set_tagStart(self.c_pointer, value)
	tagStart = property(get_tagStart, set_tagStart)
	def get_tagEnd(self):
		return SMD3Header_get_tagEnd(self.c_pointer)
	def set_tagEnd(self, value):
		SMD3Header_set_tagEnd(self.c_pointer, value)
	tagEnd = property(get_tagEnd, set_tagEnd)
	def get_fileSize(self):
		return SMD3Header_get_fileSize(self.c_pointer)
	def set_fileSize(self, value):
		SMD3Header_set_fileSize(self.c_pointer, value)
	fileSize = property(get_fileSize, set_fileSize)

class SMD3MeshHeader(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3MeshHeader_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3MeshHeader_ctor()
	def get_meshID(self):
		return SMD3MeshHeader_get_meshID(self.c_pointer)
	def set_meshID(self, value):
		SMD3MeshHeader_set_meshID(self.c_pointer, value)
	meshID = property(get_meshID, set_meshID)
	def get_meshName(self):
		return SMD3MeshHeader_get_meshName(self.c_pointer)
	def set_meshName(self, value):
		SMD3MeshHeader_set_meshName(self.c_pointer, value)
	meshName = property(get_meshName, set_meshName)
	def get_numFrames(self):
		return SMD3MeshHeader_get_numFrames(self.c_pointer)
	def set_numFrames(self, value):
		SMD3MeshHeader_set_numFrames(self.c_pointer, value)
	numFrames = property(get_numFrames, set_numFrames)
	def get_numShader(self):
		return SMD3MeshHeader_get_numShader(self.c_pointer)
	def set_numShader(self, value):
		SMD3MeshHeader_set_numShader(self.c_pointer, value)
	numShader = property(get_numShader, set_numShader)
	def get_numVertices(self):
		return SMD3MeshHeader_get_numVertices(self.c_pointer)
	def set_numVertices(self, value):
		SMD3MeshHeader_set_numVertices(self.c_pointer, value)
	numVertices = property(get_numVertices, set_numVertices)
	def get_numTriangles(self):
		return SMD3MeshHeader_get_numTriangles(self.c_pointer)
	def set_numTriangles(self, value):
		SMD3MeshHeader_set_numTriangles(self.c_pointer, value)
	numTriangles = property(get_numTriangles, set_numTriangles)
	def get_offset_triangles(self):
		return SMD3MeshHeader_get_offset_triangles(self.c_pointer)
	def set_offset_triangles(self, value):
		SMD3MeshHeader_set_offset_triangles(self.c_pointer, value)
	offset_triangles = property(get_offset_triangles, set_offset_triangles)
	def get_offset_shaders(self):
		return SMD3MeshHeader_get_offset_shaders(self.c_pointer)
	def set_offset_shaders(self, value):
		SMD3MeshHeader_set_offset_shaders(self.c_pointer, value)
	offset_shaders = property(get_offset_shaders, set_offset_shaders)
	def get_offset_st(self):
		return SMD3MeshHeader_get_offset_st(self.c_pointer)
	def set_offset_st(self, value):
		SMD3MeshHeader_set_offset_st(self.c_pointer, value)
	offset_st = property(get_offset_st, set_offset_st)
	def get_vertexStart(self):
		return SMD3MeshHeader_get_vertexStart(self.c_pointer)
	def set_vertexStart(self, value):
		SMD3MeshHeader_set_vertexStart(self.c_pointer, value)
	vertexStart = property(get_vertexStart, set_vertexStart)
	def get_offset_end(self):
		return SMD3MeshHeader_get_offset_end(self.c_pointer)
	def set_offset_end(self, value):
		SMD3MeshHeader_set_offset_end(self.c_pointer, value)
	offset_end = property(get_offset_end, set_offset_end)

class SMD3Vertex(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3Vertex_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3Vertex_ctor()
	def get_position(self):
		return SMD3Vertex_get_position(self.c_pointer)
	def set_position(self, value):
		SMD3Vertex_set_position(self.c_pointer, value)
	position = property(get_position, set_position)
	def get_normal(self):
		return SMD3Vertex_get_normal(self.c_pointer)
	def set_normal(self, value):
		SMD3Vertex_set_normal(self.c_pointer, value)
	normal = property(get_normal, set_normal)

class SMD3TexCoord(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3TexCoord_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3TexCoord_ctor()
	def get_u(self):
		return SMD3TexCoord_get_u(self.c_pointer)
	def set_u(self, value):
		SMD3TexCoord_set_u(self.c_pointer, value)
	u = property(get_u, set_u)
	def get_v(self):
		return SMD3TexCoord_get_v(self.c_pointer)
	def set_v(self, value):
		SMD3TexCoord_set_v(self.c_pointer, value)
	v = property(get_v, set_v)

class SMD3Face(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3Face_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3Face_ctor()
	def get_Index(self):
		return SMD3Face_get_Index(self.c_pointer)
	def set_Index(self, value):
		SMD3Face_set_Index(self.c_pointer, value)
	Index = property(get_Index, set_Index)

class SMD3MeshBuffer(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor()
			self.delete_c_pointer = True
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3MeshBuffer_delete(self.c_pointer)
			except:
				pass
	def ctor(self):
		return SMD3MeshBuffer_ctor()
	def get_MeshHeader(self):
		return SMD3MeshBuffer_get_MeshHeader(self.c_pointer)
	def set_MeshHeader(self, value):
		SMD3MeshBuffer_set_MeshHeader(self.c_pointer, value)
	MeshHeader = property(get_MeshHeader, set_MeshHeader)
	def get_Shader(self):
		return SMD3MeshBuffer_get_Shader(self.c_pointer)
	def set_Shader(self, value):
		SMD3MeshBuffer_set_Shader(self.c_pointer, value)
	Shader = property(get_Shader, set_Shader)
	def get_Indices(self):
		return array(_type_ = int, c_pointer = SMD3MeshBuffer_get_Indices(self.c_pointer))
	def set_Indices(self, value):
		SMD3MeshBuffer_set_Indices(self.c_pointer, value.c_pointer)
	Indices = property(get_Indices, set_Indices)
	def get_Vertices(self):
		return array(_type_ = SMD3Vertex, c_pointer = SMD3MeshBuffer_get_Vertices(self.c_pointer))
	def set_Vertices(self, value):
		SMD3MeshBuffer_set_Vertices(self.c_pointer, value.c_pointer)
	Vertices = property(get_Vertices, set_Vertices)
	def get_Tex(self):
		return array(_type_ = SMD3TexCoord, c_pointer = SMD3MeshBuffer_get_Tex(self.c_pointer))
	def set_Tex(self, value):
		SMD3MeshBuffer_set_Tex(self.c_pointer, value.c_pointer)
	Tex = property(get_Tex, set_Tex)

class SMD3QuaternionTag(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 1:
			if isinstance(args[0], SMD3QuaternionTag):
				self.c_pointer = self.ctor4(*args)
			else:
				self.c_pointer = self.ctor1(*args)
		elif len(args) > 1:
			if isinstance(args[0], vector3df):
				self.c_pointer = self.ctor3(*args)
			else:
				self.c_pointer = self.ctor2(*args)
		elif 'other' in kwargs:
			self.c_pointer = self.ctor4(kwargs.pop('other', None))
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3QuaternionTag_delete(self.c_pointer)
			except:
				pass
	def ctor1(self, name):
		return SMD3QuaternionTag_ctor1(name)
	def ctor2(self, name, m):
		return SMD3QuaternionTag_ctor2(name, m.c_pointer)
	def ctor3(self, pos, angle):
		return SMD3QuaternionTag_ctor3(pos.c_pointer, angle.c_pointer)
	def ctor4(self, copyMe):
		return SMD3QuaternionTag_ctor4(copyMe.c_pointer)
	def setto(self, m):
		SMD3QuaternionTag_setto(self.c_pointer, m.c_pointer)
	def operator_eq(self, other):
		return SMD3QuaternionTag_operator_eq(self.c_pointer, other.c_pointer)
	def operator_set(self, copyMe):
		return SMD3QuaternionTag_operator_set(self.c_pointer, copyMe.c_pointer)
	def get_Name(self):
		return SMD3QuaternionTag_get_Name(self.c_pointer)
	def set_Name(self, value):
		SMD3QuaternionTag_set_Name(self.c_pointer, value)
	Name = property(get_Name, set_Name)
	def get_position(self):
		return vector3df(SMD3QuaternionTag_get_position(self.c_pointer))
	def set_position(self, value):
		SMD3QuaternionTag_set_position(self.c_pointer, value.c_pointer)
	position = property(get_position, set_position)
	def get_rotation(self):
		return quaternion(SMD3QuaternionTag_get_rotation(self.c_pointer))
	def set_rotation(self, value):
		SMD3QuaternionTag_set_rotation(self.c_pointer, value.c_pointer)
	rotation = property(get_rotation, set_rotation)

class SMD3QuaternionTagList:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = self.ctor1()
		elif 'other' in kwargs:
			self.c_pointer = self.ctor2(kwargs.pop('other', None))
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __len__(self):
		return self.size()
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3QuaternionTagList_delete(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self.size()
	def __getitem__(self, key):
		return self.const_operator_index(key)
	def __setitem__(self, key, value):
		self.set_tag_item(key, value)
	def ctor1(self):
		return SMD3QuaternionTagList_ctor1()
	def ctor2(self, copyMe):
		return SMD3QuaternionTagList_ctor2(copyMe.c_pointer)
	def get(self, name):
		return SMD3QuaternionTag(c_pointer = SMD3QuaternionTagList_get(self.c_pointer, name))
	def size(self):
		return SMD3QuaternionTagList_size(self.c_pointer)
	def set_used(self, new_size):
		SMD3QuaternionTagList_set_used(self.c_pointer, new_size)
	def const_operator_index(self, index):
		return SMD3QuaternionTag(c_pointer = SMD3QuaternionTagList_const_operator_index(self.c_pointer, index))
	def operator_index(self, index):
		return SMD3QuaternionTag(c_pointer = SMD3QuaternionTagList_operator_index(self.c_pointer, index))
	def push_back(self, other):
		SMD3QuaternionTagList_push_back(self.c_pointer, other.c_pointer)
	def operator_set(self, copyMe):
		return SMD3QuaternionTagList(c_pointer = SMD3QuaternionTagList_operator_set(self.c_pointer, copyMe.c_pointer))
	def set_tag_item(self, index, item):
		SMD3QuaternionTagList_set_tag_item(self.c_pointer, index, item.c_pointer)

class SMD3Mesh(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.delete_c_pointer = False
		if len(args) > 0:
			self.c_pointer = args[0]
		else:
			self.c_pointer = SMD3Mesh_ctor()
			self.delete_c_pointer = True
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				SMD3Mesh_delete(self.c_pointer)
			except:
				pass
	def get_Name(self):
		return SMD3Mesh_get_Name(self.c_pointer)
	def set_Name(self, value):
		SMD3Mesh_set_Name(self.c_pointer, value)
	Name = property(get_Name, set_Name)
	def get_Buffer(self):
		return array(_type_ = SMD3MeshBuffer, c_pointer = SMD3Mesh_get_Buffer(self.c_pointer))
	def set_Buffer(self, value):
		SMD3Mesh_set_Buffer(self.c_pointer, value.c_pointer)
	Buffer = property(get_Buffer, set_Buffer)
	def get_TagList(self):
		return SMD3QuaternionTagList(c_pointer = SMD3Mesh_get_TagList(self.c_pointer))
	def set_TagList(self, value):
		SMD3Mesh_set_TagList(self.c_pointer, value.c_pointer)
	TagList = property(get_TagList, set_TagList)
	def get_MD3Header(self):
		return SMD3Header(c_pointer = SMD3Mesh_get_MD3Header(self.c_pointer))
	def set_MD3Header(self, value):
		SMD3Mesh_set_MD3Header(self.c_pointer, value.c_pointer)
	MD3Header = property(get_MD3Header, set_MD3Header)

class IMeshBuffer(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getMaterial(self):
		return SMaterial(IMeshBuffer_getMaterial(self.c_pointer))
	def getVertexType(self):
		return IMeshBuffer_getVertexType(self.c_pointer)
	def getVertices(self):
		return IMeshBuffer_getVertices(self.c_pointer)
	def getVertexCount(self):
		return IMeshBuffer_getVertexCount(self.c_pointer)
	def getIndexType(self):
		return IMeshBuffer_getIndexType(self.c_pointer)
	def getIndices(self):
		return IMeshBuffer_getIndices(self.c_pointer)
	def getIndexCount(self):
		return IMeshBuffer_getIndexCount(self.c_pointer)
	def getBoundingBox(self):
		return aabbox3df(IMeshBuffer_getBoundingBox(self.c_pointer))
	def setBoundingBox(self, box):
		IMeshBuffer_setBoundingBox(self.c_pointer, box.c_pointer)
	def recalculateBoundingBox(self):
		IMeshBuffer_recalculateBoundingBox(self.c_pointer)
	def getPosition(self, i):
		return vector3df(IMeshBuffer_getPosition(self.c_pointer, i))
	def getNormal(self, i):
		return vector3df(IMeshBuffer_getNormal(self.c_pointer, i))
	def getTCoords(self, i):
		return vector2df(IMeshBuffer_getTCoords(self.c_pointer, i))
	def append(self, *args):
		if isinstance(args[0], IMeshBuffer):
			IMeshBuffer_append2(self.c_pointer, args[0].c_pointer)
		else:
			IMeshBuffer_append1(self.c_pointer, *args)
	def append1(self, vertices, numVertices, indices, numIndices):
		IMeshBuffer_append1(self.c_pointer, vertices, numVertices, indices, numIndices)
	def append2(self, other):
		IMeshBuffer_append2(self.c_pointer, other.c_pointer)
	def getHardwareMappingHint_Vertex(self):
		return IMeshBuffer_getHardwareMappingHint_Vertex(self.c_pointer)
	def getHardwareMappingHint_Index(self):
		return IMeshBuffer_getHardwareMappingHint_Index(self.c_pointer)
	def setHardwareMappingHint(self, newMappingHint, buffer = EBT_VERTEX_AND_INDEX):
		IMeshBuffer_setHardwareMappingHint(self.c_pointer, newMappingHint, buffer)
	def setDirty(self, buffer = EBT_VERTEX_AND_INDEX):
		IMeshBuffer_setDirty(self.c_pointer, buffer)
	def getChangedID_Vertex(self):
		return IMeshBuffer_getChangedID_Vertex(self.c_pointer)
	def getChangedID_Index(self):
		return IMeshBuffer_getChangedID_Index(self.c_pointer)

class IDynamicMeshBuffer(IMeshBuffer):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getVertexBuffer(self):
		return IDynamicMeshBuffer_getVertexBuffer(self.c_pointer)
	def getIndexBuffer(self):
		return IDynamicMeshBuffer_getIndexBuffer(self.c_pointer)
	def setVertexBuffer(self, vertexBuffer):
		IDynamicMeshBuffer_setVertexBuffer(self.c_pointer, vertexBuffer.c_pointer)
	def setIndexBuffer(self, indexBuffer):
		IDynamicMeshBuffer_setIndexBuffer(self.c_pointer, indexBuffer.c_pointer)
	def getMaterial1(self):
		return SMaterial(IDynamicMeshBuffer_getMaterial1(self.c_pointer))
	def getMaterial2(self):
		return SMaterial(IDynamicMeshBuffer_getMaterial2(self.c_pointer))
	def getMaterial(self):
		return self.getMaterial1()
	def getBoundingBox(self):
		return aabbox3df(IDynamicMeshBuffer_getBoundingBox(self.c_pointer))
	def setBoundingBox(self, box):
		IDynamicMeshBuffer_setBoundingBox(self.c_pointer, box.c_pointer)
	def recalculateBoundingBox(self):
		IDynamicMeshBuffer_recalculateBoundingBox(self.c_pointer)
	def append1(self, vertices, numVertices, indices, numIndices):
		IDynamicMeshBuffer_append1(self.c_pointer, vertices, numVertices, indices, numIndices)
	def append2(self, other):
		IDynamicMeshBuffer_append2(self.c_pointer, other.c_pointer)
	def getHardwareMappingHint_Vertex(self):
		return IDynamicMeshBuffer_getHardwareMappingHint_Vertex(self.c_pointer)
	def getHardwareMappingHint_Index(self):
		return IDynamicMeshBuffer_getHardwareMappingHint_Index(self.c_pointer)
	def setHardwareMappingHint(self, NewMappingHint, Buffer = EBT_VERTEX_AND_INDEX):
		IDynamicMeshBuffer_setHardwareMappingHint(self.c_pointer, NewMappingHint, Buffer)
	def setDirty(self, Buffer = EBT_VERTEX_AND_INDEX):
		IDynamicMeshBuffer_setDirty(self.c_pointer, Buffer)
	def getChangedID_Vertex(self):
		return IDynamicMeshBuffer_getChangedID_Vertex(self.c_pointer)
	def getChangedID_Index(self):
		return IDynamicMeshBuffer_getChangedID_Index(self.c_pointer)
	def getVertexType(self):
		return IDynamicMeshBuffer_getVertexType(self.c_pointer)
	def getVertices1(self):
		return IDynamicMeshBuffer_getVertices1(self.c_pointer)
	def getVertices2(self):
		return IDynamicMeshBuffer_getVertices2(self.c_pointer)
	def getVertexCount(self):
		return IDynamicMeshBuffer_getVertexCount(self.c_pointer)
	def getIndexType(self):
		return IDynamicMeshBuffer_getIndexType(self.c_pointer)
	def getIndices1(self):
		return IDynamicMeshBuffer_getIndices1(self.c_pointer)
	def getIndices2(self):
		return IDynamicMeshBuffer_getIndices2(self.c_pointer)
	def getIndexCount(self):
		return IDynamicMeshBuffer_getIndexCount(self.c_pointer)
	def getPosition1(self, i):
		return vector3df(IDynamicMeshBuffer_getPosition1(self.c_pointer, i))
	def getPosition2(self, i):
		return vector3df(IDynamicMeshBuffer_getPosition2(self.c_pointer, i))
	def getPosition(self, i):
		return self.getPosition1(i)
	def getTCoords1(self, i):
		return vector2df(IDynamicMeshBuffer_getTCoords1(self.c_pointer, i))
	def getTCoords2(self, i):
		return vector2df(IDynamicMeshBuffer_getTCoords2(self.c_pointer, i))
	def getTCoords(self, i):
		return self.getTCoords1(i)
	def getNormal1(self, i):
		return vector3df(IDynamicMeshBuffer_getNormal1(self.c_pointer, i))
	def getNormal2(self, i):
		return vector3df(IDynamicMeshBuffer_getNormal2(self.c_pointer, i))
	def getNormal(self, i):
		return self.getNormal1(i)

class CDynamicMeshBuffer(IDynamicMeshBuffer):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0:
			self.c_pointer = args[0]
			self.delete_c_pointer = False
		else:
			self.c_pointer = self.ctor(*args)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				CDynamicMeshBuffer_delete(self.c_pointer)
			except:
				pass
	def ctor(self, vertexType, indexType):
		return CDynamicMeshBuffer_ctor(self.c_pointer, vertexType, indexType)
	def getVertexBuffer(self):
		return CDynamicMeshBuffer_getVertexBuffer(self.c_pointer)
	def getIndexBuffer(self):
		return CDynamicMeshBuffer_getIndexBuffer(self.c_pointer)
	def setVertexBuffer(self, newVertexBuffer):
		CDynamicMeshBuffer_setVertexBuffer(self.c_pointer, newVertexBuffer.c_pointer)
	def setIndexBuffer(self, newIndexBuffer):
		CDynamicMeshBuffer_setIndexBuffer(self.c_pointer, newIndexBuffer.c_pointer)
	def getMaterial1(self):
		return SMaterial(CDynamicMeshBuffer_getMaterial1(self.c_pointer))
	def getMaterial2(self):
		return SMaterial(CDynamicMeshBuffer_getMaterial2(self.c_pointer))
	def getMaterial(self):
		return self.getMaterial1()
	def setMaterial(self, value):
		CDynamicMeshBuffer_setMaterial(self.c_pointer, value.c_pointer)
	def getBoundingBox(self):
		return aabbox3df(CDynamicMeshBuffer_getBoundingBox(self.c_pointer))
	def setBoundingBox(self, box):
		CDynamicMeshBuffer_setBoundingBox(self.c_pointer, box.c_pointer)
	def recalculateBoundingBox(self):
		CDynamicMeshBuffer_recalculateBoundingBox(self.c_pointer)

class IMesh(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getMeshBufferCount(self):
		return IMesh_getMeshBufferCount(self.c_pointer)
	def getMeshBuffer(self, value):
		if isinstance(value, SMaterial):
			return IMeshBuffer(IMesh_getMeshBuffer2(self.c_pointer, value.c_pointer))
		else:
			return IMeshBuffer(IMesh_getMeshBuffer(self.c_pointer, value))
	def getMeshBuffer1(self, nr):
		return IMeshBuffer(IMesh_getMeshBuffer(self.c_pointer, nr))
	def getMeshBuffer2(self, material):
		return IMeshBuffer(IMesh_getMeshBuffer2(self.c_pointer, material.c_pointer))
	def getBoundingBox(self):
		return aabbox3df(IMesh_getBoundingBox(self.c_pointer))
	def setBoundingBox(self, box):
		IMesh_setBoundingBox(self.c_pointer, box.c_pointer)
	def setMaterialFlag(self, flag, newvalue):
		IMesh_setMaterialFlag(self.c_pointer, flag, newvalue)
	def setHardwareMappingHint(self, newMappingHint, buffer = EBT_VERTEX_AND_INDEX):
		IMesh_setHardwareMappingHint(self.c_pointer, newMappingHint, buffer)
	def setDirty(self, buffer = EBT_VERTEX_AND_INDEX):
		IMesh_setDirty(self.c_pointer, buffer)

class SMesh(IMesh):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SMesh_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = SMesh_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				 SMesh_delete(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SMesh(c_pointer = SMesh_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SMesh_set_item(self.c_pointer, item.c_pointer, index)
	def getMeshBufferCount(self):
		return SMesh_getMeshBufferCount(self.c_pointer)
	def getMeshBuffer1(self, nr):
		return IMeshBuffer(SMesh_getMeshBuffer1(self.c_pointer, nr))
	def getMeshBuffer2(self, material):
		return IMeshBuffer(SMesh_getMeshBuffer2(self.c_pointer, material.c_pointer))
	def getMeshBuffer(self, arg):
		if isinstance(arg, SMaterial):
			return self.getMeshBuffer2(arg)
		else:
			return self.getMeshBuffer1(arg)
	def getBoundingBox(self):
		return aabbox3df(SMesh_getBoundingBox(self.c_pointer))
	def setBoundingBox(self, box):
		SMesh_setBoundingBox(self.c_pointer, box.c_pointer)
	BoundingBox = property(getBoundingBox, setBoundingBox)
	def recalculateBoundingBox(self):
		SMesh_recalculateBoundingBox(self.c_pointer)
	def addMeshBuffer(self, buf):
		SMesh_addMeshBuffer(self.c_pointer, buf.c_pointer)
	def setMaterialFlag(self, flag, newvalue):
		SMesh_setMaterialFlag(self.c_pointer, flag, newvalue)
	def setHardwareMappingHint(self, newMappingHint, buffer_type = EBT_VERTEX_AND_INDEX):
		SMesh_setHardwareMappingHint(self.c_pointer, newMappingHint, buffer_type)
	def setDirty(self, buffer_type = EBT_VERTEX_AND_INDEX):
		SMesh_setDirty(self.c_pointer, buffer_type)
	def get_MeshBuffers(self):
		return array(_type_ = IMeshBuffer, c_pointer = SMesh_get_MeshBuffers(self.c_pointer))
	def set_MeshBuffers(self, value):
		SMesh_set_MeshBuffers(self.c_pointer, value.c_pointer)
	MeshBuffers = property(get_MeshBuffers, set_MeshBuffers)

class IAnimatedMesh(IMesh):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getFrameCount(self):
		return IAnimatedMesh_getFrameCount(self.c_pointer)
	def getMesh(self, frame, detailLevel=255, startFrameLoop=-1, endFrameLoop=-1):
		return IMesh(IAnimatedMesh_getMesh(self.c_pointer, frame, detailLevel, startFrameLoop, endFrameLoop))
	def getMeshType(self):
		return IAnimatedMesh_getMeshType(self.c_pointer)

class IAnimatedMeshMD2(IAnimatedMesh):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
	def getFrameLoop1(self, l, outBegin, outEnd, outFPS):
		IAnimatedMeshMD2_getFrameLoop1(self.c_pointer, l, ctypes.byref(outBegin), ctypes.byref(outEnd), ctypes.byref(outFPS))
	def getFrameLoop2(self, name, outBegin, outEnd, outFPS):
		return IAnimatedMeshMD2_getFrameLoop2(self.c_pointer, name, ctypes.byref(outBegin), ctypes.byref(outEnd), ctypes.byref(outFPS))
	def getFrameLoop(self, arg, outBegin, outEnd, outFPS):
		if isinstance(arg, int):
			self.getFrameLoop1(arg, outBegin, outEnd, outFPS)
		else:
			return self.getFrameLoop2(arg, outBegin, outEnd, outFPS)
	def get_frame_loop(self, arg):
		outBegin, outEnd, outFPS = ctypes.c_int(), ctypes.c_int(), ctypes.c_int()
		if isinstance(arg, int):
			self.getFrameLoop1(arg, outBegin, outEnd, outFPS)
			return (None, outBegin.value, outEnd.value, outFPS.value)
		else:
			result = self.getFrameLoop2(arg, outBegin, outEnd, outFPS)
			return (result, outBegin.value, outEnd.value, outFPS.value)
	def getAnimationCount(self):
		return IAnimatedMeshMD2_getAnimationCount(self.c_pointer)
	def getAnimationName(self, nr):
		return IAnimatedMeshMD2_getAnimationName(self.c_pointer, nr)

class IAnimatedMeshMD3(IAnimatedMesh):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setInterpolationShift(self, shift, loopMode):
		IAnimatedMeshMD3_setInterpolationShift(self.c_pointer, shift, loopMode)
	def getTagList(self, frame, detailLevel, startFrameLoop, endFrameLoop):
		return SMD3QuaternionTagList(c_pointer = IAnimatedMeshMD3_getTagList(self.c_pointer, frame, detailLevel, startFrameLoop, endFrameLoop))
	def getOriginalMesh(self):
		return SMD3Mesh(IAnimatedMeshMD3_getOriginalMesh(self.c_pointer))

class IMeshCache(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def addMesh(self, name, mesh):
		IMeshCache_addMesh(self.c_pointer, name, mesh)
	def removeMesh1(self, mesh):
		IMeshCache_removeMesh1(self.c_pointer, mesh)
	def removeMesh2(self, mesh):
		IMeshCache_removeMesh2(self.c_pointer, mesh)
	def getMeshCount(self):
		return IMeshCache_getMeshCount(self.c_pointer)
	def getMeshIndex1(self, mesh):
		return IMeshCache_getMeshIndex1(self.c_pointer, mesh)
	def getMeshIndex2(self, mesh):
		return IMeshCache_getMeshIndex2(self.c_pointer, mesh)
	def getMeshByIndex(self, index):
		return IMeshCache_getMeshByIndex(self.c_pointer, index)
	def getMeshByName(self, name):
		return IMeshCache_getMeshByName(self.c_pointer, name)
	def getMeshNameByIndex(self, index):
		return IMeshCache_getMeshNameByIndex(self.c_pointer, index)
	def getMeshName1(self, mesh):
		return IMeshCache_getMeshName1(self.c_pointer, mesh)
	def getMeshName2(self, mesh):
		return IMeshCache_getMeshName2(self.c_pointer, mesh)
	def renameMeshByIndex(self, index, name):
		return IMeshCache_renameMeshByIndex(self.c_pointer, index, name)
	def renameMesh1(self, mesh, name):
		return IMeshCache_renameMesh1(self.c_pointer, mesh, name)
	def renameMesh2(self, mesh, name):
		return IMeshCache_renameMesh2(self.c_pointer, mesh, name)
	def isMeshLoaded(self, name):
		return IMeshCache_isMeshLoaded(self.c_pointer, name)
	def clear(self):
		IMeshCache_clear(self.c_pointer)
	def clearUnusedMeshes(self):
		IMeshCache_clearUnusedMeshes(self.c_pointer)

class IMeshManipulator(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def flipSurfaces(self, mesh):
		IMeshManipulator_flipSurfaces(self.c_pointer, mesh.c_pointer)
	def setVertexColorAlpha(self, mesh, alpha):
		IMeshManipulator_setVertexColorAlpha(self.c_pointer, mesh.c_pointer, alpha)
	def setVertexColors(self, mesh, color):
		IMeshManipulator_setVertexColors(self.c_pointer, mesh.c_pointer, color.c_pointer)
	def recalculateNormals1(self, mesh, smooth = False, angleWeighted = False):
		IMeshManipulator_recalculateNormals1(self.c_pointer, mesh.c_pointer, smooth, angleWeighted)
	def recalculateNormals2(self, buffer, smooth = False, angleWeighted = False):
		IMeshManipulator_recalculateNormals2(self.c_pointer, buffer.c_pointer, smooth, angleWeighted)
	def recalculateNormals(self, mesh_or_buffer, smooth = False, angleWeighted = False):
		if isinstance(mesh_or_buffer, IMeshBuffer):
			self.recalculateNormals2(mesh_or_buffer, smooth, angleWeighted)
		else:
			self.recalculateNormals1(mesh_or_buffer, smooth, angleWeighted)
	def recalculateTangents(self, mesh, recalculateNormals = False, smooth = False, angleWeighted = False):
		IMeshManipulator_recalculateTangents(self.c_pointer, mesh.c_pointer, recalculateNormals, smooth, angleWeighted)
	def scale1(self, mesh, factor):
		IMeshManipulator_scale1(self.c_pointer, mesh.c_pointer, factor.c_pointer)
	def scale2(self, buffer, factor):
		IMeshManipulator_scale2(self.c_pointer, buffer.c_pointer, factor.c_pointer)
	def scale(self, mesh_or_buffer, factor):
		if isinstance(mesh_or_buffer, IMeshBuffer):
			self.scale2(mesh_or_buffer, factor)
		else:
			self.scale1(mesh_or_buffer, factor)
	if IRRLICHT_VERSION < 180:
		def scaleMesh(self, mesh, factor):
			IMeshManipulator_scaleMesh(self.c_pointer, mesh.c_pointer, factor.c_pointer)
		def transformMesh(self, mesh, m):
			IMeshManipulator_transformMesh(self.c_pointer, mesh.c_pointer, m.c_pointer)
	def scaleTCoords1(self, mesh, factor, level = 1):
		IMeshManipulator_scaleTCoords1(self.c_pointer, mesh.c_pointer, factor.c_pointer, level)
	def scaleTCoords2(self, buffer, factor, level = 1):
		IMeshManipulator_scaleTCoords2(self.c_pointer, buffer.c_pointer, factor.c_pointer, level)
	def scaleTCoords(self, mesh_or_buffer, factor, level = 1):
		if isinstance(mesh_or_buffer, IMeshBuffer):
			self.scaleTCoords2(mesh_or_buffer, factor, level)
		else:
			self.scaleTCoords1(mesh_or_buffer, factor, level)
	def transform1(self, mesh, m):
		IMeshManipulator_transform1(self.c_pointer, mesh.c_pointer, m.c_pointer)
	def transform2(self, buffer, m):
		IMeshManipulator_transform2(self.c_pointer, buffer.c_pointer, m.c_pointer)
	def transform(self, mesh_or_buffer, m):
		if isinstance(mesh_or_buffer, IMeshBuffer):
			self.transform2(mesh_or_buffer, m)
		else:
			self.transform1(mesh_or_buffer, m)
	def createMeshCopy(self, mesh):
		return SMesh(IMeshManipulator_createMeshCopy(self.c_pointer, mesh.c_pointer))
	def makePlanarTextureMapping1(self, mesh, resolution = 0.001):
		IMeshManipulator_makePlanarTextureMapping1(self.c_pointer, mesh.c_pointer, resolution)
	def makePlanarTextureMapping2(self, meshbuffer, resolution = 0.001):
		IMeshManipulator_makePlanarTextureMapping2(self.c_pointer, meshbuffer.c_pointer, resolution)
	def makePlanarTextureMapping3(self, buffer, resolutionS, resolutionT, axis, offset):
		IMeshManipulator_makePlanarTextureMapping3(self.c_pointer, buffer.c_pointer, resolutionS, resolutionT, axis, offset.c_pointer)
	def makePlanarTextureMapping(self, *args):
		if len(args) > 2:
			self.makePlanarTextureMapping3(*args)
		elif isinstance(args[0], IMeshBuffer):
			self.makePlanarTextureMapping2(*args)
		else:
			self.makePlanarTextureMapping1(*args)
	def createMeshWithTangents(self, mesh, recalculateNormals = False, smooth = False, angleWeighted = False, recalculateTangents = True):
		return IMesh(IMeshManipulator_createMeshWithTangents(self.c_pointer, mesh.c_pointer, recalculateNormals, smooth, angleWeighted, recalculateTangents))
	def createMeshWith2TCoords(self, mesh):
		return IMesh(IMeshManipulator_createMeshWith2TCoords(self.c_pointer, mesh.c_pointer))
	def createMeshWith1TCoords(self, mesh):
		return IMesh(IMeshManipulator_createMeshWith1TCoords(self.c_pointer, mesh.c_pointer))
	def createMeshUniquePrimitives(self, mesh):
		return IMesh(IMeshManipulator_createMeshUniquePrimitives(self.c_pointer, mesh.c_pointer))
	def createMeshWelded(self, mesh, tolerance = ROUNDING_ERROR_f32):
		return IMesh(IMeshManipulator_createMeshWelded(self.c_pointer, mesh.c_pointer, tolerance))
	def getPolyCount1(self, mesh):
		return IMeshManipulator_getPolyCount1(self.c_pointer, mesh.c_pointer)
	def getPolyCount2(self, mesh):
		return IMeshManipulator_getPolyCount2(self.c_pointer, mesh.c_pointer)
	def getPolyCount(self, mesh):
		if isinstance(mesh, IAnimatedMesh):
			return self.getPolyCount2(mesh)
		else:
			return self.getPolyCount1(mesh)
	def createAnimatedMesh(self, mesh, type = EAMT_UNKNOWN):
		return IAnimatedMesh(IMeshManipulator_createAnimatedMesh(self.c_pointer, mesh.c_pointer, type))

class IGeometryCreator(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def createCubeMesh(self, size = vector3df(5.0,5.0,5.0)):
		return IMesh(IGeometryCreator_createCubeMesh(self.c_pointer, size.c_pointer))
	def createHillPlaneMesh(self, tileSize, tileCount, material, hillHeight, countHills, textureRepeatCount):
		return IMesh(IGeometryCreator_createHillPlaneMesh(self.c_pointer, tileSize.c_pointer, tileCount.c_pointer, material.c_pointer, hillHeight, countHills.c_pointer, textureRepeatCount.c_pointer))
	def createPlaneMesh(self, tileSize, tileCount, material, textureRepeatCount):
		return IMesh(IGeometryCreator_createPlaneMesh(self.c_pointer, tileSize.c_pointer, tileCount.c_pointer, material.c_pointer, textureRepeatCount.c_pointer))
	def createTerrainMesh(self, texture, heightmap, stretchSize, maxHeight, driver, defaultVertexBlockSize, debugBorders = False):
		return IMesh(IGeometryCreator_createTerrainMesh(self.c_pointer, texture.c_pointer, heightmap.c_pointer, stretchSize.c_pointer, maxHeight, driver.c_pointer, defaultVertexBlockSize.c_pointer, debugBorders))
	def createArrowMesh(self, tesselationCylinder = 4, tesselationCone = 8, height = 1.0, cylinderHeight = 0.6, widthCylinder = 0.05, widthCone = 0.3, colorCylinder = SColor(255,255,255,255), colorCone = SColor(255,255,255,255)):
		return IMesh(IGeometryCreator_createArrowMesh(self.c_pointer, tesselationCylinder, tesselationCone, height, cylinderHeight, widthCylinder, widthCone, colorCylinder.c_pointer, colorCone.c_pointer))
	def createSphereMesh(self, radius = 5.0, polyCountX = 16, polyCountY = 16):
		return IMesh(IGeometryCreator_createSphereMesh(self.c_pointer, radius, polyCountX, polyCountY))
	def createCylinderMesh(self, radius, length, tesselation, color = SColor(255,255,255,255), closeTop = True, oblique = 0.0):
		return IMesh(IGeometryCreator_createCylinderMesh(self.c_pointer, radius, length, tesselation, color.c_pointer, closeTop, oblique))
	def createConeMesh(self, radius, length, tesselation, colorTop = SColor(255,255,255,255), colorBottom = SColor(255,255,255,255), oblique = 0.0):
		return IMesh(IGeometryCreator_createConeMesh(self.c_pointer, radius, length, tesselation, colorTop.c_pointer, colorBottom.c_pointer, oblique))
	def createVolumeLightMesh(self, subdivideU = 32, subdivideV = 32, footColor = SColor(255,255,255,255), tailColor = SColor(255,255,255,255), lpDistance = 8.0, lightDim = vector3df(1.0,1.2,1.0)):
		return IMesh(IGeometryCreator_createVolumeLightMesh(self.c_pointer, subdivideU, subdivideV, footColor.c_pointer, tailColor.c_pointer, lpDistance, lightDim.c_pointer))

class IImage(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def lock(self):
		return IImage_lock(self.c_pointer)
	def unlock(self):
		IImage_unlock(self.c_pointer)
	def getDimension(self):
		return dimension2du(pointer = IImage_getDimension(self.c_pointer))
	def getBitsPerPixel(self):
		return IImage_getBitsPerPixel(self.c_pointer)
	def getBytesPerPixel(self):
		return IImage_getBytesPerPixel(self.c_pointer)
	def getImageDataSizeInBytes(self):
		return IImage_getImageDataSizeInBytes(self.c_pointer)
	def getImageDataSizeInPixels(self):
		return IImage_getImageDataSizeInPixels(self.c_pointer)
	def getPixel(self, x, y):
		return SColor(IImage_getPixel(self.c_pointer, x, y))
	def setPixel(self, x, y, color, blend = False):
		IImage_setPixel(self.c_pointer, x, y, color.c_pointer, blend)
	def getColorFormat(self):
		return IImage_getColorFormat(self.c_pointer)
	def getRedMask(self):
		return IImage_getRedMask(self.c_pointer)
	def getGreenMask(self):
		return IImage_getGreenMask(self.c_pointer)
	def getBlueMask(self):
		return IImage_getBlueMask(self.c_pointer)
	def getAlphaMask(self):
		return IImage_getAlphaMask(self.c_pointer)
	def getPitch(self):
		return IImage_getPitch(self.c_pointer)
	def copyToScaling(self, *args):
		if isinstance(args[0], IImage):
			IImage_copyToScaling2(self.c_pointer, args[0].c_pointer)
		else:
			target, width, height, format, pitch = 0, 0, 0, ECF_A8R8G8B8, 0
			if len(args) == 3:
				target, width, height = args
			elif len(args) == 4:
				target, width, height, format = args
			elif len(args) == 5:
				target, width, height, format, pitch = args
			else:
				return
			IImage_copyToScaling1(self.c_pointer, target, width, height, format, pitch)
	def copyToScaling1(self, target, width, height, format = ECF_A8R8G8B8, pitch = 0):
		IImage_copyToScaling1(self.c_pointer, target, width, height, format, pitch)
	def copyToScaling2(self, target):
		IImage_copyToScaling2(self.c_pointer, target.c_pointer)
	def copyTo(self, *args):
		if len(args) == 1:
			IImage_copyTo1(self.c_pointer, args[0].c_pointer, position2di(0, 0))
		elif len(args) == 2:
			IImage_copyTo1(self.c_pointer, args[0].c_pointer, args[1].c_pointer)
		elif len(args) == 3:
			IImage_copyTo2(self.c_pointer, args[0].c_pointer, args[1].c_pointer, args[2].c_pointer, recti(0))
		elif len(args) == 4:
			IImage_copyTo2(self.c_pointer, args[0].c_pointer, args[1].c_pointer, args[2].c_pointer, args[3].c_pointer)
	def copyTo1(self, target, pos = position2di(0, 0)):
		IImage_copyTo1(self.c_pointer, target.c_pointer, pos.c_pointer)
	def copyTo2(self, target, pos, sourceRect, clipRect = recti(0)):
		IImage_copyTo2(self.c_pointer, target.c_pointer, pos.c_pointer, sourceRect.c_pointer, clipRect.c_pointer)
	def copyToWithAlpha(self, target, pos, sourceRect, color, clipRect = recti(0)):
		IImage_copyToWithAlpha(self.c_pointer, target.c_pointer, pos.c_pointer, sourceRect.c_pointer, color.c_pointer, clipRect.c_pointer)
	def copyToScalingBoxFilter(self, target, bias = 0, blend = False):
		IImage_copyToScalingBoxFilter(self.c_pointer, target.c_pointer, bias, blend)
	def fill(self, color):
		IImage_fill(self.c_pointer, color.c_pointer)
	def getBitsPerPixelFromFormat(self, format):
		return IImage_getBitsPerPixelFromFormat(self.c_pointer, format)
	def isRenderTargetOnlyFormat(self, format):
		return IImage_isRenderTargetOnlyFormat(self.c_pointer, format)

class IImageLoader(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def isALoadableFileExtension(self, filename):
		return IImageLoader_isALoadableFileExtension(self.c_pointer, filename)
	def isALoadableFileFormat(self, file):
		return IImageLoader_isALoadableFileFormat(self.c_pointer, file.c_pointer)
	def loadImage(self, file):
		return IImage(IImageLoader_loadImage(self.c_pointer, file.c_pointer))

class IImageWriter(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def isAWriteableFileExtension(self, filename):
		return IImageWriter_isAWriteableFileExtension(self.c_pointer, filename)
	def writeImage(self, file, image, param = 0):
		return IImageWriter_writeImage(self.c_pointer, file.c_pointer, image.c_pointer, param)

class ITexture(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def __del__(self):
		if self.c_pointer:
			try:
				ITexture_delete(self.c_pointer)
			except:
				pass
	if IRRLICHT_VERSION < 180:
		def lock(self, readOnly = False, mipmapLevel = 0):
			return ITexture_lock(self.c_pointer, readOnly, mipmapLevel)
	else:
		def lock(self, mode = ETLM_READ_WRITE, mipmapLevel = 0):
			return ITexture_lock(self.c_pointer, mode, mipmapLevel)
	def unlock(self):
		ITexture_unlock(self.c_pointer)
	def getOriginalSize(self):
		return dimension2du(pointer = ITexture_getOriginalSize(self.c_pointer))
	def getSize(self):
		return dimension2du(pointer = ITexture_getSize(self.c_pointer))
	def getDriverType(self):
		return ITexture_getDriverType(self.c_pointer)
	def getColorFormat(self):
		return ITexture_getColorFormat(self.c_pointer)
	def getPitch(self):
		return ITexture_getPitch(self.c_pointer)
	def hasMipMaps(self):
		return ITexture_hasMipMaps(self.c_pointer)
	def hasAlpha(self):
		return ITexture_hasAlpha(self.c_pointer)
	def regenerateMipMapLevels(self):
		ITexture_regenerateMipMapLevels(self.c_pointer)
	def isRenderTarget(self):
		return ITexture_isRenderTarget(self.c_pointer)
	def getName(self):
		return ITexture_getName(self.c_pointer)

class tTexArray(array):
	def __init__(self, *args, **kwargs):
		array.__init__(self, *args, **kwargs)
		self._type_ = ITexture
		#~ self.c_pointer = args[0]
		#~ self.delete_c_pointer = True

class ITriangleSelector(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	#~ def Destructor(self):
		#~ ITriangleSelector_Destructor(self.c_pointer)
	def getTriangleCount(self):
		return ITriangleSelector_getTriangleCount(self.c_pointer)
	def getTriangles(self, triangles, arraySize, outTriangleCount, p1 = None, p2 = None):
		if p1 is None:
			p1 = matrix4(0)
		if isinstance(p1, matrix4):
			ITriangleSelector_getTriangles(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, p1.c_pointer)
		else:
			if p2 is None:
				p2 = matrix4(0)
			if isinstance(p1, aabbox3df):
				ITriangleSelector_getTriangles2(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, p1.c_pointer, p2.c_pointer)
			elif isinstance(p1, line3df):
				ITriangleSelector_getTriangles3(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, p1.c_pointer, p2.c_pointer)
			else:
				print('WARNING: parameter 4 must be aabbox3df or line3df')
	def getTriangles1(self, triangles, arraySize, outTriangleCount, transform = matrix4(0)):
		ITriangleSelector_getTriangles(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, transform.c_pointer)
	def getTriangles2(self, triangles, arraySize, outTriangleCount, box, transform = matrix4(0)):
		ITriangleSelector_getTriangles2(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, box.c_pointer, transform.c_pointer)
	def getTriangles3(self, triangles, arraySize, outTriangleCount, line, transform = matrix4(0)):
		ITriangleSelector_getTriangles3(self.c_pointer, triangles.c_pointer, arraySize, outTriangleCount, line.c_pointer, transform.c_pointer)
	def getSceneNodeForTriangle(self, triangleIndex):
		return ISceneNode(ITriangleSelector_getSceneNodeForTriangle(self.c_pointer, triangleIndex))

class IMetaTriangleSelector(ITriangleSelector):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def addTriangleSelector(self, toAdd):
		IMetaTriangleSelector_addTriangleSelector(self.c_pointer, toAdd.c_pointer)
	def removeTriangleSelector(self, toRemove):
		return IMetaTriangleSelector_removeTriangleSelector(self.c_pointer, toRemove.c_pointer)
	def removeAllTriangleSelectors(self):
		IMetaTriangleSelector_removeAllTriangleSelectors(self.c_pointer)

class IAttributeExchangingObject(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def serializeAttributes(self, out, options = 0):#io::IAttributes* out, io::SAttributeReadWriteOptions* options=0
		IAttributeExchangingObject_serializeAttributes(self.c_pointer, out.c_pointer, options)
	def deserializeAttributes(self, inp, options = 0):#io::IAttributes* in, io::SAttributeReadWriteOptions* options=0
		IAttributeExchangingObject_deserializeAttributes(self.c_pointer, inp.c_pointer, options)

class IAttributes(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getAttributeCount(self):
		return IAttributes_getAttributeCount(self.c_pointer)
	def getAttributeName(self, index):
		return IAttributes_getAttributeName(self.c_pointer, index)
	def getAttributeType1(self, attributeName):
		return IAttributes_getAttributeType1(self.c_pointer, attributeName)
	def getAttributeType2(self, index):
		return IAttributes_getAttributeType2(self.c_pointer, index)
	def getAttributeTypeString1(self, attributeName):
		return IAttributes_getAttributeTypeString1(self.c_pointer, attributeName)
	def getAttributeTypeString2(self, index):
		return IAttributes_getAttributeTypeString2(self.c_pointer, index)
	def existsAttribute(self, attributeName):
		return IAttributes_existsAttribute(self.c_pointer, attributeName)
	def findAttribute(self, attributeName):
		return IAttributes_findAttribute(self.c_pointer, attributeName)
	def clear(self):
		IAttributes_clear(self.c_pointer)
	def read(self, reader, readCurrentElementOnly = False, elementName = 0):
		return IAttributes_read(self.c_pointer, reader, readCurrentElementOnly, elementName)
	def write(self, writer, writeXMLHeader = False, elementName = 0):
		return IAttributes_write(self.c_pointer, writer, writeXMLHeader, elementName)
	def addInt(self, attributeName, value):
		IAttributes_addInt(self.c_pointer, attributeName, value)
	def setAttribute1(self, attributeName, value):
		IAttributes_setAttribute1(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute2(self, index, value):
		IAttributes_setAttribute2(self.c_pointer, index, value)
	def setAttribute3(self, attributeName, value):
		IAttributes_setAttribute3(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute4(self, index, value):
		IAttributes_setAttribute4(self.c_pointer, index, value)
	def setAttribute5(self, attributeName, value):
		IAttributes_setAttribute5(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute6(self, index, value):
		IAttributes_setAttribute6(self.c_pointer, index, value)
	def setAttribute7(self, attributeName, value):
		IAttributes_setAttribute7(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute8(self, index, value):
		IAttributes_setAttribute8(self.c_pointer, index, value)
	def setAttribute9(self, attributeName, data, dataSizeInBytes):
		IAttributes_setAttribute9(self.c_pointer, as_ansi(attributeName), data, dataSizeInBytes)
	def setAttribute10(self, index, data, dataSizeInBytes):
		IAttributes_setAttribute10(self.c_pointer, index, data, dataSizeInBytes)
	def setAttribute11(self, attributeName, value):
		IAttributes_setAttribute11(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute12(self, index, value):
		IAttributes_setAttribute12(self.c_pointer, index, value)
	def setAttribute13(self, attributeName, value):
		IAttributes_setAttribute13(self.c_pointer, as_ansi(attributeName), value)
	def setAttribute14(self, index, value):
		IAttributes_setAttribute14(self.c_pointer, index, value)
	def setAttribute15(self, attributeName, enumValue, enumerationLiterals):
		IAttributes_setAttribute15(self.c_pointer, as_ansi(attributeName), enumValue, enumerationLiterals)
	def setAttribute16(self, index, enumValue, enumerationLiterals):
		IAttributes_setAttribute16(self.c_pointer, index, enumValue, enumerationLiterals)
	def setAttribute17(self, attributeName, color):
		IAttributes_setAttribute17(self.c_pointer, as_ansi(attributeName), color)
	def setAttribute18(self, index, color):
		IAttributes_setAttribute18(self.c_pointer, index, color)
	def setAttribute19(self, attributeName, color):
		IAttributes_setAttribute19(self.c_pointer, as_ansi(attributeName), color)
	def setAttribute20(self, index, color):
		IAttributes_setAttribute20(self.c_pointer, index, color)
	def setAttribute21(self, attributeName, v):
		IAttributes_setAttribute21(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute22(self, index, v):
		IAttributes_setAttribute22(self.c_pointer, index, v)
	def setAttribute23(self, attributeName, v):
		IAttributes_setAttribute23(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute24(self, index, v):
		IAttributes_setAttribute24(self.c_pointer, index, v)
	def setAttribute25(self, attributeName, v):
		IAttributes_setAttribute25(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute26(self, index, v):
		IAttributes_setAttribute26(self.c_pointer, index, v)
	def setAttribute27(self, attributeName, v):
		IAttributes_setAttribute27(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute28(self, index, v):
		IAttributes_setAttribute28(self.c_pointer, index, v)
	def setAttribute29(self, attributeName, v):
		IAttributes_setAttribute29(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute30(self, index, v):
		IAttributes_setAttribute30(self.c_pointer, index, v)
	def setAttribute31(self, attributeName, v):
		IAttributes_setAttribute31(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute32(self, index, v):
		IAttributes_setAttribute32(self.c_pointer, index, v)
	def setAttribute33(self, attributeName, v):
		IAttributes_setAttribute33(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute34(self, index, v):
		IAttributes_setAttribute34(self.c_pointer, index, v)
	def setAttribute35(self, attributeName, v):
		IAttributes_setAttribute35(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute36(self, index, v):
		IAttributes_setAttribute36(self.c_pointer, index, v)
	def setAttribute37(self, attributeName, v):
		IAttributes_setAttribute37(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute38(self, index, v):
		IAttributes_setAttribute38(self.c_pointer, index, v)
	def setAttribute39(self, attributeName, v):
		IAttributes_setAttribute39(self.c_pointer, as_ansi(attributeName), v)
	def setAttribute40(self, index, v):
		IAttributes_setAttribute40(self.c_pointer, index, v)
	def setAttribute41(self, attributeName, texture):
		IAttributes_setAttribute41(self.c_pointer, as_ansi(attributeName), texture)
	def setAttribute42(self, index, texture):
		IAttributes_setAttribute42(self.c_pointer, index, texture)
	def setAttribute43(self, attributeName, userPointer):
		IAttributes_setAttribute43(self.c_pointer, as_ansi(attributeName), userPointer)
	def setAttribute44(self, index, userPointer):
		IAttributes_setAttribute44(self.c_pointer, index, userPointer)
	def setAttribute(self, *args):
		if isinstance(args[0], str):
			if isinstance(args[1], int) and len(args) == 2:
				IAttributes_setAttribute1(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], float) and len(args) == 2:
				IAttributes_setAttribute3(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_str) and len(args) == 2:
				IAttributes_setAttribute5(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_unicode) and len(args) == 2:
				IAttributes_setAttribute7(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_str) and len(args) == 3:
				IAttributes_setAttribute9(self.c_pointer, args[0], args[1], args[2])
			elif isinstance(args[1], (array, struct)) and len(args) == 2:
				IAttributes_setAttribute11(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], bool) and len(args) == 2:
				IAttributes_setAttribute13(self.c_pointer, args[0], args[1])
			else:
				print('ERROR in IAttributes::setAttribute: not supported type args[1]', args[1])
		elif isinstance(args[0], int):
			if isinstance(args[1], int) and len(args) == 2:
				IAttributes_setAttribute2(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], float) and len(args) == 2:
				IAttributes_setAttribute4(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_str) and len(args) == 2:
				IAttributes_setAttribute6(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_unicode) and len(args) == 2:
				IAttributes_setAttribute8(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], type_str) and len(args) == 3:
				IAttributes_setAttribute10(self.c_pointer, args[0], args[1], args[2])
			elif isinstance(args[1], (array, struct)) and len(args) == 2:
				IAttributes_setAttribute12(self.c_pointer, args[0], args[1])
			elif isinstance(args[1], bool) and len(args) == 2:
				IAttributes_setAttribute14(self.c_pointer, args[0], args[1])
			else:
				print('ERROR in IAttributes::setAttribute: not supported type args[1]', args[1])
		else:
			print('ERROR in IAttributes::setAttribute: not supported type args[0]', args[0])
	def getAttributeAsInt1(self, attributeName):
		return IAttributes_getAttributeAsInt1(self.c_pointer, attributeName)
	def getAttributeAsInt2(self, index):
		return IAttributes_getAttributeAsInt2(self.c_pointer, index)
	def getAttributeAsInt(self, arg):
		if isinstance(arg, int):
			return self.getAttributeAsInt2(arg)
		else:
			return self.getAttributeAsInt1(arg)
	def addFloat(self, attributeName, value):
		IAttributes_addFloat(self.c_pointer, attributeName, value)
	def getAttributeAsFloat1(self, attributeName):
		return IAttributes_getAttributeAsFloat1(self.c_pointer, attributeName)
	def getAttributeAsFloat2(self, index):
		return IAttributes_getAttributeAsFloat2(self.c_pointer, index)
	def addString1(self, attributeName, value):
		IAttributes_addString1(self.c_pointer, attributeName, value)
	def addString2(self, attributeName, value):
		IAttributes_addString2(self.c_pointer, attributeName, value)
	def getAttributeAsString1(self, attributeName):
		return IAttributes_getAttributeAsString1(self.c_pointer, attributeName)
	def getAttributeAsString2(self, index):
		return IAttributes_getAttributeAsString2(self.c_pointer, index)
	def getAttributeAsString3(self, attributeName, target):
		IAttributes_getAttributeAsString3(self.c_pointer, attributeName, target)
	def getAttributeAsStringW1(self, attributeName):
		return IAttributes_getAttributeAsStringW1(self.c_pointer, attributeName)
	def getAttributeAsStringW2(self, index):
		return IAttributes_getAttributeAsStringW2(self.c_pointer, index)
	def getAttributeAsStringW3(self, attributeName, target):
		IAttributes_getAttributeAsStringW3(self.c_pointer, attributeName, target)
	def addBinary1(self, attributeName, data, dataSizeInBytes):
		IAttributes_addBinary1(self.c_pointer, attributeName, data, dataSizeInBytes)
	def addArray2(self, attributeName, value):
		IAttributes_addArray2(self.c_pointer, attributeName, value)
	def getAttributeAsBinaryData1(self, attributeName, outData, maxSizeInBytes):
		IAttributes_getAttributeAsBinaryData1(self.c_pointer, attributeName, outData, maxSizeInBytes)
	def getAttributeAsBinaryData2(self, index, outData, maxSizeInBytes):
		IAttributes_getAttributeAsBinaryData2(self.c_pointer, index, outData, maxSizeInBytes)
	def getAttributeAsArray1(self, attributeName):
		return IAttributes_getAttributeAsArray1(self.c_pointer, attributeName)
	def getAttributeAsArray2(self, index):
		return IAttributes_getAttributeAsArray2(self.c_pointer, index)
	def addBool(self, attributeName, value):
		IAttributes_addBool(self.c_pointer, attributeName, value)
	def getAttributeAsBool1(self, attributeName):
		return IAttributes_getAttributeAsBool1(self.c_pointer, attributeName)
	def getAttributeAsBool2(self, index):
		return IAttributes_getAttributeAsBool2(self.c_pointer, index)
	def addEnum1(self, attributeName, enumValue, enumerationLiterals):
		IAttributes_addEnum1(self.c_pointer, attributeName, enumValue, enumerationLiterals)
	def addEnum2(self, attributeName, enumValue, enumerationLiterals):
		IAttributes_addEnum2(self.c_pointer, attributeName, enumValue, enumerationLiterals)
	def getAttributeAsEnumeration1(self, attributeName):
		return IAttributes_getAttributeAsEnumeration1(self.c_pointer, attributeName)
	def getAttributeAsEnumeration2(self, index):
		return IAttributes_getAttributeAsEnumeration2(self.c_pointer, index)
	def getAttributeAsEnumeration3(self, index, enumerationLiteralsToUse):
		return IAttributes_getAttributeAsEnumeration3(self.c_pointer, index, enumerationLiteralsToUse)
	def getAttributeAsEnumeration4(self, attributeName, enumerationLiteralsToUse):
		return IAttributes_getAttributeAsEnumeration4(self.c_pointer, attributeName, enumerationLiteralsToUse)
	def getAttributeEnumerationLiteralsOfEnumeration1(self, attributeName, outLiterals):
		IAttributes_getAttributeEnumerationLiteralsOfEnumeration1(self.c_pointer, attributeName, outLiterals)
	def getAttributeEnumerationLiteralsOfEnumeration2(self, index, outLiterals):
		IAttributes_getAttributeEnumerationLiteralsOfEnumeration2(self.c_pointer, index, outLiterals)
	def addColor(self, attributeName, value):
		IAttributes_addColor(self.c_pointer, attributeName, value)
	def getAttributeAsColor1(self, attributeName):
		return IAttributes_getAttributeAsColor1(self.c_pointer, attributeName)
	def getAttributeAsColor2(self, index):
		return IAttributes_getAttributeAsColor2(self.c_pointer, index)
	def addColorf(self, attributeName, value):
		IAttributes_addColorf(self.c_pointer, attributeName, value)
	def getAttributeAsColorf1(self, attributeName):
		return IAttributes_getAttributeAsColorf1(self.c_pointer, attributeName)
	def getAttributeAsColorf2(self, index):
		return IAttributes_getAttributeAsColorf2(self.c_pointer, index)
	def addVector3d(self, attributeName, value):
		IAttributes_addVector3d(self.c_pointer, attributeName, value)
	def getAttributeAsVector3d1(self, attributeName):
		return IAttributes_getAttributeAsVector3d1(self.c_pointer, attributeName)
	def getAttributeAsVector3d2(self, index):
		return IAttributes_getAttributeAsVector3d2(self.c_pointer, index)
	def addPosition2d(self, attributeName, value):
		IAttributes_addPosition2d(self.c_pointer, attributeName, value)
	def getAttributeAsPosition2d1(self, attributeName):
		return IAttributes_getAttributeAsPosition2d1(self.c_pointer, attributeName)
	def getAttributeAsPosition2d2(self, index):
		return IAttributes_getAttributeAsPosition2d2(self.c_pointer, index)
	def addRect(self, attributeName, value):
		IAttributes_addRect(self.c_pointer, attributeName, value)
	def getAttributeAsRect1(self, attributeName):
		return IAttributes_getAttributeAsRect1(self.c_pointer, attributeName)
	def getAttributeAsRect2(self, index):
		return IAttributes_getAttributeAsRect2(self.c_pointer, index)
	def addMatrix(self, attributeName, v):
		IAttributes_addMatrix(self.c_pointer, attributeName, v)
	def getAttributeAsMatrix1(self, attributeName):
		return IAttributes_getAttributeAsMatrix1(self.c_pointer, attributeName)
	def getAttributeAsMatrix2(self, index):
		return IAttributes_getAttributeAsMatrix2(self.c_pointer, index)
	def addQuaternion(self, attributeName, v):
		IAttributes_addQuaternion(self.c_pointer, attributeName, v)
	def getAttributeAsQuaternion1(self, attributeName):
		return IAttributes_getAttributeAsQuaternion1(self.c_pointer, attributeName)
	def getAttributeAsQuaternion2(self, index):
		return IAttributes_getAttributeAsQuaternion2(self.c_pointer, index)
	def addBox3d(self, attributeName, v):
		IAttributes_addBox3d(self.c_pointer, attributeName, v)
	def getAttributeAsBox3d1(self, attributeName):
		return IAttributes_getAttributeAsBox3d1(self.c_pointer, attributeName)
	def getAttributeAsBox3d2(self, index):
		return IAttributes_getAttributeAsBox3d2(self.c_pointer, index)
	def addPlane3d(self, attributeName, v):
		IAttributes_addPlane3d(self.c_pointer, attributeName, v)
	def getAttributeAsPlane3d1(self, attributeName):
		return IAttributes_getAttributeAsPlane3d1(self.c_pointer, attributeName)
	def getAttributeAsPlane3d2(self, index):
		return IAttributes_getAttributeAsPlane3d2(self.c_pointer, index)
	def addTriangle3d(self, attributeName, v):
		IAttributes_addTriangle3d(self.c_pointer, attributeName, v)
	def getAttributeAsTriangle3d1(self, attributeName):
		return IAttributes_getAttributeAsTriangle3d1(self.c_pointer, attributeName)
	def getAttributeAsTriangle3d2(self, index):
		return IAttributes_getAttributeAsTriangle3d2(self.c_pointer, index)
	def addLine2d(self, attributeName, v):
		IAttributes_addLine2d(self.c_pointer, attributeName, v)
	def getAttributeAsLine2d1(self, attributeName):
		return IAttributes_getAttributeAsLine2d1(self.c_pointer, attributeName)
	def getAttributeAsLine2d2(self, index):
		return IAttributes_getAttributeAsLine2d2(self.c_pointer, index)
	def addLine3d(self, attributeName, v):
		IAttributes_addLine3d(self.c_pointer, attributeName, v)
	def getAttributeAsLine3d1(self, attributeName):
		return IAttributes_getAttributeAsLine3d1(self.c_pointer, attributeName)
	def getAttributeAsLine3d2(self, index):
		return IAttributes_getAttributeAsLine3d2(self.c_pointer, index)
	def addTexture(self, attributeName, texture):
		IAttributes_addTexture(self.c_pointer, attributeName, texture)
	def getAttributeAsTexture1(self, attributeName):
		return IAttributes_getAttributeAsTexture1(self.c_pointer, attributeName)
	def getAttributeAsTexture2(self, index):
		return IAttributes_getAttributeAsTexture2(self.c_pointer, index)
	def addUserPointer(self, attributeName, userPointer):
		IAttributes_addUserPointer(self.c_pointer, attributeName, userPointer)
	def getAttributeAsUserPointer1(self, attributeName):
		return IAttributes_getAttributeAsUserPointer1(self.c_pointer, attributeName)
	def getAttributeAsUserPointer2(self, index):
		return IAttributes_getAttributeAsUserPointer2(self.c_pointer, index)

class listIGUIElementIterator:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = listIGUIElementIterator_ctor()
	def __del__(self):
		if self.c_pointer:
			try:
				listIGUIElementIterator_delete(self.c_pointer)
			except:
				pass
	def __iter__(self):
		return self
	def next(self):
		try:
			return listIGUIElementIterator_operator_next(self.c_pointer)
		except:
			try:
				raise StopIteration
			except:
				print('ERROR iteration, ERROR raise StopIteration!')
	def previous(self):
		return listIGUIElementIterator_operator_prev(self.c_pointer)
	def __eq__(self, other):
		return listIGUIElementIterator_operator_eq(self.c_pointer, other.c_pointer)
	def __ne__(self, other):
		return listIGUIElementIterator_operator_ne(self.c_pointer, other.c_pointer)
	def __iadd__(self, num):
		return listIGUIElementIterator(listIGUIElementIterator_operator_add_set(self.c_pointer, num))
	def __add__(self, num):
		return listIGUIElementIterator(listIGUIElementIterator_operator_add(self.c_pointer, num))
	def __sub__(self, num):
		return listIGUIElementIterator(listIGUIElementIterator_operator_sub(self.c_pointer, num))

class listIGUIElement:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = listIGUIElement_ctor2(args[0].c_pointer)
		else:
			self.c_pointer = listIGUIElement_ctor1()
	def __del__(self):
		if self.c_pointer:
			try:
				listIGUIElement_delete(self.c_pointer)
			except:
				pass
	def set(self, other):
		listIGUIElement_operator_set(self.c_pointer, other.c_pointer)
	def size(self):
		return listIGUIElement_size(self.c_pointer)
	def getSize(self):
		return listIGUIElement_getSize(self.c_pointer)
	def clear(self):
		listIGUIElement_clear(self.c_pointer)
	def empty(self):
		return listIGUIElement_empty(self.c_pointer)
	def push_back(self, element):
		listIGUIElement_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		listIGUIElement_push_front(self.c_pointer, element.c_pointer)
	def begin(self):
		return listIGUIElementIterator(listIGUIElement_begin(self.c_pointer))
	def end(self):
		return listIGUIElementIterator(listIGUIElement_end(self.c_pointer))
	def getLast(self):
		return listIGUIElementIterator(listIGUIElement_getLast(self.c_pointer))
	def insert_after(self, it, element):
		listIGUIElement_insert_after(self.c_pointer, it.c_pointer, element.c_pointer)
	def insert_before(self, it, element):
		listIGUIElement_insert_before(self.c_pointer, it.c_pointer, element.c_pointer)
	def erase(self, it):
		return listIGUIElementIterator(listIGUIElement_erase(self.c_pointer, it.c_pointer))
	def swap(self, other):
		listIGUIElement_swap(self.c_pointer, other.c_pointer)

class SAttributeReadWriteOptions:
	c_pointer = 0

class IGUIElement(IAttributeExchangingObject, IEventReceiver):
	def __init__(self, *args, **kwargs):
		IEventReceiver.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 4:
			self.c_pointer = IGUIElement_ctor(args[0], args[1].c_pointer, args[2].c_pointer, args[3], args[4].c_pointer)
	def __del__(self):
		if self.c_pointer:
			try:
				IGUIElement_delete(self.c_pointer)
			except:
				pass
	def getParent(self):
		return IGUIElement(IGUIElement_getParent(self.c_pointer))
	def getRelativePosition(self):
		return recti(IGUIElement_getRelativePosition(self.c_pointer))
	def setRelativePosition(self, value):
		if isinstance(value, recti):
			self.setRelativePosition1(value)
		elif isinstance(value, position2di):
			self.setRelativePosition2(value)
		else:
			print('ERROR: not valid argument with IGUIElement.setRelativePosition method!')
	def setRelativePosition1(self, r):
		IGUIElement_setRelativePosition1(self.c_pointer, r.c_pointer)
	def setRelativePosition2(self, position):
		IGUIElement_setRelativePosition2(self.c_pointer, position.c_pointer)
	def setRelativePositionProportional(self, r):
		IGUIElement_setRelativePositionProportional(self.c_pointer, r.c_pointer)
	def getAbsolutePosition(self):
		return recti(IGUIElement_getAbsolutePosition(self.c_pointer))
	def getAbsoluteClippingRect(self):
		return recti(IGUIElement_getAbsoluteClippingRect(self.c_pointer))
	def setNotClipped(self, noClip):
		IGUIElement_setNotClipped(self.c_pointer, noClip)
	def isNotClipped(self):
		return IGUIElement_isNotClipped(self.c_pointer)
	def setMaxSize(self, size):
		IGUIElement_setMaxSize(self.c_pointer, size.c_pointer)
	def setMinSize(self, size):
		IGUIElement_setMinSize(self.c_pointer, size.c_pointer)
	def setAlignment(self, left, right, top, bottom):
		IGUIElement_setAlignment(self.c_pointer, left, right, top, bottom)
	def updateAbsolutePosition(self):
		IGUIElement_updateAbsolutePosition(self.c_pointer)
	def getElementFromPoint(self, point):
		return IGUIElement(IGUIElement_getElementFromPoint(self.c_pointer, point.c_pointer))
	def isPointInside(self, point):
		return IGUIElement_isPointInside(self.c_pointer, point.c_pointer)
	def addChild(self, child):
		IGUIElement_addChild(self.c_pointer, child.c_pointer)
	def removeChild(self, child):
		IGUIElement_removeChild(self.c_pointer, child.c_pointer)
		child.c_pointer = None
	def remove(self):
		IGUIElement_remove(self.c_pointer)
		self.c_pointer = None
	def draw(self):
		IGUIElement_draw(self.c_pointer)
	def OnPostRender(self, timeMs):
		IGUIElement_OnPostRender(self.c_pointer, timeMs)
	def move(self, absoluteMovement):
		IGUIElement_move(self.c_pointer, absoluteMovement.c_pointer)
	def isVisible(self):
		return IGUIElement_isVisible(self.c_pointer)
	def setVisible(self, visible):
		IGUIElement_setVisible(self.c_pointer, visible)
	def isSubElement(self):
		return IGUIElement_isSubElement(self.c_pointer)
	def setSubElement(self, subElement):
		IGUIElement_setSubElement(self.c_pointer, subElement)
	def setTabStop(self, enable):
		IGUIElement_setTabStop(self.c_pointer, enable)
	def isTabStop(self):
		return IGUIElement_isTabStop(self.c_pointer)
	def setTabOrder(self, index):
		IGUIElement_setTabOrder(self.c_pointer, index)
	def getTabOrder(self):
		return IGUIElement_getTabOrder(self.c_pointer)
	def setTabGroup(self, isGroup):
		IGUIElement_setTabGroup(self.c_pointer, isGroup)
	def isTabGroup(self):
		return IGUIElement_isTabGroup(self.c_pointer)
	def getTabGroup(self):
		return IGUIElement(IGUIElement_getTabGroup(self.c_pointer))
	def isEnabled(self):
		return IGUIElement_isEnabled(self.c_pointer)
	def setEnabled(self, enabled):
		IGUIElement_setEnabled(self.c_pointer, enabled)
	def setText(self, text):
		IGUIElement_setText(self.c_pointer, text)
	def getText(self):
		return IGUIElement_getText(self.c_pointer)
	def setToolTipText(self, text):
		IGUIElement_setToolTipText(self.c_pointer, text)
	def getToolTipText(self):
		return IGUIElement_getToolTipText(self.c_pointer)
	def getID(self):
		return IGUIElement_getID(self.c_pointer)
	def setID(self, id):
		IGUIElement_setID(self.c_pointer, id)
	def bringToFront(self, element):
		return IGUIElement_bringToFront(self.c_pointer, element.c_pointer)
	def getChildren(self):
		return listIGUIElement(IGUIElement_getChildren(self.c_pointer))
	def getElementFromId(self, id, searchchildren = False):
		return IGUIElement(IGUIElement_getElementFromId(self.c_pointer, id, searchchildren))
	def isMyChild(self, child):
		return IGUIElement_isMyChild(self.c_pointer, child.c_pointer)
	def getNextElement(self, startOrder, reverse, group, first, closest, includeInvisible = False):
		return IGUIElement_getNextElement(self.c_pointer, startOrder, reverse, group, first.c_pointer, closest.c_pointer, includeInvisible)
	def getType(self):
		return IGUIElement_getType(self.c_pointer)
	def hasType(self, type):
		return IGUIElement_hasType(self.c_pointer, type)
	def getTypeName(self):
		return IGUIElement_getTypeName(self.c_pointer)
	def serializeAttributes(self, out_IAttributes, options = SAttributeReadWriteOptions()):
		IGUIElement_serializeAttributes(self.c_pointer, out_IAttributes.c_pointer, options.c_pointer)
	def deserializeAttributes(self, in_IAttributes, options = SAttributeReadWriteOptions()):
		IGUIElement_deserializeAttributes(self.c_pointer, in_IAttributes.c_pointer, options.c_pointer)

class IGUICheckBox(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUICheckBox_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def __del__(self):
		if self.c_pointer:
			try:
				IGUICheckBox_delete(self.c_pointer)
			except:
				pass
	def setChecked(self, checked):
		IGUICheckBox_setChecked(self.c_pointer, checked)
	def isChecked(self):
		return IGUICheckBox_isChecked(self.c_pointer)

class IGUIColorSelectDialog(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIColorSelectDialog_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def __del__(self):
		if self.c_pointer:
			try:
				IGUIColorSelectDialog_delete(self.c_pointer)
			except:
				pass

class IGUIEditBox(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIEditBox_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setOverrideFont(self, font = 0):
		IGUIEditBox_setOverrideFont(self.c_pointer, font)
	def setOverrideColor(self, color):
		IGUIEditBox_setOverrideColor(self.c_pointer, color)
	def enableOverrideColor(self, enable):
		IGUIEditBox_enableOverrideColor(self.c_pointer, enable)
	def setDrawBorder(self, border):
		IGUIEditBox_setDrawBorder(self.c_pointer, border)
	def setTextAlignment(self, horizontal, vertical):
		IGUIEditBox_setTextAlignment(self.c_pointer, horizontal, vertical)
	def setWordWrap(self, enable):
		IGUIEditBox_setWordWrap(self.c_pointer, enable)
	def isWordWrapEnabled(self):
		return IGUIEditBox_isWordWrapEnabled(self.c_pointer)
	def setMultiLine(self, enable):
		IGUIEditBox_setMultiLine(self.c_pointer, enable)
	def isMultiLineEnabled(self):
		return IGUIEditBox_isMultiLineEnabled(self.c_pointer)
	def setAutoScroll(self, enable):
		IGUIEditBox_setAutoScroll(self.c_pointer, enable)
	def isAutoScrollEnabled(self):
		return IGUIEditBox_isAutoScrollEnabled(self.c_pointer)
	def setPasswordBox(self, passwordBox, passwordChar =  '*'):
		IGUIEditBox_setPasswordBox(self.c_pointer, passwordBox, passwordChar)
	def isPasswordBox(self):
		return IGUIEditBox_isPasswordBox(self.c_pointer)
	def getTextDimension(self):
		return dimension2du(IGUIEditBox_getTextDimension(self.c_pointer))
	def setMax(self, max):
		IGUIEditBox_setMax(self.c_pointer, max)
	def getMax(self):
		return IGUIEditBox_getMax(self.c_pointer)

class IGUIFileOpenDialog(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
		elif len(args) > 0:
			if isinstance(args[0], (int, long)):
				self.c_pointer = args[0]
			elif isinstance(args[0], IGUIElement):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = self.ctor(*args, **kwargs)
	def ctor(self, gui_environment, parent = IGUIElement(), id = -1, rectangle = recti(0,0,200,200)):
		if not isinstance(parent, IGUIElement):
			parent = gui_environment.getRootGUIElement()
		return IGUIFileOpenDialog_ctor(gui_environment.c_pointer, parent.c_pointer, id, rectangle.c_pointer)
	def getFileName(self):
		return IGUIFileOpenDialog_getFileName(self.c_pointer)
	def getDirectoryName(self):
		return IGUIFileOpenDialog_getDirectoryName(self.c_pointer)

if BUILD_WITH_GUI_FILE_SELECTOR:
	class CGUIFileSelector(IGUIFileOpenDialog):
		def __init__(self, *args, **kwargs):
			self.c_pointer = None
			self.delete_c_pointer = False
			if 'c_pointer' in kwargs:
				self.c_pointer = kwargs.pop('c_pointer', None)
			elif len(args) > 0:
				if isinstance(args[0], (int, long)):
					self.c_pointer = args[0]
				elif isinstance(args[0], IGUIElement):
					self.c_pointer = args[0].c_pointer
				else:
					self.c_pointer = self.ctor(*args, **kwargs)
		def __del__(self):
			if self.c_pointer:
				try:
					CGUIFileSelector_delete(self.c_pointer)
				except:
					pass
		def ctor(self, title, gui_environment, parent = IGUIElement(), id = -1, type = EFST_OPEN_DIALOG):
			if not isinstance(parent, IGUIElement):
				parent = gui_environment.getRootGUIElement()
			return CGUIFileSelector_ctor(title, gui_environment.c_pointer, parent.c_pointer, id, type)
		def getFileName(self):
			return CGUIFileSelector_getFileName(self.c_pointer)
		def getDirectoryName(self):
			return CGUIFileSelector_getDirectoryName(self.c_pointer)
		def getFileFilter(self):
			return CGUIFileSelector_getFileFilter(self.c_pointer)
		def getDialogType(self):
			return CGUIFileSelector_getDialogType(self.c_pointer)
		#~ def addFileFilter(self, name, ext, texture = ITexture(0)):
			#~ CGUIFileSelector_addFileFilter(self.c_pointer, name, ext, texture.c_pointer)
		def addFileFilter(self, name, ext, texture = 0):
			if hasattr(texture, 'c_pointer'):
				CGUIFileSelector_addFileFilter(self.c_pointer, name, ext, texture.c_pointer)
			else:
				CGUIFileSelector_addFileFilter(self.c_pointer, name, ext, texture)
		def setCustomFileIcon(self, texture):
			CGUIFileSelector_setCustomFileIcon(self.c_pointer, texture.c_pointer)
		def setCustomDirectoryIcon(self, texture):
			CGUIFileSelector_setCustomDirectoryIcon(self.c_pointer, texture.c_pointer)
		def setDirectoryChoosable(self, choosable = True):
			CGUIFileSelector_setDirectoryChoosable(self.c_pointer, choosable)

class IGUIFont(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def draw(self, text, position, color, hcenter = False, vcenter = False, clip = recti(0)):
		IGUIFont_draw(self.c_pointer, text, position.c_pointer, color.c_pointer, hcenter, vcenter, clip.c_pointer)
	def getDimension(self, text):
		return dimension2du(IGUIFont_getDimension(self.c_pointer, text))
	def getCharacterFromPos(self, text, pixel_x):
		return IGUIFont_getCharacterFromPos(self.c_pointer, text, pixel_x)
	def getType(self):
		return IGUIFont_getType(self.c_pointer)
	def setKerningWidth(self, kerning):
		IGUIFont_setKerningWidth(self.c_pointer, kerning)
	def setKerningHeight(self, kerning):
		IGUIFont_setKerningHeight(self.c_pointer, kerning)
	def getKerningWidth(self, thisLetter, previousLetter):
		return IGUIFont_getKerningWidth(self.c_pointer, thisLetter, previousLetter)
	def getKerningHeight(self):
		return IGUIFont_getKerningHeight(self.c_pointer)
	def setInvisibleCharacters(self, s):
		IGUIFont_setInvisibleCharacters(self.c_pointer, s)

class SGUISpriteFrame(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SGUISpriteFrame_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
	def get_rectNumber(self):
		return SGUISpriteFrame_get_rectNumber(self.c_pointer)
	def set_rectNumber(self, value):
		SGUISpriteFrame_set_rectNumber(self.c_pointer, value)
	def get_textureNumber(self):
		return SGUISpriteFrame_get_textureNumber(self.c_pointer)
	def set_textureNumber(self, value):
		SGUISpriteFrame_set_textureNumber(self.c_pointer, value)
	rectNumber = property(get_rectNumber, set_rectNumber)
	textureNumber = property(get_textureNumber, set_textureNumber)

class SGUISpriteFrameArray:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SGUISpriteFrameArray_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return self.get_item(key)
	def reallocate(self, new_size):
		SGUISpriteFrameArray_reallocate(self.c_pointer, new_size)
	def setAllocStrategy(self, newStrategy = ALLOC_STRATEGY_DOUBLE):
		SGUISpriteFrameArray_setAllocStrategy(self.c_pointer, newStrategy)
	def push_back(self, element):
		SGUISpriteFrameArray_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		SGUISpriteFrameArray_push_front(self.c_pointer, element.c_pointer)
	def insert(self, element, index = 0):
		SGUISpriteFrameArray_insert(self.c_pointer, element.c_pointer, index)
	def clear(self):
		SGUISpriteFrameArray_clear(self.c_pointer)
	def set_pointer(self, newPointer, size, _is_sorted = False, _free_when_destroyed = True):
		SGUISpriteFrameArray_set_pointer(self.c_pointer, newPointer.c_pointer, size, _is_sorted, _free_when_destroyed)
	def set_free_when_destroyed(self, f):
		SGUISpriteFrameArray_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		SGUISpriteFrameArray_set_used(self.c_pointer, usedNow)
	def get_item(self, index):
		return SGUISpriteFrame(SGUISpriteFrameArray_get_item(self.c_pointer, index))
	def size(self):
		return SGUISpriteFrameArray_size(self.c_pointer)
	def empty(self):
		return SGUISpriteFrameArray_empty(self.c_pointer)
	def erase1(self, index):
		SGUISpriteFrameArray_erase1(self.c_pointer, index)
	def erase2(self, index, count):
		SGUISpriteFrameArray_erase2(self.c_pointer, index, count)
	def erase(self, *args):
		if len(args) == 1:
			self.erase1(*args)
		elif len(args) > 1:
			self.erase2(*args)
	def set_sorted(self, _is_sorted):
		SGUISpriteFrameArray_set_sorted(self.c_pointer, _is_sorted)
	def swap(self, other):
		SGUISpriteFrameArray_swap(self.c_pointer, other.c_pointer)

class SGUISprite(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SGUISprite_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
	def get_Frames(self):
		return SGUISpriteFrameArray(SGUISprite_get_Frames(self.c_pointer))
	def set_Frames(self, value):
		SGUISprite_set_Frames(self.c_pointer, value.c_pointer)
	def get_frameTime(self):
		return SGUISprite_get_frameTime(self.c_pointer)
	def set_frameTime(self, value):
		SGUISprite_set_frameTime(self.c_pointer, value)
	Frames = property(get_Frames, set_Frames)
	frameTime = property(get_frameTime, set_frameTime)

class SGUISpriteArray:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SGUISpriteArray_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return self.get_item(key)
	def reallocate(self, new_size):
		SGUISpriteArray_reallocate(self.c_pointer, new_size)
	def setAllocStrategy(self, newStrategy = ALLOC_STRATEGY_DOUBLE):
		SGUISpriteArray_setAllocStrategy(self.c_pointer, newStrategy)
	def push_back(self, element):
		SGUISpriteArray_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		SGUISpriteArray_push_front(self.c_pointer, element.c_pointer)
	def insert(self, element, index = 0):
		SGUISpriteArray_insert(self.c_pointer, element.c_pointer, index)
	def clear(self):
		SGUISpriteArray_clear(self.c_pointer)
	def set_pointer(self, newPointer, size, _is_sorted = False, _free_when_destroyed = True):
		SGUISpriteArray_set_pointer(self.c_pointer, newPointer.c_pointer, size, _is_sorted, _free_when_destroyed)
	def set_free_when_destroyed(self, f):
		SGUISpriteArray_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		SGUISpriteArray_set_used(self.c_pointer, usedNow)
	def get_item(self, index):
		return SGUISprite(SGUISpriteArray_get_item(self.c_pointer, index))
	def size(self):
		return SGUISpriteArray_size(self.c_pointer)
	def empty(self):
		return SGUISpriteArray_empty(self.c_pointer)
	def erase1(self, index):
		SGUISpriteArray_erase1(self.c_pointer, index)
	def erase2(self, index, count):
		SGUISpriteArray_erase2(self.c_pointer, index, count)
	def erase(self, *args):
		if len(args) == 1:
			self.erase1(*args)
		elif len(args) > 1:
			self.erase2(*args)
	def set_sorted(self, _is_sorted):
		SGUISpriteArray_set_sorted(self.c_pointer, _is_sorted)
	def swap(self, other):
		SGUISpriteArray_swap(self.c_pointer, other.c_pointer)

class IGUISpriteBank(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getPositions(self):
		return rects32array(IGUISpriteBank_getPositions(self.c_pointer))
	def getSprites(self):
		return SGUISpriteArray(IGUISpriteBank_getSprites(self.c_pointer))
	def getTextureCount(self):
		return IGUISpriteBank_getTextureCount(self.c_pointer)
	def getTexture(self, index):
		return IGUISpriteBank_getTexture(self.c_pointer, index)
	def addTexture(self, texture):
		IGUISpriteBank_addTexture(self.c_pointer, texture.c_pointer)
	def setTexture(self, index, texture):
		IGUISpriteBank_setTexture(self.c_pointer, index, texture.c_pointer)
	def addTextureAsSprite(self, texture):
		return IGUISpriteBank_addTextureAsSprite(self.c_pointer, texture.c_pointer)
	def clear(self):
		IGUISpriteBank_clear(self.c_pointer)
	def draw2DSprite(self, index, pos, clip = recti(0), color = SColor(255,255,255,255), starttime = 0, currenttime = 0, loop = True, center = False):
		IGUISpriteBank_draw2DSprite(self.c_pointer, index, pos.c_pointer, clip.c_pointer, color.c_pointer, starttime, currenttime, loop, center)
	def draw2DSpriteBatch(self, indices, pos, clip = recti(0), color = SColor(255,255,255,255), starttime = 0, currenttime = 0, loop = True, center = False):
		IGUISpriteBank_draw2DSpriteBatch(self.c_pointer, indices.c_pointer, pos.c_pointer, clip.c_pointer, color.c_pointer, starttime, currenttime, loop, center)

class IGUIFontBitmap(IGUIFont):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getType(self):
		return IGUIFontBitmap_getType(self.c_pointer)
	def getSpriteBank(self):
		return IGUISpriteBank(IGUIFontBitmap_getSpriteBank(self.c_pointer))
	def getSpriteNoFromChar(self, c):
		return IGUIFontBitmap_getSpriteNoFromChar(self.c_pointer, c)
	def getKerningWidth(self, thisLetter = 0, previousLetter = 0):
		return IGUIFontBitmap_getKerningWidth(self.c_pointer, thisLetter, previousLetter)

class IGUISkin(IAttributeExchangingObject):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def getColor(self, color):
		return SColor(c_pointer = IGUISkin_getColor(self.c_pointer, color))
	def setColor(self, which, newColor):
		IGUISkin_setColor(self.c_pointer, which, newColor.c_pointer)
	def getSize(self, size):
		return IGUISkin_getSize(self.c_pointer, size)
	def getDefaultText(self, text):
		return IGUISkin_getDefaultText(self.c_pointer, text)
	def setDefaultText(self, which, newText):
		IGUISkin_setDefaultText(self.c_pointer, which, newText)
	def setSize(self, which, size):
		IGUISkin_setSize(self.c_pointer, which, size)
	def getFont(self, which):
		return IGUIFont(IGUISkin_getFont(self.c_pointer, which))
	def setFont(self, font, which = EGDF_DEFAULT):
		IGUISkin_setFont(self.c_pointer, font.c_pointer, which)
	def getSpriteBank(self):
		return IGUISpriteBank(IGUISkin_getSpriteBank(self.c_pointer))
	def setSpriteBank(self, bank):
		IGUISkin_setSpriteBank(self.c_pointer, bank.c_pointer)
	def getIcon(self, icon):
		return IGUISkin_getIcon(self.c_pointer, icon)
	def setIcon(self, icon, index):
		IGUISkin_setIcon(self.c_pointer, icon, index)
	def draw3DButtonPaneStandard(self, element, rect, clip = recti(0)):
		IGUISkin_draw3DButtonPaneStandard(self.c_pointer, element.c_pointer, rect.c_pointer, clip.c_pointer)
	def draw3DButtonPanePressed(self, element, rect, clip = recti(0)):
		IGUISkin_draw3DButtonPanePressed(self.c_pointer, element.c_pointer, rect.c_pointer, clip.c_pointer)
	def draw3DSunkenPane(self, element, bgcolor, flat, fillBackGround, rect, clip = recti(0)):
		IGUISkin_draw3DSunkenPane(self.c_pointer, element.c_pointer, bgcolor.c_pointer, flat, fillBackGround, rect.c_pointer, clip.c_pointer)
	def draw3DWindowBackground(self, element, drawTitleBar, titleBarColor, rect, clip = recti(0), checkClientArea = recti(0)):
		return recti(IGUISkin_draw3DWindowBackground(self.c_pointer, element.c_pointer, drawTitleBar, titleBarColor.c_pointer, rect.c_pointer, clip.c_pointer, checkClientArea.c_pointer))
	def draw3DMenuPane(self, element, rect, clip = recti(0)):
		IGUISkin_draw3DMenuPane(self.c_pointer, element.c_pointer, rect.c_pointer, clip.c_pointer)
	def draw3DToolBar(self, element, rect, clip = recti(0)):
		IGUISkin_draw3DToolBar(self.c_pointer, element.c_pointer, rect.c_pointer, clip.c_pointer)
	def draw3DTabButton(self, element, active, rect, clip = recti(0), alignment = EGUIA_UPPERLEFT):
		IGUISkin_draw3DTabButton(self.c_pointer, element.c_pointer, active, rect.c_pointer, clip.c_pointer, alignment)
	def draw3DTabBody(self, element, border, background, rect, clip = recti(0), tabHeight = -1, alignment = EGUIA_UPPERLEFT):
		IGUISkin_draw3DTabBody(self.c_pointer, element.c_pointer, border, background, rect.c_pointer, clip.c_pointer, tabHeight, alignment)
	def drawIcon(self, element, icon, position, starttime = 0, currenttime = 0, loop = False, clip = recti(0)):
		IGUISkin_drawIcon(self.c_pointer, element.c_pointer, icon, position.c_pointer, starttime, currenttime, loop, clip.c_pointer)
	def draw2DRectangle(self, element, color, pos, clip = recti(0)):
		IGUISkin_draw2DRectangle(self.c_pointer, element.c_pointer, color.c_pointer, pos.c_pointer, clip.c_pointer)
	def getType(self):
		return IGUISkin_getType(self.c_pointer)

class IGUIButton(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIButton_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setOverrideFont(self, font = IGUIFont()):
		IGUIButton_setOverrideFont(self.c_pointer, font.c_pointer)
	def setImage(self, *args):
		if len(args) == 0:
			self.setImage1()
		elif len(args) == 1:
			self.setImage1(args[0])
		elif len(args) > 1:
			self.setImage2(*args)
	def setImage1(self, image = ITexture()):
		IGUIButton_setImage1(self.c_pointer, image.c_pointer)
	def setImage2(self, image, pos):
		IGUIButton_setImage2(self.c_pointer, image.c_pointer, pos.c_pointer)
	def setPressedImage(self, *args):
		if len(args) == 0:
			self.setPressedImage1()
		elif len(args) == 1:
			self.setPressedImage1(args[0])
		elif len(args) > 1:
			self.setPressedImage2(*args)
	def setPressedImage1(self, image = ITexture()):
		IGUIButton_setPressedImage1(self.c_pointer, image.c_pointer)
	def setPressedImage2(self, image, pos):
		IGUIButton_setPressedImage2(self.c_pointer, image.c_pointer, pos.c_pointer)
	def setSpriteBank(self, bank = IGUISpriteBank()):
		IGUIButton_setSpriteBank(self.c_pointer, bank.c_pointer)
	def setSprite(self, state, index, color = SColor(255,255,255,255), loop = False):
		IGUIButton_setSprite(self.c_pointer, state, index, color.c_pointer, loop)
	def setIsPushButton(self, isPushButton = True):
		IGUIButton_setIsPushButton(self.c_pointer, isPushButton)
	def setPressed(self, pressed = True):
		IGUIButton_setPressed(self.c_pointer, pressed)
	def isPressed(self):
		return IGUIButton_isPressed(self.c_pointer)
	def setUseAlphaChannel(self, useAlphaChannel = True):
		IGUIButton_setUseAlphaChannel(self.c_pointer, useAlphaChannel)
	def isAlphaChannelUsed(self):
		return IGUIButton_isAlphaChannelUsed(self.c_pointer)
	def isPushButton(self):
		return IGUIButton_isPushButton(self.c_pointer)
	def setDrawBorder(self, border = True):
		IGUIButton_setDrawBorder(self.c_pointer, border)
	def isDrawingBorder(self):
		return IGUIButton_isDrawingBorder(self.c_pointer)
	def setScaleImage(self, scaleImage = True):
		IGUIButton_setScaleImage(self.c_pointer, scaleImage)
	def isScalingImage(self):
		return IGUIButton_isScalingImage(self.c_pointer)

class IGUIWindow(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIWindow_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getCloseButton(self):
		return IGUIButton(IGUIWindow_getCloseButton(self.c_pointer))
	def getMinimizeButton(self):
		return IGUIButton(IGUIWindow_getMinimizeButton(self.c_pointer))
	def getMaximizeButton(self):
		return IGUIButton(IGUIWindow_getMaximizeButton(self.c_pointer))
	def isDraggable(self):
		return IGUIWindow_isDraggable(self.c_pointer)
	def setDraggable(self, draggable):
		IGUIWindow_setDraggable(self.c_pointer, draggable)
	def setDrawBackground(self, draw):
		IGUIWindow_setDrawBackground(self.c_pointer, draw)
	def getDrawBackground(self):
		return IGUIWindow_getDrawBackground(self.c_pointer)
	def setDrawTitlebar(self, draw):
		IGUIWindow_setDrawTitlebar(self.c_pointer, draw)
	def getDrawTitlebar(self):
		return IGUIWindow_getDrawTitlebar(self.c_pointer)
	def getClientRect(self):
		return recti(IGUIWindow_getClientRect(self.c_pointer))

class IGUIStaticText(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIStaticText_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setOverrideFont(self, font = IGUIFont()):
		IGUIStaticText_setOverrideFont(self.c_pointer, font.c_pointer)
	def getOverrideFont(self):
		return IGUIFont(IGUIStaticText_getOverrideFont(self.c_pointer))
	def setOverrideColor(self, color):
		IGUIStaticText_setOverrideColor(self.c_pointer, color.c_pointer)
	def getOverrideColor(self):
		return SColor(IGUIStaticText_getOverrideColor(self.c_pointer))
	def enableOverrideColor(self, enable):
		IGUIStaticText_enableOverrideColor(self.c_pointer, enable)
	def isOverrideColorEnabled(self):
		return IGUIStaticText_isOverrideColorEnabled(self.c_pointer)
	def setBackgroundColor(self, color):
		IGUIStaticText_setBackgroundColor(self.c_pointer, color.c_pointer)
	def setDrawBackground(self, draw = True):
		IGUIStaticText_setDrawBackground(self.c_pointer, draw)
	def setDrawBorder(self, draw = True):
		IGUIStaticText_setDrawBorder(self.c_pointer, draw)
	def setTextAlignment(self, horizontal, vertical):
		IGUIStaticText_setTextAlignment(self.c_pointer, horizontal, vertical)
	def setWordWrap(self, enable = True):
		IGUIStaticText_setWordWrap(self.c_pointer, enable)
	def isWordWrapEnabled(self):
		return IGUIStaticText_isWordWrapEnabled(self.c_pointer)
	def getTextHeight(self):
		return IGUIStaticText_getTextHeight(self.c_pointer)
	def getTextWidth(self):
		return IGUIStaticText_getTextWidth(self.c_pointer)

class IGUIComboBox(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIComboBox_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def __del__(self):
		if self.c_pointer:
			try:
				CGUIComboBox_delete(self.c_pointer)
			except:
				pass
	def getItemCount(self):
		return IGUIComboBox_getItemCount(self.c_pointer)
	def getItem(self, idx):
		return IGUIComboBox_getItem(self.c_pointer, idx)
	def getItemData(self, idx):
		return IGUIComboBox_getItemData(self.c_pointer, idx)
	def getIndexForItemData(self, data):
		return IGUIComboBox_getIndexForItemData(self.c_pointer, data)
	def addItem(self, text, data = 0):
		return IGUIComboBox_addItem(self.c_pointer, text, data)
	def removeItem(self, idx):
		IGUIComboBox_removeItem(self.c_pointer, idx)
	def clear(self):
		IGUIComboBox_clear(self.c_pointer)
	def getSelected(self):
		return IGUIComboBox_getSelected(self.c_pointer)
	def setSelected(self, idx):
		IGUIComboBox_setSelected(self.c_pointer, idx)
	def setTextAlignment(self, horizontal, vertical):
		IGUIComboBox_setTextAlignment(self.c_pointer, horizontal, vertical)

class IGUIContextMenu(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIContextMenu_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setCloseHandling(self, onClose):
		IGUIContextMenu_setCloseHandling(self.c_pointer, onClose)
	def getCloseHandling(self):
		return IGUIContextMenu_getCloseHandling(self.c_pointer)
	def getItemCount(self):
		return IGUIContextMenu_getItemCount(self.c_pointer)
	def addItem(self, text, commandId = -1, enabled = True, hasSubMenu = False, checked = False, autoChecking = False):
		return IGUIContextMenu_addItem(self.c_pointer, text, commandId, enabled, hasSubMenu, checked, autoChecking)
	def insertItem(self, idx, text, commandId = -1, enabled = True, hasSubMenu = False, checked = False, autoChecking = False):
		return IGUIContextMenu_insertItem(self.c_pointer, idx, text, commandId, enabled, hasSubMenu, checked, autoChecking)
	def findItemWithCommandId(self, commandId, idxStartSearch = 0):
		return IGUIContextMenu_findItemWithCommandId(self.c_pointer, commandId, idxStartSearch)
	def addSeparator(self):
		IGUIContextMenu_addSeparator(self.c_pointer)
	def getItemText(self, idx):
		return IGUIContextMenu_getItemText(self.c_pointer, idx)
	def setItemText(self, idx, text):
		IGUIContextMenu_setItemText(self.c_pointer, idx, text)
	def isItemEnabled(self, idx):
		return IGUIContextMenu_isItemEnabled(self.c_pointer, idx)
	def setItemEnabled(self, idx, enabled):
		IGUIContextMenu_setItemEnabled(self.c_pointer, idx, enabled)
	def setItemChecked(self, idx, enabled):
		IGUIContextMenu_setItemChecked(self.c_pointer, idx, enabled)
	def isItemChecked(self, idx):
		return IGUIContextMenu_isItemChecked(self.c_pointer, idx)
	def removeItem(self, idx):
		IGUIContextMenu_removeItem(self.c_pointer, idx)
	def removeAllItems(self):
		IGUIContextMenu_removeAllItems(self.c_pointer)
	def getSelectedItem(self):
		return IGUIContextMenu_getSelectedItem(self.c_pointer)
	def getItemCommandId(self, idx):
		return IGUIContextMenu_getItemCommandId(self.c_pointer, idx)
	def setItemCommandId(self, idx, id):
		IGUIContextMenu_setItemCommandId(self.c_pointer, idx, id)
	def getSubMenu(self, idx):
		return IGUIContextMenu(IGUIContextMenu_getSubMenu(self.c_pointer, idx))
	def setItemAutoChecking(self, idx, autoChecking):
		IGUIContextMenu_setItemAutoChecking(self.c_pointer, idx, autoChecking)
	def getItemAutoChecking(self, idx):
		return IGUIContextMenu_getItemAutoChecking(self.c_pointer, idx)
	def setEventParent(self, *parent):
		IGUIContextMenu_setEventParent(self.c_pointer, *parent)

class IGUIImage(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIImage_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setImage(self, image):
		IGUIImage_setImage(self.c_pointer, image)
	def setColor(self, color):
		IGUIImage_setColor(self.c_pointer, color)
	def setScaleImage(self, scale):
		IGUIImage_setScaleImage(self.c_pointer, scale)
	def setUseAlphaChannel(self, use):
		IGUIImage_setUseAlphaChannel(self.c_pointer, use)
	def isImageScaled(self):
		return IGUIImage_isImageScaled(self.c_pointer)
	def isAlphaChannelUsed(self):
		return IGUIImage_isAlphaChannelUsed(self.c_pointer)

class IGUIImageList(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def draw(self, index, destPos, clip = recti(0)):
		IGUIImageList_draw(self.c_pointer, index, destPos.c_pointer, clip.c_pointer)
	def getImageCount(self):
		return IGUIImageList_getImageCount(self.c_pointer)
	def getImageSize(self):
		return dimension2di(IGUIImageList_getImageSize(self.c_pointer))

class IGUIInOutFader(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIInOutFader_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getColor(self):
		return SColor(c_pointer = IGUIInOutFader_getColor(self.c_pointer))
	def setColor(self, *args):
		if len(args) == 1:
			IGUIInOutFader_setColor1(self.c_pointer, args[0].c_pointer)
		elif len(args) > 1:
			IGUIInOutFader_setColor2(self.c_pointer, args[0].c_pointer, args[1].c_pointer)
	def setColor1(self, color):
		IGUIInOutFader_setColor1(self.c_pointer, color.c_pointer)
	def setColor2(self, source, dest):
		IGUIInOutFader_setColor2(self.c_pointer, source.c_pointer, dest.c_pointer)
	def fadeIn(self, time):
		IGUIInOutFader_fadeIn(self.c_pointer, time)
	def fadeOut(self, time):
		IGUIInOutFader_fadeOut(self.c_pointer, time)
	def isReady(self):
		return IGUIInOutFader_isReady(self.c_pointer)

class IGUIListBox(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIListBox_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getItemCount(self):
		return IGUIListBox_getItemCount(self.c_pointer)
	def getListItem(self, id):
		return IGUIListBox_getListItem(self.c_pointer, id)
	def addItem1(self, text):
		return IGUIListBox_addItem1(self.c_pointer, text)
	def addItem2(self, text, icon):
		return IGUIListBox_addItem2(self.c_pointer, text, icon)
	def addItem(self, *args):
		if len(args) == 1:
			return self.addItem1(*args)
		elif len(args) == 2:
			return self.addItem2(*args)
	def removeItem(self, index):
		IGUIListBox_removeItem(self.c_pointer, index)
	def getIcon(self, index):
		return IGUIListBox_getIcon(self.c_pointer, index)
	def setSpriteBank(self, bank):
		IGUIListBox_setSpriteBank(self.c_pointer, bank.c_pointer)
	def clear(self):
		IGUIListBox_clear(self.c_pointer)
	def getSelected(self):
		return IGUIListBox_getSelected(self.c_pointer)
	def setSelected1(self, index):
		IGUIListBox_setSelected1(self.c_pointer, index)
	def setSelected2(self, item):
		IGUIListBox_setSelected2(self.c_pointer, item)
	def setSelected(self, arg):
		if isinstance(arg, (int, long)):
			self.setSelected1(arg)
		else:
			self.setSelected2(arg)
	def setAutoScrollEnabled(self, scroll):
		IGUIListBox_setAutoScrollEnabled(self.c_pointer, scroll)
	def isAutoScrollEnabled(self):
		return IGUIListBox_isAutoScrollEnabled(self.c_pointer)
	def setItemOverrideColor1(self, index, color = SColor(128,128,128,128)):
		IGUIListBox_setItemOverrideColor1(self.c_pointer, index, color)
	def setItemOverrideColor2(self, index, colorType, color = SColor(128,128,128,128)):
		IGUIListBox_setItemOverrideColor2(self.c_pointer, index, colorType, color)
	def setItemOverrideColor(self, *args):
		if len(args) > 1:
			if isinstance(args[1], int):
				self.setItemOverrideColor2(*args)
			else:
				self.setItemOverrideColor1(*args)
		else:
			self.setItemOverrideColor1(*args)
	def clearItemOverrideColor1(self, index):
		IGUIListBox_clearItemOverrideColor1(self.c_pointer, index)
	def clearItemOverrideColor2(self, index, colorType):
		IGUIListBox_clearItemOverrideColor2(self.c_pointer, index, colorType)
	def clearItemOverrideColor(self, *args):
		if len(args) == 1:
			self.clearItemOverrideColor1(*args)
		else:
			self.clearItemOverrideColor2(*args)
	def hasItemOverrideColor(self, index, colorType):
		return IGUIListBox_hasItemOverrideColor(self.c_pointer, index, colorType)
	def getItemOverrideColor(self, index, colorType):
		return IGUIListBox_getItemOverrideColor(self.c_pointer, index, colorType)
	def getItemDefaultColor(self, colorType):
		return IGUIListBox_getItemDefaultColor(self.c_pointer, colorType)
	def setItem(self, index, text, icon):
		IGUIListBox_setItem(self.c_pointer, index, text, icon)
	def insertItem(self, index, text, icon):
		return IGUIListBox_insertItem(self.c_pointer, index, text, icon)
	def swapItems(self, index1, index2):
		IGUIListBox_swapItems(self.c_pointer, index1, index2)
	def setItemHeight(self, height):
		IGUIListBox_setItemHeight(self.c_pointer, height)
	def setDrawBackground(self, draw):
		IGUIListBox_setDrawBackground(self.c_pointer, draw)

class IGUITab(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUITab_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getNumber(self):
		return IGUITab_getNumber(self.c_pointer)
	def setDrawBackground(self, draw = True):
		IGUITab_setDrawBackground(self.c_pointer, draw)
	def setBackgroundColor(self, color =  SColor(0, 255, 255, 255)):
		IGUITab_setBackgroundColor(self.c_pointer, color.c_pointer)
	def isDrawingBackground(self):
		return IGUITab_isDrawingBackground(self.c_pointer)
	def getBackgroundColor(self):
		return IGUITab_getBackgroundColor(self.c_pointer)
	def setTextColor(self, color =  SColor(0, 0, 0, 0)):
		IGUITab_setTextColor(self.c_pointer, color.c_pointer)
	def getTextColor(self):
		return IGUITab_getTextColor(self.c_pointer)

class IGUITabControl(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUITabControl_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def addTab(self, caption, id = -1):
		return IGUITab(IGUITabControl_addTab(self.c_pointer, caption, id))
	def getTabCount(self):
		return IGUITabControl_getTabCount(self.c_pointer)
	def getTab(self, idx):
		return IGUITab(IGUITabControl_getTab(self.c_pointer, idx))
	def setActiveTab(self, value):
		if isinstance(value, int):
			return IGUITabControl_setActiveTab1(self.c_pointer, value)
		else:
			return IGUITabControl_setActiveTab2(self.c_pointer, value.c_pointer)
	def setActiveTab1(self, idx):
		return IGUITabControl_setActiveTab1(self.c_pointer, idx)
	def setActiveTab2(self, tab):
		return IGUITabControl_setActiveTab2(self.c_pointer, tab.c_pointer)
	def getActiveTab(self):
		return IGUITab(IGUITabControl_getActiveTab(self.c_pointer))
	def setTabHeight(self, height):
		IGUITabControl_setTabHeight(self.c_pointer, height)
	def getTabHeight(self):
		return IGUITabControl_getTabHeight(self.c_pointer)
	def setTabMaxWidth(self, width):
		IGUITabControl_setTabMaxWidth(self.c_pointer, width)
	def getTabMaxWidth(self):
		return IGUITabControl_getTabMaxWidth(self.c_pointer)
	def setTabVerticalAlignment(self, alignment):
		IGUITabControl_setTabVerticalAlignment(self.c_pointer, alignment)
	def getTabVerticalAlignment(self):
		return IGUITabControl_getTabVerticalAlignment(self.c_pointer)
	def setTabExtraWidth(self, extraWidth):
		IGUITabControl_setTabExtraWidth(self.c_pointer, extraWidth)
	def getTabExtraWidth(self):
		return IGUITabControl_getTabExtraWidth(self.c_pointer)

class IGUITable(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUITable_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def addColumn(self, caption, columnIndex = -1):
		IGUITable_addColumn(self.c_pointer, caption, columnIndex)
	def removeColumn(self, columnIndex):
		IGUITable_removeColumn(self.c_pointer, columnIndex)
	def getColumnCount(self):
		return IGUITable_getColumnCount(self.c_pointer)
	def setActiveColumn(self, idx, doOrder = False):
		return IGUITable_setActiveColumn(self.c_pointer, idx, doOrder)
	def getActiveColumn(self):
		return IGUITable_getActiveColumn(self.c_pointer)
	def getActiveColumnOrdering(self):
		return IGUITable_getActiveColumnOrdering(self.c_pointer)
	def setColumnWidth(self, columnIndex, width):
		IGUITable_setColumnWidth(self.c_pointer, columnIndex, width)
	def setResizableColumns(self, resizable):
		IGUITable_setResizableColumns(self.c_pointer, resizable)
	def hasResizableColumns(self):
		return IGUITable_hasResizableColumns(self.c_pointer)
	def setColumnOrdering(self, columnIndex, mode):
		IGUITable_setColumnOrdering(self.c_pointer, columnIndex, mode)
	def getSelected(self):
		return IGUITable_getSelected(self.c_pointer)
	def setSelected(self, index):
		IGUITable_setSelected(self.c_pointer, index)
	def getRowCount(self):
		return IGUITable_getRowCount(self.c_pointer)
	def addRow(self, rowIndex):
		return IGUITable_addRow(self.c_pointer, rowIndex)
	def removeRow(self, rowIndex):
		IGUITable_removeRow(self.c_pointer, rowIndex)
	def clearRows(self):
		IGUITable_clearRows(self.c_pointer)
	def swapRows(self, rowIndexA, rowIndexB):
		IGUITable_swapRows(self.c_pointer, rowIndexA, rowIndexB)
	def orderRows(self, columnIndex = -1, mode = EGOM_NONE):
		IGUITable_orderRows(self.c_pointer, columnIndex, mode)
	def setCellText1(self, rowIndex, columnIndex, text):
		IGUITable_setCellText1(self.c_pointer, rowIndex, columnIndex, text)
	def setCellText2(self, rowIndex, columnIndex, text, color = SColor(128,128,128,128)):
		IGUITable_setCellText2(self.c_pointer, rowIndex, columnIndex, text, color.c_pointer)
	def setCellText(self, *args):
		if len(args) == 3:
			self.setCellText1(*args)
		else:
			self.setCellText2(*args)
	def setCellData(self, rowIndex, columnIndex, data):
		IGUITable_setCellData(self.c_pointer, rowIndex, columnIndex, data)
	def setCellColor(self, rowIndex, columnIndex, color = SColor(128,128,128,128)):
		IGUITable_setCellColor(self.c_pointer, rowIndex, columnIndex, color.c_pointer)
	def getCellText(self, rowIndex, columnIndex):
		return IGUITable_getCellText(self.c_pointer, rowIndex, columnIndex)
	def getCellData(self, rowIndex, columnIndex):
		return IGUITable_getCellData(self.c_pointer, rowIndex, columnIndex)
	def clear(self):
		IGUITable_clear(self.c_pointer)
	def setDrawFlags(self, flags):
		IGUITable_setDrawFlags(self.c_pointer, flags)
	def getDrawFlags(self):
		return IGUITable_getDrawFlags(self.c_pointer)

class CGUITTFont(IGUIFont):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = args[0]
		elif len(args) == 3:
			self.c_pointer = CGUITTFont_ctor(args[0].c_pointer, as_ansi(args[1]), args[2])
		elif len(args) > 3:
			self.c_pointer = CGUITTFont_createTTFont(CGUITTFont_ctor(args[0].c_pointer).c_pointer, args[1].c_pointer, as_ansi(args[2]), args[3])
	def as_IGUIFont(self):
		return IGUIFont(CGUITTFont_as_IGUIFont(self.c_pointer))
	def createTTFont(self, env, filename, size):
		return CGUITTFont(CGUITTFont_createTTFont(env.c_pointer, filename, size))
	def openTTFont(self, env, filename, size):
		self.c_pointer = CGUITTFont_createTTFont(self.c_pointer, env.c_pointer, filename, size)
	def setBatchLoadSize(self, batch_size):
		CGUITTFont_setBatchLoadSize(self.c_pointer, batch_size)
	def setMaxPageTextureSize(self, texture_size):
		CGUITTFont_setMaxPageTextureSize(self.c_pointer, texture_size.c_pointer)
	def setTransparency(self, flag):
		CGUITTFont_setTransparency(self.c_pointer, flag)
	def setMonochrome(self, flag):
		CGUITTFont_setMonochrome(self.c_pointer, flag)
	def setFontHinting(self, enable, enable_auto_hinting =  True):
		CGUITTFont_setFontHinting(self.c_pointer, enable, enable_auto_hinting)
	def draw(self, text, position, color, hcenter = False, vcenter = False, clip = recti(0)):
		CGUITTFont_draw(self.c_pointer, text, position.c_pointer, color.c_pointer, hcenter, vcenter, clip.c_pointer)
	def getDimension1(self, text):
		return dimension2du(pointer = CGUITTFont_getDimension1(self.c_pointer, text))
	def getDimension2(self, text):
		return dimension2du(pointer = CGUITTFont_getDimension2(self.c_pointer, text))
	def getDimension(self, text):
		try:
			return self.getDimension1(text)
		except:
			return self.getDimension2(text)
	def getCharacterFromPos1(self, text, pixel_x):
		return CGUITTFont_getCharacterFromPos1(self.c_pointer, text, pixel_x)
	def getCharacterFromPos2(self, text, pixel_x):
		return CGUITTFont_getCharacterFromPos2(self.c_pointer, text, pixel_x)
	def setKerningWidth(self, kerning):
		CGUITTFont_setKerningWidth(self.c_pointer, kerning)
	def setKerningHeight(self, kerning):
		CGUITTFont_setKerningHeight(self.c_pointer, kerning)
	def getKerningWidth1(self, thisLetter = '', previousLetter = ''):
		return CGUITTFont_getKerningWidth1(self.c_pointer, thisLetter, previousLetter)
	def getKerningWidth2(self, thisLetter = 0, previousLetter = 0):
		return CGUITTFont_getKerningWidth2(self.c_pointer, thisLetter, previousLetter)
	def getKerningWidth(self, *args):
		if isinstance(args[0], type_unicode):
			return self.getKerningWidth1(*args)
		else:
			return self.getKerningWidth2(*args)
	def getKerningHeight(self):
		return CGUITTFont_getKerningHeight(self.c_pointer)
	def setInvisibleCharacters1(self, s):
		CGUITTFont_setInvisibleCharacters1(self.c_pointer, s)
	def setInvisibleCharacters2(self, s):
		CGUITTFont_setInvisibleCharacters2(self.c_pointer, s)
	def setInvisibleCharacters(self, s):
		try:
			self.setInvisibleCharacters1(s)
		except:
			self.setInvisibleCharacters2(s)
	def forceGlyphUpdate(self):
		CGUITTFont_forceGlyphUpdate(self.c_pointer)

class IGUIToolBar(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 1:
			self.c_pointer = IGUIToolBar_ctor(*args)
	def addButton(self, id = -1, text = '', tooltiptext = '', img = ITexture(0), pressedimg = ITexture(0), isPushButton = False, useAlphaChannel = False):
		if not isinstance(img, ITexture):
			img = ITexture(0)
		if not isinstance(pressedimg, ITexture):
			pressedimg = ITexture(0)
		return IGUIButton(IGUIToolBar_addButton(self.c_pointer, id, text, tooltiptext, img.c_pointer, pressedimg.c_pointer, isPushButton, useAlphaChannel))

class IGUITreeViewNode(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
	def getOwner(self):
		return IGUITreeView(IGUITreeViewNode_getOwner(self.c_pointer))
	def getParent(self):
		return IGUITreeViewNode_getParent(self.c_pointer)
	def getText(self):
		return IGUITreeViewNode_getText(self.c_pointer)
	def setText(self, text):
		IGUITreeViewNode_setText(self.c_pointer, text)
	def getIcon(self):
		return IGUITreeViewNode_getIcon(self.c_pointer)
	def setIcon(self, icon):
		IGUITreeViewNode_setIcon(self.c_pointer, icon)
	def getImageIndex(self):
		return IGUITreeViewNode_getImageIndex(self.c_pointer)
	def setImageIndex(self, imageIndex):
		IGUITreeViewNode_setImageIndex(self.c_pointer, imageIndex)
	def getSelectedImageIndex(self):
		return IGUITreeViewNode_getSelectedImageIndex(self.c_pointer)
	def setSelectedImageIndex(self, imageIndex):
		IGUITreeViewNode_setSelectedImageIndex(self.c_pointer, imageIndex)
	def getData(self):
		return IGUITreeViewNode_getData(self.c_pointer)
	def setData(self, data):
		IGUITreeViewNode_setData(self.c_pointer, data)
	def getData2(self):
		return IReferenceCounted(IGUITreeViewNode_getData2(self.c_pointer))
	def setData2(self, data):
		IGUITreeViewNode_setData2(self.c_pointer, data.c_pointer)
	def getChildCount(self):
		return IGUITreeViewNode_getChildCount(self.c_pointer)
	if IRRLICHT_VERSION < 180:
		def clearChilds(self):
			IGUITreeViewNode_clearChilds(self.c_pointer)
		def hasChilds(self):
			return IGUITreeViewNode_hasChilds(self.c_pointer)
	def addChildBack(self, text, icon = 0, imageIndex = -1, selectedImageIndex = -1, data = 0, data2 = IReferenceCounted()):
		return IGUITreeViewNode(IGUITreeViewNode_addChildBack(self.c_pointer, text, icon, imageIndex, selectedImageIndex, data, data2.c_pointer))
	def addChildFront(self, text, icon = 0, imageIndex = -1, selectedImageIndex = -1, data = 0, data2 = IReferenceCounted()):
		return IGUITreeViewNode(IGUITreeViewNode_addChildFront(self.c_pointer, text, icon, imageIndex, selectedImageIndex, data, data2.c_pointer))
	def insertChildAfter(self, other, text, icon = 0, imageIndex = -1, selectedImageIndex = -1, data = 0, data2 = IReferenceCounted()):
		return IGUITreeViewNode(IGUITreeViewNode_insertChildAfter(self.c_pointer, other.c_pointer, text, icon, imageIndex, selectedImageIndex, data, data2.c_pointer))
	def insertChildBefore(self, other, text, icon = 0, imageIndex = -1, selectedImageIndex = -1, data = 0, data2 = IReferenceCounted()):
		return IGUITreeViewNode(IGUITreeViewNode_insertChildBefore(self.c_pointer, other.c_pointer, text, icon, imageIndex, selectedImageIndex, data, data2.c_pointer))
	def getFirstChild(self):
		return IGUITreeViewNode(IGUITreeViewNode_getFirstChild(self.c_pointer))
	def getLastChild(self):
		return IGUITreeViewNode(IGUITreeViewNode_getLastChild(self.c_pointer))
	def getPrevSibling(self):
		return IGUITreeViewNode(IGUITreeViewNode_getPrevSibling(self.c_pointer))
	def getNextSibling(self):
		return IGUITreeViewNode(IGUITreeViewNode_getNextSibling(self.c_pointer))
	def getNextVisible(self):
		return IGUITreeViewNode(IGUITreeViewNode_getNextVisible(self.c_pointer))
	def deleteChild(self, child):
		return IGUITreeViewNode_deleteChild(self.c_pointer, child.c_pointer)
	def moveChildUp(self, child):
		return IGUITreeViewNode_moveChildUp(self.c_pointer, child.c_pointer)
	def moveChildDown(self, child):
		return IGUITreeViewNode_moveChildDown(self.c_pointer, child.c_pointer)
	def getExpanded(self):
		return IGUITreeViewNode_getExpanded(self.c_pointer)
	def setExpanded(self, expanded):
		IGUITreeViewNode_setExpanded(self.c_pointer, expanded)
	def getSelected(self):
		return IGUITreeViewNode_getSelected(self.c_pointer)
	def setSelected(self, selected):
		IGUITreeViewNode_setSelected(self.c_pointer, selected)
	def isRoot(self):
		return IGUITreeViewNode_isRoot(self.c_pointer)
	def getLevel(self):
		return IGUITreeViewNode_getLevel(self.c_pointer)
	def isVisible(self):
		return IGUITreeViewNode_isVisible(self.c_pointer)

class IGUITreeView(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUITreeView_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getRoot(self):
		return IGUITreeViewNode(IGUITreeView_getRoot(self.c_pointer))
	def getSelected(self):
		return IGUITreeViewNode(IGUITreeView_getSelected(self.c_pointer))
	def getLinesVisible(self):
		return IGUITreeView_getLinesVisible(self.c_pointer)
	def setLinesVisible(self, visible):
		IGUITreeView_setLinesVisible(self.c_pointer, visible)
	def setIconFont(self, font):
		IGUITreeView_setIconFont(self.c_pointer, font.c_pointer)
	def setImageList(self, imageList):
		IGUITreeView_setImageList(self.c_pointer, imageList.c_pointer)
	def getImageList(self):
		return IGUIImageList(IGUITreeView_getImageList(self.c_pointer))
	def setImageLeftOfIcon(self, bLeftOf):
		IGUITreeView_setImageLeftOfIcon(self.c_pointer, bLeftOf)
	def getImageLeftOfIcon(self):
		return IGUITreeView_getImageLeftOfIcon(self.c_pointer)
	def getLastEventNode(self):
		return IGUITreeViewNode(IGUITreeView_getLastEventNode(self.c_pointer))

class IGUIScrollBar(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUIScrollBar_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def setMax(self, max):
		IGUIScrollBar_setMax(self.c_pointer, max)
	def getMax(self):
		return IGUIScrollBar_getMax(self.c_pointer)
	def setMin(self, max):
		IGUIScrollBar_setMin(self.c_pointer, max)
	def getMin(self):
		return IGUIScrollBar_getMin(self.c_pointer)
	def getSmallStep(self):
		return IGUIScrollBar_getSmallStep(self.c_pointer)
	def setSmallStep(self, step):
		IGUIScrollBar_setSmallStep(self.c_pointer, step)
	def getLargeStep(self):
		return IGUIScrollBar_getLargeStep(self.c_pointer)
	def setLargeStep(self, step):
		IGUIScrollBar_setLargeStep(self.c_pointer, step)
	def getPos(self):
		return IGUIScrollBar_getPos(self.c_pointer)
	def setPos(self, pos = 0):# s32 pos = 0
		IGUIScrollBar_setPos(self.c_pointer, pos)

class IGUISpinBox(IGUIElement):
	def __init__(self, *args, **kwargs):
		IGUIElement.__init__(self)
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = args[0]
		elif len(args) > 3:
			self.c_pointer = IGUISpinBox_ctor(args[0].c_pointer, args[1].c_pointer, args[2], args[3].c_pointer)
	def getEditBox(self):
		return IGUISpinBox_getEditBox(self.c_pointer)
	def setValue(self, val):
		IGUISpinBox_setValue(self.c_pointer, val)
	def getValue(self):
		return IGUISpinBox_getValue(self.c_pointer)
	def setRange(self, min, max):
		IGUISpinBox_setRange(self.c_pointer, min, max)
	def getMin(self):
		return IGUISpinBox_getMin(self.c_pointer)
	def getMax(self):
		return IGUISpinBox_getMax(self.c_pointer)
	def setStepSize(self, step = 1.0):
		IGUISpinBox_setStepSize(self.c_pointer, step)
	def setDecimalPlaces(self, places):
		IGUISpinBox_setDecimalPlaces(self.c_pointer, places)
	def getStepSize(self):
		return IGUISpinBox_getStepSize(self.c_pointer)

#extended methods for class IGUIElement
IGUIElement.as_IGUIButton = lambda self: IGUIButton(IGUIElement_as_IGUIButton(self.c_pointer))
IGUIElement.as_IGUICheckBox = lambda self: IGUICheckBox(IGUIElement_as_IGUICheckBox(self.c_pointer))
IGUIElement.as_IGUIColorSelectDialog = lambda self: IGUIColorSelectDialog(IGUIElement_as_IGUIColorSelectDialog(self.c_pointer))
IGUIElement.as_IGUIComboBox = lambda self: IGUIComboBox(IGUIElement_as_IGUIComboBox(self.c_pointer))
IGUIElement.as_IGUIContextMenu = lambda self: IGUIContextMenu(IGUIElement_as_IGUIContextMenu(self.c_pointer))
IGUIElement.as_IGUIEditBox = lambda self: IGUIEditBox(IGUIElement_as_IGUIEditBox(self.c_pointer))
IGUIElement.as_IGUIFileOpenDialog = lambda self: IGUIFileOpenDialog(IGUIElement_as_IGUIFileOpenDialog(self.c_pointer))
IGUIElement.as_IGUIFontBitmap = lambda self: IGUIFontBitmap(IGUIElement_as_IGUIFontBitmap(self.c_pointer))
IGUIElement.as_IGUIImage = lambda self: IGUIImage(IGUIElement_as_IGUIImage(self.c_pointer))
IGUIElement.as_IGUIListBox = lambda self: IGUIListBox(IGUIElement_as_IGUIListBox(self.c_pointer))
IGUIElement.as_IGUIMeshViewer = lambda self: IGUIMeshViewer(IGUIElement_as_IGUIMeshViewer(self.c_pointer))
IGUIElement.as_IGUIScrollBar = lambda self: IGUIScrollBar(IGUIElement_as_IGUIScrollBar(self.c_pointer))
IGUIElement.as_IGUISpinBox = lambda self: IGUISpinBox(IGUIElement_as_IGUISpinBox(self.c_pointer))
IGUIElement.as_IGUIStaticText = lambda self: IGUIStaticText(IGUIElement_as_IGUIStaticText(self.c_pointer))
IGUIElement.as_IGUITab = lambda self: IGUITab(IGUIElement_as_IGUITab(self.c_pointer))
IGUIElement.as_IGUITabControl = lambda self: IGUITabControl(IGUIElement_as_IGUITabControl(self.c_pointer))
IGUIElement.as_IGUITable = lambda self: IGUITable(IGUIElement_as_IGUITable(self.c_pointer))
IGUIElement.as_IGUIToolBar = lambda self: IGUIToolBar(IGUIElement_as_IGUIToolBar(self.c_pointer))
IGUIElement.as_IGUITreeView = lambda self: IGUITreeView(IGUIElement_as_IGUITreeView(self.c_pointer))
IGUIElement.as_IGUIWindow = lambda self: IGUIWindow(IGUIElement_as_IGUIWindow(self.c_pointer))


class SParticle(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) == 0 and len(kwargs) == 0:
			self.ctor()
		elif len(args) > 0:
			self.ctor(args[0])
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
			self.delete_c_pointer = False
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def ctor(self, length = 1):
		self.c_pointer = SParticle_ctor(length)
	def get_item(self, index = 0):
		return SParticle_get_item(self.c_pointer, index)
	def set_item(self, value, index = 0):
		SParticle_set_item(self.c_pointer, value, index)
	def get_pos(self, index = 0):
		return vector3df(SParticle_get_pos(self.c_pointer, index))
	def set_pos(self, value, index = 0):
		SParticle_set_pos(self.c_pointer, value.c_pointer, index)
	def get_vector(self, index = 0):
		return vector3df(SParticle_get_vector(self.c_pointer, index))
	def set_vector(self, value, index = 0):
		SParticle_set_vector(self.c_pointer, value.c_pointer, index)
	def get_startTime(self, index = 0):
		return SParticle_get_startTime(self.c_pointer, index)
	def set_startTime(self, value, index = 0):
		SParticle_set_startTime(self.c_pointer, value, index)
	def get_endTime(self, index = 0):
		return SParticle_get_endTime(self.c_pointer, index)
	def set_endTime(self, value, index = 0):
		SParticle_set_endTime(self.c_pointer, value, index)
	def get_color(self, index = 0):
		return SColor(SParticle_get_color(self.c_pointer, index))
	def set_color(self, value, index = 0):
		SParticle_set_color(self.c_pointer, value.c_pointer, index)
	def get_startColor(self, index = 0):
		return SColor(SParticle_get_startColor(self.c_pointer, index))
	def set_startColor(self, value, index = 0):
		SParticle_set_startColor(self.c_pointer, value.c_pointer, index)
	def get_startVector(self, index = 0):
		return vector3df(SParticle_get_startVector(self.c_pointer, index))
	def set_startVector(self, value, index = 0):
		SParticle_set_startVector(self.c_pointer, value.c_pointer, index)
	def get_size(self, index = 0):
		return dimension2df(SParticle_get_size(self.c_pointer, index))
	def set_size(self, value, index = 0):
		SParticle_set_size(self.c_pointer, value.c_pointer, index)
	def get_startSize(self, index = 0):
		return dimension2df(SParticle_get_startSize(self.c_pointer, index))
	def set_startSize(self, value, index = 0):
		SParticle_set_startSize(self.c_pointer, value.c_pointer, index)
	pos = property(get_pos, set_pos)
	vector = property(get_vector, set_vector)
	startTime = property(get_startTime, set_startTime)
	endTime = property(get_endTime, set_endTime)
	color = property(get_color, set_color)
	startColor = property(get_startColor, set_startColor)
	startVector = property(get_startVector, set_startVector)
	size = property(get_size, set_size)
	startSize = property(get_startSize, set_startSize)

class IParticleAffector(IAttributeExchangingObject):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def ctor(self):
		return IParticleAffector_ctor()
	def affect(self, now, particlearray, count):
		IParticleAffector_affect(self.c_pointer, now, particlearray.c_pointer, count)
	def setEnabled(self, enabled):
		IParticleAffector_setEnabled(self.c_pointer, enabled)
	def getEnabled(self):
		return IParticleAffector_getEnabled(self.c_pointer)
	def getType(self):
		return IParticleAffector_getType(self.c_pointer)

class IParticleAttractionAffector(IParticleAffector):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setPoint(self, point):
		IParticleAttractionAffector_setPoint(self.c_pointer, point.c_pointer)
	def setAttract(self, attract):
		IParticleAttractionAffector_setAttract(self.c_pointer, attract)
	def setAffectX(self, affect):
		IParticleAttractionAffector_setAffectX(self.c_pointer, affect)
	def setAffectY(self, affect):
		IParticleAttractionAffector_setAffectY(self.c_pointer, affect)
	def setAffectZ(self, affect):
		IParticleAttractionAffector_setAffectZ(self.c_pointer, affect)
	def getPoint(self):
		return vector3df(IParticleAttractionAffector_getPoint(self.c_pointer))
	def getAttract(self):
		return IParticleAttractionAffector_getAttract(self.c_pointer)
	def getAffectX(self):
		return IParticleAttractionAffector_getAffectX(self.c_pointer)
	def getAffectY(self):
		return IParticleAttractionAffector_getAffectY(self.c_pointer)
	def getAffectZ(self):
		return IParticleAttractionAffector_getAffectZ(self.c_pointer)
	def getType(self):
		return IParticleAttractionAffector_getType(self.c_pointer)

class IParticleFadeOutAffector(IParticleAffector):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setTargetColor(self, targetColor):
		IParticleFadeOutAffector_setTargetColor(self.c_pointer, targetColor.c_pointer)
	def setFadeOutTime(self, fadeOutTime):
		IParticleFadeOutAffector_setFadeOutTime(self.c_pointer, fadeOutTime)
	def getTargetColor(self):
		return SColor(IParticleFadeOutAffector_getTargetColor(self.c_pointer))
	def getFadeOutTime(self):
		return IParticleFadeOutAffector_getFadeOutTime(self.c_pointer)
	def getType(self):
		return IParticleFadeOutAffector_getType(self.c_pointer)

class IParticleGravityAffector(IParticleAffector):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setTimeForceLost(self, timeForceLost):
		IParticleGravityAffector_setTimeForceLost(self.c_pointer, timeForceLost)
	def setGravity(self, gravity):
		IParticleGravityAffector_setGravity(self.c_pointer, gravity.c_pointer)
	def getTimeForceLost(self):
		return IParticleGravityAffector_getTimeForceLost(self.c_pointer)
	def getGravity(self):
		return vector3df(IParticleGravityAffector_getGravity(self.c_pointer))
	def getType(self):
		return IParticleGravityAffector_getType(self.c_pointer)

class IParticleRotationAffector(IParticleAffector):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setPivotPoint(self, point):
		IParticleRotationAffector_setPivotPoint(self.c_pointer, point.c_pointer)
	def setSpeed(self, speed):
		IParticleRotationAffector_setSpeed(self.c_pointer, speed.c_pointer)
	def getPivotPoint(self):
		return vector3df(IParticleRotationAffector_getPivotPoint(self.c_pointer))
	def getSpeed(self):
		return vector3df(IParticleRotationAffector_getSpeed(self.c_pointer))
	def getType(self):
		return IParticleRotationAffector_getType(self.c_pointer)

class IParticleEmitter(IAttributeExchangingObject):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def emitt(self, now, timeSinceLastCall, outArray):
		return IParticleEmitter_emitt(self.c_pointer, now, timeSinceLastCall, outArray.c_pointer)#ctypes.byref(ctypes.c_long(outArray.c_pointer))
	def setDirection(self, newDirection):
		IParticleEmitter_setDirection(self.c_pointer, newDirection.c_pointer)
	def setMinParticlesPerSecond(self, minPPS):
		IParticleEmitter_setMinParticlesPerSecond(self.c_pointer, minPPS)
	def setMaxParticlesPerSecond(self, maxPPS):
		IParticleEmitter_setMaxParticlesPerSecond(self.c_pointer, maxPPS)
	def setMinStartColor(self, color):
		IParticleEmitter_setMinStartColor(self.c_pointer, color.c_pointer)
	def setMaxStartColor(self, color):
		IParticleEmitter_setMaxStartColor(self.c_pointer, color.c_pointer)
	def setMaxStartSize(self, size):
		IParticleEmitter_setMaxStartSize(self.c_pointer, size.c_pointer)
	def setMinStartSize(self, size):
		IParticleEmitter_setMinStartSize(self.c_pointer, size.c_pointer)
	def getDirection(self):
		return vector3df(IParticleEmitter_getDirection(self.c_pointer))
	def getMinParticlesPerSecond(self):
		return IParticleEmitter_getMinParticlesPerSecond(self.c_pointer)
	def getMaxParticlesPerSecond(self):
		return IParticleEmitter_getMaxParticlesPerSecond(self.c_pointer)
	def getMinStartColor(self):
		return SColor(IParticleEmitter_getMinStartColor(self.c_pointer))
	def getMaxStartColor(self):
		return SColor(IParticleEmitter_getMaxStartColor(self.c_pointer))
	def getMaxStartSize(self):
		return dimension2df(IParticleEmitter_getMaxStartSize(self.c_pointer))
	def getMinStartSize(self):
		return dimension2df(IParticleEmitter_getMinStartSize(self.c_pointer))
	def getType(self):
		return IParticleEmitter_getType(self.c_pointer)

class IParticleAnimatedMeshSceneNodeEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setAnimatedMeshSceneNode(self, node):
		IParticleAnimatedMeshSceneNodeEmitter_setAnimatedMeshSceneNode(self.c_pointer, node.c_pointer)
	def setUseNormalDirection(self, useNormalDirection = True):
		IParticleAnimatedMeshSceneNodeEmitter_setUseNormalDirection(self.c_pointer, useNormalDirection)
	def setNormalDirectionModifier(self, normalDirectionModifier):
		IParticleAnimatedMeshSceneNodeEmitter_setNormalDirectionModifier(self.c_pointer, normalDirectionModifier)
	def setEveryMeshVertex(self, everyMeshVertex = True):
		IParticleAnimatedMeshSceneNodeEmitter_setEveryMeshVertex(self.c_pointer, everyMeshVertex)
	def getAnimatedMeshSceneNode(self):
		return IAnimatedMeshSceneNode(IParticleAnimatedMeshSceneNodeEmitter_getAnimatedMeshSceneNode(self.c_pointer))
	def isUsingNormalDirection(self):
		return IParticleAnimatedMeshSceneNodeEmitter_isUsingNormalDirection(self.c_pointer)
	def getNormalDirectionModifier(self):
		return IParticleAnimatedMeshSceneNodeEmitter_getNormalDirectionModifier(self.c_pointer)
	def getEveryMeshVertex(self):
		return IParticleAnimatedMeshSceneNodeEmitter_getEveryMeshVertex(self.c_pointer)
	def getType(self):
		return IParticleAnimatedMeshSceneNodeEmitter_getType(self.c_pointer)

class IParticleBoxEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setBox(self, box):
		IParticleBoxEmitter_setBox(self.c_pointer, box.c_pointer)
	def getBox(self):
		return aabbox3df(IParticleBoxEmitter_getBox(self.c_pointer))
	def getType(self):
		return IParticleBoxEmitter_getType(self.c_pointer)

class IParticleCylinderEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setCenter(self, center):
		IParticleCylinderEmitter_setCenter(self.c_pointer, center.c_pointer)
	def setNormal(self, normal):
		IParticleCylinderEmitter_setNormal(self.c_pointer, normal.c_pointer)
	def setRadius(self, radius):
		IParticleCylinderEmitter_setRadius(self.c_pointer, radius)
	def setLength(self, length):
		IParticleCylinderEmitter_setLength(self.c_pointer, length)
	def setOutlineOnly(self, outlineOnly = True):
		IParticleCylinderEmitter_setOutlineOnly(self.c_pointer, outlineOnly)
	def getCenter(self):
		return vector3df(IParticleCylinderEmitter_getCenter(self.c_pointer))
	def getNormal(self):
		return vector3df(IParticleCylinderEmitter_getNormal(self.c_pointer))
	def getRadius(self):
		return IParticleCylinderEmitter_getRadius(self.c_pointer)
	def getLength(self):
		return IParticleCylinderEmitter_getLength(self.c_pointer)
	def getOutlineOnly(self):
		return IParticleCylinderEmitter_getOutlineOnly(self.c_pointer)
	def getType(self):
		return IParticleCylinderEmitter_getType(self.c_pointer)

class IParticleMeshEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setMesh(self, mesh):
		IParticleMeshEmitter_setMesh(self.c_pointer, mesh.c_pointer)
	def setUseNormalDirection(self, useNormalDirection = True):
		IParticleMeshEmitter_setUseNormalDirection(self.c_pointer, useNormalDirection)
	def setNormalDirectionModifier(self, normalDirectionModifier):
		IParticleMeshEmitter_setNormalDirectionModifier(self.c_pointer, normalDirectionModifier)
	def setEveryMeshVertex(self, everyMeshVertex = True):
		IParticleMeshEmitter_setEveryMeshVertex(self.c_pointer, everyMeshVertex)
	def getMesh(self):
		return IMesh(IParticleMeshEmitter_getMesh(self.c_pointer))
	def isUsingNormalDirection(self):
		return IParticleMeshEmitter_isUsingNormalDirection(self.c_pointer)
	def getNormalDirectionModifier(self):
		return IParticleMeshEmitter_getNormalDirectionModifier(self.c_pointer)
	def getEveryMeshVertex(self):
		return IParticleMeshEmitter_getEveryMeshVertex(self.c_pointer)
	def getType(self):
		return IParticleMeshEmitter_getType(self.c_pointer)

class IParticleRingEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setCenter(self, center):
		IParticleRingEmitter_setCenter(self.c_pointer, center.c_pointer)
	def setRadius(self, radius):
		IParticleRingEmitter_setRadius(self.c_pointer, radius)
	def setRingThickness(self, ringThickness):
		IParticleRingEmitter_setRingThickness(self.c_pointer, ringThickness)
	def getCenter(self):
		return vector3df(IParticleRingEmitter_getCenter(self.c_pointer))
	def getRadius(self):
		return IParticleRingEmitter_getRadius(self.c_pointer)
	def getRingThickness(self):
		return IParticleRingEmitter_getRingThickness(self.c_pointer)
	def getType(self):
		return IParticleRingEmitter_getType(self.c_pointer)

class IParticleSphereEmitter(IParticleEmitter):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setCenter(self, center):
		IParticleSphereEmitter_setCenter(self.c_pointer, center.c_pointer)
	def setRadius(self, radius):
		IParticleSphereEmitter_setRadius(self.c_pointer, radius)
	def getCenter(self):
		return vector3df(IParticleSphereEmitter_getCenter(self.c_pointer))
	def getRadius(self):
		return IParticleSphereEmitter_getRadius(self.c_pointer)
	def getType(self):
		return IParticleSphereEmitter_getType(self.c_pointer)


class ISceneNodeAnimator(IAttributeExchangingObject, IEventReceiver):
	def __init__(self, *args, **kwargs):
		IEventReceiver.__init__(self)
		self.c_pointer = args[0]
	def animateNode(self, node, timeMs):
		ISceneNodeAnimator_animateNode(self.c_pointer, node.c_pointer, timeMs)
	def createClone(self, node, newManager = 0):
		return ISceneNodeAnimator(ISceneNodeAnimator_createClone(self.c_pointer, node.c_pointer, newManager.c_pointer))
	def isEventReceiverEnabled(self):
		return ISceneNodeAnimator_isEventReceiverEnabled(self.c_pointer)
	def OnEvent(self, event):
		return ISceneNodeAnimator_OnEvent(self.c_pointer, event)
	def getType(self):
		return ISceneNodeAnimator_getType(self.c_pointer)
	def hasFinished(self):
		return ISceneNodeAnimator_hasFinished(self.c_pointer)
	def set_func_event(self, func_event):
		return ISceneNodeAnimator_set_func_event(self.c_pointer, OnEventFunc(func_event))

class ISceneNodeAnimatorCollisionResponse(ISceneNodeAnimator):
	def __init__(self, *args, **kwargs):
		IEventReceiver.__init__(self)
		self.c_pointer = None
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
	#~ def Destructor(self):
		#~ ISceneNodeAnimatorCollisionResponse_Destructor(self.c_pointer)
	def isFalling(self):
		return ISceneNodeAnimatorCollisionResponse_isFalling(self.c_pointer)
	def setEllipsoidRadius(self, radius):
		ISceneNodeAnimatorCollisionResponse_setEllipsoidRadius(self.c_pointer, radius.c_pointer)
	def getEllipsoidRadius(self):
		return vector3df(ISceneNodeAnimatorCollisionResponse_getEllipsoidRadius(self.c_pointer), True)
	def setGravity(self, gravity):
		ISceneNodeAnimatorCollisionResponse_setGravity(self.c_pointer, gravity.c_pointer)
	def getGravity(self):
		return vector3df(ISceneNodeAnimatorCollisionResponse_getGravity(self.c_pointer), True)
	def jump(self, jumpSpeed):
		ISceneNodeAnimatorCollisionResponse_jump(self.c_pointer, jumpSpeed)
	def setAnimateTarget(self, enable = True):
		ISceneNodeAnimatorCollisionResponse_setAnimateTarget(self.c_pointer, enable)
	def getAnimateTarget(self):
		return ISceneNodeAnimatorCollisionResponse_getAnimateTarget(self.c_pointer)
	def setEllipsoidTranslation(self, translation):
		ISceneNodeAnimatorCollisionResponse_setEllipsoidTranslation(self.c_pointer, translation.c_pointer)
	def getEllipsoidTranslation(self):
		return vector3df(ISceneNodeAnimatorCollisionResponse_getEllipsoidTranslation(self.c_pointer), True)
	def setWorld(self, newWorld):
		ISceneNodeAnimatorCollisionResponse_setWorld(self.c_pointer, newWorld.c_pointer)
	def getWorld(self):
		return ITriangleSelector(ISceneNodeAnimatorCollisionResponse_getWorld(self.c_pointer))
	def setTargetNode(self, node):
		ISceneNodeAnimatorCollisionResponse_setTargetNode(self.c_pointer, node.c_pointer)
	def getTargetNode(self):
		return ISceneNode(ISceneNodeAnimatorCollisionResponse_getTargetNode(self.c_pointer))
	def collisionOccurred(self):
		return ISceneNodeAnimatorCollisionResponse_collisionOccurred(self.c_pointer)
	def getCollisionPoint(self):
		return vector3df(ISceneNodeAnimatorCollisionResponse_getCollisionPoint(self.c_pointer))
	def getCollisionTriangle(self):
		return triangle3df(ISceneNodeAnimatorCollisionResponse_getCollisionTriangle(self.c_pointer))
	def getCollisionResultPosition(self):
		return vector3df(ISceneNodeAnimatorCollisionResponse_getCollisionResultPosition(self.c_pointer))
	def getCollisionNode(self):
		return ISceneNode(ISceneNodeAnimatorCollisionResponse_getCollisionNode(self.c_pointer))
	def setCollisionCallback(self, callback):
		ISceneNodeAnimatorCollisionResponse_setCollisionCallback(self.c_pointer, callback.c_pointer)

class ISceneNodeList:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = True
		if len(args) > 0:
			self.c_pointer = args[0]
		elif 'other' in kwargs:
			self.c_pointer = ISceneNodeList_ctor(kwargs.pop('other', None))
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def __del__(self):
		if self.c_pointer and self.delete_c_pointer:
			try:
				ISceneNodeList_delete(self.c_pointer)
			except:
				pass
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return ISceneNode(ISceneNodeList_get_item(self.c_pointer, key))
	def __setitem__(self, key, value):
		self.__getitem__(key).c_pointer = value.c_pointer
	def __iter__(self):
		return self
	def size(self):
		return ISceneNodeList_size(self.c_pointer)
	def clear(self):
		ISceneNodeList_clear(self.c_pointer)
	def empty(self):
		return ISceneNodeList_empty(self.c_pointer)
	def push_back(self, element):
		ISceneNodeList_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		ISceneNodeList_push_front(self.c_pointer, element.c_pointer)
	def first(self):
		return ISceneNode(ISceneNodeList_first(self.c_pointer))
	def next(self, from_first = False):
		result = ISceneNodeList_next(self.c_pointer, from_first)
		if not result:
			raise StopIteration
		return ISceneNode(result)
	def last(self):
		return ISceneNode(ISceneNodeList_last(self.c_pointer))

class ISceneNodeAnimatorList:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return ISceneNodeAnimator(ISceneNodeAnimatorList_get_item(self.c_pointer, key))
	def __setitem__(self, key, value):
		self.__getitem__(key).c_pointer = value.c_pointer
	def __iter__(self):
		return self
	def size(self):
		return ISceneNodeAnimatorList_size(self.c_pointer)
	def clear(self):
		ISceneNodeAnimatorList_clear(self.c_pointer)
	def empty(self):
		return ISceneNodeAnimatorList_empty(self.c_pointer)
	def push_back(self, element):
		ISceneNodeAnimatorList_push_back(self.c_pointer, element)
	def push_front(self, element):
		ISceneNodeAnimatorList_push_front(self.c_pointer, element)
	def first(self):
		return ISceneNodeAnimator(ISceneNodeAnimatorList_first(self.c_pointer))
	def current(self):
		return ISceneNodeAnimator(ISceneNodeAnimatorList_current(self.c_pointer))
	def next(self, from_first = False):
		result = ISceneNodeAnimatorList_next(self.c_pointer, from_first)
		if not result:
			raise StopIteration
		return ISceneNodeAnimator(result)
	def last(self):
		return ISceneNodeAnimator(ISceneNodeAnimatorList_last(self.c_pointer))

class ISceneNode(IAttributeExchangingObject):
	def __init__(self, *args, **kwargs):
		try:
			self.c_pointer = args[0]
		except:
			self.c_pointer = None
	#~ def Destructor(self):
		#~ ISceneNode_Destructor(self.c_pointer)
	def OnRegisterSceneNode(self):
		ISceneNode_OnRegisterSceneNode(self.c_pointer)
	def OnAnimate(self, timeMs):
		ISceneNode_OnAnimate(self.c_pointer, timeMs)
	def render(self):
		ISceneNode_render(self.c_pointer)
	def getName(self):
		return ISceneNode_getName(self.c_pointer)
	def setName(self, name):
		ISceneNode_setName(self.c_pointer, as_ansi(name))
	def getBoundingBox(self):
		return aabbox3df(ISceneNode_getBoundingBox(self.c_pointer))
	def getTransformedBoundingBox(self):
		return aabbox3df(c_pointer = ISceneNode_getTransformedBoundingBox(self.c_pointer))
	def getAbsoluteTransformation(self):
		return matrix4(ISceneNode_getAbsoluteTransformation(self.c_pointer))
	def getRelativeTransformation(self):
		return matrix4(c_pointer = ISceneNode_getRelativeTransformation(self.c_pointer))
	def isVisible(self):
		return ISceneNode_isVisible(self.c_pointer)
	def isTrulyVisible(self):
		return ISceneNode_isTrulyVisible(self.c_pointer)
	def setVisible(self, isVisible = True):
		ISceneNode_setVisible(self.c_pointer, isVisible)
	def getID(self):
		return ISceneNode_getID(self.c_pointer)
	def setID(self, id_value = -1):
		ISceneNode_setID(self.c_pointer, id_value)
	def addChild(self, child):
		ISceneNode_addChild(self.c_pointer, child.c_pointer)
	def removeChild(self, child):
		return ISceneNode_removeChild(self.c_pointer, child.c_pointer)
	def removeAll(self):
		ISceneNode_removeAll(self.c_pointer)
	def remove(self):
		ISceneNode_remove(self.c_pointer)
	def addAnimator(self, node_animator):
		ISceneNode_addAnimator(self.c_pointer, node_animator.c_pointer)
	def getAnimators(self):
		return ISceneNodeAnimatorList(ISceneNode_getAnimators(self.c_pointer))
	def removeAnimator(self, animator):
		ISceneNode_removeAnimator(self.c_pointer, animator.c_pointer)
	def removeAnimators(self):
		ISceneNode_removeAnimators(self.c_pointer)
	def getMaterial(self, num):
		return SMaterial(ISceneNode_getMaterial(self.c_pointer, num))
	def setMaterial(self, material, num = 0):
		ISceneNode_setMaterial(self.c_pointer, material.c_pointer, num)
	def getMaterialCount(self):
		return ISceneNode_getMaterialCount(self.c_pointer)
	def setMaterialFlag(self, flag, newvalue = True):
		ISceneNode_setMaterialFlag(self.c_pointer, flag, newvalue)
	def setMaterialTexture(self, textureLayer, texture):
		ISceneNode_setMaterialTexture(self.c_pointer, textureLayer, texture.c_pointer)
	def setMaterialType(self, newType):
		ISceneNode_setMaterialType(self.c_pointer, newType)
	def getScale(self):
		return vector3df(ISceneNode_getScale(self.c_pointer))
	def setScale(self, scale):
		ISceneNode_setScale(self.c_pointer, scale.c_pointer)
	def getRotation(self):
		return vector3df(ISceneNode_getRotation(self.c_pointer))
	def setRotation(self, rotation):
		ISceneNode_setRotation(self.c_pointer, rotation.c_pointer)
	def getPosition(self):
		return vector3df(ISceneNode_getPosition(self.c_pointer))
	def setPosition(self, position):
		ISceneNode_setPosition(self.c_pointer, position.c_pointer)
	def getAbsolutePosition(self):
		return vector3df(ISceneNode_getAbsolutePosition(self.c_pointer))
	def setAutomaticCulling(self, state):
		ISceneNode_setAutomaticCulling(self.c_pointer, state)
	def getAutomaticCulling(self):
		return ISceneNode_getAutomaticCulling(self.c_pointer)
	def setDebugDataVisible(self, state):
		ISceneNode_setDebugDataVisible(self.c_pointer, state)
	def isDebugDataVisible(self):
		return ISceneNode_isDebugDataVisible(self.c_pointer)
	def setIsDebugObject(self, debugObject = True):
		ISceneNode_setIsDebugObject(self.c_pointer, debugObject)
	def isDebugObject(self):
		return ISceneNode_isDebugObject(self.c_pointer)
	def getChildren(self):
		return ISceneNodeList(ISceneNode_getChildren(self.c_pointer))
	def setParent(self, newParent):
		ISceneNode_setParent(self.c_pointer, newParent.c_pointer)
	def getTriangleSelector(self):
		return ISceneNode_getTriangleSelector(self.c_pointer)
	def setTriangleSelector(self, selector):
		ISceneNode_setTriangleSelector(self.c_pointer, selector.c_pointer)
	def updateAbsolutePosition(self):
		ISceneNode_updateAbsolutePosition(self.c_pointer)
	def getParent(self):
		return ISceneNode(ISceneNode_getParent(self.c_pointer))
	def getType(self):
		return ISceneNode_getType(self.c_pointer)
	def serializeAttributes(self, out_IAttributes, options = 0):
		ISceneNode_serializeAttributes(self.c_pointer, out_IAttributes.c_pointer, options)
	def deserializeAttributes(self, in_IAttributes, options = 0):
		ISceneNode_deserializeAttributes(self.c_pointer, in_IAttributes.c_pointer, options)
	def clone(self, newParent = 0, newManager = 0):
		if not isinstance(newParent, ISceneNode):
			newParent = ISceneNode(0)
		if not isinstance(newManager, ISceneManager):
			newManager = ISceneManager(0)
		return ISceneNode_clone(self.c_pointer, newParent.c_pointer, newManager.c_pointer)
	def getSceneManager(self):
		return ISceneManager(ISceneNode_getSceneManager(self.c_pointer))

class IBoneSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = args[0]
		elif len(args) > 1:
			self.c_pointer = ctor(*args, **kwargs)
	def ctor(self, parent, mgr, id = -1):
		return IBoneSceneNode_ctor(parent.c_pointer, mgr.c_pointer, id)
	if IRRLICHT_VERSION < 180:
		def getBoneName(self):
			return IBoneSceneNode_getBoneName(self.c_pointer)
	def getBoneIndex(self):
		return IBoneSceneNode_getBoneIndex(self.c_pointer)
	def setAnimationMode(self, mode):
		return IBoneSceneNode_setAnimationMode(self.c_pointer, mode)
	def getAnimationMode(self):
		return IBoneSceneNode_getAnimationMode(self.c_pointer)
	def getBoundingBox(self):
		return aabbox3df(IBoneSceneNode_getBoundingBox(self.c_pointer))
	def OnAnimate(self, timeMs):
		IBoneSceneNode_OnAnimate(self.c_pointer, timeMs)
	def render(self):
		IBoneSceneNode_render(self.c_pointer)
	def setSkinningSpace(self, space):
		IBoneSceneNode_setSkinningSpace(self.c_pointer, space)
	def getSkinningSpace(self):
		return IBoneSceneNode_getSkinningSpace(self.c_pointer)
	def updateAbsolutePositionOfAllChildren(self):
		IBoneSceneNode_updateAbsolutePositionOfAllChildren(self.c_pointer)
	def set_positionHint(self, value):
		IBoneSceneNode_set_positionHint(self.c_pointer, value)
	def get_positionHint(self):
		return IBoneSceneNode_get_positionHint(self.c_pointer)
	def set_scaleHint(self, value):
		IBoneSceneNode_set_scaleHint(self.c_pointer, value)
	def get_scaleHint(self):
		return IBoneSceneNode_get_scaleHint(self.c_pointer)
	def set_rotationHint(self, value):
		IBoneSceneNode_set_rotationHint(self.c_pointer, value)
	def get_rotationHint(self):
		return IBoneSceneNode_get_rotationHint(self.c_pointer)

class CustomSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = self.ctor(*args, **kwargs)
		self.callback_OnRegisterSceneNode = func_OnRegisterSceneNode(self.OnRegisterSceneNode)
		CustomSceneNode_set_OnRegisterSceneNode(self.c_pointer, self.callback_OnRegisterSceneNode)
		self.callback_render = func_render(self.render)
		CustomSceneNode_set_render(self.c_pointer, self.callback_render)
		self.callback_getBoundingBox = func_getBoundingBox(self.getBoundingBox)
		CustomSceneNode_set_getBoundingBox(self.c_pointer, self.callback_getBoundingBox)
		self.callback_getMaterial = func_getMaterial(self.getMaterial)
		CustomSceneNode_set_getMaterial(self.c_pointer, self.callback_getMaterial)
		self.callback_getMaterialCount = func_getMaterialCount(self.getMaterialCount)
		CustomSceneNode_set_getMaterialCount(self.c_pointer, self.callback_getMaterialCount)
	def ctor(self, parent, mgr, id = -1):
		return CustomSceneNode_ctor(parent.c_pointer, mgr.c_pointer, id)
	def __del__(self):
		if self.c_pointer:
			try:
				CustomSceneNode_delete(self.c_pointer)
			except:
				pass
	def OnRegisterSceneNode(self):
		'must be replaced with user class'
	def render(self):
		'must be replaced with user class'
	def getBoundingBox(self):
		'must be replaced with user class'
	def getMaterial(self, num = 0):
		'must be replaced with user class'
	def getMaterialCount(self):
		'must be replaced with user class'

class IParticleSystemSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 1:
			self.c_pointer = args[0]
		elif len(args) > 1:
			self.c_pointer = self.ctor(*args)
	def ctor(self, parent, mgr, id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		return IParticleSystemSceneNode_ctor(parent.c_pointer, mgr.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer)
	def setParticleSize(self, size = dimension2df(5.0, 5.0)):
		IParticleSystemSceneNode_setParticleSize(self.c_pointer, size.c_pointer)
	def setParticlesAreGlobal(self, _global_ = True):
		IParticleSystemSceneNode_setParticlesAreGlobal(self.c_pointer, _global_)
	def getEmitter(self):
		return IParticleEmitter(IParticleSystemSceneNode_getEmitter(self.c_pointer))
	def setEmitter(self, emitter):
		IParticleSystemSceneNode_setEmitter(self.c_pointer, emitter.c_pointer)
	def addAffector(self, affector):
		IParticleSystemSceneNode_addAffector(self.c_pointer, affector.c_pointer)
	def removeAllAffectors(self):
		IParticleSystemSceneNode_removeAllAffectors(self.c_pointer)
	def createAnimatedMeshSceneNodeEmitter(self, node, useNormalDirection = True, direction = vector3df(0.0,0.03,0.0), normalDirectionModifier = 100.0, mbNumber = -1, everyMeshVertex = False, minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleAnimatedMeshSceneNodeEmitter(IParticleSystemSceneNode_createAnimatedMeshSceneNodeEmitter(self.c_pointer, node.c_pointer, useNormalDirection, direction.c_pointer, normalDirectionModifier, mbNumber, everyMeshVertex, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createBoxEmitter(self, box = aabbox3df(-10,28,-10,10,30,10), direction = vector3df(0.0,0.03,0.0), minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleBoxEmitter(IParticleSystemSceneNode_createBoxEmitter(self.c_pointer, box.c_pointer, direction.c_pointer, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createCylinderEmitter(self, center, radius, normal, length, outlineOnly = False, direction = vector3df(0.0,0.03,0.0), minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleCylinderEmitter(IParticleSystemSceneNode_createCylinderEmitter(self.c_pointer, center.c_pointer, radius, normal.c_pointer, length, outlineOnly, direction.c_pointer, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createMeshEmitter(self, mesh, useNormalDirection = True, direction = vector3df(0.0,0.03,0.0), normalDirectionModifier = 100.0, mbNumber = -1, everyMeshVertex = False, minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleMeshEmitter(IParticleSystemSceneNode_createMeshEmitter(self.c_pointer, mesh.c_pointer, useNormalDirection, direction.c_pointer, normalDirectionModifier, mbNumber, everyMeshVertex, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createPointEmitter(self, direction = vector3df(0.0,0.03,0.0), minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticlePointEmitter(IParticleSystemSceneNode_createPointEmitter(self.c_pointer, direction.c_pointer, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createRingEmitter(self, center, radius, ringThickness, direction = vector3df(0.0,0.03,0.0), minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleRingEmitter(IParticleSystemSceneNode_createRingEmitter(self.c_pointer, center.c_pointer, radius, ringThickness, direction.c_pointer, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createSphereEmitter(self, center, radius, direction = vector3df(0.0,0.03,0.0), minParticlesPerSecond = 5, maxParticlesPerSecond = 10, minStartColor = SColor(255,0,0,0), maxStartColor = SColor(255,255,255,255), lifeTimeMin = 2000, lifeTimeMax = 4000, maxAngleDegrees = 0, minStartSize = dimension2df(5.0,5.0), maxStartSize = dimension2df(5.0,5.0)):
		return IParticleSphereEmitter(IParticleSystemSceneNode_createSphereEmitter(self.c_pointer, center.c_pointer, radius, direction.c_pointer, minParticlesPerSecond, maxParticlesPerSecond, minStartColor.c_pointer, maxStartColor.c_pointer, lifeTimeMin, lifeTimeMax, maxAngleDegrees, minStartSize.c_pointer, maxStartSize.c_pointer))
	def createAttractionAffector(self, point, speed = 1.0, attract = True, affectX = True, affectY = True, affectZ = True):
		return IParticleAttractionAffector(IParticleSystemSceneNode_createAttractionAffector(self.c_pointer, point.c_pointer, speed, attract, affectX, affectY, affectZ))
	def createScaleParticleAffector(self, scaleTo = dimension2df(1.0, 1.0)):
		return IParticleAffector(IParticleSystemSceneNode_createScaleParticleAffector(self.c_pointer, scaleTo.c_pointer))
	def createFadeOutParticleAffector(self, targetColor = SColor(0,0,0,0), timeNeededToFadeOut = 1000):
		return IParticleFadeOutAffector(IParticleSystemSceneNode_createFadeOutParticleAffector(self.c_pointer, targetColor.c_pointer, timeNeededToFadeOut))
	def createGravityAffector(self, gravity = vector3df(0.0,-0.03,0.0), timeForceLost = 1000):
		return IParticleGravityAffector(IParticleSystemSceneNode_createGravityAffector(self.c_pointer, gravity.c_pointer, timeForceLost))
	def createRotationAffector(self, speed = vector3df(5.0,5.0,5.0), pivotPoint = vector3df(0.0,0.0,0.0)):
		return IParticleRotationAffector(IParticleSystemSceneNode_createRotationAffector(self.c_pointer, speed.c_pointer, pivotPoint.c_pointer))

if BUILD_WITH_GRID_SCENE_NODE:
	class CGridSceneNode(ISceneNode):
		def __init__(self, *args, **kwargs):
			self.c_pointer = None
			if len(args) == 1:
				self.c_pointer = args[0]
			elif len(args) > 1 or len(kwargs) > 1:
				self.c_pointer = self.Constructor(*args, **kwargs)
		def __del__(self):
			if self.c_pointer:
				try:
					CGridSceneNode_delete(self.c_pointer)
				except:
					pass
		def Constructor(self, parent, smgr, id = -1, spacing = 8, size = 1024, gridcolor = SColor(255,128,128,128), accentlineoffset = 8, accentgridcolor = SColor(255,192,192,192), axislinestate = False):
			return CGridSceneNode_ctor(parent.c_pointer, smgr.c_pointer, id, spacing, size, gridcolor.c_pointer, accentlineoffset, accentgridcolor.c_pointer, axislinestate)
		def clone(self, newParent = 0, newSceneManager = 0):
			return CGridSceneNode(CGridSceneNode_clone(self.c_pointer, newParent, newSceneManager))
		def OnRegisterSceneNode(self):
			CGridSceneNode_OnRegisterSceneNode(self.c_pointer)
		def render(self):
			CGridSceneNode_render(self.c_pointer)
		def getBoundingBox(self):
			return aabbox3df(CGridSceneNode_getBoundingBox(self.c_pointer))
		def getMaterialCount(self):
			return CGridSceneNode_getMaterialCount(self.c_pointer)
		def getMaterial(self, i):
			return SMaterial(CGridSceneNode_getMaterial(self.c_pointer, i))
		def RegenerateGrid(self):
			CGridSceneNode_RegenerateGrid(self.c_pointer)
		def GetSpacing(self):
			return CGridSceneNode_GetSpacing(self.c_pointer)
		def GetSize(self):
			return CGridSceneNode_GetSize(self.c_pointer)
		def GetGridColor(self):
			return SColor(CGridSceneNode_GetGridColor(self.c_pointer))
		def GetAccentlineOffset(self):
			return CGridSceneNode_GetAccentlineOffset(self.c_pointer)
		def GetAccentlineColor(self):
			return SColor(CGridSceneNode_GetAccentlineColor(self.c_pointer))
		def AreAxisLineActive(self):
			return CGridSceneNode_AreAxisLineActive(self.c_pointer)
		def GetAxisLineXColor(self):
			return SColor(CGridSceneNode_GetAxisLineXColor(self.c_pointer))
		def GetAxisLineZColor(self):
			return SColor(CGridSceneNode_GetAxisLineZColor(self.c_pointer))
		def SetSpacing(self, newspacing):
			CGridSceneNode_SetSpacing(self.c_pointer, newspacing)
		def SetSize(self, newsize):
			CGridSceneNode_SetSize(self.c_pointer, newsize)
		def SetGridColor(self, newcolor):
			CGridSceneNode_SetGridColor(self.c_pointer, newcolor.c_pointer)
		def SetAccentlineOffset(self, newoffset):
			CGridSceneNode_SetAccentlineOffset(self.c_pointer, newoffset)
		def SetAccentlineColor(self, newcolor):
			CGridSceneNode_SetAccentlineColor(self.c_pointer, newcolor.c_pointer)
		def SetAxisLineActive(self, active):
			CGridSceneNode_SetAxisLineActive(self.c_pointer, active)
		def SetAxisLineXColor(self, XLine):
			CGridSceneNode_SetAxisLineXColor(self.c_pointer, XLine.c_pointer)
		def SetAxisLineZColor(self, ZLine):
			CGridSceneNode_SetAxisLineZColor(self.c_pointer, ZLine.c_pointer)
		def SetMaterial(self, newMaterial):
			CGridSceneNode_SetMaterial(self.c_pointer, newMaterial.c_pointer)

class IMeshSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def setMesh(self, mesh):
		IMeshSceneNode_setMesh(self.c_pointer, mesh.c_pointer)
	def getMesh(self):
		return IMesh(IMeshSceneNode_getMesh(self.c_pointer))
	def setReadOnlyMaterials(self, readonly = True):
		IMeshSceneNode_setReadOnlyMaterials(self.c_pointer, readonly)
	def isReadOnlyMaterials(self):
		return IMeshSceneNode_isReadOnlyMaterials(self.c_pointer)

class IBillboardSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def setSize(self, size):
		IBillboardSceneNode_setSize(self.c_pointer, size.c_pointer)
	def getSize(self):
		return dimension2d(IBillboardSceneNode_getSize(self.c_pointer))
	def setColor(self, overallColor):
		IBillboardSceneNode_setColor(self.c_pointer, overallColor.c_pointer)
	def setColor2(self, topColor, bottomColor):
		IBillboardSceneNode_setColor2(self.c_pointer, topColor.c_pointer, bottomColor.c_pointer)
	def getColor(self, topColor, bottomColor):
		IBillboardSceneNode_getColor(self.c_pointer, topColor.c_pointer, bottomColor.c_pointer)

class IBillboardTextSceneNode(IBillboardSceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setSize(self, size):
		IBillboardTextSceneNode_setSize(self.c_pointer, size.c_pointer)
	def getSize(self):
		return IBillboardTextSceneNode_getSize(self.c_pointer)
	def setColor1(self, overallColor):
		IBillboardTextSceneNode_setColor1(self.c_pointer, overallColor.c_pointer)
	def setColor2(self, topColor, bottomColor):
		IBillboardTextSceneNode_setColor2(self.c_pointer, topColor.c_pointer, bottomColor.c_pointer)
	def getColor(self, topColor, bottomColor):
		IBillboardTextSceneNode_getColor(self.c_pointer, topColor.c_pointer, bottomColor.c_pointer)
	def setText(self, text):
		IBillboardTextSceneNode_setText(self.c_pointer, text)
	def setTextColor(self, color):
		IBillboardTextSceneNode_setTextColor(self.c_pointer, color.c_pointer)

class ILightSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def setLightData(self, light):
		ILightSceneNode_setLightData(self.c_pointer, light)
	def getLightData(self):
		return ILightSceneNode_getLightData(self.c_pointer)[0]
	def setVisible(self, isVisible):
		ILightSceneNode_setVisible(self.c_pointer, isVisible)
	def setRadius(self, radius):
		ILightSceneNode_setRadius(self.c_pointer, radius)
	def getRadius(self):
		return ILightSceneNode_getRadius(self.c_pointer)
	def setLightType(self, type):
		ILightSceneNode_setLightType(self.c_pointer, type)
	def getLightType(self):
		return ILightSceneNode_getLightType(self.c_pointer)
	def enableCastShadow(self, shadow=True):
		ILightSceneNode_enableCastShadow(self.c_pointer, shadow)
	def getCastShadow(self):
		return ILightSceneNode_getCastShadow(self.c_pointer)

class ICameraSceneNode(ISceneNode, IEventReceiver):
	def __init__(self, *args, **kwargs):
		IEventReceiver.__init__(self)
		self.c_pointer = ICameraSceneNode_ctor(args[0])
	#~ def Destructor(self):
		#~ ICameraSceneNode_Destructor(self.c_pointer)
	def set_func_event(self, event_func):
		ICameraSceneNode_set_func_event(self.c_pointer, event_func)
	def OnEvent(self, event):
		'must be replaced with custom CameraSceneNode class'
		return False
	def convert_pointer(self):
		self.c_pointer = ICameraSceneNode_ctor(self.c_pointer)
	def setProjectionMatrix(self, projection, isOrthogonal=False):
		ICameraSceneNode_setProjectionMatrix(self.c_pointer, projection.c_pointer, isOrthogonal)
	def getProjectionMatrix(self):
		return matrix4(ICameraSceneNode_getProjectionMatrix(self.c_pointer))
	def getViewMatrix(self):
		return matrix4(ICameraSceneNode_getViewMatrix(self.c_pointer))
	def setViewMatrixAffector(self, affector):
		ICameraSceneNode_setViewMatrixAffector(self.c_pointer, affector.c_pointer)
	def getViewMatrixAffector(self):
		return matrix4(ICameraSceneNode_getViewMatrixAffector(self.c_pointer))
	def setTarget(self, pos):
		ICameraSceneNode_setTarget(self.c_pointer, pos.c_pointer)
	def setRotation(self, rotation):
		ICameraSceneNode_setRotation(self.c_pointer, rotation.c_pointer)
	def getTarget(self):
		return vector3df(ICameraSceneNode_getTarget(self.c_pointer))
	def setUpVector(self, pos):
		ICameraSceneNode_setUpVector(self.c_pointer, pos.c_pointer)
	def getUpVector(self):
		return vector3df(ICameraSceneNode_getUpVector(self.c_pointer))
	def getNearValue(self):
		return ICameraSceneNode_getNearValue(self.c_pointer)
	def getFarValue(self):
		return ICameraSceneNode_getFarValue(self.c_pointer)
	def getAspectRatio(self):
		return ICameraSceneNode_getAspectRatio(self.c_pointer)
	def getFOV(self):
		return ICameraSceneNode_getFOV(self.c_pointer)
	def setNearValue(self, zn):
		ICameraSceneNode_setNearValue(self.c_pointer, zn)
	def setFarValue(self, zf):
		ICameraSceneNode_setFarValue(self.c_pointer, zf)
	def setAspectRatio(self, aspect):
		ICameraSceneNode_setAspectRatio(self.c_pointer, aspect)
	def setFOV(self, fovy):
		ICameraSceneNode_setFOV(self.c_pointer, fovy)
	def getViewFrustum(self):
		return SViewFrustum(ICameraSceneNode_getViewFrustum(self.c_pointer))
	def setInputReceiverEnabled(self, enabled):
		ICameraSceneNode_setInputReceiverEnabled(self.c_pointer, enabled)
	def isInputReceiverEnabled(self):
		return ICameraSceneNode_isInputReceiverEnabled(self.c_pointer)
	def isOrthogonal(self):
		return ICameraSceneNode_isOrthogonal(self.c_pointer)
	def bindTargetAndRotation(self, bound):
		ICameraSceneNode_bindTargetAndRotation(self.c_pointer, bound)
	def getTargetAndRotationBinding(self):
		return ICameraSceneNode_getTargetAndRotationBinding(self.c_pointer)

class ISceneCollisionManager(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getCollisionPoint(self, ray, selector, outCollisionPoint, outTriangle, outNode):
		return ISceneCollisionManager_getCollisionPoint(self.c_pointer, ray.c_pointer, selector.c_pointer, outCollisionPoint.c_pointer, outTriangle.c_pointer, outNode.c_pointer)
	def getCollisionResultPosition(self, selector, ellipsoidPosition, ellipsoidRadius, ellipsoidDirectionAndSpeed, triout, hitPosition, outFalling, outNode, slidingSpeed = 0.0005, gravityDirectionAndSpeed = vector3df(0.0, 0.0, 0.0)):
		return vector3df(ISceneCollisionManager_getCollisionResultPosition(self.c_pointer, selector.c_pointer, ellipsoidPosition.c_pointer, ellipsoidRadius.c_pointer, ellipsoidDirectionAndSpeed.c_pointer, triout.c_pointer, hitPosition.c_pointer, outFalling, outNode.c_pointer, slidingSpeed, gravityDirectionAndSpeed.c_pointer))
	def getRayFromScreenCoordinates(self, pos, camera = ICameraSceneNode(0)):
		return line3df(ISceneCollisionManager_getRayFromScreenCoordinates(self.c_pointer, pos.c_pointer, camera.c_pointer))
	def getScreenCoordinatesFrom3DPosition(self, pos, camera = ICameraSceneNode(0)):
		return position2di(c_pointer = ISceneCollisionManager_getScreenCoordinatesFrom3DPosition(self.c_pointer, pos.c_pointer, camera.c_pointer))
	def getSceneNodeFromScreenCoordinatesBB(self, pos, idBitMask = 0, bNoDebugObjects = False, root = ISceneNode(0)):
		return ISceneNode(ISceneCollisionManager_getSceneNodeFromScreenCoordinatesBB(self.c_pointer, pos.c_pointer, idBitMask, bNoDebugObjects, root.c_pointer))
	def getSceneNodeFromRayBB(self, ray, idBitMask = 0, bNoDebugObjects = False, root = ISceneNode(0)):
		return ISceneNode(ISceneCollisionManager_getSceneNodeFromRayBB(self.c_pointer, ray.c_pointer, idBitMask, bNoDebugObjects, root.c_pointer))
	def getSceneNodeFromCameraBB(self, camera, idBitMask = 0, bNoDebugObjects = False):
		return ISceneNode(ISceneCollisionManager_getSceneNodeFromCameraBB(self.c_pointer, camera.c_pointer, idBitMask, bNoDebugObjects))
	def getSceneNodeAndCollisionPointFromRay(self, ray, outCollisionPoint, outTriangle, idBitMask = 0, collisionRootNode = ISceneNode(0), noDebugObjects = False):
		#~ if isinstance(collisionRootNode, int):
			#~ collisionRootNode = ISceneNode(0)
		return ISceneNode(ISceneCollisionManager_getSceneNodeAndCollisionPointFromRay(self.c_pointer, ray.c_pointer, outCollisionPoint.c_pointer, outTriangle.c_pointer, idBitMask, collisionRootNode.c_pointer, noDebugObjects))

class ISceneNodeAnimatorFactory(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def createSceneNodeAnimator1(self, type, target):
		return ISceneNodeAnimator(ISceneNodeAnimatorFactory_createSceneNodeAnimator1(self.c_pointer, type, target.c_pointer))
	def createSceneNodeAnimator2(self, typeName, target):
		return ISceneNodeAnimator(ISceneNodeAnimatorFactory_createSceneNodeAnimator2(self.c_pointer, typeName, target.c_pointer))
	def createSceneNodeAnimator(self, type_or_typeName, target):
		if isinstance(type_or_typeName, int):
			return self.createSceneNodeAnimator1(type_or_typeName, target)
		else:
			return self.createSceneNodeAnimator2(type_or_typeName, target)
	def getCreatableSceneNodeAnimatorTypeCount(self):
		return ISceneNodeAnimatorFactory_getCreatableSceneNodeAnimatorTypeCount(self.c_pointer)
	def getCreateableSceneNodeAnimatorType(self, idx):
		return ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorType(self.c_pointer, idx)
	def getCreateableSceneNodeAnimatorTypeName1(self, idx):
		return ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1(self.c_pointer, idx)
	def getCreateableSceneNodeAnimatorTypeName2(self, _type_):
		return ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2(self.c_pointer, _type_)
	def getCreateableSceneNodeAnimatorTypeName(self, arg):
		try:
			return self.getCreateableSceneNodeAnimatorTypeName2(arg)
		except:
			return self.getCreateableSceneNodeAnimatorTypeName1(arg)
	def name_from_index(self, idx):
		return self.getCreateableSceneNodeAnimatorTypeName1(idx)
	def name_from_type(self, _type_):
		return self.getCreateableSceneNodeAnimatorTypeName2(_type_)

class ISceneNodeFactory(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def addSceneNode1(self, type, parent = ISceneNode(0)):
		return ISceneNodeFactory_addSceneNode1(self.c_pointer, type, parent.c_pointer)
	def addSceneNode2(self, typeName, parent = ISceneNode(0)):
		return ISceneNodeFactory_addSceneNode2(self.c_pointer, typeName, parent.c_pointer)
	def addSceneNode(self, type_or_typeName, parent = ISceneNode(0)):
		if isinstance(type_or_typeName, int):
			return self.addSceneNode1(type_or_typeName, parent)
		else:
			return self.addSceneNode2(type_or_typeName, parent)
	def getCreatableSceneNodeTypeCount(self):
		return ISceneNodeFactory_getCreatableSceneNodeTypeCount(self.c_pointer)
	def getCreateableSceneNodeType(self, idx):
		return ISceneNodeFactory_getCreateableSceneNodeType(self.c_pointer, idx)
	def getCreateableSceneNodeTypeName1(self, idx):
		return ISceneNodeFactory_getCreateableSceneNodeTypeName1(self.c_pointer, idx)
	def getCreateableSceneNodeTypeName2(self, _type_):
		return ISceneNodeFactory_getCreateableSceneNodeTypeName2(self.c_pointer, _type_)
	def getCreateableSceneNodeTypeName(self, arg):
		try:
			return self.getCreateableSceneNodeTypeName2(arg)
		except:
			return self.getCreateableSceneNodeTypeName1(arg)
	def name_from_index(self, idx):
		return self.getCreateableSceneNodeTypeName1(idx)
	def name_from_type(self, _type_):
		return self.getCreateableSceneNodeTypeName2(_type_)

class D3D8(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def get_D3D8(self):
		return D3D8_get_D3D8(self.c_pointer)
	def get_D3DDev8(self):
		return D3D8_get_D3DDev8(self.c_pointer)
	def get_HWnd(self):
		return D3D8_get_HWnd(self.c_pointer)
	def set_D3D8(self, value):
		D3D8_set_D3D8(self.c_pointer, value)
	def set_D3DDev8(self, value):
		D3D8_set_D3DDev8(self.c_pointer, value)
	def set_HWnd(self, value):
		D3D8_set_HWnd(self.c_pointer, value)
	D3D8 = property(get_D3D8, set_D3D8)
	D3DDev8 = property(get_D3DDev8, set_D3DDev8)
	HWnd = property(get_HWnd, set_HWnd)

class D3D9(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def get_D3D9(self):
		return D3D9_get_D3D9(self.c_pointer)
	def get_D3DDev9(self):
		return D3D9_get_D3DDev9(self.c_pointer)
	def get_HWnd(self):
		return D3D9_get_HWnd(self.c_pointer)
	def set_D3D9(self, value):
		D3D9_set_D3D9(self.c_pointer, value)
	def set_D3DDev9(self, value):
		D3D9_set_D3DDev9(self.c_pointer, value)
	def set_HWnd(self, value):
		D3D9_set_HWnd(self.c_pointer, value)
	D3D9 = property(get_D3D9, set_D3D9)
	D3DDev9 = property(get_D3DDev9, set_D3DDev9)
	HWnd = property(get_HWnd, set_HWnd)

class OpenGLWin32(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def get_HDc(self):
		return OpenGLWin32_get_HDc(self.c_pointer)
	def get_HRc(self):
		return OpenGLWin32_get_HRc(self.c_pointer)
	def get_HWnd(self):
		return OpenGLWin32_get_HWnd(self.c_pointer)
	def set_HDc(self, value):
		OpenGLWin32_set_HDc(self.c_pointer, value)
	def set_HRc(self, value):
		OpenGLWin32_set_HRc(self.c_pointer, value)
	def set_HWnd(self, value):
		OpenGLWin32_set_HWnd(self.c_pointer, value)
	HDc = property(get_HDc, set_HDc)
	HRc = property(get_HRc, set_HRc)
	HWnd = property(get_HWnd, set_HWnd)

class OpenGLLinux(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def get_X11Display(self):
		return OpenGLLinux_get_X11Display(self.c_pointer)
	def get_X11Context(self):
		return OpenGLLinux_get_X11Context(self.c_pointer)
	def get_X11Window(self):
		return OpenGLLinux_get_X11Window(self.c_pointer)
	def set_X11Display(self, value):
		OpenGLLinux_set_X11Display(self.c_pointer, value)
	def set_X11Context(self, value):
		OpenGLLinux_set_X11Context(self.c_pointer, value)
	def set_X11Window(self, value):
		OpenGLLinux_set_X11Window(self.c_pointer, value)
	X11Display = property(get_X11Display, set_X11Display)
	X11Context = property(get_X11Context, set_X11Context)
	X11Window = property(get_X11Window, set_X11Window)

class SExposedVideoData(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0:
			self.c_pointer = SExposedVideoData_ctor1()
		elif len(args) > 0:
			self.c_pointer = args[0]
		elif 'Window' in kwargs:
			self.c_pointer = SExposedVideoData_ctor2(kwargs.pop('Window'))
	#~ def destructor(self):
		#~ SExposedVideoData_destructor(self.c_pointer)
	def get_D3D8(self):
		return D3D8(SExposedVideoData_get_D3D8(self.c_pointer))
	def get_D3D8_D3D8(self):
		return SExposedVideoData_get_D3D8_D3D8(self.c_pointer)
	def get_D3D8_D3DDev8(self):
		return SExposedVideoData_get_D3D8_D3DDev8(self.c_pointer)
	def get_D3D8_HWnd(self):
		return SExposedVideoData_get_D3D8_HWnd(self.c_pointer)
	def get_D3D9(self):
		return D3D9(SExposedVideoData_get_D3D9(self.c_pointer))
	def get_D3D9_D3D9(self):
		return SExposedVideoData_get_D3D9_D3D9(self.c_pointer)
	def get_D3D9_D3DDev9(self):
		return SExposedVideoData_get_D3D9_D3DDev9(self.c_pointer)
	def get_D3D9_HWnd(self):
		return SExposedVideoData_get_D3D9_HWnd(self.c_pointer)
	def get_OpenGLWin32(self):
		return OpenGLWin32(SExposedVideoData_get_OpenGLWin32(self.c_pointer))
	def get_OpenGLWin32_HDc(self):
		return SExposedVideoData_get_OpenGLWin32_HDc(self.c_pointer)
	def get_OpenGLWin32_HRc(self):
		return SExposedVideoData_get_OpenGLWin32_HRc(self.c_pointer)
	def get_OpenGLWin32_HWnd(self):
		return SExposedVideoData_get_OpenGLWin32_HWnd(self.c_pointer)
	def get_OpenGLLinux(self):
		return OpenGLLinux(SExposedVideoData_get_OpenGLLinux(self.c_pointer))
	def get_OpenGLLinux_X11Display(self):
		return SExposedVideoData_get_OpenGLLinux_X11Display(self.c_pointer)
	def get_OpenGLLinux_X11Context(self):
		return SExposedVideoData_get_OpenGLLinux_X11Context(self.c_pointer)
	def get_OpenGLLinux_X11Window(self):
		return SExposedVideoData_get_OpenGLLinux_X11Window(self.c_pointer)
	def set_D3D8_D3D8(self, value):
		SExposedVideoData_set_D3D8_D3D8(self.c_pointer, value)
	def set_D3D8_D3DDev8(self, value):
		SExposedVideoData_set_D3D8_D3DDev8(self.c_pointer, value)
	def set_D3D8_HWnd(self, value):
		SExposedVideoData_set_D3D8_HWnd(self.c_pointer, value)
	def set_D3D9_D3D9(self, value):
		SExposedVideoData_set_D3D9_D3D9(self.c_pointer, value)
	def set_D3D9_D3DDev9(self, value):
		SExposedVideoData_set_D3D9_D3DDev9(self.c_pointer, value)
	def set_D3D9_HWnd(self, value):
		SExposedVideoData_set_D3D9_HWnd(self.c_pointer, value)
	def set_OpenGLWin32_HDc(self, value):
		SExposedVideoData_set_OpenGLWin32_HDc(self.c_pointer, value)
	def set_OpenGLWin32_HRc(self, value):
		SExposedVideoData_set_OpenGLWin32_HRc(self.c_pointer, value)
	def set_OpenGLWin32_HWnd(self, value):
		SExposedVideoData_set_OpenGLWin32_HWnd(self.c_pointer, value)
	def set_OpenGLLinux_X11Display(self, value):
		SExposedVideoData_set_OpenGLLinux_X11Display(self.c_pointer, value)
	def set_OpenGLLinux_X11Context(self, value):
		SExposedVideoData_set_OpenGLLinux_X11Context(self.c_pointer, value)
	def set_OpenGLLinux_X11Window(self, value):
		SExposedVideoData_set_OpenGLLinux_X11Window(self.c_pointer, value)
	D3D8 = property(get_D3D8)#, set_D3D8)
	D3D9 = property(get_D3D9)#, set_D3D9)
	OpenGLWin32 = property(get_OpenGLWin32)#, set_OpenGLWin32)
	OpenGLLinux = property(get_OpenGLLinux)#, set_OpenGLLinux)

class IVideoDriver(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
		#~ OnResizeFunc = func_type(None, ctypes.c_void_p)
		#~ self.callback = OnResizeFunc(self.OnResize)
		if IRRLICHT_VERSION < 170:
			def beginScene(backBuffer = True, zBuffer = True, color = SColor(255,0,0,0), windowId = 0, sourceRect = recti(0)):
				return IVideoDriver_beginScene(self.c_pointer, backBuffer, zBuffer, color.c_pointer, windowId, sourceRect.c_pointer)
			self.beginScene = beginScene
		else:
			def beginScene(backBuffer = True, zBuffer = True, color = SColor(255,0,0,0), videoData = SExposedVideoData(), sourceRect = recti(0)):
				return IVideoDriver_beginScene(self.c_pointer, backBuffer, zBuffer, color.c_pointer, videoData.c_pointer, sourceRect.c_pointer)
			self.beginSceneFull = beginScene
	def beginSceneDefault(self, backBuffer = True, zBuffer = True, color = SColor(255,0,0,0)):
		return IVideoDriver_beginSceneDefault(self.c_pointer, backBuffer, zBuffer, color.c_pointer)
	def beginScene(self, *args, **kwargs):
		if len(args) < 4:
			return self.beginSceneDefault(*args, **kwargs)
		else:
			return self.beginSceneFull(*args, **kwargs)
	def endScene(self):
		return IVideoDriver_endScene(self.c_pointer)
	def queryFeature(self, feature):#E_VIDEO_DRIVER_FEATURE
		return IVideoDriver_queryFeature(self.c_pointer, feature)
	def disableFeature(self, feature, flag = True):
		IVideoDriver_disableFeature(self.c_pointer, feature, flag)
	if IRRLICHT_VERSION >= 180:
		def getDriverAttributes(self):
			return IAttributes(IVideoDriver_getDriverAttributes(self.c_pointer))
	def checkDriverReset(self):
		return IVideoDriver_checkDriverReset(self.c_pointer)
	def setTransform(self, state, mat):
		IVideoDriver_setTransform(self.c_pointer, state, mat.c_pointer)
	def getTransform(self, state):
		return matrix4(IVideoDriver_getTransform(self.c_pointer, state))
	def getImageLoaderCount(self):
		return IVideoDriver_getImageLoaderCount(self.c_pointer)
	def getImageLoader(self, n):
		return IImageLoader(IVideoDriver_getImageLoader(self.c_pointer, n))
	def getImageWriterCount(self):
		return IVideoDriver_getImageWriterCount(self.c_pointer)
	def getImageWriter(self, n):
		return IImageWriter(IVideoDriver_getImageWriter(self.c_pointer, n))
	def setMaterial(self, material):
		IVideoDriver_setMaterial(self.c_pointer, material.c_pointer)
	def getTexture(self, file_or_filename):
		if isinstance(file_or_filename, str):
			return self.getTexture1(as_ansi(file_or_filename))
		else:
			return self.getTexture2(file_or_filename)
	def getTexture1(self, filename):
		return ITexture(IVideoDriver_getTexture1(self.c_pointer, filename))
	def getTexture2(self, file):
		return ITexture(IVideoDriver_getTexture2(self.c_pointer, file))
	def getTextureByIndex(self, index = 0):
		return ITexture(IVideoDriver_getTextureByIndex(self.c_pointer, index))
	def getTextureCount(self):
		return IVideoDriver_getTextureCount(self.c_pointer)
	def renameTexture(self, texture, newName):
		IVideoDriver_renameTexture(self.c_pointer, texture.c_pointer, newName)
	def addTexture(self, *args):
		if isinstance(args[0], (type_str, type_unicode)):
			mipmapData = None
			if len(args) > 2:
				mipmapData = args[2]
			return self.addTexture2(fs_conv(args[0]), args[1], mipmapData)
		else:
			if len(args) == 2:
				return ITexture(IVideoDriver_addTexture1(self.c_pointer, args[0].c_pointer, args[1], ECF_A8R8G8B8))
			elif len(args) > 2:
				return ITexture(IVideoDriver_addTexture1(self.c_pointer, args[0].c_pointer, args[1], args[2]))
			else:
				print('ERROR: IVideoDriver.addTexture has not valid arguments!')
				return ITexture(0)
	def addTexture1(self, size, name, format = ECF_A8R8G8B8):
		return ITexture(IVideoDriver_addTexture1(self.c_pointer, size.c_pointer, name, format))
	def addTexture2(self, name, image, mipmapData = None):
		return ITexture(IVideoDriver_addTexture2(self.c_pointer, name, image.c_pointer, mipmapData))
	def addRenderTargetTexture(self, size, name = "rt", format = ECF_UNKNOWN):
		return ITexture(IVideoDriver_addRenderTargetTexture(self.c_pointer, size.c_pointer, name, format))
	def removeTexture(self, texture):
		IVideoDriver_removeTexture(self.c_pointer, texture.c_pointer)
	def removeAllTextures(self):
		IVideoDriver_removeAllTextures(self.c_pointer)
	def removeHardwareBuffer(self, mb):#IMeshBuffer
		IVideoDriver_removeHardwareBuffer(self.c_pointer, mb.c_pointer)
	def removeAllHardwareBuffers(self):
		IVideoDriver_removeAllHardwareBuffers(self.c_pointer)
	if IRRLICHT_VERSION >= 180:
		def addOcclusionQuery(self, node, mesh = IMesh(0)):
			IVideoDriver_addOcclusionQuery(self.c_pointer, node.c_pointer, mesh.c_pointer)
		def removeOcclusionQuery(self, node):
			IVideoDriver_removeOcclusionQuery(self.c_pointer, node.c_pointer)
		def removeAllOcclusionQueries(self):
			IVideoDriver_removeAllOcclusionQueries(self.c_pointer)
		def runOcclusionQuery(self, node, visible = False):
			IVideoDriver_runOcclusionQuery(self.c_pointer, node.c_pointer, visible)
		def runAllOcclusionQueries(self, visible = False):
			IVideoDriver_runAllOcclusionQueries(self.c_pointer, visible)
		def updateOcclusionQuery(self, node, block = True):
			IVideoDriver_updateOcclusionQuery(self.c_pointer, node.c_pointer, block)
		def updateAllOcclusionQueries(self, block = True):
			IVideoDriver_updateAllOcclusionQueries(self.c_pointer, block)
		def getOcclusionQueryResult(self, node):
			return IVideoDriver_getOcclusionQueryResult(self.c_pointer, node.c_pointer)
	def makeColorKeyTexture1(self, texture, color, zeroTexels = False):
		IVideoDriver_makeColorKeyTexture1(self.c_pointer, texture.c_pointer, color.c_pointer, zeroTexels)
	def makeColorKeyTexture2(self, texture, colorKeyPixelPos, zeroTexels = False):
		IVideoDriver_makeColorKeyTexture2(self.c_pointer, texture.c_pointer, colorKeyPixelPos.c_pointer, zeroTexels)
	def makeColorKeyTexture(self, *args, **kwargs):
		if isinstance(args[1], (SColor, SColorf)):
			self.makeColorKeyTexture1(*args, **kwargs)
		else:
			self.makeColorKeyTexture2(*args, **kwargs)
	def makeNormalMapTexture(self, texture, amplitude=1.0):
		IVideoDriver_makeNormalMapTexture(self.c_pointer, texture.c_pointer, amplitude)
	def setRenderTarget1(self, texture, clearBackBuffer=True, clearZBuffer=True, color=SColor(0,0,0,0)):
		return IVideoDriver_setRenderTarget1(self.c_pointer, texture.c_pointer, clearBackBuffer, clearZBuffer, color.c_pointer)
	def setRenderTarget2(self, target, clearTarget=True, clearZBuffer=True, color=SColor(0,0,0,0)):
		return IVideoDriver_setRenderTarget2(self.c_pointer, target, clearTarget, clearZBuffer, color.c_pointer)
	def setRenderTarget(self, *args, **kwargs):
		if isinstance(args[0], int):
			self.setRenderTarget2(*args, **kwargs)
		else:
			self.setRenderTarget1(*args, **kwargs)
	def setViewPort(self, area):
		IVideoDriver_setViewPort(self.c_pointer, area.c_pointer)
	def getViewPort(self):
		return recti(IVideoDriver_getViewPort(self.c_pointer))
	def drawVertexPrimitiveList(self, vertices, vertexCount, indexList, primCount, vType=EVT_STANDARD, pType=EPT_TRIANGLES, iType=EIT_16BIT):
		IVideoDriver_drawVertexPrimitiveList(self.c_pointer, vertices.c_pointer, vertexCount, indexList, primCount, vType, pType, iType)
	def draw2DVertexPrimitiveList(self, vertices, vertexCount, indexList, primCount, vType=EVT_STANDARD, pType=EPT_TRIANGLES, iType=EIT_16BIT):
		IVideoDriver_draw2DVertexPrimitiveList(self.c_pointer, vertices.c_pointer, vertexCount, indexList, primCount, vType, pType, iType)
	def drawIndexedTriangleList1(self, vertices, vertexCount, indexList, triangleCount):
		IVideoDriver_drawIndexedTriangleList1(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	def drawIndexedTriangleList2(self, vertices, vertexCount, indexList, triangleCount):
		IVideoDriver_drawIndexedTriangleList2(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	def drawIndexedTriangleList3(self, vertices, vertexCount, indexList, triangleCount):
		IVideoDriver_drawIndexedTriangleList3(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	def drawIndexedTriangleList(self, *args, **kwargs):
		if isinstance(args[0], S3DVertex):
			self.drawIndexedTriangleList1(*args, **kwargs)
		elif isinstance(args[0], S3DVertex2TCoords):
			self.drawIndexedTriangleList1(*args, **kwargs)
		else:#S3DVertexTangents
			self.drawIndexedTriangleList3(*args, **kwargs)
	def drawIndexedTriangleFan(self, vertices, vertexCount, indexList, triangleCount):
		'vertices can be as S3DVertex, S3DVertex2TCoords or S3DVertexTangents'
		IVideoDriver_drawIndexedTriangleFan(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	#~ def drawIndexedTriangleFan1(self, vertices, vertexCount, indexList, triangleCount):
		#~ IVideoDriver_drawIndexedTriangleFan1(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	#~ def drawIndexedTriangleFan2(self, vertices, vertexCount, indexList, triangleCount):
		#~ IVideoDriver_drawIndexedTriangleFan2(self.c_pointer, vertices.c_pointer, vertexCount, indexList, triangleCount)
	def draw3DLine(self, start, end, color = SColor(255,255,255,255)):
		IVideoDriver_draw3DLine(self.c_pointer, start.c_pointer, end.c_pointer, color.c_pointer)
	def draw3DTriangle(self, triangle, color = SColor(255,255,255,255)):
		IVideoDriver_draw3DTriangle(self.c_pointer, triangle.c_pointer, color.c_pointer)
	def draw3DBox(self, box, color = SColor(255,255,255,255)):
		IVideoDriver_draw3DBox(self.c_pointer, box.c_pointer, color.c_pointer)
	def draw2DImage1(self, texture, destPos):
		'ITexture, position2di'
		IVideoDriver_draw2DImage1(self.c_pointer, texture.c_pointer, destPos.c_pointer)
	def draw2DImage2(self, texture, destPos, sourceRect, clipRect = recti(0), color = SColor(255,255,255,255), useAlphaChannelOfTexture = False):
		'ITexture, position2di, recti, recti, SColor, bool'
		IVideoDriver_draw2DImage2(self.c_pointer, texture.c_pointer, destPos.c_pointer, sourceRect.c_pointer, clipRect.c_pointer, color.c_pointer, useAlphaChannelOfTexture)
	def draw2DImage3(self, texture, destRect, sourceRect, clipRect = recti(0), colors = 0, useAlphaChannelOfTexture = False):
		'ITexture, position2di, recti, recti, SColor* array(4), bool'
		IVideoDriver_draw2DImage3(self.c_pointer, texture.c_pointer, destRect.c_pointer, sourceRect.c_pointer, clipRect.c_pointer, colors, useAlphaChannelOfTexture)
	def draw2DImage(self, *args, **kwargs):
		if len(args) == 2:
			self.draw2DImage1(*args)
		elif len(kwargs) == 0:
			clipRect = recti(0)
			color = SColor(255,255,255,255)
			useAlphaChannelOfTexture = False
			if len(args) == 3:
				texture, destPos, sourceRect = args
			elif len(args) == 4:
				texture, destPos, sourceRect, clipRect = args
			elif len(args) == 5:
				texture, destPos, sourceRect, clipRect, color = args
			elif len(args) == 6:
				texture, destPos, sourceRect, clipRect, color, useAlphaChannelOfTexture = args
			if isinstance(clipRect, int):
				clipRect = recti(clipRect)
			if isinstance(color, SColor):
				self.draw2DImage2(texture, destPos, sourceRect, clipRect, color, useAlphaChannelOfTexture)
			else:
				self.draw2DImage3(texture, destPos, sourceRect, clipRect, color, useAlphaChannelOfTexture)
		else:
			if 'color' in kwargs:
				self.draw2DImage2(*args, **kwargs)
			else:
				self.draw2DImage3(*args, **kwargs)
	def draw2DImageBatch1(self, texture, pos, sourceRects, indices, kerningWidth=0, clipRect=0, color=SColor(255,255,255,255), useAlphaChannelOfTexture=False):
		IVideoDriver_draw2DImageBatch1(self.c_pointer, texture.c_pointer, pos.c_pointer, sourceRects, indices, kerningWidth, clipRect.c_pointer, color.c_pointer, useAlphaChannelOfTexture)
	def draw2DImageBatch2(self, texture, positions, sourceRects, clipRect = recti(0), color=SColor(255,255,255,255), useAlphaChannelOfTexture=False):
		IVideoDriver_draw2DImageBatch2(self.c_pointer, texture.c_pointer, positions, sourceRects, clipRect.c_pointer, color.c_pointer, useAlphaChannelOfTexture)
	def draw2DImageBatch(self, *args, **kwargs):
		if isinstance(args[1], position2di):
			self.draw2DImageBatch1(*args, **kwargs)
		else:
			self.draw2DImageBatch2(*args, **kwargs)
	def draw2DRectangle1(self, color, pos, clip = recti(0)):
		'SColor, recti, recti'
		IVideoDriver_draw2DRectangle1(self.c_pointer, color.c_pointer, pos.c_pointer, clip.c_pointer)
	def draw2DRectangle2(self, pos, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown, clip = recti(0)):
		'recti, SColor, SColor, SColor, SColor, recti'
		IVideoDriver_draw2DRectangle2(self.c_pointer, pos.c_pointer, colorLeftUp.c_pointer, colorRightUp.c_pointer, colorLeftDown.c_pointer, colorRightDown.c_pointer, clip.c_pointer)
	def draw2DRectangle(self, *args):
		clip = recti(0)
		if isinstance(args[0], SColor):
			if len(args) == 2:
				color, pos = args
			else:
				color, pos, clip = args
			self.draw2DRectangle1(color, pos, clip)
		else:
			if len(args) == 5:
				pos, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown = args
			else:
				pos, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown, clip = args
			self.draw2DRectangle2(pos, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown, clip)
	def draw2DRectangle_f1(self, color, pos_x1, pos_y1, pos_x2, pos_y2):
		IVideoDriver_draw2DRectangle_f1(self.c_pointer, color.c_pointer, pos_x1, pos_y1, pos_x2, pos_y2)
	def draw2DRectangle_f2(self, color, pos_x1, pos_y1, pos_x2, pos_y2, clip_x1, clip_y1, clip_x2, clip_y2):
		IVideoDriver_draw2DRectangle_f2(self.c_pointer, color.c_pointer, pos_x1, pos_y1, pos_x2, pos_y2, clip_x1, clip_y1, clip_x2, clip_y2)
	def draw2DRectangle_f3(self, pos_x1, pos_y1, pos_x2, pos_y2, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown):
		IVideoDriver_draw2DRectangle_f3(self.c_pointer, pos_x1, pos_y1, pos_x2, pos_y2, colorLeftUp.c_pointer, colorRightUp.c_pointer, colorLeftDown.c_pointer, colorRightDown.c_pointer)
	def draw2DRectangle_f4(self, pos_x1, pos_y1, pos_x2, pos_y2, colorLeftUp, colorRightUp, colorLeftDown, colorRightDown, clip_x1, clip_y1, clip_x2, clip_y2):
		IVideoDriver_draw2DRectangle_f4(self.c_pointer, pos_x1, pos_y1, pos_x2, pos_y2, colorLeftUp.c_pointer, colorRightUp.c_pointer, colorLeftDown.c_pointer, colorRightDown.c_pointer, clip_x1, clip_y1, clip_x2, clip_y2)
	def draw2DRectangleOutline(self, pos, color=SColor(255,255,255,255)):
		IVideoDriver_draw2DRectangleOutline(self.c_pointer, pos.c_pointer, color.c_pointer)
	def draw2DRectangleOutline_f(self, x1, y1, x2, y2, color = SColor(255,255,255,255)):
		IVideoDriver_draw2DRectangleOutline_f(self.c_pointer, x1, y1, x2, y2, color.c_pointer)
	def draw2DLine(self, start, end, color=SColor(255,255,255,255)):
		IVideoDriver_draw2DLine(self.c_pointer, start.c_pointer, end.c_pointer, color.c_pointer)
	def draw2DLine_f(self, start_x, start_y, end_x, end_y, color=SColor(255,255,255,255)):
		IVideoDriver_draw2DLine_f(self.c_pointer, start_x, start_y, end_x, end_y, color.c_pointer)
	def draw2DLineW(self, start, end, color=SColor(255,255,255,255), width = 0):
		IVideoDriver_draw2DLineW(self.c_pointer, start.c_pointer, end.c_pointer, color.c_pointer, width)
	def draw2DLineWf(self, start_x, start_y, end_x, end_y, color=SColor(255,255,255,255), width = 0):
		IVideoDriver_draw2DLineWf(self.c_pointer, start_x, start_y, end_x, end_y, color.c_pointer, width)
	def drawPixel(self, x, y, color):
		IVideoDriver_drawPixel(self.c_pointer, x, y, color)
	def drawPixel_f(self, x, y, color):
		IVideoDriver_drawPixel_f(self.c_pointer, x, y, color.c_pointer)
	def draw2DPolygon(self, center, radius, color=SColor(100,255,255,255), vertexCount=10):
		IVideoDriver_draw2DPolygon(self.c_pointer, center.c_pointer, radius, color.c_pointer, vertexCount)
	def draw2DPolygon_f(self, center_x, center_y, radius, color=SColor(100,255,255,255), vertexCount=10):
		IVideoDriver_draw2DPolygon_f(self.c_pointer, center_x, center_y, radius, color.c_pointer, vertexCount)
	if IRRLICHT_VERSION < 180:
		def drawStencilShadowVolume(self, triangles, count, zfail = True):
			IVideoDriver_drawStencilShadowVolume(self.c_pointer, triangles, count, zfail)
	else:
		def drawStencilShadowVolume(self, triangles, zfail = True, debugDataVisible = 0):
			IVideoDriver_drawStencilShadowVolume(self.c_pointer, triangles.c_pointer, zfail, debugDataVisible)
	def drawStencilShadow(self, clearStencilBuffer=False, leftUpEdge = SColor(255,0,0,0), rightUpEdge = SColor(255,0,0,0), leftDownEdge = SColor(255,0,0,0), rightDownEdge = SColor(255,0,0,0)):
		IVideoDriver_drawStencilShadow(self.c_pointer, clearStencilBuffer, leftUpEdge.c_pointer, rightUpEdge.c_pointer, leftDownEdge.c_pointer, rightDownEdge.c_pointer)
	def drawMeshBuffer(self, mb):
		'IMeshBuffer'
		IVideoDriver_drawMeshBuffer(self.c_pointer, mb.c_pointer)
	def setFog(self, color=SColor(0,255,255,255), fogType=EFT_FOG_LINEAR, start=50.0, end=100.0, density=0.01, pixelFog=False, rangeFog=False):
		IVideoDriver_setFog(self.c_pointer, color.c_pointer, fogType, start, end, density, pixelFog, rangeFog)
	def getFog(self):
		color = ctypes.c_void_p()
		fogType = ctypes.c_int()
		start = ctypes.c_float()
		end = ctypes.c_float()
		density = ctypes.c_float()
		pixelFog = ctypes.c_bool()
		rangeFog = ctypes.c_bool()
		IVideoDriver_getFog(self.c_pointer, ctypes.byref(color), ctypes.byref(fogType), ctypes.byref(start), ctypes.byref(end), ctypes.byref(density), ctypes.byref(pixelFog), ctypes.byref(rangeFog))
		return SColor(ctypes.pointer(color)), fogType.value, start.value, end.value, density.value, bool(pixelFog.value), bool(rangeFog.value)
	def getColorFormat(self):
		return IVideoDriver_getColorFormat(self.c_pointer)
	def getScreenSize(self):
		return dimension2du(pointer = IVideoDriver_getScreenSize(self.c_pointer))
	def getCurrentRenderTargetSize(self):
		return dimension2du(pointer = IVideoDriver_getCurrentRenderTargetSize(self.c_pointer))
	def getFPS(self):
		return IVideoDriver_getFPS(self.c_pointer)
	def getPrimitiveCountDrawn(self, mode = 0):
		return IVideoDriver_getPrimitiveCountDrawn(self.c_pointer, mode)
	def deleteAllDynamicLights(self):
		IVideoDriver_deleteAllDynamicLights(self.c_pointer)
	def addDynamicLight(self, light):
		return IVideoDriver_addDynamicLight(self.c_pointer, light)
	def getMaximalDynamicLightAmount(self):
		return IVideoDriver_getMaximalDynamicLightAmount(self.c_pointer)
	def getDynamicLightCount(self):
		return IVideoDriver_getDynamicLightCount(self.c_pointer)
	def getDynamicLight(self, idx):
		return IVideoDriver_getDynamicLight(self.c_pointer, idx)
	def turnLightOn(self, lightIndex, turnOn):
		IVideoDriver_turnLightOn(self.c_pointer, lightIndex, turnOn)
	def getName(self):
		return IVideoDriver_getName(self.c_pointer)
	def addExternalImageLoader(self, loader):
		IVideoDriver_addExternalImageLoader(self.c_pointer, loader.c_pointer)
	def addExternalImageWriter(self, writer):
		IVideoDriver_addExternalImageWriter(self.c_pointer, writer.c_pointer)
	def getMaximalPrimitiveCount(self):
		return IVideoDriver_getMaximalPrimitiveCount(self.c_pointer)
	def setTextureCreationFlag(self, flag, enabled=True):
		IVideoDriver_setTextureCreationFlag(self.c_pointer, flag, enabled)
	def getTextureCreationFlag(self, flag):
		return IVideoDriver_getTextureCreationFlag(self.c_pointer, flag)
	def createImageFromFile(self, file_or_filename):
		if isinstance(file_or_filename, str):
			return self.createImageFromFile1(file_or_filename)
		else:
			return self.createImageFromFile2(file_or_filename)
	def createImageFromFile1(self, filename):
		return IImage(IVideoDriver_createImageFromFile1(self.c_pointer, filename))
	def createImageFromFile2(self, file):
		return IImage(IVideoDriver_createImageFromFile2(self.c_pointer, file.c_pointer))
	def writeImageToFile(self, image, file_or_filename, param = 0):
		if isinstance(file_or_filename, (type_str, type_unicode)):
			return self.writeImageToFile1(image, file_or_filename, param)
		else:
			return self.writeImageToFile2(image, file_or_filename, param)
	def writeImageToFile1(self, image, filename, param = 0):
		try:
			return IVideoDriver_writeImageToFile1(self.c_pointer, image.c_pointer, filename, param)
		except Exception as e:
			print(e)
	def writeImageToFile2(self, image, file, param = 0):
		return IVideoDriver_writeImageToFile2(self.c_pointer, image.c_pointer, file.c_pointer, param)
	def createImageFromData(self, format, size, data, ownForeignMemory = False, deleteMemory = True):
		return IImage(IVideoDriver_createImageFromData(self.c_pointer, format, size, data, ownForeignMemory, deleteMemory))
	def createImage(self, *args):
		if isinstance(args[0], int):
			if isinstance(args[1], dimension2du):# int, dimension2du
				return self.createImage1(*args)
			elif isinstance(args[1], IImage) and IRRLICHT_VERSION < 180:
				return self.createImage2(*args)# int, IImage
		else:
			if isinstance(args[0], ITexture):# ITexture, position2di, dimension2du
				return self.createImage4(*args)
			elif isinstance(args[0], IImage) and IRRLICHT_VERSION < 180:
				return self.createImage3(*args)# IImage, position2di, dimension2du
	def createImage1(self, format, size):
		return IImage(IVideoDriver_createImage1(self.c_pointer, format, size.c_pointer))
	if IRRLICHT_VERSION < 180:
		def createImage2(self, format, imageToCopy):
			return IImage(IVideoDriver_createImage2(self.c_pointer, format, imageToCopy.c_pointer))
		def createImage3(self, imageToCopy, pos, size):
			return IImage(IVideoDriver_createImage3(self.c_pointer, imageToCopy.c_pointer, pos.c_pointer, size.c_pointer))
	def createImage4(self, texture, pos, size):
		return IImage(IVideoDriver_createImage4(self.c_pointer, texture.c_pointer, pos.c_pointer, size.c_pointer))
	def OnResize(self, size):
		'Event handler for resize events. Only used by the engine internally.'
		IVideoDriver_OnResize(self.c_pointer, size.c_pointer)
	def addMaterialRenderer(self, renderer, name = 0):
		return IVideoDriver_addMaterialRenderer(self.c_pointer, renderer, name)
	def getMaterialRenderer(self, idx):
		return IVideoDriver_getMaterialRenderer(self.c_pointer, idx)
	def getMaterialRendererCount(self):
		return IVideoDriver_getMaterialRendererCount(self.c_pointer)
	def getMaterialRendererName(self, idx):
		return IVideoDriver_getMaterialRendererName(self.c_pointer, idx)
	def setMaterialRendererName(self, idx, name):
		IVideoDriver_setMaterialRendererName(self.c_pointer, idx, name)
	def createAttributesFromMaterial(self, material):
		return IVideoDriver_createAttributesFromMaterial(self.c_pointer, material)
	def fillMaterialStructureFromAttributes(self, outMaterial, attributes):
		IVideoDriver_fillMaterialStructureFromAttributes(self.c_pointer, outMaterial.c_pointer, attributes.c_pointer)
	def getExposedVideoData(self):
		return SExposedVideoData(IVideoDriver_getExposedVideoData(self.c_pointer))
	def getDriverType(self):
		return IVideoDriver_getDriverType(self.c_pointer)
	def getGPUProgrammingServices(self):
		return IVideoDriver_getGPUProgrammingServices(self.c_pointer)
	def getMeshManipulator(self):
		return IMeshManipulator(IVideoDriver_getMeshManipulator(self.c_pointer))
	def clearZBuffer(self):
		IVideoDriver_clearZBuffer(self.c_pointer)
	def createScreenShot(self):
		return IImage(IVideoDriver_createScreenShot(self.c_pointer))
	def findTexture(self, filename):
		return ITexture(IVideoDriver_findTexture(self.c_pointer, filename))
	def setClipPlane(self, index, plane, enable=False):
		return IVideoDriver_setClipPlane(self.c_pointer, index, plane.c_pointer, enable)
	def enableClipPlane(self, index, enable):
		IVideoDriver_enableClipPlane(self.c_pointer, index, enable)
	def setMinHardwareBufferVertexCount(self, count):
		IVideoDriver_setMinHardwareBufferVertexCount(self.c_pointer, count)
	def getOverrideMaterial(self):
		return SOverrideMaterial(IVideoDriver_getOverrideMaterial(self.c_pointer))
	def getMaterial2D(self):
		return SMaterial(IVideoDriver_getMaterial2D(self.c_pointer))
	def enableMaterial2D(self, enable = True):
		IVideoDriver_enableMaterial2D(self.c_pointer, enable)
	def getVendorInfo(self):
		return ctypes.string_at(IVideoDriver_getVendorInfo(self.c_pointer))
	def setAmbientLight(self, color):
		IVideoDriver_setAmbientLight(self.c_pointer, color.c_pointer)
	def setAllowZWriteOnTransparent(self, flag):
		IVideoDriver_setAllowZWriteOnTransparent(self.c_pointer, flag)
	def getMaxTextureSize(self):
		return dimension2du(pointer = IVideoDriver_getMaxTextureSize(self.c_pointer))
	def GetHandle(self):
		return IVideoDriver_GetHandle(self.c_pointer)
	def SetIcon(self, icon_id = IDI_APPLICATION, big_icon = False):
		IVideoDriver_SetIcon(self.c_pointer, icon_id, big_icon)
	def addAggSvgImageLoader(self):
		IVideoDriver_addAggSvgImageLoader(self.c_pointer)

class IDummyTransformationSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0:
			self.c_pointer = args[0]
		elif len(args) == 3:
			self.c_pointer = IDummyTransformationSceneNode_ctor(args[0].c_pointer, args[1].c_pointer, args[2])
	def getRelativeTransformationMatrix(self):
		return matrix4(IDummyTransformationSceneNode_getRelativeTransformationMatrix(self.c_pointer))

class ITextSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def setText(self, text):
		ITextSceneNode_setText(self.c_pointer, text)
	def setTextColor(self, color = SColor(0,0,0,0)):
		ITextSceneNode_setTextColor(self.c_pointer, color.c_pointer)

class IVolumeLightSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def ctor(self, parent, mgr, id, position, rotation, scale):
		return IVolumeLightSceneNode_ctor(parent.c_pointer, mgr.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer)
	def getType(self):
		return IVolumeLightSceneNode_getType(self.c_pointer)
	def setSubDivideU(self, inU):
		IVolumeLightSceneNode_setSubDivideU(self.c_pointer, inU)
	def setSubDivideV(self, inV):
		IVolumeLightSceneNode_setSubDivideV(self.c_pointer, inV)
	def getSubDivideU(self):
		return IVolumeLightSceneNode_getSubDivideU(self.c_pointer)
	def getSubDivideV(self):
		return IVolumeLightSceneNode_getSubDivideV(self.c_pointer)
	def setFootColor(self, inColour):
		IVolumeLightSceneNode_setFootColor(self.c_pointer, inColour.c_pointer)
	def setTailColor(self, inColour):
		IVolumeLightSceneNode_setTailColor(self.c_pointer, inColour.c_pointer)
	def getFootColor(self):
		return SColor(IVolumeLightSceneNode_getFootColor(self.c_pointer))
	def getTailColor(self):
		return SColor(IVolumeLightSceneNode_getTailColor(self.c_pointer))

class ICursorControl(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def setVisible(self, visible = True):
		ICursorControl_setVisible(self.c_pointer, visible)
	def isVisible(self):
		return ICursorControl_isVisible(self.c_pointer)
	def setPosition(self, *args):
		if len(args) == 1:
			if isinstance(args[0], position2df):
				ICursorControl_setPositionF(self.c_pointer, args[0].c_pointer)
			elif isinstance(args[0], position2di):
				ICursorControl_setPositionI(self.c_pointer, args[0].c_pointer)
		elif len(args) > 1:
			if isinstance(args[0], float) and isinstance(args[1], float):
				ICursorControl_setPositionF2(self.c_pointer, args[0], args[1])
			elif isinstance(args[0], (int, long)) and isinstance(args[1], (int, long)):
				ICursorControl_setPositionI2(self.c_pointer, args[0], args[1])
	def setPositionF(self, *args):
		if len(args) == 0:
			ICursorControl_setPositionF2(self.c_pointer, 0.0, 0.0)
		elif len(args) == 1:
			if isinstance(args[0], float):
				ICursorControl_setPositionF2(self.c_pointer, args[0], 0.0)
			else:
				ICursorControl_setPositionF(self.c_pointer, args[0].c_pointer)
		elif len(args) == 2:
			ICursorControl_setPositionF2(self.c_pointer, *args)
	def setPositionF1(self, pos):
		ICursorControl_setPositionF(self.c_pointer, pos.c_pointer)
	def setPositionF2(self, x = 0.0, y = 0.0):
		ICursorControl_setPositionF2(self.c_pointer, x, y)
	def setPositionI(self, *args):
		if len(args) == 0:
			ICursorControl_setPositionI2(self.c_pointer, 0, 0)
		elif len(args) == 1:
			if isinstance(args[0], int):
				ICursorControl_setPositionI2(self.c_pointer, args[0], 0)
			else:
				ICursorControl_setPositionI(self.c_pointer, args[0].c_pointer)
		elif len(args) == 2:
			ICursorControl_setPositionI2(self.c_pointer, *args)
	def setPositionI1(self, pos):
		ICursorControl_setPositionI(self.c_pointer, pos.c_pointer)
	def setPositionI2(self, x = 0, y = 0):
		ICursorControl_setPositionI2(self.c_pointer, x, y)
	def getPosition(self):
		return position2di(c_pointer = ICursorControl_getPosition(self.c_pointer))
	def getRelativePosition(self):
		return position2df(c_pointer = ICursorControl_getRelativePosition(self.c_pointer))
	def setReferenceRect(self, rect = recti(0)):
		ICursorControl_setReferenceRect(self.c_pointer, rect.c_pointer)

class IFileSystem(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def createAndOpenFile(self, filename):
		return IReadFile(IFileSystem_createAndOpenFile(self.c_pointer, fs_conv(filename)))
	def createMemoryReadFile(self, memory, len, fileName, deleteMemoryWhenDropped = False):
		if hasattr(memory, 'c_pointer'):
			memory = memory.c_pointer
		return IReadFile(IFileSystem_createMemoryReadFile(self.c_pointer, memory, len, fs_conv(fileName), deleteMemoryWhenDropped))
		#~ return IReadFile(IFileSystem_createMemoryReadFile(self.c_pointer, memory, len, fileName, deleteMemoryWhenDropped))
	def createLimitReadFile(self, fileName, alreadyOpenedFile, pos, areaSize):
		return IReadFile(IFileSystem_createLimitReadFile(self.c_pointer, fileName, alreadyOpenedFile, pos, areaSize))
	def createMemoryWriteFile(self, memory, len, fileName, deleteMemoryWhenDropped=False):
		return IWriteFile(IFileSystem_createMemoryWriteFile(self.c_pointer, memory, len, fs_conv(fileName), deleteMemoryWhenDropped))
	def createAndWriteFile(self, filename, append=False):
		return IWriteFile(IFileSystem_createAndWriteFile(self.c_pointer, fs_conv(filename), append))
	def addFileArchive(self, filename, ignoreCase=True, ignorePaths=True, archiveType=EFAT_UNKNOWN):
		return IFileSystem_addFileArchive(self.c_pointer, fs_conv(filename), ignoreCase, ignorePaths, archiveType)
	def addArchiveLoader(self, loader):
		IFileSystem_addArchiveLoader(self.c_pointer, loader)
	def getFileArchiveCount(self):
		return IFileSystem_getFileArchiveCount(self.c_pointer)
	def removeFileArchive1(self, index):
		return IFileSystem_removeFileArchive1(self.c_pointer, index)
	def removeFileArchive2(self, filename):
		return IFileSystem_removeFileArchive2(self.c_pointer, fs_conv(filename))
	def removeFileArchive(self, arg):
		if isinstance(arg, int):
			return self.removeFileArchive1(arg)
		else:
			return self.removeFileArchive2(arg)
	def moveFileArchive(self, sourceIndex, relative):
		return IFileSystem_moveFileArchive(self.c_pointer, sourceIndex, relative)
	def getFileArchive(self, index):
		return IFileArchive(IFileSystem_getFileArchive(self.c_pointer, index))
	if IRRLICHT_VERSION < 180:
		def addZipFileArchive(self, filename, ignoreCase=True, ignorePaths=True):
			return IFileSystem_addZipFileArchive(self.c_pointer, as_ansi(filename), ignoreCase, ignorePaths)
		def addFolderFileArchive(self, filename, ignoreCase=True, ignorePaths=True):
			return IFileSystem_addFolderFileArchive(self.c_pointer, as_ansi(filename), ignoreCase, ignorePaths)
		def addPakFileArchive(self, filename, ignoreCase=True, ignorePaths=True):
			return IFileSystem_addPakFileArchive(self.c_pointer, as_ansi(filename), ignoreCase, ignorePaths)
	def getWorkingDirectory(self):
		return IFileSystem_getWorkingDirectory(self.c_pointer)
	def changeWorkingDirectoryTo(self, newDirectory):
		return IFileSystem_changeWorkingDirectoryTo(self.c_pointer, fs_conv(newDirectory))
	def getAbsolutePath(self, filename):
		return IFileSystem_getAbsolutePath(self.c_pointer, fs_conv(filename))
	def getFileDir(self, filename):
		return IFileSystem_getFileDir(self.c_pointer, fs_conv(filename))
	def getFileBasename(self, filename, keepExtension=True):
		return IFileSystem_getFileBasename(self.c_pointer, fs_conv(filename), keepExtension)
	def flattenFilename(self, directory, root='/'):
		return IFileSystem_flattenFilename(self.c_pointer, fs_conv(directory), root)
	def createFileList(self):
		return IFileList(IFileSystem_createFileList(self.c_pointer))
	def createEmptyFileList(self, path, ignoreCase, ignorePaths):
		return IFileList(IFileSystem_createEmptyFileList(self.c_pointer, fs_conv(path), ignoreCase, ignorePaths))
	def setFileListSystem(self, listType):
		return IFileSystem_setFileListSystem(self.c_pointer, listType)
	def existFile(self, filename):
		return IFileSystem_existFile(self.c_pointer, fs_conv(filename))
	def createXMLReader1(self, filename):
		return IXMLReader(IFileSystem_createXMLReader1(self.c_pointer, fs_conv(filename)))
	def createXMLReader2(self, file):
		return IXMLReader(IFileSystem_createXMLReader2(self.c_pointer, file.c_pointer))
	def createXMLReader(self, name_or_file):
		if isinstance(name_or_file, (type_str, type_unicode)):
			return self.createXMLReader1(name_or_file)
		elif isinstance(name_or_file, IReadFile):
			return self.createXMLReader2(name_or_file)
		else:
			print('ERROR in IFileSystem::createXMLReader, unsupported type argument', name_or_file)
			return None
	def createXMLReaderUTF8name(self, filename):
		return IXMLReaderUTF8(IFileSystem_createXMLReaderUTF8(self.c_pointer, fs_conv(filename)))
	def createXMLReaderUTF8stream(self, file):
		return IXMLReaderUTF8(IFileSystem_createXMLReaderUTF8stream(self.c_pointer, file.c_pointer))
	def createXMLReaderUTF8(self, name_or_file):
		if isinstance(name_or_file, type_str):
			return self.createXMLReaderUTF8name(name_or_file)
		elif isinstance(name_or_file, IReadFile):
			return self.createXMLReaderUTF8stream(name_or_file)
		else:
			print('ERROR in IFileSystem::createXMLReaderUTF8, unsupported argument type', name_or_file)
			return None
	def createXMLWriter1(self, filename):
		return IXMLWriter(IFileSystem_createXMLWriter1(self.c_pointer, fs_conv(filename)))
	def createXMLWriter2(self, file):
		return IXMLWriter(IFileSystem_createXMLWriter2(self.c_pointer, file.c_pointer))
	def createXMLWriter(self, name_or_file):
		if isinstance(name_or_file, type_str):
			return self.createXMLWriter1(name_or_file)
		elif isinstance(name_or_file, IWriteFile):
			return self.createXMLWriter2(name_or_file)
		else:
			print('ERROR in IFileSystem::createXMLWriter, unsupported argument type', name_or_file)
			return None
	def createEmptyAttributes(self, driver = IVideoDriver(0)):
		return IAttributes(IFileSystem_createEmptyAttributes(self.c_pointer, driver.c_pointer))

class ISceneManager(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getMesh(self, file_or_filename):
		if isinstance(file_or_filename, IReadFile):
			return self.getMesh2(file_or_filename)
		else:
			return self.getMesh1(as_ansi(file_or_filename))
	def getMesh1(self, filename):
		return IAnimatedMesh(ISceneManager_getMesh(self.c_pointer, filename))
	def getMesh2(self, file):
		return IAnimatedMesh(ISceneManager_getMesh2(self.c_pointer, file.c_pointer))
	def getMeshCache(self):
		return IMeshCache(ISceneManager_getMeshCache(self.c_pointer))
	def getVideoDriver(self):
		return IVideoDriver(ISceneManager_getVideoDriver(self.c_pointer))
	def getGUIEnvironment(self):
		return IGUIEnvironment(ISceneManager_getGUIEnvironment(self.c_pointer))
	def getFileSystem(self):
		return IFileSystem(ISceneManager_getFileSystem(self.c_pointer))
	def addVolumeLightSceneNode(self, parent = ISceneNode(0), id = -1, subdivU = 32, subdivV = 32, foot = SColor(51, 0, 230, 180), tail = SColor(0, 0, 0, 0), position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IVolumeLightSceneNode(ISceneManager_addVolumeLightSceneNode(self.c_pointer, parent.c_pointer, id, subdivU, subdivV, foot.c_pointer, tail.c_pointer, position.c_pointer, rotation.c_pointer, scale.c_pointer))
	def addCubeSceneNode(self, size = 10.0, parent = ISceneNode(0), id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IMeshSceneNode(ISceneManager_addCubeSceneNode(self.c_pointer, size, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer))
	def addSphereSceneNode(self, radius = 5.0, polyCount = 16, parent = ISceneNode(0), id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IMeshSceneNode(ISceneManager_addSphereSceneNode(self.c_pointer, radius, polyCount, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer))
	def addAnimatedMeshSceneNode(self, mesh, parent = ISceneNode(0), id = -1, position = vector3df(.0,.0,.0), rotation = vector3df(.0,.0,.0), scale = vector3df(1.0, 1.0, 1.0), alsoAddIfMeshPointerZero = False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IAnimatedMeshSceneNode(ISceneManager_addAnimatedMeshSceneNode(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer, alsoAddIfMeshPointerZero))
	def addAnimatedMeshSceneNode2(self, mesh):
		return IAnimatedMeshSceneNode(ISceneManager_addAnimatedMeshSceneNode2(self.c_pointer, mesh.c_pointer))
	def addMeshSceneNode(self, mesh, parent = ISceneNode(0), id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0), alsoAddIfMeshPointerZero = False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IMeshSceneNode(ISceneManager_addMeshSceneNode(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer, alsoAddIfMeshPointerZero))
	def addWaterSurfaceSceneNode(self, mesh, waveHeight = 2.0, waveSpeed = 300.0, waveLength = 10.0, parent = ISceneNode(0), id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		return ISceneNode(ISceneManager_addWaterSurfaceSceneNode(self.c_pointer, mesh.c_pointer, waveHeight, waveSpeed, waveLength, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer))
	def addOctTreeSceneNode(self, mesh, parent = ISceneNode(0), id=-1, minimalPolysPerNode=512, alsoAddIfMeshPointerZero=False):
		if IRRLICHT_VERSION < 180:
			if parent in (None, 0):
				parent = ISceneNode(0)
			if isinstance(mesh, IAnimatedMesh):
				return IMeshSceneNode(ISceneManager_addOctTreeSceneNode1(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
			elif isinstance(mesh, IMesh):
				return IMeshSceneNode(ISceneManager_addOctTreeSceneNode2(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
			else:
				print('WARNING: mesh is not valid instance')
				return IMeshSceneNode(0)
		else:
			print('WARNING: addOctTreeSceneNode deprecate, use addOctreeSceneNode instead')
			return self.addOctreeSceneNode(mesh, parent, id, minimalPolysPerNode, alsoAddIfMeshPointerZero)
	def addOctTreeSceneNode1(self, mesh, parent = ISceneNode(0), id=-1, minimalPolysPerNode=512, alsoAddIfMeshPointerZero=False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IMeshSceneNode(ISceneManager_addOctTreeSceneNode1(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
	def addOctTreeSceneNode2(self, mesh, parent = ISceneNode(0), id=-1, minimalPolysPerNode=256, alsoAddIfMeshPointerZero=False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IMeshSceneNode(ISceneManager_addOctTreeSceneNode2(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
	def addOctreeSceneNode(self, mesh, parent = ISceneNode(0), id=-1, minimalPolysPerNode=512, alsoAddIfMeshPointerZero=False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		if isinstance(mesh, IAnimatedMesh):
			return IMeshSceneNode(ISceneManager_addOctreeSceneNode1(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
		elif isinstance(mesh, IMesh):
			return IMeshSceneNode(ISceneManager_addOctreeSceneNode2(self.c_pointer, mesh.c_pointer, parent.c_pointer, id, minimalPolysPerNode, alsoAddIfMeshPointerZero))
		else:
			print('WARNING: mesh is not valid instance')
			return IMeshSceneNode(0)
	def addCameraSceneNode(self, parent = ISceneNode(0), position = vector3df(0,0,0), lookat = vector3df(0,0,100), id = -1):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return ICameraSceneNode(ISceneManager_addCameraSceneNode(self.c_pointer, parent.c_pointer, position.c_pointer, lookat.c_pointer, id))
	def addCameraSceneNodeMaya(self, parent = ISceneNode(0), rotateSpeed = -1500.0, zoomSpeed = 200.0, translationSpeed = 1500.0, id = -1, distance = 70.0, makeActive = True):
		if parent in (None, 0):
			parent = ISceneNode(0)
		if IRRLICHT_VERSION < 180:
			return ICameraSceneNode(ISceneManager_addCameraSceneNodeMaya(self.c_pointer, parent.c_pointer, rotateSpeed, zoomSpeed, translationSpeed, id))
		else:
			return ICameraSceneNode(ISceneManager_addCameraSceneNodeMaya(self.c_pointer, parent.c_pointer, rotateSpeed, zoomSpeed, translationSpeed, id, distance, makeActive))
	def addCameraSceneNodeFPS(self, parent = ISceneNode(0), rotateSpeed = 100.0, moveSpeed = 0.5, id = -1, keyMapArray = SKeyMap(), keyMapSize = 0, noVerticalMovement = False, jumpSpeed = 0.0, invertMouse = False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		if not isinstance(keyMapArray, SKeyMap):
			keyMapArray = SKeyMap()
		return ICameraSceneNode(ISceneManager_addCameraSceneNodeFPS(self.c_pointer, parent.c_pointer, rotateSpeed, moveSpeed, id, keyMapArray.c_pointer, keyMapSize, noVerticalMovement, jumpSpeed, invertMouse))
	def addLightSceneNode(self, parent = ISceneNode(0), position = vector3df(0,0,0), color = SColorf(1.0, 1.0, 1.0), radius = 100.0, id = -1):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return ILightSceneNode(ISceneManager_addLightSceneNode(self.c_pointer, parent.c_pointer, position.c_pointer, color.c_pointer, radius, id))
	def addBillboardSceneNode(self, parent = ISceneNode(0), size = dimension2df(10.0, 10.0), position = vector3df(0,0,0), id = -1, colorTop = SColor(color = 0xFFFFFFFF), colorBottom = SColor(color = 0xFFFFFFFF)):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IBillboardSceneNode(ISceneManager_addBillboardSceneNode(self.c_pointer, parent.c_pointer, size.c_pointer, position.c_pointer, id, colorTop.c_pointer, colorBottom.c_pointer))
	def addSkyBoxSceneNode(self, top, bottom, left, right, front, back, parent = ISceneNode(0), id = -1):
		return ISceneNode(ISceneManager_addSkyBoxSceneNode(self.c_pointer, top.c_pointer, bottom.c_pointer, left.c_pointer, right.c_pointer, front.c_pointer, back.c_pointer, parent.c_pointer, id))
	def addSkyDomeSceneNode(self, texture, horiRes = 16, vertRes = 8, texturePercentage = 0.9, spherePercentage = 2.0, radius = 1000.0, parent = ISceneNode(0), id = -1):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return ISceneNode(ISceneManager_addSkyDomeSceneNode(self.c_pointer, texture.c_pointer, horiRes, vertRes, texturePercentage, spherePercentage, radius, parent.c_pointer, id))
	def addParticleSystemSceneNode(self, withDefaultEmitter = True, parent = ISceneNode(0), id = -1, position = vector3df(0,0,0), rotation = vector3df(0,0,0), scale = vector3df(1.0, 1.0, 1.0)):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return IParticleSystemSceneNode(ISceneManager_addParticleSystemSceneNode(self.c_pointer, withDefaultEmitter, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer))
	def addTerrainSceneNode(self, heightMapFileName, parent = ISceneNode(0), id = -1, position = vector3df(0.0,0.0,0.0), rotation = vector3df(0.0,0.0,0.0), scale = vector3df(1.0,1.0,1.0), vertexColor = SColor(255,255,255,255), maxLOD = 5, patchSize = ETPS_17, smoothFactor = 0, addAlsoIfHeightmapEmpty = False):
		if parent in (None, 0):
			parent = ISceneNode(0)
		return ITerrainSceneNode(ISceneManager_addTerrainSceneNode(self.c_pointer, heightMapFileName, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer, vertexColor.c_pointer, maxLOD, patchSize, smoothFactor, addAlsoIfHeightmapEmpty))
	def addTerrainSceneNode2(self, heightMapFile, parent = ISceneNode(0), id = -1, position = vector3df(0.0,0.0,0.0), rotation = vector3df(0.0,0.0,0.0), scale = vector3df(1.0,1.0,1.0), vertexColor = SColor(255,255,255,255), maxLOD = 5, patchSize = ETPS_17, smoothFactor = 0, addAlsoIfHeightmapEmpty = False):
		return ITerrainSceneNode(ISceneManager_addTerrainSceneNode2(self.c_pointer, heightMapFile.c_pointer, parent.c_pointer, id, position.c_pointer, rotation.c_pointer, scale.c_pointer, vertexColor.c_pointer, maxLOD, patchSize, smoothFactor, addAlsoIfHeightmapEmpty))
	def addQuake3SceneNode(self, meshBuffer, shader, parent = ISceneNode(0), id = -1):
		return IMeshSceneNode(ISceneManager_addQuake3SceneNode(self.c_pointer, meshBuffer.c_pointer, shader.c_pointer, parent.c_pointer, id))
	def addEmptySceneNode(self, parent = ISceneNode(0), id = -1):
		return ISceneNode(ISceneManager_addEmptySceneNode(self.c_pointer, parent.c_pointer, id))
	def addDummyTransformationSceneNode(self, parent = ISceneNode(0), id = -1):
		return IDummyTransformationSceneNode(ISceneManager_addDummyTransformationSceneNode(self.c_pointer, parent.c_pointer, id))
	def addTextSceneNode(self, font, text, color = SColor(100,255,255,255), parent = ISceneNode(0), position = vector3df(0,0,0), id=-1):
		return ITextSceneNode(ISceneManager_addTextSceneNode(self.c_pointer, font.c_pointer, text, color.c_pointer, parent.c_pointer, position.c_pointer, id))
	def addBillboardTextSceneNode(self, font, text, parent = ISceneNode(0), size = dimension2df(10.0, 10.0), position = vector3df(0,0,0), id = -1, colorTop = SColor(255, 255, 255, 255), colorBottom = SColor(255, 255, 255, 255)):
		return IBillboardTextSceneNode(ISceneManager_addBillboardTextSceneNode(self.c_pointer, font.c_pointer, text, parent.c_pointer, size.c_pointer, position.c_pointer, id, colorTop.c_pointer, colorBottom.c_pointer))
	def addHillPlaneMesh(self, name, tileSize = dimension2df(), tileCount = dimension2du(), material = SMaterial(0), hillHeight = 0.0, countHills = dimension2df(0.0, 0.0), textureRepeatCount = dimension2df(1.0, 1.0)):
		return IAnimatedMesh(ISceneManager_addHillPlaneMesh(self.c_pointer, as_ansi(name), tileSize.c_pointer, tileCount.c_pointer, material.c_pointer, hillHeight, countHills.c_pointer, textureRepeatCount.c_pointer))
	def addTerrainMesh(self, meshname, texture = IImage(0), heightmap = IImage(0), stretchSize = dimension2df(10.0,10.0), maxHeight = 200.0, defaultVertexBlockSize = dimension2du(64,64)):
		return IAnimatedMesh(ISceneManager_addTerrainMesh(self.c_pointer, meshname, texture.c_pointer, heightmap.c_pointer, stretchSize.c_pointer, maxHeight, defaultVertexBlockSize.c_pointer))
	def addArrowMesh(self, name, vtxColorCylinder = SColor(255, 255, 255, 255), vtxColorCone = SColor(255, 255, 255, 255), tesselationCylinder = 4, tesselationCone = 8, height = 1.0, cylinderHeight = 0.6, widthCylinder = 0.05, widthCone = 0.3):
		if not isinstance(name, type_str):
			name = as_ansi(name)
		return IAnimatedMesh(ISceneManager_addArrowMesh(self.c_pointer, name, vtxColorCylinder.c_pointer, vtxColorCone.c_pointer, tesselationCylinder, tesselationCone, height, cylinderHeight, widthCylinder, widthCone))
	def addSphereMesh(self, name, radius=5.0, polyCountX = 16, polyCountY = 16):
		return IAnimatedMesh(ISceneManager_addSphereMesh(self.c_pointer, name, radius=5.0, polyCountX = 16, polyCountY = 16))
	def addVolumeLightMesh(self, name, SubdivideU = 32, SubdivideV = 32, FootColor = SColor(51, 0, 230, 180), TailColor = SColor(0, 0, 0, 0)):
		return IAnimatedMesh(ISceneManager_addVolumeLightMesh(self.c_pointer, name, SubdivideU, SubdivideV, FootColor.c_pointer, TailColor.c_pointer))
	def getRootSceneNode(self):
		return ISceneNode(ISceneManager_getRootSceneNode(self.c_pointer))
	def getSceneNodeFromId(self, id = -1, start = ISceneNode(0)):
		return ISceneNode(ISceneManager_getSceneNodeFromId(self.c_pointer, id, start.c_pointer))
	def getSceneNodeFromName(self, name = '', start = ISceneNode(0)):
		return ISceneNode(ISceneManager_getSceneNodeFromName(self.c_pointer, name, start.c_pointer))
	def getSceneNodeFromType(self, type = 0, start = ISceneNode(0)):
		'ESCENE_NODE_TYPE type, ISceneNode* start'
		return ISceneNode(ISceneManager_getSceneNodeFromType(self.c_pointer, type, start.c_pointer))
	def getSceneNodesFromType(self, type, outNodes, start=ISceneNode(0)):
		ISceneManager_getSceneNodesFromType(self.c_pointer, type, outNodes.c_pointer, start.c_pointer)
	def getActiveCamera(self):
		return ICameraSceneNode(ISceneManager_getActiveCamera(self.c_pointer))
	def setActiveCamera(self, camera = ICameraSceneNode(0)):
		if not isinstance(camera, ICameraSceneNode):
			camera = ICameraSceneNode(0)
		ISceneManager_setActiveCamera(self.c_pointer, camera.c_pointer)
	def setShadowColor(self, color = SColor(150,0,0,0)):
		ISceneManager_setShadowColor(self.c_pointer, color.c_pointer)
	def getShadowColor(self):
		return SColor(c_pointer = ISceneManager_getShadowColor(self.c_pointer))
	def registerNodeForRendering(self, node, param_pass = ESNRP_AUTOMATIC):
		return ISceneManager_registerNodeForRendering(self.c_pointer, node.c_pointer, param_pass)
	def drawAll(self):
		ISceneManager_drawAll(self.c_pointer)
	def createRotationAnimator(self, rotationSpeed):
		return ISceneNodeAnimator(ISceneManager_createRotationAnimator(self.c_pointer, rotationSpeed.c_pointer))
	def createFlyCircleAnimator(self, center = vector3df(0.0,0.0,0.0), radius = 100.0, speed = 0.001, direction = vector3df(0.0, 1.0, 0.0), startPosition = 0.0, radiusEllipsoid = 0.0):
		return ISceneNodeAnimator(ISceneManager_createFlyCircleAnimator(self.c_pointer, center.c_pointer, radius, speed, direction.c_pointer, startPosition, radiusEllipsoid))
	def createFlyStraightAnimator(self, startPoint, endPoint, timeForWay, loop = False, pingpong = False):
		return ISceneNodeAnimator(ISceneManager_createFlyStraightAnimator(self.c_pointer, startPoint.c_pointer, endPoint.c_pointer, timeForWay, loop, pingpong))
	def createTextureAnimator(self, textures, timePerFrame, loop = True):
		return ISceneNodeAnimator(ISceneManager_createTextureAnimator(self.c_pointer, textures.c_pointer, timePerFrame, loop))
	def createDeleteAnimator(self, timeMs):
		return ISceneNodeAnimator(ISceneManager_createDeleteAnimator(self.c_pointer, timeMs))
	def createCollisionResponseAnimator(self, world, sceneNode, ellipsoidRadius = vector3df(30,60,30), gravityPerSecond = vector3df(0,-10.0,0), ellipsoidTranslation = vector3df(0,0,0), slidingValue = 0.0005):
		'world as ITriangleSelector, sceneNode as ISceneNode, ellipsoidRadius as vector3df, gravityPerSecond as vector3df, ellipsoidTranslation as vector3df, slidingValue as float'
		return ISceneNodeAnimatorCollisionResponse(ISceneManager_createCollisionResponseAnimator(self.c_pointer, world.c_pointer, sceneNode.c_pointer, ellipsoidRadius.c_pointer, gravityPerSecond.c_pointer, ellipsoidTranslation.c_pointer, slidingValue))
	def createFollowSplineAnimator(self, startTime, points, speed = 1.0, tightness = 0.5):
		return ISceneNodeAnimator(ISceneManager_createFollowSplineAnimator(self.c_pointer, startTime, points, speed, tightness))
	def createTriangleSelector(self, *args):
		if isinstance(args[0], IMesh):
			return self.createTriangleSelector1(*args)
		elif isinstance(args[0], IAnimatedMeshSceneNode):
			return self.createTriangleSelector2(*args)
		else:
			print('ERROR createTriangleSelector : argument 0 must be IMesh or IAnimatedMeshSceneNode. Found %s' % repr(args[0]))
			return None
	def createTriangleSelector1(self, mesh, node = None):
		if hasattr(node, 'c_pointer'):
			node = node.c_pointer
		return ITriangleSelector(ISceneManager_createTriangleSelector1(self.c_pointer, mesh.c_pointer, node))
	def createTriangleSelector2(self, node):
		'node as IAnimatedMeshSceneNode'
		return ITriangleSelector(ISceneManager_createTriangleSelector2(self.c_pointer, node.c_pointer))
	def createTriangleSelectorFromBoundingBox(self, node):
		return ITriangleSelector(ISceneManager_createTriangleSelectorFromBoundingBox(self.c_pointer, node.c_pointer))
	def createOctTreeTriangleSelector(self, mesh, node, minimalPolysPerNode = 32):
		'mesh as IMesh, node as ISceneNode'
		if IRRLICHT_VERSION < 180:
			return ITriangleSelector(ISceneManager_createOctTreeTriangleSelector(self.c_pointer, mesh.c_pointer, node.c_pointer, minimalPolysPerNode))
		else:
			print('WARNING: createOctTreeTriangleSelector deprecate, use createOctreeTriangleSelector instead')
			return self.createOctreeTriangleSelector(mesh, node, minimalPolysPerNode)
	def createOctreeTriangleSelector(self, mesh, node = ISceneNode(0), minimalPolysPerNode = 32):
		'mesh as IMesh, node as ISceneNode'
		if node in (None, 0):
			node = ISceneNode(0)
		return ITriangleSelector(ISceneManager_createOctreeTriangleSelector(self.c_pointer, mesh.c_pointer, node.c_pointer, minimalPolysPerNode))
	def createMetaTriangleSelector(self):
		return IMetaTriangleSelector(ISceneManager_createMetaTriangleSelector(self.c_pointer))
	def createTerrainTriangleSelector(self, node, LOD = 0):
		return ITriangleSelector(ISceneManager_createTerrainTriangleSelector(self.c_pointer, node.c_pointer, LOD))
	def addExternalMeshLoader(self, externalLoader):
		ISceneManager_addExternalMeshLoader(self.c_pointer, externalLoader.c_pointer)
	def getSceneCollisionManager(self):
		return ISceneCollisionManager(ISceneManager_getSceneCollisionManager(self.c_pointer))
	def getMeshManipulator(self):
		return IMeshManipulator(ISceneManager_getMeshManipulator(self.c_pointer))
	def addToDeletionQueue(self, node):
		ISceneManager_addToDeletionQueue(self.c_pointer, node.c_pointer)
	def postEventFromUser(self, event):
		return ISceneManager_postEventFromUser(self.c_pointer, event)
	def clear(self):
		ISceneManager_clear(self.c_pointer)
	def getParameters(self):
		return IAttributes(ISceneManager_getParameters(self.c_pointer))
	def getSceneNodeRenderPass(self):
		return ISceneManager_getSceneNodeRenderPass(self.c_pointer)
	def getDefaultSceneNodeFactory(self):
		return ISceneManager_getDefaultSceneNodeFactory(self.c_pointer)
	def registerSceneNodeFactory(self, factoryToAdd):
		ISceneManager_registerSceneNodeFactory(self.c_pointer, factoryToAdd.c_pointer)
	def getRegisteredSceneNodeFactoryCount(self):
		return ISceneManager_getRegisteredSceneNodeFactoryCount(self.c_pointer)
	def getSceneNodeFactory(self, index):
		return ISceneNodeFactory(ISceneManager_getSceneNodeFactory(self.c_pointer, index))
	def getDefaultSceneNodeAnimatorFactory(self):
		return ISceneNodeAnimatorFactory(ISceneManager_getDefaultSceneNodeAnimatorFactory(self.c_pointer))
	def registerSceneNodeAnimatorFactory(self, factoryToAdd):
		ISceneManager_registerSceneNodeAnimatorFactory(self.c_pointer, factoryToAdd.c_pointer)
	def getRegisteredSceneNodeAnimatorFactoryCount(self):
		return ISceneManager_getRegisteredSceneNodeAnimatorFactoryCount(self.c_pointer)
	def getSceneNodeAnimatorFactory(self, index):
		return ISceneNodeAnimatorFactory(ISceneManager_getSceneNodeAnimatorFactory(self.c_pointer, index))
	def getSceneNodeTypeName(self, type):
		return ISceneManager_getSceneNodeTypeName(self.c_pointer, type)
	def getAnimatorTypeName(self, type):
		return ISceneManager_getAnimatorTypeName(self.c_pointer, type)
	def addSceneNode(self, sceneNodeTypeName, parent = ISceneNode(0)):
		return ISceneNode(ISceneManager_addSceneNode(self.c_pointer, sceneNodeTypeName, parent.c_pointer))
	def createNewSceneManager(self, cloneContent = False):
		return ISceneManager(ISceneManager_createNewSceneManager(self.c_pointer, cloneContent))
	def saveScene1(self, filename, userDataSerializer = ISceneUserDataSerializer()):
		return ISceneManager_saveScene(self.c_pointer, filename, userDataSerializer.c_pointer)
	def saveScene2(self, file, userDataSerializer = ISceneUserDataSerializer()):
		return ISceneManager_saveScene2(self.c_pointer, file.c_pointer, userDataSerializer.c_pointer)
	def saveScene(self, filename_or_file, userDataSerializer = ISceneUserDataSerializer()):
		if isinstance(filename_or_file, type_str):
			return self.saveScene1(filename_or_file, userDataSerializer)
		else:
			return self.saveScene2(filename_or_file, userDataSerializer)
	def loadScene1(self, filename, userDataSerializer = ISceneUserDataSerializer()):
		return ISceneManager_loadScene(self.c_pointer, filename, userDataSerializer.c_pointer)
	def loadScene2(self, file, userDataSerializer = ISceneUserDataSerializer()):
		return ISceneManager_loadScene2(self.c_pointer, file.c_pointer, userDataSerializer.c_pointer)
	def loadScene(self, filename_or_file, userDataSerializer = ISceneUserDataSerializer()):
		if isinstance(filename_or_file, type_str):
			return self.loadScene1(filename_or_file, userDataSerializer)
		else:
			return self.loadScene2(filename_or_file, userDataSerializer)
	def createMeshWriter(self, type):
		return ISceneManager_createMeshWriter(self.c_pointer, type)
	def createSkinnedMesh(self):
		return ISceneManager_createSkinnedMesh(self.c_pointer)
	def setAmbientLight(self, ambientColor):
		ISceneManager_setAmbientLight(self.c_pointer, ambientColor.c_pointer)
	def getAmbientLight(self):
		return ISceneManager_getAmbientLight(self.c_pointer)
	def setLightManager(self, lightManager):
		ISceneManager_setLightManager(self.c_pointer, lightManager.c_pointer)
	def getGeometryCreator(self):
		return IGeometryCreator(ISceneManager_getGeometryCreator(self.c_pointer))
	def isCulled(self, node):
		return ISceneManager_isCulled(self.c_pointer, node.c_pointer)

class IAnimationEndCallBack(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.callback = OnAnimationEndFunc(self.OnAnimationEnd)
		if len(args) > 0:
			if args[0]:
				self.c_pointer = args[0]
			else:
				self.c_pointer = IAnimationEndCallBack_ctor1()
		else:
			self.c_pointer = IAnimationEndCallBack_ctor2(self.callback)
	def __del__(self):
		if self.c_pointer:
			try:
				IAnimationEndCallBack_delete(self.c_pointer)
			except:
				pass
	def set_func_event(self, event_func):
		IAnimationEndCallBack_set_func_event(self.c_pointer, event_func)
	def OnAnimationEnd(self, node):
		'must be replaced with custom animation end callback class'
	def convert_pointer(self):
		self.c_pointer = IAnimationEndCallBack_UserAnimationEndCallBack(self.c_pointer)

class IAnimatedMeshSceneNode(ISceneNode):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
	def __del__(self):
		if self.c_pointer:
			try:
				IAnimatedMeshSceneNode_delete(self.c_pointer)
			except:
				pass
	def setCurrentFrame(self, frame):
		IAnimatedMeshSceneNode_setCurrentFrame(self.c_pointer, frame)
	def setFrameLoop(self, begin, end):
		return IAnimatedMeshSceneNode_setFrameLoop(self.c_pointer, begin, end)
	def setAnimationSpeed(self, framesPerSecond):
		IAnimatedMeshSceneNode_setAnimationSpeed(self.c_pointer, framesPerSecond)
	def getAnimationSpeed(self):
		return IAnimatedMeshSceneNode_getAnimationSpeed(self.c_pointer)
	def addShadowVolumeSceneNode(self, shadowMesh = IMesh(0), id = -1, zfailmethod = True, infinity = 10000.0):
		return IAnimatedMeshSceneNode_addShadowVolumeSceneNode(self.c_pointer, shadowMesh.c_pointer, id, zfailmethod, infinity)
	def getJointNode1(self, jointName):
		return IAnimatedMeshSceneNode_getJointNode1(self.c_pointer, jointName)
	def getJointNode2(self, jointID):
		return IAnimatedMeshSceneNode_getJointNode2(self.c_pointer, jointID)
	def getJointNode(self, arg):
		if isinstance(arg, int):
			return self.getJointNode2(arg)
		else:
			return self.getJointNode1(arg)
	def getJointCount(self):
		return IAnimatedMeshSceneNode_getJointCount(self.c_pointer)
	def setMD2Animation1(self, emd2_anim_type):
		return IAnimatedMeshSceneNode_setMD2Animation1(self.c_pointer, emd2_anim_type)
	def setMD2Animation2(self, animationName):
		return IAnimatedMeshSceneNode_setMD2Animation2(self.c_pointer, animationName)
	def setMD2Animation(self, arg):
		if isinstance(arg, int):
			return self.setMD2Animation1(arg)
		else:
			return self.setMD2Animation2(arg)
	def getFrameNr(self):
		return IAnimatedMeshSceneNode_getFrameNr(self.c_pointer)
	def getStartFrame(self):
		return IAnimatedMeshSceneNode_getStartFrame(self.c_pointer)
	def getEndFrame(self):
		return IAnimatedMeshSceneNode_getEndFrame(self.c_pointer)
	def setLoopMode(self, playAnimationLooped):
		IAnimatedMeshSceneNode_setLoopMode(self.c_pointer, playAnimationLooped)
	def setAnimationEndCallback(self, callback):#callback = IAnimationEndCallBack(0)
		IAnimatedMeshSceneNode_setAnimationEndCallback(self.c_pointer, callback.c_pointer)
	def setReadOnlyMaterials(self, readonly):
		IAnimatedMeshSceneNode_setReadOnlyMaterials(self.c_pointer, readonly)
	def isReadOnlyMaterials(self):
		return IAnimatedMeshSceneNode_isReadOnlyMaterials(self.c_pointer)
	def setMesh(self, mesh):
		IAnimatedMeshSceneNode_setMesh(self.c_pointer, mesh.c_pointer)
	def getMesh(self):
		return IAnimatedMesh(IAnimatedMeshSceneNode_getMesh(self.c_pointer))
	def getMD3TagTransformation(self, tagname):
		return IAnimatedMeshSceneNode_getMD3TagTransformation(self.c_pointer, tagname)
	def setJointMode(self, mode):
		IAnimatedMeshSceneNode_setJointMode(self.c_pointer, mode)
	def setTransitionTime(self, Time):
		IAnimatedMeshSceneNode_setTransitionTime(self.c_pointer, Time)
	def animateJoints(self, CalculateAbsolutePositions = True):
		IAnimatedMeshSceneNode_animateJoints(self.c_pointer, CalculateAbsolutePositions)
	def setRenderFromIdentity(self, On):
		IAnimatedMeshSceneNode_setRenderFromIdentity(self.c_pointer, On)
	def clone(self, newParent = ISceneNode(0), newManager = ISceneManager(0)):
		return ISceneNode(IAnimatedMeshSceneNode_clone(self.c_pointer, newParent.c_pointer, newManager.c_pointer))

class IGUIEnvironment(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def drawAll(self):
		IGUIEnvironment_drawAll(self.c_pointer)
	def setFocus(self, element):
		return IGUIEnvironment_setFocus(self.c_pointer, element.c_pointer)
	def getFocus(self):
		return IGUIEnvironment_getFocus(self.c_pointer)
	def removeFocus(self, element):
		return IGUIEnvironment_removeFocus(self.c_pointer, element.c_pointer)
	def hasFocus(self, element):
		return IGUIEnvironment_hasFocus(self.c_pointer, element.c_pointer)
	def getVideoDriver(self):
		return IVideoDriver(IGUIEnvironment_getVideoDriver(self.c_pointer))
	def getFileSystem(self):
		return IFileSystem(IGUIEnvironment_getFileSystem(self.c_pointer))
	def getOSOperator(self):
		return IOSOperator(IGUIEnvironment_getOSOperator(self.c_pointer))
	def clear(self):
		IGUIEnvironment_clear(self.c_pointer)
	def postEventFromUser(self, event):
		return IGUIEnvironment_postEventFromUser(self.c_pointer, event)
	def setUserEventReceiver(self, evr):
		IGUIEnvironment_setUserEventReceiver(self.c_pointer, evr.c_pointer)
	def getSkin(self):
		return IGUISkin(IGUIEnvironment_getSkin(self.c_pointer))
	def setSkin(self, skin):
		IGUIEnvironment_setSkin(self.c_pointer, skin.c_pointer)
	def createSkin(self, type):
		return IGUISkin(IGUIEnvironment_createSkin(self.c_pointer, type))
	def createImageList(self, texture, imageSize, useAlphaChannel):
		return IGUIImageList(IGUIEnvironment_createImageList(self.c_pointer, texture.c_pointer, imageSize.c_pointer, useAlphaChannel))
	def getFont(self, filename):
		return IGUIFont(IGUIEnvironment_getFont(self.c_pointer, as_ansi(filename)))
	def getBuiltInFont(self):
		return IGUIFont(IGUIEnvironment_getBuiltInFont(self.c_pointer))
	def getSpriteBank(self, filename):
		return IGUISpriteBank(IGUIEnvironment_getSpriteBank(self.c_pointer, as_ansi(filename)))
	def addEmptySpriteBank(self, name):
		return IGUISpriteBank(IGUIEnvironment_addEmptySpriteBank(self.c_pointer, as_ansi(name)))
	def getRootGUIElement(self):
		return IGUIElement(IGUIEnvironment_getRootGUIElement(self.c_pointer))
	def addButton(self, rectangle, parent = IGUIElement(), id = -1, text = '', tooltiptext = ''):
		if not parent:
			parent = IGUIElement()
		return IGUIButton(IGUIEnvironment_addButton(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, text, tooltiptext))
	def addWindow(self, rectangle, modal = False, text = '', parent = IGUIElement(), id = -1):
		return IGUIWindow(IGUIEnvironment_addWindow(self.c_pointer, rectangle.c_pointer, modal, text, parent.c_pointer, id))
	def addModalScreen(self, parent):
		return IGUIElement(IGUIEnvironment_addModalScreen(self.c_pointer, parent.c_pointer))
	def addMessageBox(self, caption, text = '', modal = True, flags = EMBF_OK, parent = IGUIElement(), id = -1, return_pointer = False):
		if return_pointer:
			return IGUIEnvironment_addMessageBox(self.c_pointer, caption, text, modal, flags, parent.c_pointer, id)
		else:
			return IGUIWindow(IGUIEnvironment_addMessageBox(self.c_pointer, caption, text, modal, flags, parent.c_pointer, id))
	def addScrollBar(self, horizontal, rectangle, parent = IGUIElement(), id = -1):
		if not parent:
			parent = IGUIElement()
		return IGUIScrollBar(IGUIEnvironment_addScrollBar(self.c_pointer, horizontal, rectangle.c_pointer, parent.c_pointer, id))
	def addImage(self, *args):
		if isinstance(args[0], ITexture):
			image, pos, useAlphaChannel, parent, id, text = None, None, True, IGUIElement(), -1, ''
			if len(args) == 2:
				image, pos = args
			elif len(args) == 3:
				image, pos, useAlphaChannel = args
			elif len(args) == 4:
				image, pos, useAlphaChannel, parent = args
			elif len(args) == 5:
				image, pos, useAlphaChannel, parent, id = args
			elif len(args) > 5:
				image, pos, useAlphaChannel, parent, id, text = args
			return IGUIImage(IGUIEnvironment_addImage(self.c_pointer, image.c_pointer, pos.c_pointer, useAlphaChannel, parent.c_pointer, id, text))
		else:
			rectangle, parent, id, text = None, IGUIElement(), -1, ''
			if len(args) == 2:
				rectangle, parent = args
			elif len(args) == 3:
				rectangle, parent, id = args
			elif len(args) == 4:
				rectangle, parent, id, text = args
			return IGUIImage(IGUIEnvironment_addImage2(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, text))
	def addImage1(self, image, pos, useAlphaChannel = True, parent = IGUIElement(), id = -1, text = ''):
		return IGUIImage(IGUIEnvironment_addImage(self.c_pointer, image.c_pointer, pos.c_pointer, useAlphaChannel, parent, id, text))
	def addImage2(self, rectangle, parent = IGUIElement(), id = -1, text = ''):
		return IGUIImage(IGUIEnvironment_addImage2(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, text))
	def addCheckBox(self, checked, rectangle, parent = IGUIElement(), id = -1, text = ''):
		return IGUICheckBox(IGUIEnvironment_addCheckBox(self.c_pointer, checked, rectangle.c_pointer, parent.c_pointer, id, text))
	def addListBox(self, rectangle, parent = IGUIElement(), id = -1, drawBackground = False):
		return IGUIListBox(IGUIEnvironment_addListBox(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, drawBackground))
	def addTreeView(self, rectangle, parent = IGUIElement(), id = -1, drawBackground = False, scrollBarVertical = True, scrollBarHorizontal = False):
		return IGUITreeView(IGUIEnvironment_addTreeView(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, drawBackground, scrollBarVertical, scrollBarHorizontal))
	def addMeshViewer(self, rectangle, parent = IGUIElement(), id = -1, text = ''):
		return IGUIMeshViewer(IGUIEnvironment_addMeshViewer(self.c_pointer, rectangle, parent.c_pointer, id, text))
	if IRRLICHT_VERSION < 180:
		def addFileOpenDialog(self, title = '', modal = True, parent = IGUIElement(), id = -1):
			return IGUIFileOpenDialog(IGUIEnvironment_addFileOpenDialog(self.c_pointer, title, modal, parent.c_pointer, id))
	else:
		def addFileOpenDialog(self, title = '', modal = True, parent = IGUIElement(), id = -1, restoreCWD = False, startDir = ''):
			return IGUIFileOpenDialog(IGUIEnvironment_addFileOpenDialog(self.c_pointer, title, modal, parent.c_pointer, id, restoreCWD, startDir))
	if BUILD_WITH_GUI_FILE_SELECTOR:
		def addFileSelectorDialog(self, title = '', modal = True, parent = IGUIElement(), id = -1, rectangle = recti(0,0,350,265), type = EFST_OPEN_DIALOG):
			return CGUIFileSelector(IGUIEnvironment_addFileSelectorDialog(self.c_pointer, title, modal, parent.c_pointer, id, rectangle.c_pointer, type))
	def addColorSelectDialog(self, title = '', modal = True, parent = IGUIElement(), id = -1):
		return IGUIColorSelectDialog(IGUIEnvironment_addColorSelectDialog(self.c_pointer, title, modal, parent.c_pointer, id))
	def addStaticText(self, text, rectangle, border = False, wordWrap = True, parent = IGUIElement(), id = -1, fillBackground = False):
		return IGUIStaticText(IGUIEnvironment_addStaticText(self.c_pointer, text, rectangle.c_pointer, border, wordWrap, parent.c_pointer, id, fillBackground))
	def addEditBox(self, text, rectangle, border = True, parent = IGUIElement(), id = -1):
		return IGUIEditBox(IGUIEnvironment_addEditBox(self.c_pointer, text, rectangle.c_pointer, border, parent.c_pointer, id))
	def addSpinBox(self, text, rectangle, border = True, parent = IGUIElement(), id = -1):
		return IGUISpinBox(IGUIEnvironment_addSpinBox(self.c_pointer, text, rectangle.c_pointer, border, parent.c_pointer, id))
	def addInOutFader(self, rectangle = 0, parent = IGUIElement(), id = -1):
		return IGUIInOutFader(IGUIEnvironment_addInOutFader(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id))
	def addTabControl(self, rectangle, parent = IGUIElement(), fillbackground = False, border = True, id = -1):
		return IGUITabControl(IGUIEnvironment_addTabControl(self.c_pointer, rectangle.c_pointer, parent.c_pointer, fillbackground, border, id))
	def addTab(self, rectangle, parent = IGUIElement(), id = -1):
		return IGUITab(IGUIEnvironment_addTab(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id))
	def addContextMenu(self, rectangle, parent = IGUIElement(), id = -1):
		return IGUIContextMenu(IGUIEnvironment_addContextMenu(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id))
	def addMenu(self, parent = IGUIElement(), id = -1):
		return IGUIContextMenu(IGUIEnvironment_addMenu(self.c_pointer, parent.c_pointer, id))
	def addToolBar(self, parent = IGUIElement(), id = -1):
		return IGUIToolBar(IGUIEnvironment_addToolBar(self.c_pointer, parent.c_pointer, id))
	def addComboBox(self, rectangle, parent = IGUIElement(), id = -1):
		return IGUIComboBox(IGUIEnvironment_addComboBox(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id))
	def addTable(self, rectangle, parent = IGUIElement(), id = -1, drawBackground = False):
		return IGUITable(IGUIEnvironment_addTable(self.c_pointer, rectangle.c_pointer, parent.c_pointer, id, drawBackground))
	def getDefaultGUIElementFactory(self):
		return IGUIElementFactory(IGUIEnvironment_getDefaultGUIElementFactory(self.c_pointer))
	def registerGUIElementFactory(self, factoryToAdd):
		IGUIEnvironment_registerGUIElementFactory(self.c_pointer, factoryToAdd.c_pointer)
	def getRegisteredGUIElementFactoryCount(self):
		return IGUIEnvironment_getRegisteredGUIElementFactoryCount(self.c_pointer)
	def getGUIElementFactory(self, index):
		return IGUIEnvironment_getGUIElementFactory(self.c_pointer, index)
	def addGUIElement(self, elementName, parent = IGUIElement()):
		return IGUIEnvironment_addGUIElement(self.c_pointer, elementName, parent.c_pointer)
	def saveGUI(self, file_or_filename, start = IGUIElement()):
		if isinstance(file_or_filename, str):
			return IGUIEnvironment_saveGUI(self.c_pointer, file_or_filename, start.c_pointer)
		else:
			return IGUIEnvironment_saveGUI2(self.c_pointer, file_or_filename, start.c_pointer)
	def saveGUI1(self, filename, start = IGUIElement()):
		return IGUIEnvironment_saveGUI(self.c_pointer, filename, start.c_pointer)
	def saveGUI2(self, file, start = IGUIElement()):
		return IGUIEnvironment_saveGUI2(self.c_pointer, file, start.c_pointer)
	def loadGUI(self, file_or_filename, parent = IGUIElement()):
		if isinstance(file_or_filename, str):
			return IGUIEnvironment_loadGUI(self.c_pointer, file_or_filename, parent.c_pointer)
		else:
			return IGUIEnvironment_loadGUI2(self.c_pointer, file_or_filename, parent.c_pointer)
	def loadGUI1(self, filename, parent = IGUIElement()):
		return IGUIEnvironment_loadGUI(self.c_pointer, filename, parent.c_pointer)
	def loadGUI2(self, file, parent = IGUIElement()):
		return IGUIEnvironment_loadGUI2(self.c_pointer, file, parent.c_pointer)
	def serializeAttributes(self, out, options=0):
		IGUIEnvironment_serializeAttributes(self.c_pointer, out, options)
	def deserializeAttributes(self, inp, options=0):
		IGUIEnvironment_deserializeAttributes(self.c_pointer, inp, options)
	def writeGUIElement(self, writer, node):
		IGUIEnvironment_writeGUIElement(self.c_pointer, writer, node)
	def readGUIElement(self, reader, node):
		IGUIEnvironment_readGUIElement(self.c_pointer, reader, node)

class IReadFile(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def read(self, buffer, sizeToRead):
		return IReadFile_read(self.c_pointer, buffer, sizeToRead)
	def seek(self, finalPos, relativeMovement =  False):
		return IReadFile_seek(self.c_pointer, finalPos, relativeMovement)
	def getSize(self):
		return IReadFile_getSize(self.c_pointer)
	def getPos(self):
		return IReadFile_getPos(self.c_pointer)
	def getFileName(self):
		return IReadFile_getFileName(self.c_pointer)

class IXMLReader(type_unicode, IReferenceCounted):
	def __init__(self, *args, **kwargs):
		IReferenceCounted.__init__(self, *args, **kwargs)
		self.c_pointer = args[0]
	def __nonzero__(self):
		return bool(self.c_pointer)
	def __bool__(self):
		return bool(self.c_pointer)
	def read(self):
		return IXMLReader_read(self.c_pointer)
	def getNodeType(self):
		return IXMLReader_getNodeType(self.c_pointer)
	def getAttributeCount(self):
		return IXMLReader_getAttributeCount(self.c_pointer)
	def getAttributeName(self, idx):
		return IXMLReader_getAttributeName(self.c_pointer, idx)
	def getAttributeValue1(self, idx):
		return IXMLReader_getAttributeValue1(self.c_pointer, idx)
	def getAttributeValue2(self, name):
		return IXMLReader_getAttributeValue2(self.c_pointer, name)
	def getAttributeValue(self, value):
		if isinstance(value, int):
			return IXMLReader_getAttributeValue1(self.c_pointer, value)
		else:
			return IXMLReader_getAttributeValue2(self.c_pointer, value)
	def getAttributeValueSafe(self, name):
		return IXMLReader_getAttributeValueSafe(self.c_pointer, name)
	def getAttributeValueAsInt1(self, name):
		return IXMLReader_getAttributeValueAsInt1(self.c_pointer, name)
	def getAttributeValueAsInt2(self, idx):
		return IXMLReader_getAttributeValueAsInt2(self.c_pointer, idx)
	def getAttributeValueAsInt(self, value):
		if isinstance(value, int):
			return IXMLReader_getAttributeValueAsInt2(self.c_pointer, value)
		else:
			return IXMLReader_getAttributeValueAsInt1(self.c_pointer, value)
	def getAttributeValueAsFloat1(self, name):
		return IXMLReader_getAttributeValueAsFloat1(self.c_pointer, name)
	def getAttributeValueAsFloat2(self, idx):
		return IXMLReader_getAttributeValueAsFloat2(self.c_pointer, idx)
	def getAttributeValueAsFloat(self, value):
		if isinstance(value, int):
			return IXMLReader_getAttributeValueAsFloat2(self.c_pointer, value)
		else:
			return IXMLReader_getAttributeValueAsFloat1(self.c_pointer, value)
	def getNodeName(self):
		return IXMLReader_getNodeName(self.c_pointer)
	def getNodeData(self):
		return IXMLReader_getNodeData(self.c_pointer)
	def isEmptyElement(self):
		return IXMLReader_isEmptyElement(self.c_pointer)
	def getSourceFormat(self):
		return IXMLReader_getSourceFormat(self.c_pointer)
	def getParserFormat(self):
		return IXMLReader_getParserFormat(self.c_pointer)

class IXMLReaderUTF8(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def read(self):
		return IXMLReaderUTF8_read(self.c_pointer)
	def getNodeType(self):
		return IXMLReaderUTF8_getNodeType(self.c_pointer)
	def getAttributeCount(self):
		return IXMLReaderUTF8_getAttributeCount(self.c_pointer)
	def getAttributeName(self, idx):
		return IXMLReaderUTF8_getAttributeName(self.c_pointer, idx)
	def getAttributeValue1(self, idx):
		return IXMLReaderUTF8_getAttributeValue1(self.c_pointer, idx)
	def getAttributeValue2(self, name):
		return IXMLReaderUTF8_getAttributeValue2(self.c_pointer, name)
	def getAttributeValue(self, value):
		if isinstance(value, int):
			return IXMLReaderUTF8_getAttributeValue1(self.c_pointer, value)
		else:
			return IXMLReaderUTF8_getAttributeValue2(self.c_pointer, value)
	def getAttributeValueSafe(self, name):
		return IXMLReaderUTF8_getAttributeValueSafe(self.c_pointer, name)
	def getAttributeValueAsInt1(self, name):
		return IXMLReaderUTF8_getAttributeValueAsInt1(self.c_pointer, name)
	def getAttributeValueAsInt2(self, idx):
		return IXMLReaderUTF8_getAttributeValueAsInt2(self.c_pointer, idx)
	def getAttributeValueAsInt(self, value):
		if isinstance(value, int):
			return IXMLReaderUTF8_getAttributeValueAsInt2(self.c_pointer, value)
		else:
			return IXMLReaderUTF8_getAttributeValueAsInt1(self.c_pointer, value)
	def getAttributeValueAsFloat1(self, name):
		return IXMLReaderUTF8_getAttributeValueAsFloat1(self.c_pointer, name)
	def getAttributeValueAsFloat2(self, idx):
		return IXMLReaderUTF8_getAttributeValueAsFloat2(self.c_pointer, idx)
	def getAttributeValueAsFloat(self, value):
		if isinstance(value, int):
			return IXMLReaderUTF8_getAttributeValueAsFloat2(self.c_pointer, value)
		else:
			return IXMLReaderUTF8_getAttributeValueAsFloat1(self.c_pointer, value)
	def getNodeName(self):
		return IXMLReaderUTF8_getNodeName(self.c_pointer)
	def getNodeData(self):
		return IXMLReaderUTF8_getNodeData(self.c_pointer)
	def isEmptyElement(self):
		return IXMLReaderUTF8_isEmptyElement(self.c_pointer)
	def getSourceFormat(self):
		return IXMLReaderUTF8_getSourceFormat(self.c_pointer)
	def getParserFormat(self):
		return IXMLReaderUTF8_getParserFormat(self.c_pointer)

class IWriteFile(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	def write(self, buffer, sizeToWrite):
		return IWriteFile_write(self.c_pointer, buffer, sizeToWrite)
	def seek(self, finalPos, relativeMovement = False):
		return IWriteFile_seek(self.c_pointer, finalPos, relativeMovement)
	def getPos(self):
		return IWriteFile_getPos(self.c_pointer)
	def getFileName(self):
		return IWriteFile_getFileName(self.c_pointer)

class IXMLWriter(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			self.c_pointer = args[0]
	#~ def Destructor(self):
		#~ IXMLWriter_Destructor(self.c_pointer)
	def writeXMLHeader(self):
		IXMLWriter_writeXMLHeader(self.c_pointer)
	def writeElement1(self, name, empty = False, attr1Name = '', attr1Value = '', attr2Name = '', attr2Value = '', attr3Name = '', attr3Value = '', attr4Name = '', attr4Value = '', attr5Name = '', attr5Value = ''):
		IXMLWriter_writeElement1(self.c_pointer, name, empty, attr1Name, attr1Value, attr2Name, attr2Value, attr3Name, attr3Value, attr4Name, attr4Value, attr5Name, attr5Value)
	def writeElement2(self, name, empty, names, values):
		IXMLWriter_writeElement2(self.c_pointer, name, empty, names, values)
	def writeElement(self, *args, **kwargs):
		if len(args) > 4 and (not 'names' or 'values' in kwargs):
			self.writeElement1(*args, **kwargs)
		else:
			self.writeElement2(*args, **kwargs)
	def writeComment(self, comment):
		IXMLWriter_writeComment(self.c_pointer, comment)
	def writeClosingTag(self, name):
		IXMLWriter_writeClosingTag(self.c_pointer, name)
	def writeText(self, text):
		IXMLWriter_writeText(self.c_pointer, text)
	def writeLineBreak(self):
		IXMLWriter_writeLineBreak(self.c_pointer)

class ILogger(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	#~ def Destructor(self):
		#~ ILogger_Destructor(self.c_pointer)
	def getLogLevel(self):
		return ILogger_getLogLevel(self.c_pointer)
	def setLogLevel(self, ll):
		ILogger_setLogLevel(self.c_pointer, ll)
	def log(self, text, ll=ELL_INFORMATION):
		ILogger_log(self.c_pointer, as_ansi(text), ll)
	def log2(self, text, hint, ll=ELL_INFORMATION):
		ILogger_log2(self.c_pointer, as_ansi(text), as_ansi(hint), ll)
	def log3(self, text, hint, ll=ELL_INFORMATION):
		ILogger_log3(self.c_pointer, as_ansi(text), hint, ll)
	def log4(self, text, hint, ll=ELL_INFORMATION):
		ILogger_log4(self.c_pointer, text, hint, ll)
	def log5(self, text, ll=ELL_INFORMATION):
		ILogger_log5(self.c_pointer, text, ll)

class IVideoModeList(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getVideoModeCount(self):
		return IVideoModeList_getVideoModeCount(self.c_pointer)
	def getVideoModeResolution1(self, modeNumber):
		return dimension2du(pointer = IVideoModeList_getVideoModeResolution(self.c_pointer, modeNumber))
	def getVideoModeResolution2(self, minSize, maxSize):
		return dimension2du(pointer = IVideoModeList_getVideoModeResolution2(self.c_pointer, minSize, maxSize))
	def getVideoModeResolution(self, *args):
		if len(args) == 1:
			return self.getVideoModeResolution1(*args)
		elif len(args) > 1:
			return self.getVideoModeResolution2(*args)
	def getVideoModeDepth(self, modeNumber):
		return IVideoModeList_getVideoModeDepth(self.c_pointer, modeNumber)
	def getDesktopResolution(self):
		return dimension2du(pointer = IVideoModeList_getDesktopResolution(self.c_pointer))
	def getDesktopDepth(self):
		return IVideoModeList_getDesktopDepth(self.c_pointer)

class IOSOperator(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	if IRRLICHT_VERSION < 180:
		def getOperationSystemVersion(self):
			return IOSOperator_getOperationSystemVersion(self.c_pointer)
	def copyToClipboard(self, text):
		IOSOperator_copyToClipboard(self.c_pointer, text)
	def getTextFromClipboard(self):
		return IOSOperator_getTextFromClipboard(self.c_pointer)
	def getProcessorSpeedMHz(self, MHz):
		return IOSOperator_getProcessorSpeedMHz(self.c_pointer, MHz)
	def getProcessorSpeedMHzAsTuple(self):
		MHz = ctypes.c_uint()
		result = IOSOperator_getProcessorSpeedMHz(self.c_pointer, ctypes.byref(MHz))
		return result, MHz.value
	def getSystemMemory(self, Total, Avail):
		return IOSOperator_getSystemMemory(self.c_pointer, Total, Avail)
	def getSystemMemoryAsTuple(self):
		Total, Avail = ctypes.c_uint(), ctypes.c_uint()
		result = IOSOperator_getSystemMemory(self.c_pointer, ctypes.byref(Total), ctypes.byref(Avail))
		return result, Total.value, Avail.value

class Q3LevelLoadParameter(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = Q3LevelLoadParameter_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = Q3LevelLoadParameter_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return Q3LevelLoadParameter(c_pointer = Q3LevelLoadParameter_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		Q3LevelLoadParameter_set_item(self.c_pointer, item.c_pointer, index)
	def get_defaultLightMapMaterial(self):
		return Q3LevelLoadParameter_get_defaultLightMapMaterial(self.c_pointer)
	def set_defaultLightMapMaterial(self, value):
		Q3LevelLoadParameter_set_defaultLightMapMaterial(self.c_pointer, value)
	defaultLightMapMaterial = property(get_defaultLightMapMaterial, set_defaultLightMapMaterial)
	def get_defaultModulate(self):
		return Q3LevelLoadParameter_get_defaultModulate(self.c_pointer)
	def set_defaultModulate(self, value):
		Q3LevelLoadParameter_set_defaultModulate(self.c_pointer, value)
	defaultModulate = property(get_defaultModulate, set_defaultModulate)
	def get_defaultFilter(self):
		return Q3LevelLoadParameter_get_defaultFilter(self.c_pointer)
	def set_defaultFilter(self, value):
		Q3LevelLoadParameter_set_defaultFilter(self.c_pointer, value)
	defaultFilter = property(get_defaultFilter, set_defaultFilter)
	def get_patchTesselation(self):
		return Q3LevelLoadParameter_get_patchTesselation(self.c_pointer)
	def set_patchTesselation(self, value):
		Q3LevelLoadParameter_set_patchTesselation(self.c_pointer, value)
	patchTesselation = property(get_patchTesselation, set_patchTesselation)
	def get_verbose(self):
		return Q3LevelLoadParameter_get_verbose(self.c_pointer)
	def set_verbose(self, value):
		Q3LevelLoadParameter_set_verbose(self.c_pointer, value)
	verbose = property(get_verbose, set_verbose)
	def get_startTime(self):
		return Q3LevelLoadParameter_get_startTime(self.c_pointer)
	def set_startTime(self, value):
		Q3LevelLoadParameter_set_startTime(self.c_pointer, value)
	startTime = property(get_startTime, set_startTime)
	def get_endTime(self):
		return Q3LevelLoadParameter_get_endTime(self.c_pointer)
	def set_endTime(self, value):
		Q3LevelLoadParameter_set_endTime(self.c_pointer, value)
	endTime = property(get_endTime, set_endTime)
	def get_mergeShaderBuffer(self):
		return Q3LevelLoadParameter_get_mergeShaderBuffer(self.c_pointer)
	def set_mergeShaderBuffer(self, value):
		Q3LevelLoadParameter_set_mergeShaderBuffer(self.c_pointer, value)
	mergeShaderBuffer = property(get_mergeShaderBuffer, set_mergeShaderBuffer)
	def get_cleanUnResolvedMeshes(self):
		return Q3LevelLoadParameter_get_cleanUnResolvedMeshes(self.c_pointer)
	def set_cleanUnResolvedMeshes(self, value):
		Q3LevelLoadParameter_set_cleanUnResolvedMeshes(self.c_pointer, value)
	cleanUnResolvedMeshes = property(get_cleanUnResolvedMeshes, set_cleanUnResolvedMeshes)
	def get_loadAllShaders(self):
		return Q3LevelLoadParameter_get_loadAllShaders(self.c_pointer)
	def set_loadAllShaders(self, value):
		Q3LevelLoadParameter_set_loadAllShaders(self.c_pointer, value)
	loadAllShaders = property(get_loadAllShaders, set_loadAllShaders)
	def get_loadSkyShader(self):
		return Q3LevelLoadParameter_get_loadSkyShader(self.c_pointer)
	def set_loadSkyShader(self, value):
		Q3LevelLoadParameter_set_loadSkyShader(self.c_pointer, value)
	loadSkyShader = property(get_loadSkyShader, set_loadSkyShader)
	def get_alpharef(self):
		return Q3LevelLoadParameter_get_alpharef(self.c_pointer)
	def set_alpharef(self, value):
		Q3LevelLoadParameter_set_alpharef(self.c_pointer, value)
	alpharef = property(get_alpharef, set_alpharef)
	def get_swapLump(self):
		return Q3LevelLoadParameter_get_swapLump(self.c_pointer)
	def set_swapLump(self, value):
		Q3LevelLoadParameter_set_swapLump(self.c_pointer, value)
	swapLump = property(get_swapLump, set_swapLump)
	def get_swapHeader(self):
		return Q3LevelLoadParameter_get_swapHeader(self.c_pointer)
	def set_swapHeader(self, value):
		Q3LevelLoadParameter_set_swapHeader(self.c_pointer, value)
	swapHeader = property(get_swapHeader, set_swapHeader)
	def get_scriptDir(self):
		return Q3LevelLoadParameter_get_scriptDir(self.c_pointer)
	def set_scriptDir(self, value):
		Q3LevelLoadParameter_set_scriptDir(self.c_pointer, value[64])
	scriptDir = property(get_scriptDir, set_scriptDir)
	def size(self):
		return Q3LevelLoadParameter_size(self.c_pointer)

class SBlendFunc(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = SBlendFunc_ctor(args[0])
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SBlendFunc(c_pointer = SBlendFunc_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SBlendFunc_set_item(self.c_pointer, item.c_pointer, index)
	def get_type(self):
		return SBlendFunc_get_type(self.c_pointer)
	def set_type(self, value):
		SBlendFunc_set_type(self.c_pointer, value)
	type = property(get_type, set_type)
	def get_modulate(self):
		return SBlendFunc_get_modulate(self.c_pointer)
	def set_modulate(self, value):
		SBlendFunc_set_modulate(self.c_pointer, value)
	modulate = property(get_modulate, set_modulate)
	def get_param0(self):
		return SBlendFunc_get_param0(self.c_pointer)
	def set_param0(self, value):
		SBlendFunc_set_param0(self.c_pointer, value)
	param0 = property(get_param0, set_param0)
	def get_isTransparent(self):
		return SBlendFunc_get_isTransparent(self.c_pointer)
	def set_isTransparent(self, value):
		SBlendFunc_set_isTransparent(self.c_pointer, value)
	isTransparent = property(get_isTransparent, set_isTransparent)

class Noiser(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = Noiser_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = Noiser_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return Noiser(c_pointer = Noiser_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		Noiser_set_item(self.c_pointer, item.c_pointer, index)
	def get(self):
		return Noiser_get(self.c_pointer)

class SModifierFunction(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SModifierFunction_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = SModifierFunction_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SModifierFunction(c_pointer = SModifierFunction_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SModifierFunction_set_item(self.c_pointer, item.c_pointer, index)
	def get_masterfunc0(self):
		return SModifierFunction_get_masterfunc0(self.c_pointer)
	def set_masterfunc0(self, value):
		SModifierFunction_set_masterfunc0(self.c_pointer, value)
	masterfunc0 = property(get_masterfunc0, set_masterfunc0)
	def get_masterfunc1(self):
		return SModifierFunction_get_masterfunc1(self.c_pointer)
	def set_masterfunc1(self, value):
		SModifierFunction_set_masterfunc1(self.c_pointer, value)
	masterfunc1 = property(get_masterfunc1, set_masterfunc1)
	def get_func(self):
		return SModifierFunction_get_func(self.c_pointer)
	def set_func(self, value):
		SModifierFunction_set_func(self.c_pointer, value)
	func = property(get_func, set_func)
	def get_tcgen(self):
		return SModifierFunction_get_tcgen(self.c_pointer)
	def set_tcgen(self, value):
		SModifierFunction_set_tcgen(self.c_pointer, value)
	tcgen = property(get_tcgen, set_tcgen)
	def get_rgbgen(self):
		return SModifierFunction_get_rgbgen(self.c_pointer)
	def set_rgbgen(self, value):
		SModifierFunction_set_rgbgen(self.c_pointer, value)
	rgbgen = property(get_rgbgen, set_rgbgen)
	def get_alphagen(self):
		return SModifierFunction_get_alphagen(self.c_pointer)
	def set_alphagen(self, value):
		SModifierFunction_set_alphagen(self.c_pointer, value)
	alphagen = property(get_alphagen, set_alphagen)
	def get_base(self):
		return SModifierFunction_get_base(self.c_pointer)
	def set_base(self, value):
		SModifierFunction_set_base(self.c_pointer, value)
	base = property(get_base, set_base)
	def get_bulgewidth(self):
		return SModifierFunction_get_bulgewidth(self.c_pointer)
	def set_bulgewidth(self, value):
		SModifierFunction_set_bulgewidth(self.c_pointer, value)
	bulgewidth = property(get_bulgewidth, set_bulgewidth)
	def get_amp(self):
		return SModifierFunction_get_amp(self.c_pointer)
	def set_amp(self, value):
		SModifierFunction_set_amp(self.c_pointer, value)
	amp = property(get_amp, set_amp)
	def get_bulgeheight(self):
		return SModifierFunction_get_bulgeheight(self.c_pointer)
	def set_bulgeheight(self, value):
		SModifierFunction_set_bulgeheight(self.c_pointer, value)
	bulgeheight = property(get_bulgeheight, set_bulgeheight)
	def get_phase(self):
		return SModifierFunction_get_phase(self.c_pointer)
	def set_phase(self, value):
		SModifierFunction_set_phase(self.c_pointer, value)
	phase = property(get_phase, set_phase)
	def get_frequency(self):
		return SModifierFunction_get_frequency(self.c_pointer)
	def set_frequency(self, value):
		SModifierFunction_set_frequency(self.c_pointer, value)
	frequency = property(get_frequency, set_frequency)
	def get_bulgespeed(self):
		return SModifierFunction_get_bulgespeed(self.c_pointer)
	def set_bulgespeed(self, value):
		SModifierFunction_set_bulgespeed(self.c_pointer, value)
	bulgespeed = property(get_bulgespeed, set_bulgespeed)
	def get_wave(self):
		return SModifierFunction_get_wave(self.c_pointer)
	def set_wave(self, value):
		SModifierFunction_set_wave(self.c_pointer, value)
	wave = property(get_wave, set_wave)
	def get_div(self):
		return SModifierFunction_get_div(self.c_pointer)
	def set_div(self, value):
		SModifierFunction_set_div(self.c_pointer, value)
	div = property(get_div, set_div)
	def get_x(self):
		return SModifierFunction_get_x(self.c_pointer)
	def set_x(self, value):
		SModifierFunction_set_x(self.c_pointer, value)
	x = property(get_x, set_x)
	def get_y(self):
		return SModifierFunction_get_y(self.c_pointer)
	def set_y(self, value):
		SModifierFunction_set_y(self.c_pointer, value)
	y = property(get_y, set_y)
	def get_z(self):
		return SModifierFunction_get_z(self.c_pointer)
	def set_z(self, value):
		SModifierFunction_set_z(self.c_pointer, value)
	z = property(get_z, set_z)
	def get_count(self):
		return SModifierFunction_get_count(self.c_pointer)
	def set_count(self, value):
		SModifierFunction_set_count(self.c_pointer, value)
	count = property(get_count, set_count)
	def evaluate(self, dt):
		return SModifierFunction_evaluate(self.c_pointer, dt)

class SVariable(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		if len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			elif len(args) > 0 or len(kwargs) > 0:
				self.c_pointer = self.ctor(*args, **kwargs)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def ctor(self, n, c = None):
		return SVariable_ctor(n, c)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SVariable(c_pointer = SVariable_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SVariable_set_item(self.c_pointer, item.c_pointer, index)
	def get_name(self):
		return SVariable_get_name(self.c_pointer)
	def set_name(self, value):
		SVariable_set_name(self.c_pointer, value)
	name = property(get_name, set_name)
	def get_content(self):
		return SVariable_get_content(self.c_pointer)
	def set_content(self, value):
		SVariable_set_content(self.c_pointer, value)
	content = property(get_content, set_content)
	def clear(self):
		SVariable_clear(self.c_pointer)
	def isValid(self):
		return SVariable_isValid(self.c_pointer)
	def __eq__(self, other):
		return SVariable_operator_eq(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return SVariable_operator_lt(self.c_pointer, other.c_pointer)

class SVarGroup(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SVarGroup_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = SVarGroup_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SVarGroup(c_pointer = SVarGroup_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SVarGroup_set_item(self.c_pointer, item.c_pointer, index)
	def isDefined(self, name, content = None):
		return SVarGroup_isDefined(self.c_pointer, name, content)
	def get(self, name):
		return SVarGroup_get(self.c_pointer, name)
	def set(self, name, content = None):
		SVarGroup_set(self.c_pointer, name, content)
	def get_Variable(self):
		return array(_type_ = SVariable, c_pointer = SVarGroup_get_Variable(self.c_pointer))
	def set_Variable(self, value):
		SVarGroup_set_Variable(self.c_pointer, value.c_pointer)
	Variable = property(get_Variable, set_Variable)

class SVarGroupList(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = SVarGroupList_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = SVarGroupList_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return SVarGroupList(c_pointer = SVarGroupList_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		SVarGroupList_set_item(self.c_pointer, item.c_pointer, index)
	def get_VariableGroup(self):
		return array(_type_ = SVarGroup, c_pointer = SVarGroupList_get_VariableGroup(self.c_pointer))
	def set_VariableGroup(self, value):
		SVarGroupList_set_VariableGroup(self.c_pointer, value.c_pointer)
	VariableGroup = property(get_VariableGroup, set_VariableGroup)

class IShader(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		self.delete_c_pointer = False
		self._size_ = 0
		if len(args) == 0 and len(kwargs) == 0:
			self.c_pointer = IShader_ctor1()
			self.delete_c_pointer = True
		elif len(args) > 0:
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = args[0].c_pointer
			else:
				self._size_ = args[0]
				self.c_pointer = IShader_ctor2(self._size_)
				self.delete_c_pointer = True
		elif 'c_pointer' in kwargs:
			self.c_pointer = kwargs.pop('c_pointer', None)
	def __del__(self):
		if self.delete_c_pointer and self.c_pointer:
			try:
				delete_struct_pointer(self.c_pointer)
			except:
				pass
	def __len__(self):
		return self._size_
	def __getitem__(self, key):
		return self.get_item(key)
	def __setitem__(self, key, value):
		self.set_item(value, key)
	def get_item(self, index = 0):
		return IShader(c_pointer = IShader_get_item(self.c_pointer, index))
	def set_item(self, item, index = 0):
		IShader_set_item(self.c_pointer, item.c_pointer, index)
	def operator_set(self, other):
		IShader_operator_set(self.c_pointer, other.c_pointer)
	def __eq__(self, other):
		return IShader_operator_eq(self.c_pointer, other.c_pointer)
	def __lt__(self, other):
		return IShader_operator_lt(self.c_pointer, other.c_pointer)
	def getGroupSize(self):
		return IShader_getGroupSize(self.c_pointer)
	def getGroup(self, stage):
		return SVarGroup(c_pointer = IShader_getGroup(self.c_pointer, stage))
	def get_ID(self):
		return IShader_get_ID(self.c_pointer)
	def set_ID(self, value):
		IShader_set_ID(self.c_pointer, value)
	def get_VarGroup(self):
		return SVarGroupList(c_pointer = IShader_get_VarGroup(self.c_pointer))
	def set_VarGroup(self, value):
		IShader_set_VarGroup(self.c_pointer, value.c_pointer)
	def get_name(self):
		return IShader_get_name(self.c_pointer)
	def set_name(self, value):
		IShader_set_name(self.c_pointer, value)
	ID = property(get_ID, set_ID)
	VarGroup = property(get_VarGroup, set_VarGroup)
	name = property(get_name, set_name)

class IEntity(IShader):
	pass

class tQ3EntityList:
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) == 0:
			self.c_pointer = tQ3EntityList_ctor()
		elif len(args) > 0:
			self.c_pointer = args[0]
	def __len__(self):
		return int(self.size())
	def __getitem__(self, key):
		return self.get_item(key)
	def reallocate(self, new_size):
		tQ3EntityList_reallocate(self.c_pointer, new_size)
	def setAllocStrategy(self, newStrategy = ALLOC_STRATEGY_DOUBLE):
		tQ3EntityList_setAllocStrategy(self.c_pointer, newStrategy)
	def push_back(self, element):
		tQ3EntityList_push_back(self.c_pointer, element.c_pointer)
	def push_front(self, element):
		tQ3EntityList_push_front(self.c_pointer, element.c_pointer)
	def insert(self, element, index = 0):
		tQ3EntityList_insert(self.c_pointer, element.c_pointer, index)
	def clear(self):
		tQ3EntityList_clear(self.c_pointer)
	def set_pointer(self, newPointer, size, _is_sorted = False, _free_when_destroyed = True):
		tQ3EntityList_set_pointer(self.c_pointer, newPointer, size, _is_sorted, _free_when_destroyed)
	def set_free_when_destroyed(self, f):
		tQ3EntityList_set_free_when_destroyed(self.c_pointer, f)
	def set_used(self, usedNow):
		tQ3EntityList_set_used(self.c_pointer, usedNow)
	def get_item(self, index):
		return IEntity(c_pointer = tQ3EntityList_get_item(self.c_pointer, index))
	def size(self):
		return tQ3EntityList_size(self.c_pointer)
	def empty(self):
		return tQ3EntityList_empty(self.c_pointer)
	def sort(self):
		tQ3EntityList_sort(self.c_pointer)
	def binary_search1(self, element):
		return tQ3EntityList_binary_search1(self.c_pointer, element.c_pointer)
	def binary_search2(self, element, left, right):
		return tQ3EntityList_binary_search2(self.c_pointer, element.c_pointer, left, right)
	def binary_search_multi(self, element, last):
		last_index = ctypes.c_int()
		result = tQ3EntityList_binary_search_multi(self.c_pointer, element.c_pointer, ctypes.byref(last_index))
		last = last_index.value
		return result
	def linear_search(self, element):
		return tQ3EntityList_linear_search(self.c_pointer, element.c_pointer)
	def linear_reverse_search(self, element):
		return tQ3EntityList_linear_reverse_search(self.c_pointer, element.c_pointer)
	def erase1(self, index):
		tQ3EntityList_erase1(self.c_pointer, index)
	def erase2(self, index, count):
		tQ3EntityList_erase2(self.c_pointer, index, count)
	def erase(self, *args):
		if len(args) > 1:
			self.erase2(*args)
		else:
			self.erase1(*args)
	def set_sorted(self, _is_sorted):
		tQ3EntityList_set_sorted(self.c_pointer, _is_sorted)
	def swap(self, other):
		tQ3EntityList_swap(self.c_pointer, other.c_pointer)

class IQ3LevelMesh(IAnimatedMesh):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if len(args) > 0:
			if isinstance(args[0], IAnimatedMesh):
				self.c_pointer = args[0].c_pointer
			else:
				self.c_pointer = args[0]
	def getShader1(self, filename, fileNameIsValid = True):
		return IShader(c_pointer = IQ3LevelMesh_getShader1(self.c_pointer, filename, fileNameIsValid))
	def getShader2(self, index):
		return IShader(c_pointer = IQ3LevelMesh_getShader2(self.c_pointer, index))
	def getShader(self, *args):
		if len(args) > 1:
			return self.getShader1(*args)
		else:
			return self.getShader2(*args)
	def getEntityList(self):
		return tQ3EntityList(IQ3LevelMesh_getEntityList(self.c_pointer))

class ITimer(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = args[0]
	def getRealTime(self):
		return ITimer_getRealTime(self.c_pointer)
	if IRRLICHT_VERSION >= 180:
		#def getRealTimeAndDate(self):
			#return ITimer_getRealTimeAndDate(self.c_pointer)[0]
		def getRealTimeAndDateAsTuple(self):
			rtd = ITimer_getRealTimeAndDate(self.c_pointer)[0]
			return (rtd.Year, rtd.Month, rtd.Day, rtd.Hour, rtd.Minute, rtd.Second)
	def getTime(self):
		return ITimer_getTime(self.c_pointer)
	def setTime(self, time):
		ITimer_setTime(self.c_pointer, time)
	def stop(self):
		ITimer_stop(self.c_pointer)
	def start(self):
		ITimer_start(self.c_pointer)
	def setSpeed(self, speed = 1.0):
		ITimer_setSpeed(self.c_pointer, speed)
	def getSpeed(self):
		return ITimer_getSpeed(self.c_pointer)
	def isStopped(self):
		return ITimer_isStopped(self.c_pointer)
	def tick(self):
		ITimer_tick(self.c_pointer)

class IrrlichtDevice(IReferenceCounted):
	def __init__(self, *args, **kwargs):
		self.c_pointer = None
		if 'IrrlichtDevice_pointer' in kwargs:
			self.c_pointer = kwargs['IrrlichtDevice_pointer']
		elif 'parameters' in kwargs:
			self.c_pointer = IrrlichtDevice_createDeviceEx(kwargs['parameters'])
		elif len(args) == 7:
			deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver = args
			if isinstance(receiver, int):
				receiver = IEventReceiver(0)
			self.c_pointer = IrrlichtDevice_createDevice(deviceType, windowSize.c_pointer, bits, fullscreen, stencilbuffer, vsync, receiver.c_pointer)
		else:
			self.c_pointer = IrrlichtDevice_createDevice(*args, **kwargs)
	def __call__(self, deviceType = EDT_SOFTWARE, windowSize = dimension2du(640,480), bits = 16, fullscreen = False, stencilbuffer = False, vsync = False, receiver = IEventReceiver(0)):
		if isinstance(receiver, int):
			receiver = IEventReceiver(0)
		self.c_pointer = IrrlichtDevice_createDevice(deviceType, windowSize.c_pointer, bits, fullscreen, stencilbuffer, vsync, receiver.c_pointer)
	def run(self):
		return IrrlichtDevice_run(self.c_pointer)
	def yield_self(self):
		IrrlichtDevice_yield(self.c_pointer)
	def _yield(self):
		'for swig compatibility'
		IrrlichtDevice_yield(self.c_pointer)
	def sleep(self, timeMs, pauseTimer = False):
		IrrlichtDevice_sleep(self.c_pointer, timeMs, pauseTimer)
	def getVideoDriver(self):
		return IVideoDriver(IrrlichtDevice_getVideoDriver(self.c_pointer))
	def getFileSystem(self):
		return IFileSystem(IrrlichtDevice_getFileSystem(self.c_pointer))
	def getGUIEnvironment(self):
		return IGUIEnvironment(IrrlichtDevice_getGUIEnvironment(self.c_pointer))
	def getSceneManager(self):
		return ISceneManager(IrrlichtDevice_getSceneManager(self.c_pointer))
	def getCursorControl(self):
		return ICursorControl(IrrlichtDevice_getCursorControl(self.c_pointer))
	def getLogger(self):
		return ILogger(IrrlichtDevice_getLogger(self.c_pointer))
	def getVideoModeList(self):
		return IVideoModeList(IrrlichtDevice_getVideoModeList(self.c_pointer))
	def getOSOperator(self):
		return IOSOperator(IrrlichtDevice_getOSOperator(self.c_pointer))
	def getTimer(self):
		return ITimer(IrrlichtDevice_getTimer(self.c_pointer))
	def setWindowCaption(self, text):
		IrrlichtDevice_setWindowCaption(self.c_pointer, text)
	def isWindowActive(self):
		return IrrlichtDevice_isWindowActive(self.c_pointer)
	def isWindowFocused(self):
		return IrrlichtDevice_isWindowFocused(self.c_pointer)
	def isWindowMinimized(self):
		return IrrlichtDevice_isWindowMinimized(self.c_pointer)
	def isFullscreen(self):
		return IrrlichtDevice_isFullscreen(self.c_pointer)
	def getColorFormat(self):
		return IrrlichtDevice_getColorFormat(self.c_pointer)
	def closeDevice(self):
		IrrlichtDevice_closeDevice(self.c_pointer)
	def getVersion(self):
		if hexversion >= 0x03000000:
			return type_unicode(IrrlichtDevice_getVersion(self.c_pointer))
		else:
			return IrrlichtDevice_getVersion(self.c_pointer)
	def setEventReceiver(self, receiver):
		IrrlichtDevice_setEventReceiver(self.c_pointer, receiver.c_pointer)
	def getEventReceiver(self):
		return IEventReceiver(IrrlichtDevice_getEventReceiver(self.c_pointer))
	def postEventFromUser(self, event):
		return IrrlichtDevice_postEventFromUser(self.c_pointer, event)
	def setInputReceivingSceneManager(self, sceneManager):
		return IrrlichtDevice_setInputReceivingSceneManager(self.c_pointer, sceneManager.c_pointer)
	def setResizable(self, resize = False):
		IrrlichtDevice_setResizable(self.c_pointer, resize)
	def minimizeWindow(self):
		IrrlichtDevice_minimizeWindow(self.c_pointer)
	def maximizeWindow(self):
		IrrlichtDevice_maximizeWindow(self.c_pointer)
	def restoreWindow(self):
		IrrlichtDevice_restoreWindow(self.c_pointer)
	def activateJoysticks(self, joystickInfo):
		#~ return IrrlichtDevice_activateJoysticks(self.c_pointer, ctypes.byref(ctypes.c_int(joystickInfo.c_pointer)))
		return IrrlichtDevice_activateJoysticks(self.c_pointer, joystickInfo.c_pointer)
	def setGammaRamp(self, red, green, blue, relativebrightness, relativecontrast):
		return IrrlichtDevice_setGammaRamp(self.c_pointer, red, green, blue, relativebrightness, relativecontrast)
	def getGammaRamp(self, red, green, blue, brightness, contrast):
		return IrrlichtDevice_getGammaRamp(self.c_pointer, red, green, blue, brightness, contrast)
	def getType(self):
		return IrrlichtDevice_getType(self.c_pointer)
	def isDriverSupported(self, driver):
		return IrrlichtDevice_isDriverSupported(self.c_pointer, driver)

class SIrrlichtCreationParameters(object):
	def __init__(self, *args, **kwargs):
		self.c_pointer = SIrrlichtCreationParameters_ctor()
		if len(args) > 0:
			self.c_pointer = args[0]
	def get_DeviceType(self):
		return SIrrlichtCreationParameters_get_DeviceType(self.c_pointer)
	def set_DeviceType(self, value):
		SIrrlichtCreationParameters_set_DeviceType(self.c_pointer, value)
	def get_DriverType(self):
		return SIrrlichtCreationParameters_get_DriverType(self.c_pointer)
	def set_DriverType(self, value):
		SIrrlichtCreationParameters_set_DriverType(self.c_pointer, value)
	def get_WindowSize(self):
		return dimension2du(pointer = SIrrlichtCreationParameters_get_WindowSize(self.c_pointer))
	def set_WindowSize(self, value):
		SIrrlichtCreationParameters_set_WindowSize(self.c_pointer, value.c_pointer)
	def get_Bits(self):
		return SIrrlichtCreationParameters_get_Bits(self.c_pointer)
	def set_Bits(self, value):
		SIrrlichtCreationParameters_set_Bits(self.c_pointer, value)
	def get_ZBufferBits(self):
		return SIrrlichtCreationParameters_get_ZBufferBits(self.c_pointer)
	def set_ZBufferBits(self, value):
		SIrrlichtCreationParameters_set_ZBufferBits(self.c_pointer, value)
	def get_Fullscreen(self):
		return SIrrlichtCreationParameters_get_Fullscreen(self.c_pointer)
	def set_Fullscreen(self, value):
		SIrrlichtCreationParameters_set_Fullscreen(self.c_pointer, value)
	def get_Stencilbuffer(self):
		return SIrrlichtCreationParameters_get_Stencilbuffer(self.c_pointer)
	def set_Stencilbuffer(self, value):
		SIrrlichtCreationParameters_set_Stencilbuffer(self.c_pointer, value)
	def get_Vsync(self):
		return SIrrlichtCreationParameters_get_Vsync(self.c_pointer)
	def set_Vsync(self, value):
		SIrrlichtCreationParameters_set_Vsync(self.c_pointer, value)
	def get_AntiAlias(self):
		return SIrrlichtCreationParameters_get_AntiAlias(self.c_pointer)
	def set_AntiAlias(self, value):
		SIrrlichtCreationParameters_set_AntiAlias(self.c_pointer, value)
	def get_WithAlphaChannel(self):
		return SIrrlichtCreationParameters_get_WithAlphaChannel(self.c_pointer)
	def set_WithAlphaChannel(self, value):
		SIrrlichtCreationParameters_set_WithAlphaChannel(self.c_pointer, value)
	def get_Doublebuffer(self):
		return SIrrlichtCreationParameters_get_Doublebuffer(self.c_pointer)
	def set_Doublebuffer(self, value):
		SIrrlichtCreationParameters_set_Doublebuffer(self.c_pointer, value)
	def get_IgnoreInput(self):
		return SIrrlichtCreationParameters_get_IgnoreInput(self.c_pointer)
	def set_IgnoreInput(self, value):
		SIrrlichtCreationParameters_set_IgnoreInput(self.c_pointer, value)
	def get_Stereobuffer(self):
		return SIrrlichtCreationParameters_get_Stereobuffer(self.c_pointer)
	def set_Stereobuffer(self, value):
		SIrrlichtCreationParameters_set_Stereobuffer(self.c_pointer, value)
	def get_HighPrecisionFPU(self):
		return SIrrlichtCreationParameters_get_HighPrecisionFPU(self.c_pointer)
	def set_HighPrecisionFPU(self, value):
		SIrrlichtCreationParameters_set_HighPrecisionFPU(self.c_pointer, value)
	def get_EventReceiver(self):
		return IEventReceiver(SIrrlichtCreationParameters_get_EventReceiver(self.c_pointer))
	def set_EventReceiver(self, value):
		SIrrlichtCreationParameters_set_EventReceiver(self.c_pointer, value.c_pointer)
	def get_WindowId(self):
		return SIrrlichtCreationParameters_get_WindowId(self.c_pointer)
	def set_WindowId(self, value):
		SIrrlichtCreationParameters_set_WindowId(self.c_pointer, value)
	def get_LoggingLevel(self):
		return SIrrlichtCreationParameters_get_LoggingLevel(self.c_pointer)
	def set_LoggingLevel(self, value):
		SIrrlichtCreationParameters_set_LoggingLevel(self.c_pointer, value)
	def get_SDK_version_do_not_use(self):
		return SIrrlichtCreationParameters_get_SDK_version_do_not_use(self.c_pointer)
	DeviceType = property(get_DeviceType, set_DeviceType)
	DriverType = property(get_DriverType, set_DriverType)
	WindowSize = property(get_WindowSize, set_WindowSize)
	Bits = property(get_Bits, set_Bits)
	ZBufferBits = property(get_ZBufferBits, set_ZBufferBits)
	Fullscreen = property(get_Fullscreen, set_Fullscreen)
	Stencilbuffer = property(get_Stencilbuffer, set_Stencilbuffer)
	Vsync = property(get_Vsync, set_Vsync)
	AntiAlias = property(get_AntiAlias, set_AntiAlias)
	WithAlphaChannel = property(get_WithAlphaChannel, set_WithAlphaChannel)
	Doublebuffer = property(get_Doublebuffer, set_Doublebuffer)
	IgnoreInput = property(get_IgnoreInput, set_IgnoreInput)
	Stereobuffer = property(get_Stereobuffer, set_Stereobuffer)
	HighPrecisionFPU = property(get_HighPrecisionFPU, set_HighPrecisionFPU)
	EventReceiver = property(get_EventReceiver, set_EventReceiver)
	WindowId = property(get_WindowId, set_WindowId)
	SDK_version_do_not_use = property(get_SDK_version_do_not_use)

class MainLoop:
	def __init__(self, *args, **kwargs):
		self.c_pointer = self.ctor(*args, **kwargs)
	def ctor(self, device, driver, smgr = ISceneManager(0), guienv = IGUIEnvironment(0), backBuffer = True, zBuffer = True, color = SColor(255,100,100,140), videoData = SExposedVideoData(0), sourceRect = recti(0), sleep_time_ms = 0, sleep_pause_timer = False):
		return MainLoop_ctor(device.c_pointer, driver.c_pointer, smgr.c_pointer, guienv.c_pointer, backBuffer, zBuffer, color.c_pointer, videoData.c_pointer, sourceRect.c_pointer, sleep_time_ms, sleep_pause_timer)
	def start(self):
		MainLoop_start(self.c_pointer)
	def stop(self):
		MainLoop_stop(self.c_pointer)

if BUILD_WITH_AGG:
	def svg_path_renderer_from_file(file_name = 'tiger.svg'):
		return agg_svg_path(file_name)

	def svg_path_renderer_from_string(buf = ''):
		return agg_svg_path_from_string(buf)

	def svg_IImage(path_renderer, video_driver, scale_value = 1.0, rotate_value = 0.0, expand_value = 0.0, color_format = ECF_A8R8G8B8, alpha_value = 0, stride_value = 4):
		return IImage(agg_svg_IImage(path_renderer, video_driver.c_pointer, scale_value, rotate_value, expand_value, color_format, alpha_value, stride_value))

	def svg_ITexture(path_renderer, video_driver, texture_name = '', scale_value = 1.0, rotate_value = 0.0, expand_value = 0.0, color_format = ECF_A8R8G8B8, alpha_value = 0, stride_value = 4):
		return ITexture(agg_svg_ITexture(path_renderer, video_driver.c_pointer, texture_name, scale_value, rotate_value, expand_value, color_format, alpha_value, stride_value))

	class svg_viewer(object):
		def __init__(self, *args, **kwargs):
			self.c_pointer = svg_viewer_ctor()
		def set_video_driver(self, drv):
			svg_viewer_set_video_driver(self.c_pointer, drv.c_pointer)
		def scale(self, scale_value = 1.0):
			svg_viewer_scale(self.c_pointer, scale_value)
		def get_texture(self):
			c_pointer = svg_viewer_get_texture(self.c_pointer)
			if c_pointer:
				return ITexture(c_pointer)
			else:
				return False

	class agg_svg_loader(IImageLoader):
		def __init__(self, *args, **kwargs):
			if hasattr(args[0], 'c_pointer'):
				self.c_pointer = agg_svg_loader_ctor(args[0].c_pointer)
			else:
				self.c_pointer = agg_svg_loader_ctor(args[0])

if BUILD_WITH_IRR_SVG_AGG:
	class svg_agg_image(object):
		def __init__(self, *args, **kwargs):
			'IVideoDriver* video_driver, IFileSystem* fs, const irr::io::path& file_name = "tiger.svg", bool content_unicode = true, u32 alpha_value = 128, video::ECOLOR_FORMAT color_format = ECF_A8R8G8B8, int stride = 4'
			if len(args) > 1 and hasattr(args[0], 'c_pointer'):
				content_unicode = True
				if len(args) > 3:
					content_unicode = args[3]
				alpha_value = 128
				if len(args) > 4:
					alpha_value = args[4]
				color_format = ECF_A8R8G8B8
				if len(args) > 5:
					color_format = args[5]
				stride = 4
				if len(args) > 6:
					stride = args[6]
				self.c_pointer = svg_agg_image_ctor1(args[0].c_pointer, args[1].c_pointer, args[2], content_unicode, alpha_value, color_format, stride)
			elif 'c_pointer' in kwargs:
				self.c_pointer = kwargs.pop('c_pointer', None)
			else:
				self.c_pointer = None
		def __del__(self):
			if self.c_pointer:
				try:
					delete_pointer(self.c_pointer)
				except:
					pass
		def parse(self, fs, file_name = 'file.svg', content_unicode = True, alpha_value = 0, color_format = ECF_A8R8G8B8, stride = 4):
			svg_agg_image_parse(self.c_pointer, fs.c_pointer, file_name, content_unicode, alpha_value, color_format, stride)
		def scale(self, x = 1.0, y = 1.0):
			svg_agg_image_scale(self.c_pointer, x, y)
		def scale_rateably(self, value = 1.0):
			svg_agg_image_scale_rateably(self.c_pointer, value)
		def get_image(self, rendering = False):
			return IImage(svg_agg_image_get_image(self.c_pointer, rendering))
		def get_texture(self, rendering = False, adding = False):
			return ITexture(svg_agg_image_get_texture(self.c_pointer, rendering, adding))
		#~ def drop(self):
			#~ return svg_agg_image_drop(self.c_pointer)
		def get_width(self):
			return svg_agg_image_get_width(self.c_pointer)
		width = property(get_width)
		def get_width_u32(self):
			return svg_agg_image_get_width_u32(self.c_pointer)
		width_u32 = property(get_width_u32)
		def get_height(self):
			return svg_agg_image_get_height(self.c_pointer)
		height = property(get_height)
		def get_height_u32(self):
			return svg_agg_image_get_height_u32(self.c_pointer)
		height_u32 = property(get_height_u32)
		def get_size(self):
			return vector2du(self.get_width_u32(), self.get_height_u32())

if BUILD_WITH_IRR_SVG_CAIRO:
	class svg_cairo_image(object):
		def __init__(self, *args, **kwargs):
			'IVideoDriver* video_driver, IFileSystem* fs, const irr::io::path& file_name = "tiger.svg", bool content_unicode = true'
			if len(args) > 1 and hasattr(args[0], 'c_pointer'):
				content_unicode = True
				if len(args) > 3:
					content_unicode = args[3]
				alpha_value = 0.0
				if len(args) > 4:
					alpha_value = args[4]
				image_format = ECF_A8R8G8B8
				if len(args) > 5:
					image_format = args[5]
				antialias_type = CAIRO_ANTIALIAS_DEFAULT
				if len(args) > 6:
					antialias_type = args[6]
				scale_x = 1.0
				if len(args) > 7:
					scale_x = args[7]
				scale_y = 1.0
				if len(args) > 8:
					scale_y = args[8]
				self.c_pointer = svg_cairo_image_ctor1(args[0].c_pointer, args[1].c_pointer, args[2], content_unicode, alpha_value, image_format, antialias_type, scale_x, scale_y)
			elif 'c_pointer' in kwargs:
				self.c_pointer = kwargs.pop('c_pointer', None)
			else:
				self.c_pointer = None
		def parse(self, fs, file_name = 'file.svg', content_unicode = True, alpha_value = 0.0, color_format = ECF_A8R8G8B8, antialias_type = CAIRO_ANTIALIAS_DEFAULT, scale_x = 1.0, scale_y = 1.0):
			svg_cairo_image_parse(self.c_pointer, fs.c_pointer, file_name, content_unicode, alpha_value, color_format, antialias_type, scale_x, scale_y)
		def scale(self, x = 1.0, y = 1.0):
			svg_cairo_image_scale(self.c_pointer, x, y)
		def get_image(self):
			return IImage(svg_cairo_image_get_image(self.c_pointer))
		def get_texture(self):
			return ITexture(svg_cairo_image_get_texture(self.c_pointer))
		def get_width(self):
			return svg_cairo_image_get_width(self.c_pointer)
		width = property(get_width)
		def get_width_u32(self):
			return svg_cairo_image_get_width_u32(self.c_pointer)
		width_u32 = property(get_width_u32)
		def get_height(self):
			return svg_cairo_image_get_height(self.c_pointer)
		height = property(get_height)
		def get_height_u32(self):
			return svg_cairo_image_get_height_u32(self.c_pointer)
		height_u32 = property(get_height_u32)
		def get_size(self):
			return vector2du(self.get_width_u32(), self.get_height_u32())

if BUILD_WITH_3D_TEXT:
	class Text3DSimple(ISceneNode):
		def __init__(self, *args, **kwargs):
			self.c_pointer = self.ctor(*args, **kwargs)
		def ctor(self, parent, mgr, id = -1):
			if not isinstance(parent, ISceneNode):
				parent = mgr.getRootSceneNode()
			return IText3DSimple_ctor(parent.c_pointer, mgr.c_pointer, id)
		def setText(self, text, font_file_name = 0, size = 10, depth = 50.0, primitive_type = EPT_TRIANGLES, index_type = EIT_16BIT):
			if not font_file_name:
				from os import environ
				font_file_name = environ['SYSTEMROOT']+'/Fonts/Arial.ttf'
			return IText3DSimple_setText(self.c_pointer, text, font_file_name, size, depth, primitive_type, index_type)

	class IText3D(ISceneNode):
		def __init__(self, *args, **kwargs):
			self.c_pointer = self.ctor(*args, **kwargs)
		def ctor(self, parent, mgr, id = -1):
			if not isinstance(parent, ISceneNode):
				parent = mgr.getRootSceneNode()
			return IText3D_ctor(parent.c_pointer, mgr.c_pointer, id)
		def setText(self, text, font_file_name = 0, size = 10, depth = 50.0, primitive_type = EPT_TRIANGLES, index_type = EIT_16BIT, color_random = RCC_NO, algorithm_build_vertices = ABSV_INTERLEAVE):
			if not font_file_name:
				from os import environ
				font_file_name = environ['SYSTEMROOT']+'/Fonts/Arial.ttf'
			return IText3D_setText(self.c_pointer, text, font_file_name, size, depth, primitive_type, index_type, color_random, algorithm_build_vertices)
		def get_color_random_type(self):
			return IText3D_get_color_random_type(self.c_pointer)
		def set_color_random_type(self, new_value = RCC_NO):
			IText3D_set_color_random_type(self.c_pointer, new_value)
		def set_auto_emissive_color(self):
			IText3D_set_auto_emissive_color(self.c_pointer)
		def get_draw_as_figures(self):
			return IText3D_get_draw_as_figures(self.c_pointer)
		def set_draw_as_figures(self, draw_as_figures = DAF_NO, material = SMaterial(0)):
			IText3D_set_draw_as_figures(self.c_pointer, draw_as_figures, material.c_pointer)

def createDevice(deviceType = EDT_SOFTWARE, windowSize = dimension2du(640,480), bits = 16, fullscreen = False, stencilbuffer = False, vsync = False, receiver = IEventReceiver(0)):
	return IrrlichtDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver)

def createDeviceEx(params):
	return IrrlichtDevice(parameters = params.c_pointer)


if platform in ('windows', 'win32'):

	def SetIcon1(drv, icon_id = IDI_APPLICATION, big_icon = False):
		WM_SETICON = 0x0080
		GetModuleHandle = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(('GetModuleHandleA', ctypes.windll.kernel32))
		LoadIcon = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('LoadIconA', ctypes.windll.user32))
		SendMessage = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int)(('SendMessageA', ctypes.windll.user32))
		SendMessage(drv.GetHandle(), WM_SETICON, big_icon, LoadIcon(GetModuleHandle(None), icon_id))

	def SetIcon2(drv, icon_id = IDI_APPLICATION):
		GCL_HICON = -14
		GetModuleHandle = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(('GetModuleHandleA', ctypes.windll.kernel32))
		LoadIcon = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_int)(('LoadIconA', ctypes.windll.user32))
		SetClassLong = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int, ctypes.c_long)(('SetClassLongA', ctypes.windll.user32))
		SetClassLong(drv.GetHandle(), GCL_HICON, LoadIcon(GetModuleHandle(None), icon_id))

	def IsGUIThread(bConvert = False):
		IsGUIThread = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_bool)(('IsGUIThread', ctypes.windll.user32))
		return IsGUIThread(bConvert)

	def GetWindow(hWnd, uCmd = 0):
		GetWindow = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(('GetWindow', ctypes.windll.user32))
		return GetWindow(hWnd, uCmd)

	def GetDesktopWindow():
		GetDesktopWindow = ctypes.WINFUNCTYPE(ctypes.c_void_p)(('GetDesktopWindow', ctypes.windll.user32))
		return GetDesktopWindow()

	def GetShellWindow():
		GetShellWindow = ctypes.WINFUNCTYPE(ctypes.c_void_p)(('GetShellWindow', ctypes.windll.user32))
		return GetShellWindow()

	def GetTopWindow(hWnd = None):
		GetTopWindow = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(('GetTopWindow', ctypes.windll.user32))
		return GetTopWindow(hWnd)

	def GetWindowRect(hWnd):
		from ctypes.wintypes import RECT
		rect = RECT()
		GetWindowRect = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(RECT))(('GetWindowRect', ctypes.windll.user32))
		GetWindowRect(hWnd, ctypes.pointer(rect))
		return rect

	def GetDesktopRect():
		return GetWindowRect(GetDesktopWindow())

	def GetIrrWindowRect(drv):
		return GetWindowRect(drv.GetHandle())

	def MoveWindow(drv, x, y, nWidth, nHeight, bRepaint):
		MoveWindow = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)(('MoveWindow', ctypes.windll.user32))
		return MoveWindow(drv.GetHandle(), x, y, nWidth, nHeight, bRepaint)

	def SetWindowPos(drv, hWndInsertAfter, x, y, width, height, uFlags):
		SetWindowPos = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint)(('SetWindowPos', ctypes.windll.user32))
		return SetWindowPos(drv.GetHandle(), hWndInsertAfter, x, y, width, height, uFlags)

	def RealChildWindowFromPoint(hwndParent, ptParentClientCoords):
		RealChildWindowFromPoint = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.POINTER(POINT))(('RealChildWindowFromPoint', ctypes.windll.user32))
		return RealChildWindowFromPoint(hwndParent, ptParentClientCoords)

	def RealChildWindowFromXY(hwndParent, x, y):
		from ctypes.wintypes import POINT
		point = POINT(x, y)
		return RealChildWindowFromPoint(hwndParent, ctypes.pointer(point))

else:
	# this my functions has not realisations for non windows platform
	# if you know as, do it and share code
	def SetIcon1(drv, icon_id = 0, big_icon = False):
		pass
	def SetIcon2(drv, icon_id = 0):
		pass
	def IsGUIThread(bConvert = False):
		pass
	def GetWindow(hWnd, uCmd = 0):
		pass
	def GetDesktopWindow():
		pass
	def GetShellWindow():
		pass
	def GetTopWindow(hWnd = None):
		pass
	def GetWindowRect(hWnd):
		pass
	def GetDesktopRect():
		return GetWindowRect(GetDesktopWindow())
	def GetIrrWindowRect(drv):
		return GetWindowRect(drv.GetHandle())
	def MoveWindow(drv, x, y, nWidth, nHeight, bRepaint):
		pass
	def SetWindowPos(drv, hWndInsertAfter, x, y, width, height, uFlags):
		pass
	def RealChildWindowFromPoint(hwndParent, ptParentClientCoords):
		pass
	def RealChildWindowFromXY(hwndParent, x, y):
		pass



def is_frozen():
	return globals()['__file__'] == '<frozen>'

def generate_texture(video_driver, image_format = ECF_R8G8B8, image_size = dimension2du(2, 2), texture_name = 'texture_01', alpha_value = 128, red = (0, 255), green = (0, 255), blue = (0, 255)):
	return ITexture(tool_texture_generator(video_driver.c_pointer, image_format, image_size.c_pointer, texture_name, alpha_value, red[0], red[1], green[0], green[1], blue[0], blue[1]))

def texture_from_svg(video_driver, file_name = 'tiger.svg', image_format = ECF_A8R8G8B8, texture_name = 'texture_01', alpha_value = 0):
	return ITexture(tool_texture_from_svg(video_driver.c_pointer, file_name, image_format, texture_name, alpha_value))

def texture_from_test_vectors(video_driver, image_format = ECF_A8R8G8B8, image_size = dimension2du(640, 480), texture_name = 'texture_01', alpha_value = 0):
	return ITexture(tool_texture_from_test_vectors(video_driver.c_pointer, image_format, image_size.c_pointer, texture_name, alpha_value))

def _getAsVector3df(string, pos):
	p = ctypes.c_uint(pos)
	result = tool_getAsVector3df(string, ctypes.byref(p))
	pos = p.value
	return vector3df(result)

def getAsVector3df(string):
	x, y, z = string.split()
	return vector3df(float(x), float(y), float(z)), len(string)

def _getAsFloat(string, pos):
	p = ctypes.c_uint(pos)
	result = tool_getAsFloat(string, ctypes.byref(p))
	pos = p.value
	return result

def getAsFloat(string):
	return float(string), len(string)

def getTextures(textures, name, startPos, fileSystem, video_driver):
	p = ctypes.c_uint()
	tool_getTextures(textures.c_pointer, name, ctypes.byref(p), fileSystem.c_pointer, video_driver.c_pointer)
	startPos = p.value


if __name__ == "__main__":
	if hexversion >= 0x03000000:
		from test_py3 import test
	else:
		from test_py2 import test
	test()

%module(directors="1") irrlicht

#define IRRLICHT_SWIG_PYTHON_VERSION "0.3"

#if defined(_IRR_USE_INPUT_METHOD)
#define IRR_USE_INPUT_METHOD 1
#else
#define IRR_USE_INPUT_METHOD 0
#endif

#if defined(_IRR_COMPILE_WITH_CGUITTFONT_)
#define IRR_COMPILE_WITH_CGUITTFONT 1
#else
#define IRR_COMPILE_WITH_CGUITTFONT 0
#endif

#pragma SWIG nowarn=312,511

//~ %include "typemaps.i"
//~ %include "exception.i"
%include <python/typemaps.i>
//~ %include <python/cstring.i>
%include <python/cwstring.i>
//~ %include <python/file.i>
//~ %include <python/wchar.i>
//~ %include <python/cpointer.i>
%include <python/carrays.i>

%{
//#define _IRR_STATIC_LIB_
#include "irrlicht.h"
using namespace irr;
using namespace core;
using namespace gui;
using namespace io;
using namespace scene;
using namespace video;
#if defined(_IRR_IMPROVE_UNICODE)
#include "irrUString.h"
using namespace unicode;
#endif
#if !defined(_IRR_COMPILE_WITH_CGUITTFONT_)
#include "IGUITTFont.h"
#endif
%}

%rename(_yield) yield;
%rename(_global) global;
%rename(_in) in;
%rename(_pass) pass;
%rename(_from) from;

%include irrTypes.h
%include irrAllocator.h
%include irrArray.h
%include irrList.h
%include irrMap.h

%typecheck(SWIG_TYPECHECK_POINTER, noblock=1) const IRR_CHAR_TYPE &
{
%#if PY_VERSION_HEX >= 0x03000000
	$1 = PyUnicode_Check($input) ? 1 : 0;
%#else
	$1 = (PyString_Check($input) || PyUnicode_Check($input)) ? 1 : 0;
%#endif
}
%typemap(in, noblock=1) const IRR_CHAR_TYPE &
{
%#if PY_VERSION_HEX >= 0x03000000
	if (PyUnicode_Check($input))
		$1 = new $*1_ltype(PyUnicode_AsUnicode($input));
	else
		%argument_fail(SWIG_TypeError, "$*ltype", $symname, $argnum);
%#else
	if (PyString_Check($input))
		$1 = new $*1_ltype(PyString_AsString($input));
	else
	{
		if (PyUnicode_Check($input))
			$1 = new $*1_ltype(PyUnicode_AsUnicode($input));
		else
			%argument_fail(SWIG_TypeError, "$*ltype", $symname, $argnum);
	}
%#endif
}
%typemap(freearg, noblock=1) const IRR_CHAR_TYPE & {delete $1;}
%typemap(out, noblock=1) const IRR_CHAR_TYPE &
{
%#if PY_VERSION_HEX >= 0x03000000
	$result = PyUnicode_FromWideChar((wchar_t*)$1->c_str(), (Py_ssize_t)$1->size());
%#else
	$result = PyString_FromString($1->c_str());
%#endif
}

%typecheck(SWIG_TYPECHECK_POINTER, noblock=1) const IRR_WCHAR_TYPE &
{
%#if PY_VERSION_HEX >= 0x03000000
	$1 = PyUnicode_Check($input) ? 1 : 0;
%#else
	$1 = (PyString_Check($input) || PyUnicode_Check($input)) ? 1 : 0;
%#endif
}
%typemap(in, noblock=1) const IRR_WCHAR_TYPE &
{
%#if PY_VERSION_HEX >= 0x03000000
	if (PyUnicode_Check($input))
		$1 = new $*1_ltype(PyUnicode_AsUnicode($input));
	else
		%argument_fail(SWIG_TypeError, "$*ltype", $symname, $argnum);
%#else
	if (PyString_Check($input))
		$1 = new $*1_ltype(PyUnicode_AsUnicode(PyUnicode_FromObject($input)));
	else
	{
		if (PyUnicode_Check($input))
			$1 = new $*1_ltype(PyUnicode_AsUnicode($input));
		else
			%argument_fail(SWIG_TypeError, "$*ltype", $symname, $argnum);
	}
%#endif
}
%typemap(freearg, noblock=1) const IRR_WCHAR_TYPE & {delete $1;}
%typemap(out, noblock=1) const IRR_WCHAR_TYPE & {$result = PyUnicode_FromWideChar($1->c_str(), (Py_ssize_t)$1->size());}

typedef int s32;
typedef unsigned int u32;
typedef float f32;
typedef double f64;

%ignore irr::core::string::operator +=;
%include irrString.h
%template(stringc) irr::core::string < c8 >;
%template(stringw) irr::core::string < wchar_t >;

//~ %#ifdef _IRR_IMPROVE_UNICODE
%include irrUString.h
%template(ustring) irr::core::ustring16 < irrAllocator < uchar16_t > >;
%apply const IRR_CHAR_TYPE & {const irr::core::stringc &};
%apply const IRR_WCHAR_TYPE & {const irr::core::ustring &, const irr::core::stringw &, const irr::io::path &, const path &, irr::io::path &, path &};
//~ %#else
//~ %apply const IRR_CHAR_TYPE & {const irr::core::stringc &, const irr::io::path &, const path &, irr::io::path &, path &};
//~ %apply const IRR_WCHAR_TYPE & {const irr::core::stringw &};
//~ %#endif


%ignore intersectsWithLine;
%include aabbox3d.h
%template(aabbox3df) irr::core::aabbox3d<irr::f32>;
%template(aabbox3di) irr::core::aabbox3d<irr::s32>;

%include dimension2d.h
%template(dimension2df) irr::core::dimension2d<irr::f32>;
%template(dimension2di) irr::core::dimension2d<irr::s32>;
%template(dimension2du) irr::core::dimension2d<irr::u32>;

%ignore getAngleTrig;
%ignore rotateBy;
%include vector2d.h
%template(vector2df) irr::core::vector2d<irr::f32>;
%template(vector2di) irr::core::vector2d<irr::s32>;

%include vector3d.h
%template(vector3df) irr::core::vector3d<irr::f32>;
%template(vector3di) irr::core::vector3d<irr::s32>;

%include line2d.h
%template(line2df) irr::core::line2d<irr::f32>;
%template(line2di) irr::core::line2d<irr::s32>;

%include line3d.h
%template(line3df) irr::core::line3d<irr::f32>;
%template(line3di) irr::core::line3d<irr::s32>;

%include plane3d.h
%template(plane3df) irr::core::plane3d<irr::f32>;
%template(plane3di) irr::core::plane3d<irr::s32>;

%include position2d.h
%template(position2df) irr::core::position2d<irr::f32>;
%template(position2di) irr::core::position2d<irr::s32>;

%include rect.h
%template(rectf) irr::core::rect<irr::f32>;
%template(recti) irr::core::rect<irr::s32>;

%include triangle3d.h
%template(triangle3df) irr::core::triangle3d<irr::f32>;
%template(triangle3di) irr::core::triangle3d<irr::s32>;

%include EAttributes.h
%include ECullingTypes.h
%include EDebugSceneTypes.h
%include EDeviceTypes.h
%include EDriverFeatures.h
%include EDriverTypes.h
%include EGUIAlignment.h
%include EGUIElementTypes.h
%include EHardwareBufferFlags.h
%include EMaterialFlags.h
%include EMaterialTypes.h
%include EMeshWriterEnums.h
%include EMessageBoxFlags.h
%include EPrimitiveTypes.h
%include ESceneNodeAnimatorTypes.h
%include ESceneNodeTypes.h

%ignore EGST_COUNT;
%include EShaderTypes.h

%include ETerrainElements.h
%include SceneParameters.h

%include SColor.h

%include IReferenceCounted.h

%include ICursorControl.h

%include IAttributes.h
%include IAttributeExchangingObject.h

%include Keycodes.h

%include SKeyMap.h
%array_functions(irr::SKeyMap, SKeyMap)
%array_class(irr::SKeyMap, newSKeyMap)
//~ %apply SWIGTYPE** OUTPUT{irr::SKeyMap **pptr};
//~ int create_SKeyMap(irr::SKeyMap** pptr);
%extend irr::SKeyMap
{
	void set(int index, EKEY_ACTION action, EKEY_CODE key_code){self[index].Action = action; self[index].KeyCode = key_code;};
};

%immutable;
struct SGUIEvent
{
	gui::IGUIElement* Caller;
	gui::IGUIElement* Element;
	gui::EGUI_EVENT_TYPE EventType;
};
struct SMouseInput
{
	s32 X;
	s32 Y;
	f32 Wheel;
	bool Shift;
	bool Control;
	u32 ButtonStates;
	bool isLeftPressed() const {return isLeftPressed();};
	bool isRightPressed() const {return isRightPressed();};
	bool isMiddlePressed() const {return isMiddlePressed();};
	EMOUSE_INPUT_EVENT Event;
};
struct SKeyInput
{
	wchar_t Char;
	EKEY_CODE Key;
	bool PressedDown;
	bool Shift;
	bool Control;
};
struct SJoystickEvent
{
	enum
	{
		NUMBER_OF_BUTTONS = 32,
		AXIS_X = 0, // e.g. analog stick 1 left to right
		AXIS_Y,		// e.g. analog stick 1 top to bottom
		AXIS_Z,		// e.g. throttle, or analog 2 stick 2 left to right
		AXIS_R,		// e.g. rudder, or analog 2 stick 2 top to bottom
		AXIS_U,
		AXIS_V,
		NUMBER_OF_AXES
	};
	u32 ButtonStates;
	s16 Axis[NUMBER_OF_AXES];
	u16 POV;
	u8 Joystick;
	bool IsButtonPressed(u32 button) const {return IsButtonPressed(button);};
};
struct SLogEvent
{
#if defined(_IRR_IMPROVE_UNICODE)
	const wchar_t* Text;
#else
	const c8* Text;
#endif
	ELOG_LEVEL Level;
};
struct SUserEvent
{
	s32 UserData1;
	s32 UserData2;
};
#if defined(_IRR_USE_INPUT_METHOD)
struct SInputMethodEvent
{
	void* Handle;
	wchar_t Char;
	EINPUT_METHOD_EVENT Event;
};
#endif
%mutable;

%ignore EGUIET_FORCE_32_BIT;
%feature("director") irr::IEventReceiver;
%include IEventReceiver.h

%{typedef irr::SEvent::SGUIEvent SGUIEvent;%}
%extend irr::SEvent::SGUIEvent
{
%immutable;
	irr::gui::IGUIElement* GetCaller(){return self->Caller;};
	irr::gui::IGUIElement* GetElement(){return self->Element;};
	irr::gui::EGUI_EVENT_TYPE GetEventType(){return self->EventType;};
%mutable;
	%pythoncode
	%{
	Caller = property(GetCaller)
	Element = property(GetElement)
	EventType = property(GetEventType)
	%}
};

%{typedef irr::SEvent::SMouseInput SMouseInput;%}
%extend irr::SEvent::SMouseInput
{
%immutable;
	s32 GetX(){return self->X;};
	s32 GetY(){return self->Y;};
	f32 GetWheel(){return self->Wheel;};
	bool GetShift(){return self->Shift;};
	bool GetControl(){return self->Control;};
	u32 GetButtonStates(){return self->ButtonStates;};
	bool isLeftPressed(){return self->isLeftPressed();};
	bool isRightPressed(){return self->isRightPressed();};
	bool isMiddlePressed(){return self->isMiddlePressed();};
	irr::EMOUSE_INPUT_EVENT GetEventType(){return self->Event;};
%mutable;
	%pythoncode
	%{
	X = property(GetX)
	Y = property(GetY)
	Wheel = property(GetWheel)
	Shift = property(GetShift)
	Control = property(GetControl)
	ButtonStates = property(GetButtonStates)
	Event = property(GetEventType)
	%}
};

%{typedef irr::SEvent::SKeyInput SKeyInput;%}
%extend irr::SEvent::SKeyInput
{
%immutable;
	wchar_t GetChar(){return self->Char;};
	irr::EKEY_CODE GetKey(){return self->Key;};
	bool GetPressedDown(){return self->PressedDown;};
	bool GetShift(){return self->Shift;};
	bool GetControl(){return self->Control;};
%mutable;
	%pythoncode
	%{
	Char = property(GetChar)
	Key = property(GetKey)
	PressedDown = property(GetPressedDown)
	Shift = property(GetShift)
	Control = property(GetControl)
	%}
};

%{typedef irr::SEvent::SJoystickEvent SJoystickEvent;%}
%extend irr::SEvent::SJoystickEvent
{
	u32 GetButtonStates(){return self->ButtonStates;};
	s16 GetAxis(){return self->Axis;};
	u16 GetPOV(){return self->POV;};
	u8 GetJoystick(){return self->Joystick;};
	bool IsButtonPressed(u32 button){return self->IsButtonPressed(button);};
	%pythoncode
	%{
	ButtonStates = property(GetButtonStates)
	Axis = property(GetAxis)
	POV = property(GetPOV)
	Joystick = property(GetJoystick)
	%}
};

%{typedef irr::SEvent::SLogEvent SLogEvent;%}
%extend irr::SEvent::SLogEvent
{
%#if defined(_IRR_IMPROVE_UNICODE)
	const wchar_t* GetText(){return self->Text;};
%#else
	const c8* GetText(){return self->Text;};
%#endif
	irr::ELOG_LEVEL GetLevel(){return self->Level;};
	%pythoncode
	%{
	Text = property(GetText)
	Level = property(GetLevel)
	%}
};

%{typedef irr::SEvent::SUserEvent SUserEvent;%}
%extend irr::SEvent::SUserEvent
{
	s32 GetUserData1(){return self->UserData1;};
	s32 GetUserData2(){return self->UserData2;};
	%pythoncode
	%{
	UserData1 = property(GetUserData1)
	UserData2 = property(GetUserData2)
	%}
};

#if defined(_IRR_USE_INPUT_METHOD)
%{typedef irr::SEvent::SInputMethodEvent SInputMethodEvent;%}
%extend irr::SEvent::SInputMethodEvent
{
	void* GetHandle(){return self->Handle;};
	wchar_t GetChar(){return self->Char;};
	EINPUT_METHOD_EVENT Event(){return self->Event;};
	%pythoncode
	%{
	Handle = property(GetHandle)
	Char = property(GetChar)
	Event = property(GetEvent)
	%}
};
#endif

%extend irr::SEvent
{
	irr::EEVENT_TYPE GetEventType(){return self->EventType;};
	const irr::SEvent::SGUIEvent& GetGUIEvent(){return self->GUIEvent;};
	const irr::SEvent::SMouseInput& GetMouseInput(){return self->MouseInput;};
	const irr::SEvent::SKeyInput& GetKeyInput(){return self->KeyInput;};
	const irr::SEvent::SJoystickEvent& GetJoystickEvent(){return self->JoystickEvent;};
	const irr::SEvent::SLogEvent& GetLogEvent(){return self->LogEvent;};
	const irr::SEvent::SUserEvent& GetUserEvent(){return self->UserEvent;};
}
#if defined(_IRR_USE_INPUT_METHOD)
%extend irr::SEvent
{const irr::SEvent::SInputMethodEvent& GetInputMethodEvent(){return self->InputMethodEvent;};}
#endif

%pythoncode
%{
	SEvent.EventType = property(SEvent.GetEventType)
	SEvent.GUIEvent = property(SEvent.GetGUIEvent)
	SEvent.MouseInput = property(SEvent.GetMouseInput)
	SEvent.KeyInput = property(SEvent.GetKeyInput)
	SEvent.JoystickEvent = property(SEvent.GetJoystickEvent)
	SEvent.LogEvent = property(SEvent.GetLogEvent)
	SEvent.UserEvent = property(SEvent.GetUserEvent)
	if IRR_USE_INPUT_METHOD:
		SEvent.InputMethodEvent = property(SEvent.GetInputMethodEvent)
%}

// for ctypes module compatibility
%extend irr::IEventReceiver
{
	EEVENT_TYPE GetEventType(SEvent* pointer){return pointer->EventType;};

	const SEvent::SGUIEvent& GetGUIEvent(SEvent* pointer){return pointer->GUIEvent;};
	gui::IGUIElement* GUIEvent_Caller(const SEvent::SGUIEvent& pointer){return pointer.Caller;};
	gui::IGUIElement* GUIEvent_Element(const SEvent::SGUIEvent& pointer){return pointer.Element;};
	gui::EGUI_EVENT_TYPE GUIEvent_EventType(const SEvent::SGUIEvent& pointer){return pointer.EventType;};

	const SEvent::SMouseInput& GetMouseInput(SEvent* pointer){return pointer->MouseInput;};
	s32 MouseInput_X(const SEvent::SMouseInput& pointer){return pointer.X;};
	s32 MouseInput_Y(const SEvent::SMouseInput& pointer){return pointer.Y;};
	f32 MouseInput_Wheel(const SEvent::SMouseInput& pointer){return pointer.Wheel;};
	bool MouseInput_Shift(const SEvent::SMouseInput& pointer){return pointer.Shift;};
	bool MouseInput_Control(const SEvent::SMouseInput& pointer){return pointer.Control;};
	u32 MouseInput_ButtonStates(const SEvent::SMouseInput& pointer){return pointer.ButtonStates;};
	bool MouseInput_isLeftPressed(const SEvent::SMouseInput& pointer){return pointer.isLeftPressed();};
	bool MouseInput_isRightPressed(const SEvent::SMouseInput& pointer){return pointer.isRightPressed();};
	bool MouseInput_isMiddlePressed(const SEvent::SMouseInput& pointer){return pointer.isMiddlePressed();};
	EMOUSE_INPUT_EVENT MouseInput_Event(const SEvent::SMouseInput& pointer){return pointer.Event;};
	EMOUSE_INPUT_EVENT MouseInput_EventType(const SEvent::SMouseInput& pointer){return pointer.Event;};

	const SEvent::SKeyInput& GetKeyInput(SEvent* pointer){return pointer->KeyInput;};
	wchar_t KeyInput_Char(const SEvent::SKeyInput& pointer){return pointer.Char;};
	EKEY_CODE KeyInput_Key(const SEvent::SKeyInput& pointer){return pointer.Key;};
	bool KeyInput_PressedDown(const SEvent::SKeyInput& pointer){return pointer.PressedDown;};
	bool KeyInput_Shift(const SEvent::SKeyInput& pointer){return pointer.Shift;};
	bool KeyInput_Control(const SEvent::SKeyInput& pointer){return pointer.Control;};

	const SEvent::SJoystickEvent& GetJoystickEvent(SEvent* pointer){return pointer->JoystickEvent;};
	u32 JoystickEvent_ButtonStates(const SEvent::SJoystickEvent& pointer){return pointer.ButtonStates;};
	s16 JoystickEvent_Axis(const SEvent::SJoystickEvent& pointer){return *(pointer.Axis);};
	u16 JoystickEvent_POV(const SEvent::SJoystickEvent& pointer){return pointer.POV;};
	u8 JoystickEvent_Joystick(const SEvent::SJoystickEvent& pointer){return pointer.Joystick;};
	bool JoystickEvent_IsButtonPressed(const SEvent::SJoystickEvent& pointer, u32 button){return pointer.IsButtonPressed(button);};

	const SEvent::SLogEvent& GetLogEvent(SEvent* pointer){return pointer->LogEvent;};
	//~ const c8* LogEvent_Text(const SEvent::SLogEvent& pointer){return pointer.Text;};
	ELOG_LEVEL LogEvent_Level(const SEvent::SLogEvent& pointer){return pointer.Level;};

	const SEvent::SUserEvent& GetUserEvent(SEvent* pointer){return pointer->UserEvent;};
	s32 UserEvent_UserData1(const SEvent::SUserEvent& pointer){return pointer.UserData1;};
	s32 UserEvent_UserData2(const SEvent::SUserEvent& pointer){return pointer.UserData2;};
}
%#if defined(_IRR_IMPROVE_UNICODE)
%extend irr::IEventReceiver
{const wchar_t* LogEvent_Text(const SEvent::SLogEvent& pointer){return pointer.Text;};}
%#else
%extend irr::IEventReceiver
{const c8* LogEvent_Text(const SEvent::SLogEvent& pointer){return pointer.Text;};}
%#endif

%include ITriangleSelector.h
%include IMetaTriangleSelector.h

%include IMeshBuffer.h
%include IMesh.h

%include IAnimatedMesh.h
%include IAnimatedMeshMD2.h

%include IQ3Shader.h
%include IQ3LevelMesh.h
%extend irr::scene::IQ3LevelMesh
{
	PyObject* get_EntityList()
	{
		PyObject* result;
		irr::scene::quake3::tQ3EntityList& entity_list = self->getEntityList();
		Py_ssize_t i, len = entity_list.size();
		result = PyTuple_New(len);
		for (i = 0; i < len; ++i)
			PyTuple_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(&entity_list[i]), $descriptor(irr::scene::quake3::IEntity*), 0));
		Py_INCREF(result);
		return result;
	};
}

%extend irr::scene::IAnimatedMesh
{
	irr::scene::IQ3LevelMesh* as_IQ3LevelMesh(){return (irr::scene::IQ3LevelMesh*)self;};
	irr::scene::IAnimatedMeshMD2* as_IAnimatedMeshMD2(){return (irr::scene::IAnimatedMeshMD2*)self;};
}

%include IGeometryCreator.h

//~ %ignore irr::scene::ISceneNode::getChildren();
//~ %ignore irr::scene::ISceneNode::getAnimators();
#if define(_IRR_STATIC_LIB_)
%ignore getMaterial;
#endif
%include ISceneNode.h
%extend irr::scene::ISceneNode
{
	void setMaterial(const irr::video::SMaterial& material, u32 num = 0){self->getMaterial(num) = material;};
	PyObject* get_childrens()
	{
		PyObject* result;
		const list<ISceneNode*>& nodes = self->getChildren();
		Py_ssize_t i, len = nodes.getSize();
		result = PyTuple_New(len);
		list<ISceneNode*>::ConstIterator it = nodes.begin();
		for (i = 0; it != nodes.end(); ++it, ++i)
			PyTuple_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(*it), $descriptor(irr::scene::ISceneNode*), 0));
		Py_INCREF(result);
		return result;
	};
	PyObject* get_animators()
	{
		PyObject* result;
		const list<ISceneNodeAnimator*>& nodes = self->getAnimators();
		Py_ssize_t i, len = nodes.getSize();
		result = PyTuple_New(len);
		list<ISceneNodeAnimator*>::ConstIterator it = nodes.begin();
		for (i = 0; it != nodes.end(); ++it, ++i)
			PyTuple_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(*it), $descriptor(irr::scene::ISceneNodeAnimator*), 0));
		Py_INCREF(result);
		return result;
	};
};
%include ISceneNodeFactory.h

%feature("director") irr::scene::ISceneNodeAnimator::OnEvent;
%include ISceneNodeAnimator.h
%extend irr::scene::ISceneNodeAnimator
{
	irr::scene::ISceneNodeAnimatorCameraFPS* as_ISceneNodeAnimatorCameraFPS(){return (irr::scene::ISceneNodeAnimatorCameraFPS*)self;};
	irr::scene::ISceneNodeAnimatorCameraMaya* as_ISceneNodeAnimatorCameraMaya(){return (irr::scene::ISceneNodeAnimatorCameraMaya*)self;};
	irr::scene::ISceneNodeAnimatorCollisionResponse* as_ISceneNodeAnimatorCollisionResponse(){return (irr::scene::ISceneNodeAnimatorCollisionResponse*)self;};
};

%include ISceneNodeAnimatorCameraFPS.h
%include ISceneNodeAnimatorCameraMaya.h

%feature("director") irr::scene::ICollisionCallback;
%include ISceneNodeAnimatorCollisionResponse.h

%include ISceneNodeAnimatorFactory.h
typedef irr::scene::ISceneNodeAnimator ISceneNodeAnimator;

%include IShadowVolumeSceneNode.h

%feature("director") irr::scene::IAnimationEndCallBack;
%include IAnimatedMeshSceneNode.h
//~ typedef irr::scene::IAnimationEndCallBack IAnimationEndCallBack;
//~ %extend irr::scene::IAnimationEndCallBack
//~ {
	//~ IAnimationEndCallBack* get_this(){return (IAnimationEndCallBack*)self;};
//~ }

%include IMeshSceneNode.h

%include ICameraSceneNode.h

#define _IRR_DEPRECATED_
%ignore addOctTreeSceneNode;
%ignore createOctTreeTriangleSelector;
%feature("compactdefaultargs") irr::scene::ISceneManager::addOctreeSceneNode;
%feature("compactdefaultargs") irr::scene::ISceneManager::createOctreeTriangleSelector;
%include ISceneManager.h
%extend irr::scene::ISceneManager
{
	irr::SKeyMap* create_keymaps(int length = 1)
	{
		irr::SKeyMap* keyMap;
		keyMap = new irr::SKeyMap[length];
		return keyMap;
	};
	void set_keymap(irr::SKeyMap* keymap, int index, EKEY_ACTION action, EKEY_CODE key_code){keymap[index].Action = action; keymap[index].KeyCode = key_code;};
	irr::scene::IAnimationEndCallBack* as_IAnimationEndCallBack(PyObject* pointer){return (irr::scene::IAnimationEndCallBack*)PyCObject_AsVoidPtr(pointer);};
}

%include IGUIElement.h
%include IGUIButton.h
%include IGUICheckBox.h
%include IGUIColorSelectDialog.h
%include IGUIComboBox.h
%include IGUIContextMenu.h

//%ignore setPasswordBox;
//line 88 in IGUIEditBox.h
//		virtual void setPasswordBox(bool passwordBox, wchar_t passwordChar = L'*') = 0;
//swig require patch for this method as next
//		virtual void setPasswordBox(bool passwordBox, wchar_t passwordChar = '*') = 0;
%include IGUIEditBox.h

%include IGUIElementFactory.h
%include IGUIFileOpenDialog.h

%include IGUIFont.h
#if !defined(_IRR_COMPILE_WITH_CGUITTFONT_)
%include IGUITTFont.h
%extend irr::gui::IGUIFont
{
	irr::gui::CGUITTFont* as_CGUITTFont(){return (irr::gui::CGUITTFont*)self;};
	irr::gui::CGUITTFont* createTTFont(IGUIEnvironment *env, const io::path& filename, const u32 size){return ((irr::gui::CGUITTFont*)self)->createTTFont(env, filename, size);};
};
#endif

%include IGUIFontBitmap.h
%include IGUIImage.h
%include IGUIImageList.h
%include IGUIInOutFader.h
%include IGUIListBox.h
%include IGUIMeshViewer.h
%include IGUIScrollBar.h
%include IGUISkin.h
%include IGUISpinBox.h

%include IGUISpriteBank.h
%extend irr::gui::SGUISprite
{
	PyObject* get_frames()
	{
		array<SGUISpriteFrame>* frames = &self->Frames;
		Py_ssize_t i, len = frames->size();
		PyObject* result;
		result = PyList_New(len);
		for (i = 0; i < len; ++i)
			PyList_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(&frames[i]), $descriptor(irr::gui::SGUISpriteFrame*), 0));
		Py_INCREF(result);
		return result;
	};
	void set_frames(PyObject* input_list)
	{
		if (PyList_Check(input_list))
		{
		array<SGUISpriteFrame>* frames = &self->Frames;
			frames->clear();
			Py_ssize_t i, len = PyList_Size(input_list);
			for (i = 0; i < len; ++i)
				frames->push_back((SGUISpriteFrame const &)*reinterpret_cast<SGUISpriteFrame*>(PyCObject_AsVoidPtr(PyList_GetItem(input_list, i))));
		}
		else
			printf("ARGUMENT set_frames FUNCTION MUST BE TYPE LIST");
	};
	void frames_push_back(SGUISpriteFrame* frame){self->Frames.push_back((SGUISpriteFrame const &)*frame);};
	void frames_set_used(u32 usedNow){self->Frames.set_used(usedNow);};
	void frames_set_free_when_destroyed(bool f){self->Frames.set_free_when_destroyed(f);};
};
%extend irr::gui::IGUISpriteBank
{
	PyObject* get_sprites()
	{
		array<SGUISprite>& sprites = self->getSprites();
		Py_ssize_t i, len = sprites.size();
		PyObject* result;
		result = PyList_New(len);
		for (i = 0; i < len; ++i)
			PyList_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(&sprites[i]), $descriptor(irr::gui::SGUISprite*), 0));
		Py_INCREF(result);
		return result;
	};
	void set_sprites(PyObject* input_list)
	{
		if (PyList_Check(input_list))
		{
			array<SGUISprite>& sprites = self->getSprites();
			sprites.clear();
			Py_ssize_t i, len = PyList_Size(input_list);
			for (i = 0; i < len; ++i)
				sprites.push_back((SGUISprite const &)*reinterpret_cast<SGUISprite*>(PyCObject_AsVoidPtr(PyList_GetItem(input_list, i))));
		}
		else
			printf("ARGUMENT set_sprites FUNCTION MUST BE TYPE LIST");
	};
	void sprites_push_back(SGUISprite* sprite){self->getSprites().push_back((SGUISprite const &)*sprite);};
	void sprites_clear(){self->getSprites().clear();};
	u32 sprites_size(){return self->getSprites().size();};
	void sprites_set_used(u32 usedNow){self->getSprites().set_used(usedNow);};
	void sprites_set_free_when_destroyed(bool f){self->getSprites().set_free_when_destroyed(f);};

	PyObject* get_positions()
	{
		array< rect<s32> >& positions = self->getPositions();
		Py_ssize_t i, len = positions.size();
		PyObject* result;
		result = PyList_New(len);
		for (i = 0; i < len; ++i)
			PyList_SetItem(result, i, SWIG_NewPointerObj(SWIG_as_voidptr(&positions[i]), $descriptor(irr::core::recti*), 0));
		Py_INCREF(result);
		return result;
	};
	void set_positions(PyObject* input_list)
	{
		if (PyList_Check(input_list))
		{
			array< rect<s32> >& positions = self->getPositions();
			positions.clear();
			Py_ssize_t i, len = PyList_Size(input_list);
			for (i = 0; i < len; ++i)
				positions.push_back((rect<s32> const &)*reinterpret_cast< rect<s32>* >(PyCObject_AsVoidPtr(PyList_GetItem(input_list, i))));
		}
		else
			printf("ARGUMENT set_positions FUNCTION MUST BE TYPE LIST");
	};
	void positions_push_back(const irr::core::rect<irr::s32>& pos){self->getPositions().push_back(pos);};
	void positions_clear(){self->getPositions().clear();};
	u32 positions_size(){return self->getPositions().size();};
	void positions_set_used(u32 usedNow){self->getPositions().set_used(usedNow);};
	void positions_set_free_when_destroyed(bool f){self->getPositions().set_free_when_destroyed(f);};
};

%include IGUIStaticText.h
%include IGUITabControl.h
%include IGUITable.h
%include IGUIToolbar.h
%include IGUITreeView.h
%include IGUIWindow.h
%extend irr::gui::IGUIElement
{
	irr::gui::IGUIButton* as_IGUIButton(){return (irr::gui::IGUIButton*)self;};
	irr::gui::IGUICheckBox* as_IGUICheckBox(){return (irr::gui::IGUICheckBox*)self;};
	irr::gui::IGUIColorSelectDialog* as_IGUIColorSelectDialog(){return (irr::gui::IGUIColorSelectDialog*)self;};
	irr::gui::IGUIComboBox* as_IGUIComboBox(){return (irr::gui::IGUIComboBox*)self;};
	irr::gui::IGUIContextMenu* as_IGUIContextMenu(){return (irr::gui::IGUIContextMenu*)self;};
	irr::gui::IGUIEditBox* as_IGUIEditBox(){return (irr::gui::IGUIEditBox*)self;};
	irr::gui::IGUIFileOpenDialog* as_IGUIFileOpenDialog(){return (irr::gui::IGUIFileOpenDialog*)self;};
	irr::gui::IGUIFontBitmap* as_IGUIFontBitmap(){return (irr::gui::IGUIFontBitmap*)self;};
	irr::gui::IGUIImage* as_IGUIImage(){return (irr::gui::IGUIImage*)self;};
	irr::gui::IGUIListBox* as_IGUIListBox(){return (irr::gui::IGUIListBox*)self;};
	irr::gui::IGUIMeshViewer* as_IGUIMeshViewer(){return (irr::gui::IGUIMeshViewer*)self;};
	irr::gui::IGUIScrollBar* as_IGUIScrollBar(){return (irr::gui::IGUIScrollBar*)self;};
	irr::gui::IGUISpinBox* as_IGUISpinBox(){return (irr::gui::IGUISpinBox*)self;};
	irr::gui::IGUIStaticText* as_IGUIStaticText(){return (irr::gui::IGUIStaticText*)self;};
	irr::gui::IGUITab* as_IGUITab(){return (irr::gui::IGUITab*)self;};
	irr::gui::IGUITabControl* as_IGUITabControl(){return (irr::gui::IGUITabControl*)self;};
	irr::gui::IGUITable* as_IGUITable(){return (irr::gui::IGUITable*)self;};
	irr::gui::IGUIToolBar* as_IGUIToolBar(){return (irr::gui::IGUIToolBar*)self;};
	irr::gui::IGUITreeView* as_IGUITreeView(){return (irr::gui::IGUITreeView*)self;};
	irr::gui::IGUIWindow* as_IGUIWindow(){return (irr::gui::IGUIWindow*)self;};
};

%include IGUIEnvironment.h
%extend irr::gui::IGUIEnvironment
{
	irr::gui::CGUITTFont* createTTFont(const io::path& filename, const u32 size){return irr::gui::CGUITTFont::createTTFont(self, filename, size);};
};

%include IImage.h
%include IImageLoader.h
%include IImageWriter.h
%include IIndexBuffer.h
%include ILightSceneNode.h
%include ILightManager.h

%include ILogger.h

%#if defined(_IRR_IMPROVE_UNICODE)
%ignore copyToClipboard;
%ignore getTextFromClipboard;
%#endif
%include IOSOperator.h

%include ITimer.h

%include IrrlichtDevice.h

%include ISceneUserDataSerializer.h
%include ISceneCollisionManager.h
%include IMaterialRendererServices.h
%include IShaderConstantSetCallBack.h
%include IParticleSystemSceneNode.h
%include ITerrainSceneNode.h
%include ITextSceneNode.h
%include IParticleEmitter.h
%include IParticleAffector.h
%include IBillboardSceneNode.h
%include IMaterialRenderer.h

%include ITexture.h

%include SExposedVideoData.h
%include IGPUProgrammingServices.h

// these functions use deprecated type position2d, replace later with new type vector2d
%ignore irr::video::IVideoDriver::makeColorKeyTexture(video::ITexture* texture, core::position2d<s32> colorKeyPixelPos, bool zeroTexels = false);
%ignore irr::video::IVideoDriver::draw2DImage(const video::ITexture* texture, const core::position2d<s32>& destPos);
%ignore irr::video::IVideoDriver::draw2DImage(const video::ITexture* texture, const core::position2d<s32>& destPos, const core::rect<s32>& sourceRect, const core::rect<s32>* clipRect =0, SColor color=SColor(255,255,255,255), bool useAlphaChannelOfTexture=false);
%ignore irr::video::IVideoDriver::draw2DImageBatch;
%include IVideoDriver.h
%extend irr::video::IVideoDriver
{
	//~ void makeColorKeyTexture(video::ITexture* texture, video::SColor color, bool zeroTexels = false){self->makeColorKeyTexture(texture, color, zeroTexels);};
	void makeColorKeyTexture(video::ITexture* texture, core::vector2di colorKeyPixelPos, bool zeroTexels = false){self->makeColorKeyTexture(texture, colorKeyPixelPos, zeroTexels);};
	void draw2DImage(const video::ITexture* texture, const core::vector2di& destPos){self->draw2DImage(texture, destPos);};
	void draw2DImage(const video::ITexture* texture, const core::vector2di& destPos, const core::recti& sourceRect, const core::recti* clipRect =0, SColor color=SColor(255,255,255,255), bool useAlphaChannelOfTexture=false){self->draw2DImage(texture, destPos, sourceRect, clipRect, color, useAlphaChannelOfTexture);};
	void draw2DImageBatch(const video::ITexture* texture, const core::vector2di& pos, const core::array<core::recti>& sourceRects, const core::array<s32>& indices, s32 kerningWidth=0, const core::recti* clipRect=0, SColor color=SColor(255,255,255,255), bool useAlphaChannelOfTexture=false){self->(texture, pos, sourceRects, indices, kerningWidth, clipRect, color, useAlphaChannelOfTexture);};
	void draw2DImageBatch(const video::ITexture* texture, const core::array<core::vector2di>& positions, const core::array<core::recti>& sourceRects, const core::recti* clipRect=0, SColor color=SColor(255,255,255,255), bool useAlphaChannelOfTexture=false){self->(texture, positions, sourceRects, clipRect, color, useAlphaChannelOfTexture);};
}

%include IVideoModeList.h
%include IrrCompileConfig.h

#if define(_IRR_STATIC_LIB_)
%ignore IdentityMatrix;
#endif
%include matrix4.h
%template(matrix4) irr::core::CMatrix4<irr::f32>;

%include quaternion.h

%ignore io::SNamedPath::stringc;
%ignore io::SNamedPath::stringw;
%include path.h

%include SAnimatedMesh.h

%include SIrrCreationParameters.h

%include S3DVertex.h
%include SLight.h

#if define(_IRR_STATIC_LIB_)
%ignore getTextureMatrix;
%ignore IdentityMaterial;
#endif
%include SMaterial.h
%include SMaterialLayer.h

%include SMesh.h
%include SMeshBuffer.h
%include SMeshBufferLightMap.h
%include SMeshBufferTangents.h
%include SViewFrustum.h

%ignore createMemoryReadFile;
%ignore createReadFile;
%ignore createLimitReadFile;
%include IReadFile.h

%ignore createWriteFile;
//~ %ignore irr::io::IWriteFile::write;
%include IWriteFile.h
%extend irr::io::IWriteFile
{
	virtual s32 write(PyObject* buffer, u32 sizeToWrite)
	{
%#if PY_VERSION_HEX >= 0x03000000
		if (PyUnicode_Check(buffer))
			return self->write(SWIG_as_voidptr(PyUnicode_AsUnicode(buffer)), sizeToWrite);
%#else
		if (PyString_Check(buffer))
			return self->write(SWIG_as_voidptr(PyString_AsString(buffer)), sizeToWrite);
		else
			if (PyUnicode_Check(buffer))
				return self->write(SWIG_as_voidptr(PyUnicode_AS_UNICODE(buffer)), sizeToWrite);
%#endif
		if (PyCObject_Check(buffer))
			return self->write(PyCObject_AsVoidPtr(buffer), sizeToWrite);
		printf("ARGUMENT IWriteFile::write FUNCTION MUST BE TYPE STRING");
		return 0;
	};
};

%include irrXML.h
%include IXMLReader.h
%template(IXMLReader) irr::io::IIrrXMLReader<wchar_t, IReferenceCounted>;
%template(IXMLReaderUTF8) irr::io::IIrrXMLReader<c8, IReferenceCounted>;

%include IXMLWriter.h

%include IFileList.h
%include IFileArchive.h
%include IFileSystem.h

//~ %feature("director") irr::scene::quake3::Q3LevelLoadParameter;
//~ %feature("director") irr::scene::quake3::Noiser;
//~ %feature("director") irr::scene::quake3::SModifierFunction;
//~ %feature("director") irr::scene::quake3::SVariable;
//~ %feature("director") irr::scene::quake3::SVarGroup;
//~ %feature("director") irr::scene::quake3::SVarGroupList;
//~ %feature("director") irr::scene::quake3::IShader;
//line 21 in IQ3Shader.h
//	static core::stringc irrEmptyStringc("");
//change to
//	static core::stringc irrEmptyStringc = "";
%include IQ3Shader.h

%include coreutil.h

namespace irr
{
	IRRLICHT_API IrrlichtDevice* IRRCALLCONV createDevice(
		video::E_DRIVER_TYPE deviceType = video::EDT_SOFTWARE, 
		const core::dimension2d<u32>& windowSize = core::dimension2d<u32>(640,480),
		u32 bits = 16,
		bool fullscreen = false,
		bool stencilbuffer = false,
		bool vsync = false,
		IEventReceiver* receiver = 0);

	IRRLICHT_API IrrlichtDevice* IRRCALLCONV createDeviceEx(
		const SIrrlichtCreationParameters& parameters);
}

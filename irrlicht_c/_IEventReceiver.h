// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

// ffi calling convention
//#define FFI_CALL __cdecl
//#define FFI_CALL __stdcall

#ifdef __cplusplus
extern "C" {
#endif

//================= SJoystickInfo
IRRLICHT_C_API SJoystickInfo* SJoystickInfo_ctor(int length = 1)
{SJoystickInfo* result; result = new SJoystickInfo[length]; return result;}
IRRLICHT_C_API u8 SJoystickInfo_get_Joystick(SJoystickInfo* pointer)
{return pointer->Joystick;}
IRRLICHT_C_API void SJoystickInfo_set_Joystick(SJoystickInfo* pointer, u8 value)
{pointer->Joystick = value;}
//IRRLICHT_C_API const char* SJoystickInfo_get_Name(SJoystickInfo* pointer)
//{return reinterpret_cast<const char*>(&pointer->Name);}
IRRLICHT_C_API const c8* SJoystickInfo_get_Name(SJoystickInfo* pointer)
{return pointer->Name.c_str();}
IRRLICHT_C_API void SJoystickInfo_set_Name(SJoystickInfo* pointer, const c8* value)
{pointer->Name = core::stringc(value);}
IRRLICHT_C_API u32 SJoystickInfo_get_Buttons(SJoystickInfo* pointer)
{return pointer->Buttons;}
IRRLICHT_C_API void SJoystickInfo_set_Buttons(SJoystickInfo* pointer, u32 value)
{pointer->Buttons = value;}
IRRLICHT_C_API u32 SJoystickInfo_get_Axes(SJoystickInfo* pointer)
{return pointer->Axes;}
IRRLICHT_C_API void SJoystickInfo_set_Axes(SJoystickInfo* pointer, u32 value)
{pointer->Axes = value;}
IRRLICHT_C_API int SJoystickInfo_get_PovHat(SJoystickInfo* pointer)
{return pointer->PovHat;}
//IRRLICHT_C_API void SJoystickInfo_set_PovHat(SJoystickInfo* pointer, irr::SJoystickInfo::PovHat value)
//{pointer->PovHat = value;}

//================= IEventReceiver
//IRRLICHT_C_API SEvent* SEvent_SEvent(){return new SEvent();}
//IRRLICHT_C_API SEvent* SEvent_void_to_SEvent(void* ptr){return (SEvent*)ptr;}
IRRLICHT_C_API EEVENT_TYPE SEvent_GetEventType(SEvent* pointer){return pointer->EventType;}

IRRLICHT_C_API const SEvent::SGUIEvent* SEvent_GetSGUIEvent(SEvent* pointer){return &pointer->GUIEvent;}
IRRLICHT_C_API IGUIElement* SGUIEvent_GetCaller(const SEvent::SGUIEvent* pointer){return pointer->Caller;}
IRRLICHT_C_API IGUIElement* SGUIEvent_GetElement(const SEvent::SGUIEvent* pointer){return pointer->Element;}
IRRLICHT_C_API EGUI_EVENT_TYPE SGUIEvent_GetEventType(const SEvent::SGUIEvent* pointer){return pointer->EventType;}

IRRLICHT_C_API const SEvent::SMouseInput* SEvent_GetSMouseInput(SEvent* pointer){return &pointer->MouseInput;}
IRRLICHT_C_API s32 SMouseInput_GetX(const SEvent::SMouseInput* pointer){return pointer->X;}
IRRLICHT_C_API s32 SMouseInput_GetY(const SEvent::SMouseInput* pointer){return pointer->Y;}
IRRLICHT_C_API f32 SMouseInput_GetWheel(const SEvent::SMouseInput* pointer){return pointer->Wheel;}
IRRLICHT_C_API bool SMouseInput_GetShift(const SEvent::SMouseInput* pointer){return pointer->Shift;}
IRRLICHT_C_API bool SMouseInput_GetControl(const SEvent::SMouseInput* pointer){return pointer->Control;}
IRRLICHT_C_API u32 SMouseInput_GetButtonStates(const SEvent::SMouseInput* pointer){return pointer->ButtonStates;}
IRRLICHT_C_API bool SMouseInput_isLeftPressed(const SEvent::SMouseInput* pointer){return pointer->isLeftPressed();}
IRRLICHT_C_API bool SMouseInput_isRightPressed(const SEvent::SMouseInput* pointer){return pointer->isRightPressed();}
IRRLICHT_C_API bool SMouseInput_isMiddlePressed(const SEvent::SMouseInput* pointer){return pointer->isMiddlePressed();}
IRRLICHT_C_API EMOUSE_INPUT_EVENT SMouseInput_GetEventType(const SEvent::SMouseInput* pointer){return pointer->Event;}

IRRLICHT_C_API const SEvent::SKeyInput* SEvent_GetSKeyInput(SEvent* pointer){return &pointer->KeyInput;}
IRRLICHT_C_API wchar_t SKeyInput_GetChar(const SEvent::SKeyInput* pointer){return pointer->Char;}
IRRLICHT_C_API EKEY_CODE SKeyInput_GetKey(const SEvent::SKeyInput* pointer){return pointer->Key;}
IRRLICHT_C_API bool SKeyInput_GetPressedDown(const SEvent::SKeyInput* pointer){return pointer->PressedDown;}
IRRLICHT_C_API bool SKeyInput_GetShift(const SEvent::SKeyInput* pointer){return pointer->Shift;}
IRRLICHT_C_API bool SKeyInput_GetControl(const SEvent::SKeyInput* pointer){return pointer->Control;}

IRRLICHT_C_API const SEvent::SJoystickEvent* SEvent_GetSJoystickEvent(SEvent* pointer){return &pointer->JoystickEvent;}
IRRLICHT_C_API u32 SJoystickEvent_GetButtonStates(const SEvent::SJoystickEvent* pointer){return pointer->ButtonStates;}
IRRLICHT_C_API s16 SJoystickEvent_GetAxis(const SEvent::SJoystickEvent* pointer){return *(pointer->Axis);}
IRRLICHT_C_API u16 SJoystickEvent_GetPOV(const SEvent::SJoystickEvent* pointer){return pointer->POV;}
IRRLICHT_C_API u8 SJoystickEvent_GetJoystick(const SEvent::SJoystickEvent* pointer){return pointer->Joystick;}
IRRLICHT_C_API bool SJoystickEvent_IsButtonPressed(const SEvent::SJoystickEvent* pointer, u32 button){return pointer->IsButtonPressed(button);}

IRRLICHT_C_API core::array<SJoystickInfo>* arraySJoystickInfo_ctor()
{return new core::array<SJoystickInfo>();}
IRRLICHT_C_API irr::u32 arraySJoystickInfo_allocated_size(core::array<SJoystickInfo>* pointer)
{return pointer->allocated_size();}
IRRLICHT_C_API irr::u32 arraySJoystickInfo_size(core::array<SJoystickInfo>* pointer)
{return pointer->size();}
IRRLICHT_C_API void arraySJoystickInfo_set_free_when_destroyed(core::array<SJoystickInfo>* pointer, bool f)
{pointer->set_free_when_destroyed(f);}
IRRLICHT_C_API void arraySJoystickInfo_set_used(core::array<SJoystickInfo>* pointer, u32 usedNow)
{pointer->set_used(usedNow);}
IRRLICHT_C_API SJoystickInfo* arraySJoystickInfo_get_item(core::array<SJoystickInfo>* pointer, u32 index)
{return &pointer->operator [](index);}


IRRLICHT_C_API const SEvent::SLogEvent* SEvent_GetSLogEvent(SEvent* pointer){return &pointer->LogEvent;}
#ifdef _IRR_IMPROVE_UNICODE
IRRLICHT_C_API const wchar_t* SLogEvent_GetText(const SEvent::SLogEvent& pointer){return pointer->Text;}
#else
IRRLICHT_C_API const c8* SLogEvent_GetText(const SEvent::SLogEvent* pointer){return pointer->Text;}
#endif
IRRLICHT_C_API ELOG_LEVEL SLogEvent_GetLevel(const SEvent::SLogEvent* pointer){return pointer->Level;}

IRRLICHT_C_API const SEvent::SUserEvent* SEvent_GetSUserEvent(SEvent* pointer){return &pointer->UserEvent;}
IRRLICHT_C_API s32 SUserEvent_GetUserData1(const SEvent::SUserEvent* pointer){return pointer->UserData1;}
IRRLICHT_C_API s32 SUserEvent_GetUserData2(const SEvent::SUserEvent* pointer){return pointer->UserData2;}

#ifdef _IRR_USE_INPUT_METHOD
IRRLICHT_C_API const SEvent::SInputMethodEvent* SEvent_GetSInputMethodEvent(SEvent* pointer){return &pointer->InputMethodEvent;}
IRRLICHT_C_API void* SInputMethodEvent_GetHandle(const SEvent::SInputMethodEvent* pointer){return pointer->Handle;}
IRRLICHT_C_API wchar_t SInputMethodEvent_GetChar(const SEvent::SInputMethodEvent* pointer){return pointer->Char;}
IRRLICHT_C_API EINPUT_METHOD_EVENT SInputMethodEvent_GetEvent(const SEvent::SInputMethodEvent* pointer){return pointer->Event;}
#endif

class UserEventReceiver : public IEventReceiver
{
public:
	UserEventReceiver(bool(IRRCALLCONV *func)(const SEvent&) = false)
	{
		func_event = func;
	}
	virtual bool OnEvent(const SEvent& event)
	{
		if (func_event != NULL)
		{
#ifdef _MSC_VER
#ifdef DEBUG_EVENTS
			__try
			{
				return (*func_event)(event);
			}
			__except(filter(_exception_code(), (struct _EXCEPTION_POINTERS *)_exception_info(), "UserEventReceiver::OnEvent"))
			{
				return false;
			}
#else
			return (*func_event)(event);
#endif
#else
			return (*func_event)(event);
#endif
		}
		else
		{
			return false;
		}
	}
	virtual void set_func_event(bool(IRRCALLCONV *func)(const SEvent&))
	{
		func_event = func;
	}
	~UserEventReceiver()
	{
		func_event = NULL;
	}
private:
	bool(IRRCALLCONV *func_event)(const SEvent&);
};
IRRLICHT_C_API UserEventReceiver* IEventReceiver_ctor1(IEventReceiver* pointer){return (UserEventReceiver*)pointer;}
IRRLICHT_C_API UserEventReceiver* IEventReceiver_ctor2(bool(IRRCALLCONV *OnEventMethod)(const SEvent&)){return new UserEventReceiver(OnEventMethod);}
//IRRLICHT_C_API void IEventReceiver_Destructor(void* pointer){delete pointer;}
IRRLICHT_C_API void IEventReceiver_set_func_event(UserEventReceiver* pointer, bool(IRRCALLCONV *OnEventMethod)(const SEvent&)){pointer->set_func_event(OnEventMethod);}

/*
IRRLICHT_C_API IEventReceiver* IEventReceiverV_virt_ctor(){return new IEventReceiver();}
IRRLICHT_C_API bool IEventReceiverV_set_func_event(IEventReceiver* pointer, void* OnEventMethod)
{
#ifdef _MSC_VER
#ifndef DEBUG
	//size_t* vptr =  *(size_t**)pointer;
	//__asm{mov ecx, pointer}
	//( (bool (IRRCALLCONV*)(const SEvent&)) (*(size_t**)pointer)[3] ) = OnEventMethod;
	(*(size_t**)pointer)[3] = (size_t)OnEventMethod;
	return true;
#else
	printf("ISceneNodeAnimator_set_func_event only for RELEASE mode, current is DEBUG!");
	return false;
#endif
#else
	pointer->_vptr[3] = OnEventMethod;
	return true;
#endif
}
*/

#ifdef __cplusplus
}
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IOSOperator
//IRRLICHT_C_API void IOSOperator_Destructor(IOSOperator* pointer){delete pointer;}
IRRLICHT_C_API const wchar_t* IOSOperator_getOperationSystemVersion(IOSOperator* pointer){return pointer->getOperationSystemVersion();}
#ifdef _IRR_IMPROVE_UNICODE
IRRLICHT_C_API void IOSOperator_copyToClipboard(IOSOperator* pointer, const wchar_t* text){pointer->copyToClipboard(text);}
IRRLICHT_C_API const wchar_t* IOSOperator_getTextFromClipboard(IOSOperator* pointer){return pointer->getTextFromClipboard();}
#else
IRRLICHT_C_API void IOSOperator_copyToClipboard(IOSOperator* pointer, const c8* text){pointer->copyToClipboard(text);}
IRRLICHT_C_API const c8* IOSOperator_getTextFromClipboard(IOSOperator* pointer){return pointer->getTextFromClipboard();}
#endif
IRRLICHT_C_API bool IOSOperator_getProcessorSpeedMHz(IOSOperator* pointer, u32* MHz){return pointer->getProcessorSpeedMHz(MHz);}
IRRLICHT_C_API bool IOSOperator_getSystemMemory(IOSOperator* pointer, u32* Total, u32* Avail){return pointer->getSystemMemory(Total, Avail);}

#ifdef __cplusplus
}
#endif

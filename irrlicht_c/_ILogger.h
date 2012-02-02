// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= ILogger
//IRRLICHT_C_API void ILogger_Destructor(ILogger* pointer){delete pointer;}
IRRLICHT_C_API ELOG_LEVEL ILogger_getLogLevel(ILogger* pointer){return pointer->getLogLevel();}
IRRLICHT_C_API void ILogger_setLogLevel(ILogger* pointer, ELOG_LEVEL ll){pointer->setLogLevel(ll);}
IRRLICHT_C_API void ILogger_log(ILogger* pointer, const c8* text, ELOG_LEVEL ll=ELL_INFORMATION){pointer->log(text, ll);}
IRRLICHT_C_API void ILogger_log2(ILogger* pointer, const c8* text, const c8* hint, ELOG_LEVEL ll=ELL_INFORMATION){pointer->log(text, hint, ll);}
IRRLICHT_C_API void ILogger_log3(ILogger* pointer, const c8* text, const wchar_t* hint, ELOG_LEVEL ll=ELL_INFORMATION){pointer->log(text, hint, ll);}
IRRLICHT_C_API void ILogger_log4(ILogger* pointer, const wchar_t* text, const wchar_t* hint, ELOG_LEVEL ll=ELL_INFORMATION){pointer->log(text, hint, ll);}
IRRLICHT_C_API void ILogger_log5(ILogger* pointer, const wchar_t* text, ELOG_LEVEL ll=ELL_INFORMATION){pointer->log(text, ll);}

#ifdef __cplusplus
}
#endif

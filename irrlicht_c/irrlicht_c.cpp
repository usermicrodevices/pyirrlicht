// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license
#include "irrlicht_c.h"

#ifdef _COMPILE_WITH_2DTTFONT_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "freetype2312MT_D.lib")
#else
#pragma comment(lib, "freetype2312MT.lib")
#endif//_DEBUG
#else//LINUX
#ifdef _DEBUG
#pragma comment(lib, "freetype2312MT_D.a")
#else
#pragma comment(lib, "freetype2312MT.a")
#endif//_DEBUG
#endif//_IRR_WINDOWS_
#endif//_COMPILE_WITH_2DTTFONT_

#ifdef _COMPILE_WITH_AGG_ || _COMPILE_WITH_IRR_SVG_AGG_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "libexpatMT_D.lib")
#else//_NDEBUG
#pragma comment(lib, "libexpatMT.lib")
#endif
#else//LINUX
#ifdef _DEBUG
#pragma comment(lib, "libexpatMT_D.a")
#else//_NDEBUG
#pragma comment(lib, "libexpatMT.a")
#endif
#endif
#endif

#ifdef _COMPILE_WITH_IRR_SVG_CAIRO_
#ifdef _IRR_WINDOWS_
#ifdef _DEBUG
#pragma comment(lib, "cairo_d.lib")
#else//_NDEBUG
//#pragma comment(lib, "msimg32.lib")
//#pragma comment(lib, "pixman-1.lib")
//#pragma comment(lib, "cairo-static.lib")
#pragma comment(lib, "cairo.lib")
#endif
#else//LINUX
#ifdef _DEBUG
#pragma comment(lib, "cairo_d.a")
#else
#pragma comment(lib, "cairo.a")
#endif
#endif
#endif

// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IXMLWriter
//IRRLICHT_C_API void IXMLWriter_Destructor(IXMLWriter* pointer){delete pointer;}
IRRLICHT_C_API void IXMLWriter_writeXMLHeader(IXMLWriter* pointer)
{pointer->writeXMLHeader();}
IRRLICHT_C_API void IXMLWriter_writeElement1(IXMLWriter* pointer, const wchar_t* name, bool empty = false, const wchar_t* attr1Name = 0, const wchar_t* attr1Value = 0, const wchar_t* attr2Name = 0, const wchar_t* attr2Value = 0, const wchar_t* attr3Name = 0, const wchar_t* attr3Value = 0, const wchar_t* attr4Name = 0, const wchar_t* attr4Value = 0, const wchar_t* attr5Name = 0, const wchar_t* attr5Value = 0)
{pointer->writeElement(name, empty, attr1Name, attr1Value, attr2Name, attr2Value, attr3Name, attr3Value, attr4Name, attr4Value, attr5Name, attr5Value);}
IRRLICHT_C_API void IXMLWriter_writeElement2(IXMLWriter* pointer, const wchar_t* name, bool empty, core::array<core::stringw>* names, core::array<core::stringw>* values)
{pointer->writeElement(name, empty, *names, *values);}
IRRLICHT_C_API void IXMLWriter_writeComment(IXMLWriter* pointer, const wchar_t* comment)
{pointer->writeComment(comment);}
IRRLICHT_C_API void IXMLWriter_writeClosingTag(IXMLWriter* pointer, const wchar_t* name)
{pointer->writeClosingTag(name);}
IRRLICHT_C_API void IXMLWriter_writeText(IXMLWriter* pointer, const wchar_t* text)
{pointer->writeText(text);}
IRRLICHT_C_API void IXMLWriter_writeLineBreak(IXMLWriter* pointer)
{pointer->writeLineBreak();}

#ifdef __cplusplus
}
#endif

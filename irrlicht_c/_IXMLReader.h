// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IXMLReader
IRRLICHT_C_API bool IXMLReader_read(IXMLReader* pointer)
{return pointer->read();}
IRRLICHT_C_API EXML_NODE IXMLReader_getNodeType(IXMLReader* pointer)
{return pointer->getNodeType();}
IRRLICHT_C_API unsigned int IXMLReader_getAttributeCount(IXMLReader* pointer)
{return pointer->getAttributeCount();}
IRRLICHT_C_API const wchar_t* IXMLReader_getAttributeName(IXMLReader* pointer, int idx)
{return pointer->getAttributeName(idx);}
IRRLICHT_C_API const wchar_t* IXMLReader_getAttributeValue1(IXMLReader* pointer, int idx)
{return pointer->getAttributeValue(idx);}
IRRLICHT_C_API const wchar_t* IXMLReader_getAttributeValue2(IXMLReader* pointer, const wchar_t* name)
{return pointer->getAttributeValue(name);}
IRRLICHT_C_API const wchar_t* IXMLReader_getAttributeValueSafe(IXMLReader* pointer, const wchar_t* name)
{return pointer->getAttributeValueSafe(name);}
IRRLICHT_C_API int IXMLReader_getAttributeValueAsInt1(IXMLReader* pointer, const wchar_t* name)
{return pointer->getAttributeValueAsInt(name);}
IRRLICHT_C_API int IXMLReader_getAttributeValueAsInt2(IXMLReader* pointer, int idx)
{return pointer->getAttributeValueAsInt(idx);}
IRRLICHT_C_API float IXMLReader_getAttributeValueAsFloat1(IXMLReader* pointer, const wchar_t* name)
{return pointer->getAttributeValueAsFloat(name);}
IRRLICHT_C_API float IXMLReader_getAttributeValueAsFloat2(IXMLReader* pointer, int idx)
{return pointer->getAttributeValueAsFloat(idx);}
IRRLICHT_C_API const wchar_t* IXMLReader_getNodeName(IXMLReader* pointer)
{return pointer->getNodeName();}
IRRLICHT_C_API const wchar_t* IXMLReader_getNodeData(IXMLReader* pointer)
{return pointer->getNodeData();}
IRRLICHT_C_API bool IXMLReader_isEmptyElement(IXMLReader* pointer)
{return pointer->isEmptyElement();}
IRRLICHT_C_API ETEXT_FORMAT IXMLReader_getSourceFormat(IXMLReader* pointer)
{return pointer->getSourceFormat();}
IRRLICHT_C_API ETEXT_FORMAT IXMLReader_getParserFormat(IXMLReader* pointer)
{return pointer->getParserFormat();}

//================= IXMLReaderUTF8
IRRLICHT_C_API bool IXMLReaderUTF8_read(IXMLReaderUTF8* pointer)
{return pointer->read();}
IRRLICHT_C_API EXML_NODE IXMLReaderUTF8_getNodeType(IXMLReaderUTF8* pointer)
{return pointer->getNodeType();}
IRRLICHT_C_API unsigned int IXMLReaderUTF8_getAttributeCount(IXMLReaderUTF8* pointer)
{return pointer->getAttributeCount();}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getAttributeName(IXMLReaderUTF8* pointer, int idx)
{return pointer->getAttributeName(idx);}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getAttributeValue1(IXMLReaderUTF8* pointer, int idx)
{return pointer->getAttributeValue(idx);}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getAttributeValue2(IXMLReaderUTF8* pointer, const c8* name)
{return pointer->getAttributeValue(name);}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getAttributeValueSafe(IXMLReaderUTF8* pointer, const c8* name)
{return pointer->getAttributeValueSafe(name);}
IRRLICHT_C_API int IXMLReaderUTF8_getAttributeValueAsInt1(IXMLReaderUTF8* pointer, const c8* name)
{return pointer->getAttributeValueAsInt(name);}
IRRLICHT_C_API int IXMLReaderUTF8_getAttributeValueAsInt2(IXMLReaderUTF8* pointer, int idx)
{return pointer->getAttributeValueAsInt(idx);}
IRRLICHT_C_API float IXMLReaderUTF8_getAttributeValueAsFloat1(IXMLReaderUTF8* pointer, const c8* name)
{return pointer->getAttributeValueAsFloat(name);}
IRRLICHT_C_API float IXMLReaderUTF8_getAttributeValueAsFloat2(IXMLReaderUTF8* pointer, int idx)
{return pointer->getAttributeValueAsFloat(idx);}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getNodeName(IXMLReaderUTF8* pointer)
{return pointer->getNodeName();}
IRRLICHT_C_API const c8* IXMLReaderUTF8_getNodeData(IXMLReaderUTF8* pointer)
{return pointer->getNodeData();}
IRRLICHT_C_API bool IXMLReaderUTF8_isEmptyElement(IXMLReaderUTF8* pointer)
{return pointer->isEmptyElement();}
IRRLICHT_C_API ETEXT_FORMAT IXMLReaderUTF8_getSourceFormat(IXMLReaderUTF8* pointer)
{return pointer->getSourceFormat();}
IRRLICHT_C_API ETEXT_FORMAT IXMLReaderUTF8_getParserFormat(IXMLReaderUTF8* pointer)
{return pointer->getParserFormat();}

#ifdef __cplusplus
}
#endif

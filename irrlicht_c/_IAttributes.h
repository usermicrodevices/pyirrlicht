// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IAttributes
IRRLICHT_C_API u32 IAttributes_getAttributeCount(IAttributes* pointer)
{return pointer->getAttributeCount();}
IRRLICHT_C_API const c8* IAttributes_getAttributeName(IAttributes* pointer, s32 index)
{return pointer->getAttributeName(index);}

IRRLICHT_C_API E_ATTRIBUTE_TYPE IAttributes_getAttributeType1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeType(attributeName);}
IRRLICHT_C_API E_ATTRIBUTE_TYPE IAttributes_getAttributeType2(IAttributes* pointer, s32 index)
{return pointer->getAttributeType(index);}

IRRLICHT_C_API const wchar_t* IAttributes_getAttributeTypeString1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeTypeString(attributeName);}
IRRLICHT_C_API const wchar_t* IAttributes_getAttributeTypeString2(IAttributes* pointer, s32 index)
{return pointer->getAttributeTypeString(index);}

IRRLICHT_C_API bool IAttributes_existsAttribute(IAttributes* pointer, const c8* attributeName)
{return pointer->existsAttribute(attributeName);}
IRRLICHT_C_API s32 IAttributes_findAttribute(IAttributes* pointer, const c8* attributeName)
{return pointer->findAttribute(attributeName);}
IRRLICHT_C_API void IAttributes_clear(IAttributes* pointer)
{pointer->clear();}
IRRLICHT_C_API bool IAttributes_read(IAttributes* pointer, io::IXMLReader* reader, bool readCurrentElementOnly=false, const wchar_t* elementName=0)
{return pointer->read(reader, readCurrentElementOnly, elementName);}
IRRLICHT_C_API bool IAttributes_write(IAttributes* pointer, io::IXMLWriter* writer, bool writeXMLHeader=false, const wchar_t* elementName=0)
{return pointer->write(writer, writeXMLHeader, elementName);}
IRRLICHT_C_API void IAttributes_addInt(IAttributes* pointer, const c8* attributeName, s32 value)
{pointer->addInt(attributeName, value);}

IRRLICHT_C_API void IAttributes_setAttribute1(IAttributes* pointer, const c8* attributeName, s32 value)
{pointer->setAttribute(attributeName, value);}
IRRLICHT_C_API void IAttributes_setAttribute2(IAttributes* pointer, s32 index, s32 value)
{pointer->setAttribute(index, value);}
IRRLICHT_C_API void IAttributes_setAttribute3(IAttributes* pointer, const c8* attributeName, f32 value)
{pointer->setAttribute(attributeName, value);}
IRRLICHT_C_API void IAttributes_setAttribute4(IAttributes* pointer, s32 index, f32 value)
{pointer->setAttribute(index, value);}
IRRLICHT_C_API void IAttributes_setAttribute5(IAttributes* pointer, const c8* attributeName, const c8* value)
{pointer->setAttribute(attributeName, value);}
IRRLICHT_C_API void IAttributes_setAttribute6(IAttributes* pointer, s32 index, const c8* value)
{pointer->setAttribute(index, value);}
IRRLICHT_C_API void IAttributes_setAttribute7(IAttributes* pointer, const c8* attributeName, const wchar_t* value)
{pointer->setAttribute(attributeName, value);}
IRRLICHT_C_API void IAttributes_setAttribute8(IAttributes* pointer, s32 index, const wchar_t* value)
{pointer->setAttribute(index, value);}
IRRLICHT_C_API void IAttributes_setAttribute9(IAttributes* pointer, const c8* attributeName, void* data, s32 dataSizeInBytes)
{pointer->setAttribute(attributeName, data, dataSizeInBytes);}
IRRLICHT_C_API void IAttributes_setAttribute10(IAttributes* pointer, s32 index, void* data, s32 dataSizeInBytes)
{pointer->setAttribute(index, data, dataSizeInBytes);}
IRRLICHT_C_API void IAttributes_setAttribute11(IAttributes* pointer, const c8* attributeName, const core::array<core::stringw>* value)
{pointer->setAttribute(attributeName, *value);}
IRRLICHT_C_API void IAttributes_setAttribute12(IAttributes* pointer, s32 index, const core::array<core::stringw>* value)
{pointer->setAttribute(index, *value);}
IRRLICHT_C_API void IAttributes_setAttribute13(IAttributes* pointer, const c8* attributeName, bool value)
{pointer->setAttribute(attributeName, value);}
IRRLICHT_C_API void IAttributes_setAttribute14(IAttributes* pointer, s32 index, bool value)
{pointer->setAttribute(index, value);}
IRRLICHT_C_API void IAttributes_setAttribute15(IAttributes* pointer, const c8* attributeName, const c8* enumValue, const c8* const* enumerationLiterals)
{pointer->setAttribute(attributeName, enumValue, enumerationLiterals);}
IRRLICHT_C_API void IAttributes_setAttribute16(IAttributes* pointer, s32 index, const c8* enumValue, const c8* const* enumerationLiterals)
{pointer->setAttribute(index, enumValue, enumerationLiterals);}
IRRLICHT_C_API void IAttributes_setAttribute17(IAttributes* pointer, const c8* attributeName, video::SColor color)
{pointer->setAttribute(attributeName, color);}
IRRLICHT_C_API void IAttributes_setAttribute18(IAttributes* pointer, s32 index, video::SColor color)
{pointer->setAttribute(index, color);}
IRRLICHT_C_API void IAttributes_setAttribute19(IAttributes* pointer, const c8* attributeName, video::SColorf color)
{pointer->setAttribute(attributeName, color);}
IRRLICHT_C_API void IAttributes_setAttribute20(IAttributes* pointer, s32 index, video::SColorf color)
{pointer->setAttribute(index, color);}
IRRLICHT_C_API void IAttributes_setAttribute21(IAttributes* pointer, const c8* attributeName, core::vector3df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute22(IAttributes* pointer, s32 index, core::vector3df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute23(IAttributes* pointer, const c8* attributeName, core::position2di v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute24(IAttributes* pointer, s32 index, core::position2di v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute25(IAttributes* pointer, const c8* attributeName, core::rect<s32> v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute26(IAttributes* pointer, s32 index, core::rect<s32> v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute27(IAttributes* pointer, const c8* attributeName, const core::matrix4& v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute28(IAttributes* pointer, s32 index, const core::matrix4& v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute29(IAttributes* pointer, const c8* attributeName, core::quaternion v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute30(IAttributes* pointer, s32 index, core::quaternion v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute31(IAttributes* pointer, const c8* attributeName, core::aabbox3df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute32(IAttributes* pointer, s32 index, core::aabbox3df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute33(IAttributes* pointer, const c8* attributeName, core::plane3df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute34(IAttributes* pointer, s32 index, core::plane3df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute35(IAttributes* pointer, const c8* attributeName, core::triangle3df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute36(IAttributes* pointer, s32 index, core::triangle3df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute37(IAttributes* pointer, const c8* attributeName, core::line2df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute38(IAttributes* pointer, s32 index, core::line2df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute39(IAttributes* pointer, const c8* attributeName, core::line3df v)
{pointer->setAttribute(attributeName, v);}
IRRLICHT_C_API void IAttributes_setAttribute40(IAttributes* pointer, s32 index, core::line3df v)
{pointer->setAttribute(index, v);}
IRRLICHT_C_API void IAttributes_setAttribute41(IAttributes* pointer, const c8* attributeName, video::ITexture* texture)
{pointer->setAttribute(attributeName, texture);}
IRRLICHT_C_API void IAttributes_setAttribute42(IAttributes* pointer, s32 index, video::ITexture* texture)
{pointer->setAttribute(index, texture);}
IRRLICHT_C_API void IAttributes_setAttribute43(IAttributes* pointer, const c8* attributeName, void* userPointer)
{pointer->setAttribute(attributeName, userPointer);}
IRRLICHT_C_API void IAttributes_setAttribute44(IAttributes* pointer, s32 index, void* userPointer)
{pointer->setAttribute(index, userPointer);}

IRRLICHT_C_API s32 IAttributes_getAttributeAsInt1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsInt(attributeName);}
IRRLICHT_C_API s32 IAttributes_getAttributeAsInt2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsInt(index);}
IRRLICHT_C_API void IAttributes_addFloat(IAttributes* pointer, const c8* attributeName, f32 value)
{pointer->addFloat(attributeName, value);}
IRRLICHT_C_API f32 IAttributes_getAttributeAsFloat1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsFloat(attributeName);}
IRRLICHT_C_API f32 IAttributes_getAttributeAsFloat2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsFloat(index);}

IRRLICHT_C_API void IAttributes_addString1(IAttributes* pointer, const c8* attributeName, const c8* value)
{pointer->addString(attributeName, value);}
IRRLICHT_C_API void IAttributes_addString2(IAttributes* pointer, const c8* attributeName, const wchar_t* value)
{pointer->addString(attributeName, value);}

IRRLICHT_C_API const c8* IAttributes_getAttributeAsString1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsString(attributeName).c_str();}
IRRLICHT_C_API const c8* IAttributes_getAttributeAsString2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsString(index).c_str();}
IRRLICHT_C_API void IAttributes_getAttributeAsString3(IAttributes* pointer, const c8* attributeName, c8* target)
{pointer->getAttributeAsString(attributeName, target);}

IRRLICHT_C_API const wchar_t* IAttributes_getAttributeAsStringW1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsStringW(attributeName).c_str();}
IRRLICHT_C_API const wchar_t* IAttributes_getAttributeAsStringW2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsStringW(index).c_str();}
IRRLICHT_C_API void IAttributes_getAttributeAsStringW3(IAttributes* pointer, const c8* attributeName, wchar_t* target)
{pointer->getAttributeAsStringW(attributeName, target);}

IRRLICHT_C_API void IAttributes_addBinary1(IAttributes* pointer, const c8* attributeName, void* data, s32 dataSizeInBytes)
{pointer->addBinary(attributeName, data, dataSizeInBytes);}
IRRLICHT_C_API void IAttributes_addArray2(IAttributes* pointer, const c8* attributeName, const core::array<core::stringw>& value)
{pointer->addArray(attributeName, value);}

IRRLICHT_C_API void IAttributes_getAttributeAsBinaryData1(IAttributes* pointer, const c8* attributeName, void* outData, s32 maxSizeInBytes)
{pointer->getAttributeAsBinaryData(attributeName, outData, maxSizeInBytes);}
IRRLICHT_C_API void IAttributes_getAttributeAsBinaryData2(IAttributes* pointer, s32 index, void* outData, s32 maxSizeInBytes)
{pointer->getAttributeAsBinaryData(index, outData, maxSizeInBytes);}

IRRLICHT_C_API core::array<core::stringw>* IAttributes_getAttributeAsArray1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsArray(attributeName);}
IRRLICHT_C_API core::array<core::stringw>* IAttributes_getAttributeAsArray2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsArray(index);}

IRRLICHT_C_API void IAttributes_addBool(IAttributes* pointer, const c8* attributeName, bool value)
{pointer->addBool(attributeName, value);}

IRRLICHT_C_API bool IAttributes_getAttributeAsBool1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsBool(attributeName);}
IRRLICHT_C_API bool IAttributes_getAttributeAsBool2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsBool(index);}

IRRLICHT_C_API void IAttributes_addEnum1(IAttributes* pointer, const c8* attributeName, const c8* enumValue, const c8* const* enumerationLiterals)
{pointer->addEnum(attributeName, enumValue, enumerationLiterals);}
IRRLICHT_C_API void IAttributes_addEnum2(IAttributes* pointer, const c8* attributeName, s32 enumValue, const c8* const* enumerationLiterals)
{pointer->addEnum(attributeName, enumValue, enumerationLiterals);}

IRRLICHT_C_API const c8* IAttributes_getAttributeAsEnumeration1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsEnumeration(attributeName);}
IRRLICHT_C_API const c8* IAttributes_getAttributeAsEnumeration2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsEnumeration(index);}
IRRLICHT_C_API s32 IAttributes_getAttributeAsEnumeration3(IAttributes* pointer, s32 index, const c8* const* enumerationLiteralsToUse)
{return pointer->getAttributeAsEnumeration(index, enumerationLiteralsToUse);}
IRRLICHT_C_API s32 IAttributes_getAttributeAsEnumeration4(IAttributes* pointer, const c8* attributeName, const c8* const* enumerationLiteralsToUse)
{return pointer->getAttributeAsEnumeration(attributeName, enumerationLiteralsToUse);}

IRRLICHT_C_API void IAttributes_getAttributeEnumerationLiteralsOfEnumeration1(IAttributes* pointer, const c8* attributeName, core::array<core::stringc>& outLiterals)
{pointer->getAttributeEnumerationLiteralsOfEnumeration(attributeName, outLiterals);}
IRRLICHT_C_API void IAttributes_getAttributeEnumerationLiteralsOfEnumeration2(IAttributes* pointer, s32 index, core::array<core::stringc>& outLiterals)
{pointer->getAttributeEnumerationLiteralsOfEnumeration(index, outLiterals);}

IRRLICHT_C_API void IAttributes_addColor(IAttributes* pointer, const c8* attributeName, video::SColor value)
{pointer->addColor(attributeName, value);}

IRRLICHT_C_API video::SColor* IAttributes_getAttributeAsColor1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsColor(attributeName);}
IRRLICHT_C_API video::SColor* IAttributes_getAttributeAsColor2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsColor(index);}

IRRLICHT_C_API void IAttributes_addColorf(IAttributes* pointer, const c8* attributeName, video::SColorf value)
{pointer->addColorf(attributeName, value);}

IRRLICHT_C_API video::SColorf* IAttributes_getAttributeAsColorf1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsColorf(attributeName);}
IRRLICHT_C_API video::SColorf* IAttributes_getAttributeAsColorf2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsColorf(index);}

IRRLICHT_C_API void IAttributes_addVector3d(IAttributes* pointer, const c8* attributeName, core::vector3df value)
{pointer->addVector3d(attributeName, value);}

IRRLICHT_C_API core::vector3df* IAttributes_getAttributeAsVector3d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsVector3d(attributeName);}
IRRLICHT_C_API core::vector3df* IAttributes_getAttributeAsVector3d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsVector3d(index);}

IRRLICHT_C_API void IAttributes_addPosition2d(IAttributes* pointer, const c8* attributeName, core::position2di value)
{pointer->addPosition2d(attributeName, value);}

IRRLICHT_C_API core::position2di* IAttributes_getAttributeAsPosition2d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsPosition2d(attributeName);}
IRRLICHT_C_API core::position2di* IAttributes_getAttributeAsPosition2d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsPosition2d(index);}

IRRLICHT_C_API void IAttributes_addRect(IAttributes* pointer, const c8* attributeName, core::rect<s32> value)
{pointer->addRect(attributeName, value);}

IRRLICHT_C_API core::rect<s32>* IAttributes_getAttributeAsRect1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsRect(attributeName);}
IRRLICHT_C_API core::rect<s32>* IAttributes_getAttributeAsRect2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsRect(index);}


IRRLICHT_C_API void IAttributes_addMatrix(IAttributes* pointer, const c8* attributeName, const core::matrix4& v)
{pointer->addMatrix(attributeName, v);}

IRRLICHT_C_API core::matrix4* IAttributes_getAttributeAsMatrix1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsMatrix(attributeName);}
IRRLICHT_C_API core::matrix4* IAttributes_getAttributeAsMatrix2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsMatrix(index);}

IRRLICHT_C_API void IAttributes_addQuaternion(IAttributes* pointer, const c8* attributeName, core::quaternion v)
{pointer->addQuaternion(attributeName, v);}

IRRLICHT_C_API core::quaternion* IAttributes_getAttributeAsQuaternion1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsQuaternion(attributeName);}
IRRLICHT_C_API core::quaternion* IAttributes_getAttributeAsQuaternion2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsQuaternion(index);}

IRRLICHT_C_API void IAttributes_addBox3d(IAttributes* pointer, const c8* attributeName, core::aabbox3df v)
{pointer->addBox3d(attributeName, v);}

IRRLICHT_C_API core::aabbox3df* IAttributes_getAttributeAsBox3d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsBox3d(attributeName);}
IRRLICHT_C_API core::aabbox3df* IAttributes_getAttributeAsBox3d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsBox3d(index);}

IRRLICHT_C_API void IAttributes_addPlane3d(IAttributes* pointer, const c8* attributeName, core::plane3df v)
{pointer->addPlane3d(attributeName, v);}

IRRLICHT_C_API core::plane3df* IAttributes_getAttributeAsPlane3d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsPlane3d(attributeName);}
IRRLICHT_C_API core::plane3df* IAttributes_getAttributeAsPlane3d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsPlane3d(index);}

IRRLICHT_C_API void IAttributes_addTriangle3d(IAttributes* pointer, const c8* attributeName, core::triangle3df v)
{pointer->addTriangle3d(attributeName, v);}

IRRLICHT_C_API core::triangle3df* IAttributes_getAttributeAsTriangle3d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsTriangle3d(attributeName);}
IRRLICHT_C_API core::triangle3df* IAttributes_getAttributeAsTriangle3d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsTriangle3d(index);}

IRRLICHT_C_API void IAttributes_addLine2d(IAttributes* pointer, const c8* attributeName, core::line2df v)
{pointer->addLine2d(attributeName, v);}

IRRLICHT_C_API core::line2df* IAttributes_getAttributeAsLine2d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsLine2d(attributeName);}
IRRLICHT_C_API core::line2df* IAttributes_getAttributeAsLine2d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsLine2d(index);}

IRRLICHT_C_API void IAttributes_addLine3d(IAttributes* pointer, const c8* attributeName, core::line3df v)
{pointer->addLine3d(attributeName, v);}

IRRLICHT_C_API core::line3df* IAttributes_getAttributeAsLine3d1(IAttributes* pointer, const c8* attributeName)
{return &pointer->getAttributeAsLine3d(attributeName);}
IRRLICHT_C_API core::line3df* IAttributes_getAttributeAsLine3d2(IAttributes* pointer, s32 index)
{return &pointer->getAttributeAsLine3d(index);}

IRRLICHT_C_API void IAttributes_addTexture(IAttributes* pointer, const c8* attributeName, video::ITexture* texture)
{pointer->addTexture(attributeName, texture);}

IRRLICHT_C_API video::ITexture* IAttributes_getAttributeAsTexture1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsTexture(attributeName);}
IRRLICHT_C_API video::ITexture* IAttributes_getAttributeAsTexture2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsTexture(index);}

IRRLICHT_C_API void IAttributes_addUserPointer(IAttributes* pointer, const c8* attributeName, void* userPointer)
{pointer->addUserPointer(attributeName, userPointer);}

IRRLICHT_C_API void* IAttributes_getAttributeAsUserPointer1(IAttributes* pointer, const c8* attributeName)
{return pointer->getAttributeAsUserPointer(attributeName);}
IRRLICHT_C_API void* IAttributes_getAttributeAsUserPointer2(IAttributes* pointer, s32 index)
{return pointer->getAttributeAsUserPointer(index);}

#ifdef __cplusplus
}
#endif

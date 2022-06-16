// Copyright(c) Max Kolosov 2010-2022 pyirrlicht@gmail.com
// github.com/usermicrodevices
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SKeyMap
// extended methods for SKeyMap
IRRLICHT_C_API SKeyMap* SKeyMap_ctor(int length = 1)
{return new SKeyMap[length];}
IRRLICHT_C_API void SKeyMap_delete(SKeyMap* pointer){if(pointer)delete[] pointer;}
IRRLICHT_C_API void SKeyMap_set(SKeyMap* pointer, int index, EKEY_ACTION action, EKEY_CODE key_code)
{pointer[index].Action = action; pointer[index].KeyCode = key_code;}

#ifdef __cplusplus
}
#endif

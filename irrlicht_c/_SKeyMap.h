// Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SKeyMap
// extended methods for SKeyMap
IRRLICHT_C_API SKeyMap* SKeyMap_ctor(int length = 1)
{SKeyMap* pointer; pointer = new SKeyMap[length]; return pointer;}
//IRRLICHT_C_API void SKeyMap_Destructor(SKeyMap* pointer){delete pointer;}
IRRLICHT_C_API void SKeyMap_set(SKeyMap* pointer, int index, EKEY_ACTION action, EKEY_CODE key_code)
{pointer[index].Action = action; pointer[index].KeyCode = key_code;}

#ifdef __cplusplus
}
#endif

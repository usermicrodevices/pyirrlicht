// Copyright(c) Max Kolosov 2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

// SParticle
IRRLICHT_C_API SParticle* SParticle_ctor(int length = 1)
{SParticle* result; result = new SParticle[length]; return result;}

IRRLICHT_C_API SParticle* SParticle_get_item(SParticle* pointer, int index = 0)
{return &pointer[index];}
IRRLICHT_C_API void SParticle_set_item(SParticle* pointer, SParticle* value, int index = 0)
{pointer[index] = *value;}

IRRLICHT_C_API core::vector3df* SParticle_get_pos(SParticle* pointer, int index = 0)
{return &pointer[index].pos;}
IRRLICHT_C_API void SParticle_set_pos(SParticle* pointer, core::vector3df* value, int index = 0)
{pointer[index].pos = *value;}

IRRLICHT_C_API core::vector3df* SParticle_get_vector(SParticle* pointer, int index = 0)
{return &pointer[index].vector;}
IRRLICHT_C_API void SParticle_set_vector(SParticle* pointer, core::vector3df* value, int index = 0)
{pointer[index].vector = *value;}

IRRLICHT_C_API u32 SParticle_get_startTime(SParticle* pointer, int index = 0)
{return pointer[index].startTime;}
IRRLICHT_C_API void SParticle_set_startTime(SParticle* pointer, u32 value, int index = 0)
{pointer[index].startTime = value;}

IRRLICHT_C_API u32 SParticle_get_endTime(SParticle* pointer, int index = 0)
{return pointer[index].endTime;}
IRRLICHT_C_API void SParticle_set_endTime(SParticle* pointer, u32 value, int index = 0)
{pointer[index].endTime = value;}

IRRLICHT_C_API video::SColor* SParticle_get_color(SParticle* pointer, int index = 0)
{return &pointer[index].color;}
IRRLICHT_C_API void SParticle_set_color(SParticle* pointer, video::SColor* value, int index = 0)
{pointer[index].color = *value;}

IRRLICHT_C_API video::SColor* SParticle_get_startColor(SParticle* pointer, int index = 0)
{return &pointer[index].startColor;}
IRRLICHT_C_API void SParticle_set_startColor(SParticle* pointer, video::SColor* value, int index = 0)
{pointer[index].startColor = *value;}

IRRLICHT_C_API core::vector3df* SParticle_get_startVector(SParticle* pointer, int index = 0)
{return &pointer[index].startVector;}
IRRLICHT_C_API void SParticle_set_startVector(SParticle* pointer, core::vector3df* value, int index = 0)
{pointer[index].startVector = *value;}

IRRLICHT_C_API core::dimension2df* SParticle_get_size(SParticle* pointer, int index = 0)
{return &pointer[index].size;}
IRRLICHT_C_API void SParticle_set_size(SParticle* pointer, core::dimension2df* value, int index = 0)
{pointer[index].size = *value;}

IRRLICHT_C_API core::dimension2df* SParticle_get_startSize(SParticle* pointer, int index = 0)
{return &pointer[index].startSize;}
IRRLICHT_C_API void SParticle_set_startSize(SParticle* pointer, core::dimension2df* value, int index = 0)
{pointer[index].startSize = *value;}

#ifdef __cplusplus
}
#endif

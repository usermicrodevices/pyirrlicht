// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= SColor
IRRLICHT_C_API SColor* SColor_ctor1(){return new SColor();}
IRRLICHT_C_API SColor* SColor_ctor2(u32 a, u32 r, u32 g, u32 b){return new SColor(a, r, g, b);}
IRRLICHT_C_API SColor* SColor_ctor3(u32 clr){return new SColor(clr);}
IRRLICHT_C_API u32 SColor_getAlpha(SColor* pointer){return pointer->getAlpha();}
IRRLICHT_C_API u32 SColor_getRed(SColor* pointer){return pointer->getRed();}
IRRLICHT_C_API u32 SColor_getGreen(SColor* pointer){return pointer->getGreen();}
IRRLICHT_C_API u32 SColor_getBlue(SColor* pointer){return pointer->getBlue();}
IRRLICHT_C_API f32 SColor_getLuminance(SColor* pointer){return pointer->getLuminance();}
IRRLICHT_C_API u32 SColor_getAverage(SColor* pointer){return pointer->getAverage();}
IRRLICHT_C_API void SColor_setAlpha(SColor* pointer, u32 a){pointer->setAlpha(a);}
IRRLICHT_C_API void SColor_setRed(SColor* pointer, u32 r){pointer->setRed(r);}
IRRLICHT_C_API void SColor_setGreen(SColor* pointer, u32 g){pointer->setGreen(g);}
IRRLICHT_C_API void SColor_setBlue(SColor* pointer, u32 b){pointer->setBlue(b);}
IRRLICHT_C_API u16 SColor_toA1R5G5B5(SColor* pointer){return pointer->toA1R5G5B5();}
IRRLICHT_C_API void SColor_toOpenGLColor(SColor* pointer, u8* dest){pointer->toOpenGLColor(dest);}
IRRLICHT_C_API void SColor_set(SColor* pointer, u32 a, u32 r, u32 g, u32 b){pointer->set(a, r, g, b);}
IRRLICHT_C_API void SColor_set2(SColor* pointer, u32 col){pointer->set(col);}
IRRLICHT_C_API bool SColor_operator_equal(SColor* pointer, const SColor& other){return pointer->operator==(other);}
IRRLICHT_C_API bool SColor_operator_notequal(SColor* pointer, const SColor& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool SColor_operator_less(SColor* pointer, const SColor& other){return pointer->operator<(other);}
IRRLICHT_C_API SColor* SColor_operator_add(SColor* pointer, const SColor& other){return &pointer->operator+(other);}
IRRLICHT_C_API SColor* SColor_getInterpolated(SColor* pointer, const SColor& other, f32 d)
{return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API SColor* SColor_getInterpolated_quadratic(SColor* pointer, const SColor& c1, const SColor& c2, f32 d)
{return &pointer->getInterpolated_quadratic(c1, c2, d);}
IRRLICHT_C_API u32 SColor_color(SColor* pointer){return pointer->color;}

//================= SColorf
IRRLICHT_C_API SColorf* SColorf_ctor1(){return new SColorf();}
IRRLICHT_C_API SColorf* SColorf_ctor2(f32 r, f32 g, f32 b, f32 a = 1.0f){return new SColorf(r, g, b, a);}
IRRLICHT_C_API SColorf* SColorf_ctor3(SColor& c){return new SColorf(*&c);}
IRRLICHT_C_API SColor* SColorf_toSColor(SColorf* pointer){return &pointer->toSColor();}
IRRLICHT_C_API void SColorf_set1(SColorf* pointer, f32 rr, f32 gg, f32 bb){pointer->set(rr, gg, bb);}
IRRLICHT_C_API void SColorf_set2(SColorf* pointer, f32 aa, f32 rr, f32 gg, f32 bb){pointer->set(aa, rr, gg, bb);}
IRRLICHT_C_API SColorf* SColorf_getInterpolated(SColorf* pointer, const SColorf& other, f32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API SColorf* SColorf_getInterpolated_quadratic(SColorf* pointer, const SColorf& c1, const SColorf& c2, f32 d){return &pointer->getInterpolated_quadratic(c1, c2, d);}
IRRLICHT_C_API void SColorf_setColorComponentValue(SColorf* pointer, s32 index, f32 value){pointer->setColorComponentValue(index, value);}
IRRLICHT_C_API f32 SColorf_getAlpha(SColorf* pointer){return pointer->getAlpha();}
IRRLICHT_C_API f32 SColorf_getRed(SColorf* pointer){return pointer->getRed();}
IRRLICHT_C_API f32 SColorf_getGreen(SColorf* pointer){return pointer->getGreen();}
IRRLICHT_C_API f32 SColorf_getBlue(SColorf* pointer){return pointer->getBlue();}
IRRLICHT_C_API void SColorf_setAlpha(SColorf* pointer, f32 value){pointer->a = value;}
IRRLICHT_C_API void SColorf_setRed(SColorf* pointer, f32 value){pointer->r = value;}
IRRLICHT_C_API void SColorf_setGreen(SColorf* pointer, f32 value){pointer->g = value;}
IRRLICHT_C_API void SColorf_setBlue(SColorf* pointer, f32 value){pointer->b = value;}

//================= SColorHSL
IRRLICHT_C_API SColorHSL* SColorHSL_ctor(f32 h = 0.f, f32 s = 0.f, f32 l = 0.f){return new SColorHSL(h, s, l);}
IRRLICHT_C_API void SColorHSL_fromRGB(SColorHSL* pointer, SColor* color){pointer->fromRGB(*color);}
IRRLICHT_C_API void SColorHSL_toRGB(SColorHSL* pointer, SColor* color){pointer->toRGB(*color);}
IRRLICHT_C_API f32 SColorHSL_get_Hue(SColorHSL* pointer){return pointer->Hue;}
IRRLICHT_C_API f32 SColorHSL_get_Saturation(SColorHSL* pointer){return pointer->Saturation;}
IRRLICHT_C_API f32 SColorHSL_get_Luminance(SColorHSL* pointer){return pointer->Luminance;}
IRRLICHT_C_API void SColorHSL_set_Hue(SColorHSL* pointer, f32 value){pointer->Hue = value;}
IRRLICHT_C_API void SColorHSL_set_Saturation(SColorHSL* pointer, f32 value){pointer->Saturation = value;}
IRRLICHT_C_API void SColorHSL_set_Luminance(SColorHSL* pointer, f32 value){pointer->Luminance = value;}

#ifdef __cplusplus
}
#endif

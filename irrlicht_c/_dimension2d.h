// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= dimension2df
IRRLICHT_C_API dimension2df* dimension2df_ctor1(){return new dimension2df();}
IRRLICHT_C_API dimension2df* dimension2df_ctor2(f32 w=0.0f, f32 h=0.0f){return new dimension2df(w, h);}
IRRLICHT_C_API dimension2df* dimension2df_ctor3(const dimension2df& other){return new dimension2df(other);}
IRRLICHT_C_API dimension2df* dimension2df_ctor4(const vector2df& other){return new dimension2df(other);}

IRRLICHT_C_API dimension2df* dimension2df_operator_set_other(dimension2df* pointer, const dimension2df& other){return &pointer->operator=(other);}
IRRLICHT_C_API bool dimension2df_operator_eq_other(dimension2df* pointer, const dimension2df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2df_operator_ne_other(dimension2df* pointer, const dimension2df& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool dimension2df_operator_eq_vector2d(dimension2df* pointer, const vector2df& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2df_operator_ne_vector2d(dimension2df* pointer, const vector2df& other){return pointer->operator!=(other);}
IRRLICHT_C_API dimension2df* dimension2df_set(dimension2df* pointer, const f32 width, const f32 height){return &pointer->set(width, height);}
IRRLICHT_C_API dimension2df* dimension2df_operator_set_div_value(dimension2df* pointer, const f32 scale){return &pointer->operator/=(scale);}
IRRLICHT_C_API dimension2df* dimension2df_operator_div_value(dimension2df* pointer, const f32 scale){return &pointer->operator/(scale);}
IRRLICHT_C_API dimension2df* dimension2df_operator_set_mult_value(dimension2df* pointer, const f32 scale){return &pointer->operator*=(scale);}
IRRLICHT_C_API dimension2df* dimension2df_operator_mult_value(dimension2df* pointer, const f32 scale){return &pointer->operator*(scale);}
IRRLICHT_C_API dimension2df* dimension2df_operator_set_add_other(dimension2df* pointer, const dimension2df& other){return &pointer->operator+=(other);}
IRRLICHT_C_API dimension2df* dimension2df_operator_set_sub_other(dimension2df* pointer, const dimension2df& other){return &pointer->operator-=(other);}
IRRLICHT_C_API dimension2df* dimension2df_operator_add_other(dimension2df* pointer, const dimension2df& other){return &pointer->operator+(other);}
IRRLICHT_C_API f32 dimension2df_getArea(dimension2df& pointer){return pointer.getArea();}
IRRLICHT_C_API dimension2df* dimension2df_getOptimalSize(dimension2df* pointer, bool requirePowerOfTwo=true, bool requireSquare=false, bool larger=true, f32 maxValue = 0){return &pointer->getOptimalSize(requirePowerOfTwo, requireSquare, larger, (u32)maxValue);}
IRRLICHT_C_API dimension2df* dimension2df_getInterpolated(dimension2df* pointer, const dimension2df& other, f32 d){return &pointer->getInterpolated(other, d);}
IRRLICHT_C_API f32 dimension2df_get_Width(dimension2df* pointer){return pointer->Width;}
IRRLICHT_C_API void dimension2df_set_Width(dimension2df* pointer, f32 value){pointer->Width = value;}
IRRLICHT_C_API f32 dimension2df_get_Height(dimension2df* pointer){return pointer->Height;}
IRRLICHT_C_API void dimension2df_set_Height(dimension2df* pointer, f32 value){pointer->Height = value;}

//================= dimension2du
IRRLICHT_C_API dimension2du* dimension2du_ctor1(){return new dimension2du();}
IRRLICHT_C_API dimension2du* dimension2du_ctor2(u32 w=0, u32 h=0){return new dimension2du(w, h);}
IRRLICHT_C_API dimension2du* dimension2du_ctor3(const dimension2du& other){return new dimension2du(other);}
IRRLICHT_C_API dimension2du* dimension2du_ctor4(const vector2d<u32>& other){return new dimension2du(other);}

IRRLICHT_C_API dimension2du* dimension2du_operator_set_other(dimension2du* pointer, const dimension2du& other){return &pointer->operator=(other);}
IRRLICHT_C_API bool dimension2du_operator_eq_other(dimension2du* pointer, const dimension2du& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2du_operator_ne_other(dimension2du* pointer, const dimension2du& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool dimension2du_operator_eq_vector2d(dimension2du* pointer, const vector2d<u32>& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2du_operator_ne_vector2d(dimension2du* pointer, const vector2d<u32>& other){return pointer->operator!=(other);}
IRRLICHT_C_API dimension2du* dimension2du_set(dimension2du* pointer, const u32 width, const u32 height){return &pointer->set(width, height);}
IRRLICHT_C_API dimension2du* dimension2du_operator_set_div_value(dimension2du* pointer, const u32 scale){return &pointer->operator/=(scale);}
IRRLICHT_C_API dimension2du* dimension2du_operator_div_value(dimension2du* pointer, const u32 scale){return &pointer->operator/(scale);}
IRRLICHT_C_API dimension2du* dimension2du_operator_set_mult_value(dimension2du* pointer, const u32 scale){return &pointer->operator*=(scale);}
IRRLICHT_C_API dimension2du* dimension2du_operator_mult_value(dimension2du* pointer, const u32 scale){return &pointer->operator*(scale);}
IRRLICHT_C_API dimension2du* dimension2du_operator_set_add_other(dimension2du* pointer, const dimension2du& other){return &pointer->operator+=(other);}
IRRLICHT_C_API dimension2du* dimension2du_operator_set_sub_other(dimension2du* pointer, const dimension2du& other){return &pointer->operator-=(other);}
IRRLICHT_C_API dimension2du* dimension2du_operator_add_other(dimension2du* pointer, const dimension2du& other){return &pointer->operator+(other);}
IRRLICHT_C_API u32 dimension2du_getArea(dimension2du& pointer){return pointer.getArea();}
IRRLICHT_C_API dimension2du* dimension2du_getOptimalSize(dimension2du* pointer, bool requirePowerOfTwo=true, bool requireSquare=false, bool larger=true, u32 maxValue = 0){return &pointer->getOptimalSize(requirePowerOfTwo, requireSquare, larger, maxValue);}
IRRLICHT_C_API dimension2du* dimension2du_getInterpolated(dimension2du* pointer, const dimension2du& other, u32 d){return &pointer->getInterpolated(other, (f32)d);}
IRRLICHT_C_API u32 dimension2du_get_Width(dimension2du* pointer){return pointer->Width;}
IRRLICHT_C_API void dimension2du_set_Width(dimension2du* pointer, u32 value){pointer->Width = value;}
IRRLICHT_C_API u32 dimension2du_get_Height(dimension2du* pointer){return pointer->Height;}
IRRLICHT_C_API void dimension2du_set_Height(dimension2du* pointer, u32 value){pointer->Height = value;}

//================= dimension2di
IRRLICHT_C_API dimension2di* dimension2di_ctor1(){return new dimension2di();}
IRRLICHT_C_API dimension2di* dimension2di_ctor2(s32 w=0, s32 h=0){return new dimension2di(w, h);}
IRRLICHT_C_API dimension2di* dimension2di_ctor3(const dimension2di& other){return new dimension2di(other);}
IRRLICHT_C_API dimension2di* dimension2di_ctor4(const vector2di& other){return new dimension2di(other);}

IRRLICHT_C_API dimension2di* dimension2di_operator_set_other(dimension2di* pointer, const dimension2di& other){return &pointer->operator=(other);}
IRRLICHT_C_API bool dimension2di_operator_eq_other(dimension2di* pointer, const dimension2di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2di_operator_ne_other(dimension2di* pointer, const dimension2di& other){return pointer->operator!=(other);}
IRRLICHT_C_API bool dimension2di_operator_eq_vector2d(dimension2di* pointer, const vector2di& other){return pointer->operator==(other);}
IRRLICHT_C_API bool dimension2di_operator_ne_vector2d(dimension2di* pointer, const vector2di& other){return pointer->operator!=(other);}
IRRLICHT_C_API dimension2di* dimension2di_set(dimension2di* pointer, const s32 width, const s32 height){return &pointer->set(width, height);}
IRRLICHT_C_API dimension2di* dimension2di_operator_set_div_value(dimension2di* pointer, const s32 scale){return &pointer->operator/=(scale);}
IRRLICHT_C_API dimension2di* dimension2di_operator_div_value(dimension2di* pointer, const s32 scale){return &pointer->operator/(scale);}
IRRLICHT_C_API dimension2di* dimension2di_operator_set_mult_value(dimension2di* pointer, const s32 scale){return &pointer->operator*=(scale);}
IRRLICHT_C_API dimension2di* dimension2di_operator_mult_value(dimension2di* pointer, const s32 scale){return &pointer->operator*(scale);}
IRRLICHT_C_API dimension2di* dimension2di_operator_set_add_other(dimension2di* pointer, const dimension2di& other){return &pointer->operator+=(other);}
IRRLICHT_C_API dimension2di* dimension2di_operator_set_sub_other(dimension2di* pointer, const dimension2di& other){return &pointer->operator-=(other);}
IRRLICHT_C_API dimension2di* dimension2di_operator_add_other(dimension2di* pointer, const dimension2di& other){return &pointer->operator+(other);}
IRRLICHT_C_API s32 dimension2di_getArea(dimension2di* pointer){return pointer->getArea();}
IRRLICHT_C_API dimension2di* dimension2di_getOptimalSize(dimension2di* pointer, bool requirePowerOfTwo=true, bool requireSquare=false, bool larger=true, s32 maxValue = 0){return &pointer->getOptimalSize(requirePowerOfTwo, requireSquare, larger, maxValue);}
IRRLICHT_C_API dimension2di* dimension2di_getInterpolated(dimension2di* pointer, const dimension2di& other, s32 d){return &pointer->getInterpolated(other, (f32)d);}
IRRLICHT_C_API s32 dimension2di_get_Width(dimension2di* pointer){return pointer->Width;}
IRRLICHT_C_API void dimension2di_set_Width(dimension2di* pointer, s32 value){pointer->Width = value;}
IRRLICHT_C_API s32 dimension2di_get_Height(dimension2di* pointer){return pointer->Height;}
IRRLICHT_C_API void dimension2di_set_Height(dimension2di* pointer, s32 value){pointer->Height = value;}

#ifdef __cplusplus
}
#endif

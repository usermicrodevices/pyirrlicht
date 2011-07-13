// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//================= IGUIInOutFader
IRRLICHT_C_API IGUIInOutFader* IGUIInOutFader_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIInOutFader*)new IGUIElement(EGUIET_IN_OUT_FADER, environment, parent, id, *rectangle);}
IRRLICHT_C_API video::SColor* IGUIInOutFader_getColor(IGUIInOutFader* pointer)
{return new video::SColor(pointer->getColor());}
IRRLICHT_C_API void IGUIInOutFader_setColor1(IGUIInOutFader* pointer, const video::SColor& color)
{pointer->setColor(color);}
IRRLICHT_C_API void IGUIInOutFader_setColor2(IGUIInOutFader* pointer, const video::SColor& source, const video::SColor& dest)
{pointer->setColor(source, dest);}
IRRLICHT_C_API void IGUIInOutFader_fadeIn(IGUIInOutFader* pointer, u32 time)
{pointer->fadeIn(time);}
IRRLICHT_C_API void IGUIInOutFader_fadeOut(IGUIInOutFader* pointer, u32 time)
{pointer->fadeOut(time);}
IRRLICHT_C_API bool IGUIInOutFader_isReady(IGUIInOutFader* pointer)
{return pointer->isReady();}

#ifdef __cplusplus
}
#endif

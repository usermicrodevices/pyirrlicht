// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

IRRLICHT_C_API IGUIButton* IGUIButton_ctor(IGUIEnvironment* environment, IGUIElement* parent, s32 id, core::rect<s32>* rectangle)
{return (IGUIButton*)new IGUIElement(EGUIET_BUTTON, environment, parent, id, *rectangle);}
IRRLICHT_C_API void IGUIButton_setOverrideFont(IGUIButton* pointer, IGUIFont* font=0){pointer->setOverrideFont(font);}
IRRLICHT_C_API void IGUIButton_setImage1(IGUIButton* pointer, video::ITexture* image=0){pointer->setImage(image);}
IRRLICHT_C_API void IGUIButton_setImage2(IGUIButton* pointer, video::ITexture* image, const core::rect<s32>& pos){pointer->setImage(image, pos);}
IRRLICHT_C_API void IGUIButton_setPressedImage1(IGUIButton* pointer, video::ITexture* image=0){pointer->setPressedImage(image);}
IRRLICHT_C_API void IGUIButton_setPressedImage2(IGUIButton* pointer, video::ITexture* image, const core::rect<s32>& pos){pointer->setPressedImage(image, pos);}
IRRLICHT_C_API void IGUIButton_setSpriteBank(IGUIButton* pointer, IGUISpriteBank* bank=0){pointer->setSpriteBank(bank);}
IRRLICHT_C_API void IGUIButton_setSprite(IGUIButton* pointer, EGUI_BUTTON_STATE state, s32 index, const video::SColor& color=video::SColor(255,255,255,255), bool loop=false){pointer->setSprite(state, index, color, loop);}
IRRLICHT_C_API void IGUIButton_setIsPushButton(IGUIButton* pointer, bool isPushButton=true){pointer->setIsPushButton(isPushButton);}
IRRLICHT_C_API void IGUIButton_setPressed(IGUIButton* pointer, bool pressed=true){pointer->setPressed(pressed);}
IRRLICHT_C_API bool IGUIButton_isPressed(IGUIButton* pointer){return pointer->isPressed();}
IRRLICHT_C_API void IGUIButton_setUseAlphaChannel(IGUIButton* pointer, bool useAlphaChannel=true){pointer->setUseAlphaChannel(useAlphaChannel);}
IRRLICHT_C_API bool IGUIButton_isAlphaChannelUsed(IGUIButton* pointer){return pointer->isAlphaChannelUsed();}
IRRLICHT_C_API bool IGUIButton_isPushButton(IGUIButton* pointer){return pointer->isPushButton();}
IRRLICHT_C_API void IGUIButton_setDrawBorder(IGUIButton* pointer, bool border=true){pointer->setDrawBorder(border);}
IRRLICHT_C_API bool IGUIButton_isDrawingBorder(IGUIButton* pointer){return pointer->isDrawingBorder();}
IRRLICHT_C_API void IGUIButton_setScaleImage(IGUIButton* pointer, bool scaleImage=true){pointer->setScaleImage(scaleImage);}
IRRLICHT_C_API bool IGUIButton_isScalingImage(IGUIButton* pointer){return pointer->isScalingImage();}

#ifdef __cplusplus
}
#endif

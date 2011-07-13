// Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
// http://vosolok2008.narod.ru
// BSD license

#ifdef __cplusplus
extern "C" {
#endif

//IRRLICHT_C_API IMetaTriangleSelector* IMetaTriangleSelector_ctor(){return new IMetaTriangleSelector();}
IRRLICHT_C_API void IMetaTriangleSelector_addTriangleSelector(IMetaTriangleSelector* pointer, ITriangleSelector* toAdd){pointer->addTriangleSelector(toAdd);}
IRRLICHT_C_API bool IMetaTriangleSelector_removeTriangleSelector(IMetaTriangleSelector* pointer, ITriangleSelector* toRemove){return pointer->removeTriangleSelector(toRemove);}
IRRLICHT_C_API void IMetaTriangleSelector_removeAllTriangleSelectors(IMetaTriangleSelector* pointer){pointer->removeAllTriangleSelectors();}

#ifdef __cplusplus
}
#endif

#! /bin/sh

gcc -shared -w -fPIC -D_IRR_STATIC_LIB_ -I../../agg-2.5/include -I../../agg-2.5/examples -I/usr/include/freetype2 -I../../irrxml-1.2/src -I../../irrlicht/include -L../../irrlicht/lib/Linux/irrlicht.a irrlicht_c.cpp -o ../irrlicht_c.so

cd ..

ldd -v irrlicht_c.so

nm -u irrlicht_c.so > exports.txt

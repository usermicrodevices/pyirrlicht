#! /bin/sh

#x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -D_IRR_STATIC_LIB_ -UWall -Iirrlicht_c -I../agg-2.5/include -I../agg-2.5/examples -I/usr/include/freetype2 -I../irrxml-1.2/src -I../irrlicht/include -I/usr/include/python3.9 -c irrlicht_c/irrlicht_c.cpp -o build/temp.linux-x86_64-3.9/irrlicht_c/irrlicht_c.o

#x86_64-linux-gnu-g++ -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.9/irrlicht_c/irrlicht_c.o -L../irrlicht/lib/Linux -o build/lib.linux-x86_64-3.9/irrlicht_c.cpython-39-x86_64-linux-gnu.so

gcc -w -l -shared -fPIC -D_IRR_STATIC_LIB_ -I../../agg-2.5/include -I../../agg-2.5/examples -I/usr/include/freetype2 -I../../irrxml-1.2/src -I../../irrlicht/include -L../../irrlicht/lib/Linux/irrlicht.a irrlicht_c.cpp -o ../irrlicht_c.so

ldd -v irrlicht_c.so

nm -u irrlicht_c.so > exports.txt

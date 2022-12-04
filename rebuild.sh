rm -rf build
python3 setup.py build_ext --debug
mv build/lib.linux-x86_64-*/irrlicht_c.cpython-*-x86_64-linux-gnu.so irrlicht_c.so
python3 pyirrlicht.py

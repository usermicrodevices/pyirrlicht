rm -rf build
python3 setup.py build_ext
mv build/lib.linux-x86_64-3.10/irrlicht_c.cpython-310-x86_64-linux-gnu.so irrlicht_c.so
python3 pyirrlicht.py

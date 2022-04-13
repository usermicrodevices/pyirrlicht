from setuptools import setup, Extension

setup(
	name='pyirrlicht',
	version='1.2.0',
	ext_modules=[Extension('irrlicht_c', sources=['irrlicht_c/irrlicht_c.cpp'], include_dirs=['irrlicht_c', '../agg-2.5/include', '../agg-2.5/examples', '/usr/include/freetype2', '../irrxml-1.2/src', '../irrlicht/include'], define_macros=[('_IRR_STATIC_LIB_', None)], undef_macros=['Wall'], library_dirs=['../irrlicht/lib/Linux'], extra_compile_args=['-target=x86_64'])]
)

from setuptools import setup, Extension

setup(
	name='pyirrlicht',
	version='1.3.0',
	ext_modules=[
		Extension(
			'irrlicht_c',
			sources=['irrlicht_c/irrlicht_c.cpp'],
			include_dirs=[
				'irrlicht_c',
				'../agg-2.5/include',
				'../agg-2.5/examples',
				'/usr/include/freetype2',
				'../irrxml-1.2/src',
				'../irrlicht/include'
			],
			define_macros=[
				('_IRR_STATIC_LIB_', None),
				('_COMPILE_WITH_2DTTFONT_', None),
				('_COMPILE_WITH_3D_TEXT_', None),
				('_COMPILE_WITH_GRID_SCENE_NODE_', None),
				('_COMPILE_WITH_GUI_FILE_SELECTOR_', None)
				#('_COMPILE_WITH_AGG_', None),
				#('_COMPILE_WITH_IRR_SVG_AGG_', None),
				#('_COMPILE_WITH_IRR_SVG_CAIRO_', None),
				#('_COMPILE_WITH_CHAR_CONVERSION_FUNCTIONS_', None),
				#('_COMPILE_WITH_STREAM_FUNCTIONS_', None)
			],
			undef_macros=['Wall', '_COMPILE_WITH_3D_TEXT_'],
			library_dirs=['../irrlicht/lib/Linux'],
			libraries=['Irrlicht', 'GL', 'X11', 'Xxf86vm', 'Xext', 'freetype']
		)
	]
)

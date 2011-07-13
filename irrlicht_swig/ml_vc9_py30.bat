@SETLOCAL

@SET i_ver=irrlicht-1.7.1
@SET freetype_ver=2.3.12
@SET ft_ver=2312

@SET py_ver=Python-3.0.1
@SET py_suffix=30

@SET py_lib=python%py_suffix%
@SET lib_name=irr_py%py_suffix%

@SET irr_lib_as_static=/D "_IRR_STATIC_LIB_"
@SET system_libs=user32.lib gdi32.lib advapi32.lib

@CALL _swig_ml_not_direct_use

@SET pyd_type=not_optimized

@CALL _vc_ml_not_direct_use

@ENDLOCAL

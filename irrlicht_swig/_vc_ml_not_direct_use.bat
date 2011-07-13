@CALL "%ProgramFiles%\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"

@SET include=..\freetype-%freetype_ver%\include;..\%py_ver%\PC;..\%py_ver%\Include;..\%i_ver%\include;%include%
@SET lib=..\freetype-%freetype_ver%\objs\win32\vc2008;..\%py_ver%\PCbuild;..\%i_ver%\lib\Win64-visualstudio;..\%i_ver%\lib\Win32-visualstudio;%lib%

@GOTO mode_%pyd_type%

:mode_optimized
@REM optimized creation dll, more slowly
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx /O2 /Oi /GL %irr_lib_as_static% /EHsc /Gy /W3 /nologo /Zi /link /OUT:%lib_name%.pyd /DLL /OPT:REF /OPT:ICF /LTCG /DYNAMICBASE /NXCOMPAT freetype%ft_ver%MT.lib %py_lib%.lib irrlicht.lib %system_libs% > log_cl.txt
@GOTO delete_temporary

:mode_not_optimized
@REM not optimized creation dll, more fast
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx /O2 /Ob1 /GL /D "_MBCS" %irr_lib_as_static% /EHsc /link /OUT:%lib_name%.pyd /DLL /LTCG freetype%ft_ver%MT.lib %py_lib%.lib irrlicht.lib %system_libs% > log_cl.txt
@GOTO delete_temporary

:mode_debug
@DEL *.exp *.lib *.obj *.idb *.pdb
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx -I "..\%py_ver%\PC" -I "..\%py_ver%\Include" -I "..\%i_ver%\include" %irr_lib_as_static% /D "_DEBUG" /D "WIN32" /D "_WINDOWS" /D "_WINDLL" /FD /EHsc /MDd /link /OUT:%lib_name%.pyd /DLL /DEBUG /SUBSYSTEM:WINDOWS /MACHINE:X86 /LIBPATH:"..\%py_ver%\PCbuild" /LIBPATH:"..\%i_ver%\lib" freetype%ft_ver%MT.lib %py_lib%.lib irrlicht.lib %system_libs% > log_cl.txt
@GOTO exit

:delete_temporary
@DEL *.exp *.lib *.obj *.idb *.pdb

:exit

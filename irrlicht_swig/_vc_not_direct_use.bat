@CALL "%ProgramFiles%\Microsoft Visual Studio 9.0\VC\vcvarsall.bat"

@GOTO mode_%pyd_type%

:mode_optimized
@REM optimized creation dll, more slowly
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx /O2 /Oi /GL -I "..\%py_ver%\PC" -I "..\%py_ver%\Include" -I "..\%i_ver%\include" /EHsc /Gy /W3 /nologo /Zi /link /OUT:%lib_name%.pyd /DLL /LIBPATH:"..\%py_ver%\PCbuild" /LIBPATH:"..\%i_ver%\lib" /OPT:REF /OPT:ICF /LTCG /DYNAMICBASE /NXCOMPAT %py_lib%.lib irrlicht.lib > log_cl.txt
@GOTO delete_temporary

:mode_not_optimized
@REM not optimized creation dll, more fast
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx -I "..\%py_ver%\PC" -I "..\%py_ver%\Include" -I "..\%i_ver%\include" /D "_MBCS" /EHsc /link /OUT:%lib_name%.pyd /DLL /LIBPATH:"..\%py_ver%\PCbuild" /LIBPATH:"..\%i_ver%\lib" %py_lib%.lib irrlicht.lib > log_cl.txt
@GOTO delete_temporary

:mode_debug
@DEL *.exp *.lib *.obj *.idb *.pdb
@"%ProgramFiles%\Microsoft Visual Studio 9.0\VC\bin\cl.exe" %lib_name%.cxx -I "..\%py_ver%\PC" -I "..\%py_ver%\Include" -I "..\%i_ver%\include" /D "_DEBUG" /D "WIN32" /D "_WINDOWS" /D "_WINDLL" /FD /EHsc /MDd /link /OUT:%lib_name%.pyd /DLL /DEBUG /SUBSYSTEM:WINDOWS /MACHINE:X86 /LIBPATH:"..\%py_ver%\PCbuild" /LIBPATH:"..\%i_ver%\lib" %py_lib%.lib irrlicht.lib > log_cl.txt
@GOTO exit

:delete_temporary
@DEL *.exp *.lib *.obj *.idb *.pdb

:exit

@DEL log_*.txt irr_py*.cxx irr_py*.h %lib_name%.pyd irrlicht.py *.pyc

@SET swig_ver=2.0.0

@GOTO %lib_name:~4,3%

:py2
@..\swigwin-%swig_ver%\swig.exe -c++ -o %lib_name%.cxx -keyword -I../freetype-%freetype_ver%/include -I../%i_ver%/include -python -castmode -cppcast -interface %lib_name% -O irrlicht.i 2> log_stderr_swig.txt
@GOTO exit

:py3
@..\swigwin-%swig_ver%\swig.exe -c++ -o %lib_name%.cxx -keyword -I../freetype-%freetype_ver%/include -I../%i_ver%/include -python -castmode -cppcast -interface %lib_name% -O -py3 irrlicht.i 2> log_stderr_swig.txt

:exit

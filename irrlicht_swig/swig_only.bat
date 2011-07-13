@SET lib_name=irr_pyXX

@SET i_ver=irrlicht-1.7.1

@DEL irr_py*.cxx irr_py*.h irrlicht.py

@..\swigwin-2.0.0\swig.exe -c++ -o %lib_name%.cxx -keyword -I../%i_ver%/include -python -castmode -cppcast -interface %lib_name% -O irrlicht.i 2> log_stderr_swig.txt

@REM PAUSE

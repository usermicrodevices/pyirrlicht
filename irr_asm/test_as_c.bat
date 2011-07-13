@SETLOCAL

@COLOR 1F

@DEL test_as_c.exe log_*.txt

@SET fasminc=\fasmw\INCLUDE

@\fasmw\fasm.exe -m16384 test_as_c.asm test_as_c.exe 2> log_err_test_as_c.txt

@IF EXIST test_as_c.exe (test_as_c.exe > log_test_as_c_exe.txt 2> log_err_test_as_c_exe.txt)

@REM PAUSE

@ENDLOCAL
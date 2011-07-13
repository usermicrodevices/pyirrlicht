@SETLOCAL

@COLOR 1F

@DEL test.exe log_*.txt

@SET fasminc=\fasmw\INCLUDE

@\fasmw\fasm.exe -m16384 test.asm test.exe 2> log_err_test.txt

@IF EXIST test.exe (test.exe > log_test_exe.txt 2> log_err_test_exe.txt)

@REM PAUSE

@ENDLOCAL
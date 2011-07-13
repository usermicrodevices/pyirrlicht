@SETLOCAL

@COLOR 1F

@DEL HelloWorld.exe log_*.txt

@SET fasminc=\fasmw\INCLUDE

@\fasmw\fasm.exe -m16384 HelloWorld.asm HelloWorld.exe 2> log_err_HelloWorld.txt

@IF EXIST HelloWorld.exe (HelloWorld.exe > log_HelloWorld_exe.txt 2> log_err_HelloWorld_exe.txt)

@REM PAUSE

@ENDLOCAL
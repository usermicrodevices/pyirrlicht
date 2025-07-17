@SETLOCAL

@COLOR 1F

@DEL log_*.txt

@IF EXIST HelloWorld.exe (HelloWorld.exe > log_HelloWorld_exe.txt 2> log_err_HelloWorld_exe.txt)

@ENDLOCAL
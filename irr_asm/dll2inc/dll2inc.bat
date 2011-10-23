@SETLOCAL

@COLOR 1F

@DEL dll2inc.exe log_*.txt

@SET fasminc=\fasmw\INCLUDE

@\fasmw\fasm.exe dll2inc.asm dll2inc.exe 2> log_err_dll2inc.txt

@REM PAUSE

@ENDLOCAL
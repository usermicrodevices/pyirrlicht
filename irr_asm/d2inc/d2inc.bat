@SETLOCAL

@COLOR 1F

@DEL test.exe log_*.txt

@SET fasminc=\fasmw\INCLUDE

@\fasmw\fasm.exe d2inc.asm d2inc.exe 2> log_err_d2inc.txt

@REM PAUSE

@ENDLOCAL
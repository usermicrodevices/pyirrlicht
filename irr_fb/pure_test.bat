@REM \FreeBASIC\fbc.exe -arch 386 -exx -g pure_test.bas

@\FreeBASIC\fbc.exe -s gui pure_test.bas

@MOVE /y *.exe ..\

@..\pure_test.exe

@REM PAUSE

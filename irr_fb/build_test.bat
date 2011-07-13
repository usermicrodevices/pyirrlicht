@REM \FreeBASIC\fbc.exe -r test.bas

@REM \FreeBASIC\fbc.exe -exx -g test.bas

@\FreeBASIC\fbc.exe -s gui test.bas resource.rc

@MOVE /y test.exe ..\

@DEL *.obj

@REM PAUSE

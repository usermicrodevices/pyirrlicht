@REM \FreeBASIC\fbc.exe -exx -g HelloWorld.bas

@\FreeBASIC\fbc.exe -s gui HelloWorld.bas resource.rc

@MOVE /y HelloWorld.exe ..\

@DEL *.obj

@PAUSE

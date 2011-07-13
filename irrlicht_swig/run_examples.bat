@DEL log_*.txt

@GOTO test_%2

:test_py2
@%1 irrlicht_test.py 1> log_stdout_irrlicht_test.txt 2> log_stderr_irrlicht_test.txt

@GOTO test_common


:test_py3
@%1 irrlicht_test_py3.py 1> log_stdout_irrlicht_test_py3.txt 2> log_stderr_irrlicht_test_py3.txt


:test_common

@%1 HelloWorld.py 1> log_stdout_HelloWorld.txt 2> log_stderr_HelloWorld.txt

@%1 Collision.py 1> log_stdout_Collision.txt 2> log_stderr_Collision.txt

@%1 2DGraphics.py 1> log_stdout_2DGraphics.txt 2> log_stderr_2DGraphics.txt

@%1 Movement.py 1> log_stdout_Movement.txt 2> log_stderr_Movement.txt

@%1 Quake3Map.py 1> log_stdout_Quake3Map.txt 2> log_stderr_Quake3Map.txt

@%1 Randomizer.py 1> log_stdout_Randomizer.txt 2> log_stderr_Randomizer.txt

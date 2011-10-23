from pyirrlicht import *

def test():
	vector3d = vector3df(1.0, 2.0, 3.0)
	if vector3d:
		print('pyirrlicht vector3d =', vector3d)
		print('pyirrlicht -vector3d =', -vector3d)
		print('pyirrlicht set vector3d =', vector3d.operator_set(vector3df(4.0, 5.0, 6.0)))
		print('pyirrlicht vector3d =', vector3d)
		#~ vector3d += 1.0
		vector3d += vector3df(1.0, 1.0, 1.0)
		print('pyirrlicht vector3d += vector3d =', vector3d)
		print('pyirrlicht vector3d + vector3d =', vector3d + vector3df(1.0, 1.0, 1.0))
		print('pyirrlicht vector3d =', vector3d)

if __name__ == "__main__":
	test()
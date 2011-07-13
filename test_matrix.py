from pyirrlicht import *

def test():
	matrix = matrix4()
	if matrix:
		print('pyirrlicht matrix =', matrix)
		m_pointer = matrix.const_pointer()
		print('matrix pointer =', m_pointer)
		print('matrix pointer length =', len(m_pointer))
		for it in m_pointer:
			print('matrix item =', it)
		#~ for i in range(16):
			#~ m_pointer[i] = float(i)
		#~ for it in m_pointer:
			#~ print('changed to item =', it)
		new_m_pointer = (ctypes.c_float*16)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
		new_matrix = matrix.setM(new_m_pointer)
		for it in matrix.const_pointer():
			print('changed matrix item =', it)
		for it in new_matrix.const_pointer():
			print('new matrix item =', it)
		#~ for it in new_m_pointer:
			#~ print('must be item =', it)

if __name__ == "__main__":
	test()
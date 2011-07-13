file_inc = open('irr_inc/func.inc', 'r+')

count_funcs = 0

current_pos = file_inc.tell()
symbol = file_inc.read(1)
while symbol:
	#~ if ord(symbol) == 0:
	if symbol == '\x00':
		count_funcs += 1
		print(count_funcs, 'current_pos', current_pos, symbol)
		file_inc.seek(current_pos-1)
		file_inc.write(',')
		file_inc.seek(current_pos)
		#~ file_inc.flush()
	symbol = file_inc.read(1)
	current_pos = file_inc.tell()

file_inc.close()

# Copyright(c) Max Kolosov 2010-2011 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license

import sys

type_convention_container = {
'void':'None',
'bool':'c_byte',
'unsigned char':'c_ubyte',
'short':'c_short',
's16':'c_short',
'u16':'c_ushort',
'unsigned short':'c_ushort',
's8':'c_byte',
'int':'c_int',
's32':'c_int',
'u8':'c_ubyte',
'unsigned int':'c_uint',
'u32':'c_uint',
'__int64':'c_longlong',
'long long':'c_longlong',
's64':'c_int64',
'unsigned __int64':'c_ulonglong',
'unsigned long long':'c_ulonglong',
'char':'c_char',
'c8':'c_char',
'stringc':'c_char',
'char*':'c_char_p',
'c8*':'c_char_p',
'stringc*':'c_char_p',
'wchar_t':'c_wchar',
'stringw':'c_wchar',
'wchar_t*':'c_wchar_p',
'stringw*':'c_wchar_p',
'long ':'c_long',
'unsigned long':'c_ulong',
'double':'c_double',
'float':'c_float',
'f32':'c_float',
'f64':'c_float',
'void*':'c_void_p',
'aabbox3di':'c_void_p',
'aabbox3df':'c_void_p',
'aabbox3di*':'c_void_p',
'aabbox3df*':'c_void_p',
'dimension2di':'c_void_p',
'dimension2du':'c_void_p',
'dimension2df':'c_void_p',
'dimension2di*':'c_void_p',
'dimension2du*':'c_void_p',
'dimension2df*':'c_void_p',
'line2di':'c_void_p',
'line2df':'c_void_p',
'line2di*':'c_void_p',
'line2df*':'c_void_p',
'line3di':'c_void_p',
'line3df':'c_void_p',
'line3di*':'c_void_p',
'line3df*':'c_void_p',
'matrix4':'c_void_p',
'matrix4*':'c_void_p',
'quaternion':'c_void_p',
'quaternion*':'c_void_p',
'position2di':'c_void_p',
'position2du':'c_void_p',
'position2df':'c_void_p',
'position2di*':'c_void_p',
'position2du*':'c_void_p',
'position2df*':'c_void_p',
'plane3di':'c_void_p',
'plane3df':'c_void_p',
'plane3di*':'c_void_p',
'plane3df*':'c_void_p',
'recti':'c_void_p',
'rectf':'c_void_p',
'recti*':'c_void_p',
'rectf*':'c_void_p',
'triangle3di':'c_void_p',
'triangle3df':'c_void_p',
'triangle3di*':'c_void_p',
'triangle3df*':'c_void_p',
'vector2di':'c_void_p',
'vector2df':'c_void_p',
'vector2di*':'c_void_p',
'vector2df*':'c_void_p',
'vector3di':'c_void_p',
'vector3df':'c_void_p',
'vector3di*':'c_void_p',
'vector3df*':'c_void_p',
'SColor':'c_void_p',
'SColorf':'c_void_p',
'SColorHSL':'c_void_p',
'SColor*':'c_void_p',
'SColorf*':'c_void_p',
'SColorHSL*':'c_void_p',
'ITexture*':'c_void_p',
'eAllocStrategy':'c_int',
'eQ3ModifierFunction':'c_int',
'array<stringc>*':'c_void_p',
'array<stringw>*':'c_void_p',
'S3DVertex':'c_void_p',
'SExposedVideoData':'c_void_p',
'SLight':'c_void_p',
'SMaterial':'c_void_p',
'SMaterial*':'c_void_p',
'IVertexBuffer':'c_void_p',
'IIndexBuffer':'c_void_p',
'IReadFile':'c_void_p',
'IWriteFile':'c_void_p',
'IImage':'c_void_p',
'IImageReader':'c_void_p',
'IImageWriter':'c_void_p',
}

IRRLICHT_C_API = 'IRRLICHT_C_API'

def split_func_args(value):
	result = []
	arg = ''
	size = len(value)
	i = 0
	while i < size:
		symbol = value[i]
		if symbol == ',':
			result.append(arg.strip())
			arg = ''
		elif symbol == '(':
			while symbol != ')':
				arg += symbol
				i = i + 1
				symbol = value[i]
			arg += symbol
		else:
			arg += symbol
		i = i + 1
	result.append(arg.strip())
	return result

def replace_type(c_type):
	c_type = c_type.replace(' ', '').replace('<f32>', 'f').replace('<s32>', 'i').replace('<u32>', 'u').replace('const', '').replace('&', '').replace('io::', '').replace('irr::', '').replace('core::', '').replace('video::', '').replace('scene::', '').replace('gui::', '').replace('SEvent::', '').replace('matrix4::', '')
	if 'unsigned' in c_type:
		c_type = c_type.replace('unsigned', 'unsigned ')
	elif c_type.find('array<') > -1:
		c_type = 'void*'
	elif c_type.isupper():
		c_type = 'int'
	if c_type in type_convention_container:
		py_type = type_convention_container[c_type]
		if py_type != 'None':
			py_type = 'ctypes.' + py_type
		return py_type
	elif ('*' or '&') in c_type:
		return 'ctypes.c_void_p'
	else:
		print('NOT IMPLEMENTED TYPE', c_type)
		return c_type

def convert(h_file_name, py_file_name = ''):
	hfile = open(h_file_name, 'r')

	if len(py_file_name) == 0:
		py_file_name = h_file_name[:-1] + 'py'

	pyfile = open(py_file_name, 'w')
	#~ pyfile = sys.stdout

	func_count = 0
	funcs_container = []
	content_line = hfile.readline()
	hfile_line_info = 1

	parent_class_container = {}

	while content_line:
		content_line = content_line.strip()
		if len(content_line) > 1:
			if content_line[:2] == '//':
				if content_line.find('class') > -1 and content_line.find(':') > content_line.find('class'):
					s1, s2 = content_line.split(':')
					if s1.find('class') > -1 and s2.find('public') > -1:
						parent_class_container[s1.split('class')[1].strip()] = s2.split('public')[1].strip()
				elif content_line.find('struct') > -1 and content_line.find(':') > content_line.find('struct'):
					s1, s2 = content_line.split(':')
					if s1.find('struct') > -1 and s2.find('public') > -1:
						parent_class_container[s1.split('struct')[1].strip()] = s2.split('public')[1].strip()
				new_content_line = content_line.replace('//', '#', 1) + '\n'
				pyfile.write(new_content_line)
			else:
				have_body = content_line.find('){')
				if have_body > -1:
					content_line = content_line[:have_body]
				else:
					content_line = content_line[:-1]
				if content_line[:len(IRRLICHT_C_API)] == IRRLICHT_C_API:
					if content_line.find('(') < 0:
						c_vtype, c_vname = content_line.split('=')[0].replace(IRRLICHT_C_API, '').strip().split(' ')
						py_vname = c_vname
						if py_vname[0] == '_':
							py_vname = py_vname[1:]
						new_content_line = py_vname + ' = ' + replace_type(c_vtype) + ".in_dll(c_module, '" + c_vname + "').value\n"
						pyfile.write(new_content_line)
					else:
						new_content_line = content_line.replace('const ', '').replace('false', 'False').replace('true', 'True').replace('1.0f', '1.0').replace(IRRLICHT_C_API + ' ', '')
						func_type_name, func_args = new_content_line.split('(', 1)
						func_type, func_name = func_type_name.rsplit(' ', 1)
						func_type, func_name, func_args = func_type.strip(), func_name.strip(), func_args.strip()
						#~ list_func_args = func_args.split(', ')
						list_func_args = split_func_args(func_args)
						func_args = []
						write_content_line = func_name + ' = func_type(' + replace_type(func_type)
						for func_arg in list_func_args:
							default_value = None
							list_func_arg = func_arg.strip().split('=')
							if len(list_func_arg) > 1:
								default_value = list_func_arg[1].strip()
							arg_type_name = list_func_arg[0].strip()
							if arg_type_name:
								arg_type, arg_name = arg_type_name.rsplit(' ', 1)
								func_args.append([arg_name, default_value])
								write_content_line += ', ' + replace_type(arg_type)
							#~ else:
								#~ func_args.append(['', default_value])
						write_content_line += ")(('" + func_name + "', c_module))\n"
						pyfile.write(write_content_line)
						funcs_container.append((func_name, func_type, func_args, hfile_line_info))
						func_count = func_count + 1
		content_line = hfile.readline()
		hfile_line_info = hfile_line_info + 1

	class_count = 0
	if len(funcs_container) > 0:
		class_name = ''
		for func_name, func_type, func_args, hfile_line_info in funcs_container:
			class_name_from_current_func = func_name.split('_')[0]
			if class_name_from_current_func != class_name:
				class_name = class_name_from_current_func
				parent_class_name = 'object'
				if class_name in parent_class_container:
					parent_class_name = parent_class_container[class_name]
				pyfile.write('\n')
				pyfile.write('class %s(%s):\n' % (class_name, parent_class_name))
				pyfile.write('	def __init__(self, *args, **kwargs):\n')
				pyfile.write('		self.c_pointer = None\n')
				pyfile.write('		if len(args) > 0:\n')
				pyfile.write('			self.c_pointer = args[0]\n')
				class_count = class_count + 1
			if len(func_name.split('_')) < 2:
				print('ERROR:', h_file_name, 'line', hfile_line_info,'last class name', class_name, 'not valid function name', func_name)
				continue
			write_line1 = '	def ' + func_name.split('_', 1)[1] + '(self'
			args_line2 = ''
			for arg_name, default_value in func_args:
				if arg_name == 'pointer':
					continue
				arg_name = ', ' + arg_name
				if default_value:
					write_line1 += arg_name + ' = ' + default_value
				else:
					write_line1 += arg_name
				args_line2 += arg_name
			pyfile.write(write_line1 + '):\n')
			write_line2 = func_name + '(self.c_pointer' + args_line2 + ')'
			if func_type == 'void':
				pyfile.write('		' + write_line2 + '\n')
			else:
				pyfile.write('		return ' + write_line2 + '\n')

	hfile.close()
	pyfile.close()
	print(func_count, 'FUNCTIONS')
	print(class_count, 'CLASSES')


if __name__ == "__main__":
	if len(sys.argv) > 1:
		if isinstance(sys.argv[1], str):
			hfile_name = sys.argv[1]
			pyfile_name = hfile_name[:-1] + 'py'
			if len(sys.argv) > 2:
				if isinstance(sys.argv[2], str):
					pyfile_name = sys.argv[2]
			convert(hfile_name, pyfile_name)
		else:
			print('USE: h2ctypes file_name.h [file_name.py]')
	else:
		print('USE: h2ctypes file_name.h [file_name.py]')
		#~ convert('irrlicht_c/_.h')

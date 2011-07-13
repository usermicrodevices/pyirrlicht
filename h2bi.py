# Copyright(c) Max Kolosov 2010 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license

import os, sys


prolog_extern_string = '''\' This file was automatic generated with "h2bi" script

Type EVENT_METHOD As Function(ByVal _event_ As Any Ptr) As UByte

#inclib "../%s"

#include once "const.bi"

Extern "c"

\tExtern _IRR_WCHAR_FILESYSTEM Alias "IRR_WCHAR_FILESYSTEM" As Integer

#if _IRR_WCHAR_FILESYSTEM
	Type fschar As WString Ptr
#else
	Type fschar As ZString Ptr
#endif

\tDeclare Sub delete_pointer(ByVal _pointer_ As Any Ptr)

'''

epilog_extern_string = '''

End Extern
'''

createDevice_string = '''
Declare Function createDevice( _
	ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, _
	ByVal windowSize As dimension2du Ptr = 0, _
	ByVal bits As UInteger = 16, _
	ByVal fullscreen As UByte = False, _
	ByVal stencilbuffer As UByte = False, _
	ByVal vsync As UByte = False, _
	ByVal receiver As IEventReceiver Ptr = 0) As IrrlichtDevice

Function createDevice(ByVal deviceType As E_DRIVER_TYPE = EDT_SOFTWARE, ByVal windowSize As dimension2du Ptr = 0, ByVal bits As UInteger = 16, ByVal fullscreen As UByte = False, ByVal stencilbuffer As UByte = False, ByVal vsync As UByte = False, ByVal receiver As IEventReceiver Ptr = 0) As IrrlichtDevice
    Return IrrlichtDevice(deviceType, windowSize, bits, fullscreen, stencilbuffer, vsync, receiver)
End Function
'''

type_convention_container = {
'void':None,
'bool':'UByte',
'unsigned char':'UByte',
'short':'Short',
'unsigned short':'UShort',
'int':'Integer',
's32':'Integer',
'unsigned int':'UInteger',
'u32':'UInteger',
'u16':'UShort',
's16':'Short',
'long':'Long',
'__int64':'Longint',
'long long':'Longint',
's64':'ULong',
'unsigned __int64':'ULongint',
'unsigned long long':'ULongint',
'char':'ZString Ptr',
'c8':'ZString Ptr',
'stringc':'ZString Ptr',
'char*':'ZString Ptr',
'c8*':'ZString Ptr',
'u8':'ZString Ptr',
'stringc*':'ZString Ptr',
'fschar_t':'fschar',
'fschar_t*':'fschar',
'wchar_t':'WString Ptr',
'stringw':'WString Ptr',
'wchar_t*':'WString Ptr',
'stringw*':'WString Ptr',
'ustring':'WString Ptr',
'uchar32_t':'WString Ptr',
'long ':'Long',
'unsigned long':'ULong',
'double':'Double',
'float':'Single',
'f32':'Single',
'f64':'Single',
'path':'ZString Ptr',
'void*':'Any Ptr',
'arrayi':'Any Ptr',
'arrayu':'Any Ptr',
'aabbox3di':'Any Ptr',
'aabbox3di*':'Any Ptr',
'aabbox3df':'Any Ptr',
'aabbox3df*':'Any Ptr',
'dimension2di':'Any Ptr',
'dimension2du':'Any Ptr',
'dimension2df':'Any Ptr',
'line2di':'Any Ptr',
'line2di*':'Any Ptr',
'line2df':'Any Ptr',
'line2df*':'Any Ptr',
'line3di':'Any Ptr',
'line3di*':'Any Ptr',
'line3df':'Any Ptr',
'line3df*':'Any Ptr',
'matrix4':'Any Ptr',
'matrix4*':'Any Ptr',
'quaternion':'Any Ptr',
'quaternion*':'Any Ptr',
'position2di':'Any Ptr',
'position2du':'Any Ptr',
'position2df':'Any Ptr',
'position2di*':'Any Ptr',
'position2du*':'Any Ptr',
'position2df*':'Any Ptr',
'plane3di':'Any Ptr',
'plane3di*':'Any Ptr',
'plane3df':'Any Ptr',
'plane3df*':'Any Ptr',
'recti':'Any Ptr',
'recti*':'Any Ptr',
'rectf':'Any Ptr',
'rectf*':'Any Ptr',
'triangle3di':'Any Ptr',
'triangle3di*':'Any Ptr',
'triangle3df':'Any Ptr',
'triangle3df*':'Any Ptr',
'vector2di':'Any Ptr',
'vector2di*':'Any Ptr',
'vector2du':'Any Ptr',
'vector2du*':'Any Ptr',
'vector2df':'Any Ptr',
'vector2df*':'Any Ptr',
'vector3di':'Any Ptr',
'vector3di*':'Any Ptr',
'vector3df':'Any Ptr',
'vector3df*':'Any Ptr',
'S3DVertex':'Any Ptr',
'SColor':'Any Ptr',
'SColorf':'Any Ptr',
'SColor*':'Any Ptr',
'SColorf*':'Any Ptr',
'SColor&':'Any Ptr',
'SColorf&':'Any Ptr',
'ITexture*':'Any Ptr',
'array<stringc>*':'Any Ptr',
'array<stringw>*':'Any Ptr',
'array<position2di>':'Any Ptr',
'IVertexBuffer':'Any Ptr',
'IIndexBuffer':'Any Ptr',
'SMaterial':'Any Ptr',
'SMaterialLayer':'Any Ptr',
'SEvent':'Any Ptr',
'SGUIEvent':'Any Ptr',
'SMouseInput':'Any Ptr',
'SKeyInput':'Any Ptr',
'SJoystickEvent':'Any Ptr',
'SLogEvent':'Any Ptr',
'SUserEvent':'Any Ptr',
'SInputMethodEvent':'Any Ptr',
'SExposedVideoData':'Any Ptr',
'SViewFrustum':'Any Ptr',
'SLight':'Any Ptr',
'SIrrlichtCreationParameters':'Any Ptr',
'SOverrideMaterial':'Any Ptr',
'list<IGUIElement>':'Any Ptr',
'list<IGUIElement>::Iterator':'Any Ptr',
'IGUIEnvironment':'Any Ptr',
'IGUIElement':'Any Ptr',
'IGUIFont':'Any Ptr',
'IImage':'Any Ptr',
'IWriteFile':'Any Ptr',
'u32(IRRCALLCONV':'Any Ptr',
'void(IRRCALLCONV':'Any Ptr',
'EIntersectionRelation3D':'EIntersectionRelation3D',
'eAllocStrategy':'eAllocStrategy',
'EFileSystemType':'EFileSystemType',
'eConstructor':'eConstructor',
'eQ3ModifierFunction':'eQ3ModifierFunction',
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

def replace_type(c_type, info = ''):
	c_type = c_type.replace(' ', '').replace('<f32>', 'f').replace('<s32>', 'i').replace('<u32>', 'u').replace('const', '').replace('&', '').replace('io::', '').replace('irr::', '').replace('core::', '').replace('video::', '').replace('scene::', '').replace('gui::', '').replace('SEvent::', '').replace('matrix4::', '')
	if 'unsigned' in c_type:
		c_type = c_type.replace('unsigned', 'unsigned ')
	elif c_type.find('array<') > -1:
		c_type = 'void*'
	#~ elif c_type.isupper():
		#~ c_type = 'int'
	if c_type in type_convention_container:
		bi_type = type_convention_container[c_type]
		if bi_type:
			bi_type = 'As ' + bi_type
		return bi_type
	elif ('*' or '&') in c_type:
		return 'As Any Ptr'
	else:
		if c_type != c_type.upper():
			print('NOT IMPLEMENTED TYPE', c_type, info)
		#~ else:
			#~ return 'As Integer'
		return 'As ' + c_type

def convert_functions(read_file, write_file):
	func_count = 0
	funcs_container = []
	funcs_names_container = []
	content_line = read_file.readline()
	hfile_line_info = 1

	class_name = ''
	class_container = {}
	parent_class_container = {}

	while content_line:
		if content_line.find('bool(IRRCALLCONV *OnEventMethod)(const SEvent&)') > -1:
			content_line = content_line.replace('bool(IRRCALLCONV *OnEventMethod)(const SEvent&)', 'EVENT_METHOD OnEventMethod')
		content_line = content_line.strip()
		if len(content_line) > 1:
			if content_line[:2] == '//':
				if content_line.find('class') > -1 and content_line.find(':') > content_line.find('class'):
					content_line = content_line.replace('scene::', '')
					try:
						s1, s2 = content_line.split(':')
					except:
						print(content_line)
						raise
					if s1.find('class') > -1 and s2.find('public') > -1:
						parent_class_container[s1.split('class')[1].strip()] = s2.split('public')[1].strip()
				#~ new_content_line = content_line.replace('//', "'", 1) + '\n'
				#~ write_file.write(new_content_line)
				#~ write_file.write('\n')
			#~ elif content_line.split()[0] in ('#ifdef', '#else', '#endif'):
				#~ write_file.write(content_line + '\n')
			else:
				have_body = content_line.find('){')
				if have_body > -1:
					content_line = content_line[:have_body]
				else:
					content_line = content_line[:-1]
				if content_line[:len(IRRLICHT_C_API)] == IRRLICHT_C_API:
					if content_line.find('(') < 0:# CONSTANTS
						c_vtype, c_vname = content_line.split('=')[0].replace(IRRLICHT_C_API, '').strip().split(' ')
						bi_vname = c_vname
						if bi_vname[0] == '_':
							bi_vname = bi_vname[1:]
						new_content_line = '\tExtern %s Alias "%s" %s\n' % (bi_vname, c_vname, replace_type(c_vtype))
						write_file.write(new_content_line)
					else:
						new_content_line = content_line.replace('const ', '').replace('false', 'False').replace('true', 'True').replace('1.0f', '1.0').replace(IRRLICHT_C_API + ' ', '')
						func_type_name, func_args = new_content_line.split('(', 1)
						func_type, func_name = func_type_name.rsplit(' ', 1)
						func_type, func_name, func_args = func_type.strip(), func_name.strip(), func_args.strip()
						alias_name = ''
						if func_name == 'ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName1':
							alias_name = str(func_name)
							func_name = 'ISceneNodeAnimatorFactory_getCreateableScNodeAnimatorTypeName1'
						if func_name == 'ISceneNodeAnimatorFactory_getCreateableSceneNodeAnimatorTypeName2':
							alias_name = str(func_name)
							func_name = 'ISceneNodeAnimatorFactory_getCreateableScNodeAnimatorTypeName2'
						class_name_from_current_func = func_name.split('_')[0]
						if class_name_from_current_func != class_name:
							class_name = class_name_from_current_func
							class_container[class_name] = []
						if len(func_name) > 64:
							print('---VERY LONG FUNCTION NAME', func_name)
							print('---MAXIMUM 64 SYMBOLS, THIS IS', len(func_name))
						replaced_func_type = replace_type(func_type, func_name)
						list_func_args = split_func_args(func_args)
						func_args = []
						declaration_string, full_args_string, only_args_names = '\t', '', ''
						if func_name in funcs_names_container:
							declaration_string += "'"
						else:
							funcs_names_container.append(func_name)
						if replaced_func_type:
							declaration_string += 'Declare Function '
						else:
							declaration_string += 'Declare Sub '
						if alias_name:
							declaration_string += func_name + ' Alias "' + alias_name + '" ('
						else:
							declaration_string += func_name + '('
						for func_arg in list_func_args:
							default_value = None
							list_func_arg = func_arg.strip().split('=')
							if len(list_func_arg) > 1:
								default_value = list_func_arg[1].strip()
							arg_type_name = list_func_arg[0].strip()
							if arg_type_name:
								arg_type, arg_name = arg_type_name.replace(' to', ' _to_').replace(' On', ' _On_').replace(' end', ' _end_').replace(' type', ' _type_').replace(' name', ' _name_').replace(' len', ' _len_').replace(' append', ' _append_').replace(' pointer', ' _pointer_').replace(' line', ' _line_').replace(' color', ' _color_').replace(' width', ' _width_').replace(' loop', ' _loop_').replace(' point', ' _point_').replace(' draw', ' _draw_').replace(' size', ' _size_').replace(' data', ' _data_').replace(' constructor', ' _constructor_').replace(' isVisible', ' _isVisible_').replace(' isPushButton', ' _isPushButton_').replace(' clearZBuffer', ' _clearZBuffer_').rsplit(' ', 1)
								arg_name = arg_name.replace('*', '').replace('&', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')
								only_args_names += arg_name + ', '
								full_args_string += 'ByVal ' + arg_name + ' ' + replace_type(arg_type, func_name) + ', '
							#~ else:
								#~ func_args.append(['', default_value])
						only_args_names = only_args_names.rstrip(', ')
						full_args_string = full_args_string.rstrip(', ')
						write_content_line = declaration_string + full_args_string + ')'
						if replaced_func_type:
							write_content_line += ' ' + replaced_func_type
						write_file.write(write_content_line + '\n')
						full_args_string = full_args_string.replace('ByVal _pointer_ As Any Ptr', '').lstrip(', ')
						only_args_names = only_args_names.replace('_pointer_', '').lstrip(', ')
						funcs_container.append((func_name, replaced_func_type, full_args_string, only_args_names, hfile_line_info))
						this_ctor = (func_name.find('_ctor') > -1 or func_name.find('_Constructor') > -1)
						if this_ctor:
							write_content_line = '\tDeclare Constructor(%s)' % full_args_string
						else:
							write_content_line = declaration_string.replace(class_name + '_', '') + full_args_string + ')'
							if replaced_func_type:
								write_content_line += ' ' + replaced_func_type
							write_content_line = write_content_line.replace(' end', ' _end_').replace(' sub', ' _sub_').replace(' next', ' _next_').replace(' swap', ' _swap_').replace(' pointer', ' _pointer_')
						class_container[class_name].append(write_content_line + '\n')
						func_count = func_count + 1
		content_line = read_file.readline()
		hfile_line_info = hfile_line_info + 1
	return funcs_container, parent_class_container, class_container, func_count

def write_class(funcs_container, parent_class_container, class_container, write_file):
	class_count = 0
	if len(funcs_container) > 0:
		class_name = ''
		for func_name, func_type, full_args_string, only_args_names, hfile_line_info in funcs_container:
			class_name_from_current_func = func_name.split('_')[0]
			if class_name_from_current_func != class_name:
				class_name = class_name_from_current_func
				parent_class_name = 'object'
				if class_name in parent_class_container:
					parent_class_name = parent_class_container[class_name]
				write_file.write('\n')
				write_file.write('Type %s\n' % class_name)
				write_file.write('\tAs Ubyte del_ptr = True\n')
				write_file.write('\tAs Any Ptr c_pointer = 0\n')
				write_file.write('\tDeclare Constructor(ByVal other As Any Ptr)\n')
				write_file.write('\tDeclare Destructor()\n')
				write_file.write('\tDeclare Operator Cast() As Any Ptr\n')
				write_file.write('\tDeclare Operator @() As Any Ptr\n')
				write_file.write(''.join(class_container[class_name]) + '\n')
				write_file.write('End Type\n')
				write_file.write('Constructor %s(ByVal other As Any Ptr)\n' % class_name)
				write_file.write('\tthis.c_pointer = other\n')
				write_file.write('\tthis.del_ptr = False\n')
				write_file.write('End Constructor\n')
				write_file.write('Destructor %s()\n' % class_name)
				write_file.write('\tIf this.del_ptr Then\n')
				write_file.write('\t\tdelete_pointer(this.c_pointer)\n')
				write_file.write('\tEnd If\n')
				write_file.write('End Destructor\n')
				write_file.write('Operator %s.Cast() As Any Ptr\n' % class_name)
				write_file.write('\tOperator = this.c_pointer\n')
				write_file.write('End Operator\n')
				write_file.write('Operator %s.@() As Any Ptr\n' % class_name)
				write_file.write('\tOperator = this.c_pointer\n')
				write_file.write('End Operator\n')
				class_count = class_count + 1
			if len(func_name.split('_')) < 2:
				print('ERROR:', h_file_name, 'line', hfile_line_info,'last class name', class_name, 'not valid function name', func_name)
				continue
			only_func_name = func_name.split('_', 1)[1]
			func_name_delimiter = '%s.%s' % (class_name, only_func_name)
			this_ctor = (func_name.find('_ctor') > -1 or func_name.find('_Constructor') > -1)
			if this_ctor:
				write_file.write('Constructor %s(%s)\n' % (class_name, full_args_string))
				write_file.write('\tthis.c_pointer = %s(%s)\n' % (func_name, only_args_names))
				write_file.write('End Constructor\n')
			else:
				if func_type:
					write_file.write('Function %s(%s) %s\n' % (func_name_delimiter, full_args_string, func_type))
				else:
					write_file.write('Sub %s(%s)\n' % (func_name_delimiter, full_args_string))
				if only_args_names:
					only_args_names = ', ' + only_args_names
				write_line = func_name + '(this.c_pointer' + only_args_names + ')'
				if func_type:
					write_file.write('\tReturn ' + write_line + '\n')
					write_file.write('End Function\n')
				else:
					write_file.write('\t' + write_line + '\n')
					write_file.write('End Sub\n')
	return class_count

def convert_file(source_file_name, destination_file_name = ''):
	read_file = open(source_file_name, 'r')

	if len(destination_file_name) == 0:
		destination_file_name = source_file_name[:-1] + 'bi'

	write_file = open(destination_file_name, 'w')
	#~ write_file = sys.stdout
	#~ write_file.write('\' This file was automatic generated with "h2bi" script\n\n')
	#~ write_file.write('Type EVENT_METHOD As Function(ByVal _event_ As Any Ptr) As UByte\n\n')
	#~ write_file.write('#inclib "irrlicht_c"\n\nExtern "c"\n')
	#~ write_file.write('\tDeclare Sub delete_pointer(ByVal _pointer_ As Any Ptr)\n')
	write_file.write(prolog_extern_string % 'irrlicht_c')
	funcs_container, parent_class_container, class_container, func_count = convert_functions(read_file, write_file)
	#~ write_file.write('End Extern\n')
	write_file.write(epilog_extern_string)
	class_count = write_class(funcs_container, parent_class_container, class_container, write_file)

	read_file.close()
	write_file.close()
	print(func_count, 'FUNCTIONS')
	print(class_count, 'CLASSES')

def convert_files(source_dir_name, destination_dir_name = None, functions_file_name_out = None, classes_file_name_out = None, classes_in_one_file = False, generate_classes = False):
	class_count = 0
	full_func_count = 0
	content_container = []
	if not functions_file_name_out:
		functions_file_name_out = source_dir_name + '.bi'
	if destination_dir_name:
		functions_file_name_out = '%s/%s' % (destination_dir_name, functions_file_name_out)
	functions_file_out = open(functions_file_name_out, 'w')
	classes_file_out = None
	if generate_classes:
		if classes_in_one_file:
			if classes_file_name_out:
				classes_file_out = open(classes_file_name_out, 'w')
				classes_file_out.write('\' This file was automatic generated with "h2bi" script\n\n')
				classes_file_out.write('\n#include once "const.bi"\n')
				classes_file_out.write('\n#include once "%s"\n' % os.path.split(functions_file_name_out)[1])

	#~ functions_file_out.write('\' This file was automatic generated with "h2bi" script\n\n')
	#~ functions_file_out.write('Type EVENT_METHOD As Function(ByVal _event_ As Any Ptr) As UByte\n\n')
	#~ functions_file_out.write('\n#inclib "%s"\n#include once "const.bi"\n\nExtern "c"\n' % source_dir_name)
	#~ functions_file_out.write('\tDeclare Sub delete_pointer(ByVal _pointer_ As Any Ptr)\n')
	functions_file_out.write(prolog_extern_string % source_dir_name)

	for root, dirs, files in os.walk(source_dir_name):
		for file_name in files:
			if file_name[0] == '_' and file_name[-2:] == '.h':
				print('====== CONVERTING FILE', file_name)
				read_file = open('%s/%s' % (source_dir_name, file_name), 'r')
				funcs_container, parent_class_container, class_container, func_count = convert_functions(read_file, functions_file_out)
				full_func_count += func_count
				if generate_classes:
					if classes_file_out:
						class_count += write_class(funcs_container, parent_class_container, class_container, classes_file_out)
					else:
						content_container.append((file_name.replace('.h', '.bi')[1:], funcs_container, parent_class_container, class_container))
				read_file.close()

	#~ functions_file_out.write('End Extern\n')
	functions_file_out.write(epilog_extern_string)

	if generate_classes:
		if classes_file_out:
			classes_file_out.close()
		else:
			main_classes_file = None
			if classes_in_one_file and not classes_file_out:
				functions_file_out.write('\n\n\' Classes\n\n')
			if destination_dir_name:
				main_classes_file = open('%s/%s.bi' % (destination_dir_name, destination_dir_name), 'w')
				main_classes_file.write('\' This file was automatic generated with "h2bi" script\n\n')
				main_classes_file.write('#include once "const.bi"\n')
			for file_name, funcs_container, parent_class_container, class_container in content_container:
				if classes_in_one_file:
					class_count += write_class(funcs_container, parent_class_container, class_container, functions_file_out)
				else:
					if destination_dir_name:
						write_file = open('%s/%s' % (destination_dir_name, file_name), 'w')
					else:
						write_file = open(file_name, 'w')
					write_file.write('\' This file was automatic generated with "h2bi" script\n\n')
					write_file.write('#include once "const.bi"\n')
					write_file.write('#include once "%s"\n' % os.path.split(functions_file_name_out)[1])
					class_count += write_class(funcs_container, parent_class_container, class_container, write_file)
					write_file.close()
					if main_classes_file:
						main_classes_file.write('#include once "%s"\n' % file_name)
			if main_classes_file:
				main_classes_file.write(createDevice_string)
				main_classes_file.close()
			else:
				functions_file_out.write(createDevice_string)
	functions_file_out.close()
	print(full_func_count, 'FUNCTIONS')
	print(class_count, 'CLASSES')


if __name__ == "__main__":
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option('-s', '--source_dir_name', dest='source_dir_name', default='irrlicht_c', help='must be source directory with h files', metavar='STRING', action='store', type='string')
	parser.add_option('-d', '--destination_dir_name', dest='destination_dir_name', default='irrlicht', help='must be destination directory name', metavar='STRING', action='store', type='string')
	parser.add_option('-f', '--functions_file_name', dest='functions_file_name', default='', help='must be destination file name', metavar='STRING', action='store', type='string')
	parser.add_option('-c', '--classes_file_name', dest='classes_file_name', default='', help='must be destination file name', metavar='STRING', action='store', type='string')
	parser.add_option('-o', '--classes_in_one_file', dest='classes_in_one_file', default=0, help='must be 0 or 1', metavar='INT', action='store', type='int')
	parser.add_option('-g', '--generate_classes', dest='generate_classes', default=0, help='generate classes or not, must be 0 or 1', metavar='INT', action='store', type='int')
	(options, args) = parser.parse_args()
	if options.functions_file_name == '':
		options.functions_file_name = options.source_dir_name + '.bi'
	if not os.path.exists(options.destination_dir_name):
		os.mkdir(options.destination_dir_name)
	if len(args) > 0:
		if options.help:
			parser.print_help()
		else:
			convert_files(options.source_dir_name, options.destination_dir_name, options.functions_file_name, options.classes_file_name, options.classes_in_one_file, options.generate_classes)
	else:
		#~ parser.print_help()
		#~ convert_file('irrlicht_c/_ISceneNode.h')
		#~ convert_files('irrlicht_c')
		convert_files(options.source_dir_name, options.destination_dir_name, options.functions_file_name, options.classes_file_name, options.classes_in_one_file, options.generate_classes)

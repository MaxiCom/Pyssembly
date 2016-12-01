from modules.global_instructions import *

import struct

def display_instruction_error(line_parsed):
	display_error_message('[' + ' '.join(line_parsed) + ']' + ' Instruction unknown')

def	convert_content(parsed_file_content):
	buffer = ""
	EAX_VALUE = 0

	for line_parsed in parsed_file_content:
	
		# MANAGE MOV INSTRUCTION
		if line_parsed[0].lower() == 'mov':
			if line_parsed[2].isdigit() == 0:
				display_instruction_error(line_parsed)

			elif line_parsed[1].lower() == 'eax':
				buffer += '66b8' + format(struct.unpack("<I", struct.pack(">I", int(line_parsed[2])))[0], 'x').zfill(8)
				EAX_VALUE = int(line_parsed[2])
			else:
				display_instruction_error(line_parsed)
					
		# MANAGE ADD INSTRUCTION
		elif line_parsed[0].lower() == 'add':
			if line_parsed[2].isdigit() == 0:
				display_instruction_error(line_parsed)

			if line_parsed[1].lower() == 'eax':
				if int(line_parsed[2]) <= 127:
					buffer += '6683c0' + format(int(line_parsed[2]), 'x').zfill(2)
					EAX_VALUE += int(line_parsed[2])
				else:
					buffer += '6605' + format(struct.unpack("<I", struct.pack(">I", int(line_parsed[2])))[0], 'x').zfill(8)
					EAX_VALUE += int(line_parsed[2])
			else:
				display_instruction_error(line_parsed)
			

		else:
				display_instruction_error(line_parsed)

	display_success_message('Convert file content ... OK')	

	print '\nFinal EAX value: %d\n' % EAX_VALUE
	return buffer

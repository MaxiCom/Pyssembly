from modules.global_instructions import *

import struct

def	convert_content(parsed_file_content):
	buffer = ""

	for line_parsed in parsed_file_content:
	
		# MANAGE MOV INSTRUCTION
		if line_parsed[0].lower() == 'mov':
			if line_parsed[2].isdigit() == 0:
				display_error_message('[' + ' '.join(line_parsed) + ']' + ' Instruction unknown')

			if line_parsed[1].lower() == 'eax':
				buffer += '66b8' + format(struct.unpack("<I", struct.pack(">I", int(line_parsed[2])))[0], 'x').zfill(8)
			else:
				display_error_message('[' + ' '.join(line_parsed) + ']' + ' Instruction unknown')
					



		else:
			display_error_message('[' + ' '.join(line_parsed) + ']' + ' Instruction unknown')

	display_success_message('Convert file content ... OK')	
	return buffer

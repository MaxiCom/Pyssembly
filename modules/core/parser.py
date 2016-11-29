from modules.global_instructions import *

def	parse_file(filename):
	buffer = []
	parsed_array = []

	with open(filename) as file:
		for line in file:

			# REMOVING COMMENTS \T \N
			buffer_line = line.split(';')[0].replace('\t', '').replace('\n', '')

			# REMOVING , THEN POPULATE ARRAY
			line_parsed = buffer_line.replace(',', '').split(' ')
			if len(line_parsed[0]) != 0:
				buffer.append(line_parsed)

	for array in buffer:
		parsed_array.append(filter(None, array))

	display_success_message('File parsing ... OK')
	return parsed_array

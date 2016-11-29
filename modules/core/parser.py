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

	print '\033[32mFile parsing ... OK\033[m'
	return parsed_array

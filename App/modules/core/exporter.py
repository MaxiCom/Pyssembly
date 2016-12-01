from modules.global_instructions import *

import binascii

def	export(buffer):
	with open('a.out', 'wb') as output_file:
		output_file.write(binascii.unhexlify(buffer))
	display_success_message('Export ... OK')

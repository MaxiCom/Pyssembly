import binascii

def	export(buffer):
	with open('a.out', 'wb') as output_file:
		output_file.write(binascii.unhexlify(buffer))

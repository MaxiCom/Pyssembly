#!/usr/bin/python2.7
from modules.arguments.manager import *
from modules.global_instructions import *
from modules.core.parser import *
from modules.core.converter import *
from modules.core.exporter import *

import sys

def	main():
	if check_args() == 0:
		parsed_file_content = parse_file(sys.argv[1])
		buffer = convert_content(parsed_file_content)
		export(buffer)
	else:
		display_help()

if __name__ == "__main__":
	main()

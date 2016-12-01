from modules.global_instructions import *

import sys
import os.path

def check_args():
	if len(sys.argv) != 2 or os.path.exists(sys.argv[1]) == 0:
		return -1
	display_success_message('Arguments ... OK')
	return 0

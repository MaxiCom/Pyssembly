import sys

def	display_help():
	display_error_message('Usage: ' + sys.argv[0] + ' [filename]')

def display_error_message(message):
	print '\033[31m%s\033[m' % message

def display_success_message(message):
	print '\033[32m%s\033[m' % message

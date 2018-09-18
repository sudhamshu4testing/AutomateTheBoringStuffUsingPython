# Ending a program early with sys.exit()

"""However you can cause the program to terminate, or exit, by calling the sys.exit() function. Since this function is in the sys module,
you have to import sys before your program can use it """

import sys

while True:
	print ('Type exit to exit. ')
	response = input()
	if response == 'exit':
		sys.exit()
	print ('You typed ' + response + '.')
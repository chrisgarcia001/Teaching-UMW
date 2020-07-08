#-----------------------------------------------------------------------------
# Author: cgarcia
# About: This is the driver for the python cryptogram solver (invertible)
#-----------------------------------------------------------------------------

import sys
from cryptogram_alg import *

# This is the main method - take encrypted message and word list files, and return the decryption.
def solve_cryptogram(encrypted_message_file, word_list_file):
	encrypted_text = open(encrypted_message_file).read()
	cleanup = lambda x: filter(lambda y: y.isalpha(), x)
	code_strings = map(cleanup, filter(lambda x: len(x) > 0, 
					   encrypted_text.lower().replace("\n", " ").split(" ")))
	code_strings = list(set(code_strings))
	word_list = WordList(word_list_file)
	ordered_code_strings = sorted(code_strings, key = lambda x: len(x))
	ordered_code_strings.reverse()
	open_codewords = map(lambda x: CodeWord(x), ordered_code_strings)
	key = find_key(open_codewords, word_list, {})
	if(key != None):
		return ''.join(map(lambda x: decode(x, key, True), encrypted_text.lower())) + "\n"
	else:
		return 'No solution in given word list!'

try:	
	print(solve_cryptogram(sys.argv[1], sys.argv[2]))
except:
	print("Usage: > python solve_cryptogram.py <coded message file> <dictionary word list file>")
	print("**If you want output to file, just add > <output filename> after the above") 


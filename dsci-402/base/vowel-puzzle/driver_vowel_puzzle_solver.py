#--------------------------------------------------------------------------
# Author: cgarcia@umw.edu
# Main program
# Sample usage: > python .\driver_vowel_puzzle_solver.py nrgtcflbgs 30
#--------------------------------------------------------------------------

import sys
from vowel_puzzle import *

try:
	words = read_words("../util-data-files/words-1000.txt")
	text = sys.argv[1]
	n = 20
	if len(sys.argv) > 1: n = int(sys.argv[2])
	results = solve(words, text)
	for line in results[0:min(len(results), n)]: # Make consonants upper case to distinguish
		a = ' '.join(line)
		b = map(lambda x: x.upper() if not(x in 'aeiou') else x, a)
		print(''.join(b))
except:
	print("\nUsage: > python driver_vowel_puzzle_solver.py <compressed text> [optional max decodings]\n")


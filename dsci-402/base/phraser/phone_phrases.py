#--------------------------------------------------------------------------------
# Author: cgarcia@umw.edu
# This is the main program for finding phrases for phone numbers.
#--------------------------------------------------------------------------------

from phraser import phraser, read_words
import sys

try:
	digits = sys.argv[1]
	wordlist = read_words(sys.argv[2])
	try:
		md = sys.argv[3]
	except IndexError:
		md = '3'
	phrases = phraser(digits, wordlist, int(md))
	print("\nPhrases for number " + digits + ":")
	for phrase in phrases:
		print("  " + phrase)
except:
	print("\nUsage: \n> python phone_phrases.py <phone number> <wordlist file> [max remaining digits]")
	exit(1)
	
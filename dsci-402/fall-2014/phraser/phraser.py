#--------------------------------------------------------------------------------
# Author: cgarcia@umw.edu
# About: This builds phrases out of phone numbers. See the phraser function at
#        the bottom - simply pass in the digit sequence, a word list, and the
#        max number of digits allowed in any phrase and it will build a list
#        of all possible phrasings for the digit sequence.
#--------------------------------------------------------------------------------

# Read in a file of words with one word per line and get the list of words.
def read_words(filename):
	return filter(lambda y: len(y) > 0, map(lambda x: x.strip().lower(), open(filename).readlines()))	

# Take a number and get the letters it codes on a phone.
def num2lett(num): 
	num = int(num)
	h = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
	if h.has_key(num):
		return h[num]
	else:
		return str(num)

# Take a letter and get the corresponding phone digit key.
def lett2num(lett):
	h = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4,
	     'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6, 'p':7, 'q':7, 'r':7,
		 's':7, 't':8, 'u':8, 'v':8 , 'w':9, 'x':9, 'y':9, 'z':9}
	if h.has_key(lett):
		return str(h[lett])
	else:
		return str(lett)

# For a given text string, get all possible wording/numeric combinations based on the word list		
# Example Usage: print(all_phrases("hit", wl)) => [['hit'], ['4', 'it'], ['4', '4', '8']]
def all_phrases(text, word_list):
	if len(text) == 0:
		return [[]]
	else:
		starts = filter(lambda x: text.startswith(x), word_list) + [lett2num(text[0])]
		phrases = []
		for start in starts:			
			np = all_phrases(text[len(start):], word_list)
			next = map(lambda x: [start] + x, np)
			phrases += next
		return phrases

# For a given digit sequence, return all text possibilities.
# Example Usage: print(all_text_combs('34')) 
#                => ['dg', 'dh', 'di', 'eg', 'eh', 'ei', 'fg', 'fh', 'fi']
def all_text_combs(digits):
	if len(digits) == 0:
		return ['']
	else:
		combs = []
		letts = map(lambda x: x, num2lett(digits[0]))
		next = all_text_combs(digits[1:])
		for lett in letts:
			for nxt in next:
				combs.append(lett + nxt)
		return combs

# Solve the phraser problem. For a string of digits and word list,
# construct every possible phrasing of the digits with at most
# max_remaining_digits in any final word. Notice in example below
# no phrase has more than 3 remaining digits.
# Example Usage: print(phraser(3433825, wl, 3)) 
#       => ['die38a5', 'didduck', '3heduck', '343duck', 'did38a5', '3ifduck', 'dieduck']
def phraser(digits, word_list, max_remaining_digits = 3):
	text_combs = all_text_combs(str(digits))
	phrases = reduce(lambda x, y: x + y, map(lambda z: all_phrases(z, word_list), text_combs))
	f = lambda x: len(filter(lambda y: y.isdigit(), x)) <= max_remaining_digits
	rem_phrases = filter(f, phrases)
	return list(set(map(lambda x: ''.join(x), rem_phrases)))
	
		

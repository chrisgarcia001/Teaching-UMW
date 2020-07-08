# This is a simple debugging test file.

from cryptogram_alg import *

wl2 = WordList("../../../util-data-files/words-1000.txt")
print(wl2.has_word("that"))
print(wl2.has_word("enr"))

dct = {1:2, 3:4}
print('Dict Inverse Test', dct, dict_inverse(dct))

code = "qbax jct qbg mqbgw"
# this and the other
# qbax jct qbg mqbgw

#code = "qbax jct qbg"

code = "how does this crazy thing work"

#code = "I will eat a little round man"
#code = "One day there will be seriously big justice"
code_strings = code.lower().split(" ")
ordered_code_strings = sorted(list(set(code.lower().split(" "))), key = lambda x: len(x))
ordered_code_strings.reverse()
print(code_strings)
open = map(lambda x: CodeWord(x), ordered_code_strings)
key = find_key(open, wl2, {})
print(key)
if(key != None):
	dec = ' '.join(map(lambda x: decode(x, key), code_strings))
	print("Decoding: ")
	print(" " + code)
	print(" " + dec)


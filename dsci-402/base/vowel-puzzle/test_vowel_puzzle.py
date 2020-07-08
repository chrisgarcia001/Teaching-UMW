# Test code

import sys
from vowel_puzzle import *

#sys.setrecursionlimit(10000)

words = read_words("../util-data-files/words-1000.txt")
print(compress("This is a sentence"))
print(all_splits(words, "thisistext"))
cmap = build_compression_map(words)
cmp_words = ['nrgtc', 'flbgs']
#print(all_decompressions(cmap, cmp_words))
#print(all_splits(cmap.keys(), 'wmn'))
#print(all_splits(cmap.keys(), 'nrgtcflbgs'))
#print(['nrgtc', 'flbgs'] in all_splits(cmap.keys(), 'nrgtcflbgs'))
result = solve(words, 'nrgtcflbgs')
print(result[1:min(len(result),100)])
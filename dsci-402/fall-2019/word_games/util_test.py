from word_util import *
from anagram import *


# Assumes we are running from the word_games directory.
words = read_words('../util-data-files/words.txt')

# Print each word
# for word in words:
	# print(word)
	
print(word_hist("ball"))
print(word_hist("beautiful"))

print(all_anagrams("spacecraft", words))
print(all_anagrams("live", words))
print(all_anagrams("silent", words))
print(time_it(all_anagrams, "spacecraft", words))
print(time_it(all_anagrams, "live", words))
print(time_it(all_anagrams, "silent", words))
from anagrams import *

#print(read_words('../util-data-files/words.txt'))
#print(word_histogram("anagram"))

word_list = read_words('../util-data-files/words.txt')
print(anagrams("cat", word_list))
print(anagrams("stick", word_list))
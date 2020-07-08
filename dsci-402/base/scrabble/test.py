from scrabbler import *

#word = "xkibvet"
word = "dou"

wl = read_words("words.txt")
print(scrabbler(word, wl, 6))
print(anagrams(word, wl))
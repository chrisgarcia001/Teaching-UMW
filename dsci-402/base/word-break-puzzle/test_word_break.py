from word_util import *
from word_break import *

#words = read_words("../util-data-files/words-1000.txt")
words = read_words("../util-data-files/words.txt")
print(word_breaks("something", words))
print(word_breaks("thisisawesome", words))
from phraser import *
w1 = read_words("words-1000.txt")
#w2 = read_words("words.txt")
print(all_phrases("hit", w1))
print(all_text_combs('34'))
print(phraser(3433825, w1))
print(phraser(6513152, w1, 5))
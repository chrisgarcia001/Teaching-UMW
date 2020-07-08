from word_chains import *
from word_util import *

print(one_off("beet", "beat"))
print(one_off("beet","beet"))
print(one_off("beat", "bats"))

# Assumes we are running from the word_games directory.
words = read_words('../util-data-files/words.txt')
#words = read_words('../util-data-files/words-1000.txt')
#graph = build_graph(words, 4)
# graph = build_graph(words, 4)

# print(graph["beet"])
# print(word_chain(graph, "bear", "beef", 4))
# print(word_chain(graph, "bear", "beef", 15))
graph = f_time(build_graph, words, 4)
print("Graph complete!")
print('---')
print(f_time(word_chain, graph, "vine", "peel", 20))
#print(f_time(word_chain, graph, "comedo", "charge", 50))
print("Solution Found")

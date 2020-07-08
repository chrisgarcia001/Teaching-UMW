from word_chains import *

words = read_words("../../../util-data-files/words.txt")
graph = build_fast_graph(words, 4)
#print(dfs_build_chain("meat", "peer", graph, (20,20))) 
print(dfs_build_chain("meat", "peer", graph)) 

# Are w1 and w2 of the same length and different
# by only 1 character?
# **Note: Assumes w1 and w2 are of same length.
def one_off(w1, w2):
	pairs = zip(w1, w2)
	off = 0
	for (c1, c2) in pairs:
		if c1 != c2:
			off += 1
		if off > 1:
			return False
	return off == 1

# Construct an adjacency-list representation 
# of the word graph.
def build_graph(word_list, word_length):
	graph = {}
	words = filter(lambda x: len(x) == word_length, word_list)
	for i in range(0, len(words) - 1):
		if not(graph.has_key(words[i])):
			graph[words[i]] = []
		for j in range(i + 1, len(words)):
			if one_off(words[i], words[j]):
				graph[words[i]].append(words[j])
				if not(graph.has_key(words[j])):
					graph[words[j]] = []
				graph[words[j]].append(words[i])
	return graph

# Construct a word chain of exactly the specified length (# of words).	
def word_chain(graph, start, end, length, seen = set([])):
	if length == 1 and start == end:
		return [start]
	elif length == 1:
		return None
	else:
		for w in set(graph[start]).difference(seen):
			path = word_chain(graph, w, end, length - 1, seen.union(set([start])))
			if path != None:
				return [start] + path
	return None
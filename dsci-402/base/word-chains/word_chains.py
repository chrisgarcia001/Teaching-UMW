# Read in a file of words with one word per line and get the list of words.
def read_words(filename):
	return filter(lambda y: len(y) > 0, map(lambda x: x.strip().lower(), open(filename).readlines()))	
	
# Are the two words just one letter apart?
def one_letter_diff(w1, w2):
	if len(w1) != len(w2):
		return False
	diffs = 0
	for (x, y) in zip(w1, w2):
		if x != y: diffs += 1
	return diffs == 1

# Efficiently build a graph of one-letter-difference connections for a word list and length.	
def build_fast_graph(word_list, word_length):
	print("Building Graph...")
	words = filter(lambda x: len(x) == word_length, word_list)
	graph = {} # Use an edge list: vertex => [vertex, vertex, ...] 
	for i in range(0, len(words)):
		searchable = words[(i + 1):]
		connections = filter(lambda x: one_letter_diff(x, words[i]), searchable)
		if not(graph.has_key(words[i])):
			graph[words[i]] = connections
		else:
			graph[words[i]] += connections
		for conn in connections:
			if not(graph.has_key(conn)):
				graph[conn] = [words[i]]
			else:
				graph[conn].append(words[i])
	print("Done!")			
	return graph
	
# Build a graph of one-letter-difference connections for a word list and length.
# In edge list format.
def build_graph(word_list, word_length):
	return build_fast_graph(word_list, word_length)

# Use depth-first search through the graph and return a chain, or None if
# a chain of length in length_range can't be found.	
def dfs_build_chain(start, target, graph, length_range = (1, 5), length = 1, prior_chain = [], seen = set([])):
	next_verts = set(graph[start]).difference(seen)
	if length > length_range[1]:
		return None
	elif length >= length_range[0] and length <= length_range[1] and start == target:
		return prior_chain + [start]
	elif len(next_verts) == 0:
		return None
	else:
		for v in next_verts:
			chain = dfs_build_chain(v, target, graph, length_range, length + 1, prior_chain + [start], seen.union([start]))
			if chain != None:
				return chain
	return None
	
	
		
	

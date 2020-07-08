# Tells if two words differ by exactly one letter.
def one_off(w1, w2):
	if len(w1) != len(w2):
		return False
	diffs = filter(lambda (x,y): x != y, zip(w1, w2)) # Difference list
	return len(diffs) == 1
	
# For a list of items and a function f(a, b) which tells
# if there is a link between a and b, build an undirected
# graph (edge-list representaion).
def build_graph(items, word_length):
	graph = {}
	items = filter(lambda w: len(w) == word_length, items)
	for i in range(len(items) - 1):
		if not(graph.has_key(items[i])):
			graph[items[i]] = []
		for j in range(i + 1, len(items)):
			if not(graph.has_key(items[j])):
				graph[items[j]] = []
			if one_off(items[i], items[j]):
				graph[items[i]].append(items[j])
				graph[items[j]].append(items[i])
	return graph

# Build a word chain of the given length fot the 
# given staring and ending word.	
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




	
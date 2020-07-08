# Find a dict key that matches the code words.	
def solve_key(open_codes, select_next_f, word_list, master_key = {}):
	for cw in open_codes:
		cw.set_vars(master_key)
	closed_codes = filter(lambda y: not(y.is_open()), open_codes)
	open_codes = filter(lambda x: x.is_open(), open_codes)
	non_words = filter(lambda x: not(word_list.has_word(x)), map(lambda y: y.word, closed_codes))
	if len(non_words) > 0:
		return None
	if len(open_codes) == 0:
		return master_key
	next_cw = select_next_f(open_codes)
	print(next_cw.code)
	for match in word_list.get_matches(next_cw.word):
		new_vars = next_cw.get_new_vars(match)
		sol = solve_key(set(open_codes).difference([next_cw]), select_next_f, word_list, dict_union(master_key, new_vars))
		if sol != None:
			return sol
	return None

# Get the codeword object out of the list 
def most_open_first(codewords):
	best_word = None
	best_num = -1
	for cw in codewords:
		oc = cw.open_chars()
		if oc > best_num:
			best_word = cw
			best_num = oc
	return best_word	

# Update the variable set and decode accordingly.
	def set_vars(self, new_vars):
		#print(new_vars)
		#print("Code: " + self.code)
		self.vars = new_vars
		#print("Before: " + self.word)
		self.word = decode(self.code, self.vars)
		#print("After: " + self.word)
		#print('----')

# Find a dict key that matches the code words.	
def find_key(open_codes, word_list, master_key = {}):
	print("Pre:")
	print(map(lambda x: str(x), open_codes))
	for cw in open_codes:
		cw.set_vars(master_key)
	print("Post:")
	print(map(lambda x: str(x), open_codes))
	closed_codes = filter(lambda y: not(y.is_open()), open_codes)
	#print("Closed:")
	#print(map(lambda x: str(x), closed_codes))
	rem_open_codes = filter(lambda x: x.is_open(), open_codes)
	non_words = filter(lambda x: not(word_list.has_word(x)), map(lambda y: y.word, closed_codes))
	#print(map(lambda x: str(x), non_words))
	if len(non_words) > 0:
		return None
	if len(rem_open_codes) == 0:
		return master_key
	next_cw = list(rem_open_codes)[0]
	#print(next_cw.code)
	for match in word_list.get_matches(next_cw.word):
		new_vars = next_cw.get_new_vars(match)
		sol = find_key(rem_open_codes[1:], word_list, dict_union(master_key, new_vars))
		if sol != None:
			return sol
	return None
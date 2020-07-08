def ownerify(owner):
	return lambda x: str(owner) + "'s " + str(x)

#define: 
# fsum = sum of a list of numbers 	
#  Ex: fsum([1,2,3]) = 6

def fsum(numbers): 
	return reduce(lambda x, y: x + y, numbers)

# fprod = product of list of numbers
#  Ex: fprod([1,2,3,4]) = 24

def fprod(numbers): 
	return reduce(lambda x, y: x * y, numbers)
	
def fac(n):
	return fprod(range(1, n + 1))
	
# fmax = maximum number in a list of numbers
#  Ex: fmax([1,2,3,4,5]) = 5
#def fmax(numbers):

# Homework: Define fzip
	# fzip(function, list1, list2, ... listn)
	#Example: fzip(lambda x: ''.join(x), ["a","b","c"], ["d, "e", "f"]) = ["ad", "be", "cf"]	

def fzip(f, *lists):
	tuples = zip(*lists)
	return map(lambda x: apply(f, x), tuples)
	
# A loopless filter built using reduce	
def my_filter(criteria_f, elements):
	combiner = lambda lst, elt: lst + [elt] if criteria_f(elt) else lst
	return reduce(combiner, [[]] + elements)
	
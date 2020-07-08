import time

# Read in a word list in 1-word-per-line format.
def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x != '', map(lambda y: y.strip().lower(), words))

# Print the execution time for a function call.	
def time_it(f, *args):
    start = time.clock()
    f(*args)
    return (time.clock() - start)*1000
	
def f_time(f, *args):
	start = time.clock()
	output = f(*args)
	print("Elapsed Time: " + str((time.clock() - start)*1000))
	return output
	

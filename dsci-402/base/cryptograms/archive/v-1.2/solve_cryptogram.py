import sys
import cryptogram_alg as cryp
#from cryptogram_alg import *

#try:	
encrypted_text = open(sys.argv[1]).read()
print(encrypted_text)
#print(open(sys.argv[2]).read())
print(cryp.solve_cryptogram(sys.argv[1], sys.argv[2]))
#except:
#	print("Usage: > python solve_cryptogram.py <coded message file> <dictionary word list file>")


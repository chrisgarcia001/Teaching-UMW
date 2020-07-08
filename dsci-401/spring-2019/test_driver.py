# from basic_examples import * # Import everything in basic_examples
# from basic_examples import print_all # Imports only print_all - import multiple functions with commas
# import basic_examples # Imports basic_examples as a module object
import basic_examples as bf # Imports basic functions into the alias bf

# Call print_all in bf:
bf.print_all(55, 100, 234, 899)


# Show examples of sorting:
a = [1,7,3,2,0,11,56,29]
b = list(a)

print(a)
a.sort()
print(a)

print("----")
print(b)
print(sorted(b))
print(b)

tups = [("a", 4), ("y", 1), ("k", 12), ("m", 6)]


print("--Key Sorting Example - Sort by first element in each tuple --")
print(sorted(tups, key=lambda x: x[0]))
print("--Key Sorting Example - Sort by second element in each tuple --")
print(sorted(tups, key=lambda x: x[1]))

print('-- Fibonacci Numbers Examples ---')
print(bf.fib(1,2,6))
print(bf.fib(1,2,8))
print(bf.fib(2,5,150))

print('-- Cartesian Product Examples ---')
print(bf.cartesian_prod([1,2,3], [4,5,6]))
print(bf.cartesian_prod([2,4,6,8],[10,12,14,16],[18,20,22,24]))

print('-- Generate Combinations Examples ---')
print(bf.gen_combs(['A','B','C','D'], 3))
print(bf.gen_combs(list(range(10)), 4))
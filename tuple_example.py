"""
Tuple Operation

() An empty tuple
T = (0,) A one-item tuple (not an expression)
T = (0, 'Ni', 1.2, 3) A four-item tuple
T = 0, 'Ni', 1.2, 3 Another four-item tuple (same as prior line)
Operation Interpretation
T = ('Bob', ('dev', 'mgr')) Nested tuples
T = tuple('spam') Tuple of items in an iterable
T[i]
T[i][j]
T[i:j]
len(T)
Index, index of index, slice, length
T1 + T2
T * 3
Concatenate, repeat
for x in T: print(x)
'spam' in T
[x ** 2 for x in T]
Iteration, membership
T.index('Ni')
T.count('Ni')
Methods in 2.6, 2.7, and 3.X: search, count
namedtuple('Emp', ['name', 'jobs']) Named tuple extension type

Tuple Function
all()	Returns true if all element are true or if tuple is empty
any()	return true if any element of the tuple is true. if tuple is empty, return false
len()	Returns length of the tuple or size of the tuple
enumerate()	Returns enumerate object of tuple
max()	return maximum element of given tuple
min()	return minimum element of given tuple
sum()	Sums up the numbers in the tuple
sorted()	input elements in the tuple and return a new sorted list
tuple()	Convert an iterable to a tuple.
"""
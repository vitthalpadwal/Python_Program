"""
Dictionary Function and Operation

D = {} Empty dictionary
D = {'name': 'Bob', 'age': 40} Two-item dictionary
E = {'cto': {'name': 'Bob', 'age': 40}} Nesting
D = dict(name='Bob', age=40)
D = dict([('name', 'Bob'), ('age', 40)])
D = dict(zip(keyslist, valueslist))
D = dict.fromkeys(['name', 'age'])
Alternative construction techniques:
keywords, key/value pairs, zipped key/value pairs, key lists
D['name']
E['cto']['age']
Indexing by key
'age' in D Membership: key present test
D.keys()
D.values()
D.items()
D.copy()
D.clear()
D.update(D2)
D.get(key, default?)
D.pop(key, default?)
D.setdefault(key, default?)
D.popitem()
Methods: all keys,
all values,
all key+value tuples,
copy (top-level),
clear (remove all items),
merge by keys,
fetch by key, if absent default (or None),
remove by key, if absent default (or error)
fetch by key, if absent set default (or None),
remove/return any (key, value) pair; etc.
len(D) Length: number of stored entries
D[key] = 42 Adding/changing keys
del D[key] Deleting entries by key
list(D.keys())
D1.keys() & D2.keys()
Dictionary views (Python 3.X)
D.viewkeys(), D.viewvalues() Dictionary views (Python 2.7)
D = {x: x*2 for x in range(10)} Dictionary comprehensions (Python 3.X, 2.7)

Dictionary Function
copy()	They copy() method returns a shallow copy of the dictionary.
clear()	The clear() method removes all items from the dictionary.
pop()	Removes and returns an element from a dictionary having the given key.
popitem()	Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
get()	It is a conventional method to access a value for a key.
dictionary_name.values()	returns a list of all the values available in a given dictionary.
str()	Produces a printable string representation of a dictionary.
update()	Adds dictionary dict2’s key-values pairs to dict
setdefault()	Set dict[key]=default if key is not already in dict
keys()	Returns list of dictionary dict’s keys
items()	Returns a list of dict’s (key, value) tuple pairs
has_key()	Returns true if key in dictionary dict, false otherwise
fromkeys()	Create a new dictionary with keys from seq and values set to value.
type()	Returns the type of the passed variable.
cmp()	Compares elements of both dict.
"""
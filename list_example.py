"""
List Operation
L = [] An empty list
L = [123, 'abc', 1.23, {}] Four items: indexes 0..3
L = ['Bob', 40.0, ['dev', 'mgr']] Nested sublists
L = list('spam')
L = list(range(-4, 4))
List of an iterable’s items, list of successive integers
L[i]
L[i][j]
L[i:j]
len(L)
Index, index of index, slice, length
L1 + L2 Concatenate, repeat
240 | Chapter 8: Lists and Dictionaries
www.it-ebooks.info
Operation Interpretation
L * 3
for x in L: print(x)
3 in L
Iteration, membership
L.append(4)
L.extend([5,6,7])
L.insert(i, X)
Methods: growing
L.index(X)
L.count(X)
Methods: searching
L.sort()
L.reverse()
L.copy()
L.clear()
Methods: sorting, reversing,
copying (3.3+), clearing (3.3+)
L.pop(i)
L.remove(X)
del L[i]
del L[i:j]
L[i:j] = []
Methods, statements: shrinking
L[i] = 3
L[i:j] = [4,5,6]
Index assignment, slice assignment
L = [x**2 for x in range(5)]
list(map(ord, 'spam'))

----------------------------------------------------------------------------
List Function

Append()	Add an element to the end of the list
Extend()	Add all elements of a list to the another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Pop()	Removes and returns an element at the given index
Clear()	Removes all items from the list
Index()	Returns the index of the first matched item
Count()	Returns the count of number of items passed as an argument
Sort()	Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()	Returns a copy of the list
round()	Rounds off to the given number of digits and returns the floating point number
reduce()	apply a particular function passed in its argument to all of the list elements stores the intermediate result and only returns the final summation value
sum()	Sums up the numbers in the list
ord()	Returns an integer representing the Unicode code point of the given Unicode character
cmp()	This function returns 1, if first list is “greater” than second list
max()	return maximum element of given list
min()	return minimum element of given list
all()	Returns true if all element are true or if list is empty
any()	return true if any element of the list is true. if list is empty, return false
len()	Returns length of the list or size of the list
enumerate()	Returns enumerate object of list
accumulate()	apply a particular function passed in its argument to all of the list elements returns a list containing the intermediate results
filter()	tests if each element of a list true or not
map()	returns a list of the results after applying the given function to each item of a given iterable
lambda()	This function can have any number of arguments but only one expression, which is evaluated and returned.


"""
from functools import reduce

'''
Reverse an array in groups of given size
Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
Output:
[3, 2, 1, 6, 5, 4, 9, 8, 7]

Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 5
Output:
[5, 4, 3, 2, 1, 8, 7, 6]

Input:
arr = [1, 2, 3, 4, 5, 6]
k = 1
Output:
[1, 2, 3, 4, 5, 6]

Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 10
Output:
[8, 7, 6, 5, 4, 3, 2, 1]
'''

# function to Reverse an array in groups of given size

def reverseGroup(input, k):
    # set starting index at 0
    start = 0

    # run a while loop len(input)/k times
    # because there will be len(input)/k number
    # of groups of size k
    result = []
    while (start < len(input)):

        # if length of group is less than k
        # that means we are left with only last
        # group reverse remaining elements
        if len(input[start:]) < k:
            result = result + list(reversed(input[start:]))
            break

        # select current group of size of k
        # reverse it and concatenate
        result = result + list(reversed(input[start:start + k]))
        start = start + k
    print(result)


#other way
result = []
input = [1, 2, 3, 4, 5, 6, 7, 8,9,10]
result = result+list(reversed(input[0:5]))
result = result + input[5:10]
print(result)

# Python code to remove all characters
# other than alphabets from string

def removeAll(input):
    # Traverse complete string and separate
    # all characters which lies between [a-z] or [A-Z]
    sepChars = [char for char in input if
                ord(char) in range(ord('a'), ord('z') + 1, 1) or ord(char) in
                range(ord('A'), ord('Z') + 1, 1)]

    # join all separated characters
    # and print them together
    return ''.join(sepChars)


# Function to Segregate 0's and 1's in an array list

def segregate(arr):
    res = ([x for x in arr if x == 0] + [x for x in arr if x == 1])
    print(res)


# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple

# creating a list
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]

# print the result
print(res)

# Python program to demonstrate list comprehension in Python

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# for understanding, above generation is same as,
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print(power_of_2)

# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i * 2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

# list for lowering the characters
print([x.lower() for x in ["A", "B", "C"]])

# list which extracts number
string = "my phone number is : 11122 !!"

print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print(numbers)

# A list of list for multiplication table
a = 5
table = [[a, b, a * b] for b in range(1, 11)]

print("\nMultiplication Table")
for i in table:
    print(i)

# Let us first create a list to demonstrate slicing
# lst contains all number from 1 to 10
lst = range(1, 11)
print(lst)

#  below list has numbers from 2 to 5
lst1_5 = lst[1: 5]
print(lst1_5)

#  below list has numbers from 6 to 8
lst5_8 = lst[5: 8]
print(lst5_8)

#  below list has numbers from 2 to 10
lst1_ = lst[1:]
print(lst1_)

#  below list has numbers from 1 to 5
lst_5 = lst[: 5]
print(lst_5)

#  below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1: 8: 2]
print(lst1_8_2)

#  below list has numbers from 10 to 1
lst_rev = lst[:: -1]
print(lst_rev)

#  below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9: 4: -2]
print(lst_rev_9_5_2)

#  filtering odd numbers
lst = filter(lambda x: x % 2 == 1, range(1, 20))
print(lst)

#  filtering odd square which are divisble by 5
lst = filter(lambda x: x % 5 == 0,
             [x ** 2 for x in range(1, 11) if x % 2 == 1])
print(lst)

#   filtering negative numbers
lst = filter((lambda x: x < 0), range(-5, 5))
print(lst)

#  implementing max() function, using
print(reduce(lambda a, b: a if (a > b) else b, [7, 12, 45, 100, 15]))


# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


# Function to find all pairs whose sum is x in
# two arrays

def allPairs(arr1, arr2, x):
    # finds all pairs in two arrays
    # whose sum is x
    print([(x - k, k) for k in arr2 if (x - k) in arr1])


# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using traversal

def maximumSum(list1):
    maxi = 0

    # traversal in the lists
    for x in list1:
        sum = 0
        # traversal in list of lists
        for y in x:
            sum += y
        maxi = max(sum, maxi)

    return maxi


# driver code
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))


# python program to check if all
# values in the list are greater
# than val using all() function

def check(list1, val):
    return (all(x > val for x in list1))


# driver code
list1 = [10, 20, 30, 40, 50, 60]
val = 5
if (check(list1, val)):
    print
    "Yes"
else:
    print
    "No"

val = 20
if (check(list1, val)):
    print
    "Yes"
else:
    print
    "No"


# function to print the first m multiple
# of a number n without using loop.
def multiple(m, n):
    # inserts all elements from n to
    # (m * n)+1 incremented by n.
    a = range(n, (m * n) + 1, n)

    print(*a)


# driver code
m = 4
n = 3
multiple(m, n)
# Driver program
if __name__ == "__main__":
    arr1 = [-1, -2, 4, -6, 5, 7]
    arr2 = [6, 3, 4, 0]
    x = 8
    allPairs(arr1, arr2, x)

    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    segregate(arr)

    input = "$Gee*k;s..fo, r'Ge^eks?"
    print
    removeAll(input)

    input = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 5
    reverseGroup(input, k)
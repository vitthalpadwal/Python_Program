'''
0) li = [fc,dc,fd,gr]
def myfun(myli = none):
  _myli - myli
  _myli.pop(-1)

What will be the way to take a precaution for above example like abc or decorator?


if you calling this function 10 times what will be happen?
'''
#this question is like handling exception for indexing or poping non existence element using decorator or abc
import operator
def decorator(func):
    def newValueOf(list):
        if len(list) == 0:
            print("Oops! Array index is out of range")
            return
        func(list)

    return newValueOf


li = ['fc', 'dc', 'fd', 'gr']

@decorator
def myfun(li1=None):
    _myli = li1
    print(_myli.pop(-1))

for i in range(10):
    myfun(li)


'''for editing the file in python'''
#!/usr/bin/env python3
import fileinput

with fileinput.FileInput("filename", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("text_to_search", "replacement_text"), end='')


def reverseWords(input):
    # split words of string separated by space
    inputWords = input.split(" ")

    # reverse list of words
    # suppose we have list of elements list = [1,2,3,4],
    # list[0]=1, list[1]=2 and index -1 represents
    # the last element list[-1]=4 ( equivalent to list[3]=4 )
    # So, inputWords[-1::-1] here we have three arguments
    # first is -1 that means start from last element
    # second argument is empty that means move to end of list
    # third arguments is difference of steps
    inputWords = inputWords[-1::-1]

    # now join words with space
    output = ' '.join(inputWords)

    return output

#other way
def reverseTheWord(input):
    input = input.split()
    for i in range(len(input)-1, -1, -1):
        print(input[i], sep=" ", end=" ")

str = "third arguments is difference of steps"
str =str.split()
print(str[::-1])
#or
print(str[-1::-1])


# file sumtree.py
def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
        else:
            tot += sumtree(x) # Recur for sublists
    return tot

def sumtree(L): # Breadth-first, explicit queue
    tot = 0
    items = list(L) # Start with copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items.extend(front) # <== Append all in nested list
    return tot

def sumtree(L): # Depth-first, explicit stack
    tot = 0
    items = list(L) # Start with copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items[:0] = front # <== Prepend all in nested list
    return tot

#for any element of the list calculate the diff of the sum of all the elments on the left side of
# the element and right of the element. And then return the lowest diff index
def accumulate():
    num_list = [1, 2, 3]
    #accu_sum = list(map(operator.add, accu_sum[1:], accu_sum[:-1]))
    accu_sum = [sum(num_list[:y]) for y in range(1, len(num_list) + 1)]
    calc_diff =  list(map(operator.sub, accu_sum[1:], accu_sum[:-1]))
    print("accumulated list = ", accu_sum)
    print("diff of each accumulate element", calc_diff)
    print("Index of minimum value is = ", calc_diff.index(min(calc_diff)))


# Python program to find if there are
# two elements wtih given sum

# function to check for the given sum
# in the array
def printPairs(arr, arr_size, sum):
    # Create an empty hash set
    s = set()

    for i in range(0, arr_size):
        temp = sum - arr[i]
        if (temp >= 0 and temp in s):
            print("Pair with the given sum is", arr[i], "and", temp)
        s.add(arr[i])


# Python3 program to print the
# sum of the consecutive elements.

# Function to print alternate sum
def pairwiseSum(lst, n):
    sum = 0;
    for i in range(len(lst) - 1):
        # adding the alternate numbers
        sum = lst[i] + lst[i + 1]
        print(sum, end=" ")


# Python 3 program to print the absolute
# difference of the consecutive elements

# Function to print pairwise absolute
# difference of consecutive elements
def pairwiseDifference(arr, n):
    for i in range(n - 1):
        # absolute difference between
        # consecutive numbers
        diff = abs(arr[i] - arr[i + 1])
        print(diff, end=" ")


#sum of theleft hand and right and element and diff it
def lefthand_righthand():
    list = [2,4,5]
    lefthand = 0
    righthand = 0
    list1 = []
    for i in range(len(list)):
        lefthand = sum(list[:i])
        print("lefthand", lefthand)
        righthand = sum(list[i+1:])
        print("righthand", righthand)
        diff = abs(lefthand - righthand)
        list1.append(diff)

    print(list1)
    print("index of the minimum element",list1.index(min(list1)))
# driver program to check the above function
if __name__ == "__main__":
    '''
    input = 'geeks quiz practice ' \
            'code'
    print(reverseWords(input))
    reverseTheWord(input)
    L = [1, [2, [3, 4], 5], 6, [7, 8]]  # Arbitrary nesting
    print(sumtree(L))  # Prints 36
    # Pathological cases
    print(sumtree([1, [2, [3, [4, [5]]]]]))  # Prints 15 (right-heavy)
    print(sumtree([[[[[1], 2], 3], 4], 5]))  # Prints 15 (left-heavy)
    accumulate()
    A = [1, 4, 45, 6, 10, 8]
    n = 16
    printPairs(A, len(A), n)
    # consecutive pair sum
    arr = [4, 10, 15, 5, 6]
    size = len(arr)
    pairwiseSum(arr, size)

    #consecutive differences
    arr = [4, 10, 15, 5, 6]
    n = len(arr)
    pairwiseDifference(arr, n)
    '''
    lefthand_righthand()


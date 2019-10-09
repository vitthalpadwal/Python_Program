"""
We define the following:

A subarray of array  of length  is a contiguous segment from  through  where .
The sum of an array is the sum of its elements.
Given an  element array of integers, , and an integer, , determine the maximum value of the sum of any of its subarrays modulo . For example, Assume  and . The following table lists all subarrays and their moduli:

		sum	%2
[1]		1	1
[2]		2	0
[3]		3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
The maximum modulus is .

Function Description

Complete the maximumSum function in the editor below. It should return a long integer that represents the maximum value of .

maximumSum has the following parameter(s):

a: an array of long integers, the array to analyze
m: a long integer, the modulo divisor
Input Format

The first line contains an integer , the number of queries to perform.

The next  pairs of lines are as follows:

The first line contains two space-separated integers  and (long), the length of  and the modulo divisor.
The second line contains  space-separated long integers .
Constraints

 the sum of  over all test cases
Output Format

For each query, return the maximum value of  as a long integer.

Sample Input

1
5 7
3 3 9 9 5
Sample Output

6
Explanation

The subarrays of array  and their respective sums modulo  are ranked in order of length and sum in the following list:

 and
 and






The maximum value for  for any subarray is .
"""

"""
The bisect module implements an algorithm for inserting elements into a list while maintaining the list in sorted order.

Inserting in Sorted Order
Here is a simple example in which insort() is used to insert items into a list in sorted order.

bisect_example.py
import bisect

# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3}  {:3}'.format(i, position), l)
The first column of the output shows the new random number. The second column shows the position where the number will be inserted into the list. The remainder of each line is the current sorted list.

$ python3 bisect_example.py

New  Pos  Contents
---  ---  --------
 14    0 [14]
 85    1 [14, 85]
 77    1 [14, 77, 85]
 26    1 [14, 26, 77, 85]
 50    2 [14, 26, 50, 77, 85]
 45    2 [14, 26, 45, 50, 77, 85]
 66    4 [14, 26, 45, 50, 66, 77, 85]
 79    6 [14, 26, 45, 50, 66, 77, 79, 85]
 10    0 [10, 14, 26, 45, 50, 66, 77, 79, 85]
  3    0 [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
 84    9 [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
 77    8 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
  1    0 [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
This is a simple example,. In fact, given the amount of data being manipulated, it might be faster to simply build the list and then sort it once. By contrast, for long lists, significant time and memory savings can be achieved using an insertion sort algorithm such as this, especially when the operation to compare two members of the list requires expensive computation.

Handling Duplicates
The result set shown previously includes a repeated value, 77. The bisect module provides two ways to handle repeats: New values can be inserted either to the left of existing values, or to the right. The insort() function is actually an alias for insort_right(), which inserts an item after the existing value. The corresponding function insort_left() inserts an item before the existing value.

bisect_example2.py
import bisect

# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  --------')

# Use bisect_left and insort_left.
l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3}  {:3}'.format(i, position), l)
When the same data is manipulated using bisect_left() and insort_left(), the results are the same sorted list but the insert positions are different for the duplicate values.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumSum function below.
from bisect import insort, bisect_right
def maximumSum(a, m):
    # [edit: calculate prefix as you go..]
    calculate_prefix = lambda cur, prev: (prev + (cur % m)) % m

    # [edit] Compute max modsum
    cur_prefix = calculate_prefix(a[0], 0)
    pq = [cur_prefix]
    maxmodsum = cur_prefix
    for i in range(1, len(a)):
        # [edit] Find cheapest prefix larger than prefix[i]
        cur_prefix = calculate_prefix(a[i], cur_prefix)
        left = bisect_right(pq, cur_prefix)
        if left != len(pq):
            # [edit] Update maxmodsum if possible
            modsum = max(cur_prefix, (cur_prefix - pq[left] + m) % m)
        else:
            modsum = cur_prefix
        maxmodsum = max(maxmodsum, modsum)

        # add current prefix to heap
        insort(pq, cur_prefix)

    return maxmodsum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

"""
A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't rearrange characters and ABCD  ABDC.

Function Description

Complete the commonChild function in the editor below. It should return the longest string which is a common child of the input strings.

commonChild has the following parameter(s):

s1, s2: two equal length strings
Input Format

There is one line with two space-separated strings,  and .

Constraints

All characters are upper case in the range ascii[A-Z].
Output Format

Print the length of the longest string , such that  is a child of both  and .

Sample Input

HARRY
SALLY
Sample Output

 2
Explanation

The longest string that can be formed by deleting zero or more characters from  and  is , whose length is 2.

Sample Input 1

AA
BB
Sample Output 1

0
Explanation 1

 and  have no characters in common and hence the output is 0.

Sample Input 2

SHINCHAN
NOHARAAA
Sample Output 2

3
Explanation 2

The longest string that can be formed between  and  while maintaining the order is .

Sample Input 3

ABCDEF
FBDAMN
Sample Output 3

2
Explanation 3
 is the longest child of the given strings.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

# Complete the commonChild function below.
def commonChild(s1, s2):
    dict = OrderedDict.fromkeys(s1, 5)
    dict1 = OrderedDict.fromkeys(s2, 10)
    print(dict)
    print(dict1)
    count =0
    list1 = dict1.keys()
    list2 = dict.keys()
    breakpoint()
    for i in list2:
        print(i)
        if i in list1:
            count +=1
    print(count)
    return count

if __name__ == '__main__':
    fptr = open('OUTPUT_PATH', 'w')

    s1 = "OUDFRMYMAW"
    #input()

    s2 = "AWHYFCCMQX" #input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(a, b):
    lengths = [[0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = \
                    max(lengths[i + 1][j], lengths[i][j + 1])

    return lengths[-1][-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

"""
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the th attribute and print the final resulting table. Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .

Constraints



Each element

Output Format

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input 0

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output 0

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation 0

The details are sorted based on the second attribute, since  is zero-indexed.
"""

# !/bin/python
'''
from __future__ import print_function
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    k = int(raw_input())

    arr.sort(key=lambda x:x[1][k])

    for i in range(N):
        for j in range(M):
            print(i[1][j])
'''
from __future__ import print_function
from collections import defaultdict, OrderedDict

I = map(int, raw_input().split())
D = OrderedDict()
for i in xrange(I[0]): D[i] = map(int, raw_input().split())
K = input()
k = sorted(D.items(), key=lambda x: x[1][K])

for i in k:
    print(*i[1])



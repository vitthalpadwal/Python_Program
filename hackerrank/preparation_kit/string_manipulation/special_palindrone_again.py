"""
A string is said to be a special palindromic string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special palindromic substring is any substring of a string which meets one of those criteria. Given a string, determine how many special palindromic substrings can be formed from it.

For example, given the string , we have the following special palindromic substrings: .

Function Description

Complete the substrCount function in the editor below. It should return an integer representing the number of special palindromic substrings that can be formed from the given string.

substrCount has the following parameter(s):

n: an integer, the length of string s
s: a string
Input Format

The first line contains an integer, , the length of .
The second line contains the string .

Constraints


Each character of the string is a lowercase alphabet, .

Output Format

Print a single line containing the count of total special palindromic substrings.

Sample Input 0

5
asasd
Sample Output 0

7
Explanation 0

The special palindromic substrings of  are

Sample Input 1

7
abcbaba
Sample Output 1

10
Explanation 1

The special palindromic substrings of  are

Sample Input 2

4
aaaa
Sample Output 2

10
Explanation 2

The special palindromic substrings of  are

Python 3
"""

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    count = len(s)
    for i, char in enumerate(s):
        diff_char_idx = None
        for j in range(i + 1, n):
            if char == s[j]:
                if diff_char_idx is None:
                    count += 1
                elif j - diff_char_idx == diff_char_idx - i:
                    count += 1
                    break
            else:
                if diff_char_idx is None:
                    diff_char_idx = j
                else:
                    break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

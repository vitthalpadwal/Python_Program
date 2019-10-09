"""
Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. For example, if your string is "bcbc", you can either remove 'b' at index  or 'c' at index . If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Function Description

Complete the palindromeIndex function in the editor below. It must return the index of the character to remove or .

palindromeIndex has the following parameter(s):

s: a string to analyze
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a query string .

Constraints

All characters are in the range ascii[a-z].
Output Format

Print an integer denoting the zero-indexed position of the character to remove to make  a palindrome. If  is already a palindrome or no such character exists, print .

Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
Explanation

Query 1: "aaab"
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 2: "baa"
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 3: "aaa"
This string is already a palindrome, so we print . Removing any one of the characters would result in a palindrome, but this test comes first.

Note: The custom checker logic for this challenge is available here.

"""


t = int(input())


def is_palindrome(s):
    return s == s[::-1]


def solve(s):
    i, j = 0, len(s) - 1
    while (i < j) and (s[i] == s[j]):
        i += 1
        j -= 1
    if i == j:
        return 0
    if is_palindrome(s[i + 1 : j + 1]):
        return i
    if is_palindrome(s[i:j]):
        return j
    raise AssertionError

for _ in range(t):
    print(solve(input()))
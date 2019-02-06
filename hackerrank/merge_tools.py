"""
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Input Format

The first line contains a single string denoting .
The second line contains an integer, , denoting the length of each subsegment.

Constraints

, where  is the length of
It is guaranteed that  is a multiple of .
Output Format

Print  lines where each line  contains string .

Sample Input

AABCAAADA
3
Sample Output

AB
CA
AD
Explanation

String  is split into  equal parts of length . We convert each  to  by removing any subsequent occurrences non-distinct characters in :

We then print each  on a new line.
"""
'''
>>> import re
>>> re.findall('...','XXXxxxXXXxxxXXXxxxXXXxxxXXX')
['XXX', 'xxx', 'XXX', 'xxx', 'XXX', 'xxx', 'XXX', 'xxx', 'XXX']

>>> chunksize=3
>>> re.findall('.{%s}'%chunksize,'XXXxxxXXXxxxXXXxxxXXXxxxXXX')
['XXX', 'xxx', 'XXX', 'xxx', 'XXX', 'xxx', 'XXX', 'xxx', 'XXX']
'''


def merge_the_tools(string, k):
    # your code goes here
    s = [string[i:i + k] for i in range(0, len(string), k)]

    for str in s:
        unique = ''
        for i in str:
            if i not in unique:
                unique += i
        print(unique)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
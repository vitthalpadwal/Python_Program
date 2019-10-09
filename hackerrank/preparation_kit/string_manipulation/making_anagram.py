"""
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

For example, if  and , we can delete  from string  and  from string  so that both remaining strings are and  which are anagrams.

Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.

makeAnagram has the following parameter(s):

a: a string
b: a string
Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.
"""

'''
a = input()
b = input()
cnt = [0] * 26
offset = ord('a')
for char in a:
	cnt[ord(char) - offset] += 1
for char in b:
	cnt[ord(char) - offset] -= 1
total = 0
for value in cnt:
	total += abs(value)
print(total)
'''


# !/usr/bin/py
def buildMap(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] += 1

    return the_map


def anagram(s1, s2):
    map1 = buildMap(s1)
    map2 = buildMap(s2)

    diff_cnt = 0
    for key in map2.keys():
        if key not in map1:
            diff_cnt += map2[key]
        else:
            diff_cnt += max(0, map2[key] - map1[key])

    for key in map1.keys():
        if key not in map2:
            diff_cnt += map1[key]
        else:
            diff_cnt += max(0, map1[key] - map2[key])

    return diff_cnt


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(anagram(s1, s2))
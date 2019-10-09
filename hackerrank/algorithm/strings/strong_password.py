"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Input Format

The first line contains an integer  denoting the length of the string.

The second line contains a string consisting of  characters, the password typed by Louise. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints

Output Format

Print a single line containing a single integer denoting the answer to the problem.

Sample Input 0

3
Ab1
Sample Output 0

3
Explanation 0

She can make the password strong by adding  characters, for example, $hk, turning the password into Ab1$hk which is strong.

 characters aren't enough since the length must be at least .

Sample Input 1

11
#HackerRank
Sample Output 1

1
Explanation 1


"""

# !/bin/python3

import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    add = 0
    if all(n not in password for n in numbers):
        add += 1

    if all(l not in password for l in lower_case):
        add += 1

    if all(u not in password for u in upper_case):
        add += 1
    if all(s not in password for s in special_characters):
        add += 1

    return add + max(0, 6 - len(password) - add)


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)

'''
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
input()
s=input()
ans = 0
found = any(i in numbers for i in s)
if not found:
    ans += 1
    s += "0"
found = any(i in lower_case for i in s)
if not found:
    ans += 1
    s += 'a'
found = any(i in upper_case for i in s)
if not found:
    ans += 1
    s += 'A'
found = any(i in special_characters for i in s)
if not found:
    ans += 1
    s += '!'
if len(s) < 6:
    ans += 6 - len(s)
print(ans)
'''
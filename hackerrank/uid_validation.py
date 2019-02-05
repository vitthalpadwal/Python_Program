"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
"""
import re

def uid_validation(uid):
    upper = r'.*([A-Z].*){2,}'
    digit = r'.*([0-9].*){3,}'
    alpha = r'([A-Za-z0-9]){10}$'
    unique =  r'.*(.).*\1'

    upper_result = bool(re.match(upper, uid))
    digit_result = bool(re.match(digit, uid))
    alpha_result = bool(re.match(alpha, uid))
    unique_result = bool(re.match(unique, uid))

    if upper_result and digit_result and alpha_result and not unique_result:
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        uid = input().strip()
        uid_validation(uid)
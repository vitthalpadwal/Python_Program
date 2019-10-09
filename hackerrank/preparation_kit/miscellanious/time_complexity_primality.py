"""
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given  integers, determine the primality of each integer and print whether it is Prime or Not prime on a new line.

Note: If possible, try to come up with an  primality algorithm, or see what sort of optimizations you can come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Function Description

Complete the primality function in the editor below. It should return Prime if  is prime, or Not prime.

primality has the following parameter(s):

n: an integer to test for primality
Input Format

The first line contains an integer, , denoting the number of integers to check for primality.
Each of the  subsequent lines contains an integer, , the number you must test for primality.

Constraints

Output Format

For each integer, print whether  is Prime or Not prime on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

We check the following  integers for primality:

 is divisible by numbers other than  and itself (i.e.: , , , ), so we print Not prime on a new line.
 is only divisible  and itself, so we print Prime on a new line.
 is only divisible  and itself, so we print Prime on a new line.
"""

'''
import math
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
'''

import math

def sieve_for_a_single_number(n):
    # arr = []
    # for a in range(2, n + 1):
    #     arr.append(a)

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


p = int(input())
for l in range(p):
    n = int(input())
    if n == 1:
        print("Not prime")
        continue
    # sieve_of_ertosthense(n)
    ans = sieve_for_a_single_number(n)
    if ans: print("Prime")
    else: print("Not prime")
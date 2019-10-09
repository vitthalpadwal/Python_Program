"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following
specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print(int((M-3*i)/2)*'-'+(i*'.|.')+int((M-3*i)/2)*'-')
print(int((M-7)/2)*'-'+'WELCOME'+int((M-7)/2)*'-')
for i in range(N-2,-1,-2):
    print(int((M-3*i)/2)*'-'+(i*'.|.')+int((M-3*i)/2)*'-')
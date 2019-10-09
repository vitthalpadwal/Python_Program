"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros . Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be .

Python 3



"""

# # !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# # Complete the arrayManipulation function below.
# def arrayManipulation(n, queries):
#     if n >= 3 and n <= 10 ** 7 and m >= 1 and m <= 2 * (10 ^ 5):
#         arr = []
#         for r in range(n):
#             arr.append(int(0))
#
#         for q in queries:
#             if q != '':
#                 a = q[0]
#                 b = q[1]
#                 c = q[2]
#                 if a >= 1 and a <= b and b <= n and c >= 0 and c <= 10 ** 9:
#                     a = a - 1
#                     b = b - 1
#                     for j in range(a, b + 1):
#                         arr[j] = arr[j] + c
#                     print(arr)
#
#         output = 0
#
#         for a in arr:
#             if a > output:
#                 output = a
#
#         return output
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     queries = []
#
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = arrayManipulation(n, queries)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


from collections import defaultdict

sums = defaultdict(int)
_, n_ranges = (int(x) for x in input().split())

for _ in range(n_ranges):
    start, stop, value = (int(x) for x in input().split())
    sums[start] += value
    sums[stop+1] -= value

max_val = running_val = 0
for _, val in sorted(sums.items()):
    running_val += val
    max_val = max(max_val, running_val)

print(max_val)
"""
There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Constraints



Output Format

For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input

2
6
4 3 2 1 3 4
3
1 3 2
Sample Output

Yes
No
Explanation

In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .


"""

from collections import deque
if __name__ == "__main__":
    for i  in range(int(input())):
        cubes = int(input())
        dq = deque(map(int, input().split()))
        result = True
        element = (2**31)+1
        while dq:
            left = dq[0]
            right = dq[-1]
            if left >= right and element >= left:
                element = dq.popleft()
            elif right >= left and element >= right:
                element = dq.pop()
            else:
                result = False
                break
        if result:
            print('Yes')
        else:
            print('No')
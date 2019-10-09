"""
You are given a square grid with some cells open (.) and some blocked (X). Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell. Given a grid, a start and an end position, determine the number of moves it will take to get to the end position.

For example, you are given a grid with sides  described as follows:

...
.X.
...
Your starting position  so you start in the top left corner. The ending position is . The path is . It takes  moves to get to the goal.

Function Description
Complete the minimumMoves function in the editor. It must print an integer denoting the minimum moves required to get from the starting position to the goal.

minimumMoves has the following parameter(s):

grid: an array of strings representing the rows of the grid
startX: an integer
startY: an integer
goalX: an integer
goalY: an integer
Input Format

The first line contains an integer , the size of the array grid.
Each of the next  lines contains a string of length .
The last line contains four space-separated integers,

Constraints

Output Format

Print an integer denoting the minimum number of steps required to move the castle to the goal position.

Sample Input

3
.X.
.X.
...
0 0 0 2
Sample Output

3
Explanation

Here is a path that one could follow in order to reach the destination in  steps:

.
"""


def getN(c, n):
    j = c[0]
    i = c[1]
    r = []
    m = [j, i]
    while m[1] + 1 < n and g[m[0]][m[1] + 1] != "X":
        m[1] += 1
        if m != c:
            r.append([m[0], m[1]])

    m = [j, i]
    while m[1] - 1 >= 0 and g[m[0]][m[1] - 1] != "X":
        m[1] -= 1
        if m != c:
            r.append([m[0], m[1]])

    m = [j, i]
    while m[0] + 1 < n and g[m[0] + 1][m[1]] != "X":
        m[0] += 1
        if m != c:
            r.append([m[0], m[1]])

    m = [j, i]
    while m[0] - 1 >= 0 and g[m[0] - 1][m[1]] != "X":
        m[0] -= 1
        if m != c:
            r.append([m[0], m[1]])

    return r


n = int(input())
g = []
for i in range(n):
    temp = input()
    row = [char for char in temp]
    g.append(row)

temp = [int(i) for i in input().split()]
start = [temp[0], temp[1]]
end = [temp[2], temp[3]]

v = []
for i in range(n):
    v.append([False] * n)

d = []
for i in range(n):
    d.append([n ** 3] * n)

d[start[0]][start[1]] = 0
q = []
q.append(start)
done = False
while q != [] and not done:
    c = q.pop(0)
    v[c[0]][c[1]] = True
    u = getN(c, n)
    for x in u:
        if v[x[0]][x[1]] == False:
            d[x[0]][x[1]] = d[c[0]][c[1]] + 1
            v[x[0]][x[1]] = True
            q.append(x)
        if x == end:
            done = True

print(d[end[0]][end[1]])








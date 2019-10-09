"""
Consider a matrix where each cell contains either a  or a  and any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the diagram below, the two colored regions show cells connected to the filled cells. Black on white are not connected.

Cells adjacent to filled cells:  image

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Regions:  image

Given an  matrix, find and print the number of cells in the largest region in the matrix.

Function Description

Complete the function maxRegion in the editor below. It must return an integer value, the size of the largest region.

maxRegion has the following parameter(s):

grid: a two dimensional array of integers
Input Format

The first line contains an integer, , the number of rows in the matrix, .
The second line contains an integer, , the number of columns in the matrix.

Each of the following  lines contains a row of  space-separated integers, .

Constraints

Output Format

Print the number of cells in the largest region in the given matrix.

Sample Input

4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output

5
Explanation

The diagram below depicts two regions of the matrix:

image
The first region has five cells and the second region has one cell. We choose the larger region.
"""


def getBiggestRegion(grid):
    largest = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count = 0
            nodes = []
            if grid[i][j]:
                nodes = [(i, j)]
            while len(nodes) > 0:
                n = nodes.pop()
                if not grid[n[0]][n[1]]:
                    continue
                grid[n[0]][n[1]] = 0

                count += 1

                if n[0] - 1 >= 0 and grid[n[0] - 1][n[1]]:
                    nodes.append((n[0] - 1, n[1]))
                if n[1] - 1 >= 0 and grid[n[0]][n[1] - 1]:
                    nodes.append((n[0], n[1] - 1))
                if n[1] + 1 < len(grid[n[0]]) and grid[n[0]][n[1] + 1]:
                    nodes.append((n[0], n[1] + 1))
                if n[0] + 1 < len(grid) and grid[n[0] + 1][n[1]]:
                    nodes.append((n[0] + 1, n[1]))

                if n[0] - 1 >= 0 and n[1] - 1 >= 0 and grid[n[0] - 1][n[1] - 1]:
                    nodes.append((n[0] - 1, n[1] - 1))
                if n[0] - 1 >= 0 and n[1] + 1 < len(grid[n[0]]) and grid[n[0] - 1][n[1] + 1]:
                    nodes.append((n[0] - 1, n[1] + 1))
                if n[0] + 1 < len(grid) and n[1] - 1 >= 0 and grid[n[0] + 1][n[1] - 1]:
                    nodes.append((n[0] + 1, n[1] - 1))
                if n[0] + 1 < len(grid) and n[1] + 1 < len(grid[n[0]]) and grid[n[0] + 1][n[1] + 1]:
                    nodes.append((n[0] + 1, n[1] + 1))
            if count > largest:
                largest = count
    return largest


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
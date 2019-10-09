"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers .
Input Format

The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x

Python 3


"""

N=int(input())
grid=[]
for i in range(0,N):
    lists=[int(i) for i in input().split()]
    grid.append(lists)
count=0
sum1=0
sum2=0
j1=0
j2=N-1
while(count<N):
    sum1=sum1+grid[count][j1]
    sum2=sum2+grid[count][j2]
    count+=1
    j1+=1
    j2-=1
print(abs(sum1-sum2))

'''
#other example 
size=int(input())
thematrix=[]
firstdiag=[]
seconddiag=[]
for i in range(size):
    line = input().strip().split(' ')
    line=[int(j) for j in line]
    thematrix.append(line)
for i in range(size):
    firstdiag.append(thematrix[i][i])
    seconddiag.append(thematrix[i][(size-1)-i])
print(abs(sum(firstdiag)-sum(seconddiag)))
'''

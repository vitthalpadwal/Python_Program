# Python code to swap the element
# of first and last row and display
# the result

def interchangeFirstLast(mat, n, m):
    rows = n

    # swapping of element between
    # first and last rows
    for i in range(n):
        t = mat[0][i]
        mat[0][i] = mat[rows - 1][i]
        mat[rows - 1][i] = t

    # Driver Program


mat = [[8, 9, 7, 6],
       [4, 7, 6, 5],
       [3, 2, 1, 8],
       [9, 9, 7, 7]]

n = 4
m = 4
interchangeFirstLast(mat, n, m)

# printing the interchanged matrix
for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print("\n")

    # This code is contributed by Shrikant13.

#password validation
# importing re library
import re


def main():
    passwd = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwd)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")

    # Driver Code


# function to remove all consecutive duplicates
# from the string in Python

from itertools import groupby


def removeAllConsecutive(input):
    # group all consecutive characters based on their
    # order in string and we are only concerned
    # about first character of each consecutive substring
    # in given string, so key value will work for us
    # and we will join these keys without space to
    # generate resultant string
    result = []
    for (key, group) in groupby(input):
        result.append(key)

    print(''.join(result))


# Python 3 program to print a rectangular
# pattern


def printRectangle(h, w):
    for i in range(0, h):
        print("")
        for j in range(0, w):
            # Print @ if this is first row
            # or last row. Or this column
            # is first or last.
            if (i == 0 or i == h - 1 or j == 0 or j == w - 1):
                print("@", end="")
            else:
                print(" ", end="")


# Python 3 program to print hollow
# square star pattern with diagonal

# Function to print hollow square with
# primary and secondary diagonal
def print_squaredi(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (i == 1 or i == n or j == 1 or j == n
                    or i == j or j == (n - i + 1)):
                print("*", end="")
            else:
                print(" ", end="")

        print()


# Python 3 program to change value of
# diagonal elements of a matrix to 0.
MAX = 100


# to print the resultant matrix
def print_1(mat, n, m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")

        print()

    # function to change the values


# of diagonal elements to 0
def makediagonalzero(mat, n, m):
    for i in range(n):
        for j in range(m):

            # right and left diagonal condition
            if (i == j or (i + j + 1) == n):
                mat[i][j] = 0

    # print resultant matrix
    print_1(mat, n, m)


# Python Program to implement matrix
# for swapping the upper diagonal
# elements with lower diagonal
# elements of matrix.

# Function to swap the diagonal
# elements in a matrix.
def swapUpperToLower(arr):
    n = 4;

    # Loop for swap the elements
    # of matrix.
    for i in range(0, n):
        for j in range(i + 1, n):
            temp = arr[i][j];
            arr[i][j] = arr[j][i];
            arr[j][i] = temp;

            # Loop for print the matrix elements.
    for i in range(0, n):
        for j in range(0, n):
            print(arr[i][j], end=" ");
        print(" ");

def tanspose_matrix():
    matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    for row in matrix:
        print(row)
    print("\n")
    t_matrix = zip(*matrix)
    for row in t_matrix:
        print(row)

    # Python3 program to check whether a given
    # matrix is magic matrix or not
    N = 3

    # Returns true if mat[][] is magic
    # square, else returns false.
    def isMagicSquare(mat):

        # calculate the sum of
        # the prime diagonal
        s = 0
        for i in range(0, N):
            s = s + mat[i][i]

            # For sums of Rows
        for i in range(0, N):
            rowSum = 0;
            for j in range(0, N):
                rowSum += mat[i][j]

                # check if every row sum is
            # equal to prime diagonal sum
            if (rowSum != s):
                return False

        # For sums of Columns
        for i in range(0, N):
            colSum = 0
            for j in range(0, N):
                colSum += mat[j][i]

                # check if every column sum is
            # equal to prime diagonal sum
            if (s != colSum):
                return False

        return True

        # Driver code
if __name__ == "__main__":
    n = 3
    m = 4
    mat = [[2, 1, 7],
           [3, 7, 2],
           [5, 4, 9]]

    makediagonalzero(mat, n, m)
    #input = 'aaaaabbbbbb'
    #removeAllConsecutive(input)
    #main()
    #h = 4
    #w = 5
    #printRectangle(h, w)
    #rows = 8
    #print_squaredi(rows)

    arr = [[2, 3, 5, 6], [4, 5, 7, 9],
           [8, 6, 4, 9], [1, 3, 5, 6]];

    # Function call
    swapUpperToLower(arr);

    mat = [[2, 7, 6],
           [9, 5, 1],
           [4, 3, 8]]

    if (isMagicSquare(mat)):
        print("Magic Square")
    else:
        print("Not a magic Square")
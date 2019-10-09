"""
A  Crossword grid is provided to you, along with a set of words (or names of places) which need to be filled into the grid. Cells are marked either + or -. Cells marked with a - are to be filled with the word list.

The following shows an example crossword from the input  grid and the list of words to fit, :

Input 	   		Output

++++++++++ 		++++++++++
+------+++ 		+POLAND+++
+++-++++++ 		+++H++++++
+++-++++++ 		+++A++++++
+++-----++ 		+++SPAIN++
+++-++-+++ 		+++A++N+++
++++++-+++ 		++++++D+++
++++++-+++ 		++++++I+++
++++++-+++ 		++++++A+++
++++++++++ 		++++++++++
POLAND;LHASA;SPAIN;INDIA
Function Description

Complete the crosswordPuzzle function in the editor below. It should return an array of strings, each representing a row of the finished puzzle.

crosswordPuzzle has the following parameter(s):

crossword: an array of  strings of length  representing the empty grid
words: a string consisting of semicolon delimited strings to fit into
Input Format

Each of the first  lines represents , each of which has  characters, .

The last line contains a string consisting of semicolon delimited  to fit.

Constraints




Output Format

Position the words appropriately in the  grid, then return your array of strings for printing.

Sample Input 0

+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA
Sample Output 0

+L++++++++
+O++++++++
+N++++++++
+DELHI++++
+O+++C++++
+N+++E++++
+++++L++++
++ANKARA++
+++++N++++
+++++D++++
Sample Input 1

+-++++++++
+-++++++++
+-------++
+-++++++++
+-++++++++
+------+++
+-+++-++++
+++++-++++
+++++-++++
++++++++++
AGRA;NORWAY;ENGLAND;GWALIOR
Sample Output 1

+E++++++++
+N++++++++
+GWALIOR++
+L++++++++
+A++++++++
+NORWAY+++
+D+++G++++
+++++R++++
+++++A++++
++++++++++
Sample Input 2

XXXXXX-XXX
XX------XX
XXXXXX-XXX
XXXXXX-XXX
XXX------X
XXXXXX-X-X
XXXXXX-X-X
XXXXXXXX-X
XXXXXXXX-X
XXXXXXXX-X
ICELAND;MEXICO;PANAMA;ALMATY
Sample Output 2

XXXXXXIXXX
XXMEXICOXX
XXXXXXEXXX
XXXXXXLXXX
XXXPANAMAX
XXXXXXNXLX
XXXXXXDXMX
XXXXXXXXAX
XXXXXXXXTX
XXXXXXXXYX
"""

import sys


def printBoard(board):
    for row in board:
        print(''.join(row))


def possibleDirections(board, word):
    length = len(word)

    for i in range(10):
        for j in range(10):

            properSlotH = True
            properSlotV = True

            for k in range(length):
                # Horizontal direction, axis marked as 0:
                if j < 10 - length + 1:
                    if board[i][j + k] not in ['-', word[k]]:
                        properSlotH = False

                # Vertival direction, axis marked as 1:
                if i < 10 - length + 1:
                    if board[i + k][j] not in ['-', word[k]]:
                        properSlotV = False

            if properSlotH and j < 10 - length + 1:
                yield (i, j, 0)
            if properSlotV and i < 10 - length + 1:
                yield (i, j, 1)


def move(board, word, startLocation):
    i, j, axis = startLocation
    length = len(word)
    if axis == 0:
        for k in range(length):
            board[i][j + k] = word[k]
    else:
        for k in range(length):
            board[i + k][j] = word[k]


def rollback(board, word, startLocation):
    i, j, axis = startLocation
    length = len(word)
    if axis == 0:
        for k in range(length):
            board[i][j + k] = '-'
    else:
        for k in range(length):
            board[i + k][j] = '-'


def solve(board, words):
    global solved
    if len(words) == 0:
        if not solved:
            printBoard(board)
        solved = True
        return

    word = words.pop()

    for direction in possibleDirections(board, word):
        move(board, word, direction)
        solve(board, words)
        rollback(board, word, direction)

    words.append(word)


if __name__ == '__main__':
    board = []
    for _ in range(10):
        board_item = list(input())
        board.append(board_item)

    words = str(input()).split(";")
    solved = False

    solve(board, words)

"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Output Format

Print the alphabet rangoli in the format explained above.

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


def print_rangoli(n):
    # your code goes here
    w = (n - 1) * 2 + ((n * 2) - 1)
    # upper half
    for i in range(1, n, 1):
        number_of_letter = (i * 2) - 1
        s = ''
        letter_value = 97 + n - 1
        for i in range(0, number_of_letter):
            if (i != 0):
                s += '-'
            s += chr(letter_value)
            if (i < (number_of_letter - 1) / 2):
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1
        print(s.center(w, '-'))

    # bottom half
    for i in range(n, 0, -1):
        number_of_letter = (i * 2) - 1
        s = ''
        letter_value = 97 + n - 1
        for i in range(0, number_of_letter):
            if (i != 0):
                s += '-'
            s += chr(letter_value)
            if (i < (number_of_letter - 1) / 2):
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1
        print(s.center(w, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
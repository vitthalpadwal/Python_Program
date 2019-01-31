#Find length of longest subsequence of one string which is substring of another string

# Python3 program to find maximum
# length of subsequence of a string
# X such it is substring in another
# string Y.

MAX = 10


# Return the maximum size of
# substring of X which is
# substring in Y.
def maxSubsequenceSubstring(x, y, n, m):

    dp = [[0 for i in range(MAX)]
          for i in range(MAX)]

    # Initialize the dp[][] to 0.

    # Calculating value for each element.
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If alphabet of string
            # X and Y are equal make
            # dp[i][j] = 1 + dp[i-1][j-1]
            if (x[j - 1] == y[i - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]

                # Else copy the previous value
            # in the row i.e dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j - 1]

                # Finding the maximum length
    print(dp)
    ans = 0
    for i in range(1, m + 1):
        ans = max(ans, dp[i][n])
    return ans


# Driver Code
x = "ABCD"
y = "BACDBDCD"
n = len(x)
m = len(y)
print(maxSubsequenceSubstring(x, y, n, m))

# This code is contributed
# by sahilshelangia

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce(lambda x, y: x + y, li)
print (sum)

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print
"The list printed sorting by age: "
print
sorted(lis, key=lambda i: i['age'])

print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print
"The list printed sorting by age and name: "
print
sorted(lis, key=lambda i: (i['age'], i['name']))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print
"The list printed sorting by age in descending order: "
print
sorted(lis, key=lambda i: i['age'], reverse=True)


# Function calling
def dictionairy():
    # Declaring hash function
    key_value = {}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=
    lambda kv: (kv[1], kv[0])))


def main():
    # function calling
    dictionairy()


# Python Program to find all anagrams of str in
# a list of strings.
from collections import Counter

my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"

# use anonymous function to filter anagrams of x.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/anagram-checking-python-collections-counter/
result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list))

# printing the result
print(result)

# Python Program to find palindromes in
# a list of strings.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]

# use anonymous function to filter palindromes.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

# printing the result
print(result)

# Python Program to find numbers divisible
# by thirteen from a list using anonymous
# function

# Take a list of numbers.
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

# use anonymous function to filter and comparing
# if divisible or not
result = list(filter(lambda x: (x % 13 == 0), my_list))

# printing the result
print(result)



from collections import Counter


def remov_duplicates(input):

    # split input string separated by space
    input = input.split(" ")

    # joins two adjacent elements in iterable way
    for i in range(0, len(input)):
        input[i] = "".join(input[i])

        # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)

    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    print(s)

    # Driver program


# A Naive recursive program to find minimum
# number insertions needed to make a string
# palindrome
import sys


# Recursive function to find minimum
# number of insertions
def findMinInsertions(str, l, h):
    # Base Cases
    if (l > h):
        return sys.maxsize
    if (l == h):
        return 0
    if (l == h - 1):
        return 0 if (str[l] == str[h]) else 1

    # Check if the first and last characters are
    # same. On the basis of the comparison result,
    # decide which subrpoblem(s) to call

    if (str[l] == str[h]):
        return findMinInsertions(str, l + 1, h - 1)
    else:
        return (min(findMinInsertions(str, l, h - 1),
                    findMinInsertions(str, l + 1, h)) + 1)

    # Driver Code


if __name__ == "__main__":
    str = "geeks"
    print(findMinInsertions(str, 0, len(str) - 1))
    input = 'Python is great and Java is also great'
    remov_duplicates(input)
    main()
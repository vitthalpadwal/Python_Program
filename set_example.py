# function to check if two strings are
# anagram or not
def check(s1, s2):
    # the sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # driver code


s1 = "listen"
s2 = "silent"
check(s1, s2)

# Function remove minimum number of characters so that
# two strings become anagram
from collections import Counter


def removeChars(str1, str2):
    # make dictionaries from both strings
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    # extract keys from dict1 and dict2
    keys1 = dict1.keys()
    keys2 = dict2.keys()

    # count number of keys in both lists of keys
    count1 = len(keys1)
    count2 = len(keys2)

    # convert list of keys in set to find common keys
    set1 = set(keys1)
    commonKeys = len(set1.intersection(keys2))

    if (commonKeys == 0):
        return count1 + count2
    else:
        return (max(count1, count2) - commonKeys)

    # Driver program


# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)

if __name__ == "__main__":
    str1 = 'bcadeh'
    str2 = 'hea'
    print
    removeChars(str1, str2)
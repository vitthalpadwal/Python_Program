"""
Python String Function
S.capitalize()                          S.ljust(width [, fill])
S.casefold()                            S.lower()
S.center(width [, fill])                S.lstrip([chars])
S.count(sub [, start [, end]])          S.maketrans(x[, y[, z]])
S.encode([encoding [,errors]])          S.partition(sep)
S.endswith(suffix [, start [, end]])    S.replace(old, new [, count])
S.expandtabs([tabsize])                 S.rfind(sub [,start [,end]])
S.find(sub [, start [, end]])           S.rindex(sub [, start [, end]])
S.format(fmtstr, *args, **kwargs)       S.rjust(width [, fill])
S.index(sub [, start [, end]])          S.rpartition(sep)
S.isalnum()                             S.rsplit([sep[, maxsplit]])
S.isalpha()                             S.rstrip([chars])
S.isdecimal()                           S.split([sep [,maxsplit]])
S.isdigit()                             S.splitlines([keepends])
S.isidentifier()                        S.startswith(prefix [, start [, end]])
S.islower()                             S.strip([chars])
S.isnumeric()                           S.swapcase()
S.isprintable()                         S.title()
S.isspace()                             S.translate(map)
S.istitle()                             S.upper()
S.isupper()                             S.zfill(width)
S.join(iterable)
"""
import re
def remove_duplicate_from_list():
    List = [1,3,4,5,1,2,1,3]
    if List:
        List.sort()
    last = List[-1]
    for i in range(len(List)-2, -1, -1):
        if last==List[i]:
            del List[i]
        else:
            last=List[i]
    print(List)


def remove_duplicate_from_list1():
    List = [1, 3, 4, 5, 1, 2, 1, 3]
    d = {}
    for x in List:
        d[x] = x
    List = d.values()
    print(List)

# count the number of vowels in string
def vowel_count():
    count = 0
    str = "geeksforgeeks"
    for i in str:
        if i in 'aeiou':
            print(i)
            count += 1
    print(count)

# Count vowels in a different way
# Using dictionary
def Check_Vow(string, vowels):
    # casefold has been used to ignore cases
    string = string.casefold()

    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)

    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1
    return count


# python program to check the validaty of the password
def check_validaty(str):
    flag = 0
    while True:
        if len(str) >=6 and len(str) <=12:
            flag=-1
            break
        elif not re.search(r'[a-z]',str):
            flag = -1
            break
        elif not re.search(r'[A-Z]', str):
            flag = -1
            break
        elif not re.search(r'[0-9]', str):
            flag = -1
            break
        elif not re.search(r'[#@!]', str):
            flag = -1
            break
        else:
            flag = 0
            break
    if flag == -1:
        print("password is not valid")


# find the url from given string
# Python code to find the URL from an input string
# Using the regular expression

def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] | [! * \(\),] | (?: %[0-9a-fA-F][0-9a-fA-F]))+',
                     string)
    return url


# Function to Check whether a given string is Heterogram or not

def heterogram(input):
    # separate out list of alphabets using list comprehension
    # ord function returns ascii value of character
    alphabets = [ch for ch in input if (ord(ch) >= ord('a') and ord(ch) <= ord('z'))]

    # convert list of alphabets into set and
    # compare lengths
    if len(set(alphabets)) == len(alphabets):
        print('Yes')
    else:
        print('No')

def palindrome():
    string= "malayalam"
    rev = str(string[::-1])
    print(rev)
    if string == rev:
        print("Palindrome")
    else:
        print("Not palindrome")


# function to check if small string is
# there in big string
def check(string, sub_str):
    if (string.find(sub_str) == -1):
        print("NO")
    else:
        print("YES")


#remove the character from if string it is present in second string
def remove_chr(string1, string2):
    print("string1=", string1, "string2=", string2)
    for i in string1:
        if i in string2:
            print(i)
            string1=string1.replace(i,'')
    print("After removing the string", string1)

if __name__ == "__main__":
    #remove_duplicate_from_list()
    #remove_duplicate_from_list1()
    #vowel_count()
    #check_validaty("ssdhjh@dF")
    #palindrome()
    remove_chr("vitthal","vihan")
    string = 'My Profile: https://auth.geeksforgeeks.org/ user / Chinmoy % 20Lenka / articles inthe portal of http: // www.geeksforgeeks.org / '
    print("Urls: ", Find(string))
    string = "geeks for geeks"
    sub_str = "geek"
    check(string, sub_str)
    # vowels = 'aeiou'
    # string = "Geeks for Geeks"
    # print(Check_Vow(string, vowels))

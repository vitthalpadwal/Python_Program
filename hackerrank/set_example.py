# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
Task
Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

Input Format

The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

Constraints


Output Format

Output total number of students who have subscriptions to the English or the French newspaper but not both.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

8
Explanation

The roll numbers of students who have subscriptions to English or French newspapers but not both are:
 and .
Hence, the total is  students.

'''
def set_example():
    e = input()
    eng = input()
    f = input()
    fre = input()
    eng = eng.split(' ')
    fre = fre.split(' ')
    output = set(eng).symmetric_difference(set(fre))
    return len(output)

if __name__ == '__main__':
    output = set_example()
    print(output)

'''
e = input()
el = set(map(int,raw_input().split()))
f = input()
fl = set(map(int,raw_input().split()))

interset = el.intersection(fl)


print len(interset)
'''
'''
We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])
.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])
.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
TASK
You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

 len(set(A))
 len(otherSets)

Output Format

Output the sum of elements in set .

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38
Explanation

After the first operation, (intersection_update operation), we get:
set

After the second operation, (update operation), we get:
set

After the third operation, (symmetric_difference_update operation), we get:
set

After the fourth operation, ( difference_update operation), we get:
set

The sum of elements in set  after these operations is .
'''

def set_mutation():
    LA = input()
    A = set(map(int, input().split()))

    N = input()

    for i in range(int(N)):
        k = input().split()
        ktemp = set(map(int,input().split()))
        if k[0] == 'update':
            A.update(ktemp)
        elif k[0] == 'intersection_update':
            A.intersection_update(ktemp)
        elif k[0] == 'difference_update':
            A.difference_update(ktemp)
        elif k[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(ktemp)
        else:
            print('Incorrect parameters')

    return (sum(A))

if __name__ == '__main__':
    output = set_mutation()
    print(output)


'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def set_with_example():
    A = {}
    e = input()
    eng = input()
    eng = eng.split(' ')
    A = set(eng)
    
    
    # N number of set
    n = input()

    #get the first operation
    intersec = input()
    i = input()
    i = i.split(' ')
    A.intersection_update(set(i))

    #get the second operation
    intersec = input()
    j = input()
    j = j.split(' ')
    A.update(set(j))

    #get the third operation
    intersec = input()
    k = input()
    k = k.split(' ')
    A.symmetric_difference_update(set(k))

    #get the four operation
    intersec = input()
    l = input()
    l = l.split(' ')
    A.difference_update(set(l))
    sum1 = 0
    for i in A:
        sum1 += int(i)
    return sum1


if __name__ == '__main__':
    # get the set A
    output = set_with_example()
    print(output)
'''
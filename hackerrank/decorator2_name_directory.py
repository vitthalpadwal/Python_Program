"""
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:

Mr. Henry Davids
For Mary George, the output should be:

Ms. Mary George
Input Format

The first line contains the integer , the number of people.
 lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Constraints


Output Format

Output  names on separate lines in the format described above in ascending order of age.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
Concept

For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it here.



"""

import operator

def person_lister(f):
    def inner(people):
        # complete the function
        list = []
        p1 = sorted(people, key=lambda x:int(x[2]))  #lambda x: x[2])
        for i in p1:
            list.append(f(i))
        return list
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
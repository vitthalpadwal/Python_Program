"""
The population of HackerWorld is . Initially, none of the people are friends with each other. In order to start a friendship, two persons  and  have to shake hands, where . The friendship relation is transitive, that is if  and  shake hands with each other,  and friends of  become friends with  and friends of .

You will be given  queries. After each query, you need to report the size of the largest friend circle (the largest group of friends) formed after considering that query.

For example, your list of queries is:

1 2
3 4
2 3
First,  and  shake hands, forming a circle of . Next,  and  do the same. Now there are two groups of  friends. When  and  become friends in the next query, both groups of friends are added together to make a circle of  friends. We would print

2
2
4
Function Description

Complete the function maxCircle in the editor below. It must return an array of integers representing the size of the maximum circle of friends after each query.

maxCircle has the following parameter(s):

queries: an array of integer arrays, each with two elements indicating a new friendship
Input Format

The first line contains an integer, , the number of queries to process.
Each of the next  lines consists of two space-separated integers denoting the 2-D array .

Constraints

 for
Output Format

Return an integer array of size , whose value at index  is the size of largest group present after processing the  query.

Sample Input 0

2
1 2
1 3
Sample Output 0

2
3
Explanation 0

In the first query,  and  shake hands. So, the size of largest group of friends is  (as no other friendships exist).
After the second query, ,  and  all become friends, as  shakes hand with ,  also become friends with  as he was already a friend of .

Sample Input 1

4
1000000000 23
11 3778
7 47
11 1000000000
Sample Output 1

2
2
2
4
Explanation 1

After first query, person  and person  become friends. So, the largest group size is .
After the second query, person  and person  become friends. So, the largest group size is still .
After the third query, person  and person  become friends. Answer is still .
After the last query, person  and person  become friends, which means , ,  and  all become friends. Hence, the answer now increased to .

Sample Input 2

6
1 2
3 4
1 3
5 7
5 6
7 4
Sample Output 2

2
2
4
4
4
7
Explanation 2

Friend circles after each iteration:

1   [1,2]
2   [1,2],[3,4]
3   [1,2,3,4]
4   [1,2,3,4],[5,7]
5   [1,2,3,4],[5,7,6]
6   [1,2,3,4,5,6,7]
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
class Node:
    def __init__(self):
        self.parent = None
        self.sum = 1

    def root(self):
        if self.parent:
            return self.parent.root()
        else:
            return self

    def add(self, other):
        assert not other.parent # cannot already have parent
        other.parent = self
        self.sum += other.sum
        return self.sum

    def join(self, other):
        root_a, root_b = self.root(), other.root()
        if root_a == root_b:
            return root_a.sum
        # join smaller sum to greater sum
        if root_b.sum > root_a.sum:
            return root_b.add(root_a)
        else:
            return root_a.add(root_b)

class NodeMap(dict):
    def __missing__(self, k):
        self[k] = Node()
        return self[k]

# Complete the maxCircle function below.
def maxCircle(queries):
    nodes = NodeMap()
    max_n = 0
    results = []
    for a, b in queries:
        max_n = max(max_n, nodes[a].join(nodes[b]))
        results.append(max_n)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

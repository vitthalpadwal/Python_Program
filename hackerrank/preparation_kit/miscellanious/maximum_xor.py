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

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxXor function below.

def maxXor(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in'{:b}'.format(n).zfill(k) :
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        ans.append(int(s, 2) ^ n)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
Greg has a tree of nodes containing integer data. He wants to insert a node with some non-zero integer value somewhere into the tree. His goal is to be able to cut two edges and have the values of each of the three new trees sum to the same amount. This is called a balanced forest. Being frugal, the data value he inserts should be minimal. Determine the minimal amount that a new node can have to allow creation of a balanced forest. If it's not possible to create a balanced forest, return -1.

For example, you are given node values  and . It is the following tree:

image

The blue node is root, the first number in a node is node number and the second is its value. Cuts can be made between nodes  and  and nodes  and  to have three trees with sums ,  and . Adding a new node  of  to the third tree completes the solution.

Function Description

Complete the balancedForest function in the editor below. It must return an integer representing the minimum value of that can be added to allow creation of a balanced forest, or  if it is not possible.

balancedForest has the following parameter(s):

c: an array of integers, the data values for each node
edges: an array of 2 element arrays, the node pairs per edge
Input Format

The first line contains a single integer, , the number of queries.

Each of the following  sets of lines is as follows:

The first line contains an integer, , the number of nodes in the tree.
The second line contains  space-separated integers describing the respective values of , where each denotes the value at node .
Each of the following  lines contains two space-separated integers,  and , describing edge  connecting nodes  and .
Constraints

Each query forms a valid undirected tree.
Subtasks

For  of the maximum score:

For  of the maximum score:

Output Format

For each query, return the minimum value of the integer . If no such value exists, return  instead.

Sample Input

2
5
1 2 2 1 1
1 2
1 3
3 5
1 4
3
1 3 5
1 3
1 2
Sample Output

2
-1
Explanation

We perform the following two queries:

The tree initially looks like this:
image
Greg can add a new node  with  and create a new edge connecting nodes  and . Then he cuts the edge connecting nodes  and  and the edge connecting nodes  and . We now have a three-tree balanced forest where each tree has a sum of .

image

In the second query, it's impossible to add a node in such a way that we can split the tree into a three-tree balanced forest so we return .

"""

from operator import attrgetter
from itertools import groupby
from sys import stderr


class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.children = []


def readtree():
    size = int(input())
    values = readints()
    assert size == len(values)
    nodes = [Node(i, v) for i, v in enumerate(values)]
    for _ in range(size - 1):
        x, y = readints()
        nodes[x - 1].children.append(nodes[y - 1])
        nodes[y - 1].children.append(nodes[x - 1])
    return nodes


def readints():
    return [int(fld) for fld in input().strip().split()]


def findbestbal(nodes):
    if len(nodes) == 1:
        return -1
    rootify(nodes[0])
    #    print([(n.index, n.value, n.totalval) for n in nodes], file=stderr)
    best = total = nodes[0].totalval
    dummynode = Node(None, None)
    dummynode.totalval = 0
    sortnode = []
    for k, g in groupby(sorted([dummynode] + nodes, key=attrgetter('totalval')),
                        attrgetter('totalval')):
        sortnode.append(list(g))
    total = nodes[0].totalval
    for ihi, n in enumerate(sortnode):
        if 3 * n[0].totalval >= total:
            break
    else:
        assert False
    ilo = ihi - 1
    for ihi in range(ihi, len(sortnode)):
        hi = sortnode[ihi][0].totalval
        lo = sortnode[ilo][0].totalval
        while 2 * hi + lo > total:
            if lo == 0:
                return -1
            if (total - lo) % 2 == 0:
                x = (total - lo) // 2
                for lonode in sortnode[ilo]:
                    if uptototalval(lonode, x + lo):
                        return x - lo
            ilo -= 1
            lo = sortnode[ilo][0].totalval
        if len(sortnode[ihi]) > 1:
            return 3 * hi - total
        hinode = sortnode[ihi][0]
        if 2 * hi + lo == total:
            for lonode in sortnode[ilo]:
                if uptototalval(lonode, hi) != hinode:
                    return hi - lo
        y = total - 2 * hi
        if uptototalval(hinode, 2 * hi) or uptototalval(hinode, hi + y):
            return hi - y


def rootify(root):
    root.parent = root.jumpup = None
    root.depth = 0
    bfnode = [root]
    i = 0
    while i < len(bfnode):
        node = bfnode[i]
        depth = node.depth + 1
        jumpup = uptodepth(node, depth & (depth - 1))
        for child in node.children:
            child.parent = node
            child.children.remove(node)
            child.depth = depth
            child.jumpup = jumpup
            bfnode.append(child)
        i += 1
    for node in reversed(bfnode):
        node.totalval = node.value + sum(child.totalval for child in node.children)


def uptodepth(node, depth):
    while node.depth > depth:
        if node.jumpup.depth <= depth:
            node = node.jumpup
        else:
            node = node.parent
    return node


def uptototalval(node, totalval):
    try:
        #    print('uptototalval(%s,%s)' % (node.index, totalval), file=stderr)
        while node.totalval < totalval:
            if node.parent is None:
                return None
            if node.jumpup.totalval <= totalval:
                node = node.jumpup
            else:
                node = node.parent
        #        print((node.index, node.totalval), file=stderr)
        if node.totalval == totalval:
            return node
        else:
            return None
    except Exception:
        return None


ncases = int(input())
for _ in range(ncases):
    print(findbestbal(readtree()))
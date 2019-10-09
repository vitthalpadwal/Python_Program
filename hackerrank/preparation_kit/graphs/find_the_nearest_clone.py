"""
n this challenge, there is a connected undirected graph where each of the nodes is a color. Given a color, find the shortest path connecting any two nodes of that color. Each edge has a weight of . If there is not a pair or if the color is not found, print .

For example, given , and  edges  and  and colors for each node are  we can draw the following graph:

image

Each of the nodes is labeled [node]/[color] and is colored appropriately. If we want the shortest path between color , blue, we see there is a direct path between nodes  and . For green, color , we see the path length  from . There is no pair for node  having color , red.

Function Description

Complete the findShortest function in the editor below. It should return an integer representing the length of the shortest path between two nodes of the same color, or  if it is not possible.

findShortest has the following parameter(s):

g_nodes: an integer, the number of nodes
g_from: an array of integers, the start nodes for each edge
g_to: an array of integers, the end nodes for each edge
ids: an array of integers, the color id per node
val: an integer, the id of the color to match
Input Format

The first line contains two space-separated integers  and , the number of nodes and edges in the graph.
Each of the next  lines contains two space-separated integers  and , the nodes connected by an edge.
The next line contains  space-seperated integers, , representing the color id of each node from  to .
The last line contains the id of the color to analyze.

Note: The nodes are indexed from  to .

Constraints




Output Format

Print the single integer representing the smallest path length or .

Sample Input 0

4 3
1 2
1 3
4 2
1 2 1 1
1
Sample Output 0

1
Explanation 0

image

In the above image the distance between the closest nodes having color label  is .

Sample Input 1

4 3
1 2
1 3
4 2
1 2 3 4
2
Sample Output 1

-1
Explanation 1

image

Sample Input 2

5 4
1 2
1 3
2 4
3 5
1 2 3 3 2
2
Sample Output 2

3
Explanation 2

image


"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
from queue import Queue
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = {i + 1: [] for i in range(graph_nodes)}
    for i in range(len(graph_from)):
        g[graph_from[i]].append(graph_to[i])
        g[graph_to[i]].append(graph_from[i])

    target_nodes = []

    for i in range(len(ids)):
        if ids[i] == val:
            target_nodes.append(i + 1)
    result = -1
    for node in target_nodes:
        w = weight(g, target_nodes, node, result)
        if w >0 and w < result or result == -1:
            result = w
    return result

def weight(g, target_nodes, node, limit=-1):
    visited = set()
    q = Queue()
    q.put((node, 0))
    while not q.empty():
        n, w = q.get()
        if n in visited:
            continue
        if n in target_nodes and n != node:
            return w
        visited.add(n)
        if w == limit:
            return -1
        for next_node in g[n]:
            if next_node not in visited:
                q.put((next_node, w + 1))
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()

"""
Consider an undirected graph consisting of  nodes where each node is labeled from  to  and the edge between any two nodes is always of length . We define node  to be the starting position for a BFS. Given a graph, determine the distances from the start node to each of its descendants and return the list in node number order, ascending. If a node is disconnected, it's distance should be .

For example, there are  nodes in the graph with a starting node . The list of , and each has a weight of .

image

Starting from node  and creating a list of distances, for nodes  through  we have .

Function Description

Define a Graph class with the required methods to return a list of distances.

Input Format

The first line contains an integer, , the number of queries.

Each of the following  sets of lines is as follows:

The first line contains two space-separated integers,  and , the number of nodes and the number of edges.
Each of the next  lines contains two space-separated integers,  and , describing an edge connecting node  to node .
The last line contains a single integer, , the index of the starting node.
Constraints

Output Format

For each of the  queries, print a single line of  space-separated integers denoting the shortest distances to each of the  other nodes from starting position . These distances should be listed sequentially by node number (i.e., ), but should not include node . If some node is unreachable from , print  as the distance to that node.

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

We perform the following two queries:

The given graph can be represented as:
image
where our start node, , is node . The shortest distances from  to the other nodes are one edge to node , one edge to node , and there is no connection to node .
The given graph can be represented as:
image
where our start node, , is node . There is only one edge here, so node  is unreachable from node  and node  has one edge connecting it to node . We then print node 's distance to nodes  and  (respectively) as a single line of space-separated integers: -1 6.

Note: Recall that the actual length of each edge is , and we print  as the distance to any node that's unreachable from .


"""

t = int(input().strip())


def calculate_cost(nodes, travel_edges):
    new_edges = []
    weight = 6
    current_cost = 0

    while travel_edges:
        for e in travel_edges:
            id, cost, edges = nodes[e - 1]

            if cost == -1:
                new_edges = new_edges + edges
                cost = current_cost
                nodes[e - 1] = (id, cost, edges)

        travel_edges = new_edges
        new_edges = []
        current_cost += weight

    return nodes


for test in range(t):
    n, m = [int(i) for i in input().strip().split()]

    nodes = [(i, -1, []) for i in range(1, n + 1)]

    for edge in range(m):
        start, end = [int(i) for i in input().strip().split()]

        id, cost, edges = nodes[start - 1]
        nodes[start - 1] = (id, cost, edges + [end])

        id, cost, edges = nodes[end - 1]
        nodes[end - 1] = (id, cost, edges + [start])

    s = int(input().strip())

    nodes = calculate_cost(nodes, [s])

    weights = ' '.join([str(node[1]) for node in nodes if node[1] != 0])

    print(weights)
"""
The kingdom of Zion has cities connected by bidirectional roads. There is a unique path between any pair of cities. Morpheus has found out that the machines are planning to destroy the whole kingdom. If two machines can join forces, they will attack. Neo has to destroy roads connecting cities with machines in order to stop them from joining forces. There must not be any path connecting two machines.

Each of the roads takes an amount of time to destroy, and only one can be worked on at a time. Given a list of edges and times, determine the minimum time to stop the attack.

For example, there are  cities called . Three of them have machines and are colored red. The time to destroy is shown next to each road. If we cut the two green roads, there are no paths between any two machines. The time required is .

image

Function Description

Complete the function minTime in the editor below. It must return an integer representing the minimum time to cut off access between the machines.

minTime has the following parameter(s):

roads: a two-dimensional array of integers, each  where cities are connected by a road that takes  to destroy
machines: an array of integers representing cities with machines
Input Format

The first line of the input contains two space-separated integers,  and , the number of cities and the number of machines.

Each of the following  lines contains three space-separated integers, , and . There is a bidirectional road connecting  and , and to destroy this road it takes  units.

Each of the last  lines contains an integer, , the label of a city with a machine.

Constraints

Output Format

Return an integer representing the minimum time required to disrupt the connections among all machines.

Sample Input

5 3
2 1 8
1 0 5
2 4 5
1 3 4
2
4
0
Sample Output

10
Explanation

image

The machines are located at the cities ,  and . Neo can destroy the green roads resulting in a time of . Destroying the road between cities  and  instead of between  and  would work, but it's not minimal.
"""


class vertex:
    def __init__(self):
        self.adj = []
        self.is_k = False


def find_smallest_edge_and_delete(arr, edg_lst):
    if len(edg_lst) == 0:
        return 0

    smallest = edg_lst[0]
    for edge in edg_lst:
        if smallest[2] > edge[2]:
            smallest = edge
    # print(smallest)
    # print(arr[smallest[0]].adj)
    # print(arr[smallest[1]].adj)
    arr[smallest[0]].adj.remove([smallest[1], smallest[2]])
    arr[smallest[1]].adj.remove([smallest[0], smallest[2]])
    return smallest[2]


# node has to be a K-type node
def BFS_and_del(arr, x, edg_lst, visited):
    visited[x] = True
    val = 0
    for edge in arr[x].adj:
        if edge[0] in visited:
            continue
        edg_lst.append([x, edge[0], edge[1]])
        if arr[edge[0]].is_k == True:
            val = find_smallest_edge_and_delete(arr, edg_lst)
        else:
            val = BFS_and_del(arr, edge[0], edg_lst, visited)
        edg_lst.remove([x, edge[0], edge[1]])
        if val != 0:
            break
    del visited[x]
    return val


var = input().split()
N, K = int(var[0]), int(var[1])

V = []
arrK = []
for i in range(0, N):
    V.append(vertex())

# Read edges
for i in range(0, N - 1):
    var = input().split()
    x, y, w = int(var[0]), int(var[1]), int(var[2])
    V[x].adj.append([y, w])
    V[y].adj.append([x, w])

# Read K vertices
for i in range(0, K):
    val = int(input())
    V[val].is_k = True
    arrK.append(val)

ans = 0
del_count = 0
while del_count < K - 1:
    for k in arrK:
        val = BFS_and_del(V, k, [], {})
        if val > 0:
            del_count += 1
            ans = ans + val

print(ans)

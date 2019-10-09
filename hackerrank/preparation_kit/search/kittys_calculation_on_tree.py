"""
Kitty has a tree, , consisting of  nodes where each node is uniquely labeled from  to . Her friend Alex gave her  sets, where each set contains  distinct nodes. Kitty needs to calculate the following expression on each set:

where:

 denotes an unordered pair of nodes belonging to the set.
 denotes the number of edges on the unique path between nodes  and .
Given  and  sets of  distinct nodes, can you help her calculate the expression for each set? For each set of nodes, print the value of the expression modulo  on a new line.

Input Format

The first line contains two space-separated integers describing the respective values of  (the number of nodes in tree ) and (the number of sets).
Each of the  subsequent lines contains two space-separated integers,  and , describing an undirected edge between nodes  and .
The  subsequent lines define each set over two lines in the following format:

The first line contains an integer, , denoting the size of the set.
The second line contains  space-separated integers describing the set's elements.
Constraints

The sum of  over all  does not exceed .
All elements in each set are distinct.
Subtasks

 for  of the maximum score.
 for  of the maximum score.
 for  of the maximum score.
Output Format

Print  lines of output where each line  contains the expression for the  query, modulo .

Sample Input 0

7 3
1 2
1 3
1 4
3 5
3 6
3 7
2
2 4
1
5
3
2 4 5
Sample Output 0

16
0
106
Explanation 0

Tree  looks like this:

image

We perform the following calculations for  sets:

Set : Given set , the only pair we can form is , where . We then calculate the following answer and print it on a new line:
Set : Given set , we cannot form any pairs because we don't have at least two elements. Thus, we print  on a new line.

Set : Given set , we can form the pairs , , and . We then calculate the following answer and print it on a new line:


"""

from collections import Counter, defaultdict

MOD = 10**9 + 7

def read_row():
    return (int(x) for x in input().split())

def mul(x, y):
    return (x * y) % MOD

def add(*args):
    return sum(args) % MOD

def sub(x, y):
    return (x - y) % MOD

n, q = read_row()

# Construct adjacency list of the tree
adj_list = defaultdict(list)

for _ in range(n - 1):
    u, v = read_row()
    adj_list[u].append(v)
    adj_list[v].append(u)

# Construct element to set mapping {element: [sets it belongs to]}
elements = {v: set() for v in adj_list}

for set_no in range(q):
    read_row()
    for x in read_row():
        elements[x].add(set_no)

# Do BFS to find parent for each node and order them in reverse depth
root = next(iter(adj_list))
current = [root]
current_depth = 0
order = []
parent = {root: None}
depth = {root: current_depth}

while current:
    current_depth += 1
    order.extend(current)
    nxt = []
    for node in current:
        for neighbor in adj_list[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                depth[neighbor] = current_depth
                nxt.append(neighbor)

    current = nxt

# Process nodes in the order created above
score = Counter()
# {node: {set_a: [depth, sum of nodes, flow]}}
state = {}
for node in reversed(order):
    states = [state[neighbor] for neighbor in adj_list[node] if neighbor != parent[node]]
    largest = {s: [depth[node], node, 0] for s in elements[node]}

    if states:
        max_index = max(range(len(states)), key=lambda x: len(states[x]))
        if len(states[max_index]) > len(largest):
            states[max_index], largest = largest, states[max_index]


    sets = defaultdict(list)
    for cur_state in states:
        for set_no, v in cur_state.items():
            sets[set_no].append(v)

    for set_no, states in sets.items():
        if len(states) == 1 and set_no not in largest:
            largest[set_no] = states[0]
            continue

        if set_no in largest:
            states.append(largest.pop(set_no))

        total_flow = 0
        total_node_sum = 0

        for node_depth, node_sum, node_flow in states:
            flow_delta = mul(node_depth - depth[node], node_sum)
            total_flow = add(total_flow, flow_delta, node_flow)
            total_node_sum += node_sum

        set_score = 0

        for node_depth, node_sum, node_flow in states:
            node_flow = add(mul(node_depth - depth[node], node_sum), node_flow)
            diff = mul(sub(total_flow, node_flow), node_sum)
            set_score = add(set_score, diff)

        score[set_no] = add(score[set_no], set_score)
        largest[set_no] = (depth[node], total_node_sum, total_flow)

    state[node] = largest

print(*(score[i] for i in range(q)), sep='\n')
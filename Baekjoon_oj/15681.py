from sys import stdin, setrecursionlimit

setrecursionlimit(1000000000)

def make_tree(current_node, parent):
    for node in connect[current_node]:
        if node != parent:
            child[current_node].append(node)
            make_tree(node, current_node)

def count_subtree_nodes(current_node):
    size[current_node] = 1
    for node in child[current_node]:
        count_subtree_nodes(node)
        size[current_node] += size[node]

N, R, Q = map(int, stdin.readline().split())
connect = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, stdin.readline().split())
    connect[U].append(V)
    connect[V].append(U)

child = [[] for _ in range(N + 1)]
make_tree(R, -1)
size = [0] * (N + 1)
count_subtree_nodes(R)
for _ in range(Q):
    root = int(stdin.readline())
    print(size[root])


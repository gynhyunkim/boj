from sys import stdin 

INF = float('inf')
n = int(stdin.readline())
m = int(stdin.readline())
graph = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0", end=" ")
        else:
            print(graph[a][b], end = " ")
    print()


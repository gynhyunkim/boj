from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

def BFS(start):
    num = [0] * (N + 1)
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                queue.append(i)
    return sum(num)

result = []
for i in range(1, N + 1):
	result.append(BFS(i))

print(result.index(min(result)) + 1)
                


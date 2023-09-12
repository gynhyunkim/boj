from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
	u, v = map(int, stdin.readline().split())
	graph[u].append(v)
	graph[v].append(u)

visited = [False] * (N + 1)

def DFS(v):
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			DFS(i)

answer = 0
for i in range(1, N + 1):
	if not visited[i]:
		answer += 1
		DFS(i)
print(answer)

from sys import stdin
from collections import deque

n = int(stdin.readline())
p1, p2 = map(int, stdin.readline().split())
m = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
for i in range(m):
	x, y = map(int, stdin.readline().split())
	graph[x].append(y)
	graph[y].append(x)

visited = [False for _ in range(n + 1)]
answer = 0
def dfs(v, cnt):
	global answer
	visited[v] = True

	if v == p2:
		answer = cnt
		return
	for i in graph[v]:
		if not visited[i]:
			dfs(i, cnt + 1)

dfs(p1, 0)
print(answer if answer > 0 else -1)



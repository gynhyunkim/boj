# DFS와 BFS

from sys import stdin

def BFS(g, start):
	visited = [False for _ in range(n + 1)]
	q = [start]
	visited[start] = True
	while q:
		cur = q.pop(0)
		print(cur, end = ' ')
		for c in sorted(g[cur]):
			if not visited[c]:
				visited[c] = True
				q.append(c)

def DFS(g, cur):
	visited[cur] = True
	print(cur, end = ' ')
	for c in sorted(g[cur]):
		if not visited[c]:
			DFS(g, c)

n, m, v = map(int, stdin.readline().split())
graph =  [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
	i, j = map(int, stdin.readline().split())
	graph[i].append(j)
	graph[j].append(i)

DFS(graph, v)
print()
BFS(graph, v)
print()

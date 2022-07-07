# 깊이 우선 탐색1
import sys
sys.setrecursionlimit(10**6)
def DFS(v, e, r):
	global o
	visited[r] = True
	v[r] = o
	for child in e[r]:
		if not visited[child]:
			o += 1
			DFS(v, e, child)
	
n, m, r = map(int, sys.stdin.readline().split())
V = [0 for _ in range(n + 1)]
E = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(m):
	u, v = map(int, sys.stdin.readline().split())
	E[u].append(v)
	E[v].append(u)

for e in E:
	e.sort()

o = 1
DFS(V, E, r)

for i in range(1, n + 1):
	print(V[i])

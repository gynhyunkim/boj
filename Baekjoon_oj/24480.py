# 깊이 우선 탐색2
import sys
sys.setrecursionlimit(10**6)
def DFS(v, e, r):
	global o
	visited[r] = True
	v[r] = o
	e[r] = sorted(e[r], reverse = True)
	for child in e[r]:
		if not visited[child]:
			o += 1
			DFS(v, e, child)
	
n, m, r = map(int, sys.stdin.readline().split())
V = [0 for _ in range(n)]
E = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(m):
	u, v = map(int, sys.stdin.readline().split())
	E[u - 1].append(v - 1)
	E[v - 1].append(u - 1)

o = 1
DFS(V, E, r - 1)
print(*V, sep = '\n')

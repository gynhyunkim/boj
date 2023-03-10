# 너비 우선 탐색2
import sys
from collections import deque

def bfs(v, e, r):
	visited = [False] * n
	q = deque([r])
	visited[r] = True
	o = 1
	while q:
		x = q.popleft()
		v[x] = o
		o += 1
		for c in sorted(e[x], reverse = True):
			if not visited[c]:
				visited[c] = True
				q.append(c)


n, m, r = map(int, sys.stdin.readline().split())
V = [0 for _ in range(n)]
E = [[] for _ in range(n)]

for _ in range(m):
	u, v = map(int, sys.stdin.readline().split())
	E[u - 1].append(v - 1)
	E[v - 1].append(u - 1)

bfs(V, E, r - 1)
print(*V, sep = '\n')

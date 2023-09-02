# 바이러스
import sys

def dfs(g, r):
	global cnt
	visited[r] = True
	for c in g[r]:
		if not visited[c]:
			cnt += 1
			dfs(g, c)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
visited = [False] * n

graph = [[] for _ in range(n)]

for _ in range(m):
	i, j = map(int, sys.stdin.readline().split())
	graph[i- 1].append(j - 1)
	graph[j - 1].append(i - 1)

cnt = 0
dfs(graph, 0)
print(cnt)
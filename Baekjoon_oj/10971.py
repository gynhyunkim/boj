from sys import stdin
from collections import deque

N = int(stdin.readline())
W = [list(map(int, stdin.readline().split())) for _ in range(N)]

visited = [1] + [0] * (N - 1)

def dfs(start, v, w, n):
	ret = float('inf')
	if n == N and W[v][start] > 0:
		return w + W[v][start]
	for next, cost in enumerate(W[v]):
		if not visited[next] and cost > 0:
			visited[next] = 1
			ret = min(ret, dfs(start, next, w + cost, n + 1))
			visited[next] = 0
	return ret

print(dfs(0, 0, 0, 1))
from sys import stdin
from collections import deque

N, Q = map(int, stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
	p, q, r = map(int, stdin.readline().split())
	graph[p].append((q, r))
	graph[q].append((p, r))

for i in range(Q):
	k, v = map(int, stdin.readline().split())
	visited = [False] * (N + 1)
	visited[v] = True
	result = 0
	q = deque([(v, float('inf'))])

	while q:
		v, usado = q.popleft()
		for next_v, next_usado in graph[v]:
			next_usado = min(next_usado, usado)
			if next_usado >= k and not visited[next_v]:
				result += 1
				q.append((next_v, next_usado))
				visited[next_v] = True
	print(result)

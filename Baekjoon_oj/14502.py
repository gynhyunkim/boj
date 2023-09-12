from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def bfs():
	visited = [[0] * M for _ in range(N)]
	q = deque([])
	for i in range(N):
		for j in range(M):
			if graph[i][j] == 2:
				q.append((i, j))
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
				q.append((nx, ny))
				visited[nx][ny] = 1
	global result
	count = 0
	for i in range(N):
		for j in range(M):
			count += 1 if graph[i][j] == 0 and not visited[i][j] else 0
	result = max(result, count)

def make_wall(count):
	if count == 3:
		bfs()
		return
	for i in range(N):
		for j in range(M):
			if graph[i][j] == 0:
				graph[i][j] = 1
				make_wall(count + 1)
				graph[i][j] = 0

make_wall(0)
print(result)
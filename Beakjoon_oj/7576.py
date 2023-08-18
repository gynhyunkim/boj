from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
q = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(N):
	for j in range(M):
		if graph[i][j] == 1:
			q.append([i, j])

def bfs():
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = dx[i] + x, dy[i] + y
			if 0<= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
				graph[nx][ny] = graph[x][y] + 1
				q.append([nx, ny])

bfs()
for i in graph:
	for j in i:
		if j == 0:
			print(-1)
			exit(0)
	res = max(res, max(i))

print(res - 1)


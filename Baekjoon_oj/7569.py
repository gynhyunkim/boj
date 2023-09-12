from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())
status = [[list(map(int, stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
	q = deque([])
	for i in range(H):
		for j in range(N):
			for k in range(M):
				if status[i][j][k] == 1:
					q.append((i, j, k, 1))
	max_days = 0
	while q:
		x, y, z, days = q.popleft()
		for i in range(6):
			nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
			if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and status[nx][ny][nz] == 0:
				status[nx][ny][nz] = days
				max_days = max(days, max_days)
				q.append((nx, ny, nz, days + 1))
	return max_days

days = bfs()
for i in range(H):
	for j in range(N):
		for k in range(M):
			if status[i][j][k] == 0:
				days = -1
				break
print(days)
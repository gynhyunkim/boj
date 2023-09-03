from sys import stdin
from collections import deque, defaultdict

N, M = map(int, stdin.readline().split())
mat = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	q = deque([(x, y)])
	info = defaultdict(int)
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < N and 0 <= ny < M:
				if not mat[nx][ny]:
					info[(x, y)] += 1
				elif not visited[nx][ny]:
					q.append((nx, ny))
					visited[nx][ny] = 1
	for x, y in info:
		mat[x][y] -= info[(x, y)]
		if mat[x][y] < 0:
			mat[x][y] = 0 

year = 0
cnt = 0
while cnt < 2:
	cnt = 0
	year += 1
	visited = [[0] * M for _ in range(N)]
	for i in range(N):
		for j in range(M):
			if mat[i][j] and not visited[i][j]:
				cnt += 1
				visited[i][j] = 1
				bfs(i, j)
	if cnt == 0:
		year = 1
		break

print(year - 1)

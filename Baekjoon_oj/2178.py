# 미로 탐색
from sys import stdin

n, m = map(int, stdin.readline().split())
maze = [list(map(int, stdin.readline().strip('\n'))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS():
	q = [(0, 0)]
	while q:
		x, y =  q.pop(0)
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= ny < n and 0 <= nx < m:
				if maze[ny][nx] == 1:
					maze[ny][nx] = maze[y][x] + 1
					q.append((nx, ny))
BFS()
print(maze[n - 1][m - 1])
	
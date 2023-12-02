# from sys import stdin
# from collections import deque

# def bfs(x, y):
# 	q = deque([(x, y)])
# 	visited[x][y] = 0
# 	while q:
# 		x, y = q.popleft()
# 		for i in range(4):
# 			nx, ny = x + dx[i], y + dy[i]
# 			while True:
# 				if not (0 <= nx < h and 0 <= ny < w):
# 					break
# 				if board[nx][ny] == "*":
# 					break
# 				if visited[nx][ny] < visited[x][y] + 1:
# 					break
# 				q.append((nx, ny))
# 				visited[nx][ny] = visited[x][y] + 1
# 				nx = nx + dx[i]
# 				ny = ny + dy[i]

# w, h = map(int, stdin.readline().split())
# board = [stdin.readline().strip('\n') for _ in range(h)]

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# C_locate = []
# for i in range(h):
# 	for j in range(w):
# 		if board[i][j] == "C":
# 			C_locate.append((i, j))
# (start_x, start_y), (end_x, end_y) = C_locate
# visited = [[float('inf')] * w for _ in range(h)]
# bfs(start_x, start_y)
# print(visited[end_x][end_y] - 1)

from sys import stdin
from collections import deque

def bfs(x, y):
	q = deque([])
	for i in range(4):
		q.append((i, x, y, 0))
		count[i][x][y] = 0
	while q:
		direct, x, y, mirror = q.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
				new_mirror = mirror + 1 if direct != i else mirror
				if count[i][nx][ny] > new_mirror:
					count[i][nx][ny] = new_mirror
					q.append((i, nx, ny, new_mirror))

w, h = map(int, stdin.readline().split())
board = [stdin.readline().strip('\n') for _ in range(h)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

C_locate = []
for i in range(h):
	for j in range(w):
		if board[i][j] == "C":
			C_locate.append((i, j))
(start_x, start_y), (end_x, end_y) = C_locate
count = [[[float('inf') for _ in range(w)] for _ in range(h)] for _ in range(4)]
bfs(start_x, start_y)
print(min(count[0][end_x][end_y], min(count[1][end_x][end_y], min(count[2][end_x][end_y], count[3][end_x][end_y]))))

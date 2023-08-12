from sys import stdin
from collections import deque, defaultdict

N, M = map(int, stdin.readline().split())

graph = [list(map(int, stdin.readline().split())) for _ in range(M)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
	
visited = [[0 for _ in range(N)] for _ in range(M)]

def bfs(x, y):
	q = deque()
	q.append([x, y])
	visited[x][y] = 1
	room = 1
	while q:
		x, y = q.popleft()
		wall = 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if ((graph[x][y] & wall) != wall):
				if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
					room += 1
					visited[nx][ny] = 1
					q.append([nx, ny])
			wall *= 2
	return room

room_cnt = 0
max_room = 0
del_room = 0

for i in range(M):
	for j in range(N):
		if not visited[i][j]:
			room_cnt += 1
			max_room = max(max_room, bfs(i, j))

for i in range(M):
	for j in range(N):
		num = 1
		while num < 9:
			if num & graph[i][j]:
				visited = [[0] * N for _ in range(M)]
				graph[i][j] -= num
				del_room = max(del_room, bfs(i, j))
				graph[i][j] += num
			num *= 2

print(room_cnt)
print(max_room)
print(del_room)
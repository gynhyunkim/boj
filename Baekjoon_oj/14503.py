from sys import stdin
from collections import deque

# 0 북, 1 동, 2 남, 3 서
N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
rotate = [3, 0, 1, 2]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
def is_empty(x, y):
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny]:
			return True
	return False
q = deque([(r, c, d)])
while q:
	x, y, d = q.popleft()
	if not graph[x][y]:
		graph[x][y] = 2
		cnt += 1
		q.append((x, y, d))
	elif is_empty(x, y):
		d = rotate[d]
		nx, ny = x + dx[d], y + dy[d]
		if 0 <= nx < N and 0 <= ny < M and not graph[nx][ny]:
			q.append((nx, ny, d))
		else:
			q.append((x, y, d))
	else:
		nx, ny = x - dx[d], y - dy[d]
		if 1 > nx or nx >= N - 1 or 1 > ny or ny >= M - 1 or graph[nx][ny] == 1:
			break
		else:
			q.append((nx, ny, d))

print(cnt)
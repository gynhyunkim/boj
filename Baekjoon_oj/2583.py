from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

N, M, K = map(int, stdin.readline().split())

grid = [[0] * M for _ in range(N)]

for i in range(K):
	x1, y1, x2, y2 = map(int, stdin.readline().split())
	for x in range(x1, x2):
		for y in range(y1, y2):
			grid[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

area = []
def DFS(x, y):
	if x < 0 or x >= M or y < 0 or y >= N or grid[y][x] == 1:
		return 
	else:
		grid[y][x] = 1
		area[-1] += 1
		for i in range(4):
			DFS(x + dx[i], y + dy[i])

for x in range(M):
	for y in range(N):
		if grid[y][x] == 0:
			area.append(0)
			DFS(x, y)

area.sort()
print(len(area))
print(*area, sep = ' ')

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

N = int(stdin.readline())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]
max_height = 0
for i in range(N):
	max_height = max(max_height, max(area[i]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y, h):
	if x < 0 or x >= N or y < 0 or y >= N or area[y][x] <= h or visited[y][x]:
		return
	visited[y][x] = True
	for i in range(4):
		DFS(x + dx[i], y + dy[i], h)

max_cnt = 0
for h in range(max_height + 1):
	cnt = 0
	visited = [[False] * N for _ in range(N)]
	for x in range(N):
		for y in range(N):
			if area[y][x] > h and not visited[y][x]:
				cnt += 1
				DFS(x, y, h)
	max_cnt = max(max_cnt, cnt)

print(max_cnt)

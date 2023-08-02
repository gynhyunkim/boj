from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 8)

M, N = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x, y):
	if (x, y) == (N - 1, M - 1):
		return 1
	if dp[y][x] > -1:
		return dp[y][x]
	
	dp[y][x] = 0
	for i in range(4):
		new_x = x + dx[i]
		new_y = y + dy[i]
		if 0 <= new_x < N and 0 <= new_y < M and graph[new_y][new_x] < graph[y][x]:
			dp[y][x] += DFS(new_x, new_y)
	return dp[y][x]

print(DFS(0, 0))
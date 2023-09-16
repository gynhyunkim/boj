from sys import stdin
from copy import deepcopy

N, M = map(int, stdin.readline().split())
office = [list(map(int, stdin.readline().split())) for _ in range(N)]
mode = [
	[],
	[[0], [1], [2], [3]],
	[[0, 2], [1, 3]],
	[[0, 1], [1, 2], [2, 3], [0, 3]],
	[[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
	[[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def fill(board, d, x, y):
	for i in d:
		nx, ny = x, y
		while 0 <= nx < N and 0 <= ny < M:
			nx += dx[i]
			ny += dy[i]
			if not 0 <= nx < N or not 0 <= ny < M:
				break
			if board[nx][ny] == 6:
				break
			elif board[nx][ny] == 0:
				board[nx][ny] = 7


def dfs(arr, depth):
	global ans
	if depth == len(cctv):
		count = 0
		for i in range(N):
			count += arr[i].count(0)
		ans = min(ans, count)
		return
	temp = deepcopy(arr)
	cctv_num, x, y = cctv[depth]
	for m in mode[cctv_num]:
		fill(temp, m, x, y)
		dfs(temp, depth + 1)
		temp = deepcopy(arr)

ans = float('inf')
cctv = []
for i in range(N):
	for j in range(M):
		if 1 <= office[i][j] < 6:
			cctv.append([office[i][j], i, j])

dfs(deepcopy(office), 0)
print(ans)

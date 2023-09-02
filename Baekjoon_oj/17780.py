from sys import stdin
from collections import defaultdict

N, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
pon_info = []
pos_info = defaultdict(list)

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]
d_reverse = [0, 2, 1, 4, 3]

for n in range(K):
	i, j, d = map(int, stdin.readline().split())
	pon_info.append([i, j, d])
	# 가장 밑에 있는 말만 추가하기

def simulation():
	for n, pon in enumerate(pon_info):
		i, j, d = pon
		if pos_info[(i, j)][0] != n:
			continue
		ni, nj = ni + di[d], nj + dj[d]
		if ni < 0 or ni >= N or nj < 0 or nj >= N or board[ni][nj] == 2:
			pon_info[n][2] = d_reverse[d]
			d = pon_info[n][2]
			ni, nj = ni + di[d], nj + dj[d]
			if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 2:
				


simulation()
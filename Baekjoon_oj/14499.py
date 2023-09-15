from sys import stdin

N, M, x, y, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
command = list(map(int, stdin.readline().split()))

EAST, WEST, SOUTH, NORTH, UP, DOWN = 0, 1, 2, 3, 4, 5

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
dice = [0] * 6
# east, west, south, north, up, down = dice[0:6]
for d in command:
	nx = x + dx[d]
	ny = y + dy[d]
	if not 0 <= nx < N or not 0 <= ny < M:
		continue
	if d == 1:
		dice[EAST], dice[WEST], dice[UP], dice[DOWN] = dice[DOWN], dice[UP], dice[EAST], dice[WEST]
	elif d == 2:
		dice[EAST], dice[WEST], dice[UP], dice[DOWN] = dice[UP], dice[DOWN], dice[WEST], dice[EAST]
	elif d == 3:
		dice[SOUTH], dice[NORTH], dice[UP], dice[DOWN] = dice[UP], dice[DOWN], dice[NORTH], dice[SOUTH]
	elif d == 4:
		dice[SOUTH], dice[NORTH], dice[UP], dice[DOWN] = dice[DOWN], dice[UP], dice[SOUTH], dice[NORTH]

	if board[nx][ny] == 0:
		board[nx][ny] = dice[DOWN]
	else:
		dice[DOWN] = board[nx][ny]
		board[nx][ny] = 0
	x, y = nx, ny
	print(dice[UP])

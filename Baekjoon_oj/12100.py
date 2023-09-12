from sys import stdin
from copy import deepcopy

N = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]

def move_left(board):
	for i in range(N):
		for j in range(N - 1):
			k = j
			while k < N and board[i][k] == 0:
				k += 1
			if k < N and k > j:
				board[i][j], board[i][k] = board[i][k], board[i][j]
		for j in range(N - 1):
			if board[i][j] == board[i][j + 1]:
				board[i][j] += board[i][j + 1]
				board[i][j + 1:] = board[i][j + 2:] + [0]
				
	return board

def move_right(board):
	for i in range(N - 1, -1, -1):
		for j in range(N - 1, 0, -1):
			k = j
			while k >= 0 and board[i][k] == 0:
				k -= 1
			if k >= 0 and k < j:
				board[i][j], board[i][k] = board[i][k], board[i][j]
		for j in range(N - 1, 0, -1):
			if board[i][j] == board[i][j - 1]:
				board[i][j] += board[i][j - 1]
				board[i][:j] = [0] + board[i][:j - 1]
	return board
	

def move_up(board):
	for j in range(N):
		for i in range(N - 1):
			k = i
			while k < N and board[k][j] == 0:
				k += 1
			if k < N and k > i:
				board[i][j], board[k][j] = board[k][j], board[i][j]
		for i in range(N - 1):
			if board[i][j] == board[i + 1][j]:
				board[i][j] += board[i + 1][j]
				for k in range(i + 1, N - 1):
					board[k][j] = board[k + 1][j]
				board[N - 1][j] = 0
	return board

def move_down(board):
	for j in range(N - 1, -1, -1):
		for i in range(N - 1, 0, -1):
			k = i
			while k >= 0 and board[k][j] == 0:
				k -= 1
			if k >= 0 and k < i:
				board[k][j], board[i][j] = board[i][j], board[k][j]
		for i in range(N - 1, 0, -1):
			if board[i][j] == board[i - 1][j]:
				board[i][j] += board[i - 1][j]
				for k in range(i - 1, 0, -1):
					board[k][j] = board[k - 1][j]
				board[0][j] = 0
	return board

direction = [move_left, move_right, move_up, move_down]

def sol(board, cnt):
	global ans
	if cnt == 5:
		for i in range(N):
			 ans = max(ans, max(board[i]))
		return 
	for i in range(4):
		tmp_board = direction[i](deepcopy(board))
		sol(tmp_board, cnt + 1)

ans = 2
sol(board, 0)
print(ans)

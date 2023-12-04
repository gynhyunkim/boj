from sys import stdin
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
INF = float('inf')

def fint_distance_to_target(start_pos, target_pos):
	global w, h, board

	q = deque()
	visited = [[False for _ in range(w)] for _ in range(h)]

	x, y = start_pos
	q.append([x, y, 0])
	visited[x][y] = True

	while q:
		x, y, cnt = q.popleft()
		if x == target_pos[0] and y == target_pos[1]:
			return cnt
		
		for t in range(4):
			nx = x + dx[t]
			ny = y + dy[t]

			if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != 'x' and not visited[nx][ny]:
				q.append([nx, ny, cnt + 1])
				visited[nx][ny] = True
	return INF

def make_combination(depth, target_cnt, start_pos, now_dist):
	global result, check, targets
	if now_dist >= result:
		return
	
	if depth == target_cnt:
		if now_dist < result:
			result = now_dist
		return 
	
	for i in range(target_cnt):
		if not check[i]:
			next_dist = now_dist + dist[start_pos][i]
			check[i] = True
			make_combination(depth + 1, target_cnt, i, next_dist)
			check[i] = False
	
while True:
	w, h = map(int, stdin.readline().split())
	if w == 0 and h == 0:
		break
	board = [stdin.readline().rstrip() for _ in range(h)]
	targets = []
	start_pos = []
	for i in range(h):
		for j in range(w):
			if board[i][j] == '*':
				targets.append([i, j])
			elif board[i][j] == 'o':
				start_pos = [i, j]
	dist = [[INF for _ in range(len(targets) + 1)] for _ in range(len(targets) + 1)]

	for i in range(len(targets)):
		for j in range(len(targets)):
			cnt = fint_distance_to_target(targets[i], targets[j])
			dist[i][j] = cnt
	
	for i in range(len(targets)):
		cnt = fint_distance_to_target(start_pos, targets[i])
		dist[len(targets)][i] = cnt
		dist[i][len(targets)] = cnt
	dist[len(targets)][len(targets)] = 0
	check = [False for _ in range(len(targets))]
	result = INF
	make_combination(0, len(targets), len(targets), 0)
	if result != INF:
		print(result)
	else:
		print(-1)

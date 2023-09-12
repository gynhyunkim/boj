from sys import stdin
from collections import deque

def bfs(x, y):
	q = deque([(x, y)])
	while q:
		x, y = q.popleft()
		for next in range(n + 2):
			if not visited[next]:
				next_x, next_y = coord[next]
				if abs(next_x - x) + abs(next_y - y) <= 1000:
					q.append((next_x, next_y))
					visited[next] = 1
	
t = int(stdin.readline())

for _ in range(t):
	n = int(stdin.readline())
	coord = [list(map(int, stdin.readline().split())) for _ in range(n + 2)]
	visited = [1] + [0] * (n + 1)
	bfs(coord[0][0], coord[0][1])
	print("happy" if visited[-1] else "sad") 

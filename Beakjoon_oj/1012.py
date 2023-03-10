# 유기농 배추
import sys
from sys import stdin
sys.setrecursionlimit(10000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
def DFS(x, y):
	if x < 0 or x >= m or y < 0 or y >= n:
		return 
	if field[y][x] == 1:
		field[y][x] = 0
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			DFS(nx, ny)

t = int(stdin.readline())
result = [0] * t
for i in range(t):
	m, n, k = map(int, stdin.readline().split())
	field = [[0] * m for _ in range(n)]

	for _ in range(k):
		x, y = map(int, stdin.readline().split())
		field[y][x] = 1
	for x in range(m):
		for y in range(n):
			if field[y][x] == 1:
				DFS(x, y)
				result[i] += 1

print(*result, sep = '\n')

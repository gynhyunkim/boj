# 좌표 정렬
import sys

n = int(sys.stdin.readline())
coord = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

coord.sort()

for i in range(n):
	print(*coord[i])
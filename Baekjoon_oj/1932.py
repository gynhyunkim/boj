# 정수 삼각형
import sys

n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
	for j in range(n - i):
		tri[n - i - 1][j] += max(tri[n - i][j], tri[n - i][j + 1])

print(tri[0][0])
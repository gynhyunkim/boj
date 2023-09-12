# 회의실 배정

import sys

n = int(sys.stdin.readline())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

times.sort()
prev = 0
result = 0

for i in range(0, n):
	if prev > times[i][1]:
		prev = times[i][1]
	elif prev <= times[i][0]:
		prev = times[i][1]
		result += 1

print(result)

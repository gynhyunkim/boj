from sys import stdin

fees = [0] + list(map(int, stdin.readline().split()))
cars = [0] * 100
time = [list(map(int, stdin.readline().split())) for _ in range(3)]
first = 101
last = 0
for start, end in time:
	cars[start : end] = [cars[x] + 1 for x in range(start, end)]
	first = min(start, first)
	last = max(end, last)

total = 0
for i in range(first, last):	
	total += cars[i] * fees[cars[i]]
print(total)

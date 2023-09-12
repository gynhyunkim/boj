import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
	cmd = sys.stdin.readline()
	size = int(sys.stdin.readline())
	dq = deque()
	for num in sys.stdin.readline().split():
		dq.append(int(num))
	for c in cmd:
		if c == 'R':
			dq.sort(reverse=True)
		elif dq and c == 'D':
			dq.pop()
		else:
			print("error")
			continue
	print(dq)


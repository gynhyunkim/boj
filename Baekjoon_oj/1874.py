# 스택 수열
import sys
from collections import deque

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
stack = deque()
result = []
cur = 1
for num in nums:
	while cur <= num:
		stack.append(cur)
		result.append("+")
		cur += 1
	if stack and stack[-1] == num:
		stack.pop()
		result.append("-")
	else:
		print("NO")
		result.clear()
		break
		

for r in result:
	print(r)
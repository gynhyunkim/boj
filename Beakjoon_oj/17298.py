# 오큰수
import sys
from collections import deque

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(n)]
stack = deque()

stack.append(0)
for i in range(1, n):
	while stack and nums[stack[-1]] < nums[i]:
		result[stack.pop()] = nums[i]
	stack.append(i)

print(*result)
		
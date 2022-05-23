# ATM

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

sum = 0
for i in range(n, 0, -1):
	sum += arr[n - i] * i
print(sum)

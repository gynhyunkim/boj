from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
dp = [0] * (100002)

q = deque([N])
while q:
	d = q.popleft()
	if K == d:
		print(dp[K])
		break
	for i in (d - 1, d + 1, d * 2):
		if 0 <= i < 100001 and dp[i] == 0:
			dp[i] = dp[d] + 1
			q.append(i)

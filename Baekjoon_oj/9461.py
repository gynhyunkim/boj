from sys import stdin

T = int(stdin.readline())
P = [0, 1, 1]
for _ in range(T):
	N = int(stdin.readline())
	dp = P + [0] * (N - 2)
	for i in range(3, N + 1):
		dp[i] = dp[i - 2] + dp[i - 3]
	print(dp[N])

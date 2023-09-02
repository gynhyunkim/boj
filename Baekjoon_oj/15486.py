from sys import stdin

N = int(stdin.readline())
t, p = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
	t[i], p[i] = map(int, stdin.readline().split())

dp = [0] * (N + 1)

for i in range(1, N + 1):
	dp[i] = max(dp[i], dp[i - 1])
	fin_date = i + t[i] - 1
	if fin_date <= N:
		dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])

print(max(dp))
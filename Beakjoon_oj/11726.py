from sys import stdin

n = int(stdin.readline())

dp = [1] + [2] * n

for i in range(2, n):
	dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

print(dp[n - 1])

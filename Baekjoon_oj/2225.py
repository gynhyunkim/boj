from sys import stdin

MOD = 1000000000
N, K = map(int, stdin.readline().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]
dp[0][0] = 1

for i in range(1, K + 1):
	for j in range(N + 1):
		dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		dp[i][j] %= MOD

print(dp[K][N])
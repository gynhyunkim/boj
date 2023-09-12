from sys import stdin

MOD = 1_000_000_000
MAX = (1 << 10) - 1

n = int(stdin.readline())

def get_stair_count():
	dp = [[0] * (MAX + 1) for _ in range(10)]
	for i in range(1, 10):
		dp[i][1 << i] = 1

	for _ in range(2, n + 1):
		next_dp = [[0] * (MAX + 1) for _ in range(10)]

		for i in range(10):
			for j in range(MAX + 1):
				if i > 0:
					next_dp[i][j | (1 << i)] = (
						next_dp[i][j | (1 << i)] + dp[i - 1][j]) % MOD
				if i < 9:
					next_dp[i][j | (1 << i)] = (
						next_dp[i][j | (1 << i)] + dp[i + 1][j]) % MOD
		dp = next_dp
	return sum(dp[i][MAX] for i in range(10)) % MOD

print(get_stair_count())
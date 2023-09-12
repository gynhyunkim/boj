from sys import stdin

n, k = map(int, stdin.readline().split())
value = [int(stdin.readline()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for v in value:
	for i in range(v, k + 1):
		if i - v >= 0:
			dp[i] += dp[i - v]
print(dp[k])

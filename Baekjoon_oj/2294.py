from sys import stdin

n, k = map(int, stdin.readline().split())
coin = [int(stdin.readline()) for _ in range(n)]
dp = [float('inf')] * (k + 1)

for i in range(1, k + 1):
	for c in coin:
		if i == c:
			dp[i] = 1
		elif i > c:
			dp[i] = min(dp[i], dp[c] + dp[i - c])
print(dp[k] if dp[k] < float('inf') else -1)

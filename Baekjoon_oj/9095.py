from sys import stdin

T = int(stdin.readline())

def dfs(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	else:
		dp[n] = dfs(n - 1) + dfs(n - 2) + dfs(n - 3)
		return dp[n]

for _ in range(T):
	n = int(stdin.readline())
	dp = [0] * (n + 1)
	print(dfs(n))

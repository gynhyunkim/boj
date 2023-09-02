from sys import stdin

INF = float('inf')
N = int(stdin.readline())
scale = [0] + list(map(int, stdin.readline().split()))
dp = [[INF] * (N + 1) for _ in range(N + 1)]
dp[1][0] = 0
dp[0][1] = 0

for i in range(N):
	for j in range(N):
		if i == j:
			continue
		next = max(i, j) + 1
		if j == 0 or i == 0:
			scale[0] = scale[next]
		dp[next][j] = min(dp[next][j], dp[i][j] + abs(scale[next] - scale[i]))
		dp[i][next] = min(dp[i][next], dp[i][j] + abs(scale[next] - scale[j]))

answer = INF
for i in range(N):
	answer = min(min(answer, dp[i][N]), dp[N][i])

print(answer)


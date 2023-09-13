from sys import stdin

N = int(stdin.readline())
T, P = [], []
for _ in range(N):
	t, p = map(int, stdin.readline().split())
	T.append(t)
	P.append(p)

dp = [0] * (N + 1)

for i in range(N):
	for j in range(i + T[i], N + 1):
		dp[j] = max(dp[j], dp[i] + P[i])

print(dp[N])

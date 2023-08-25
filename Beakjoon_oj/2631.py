from sys import stdin

N = int(stdin.readline())
children = [0] + [int(stdin.readline()) for _ in range(N)]
dp = [1] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))

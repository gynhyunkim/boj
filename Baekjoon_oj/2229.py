import sys

N = int(sys.stdin.readline())
score = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j - 1] + max(score[j:i + 1]) - min(score[j:i + 1]))
print(dp[-1])
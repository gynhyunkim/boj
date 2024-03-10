import sys

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    dp = [[i for i in range(n + 1)] for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = sum(dp[i - 1][:j + 1])
    print(dp[k][n])


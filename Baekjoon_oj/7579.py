from sys import stdin

INF = float('inf')
N, M = map(int, stdin.readline().split())
memories = [0] + list(map(int, stdin.readline().split()))
cost = [0] + list(map(int, stdin.readline().split()))

total_cost = sum(cost)
dp = [[0 for _ in range(total_cost + 1)] for _ in range(N + 1)]
result = INF

for i in range(1, N + 1):
    for j in range(0, total_cost + 1):
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(dp[i - 1][j], memories[i] + dp[i - 1][j - cost[i]])
        if dp[i][j] >= M:
            result = min(result, j)
if total_cost == 0:
    result = 0
print(result)

from sys import stdin

N = int(stdin.readline())
R, G, B = 0, 1, 2
cost = [list(map(int, stdin.readline().split())) for _ in range(N)]
INF = float("inf")
ans = INF
for color in [R, G, B]:
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][color] = cost[0][color]
    for i in range(1, N):
        dp[i][R] = cost[i][R] + min(dp[i - 1][G], dp[i - 1][B])
        dp[i][G] = cost[i][G] + min(dp[i - 1][R], dp[i - 1][B])
        dp[i][B] = cost[i][B] + min(dp[i - 1][R], dp[i - 1][G])
    dp[-1][color] = INF
    ans = min(ans, mint(dp[-1]))
print(ans)


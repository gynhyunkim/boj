from sys import stdin

N, K = map(int, stdin.readline().split())
stuff = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [0] * (K + 1)
stuff.sort()

for W, V in stuff:
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
print(dp[K])       


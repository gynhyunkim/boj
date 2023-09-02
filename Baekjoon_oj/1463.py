n = int(input())
dp = [0, 0, 1, 1]

for i in range(4, n + 1):
    dp.append(dp[i - 1])
    if i % 2 == 0 and dp[i // 2] < dp[i]:
        dp[i] = dp[i // 2]
    if i % 3 == 0 and dp[i // 3] < dp[i]:
        dp[i] = dp[i // 3]
    dp[i] = dp[i] + 1
print(dp[n])
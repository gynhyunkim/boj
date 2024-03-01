import sys

MOD = 1_000_000
code = [0] + [int(s) for s in sys.stdin.readline().strip()]
n = len(code)

dp = [1] + [0] * (n - 1)
for i in range(1, n):
    if code[i] == 0 and code[i - 1] == 0:
        dp[-1] = 0
        break
    if code[i] > 0:  
        dp[i] += dp[i - 1]
    if i - 2 >= 0 and code[i - 1] != 0 and code[i - 1] * 10 + code[i] < 27:
        dp[i] += dp[i - 2]
    dp[i] %= MOD
print(dp[-1])

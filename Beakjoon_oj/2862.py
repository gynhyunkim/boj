from sys import stdin

N = int(stdin.readline())
dp = [0, 1]
for i in range(2, N + 1):
	dp.append(dp[i - 2] + dp[i - 1])
	if dp[i] > N:
		break
print(dp)
for i in range(len(dp) - 1, 2, -1):
	if N < dp[i]:
		continue
	elif N == dp[i]:
		break
	N -= dp[i]

print(N)

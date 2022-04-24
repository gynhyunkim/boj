# 계단 오르기
import sys

n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(n)]
dp = []

dp.append(stairs[0])
dp.append(max(stairs[0] + stairs[1], stairs[1]))
dp.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
for i in range(3, n):
	dp.append(max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]))
	
print(dp.pop())
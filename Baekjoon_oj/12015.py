from sys import stdin
import bisect

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

dp = [A[0]]

for i in range(N):
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]

print(len(dp))

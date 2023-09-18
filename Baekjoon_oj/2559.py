from sys import stdin

N, K = map(int, stdin.readline().split())
temp = list(map(int, stdin.readline().split()))
pre = [0] * (N + 1)
for i in range(1, N + 1):
	pre[i] += pre[i - 1] + temp[i - 1]

ans = -100 * 100000 + 1
for i in range(K, N + 1):
	ans = max(ans, pre[i] - pre[i - K])
print(ans)
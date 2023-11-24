from sys import stdin
# 박수를 치는 춘배의 모습
# https://www.acmicpc.net/contest/problem/1151/3
N, K = map(int, stdin.readline().split())
X = list(map(int, stdin.readline().split()))

prev = 0
cnt = 0
for x in X:
	if prev < x:
		prev = x + K
		cnt += 1
print(cnt)

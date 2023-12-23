from sys import stdin
from heapq import heappush, heappop

N, M = map(int, stdin.readline().split())
sub = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    sub[A].append(B)
    degree[B] += 1
q = []
for i in range(1, N + 1):
    if not degree[i]:
        heappush(q, i)

while q:
    prior = heappop(q)
    print(prior, end = ' ')
    for s in sub[prior]:
        degree[s] -= 1
        if not degree[s]:
            heappush(q, s)

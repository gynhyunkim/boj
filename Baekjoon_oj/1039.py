from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
length = len(str(N))
q = deque([(N, 0)])
visited = set()
visited.add((N, 0))
answer = 0
while q:
    n, k = q.popleft()
    if k == K:
        answer = max(answer, n)
        continue
    n = list(str(n))
    for i in range(length - 1):
        for j in range(i + 1, length):
            if i == 0 and n[j] == '0':
                continue
            n[i], n[j] = n[j], n[i]
            temp = int(''.join(n))
            if (temp, k + 1) not in visited:
                q.append((temp, k + 1))
                visited.add((temp, k + 1))
            n[i], n[j] = n[j], n[i]
print(answer if answer else -1)

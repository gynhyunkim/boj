# 동전0

import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
result = 0

coins.sort(reverse=True)
for c in coins:
    if k == 0:
        break
    if c <= k:
        result += k // c
        k = k % c
        
print(result)
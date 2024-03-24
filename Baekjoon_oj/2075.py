from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())

pq = []
for _ in range(N):
    for num in list(map(int, sys.stdin.readline().split())):
        heappush(pq, num)
        if len(pq) > N:
            heappop(pq)
print(heappop(pq))


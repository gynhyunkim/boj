# 최대 힙
import sys
import heapq

n = int(sys.stdin.readline())
input = [int(sys.stdin.readline()) for _ in range(n)]
heap = []

for i in input:
	if i == 0:
		print(heapq.heappop(heap)[1] if heap else 0)
	else:
		heapq.heappush(heap, (-i, i))


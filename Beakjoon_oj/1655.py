#가운데를 말해요
import sys
import heapq

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
max_heap = []
min_heap = []

for num in nums:
	if len(min_heap) == len(max_heap):
		heapq.heappush(max_heap, (-num, num))
	else:
		heapq.heappush(min_heap, num)
	if min_heap and min_heap[0] < max_heap[0][1]:
		tmp = heapq.heappop(min_heap)
		heapq.heappush(min_heap, heapq.heappop(max_heap)[1])
		heapq.heappush(max_heap, (-tmp, tmp))
	print(max_heap[0][1] if max_heap else min_heap[0])

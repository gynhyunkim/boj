from sys import stdin
import heapq as hq

N, C = map(int, stdin.readline().split())
points = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]

def prim(start):
	heap = list()
	visited = [False] * N 
	sum_w = 0
	hq.heappush(heap, (0, start))
	
	while heap and False in visited:
		weight, v = hq.heappop(heap)
		if not visited[v]:
			visited[v] = True
			sum_w += weight
			for i in [i for i, v in enumerate(visited) if not v]:
				distance = (points[i][0] - points[v][0]) ** 2 + (points[i][1] - points[v][1]) ** 2
				if i != v and not visited[i] and distance >= C:
					hq.heappush(heap, (distance, i))
	return sum_w if False not in visited else -1

print(prim(0))
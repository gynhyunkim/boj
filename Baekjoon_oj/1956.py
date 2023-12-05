from sys import stdin
from heapq import heappush, heappop

# 플루이드 워샬
INF = float('inf')
V, E = map(int, stdin.readline().split())
dist = [[INF for i in range(V + 1)] for j in range(V + 1)]

for _ in range(E):
	a, b, c = map(int, stdin.readline().split())
	dist[a][b] = c


for k in range(1, V + 1):
	for a in range(1, V + 1):
		for b in range(1, V + 1):
			dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

answer = INF
for v in range(1, V + 1):
	answer = min(answer, dist[v][v])
print(answer if answer != INF else -1)


# 다익스트라
# INF = float('inf')
# V, E = map(int, stdin.readline().split())
# dist = [[INF for i in range(V + 1)] for j in range(V + 1)]
# heap = []
# edge = [[] for _ in range(V + 1)]


# for _ in range(E):
# 	a, b, c = map(int, stdin.readline().split())
# 	if dist[a][b] > c:
# 		dist[a][b] = min(dist[a][b], c)

# visited = [False for _ in range(V + 1)]

# heappush(heap, [dist[1][2], 1, 2])

# while heap:
# 	w, start, end = heappop(heap)
# 	if start == end:
# 		print(w)
# 		break
# 	if w != dist[start][end]:
# 		continue
# 	for next_end in range(1, V + 1):
# 		if dist[start][next_end] > dist[start][end] + dist[end][next_end]:
# 			dist[start][next_end] = dist[start][end] + dist[end][next_end]
# 			heappush(heap, [dist[start][next_end], start, next_end])
# else:
# 	print(-1)



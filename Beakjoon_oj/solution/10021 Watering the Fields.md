#MST

# 문제
https://www.acmicpc.net/problem/10021

# 코드
```python
```

# 정리
- Spanning Tree(신장 트리)란 그래프 내의 모든 정점을 포함하는 트리이다.
- Spanning Tree는 그래프의 최소 연결 부분 그래프이다. 최소 연결은 간선의 수가 가장 적다는 것을 뜻한다.
- n개의 정점을 가지는 그래프의 최소 간선의 수는 (n - 1)개이고, (n - 1)개의 간선으로 연결되어 있으면 필연적으로 트리 형태가 되고 이것이 바로 Spanning Tree가 된다.
- DFS, BFS를 이용하여 그래프에서 Spannign Tree를 찾을 수 있다.
- Spanning Tree는 트리의 특수한 형태이므로 모든 정점들이 연결되어 있어야 하고 사이클을 포함해서는 안된다.
- Kruskal MST 알고리즘
	- 낮은 비용의 간선부터 차례로 선택하되, 간선의 선택으로 인해 기존의 선택된 간선들과 함께 사이클이 형성되는 경우는 제외시키는 방법
	- greedy  method를 이용하여 네트워크 (가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 것이다.
	- 동작 방식
		1. 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
		2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
			- 즉, 가장 낮은 가중치를 먼저 선택한다.
			- 사이클을 형성하는 간선을 제외한다.
		3. 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
- 해당 문제에 Prim 알고리즘 적용하기
	- 각 간선의 가중치 구하기
	- 가중치를 우선순위 큐에 넣어서 최소 값이면서 사이클이 생성되지 않는 간선 선택하기
	- 선택이 완료되면 모든 정점이 연결되었는지 확인하고 총합 출력, 모든 정점을 연결할 수 없다면 `-1` 출력
# 코드
```python
from sys import stdin
import heapq as hq
from collections import defaultdict

N, C = map(int, stdin.readline().split())
points = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
graph = defaultdict(list)

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
			for i, w in graph[v]:
				if not visited[i]:
					hq.heappush(heap, (w, i))
	return sum_w if False not in visited else -1

for i in range(N):
	for j in range(i + 1, N):
		distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
		if distance >= C:
			graph[i].append([j, distance])
			graph[j].append([i, distance])
print(prim(0))
```
- 메모리 초과 발생... N * N개의 간선을 저장해서 발생
- 간선을 메모리에 저장하지 않고 풀이하도록 수정
```python
from sys import stdin
import heapq as hq
from collections import defaultdict

N, C = map(int, stdin.readline().split())
points = [list(map(int, stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
graph = defaultdict(list)

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
			for i in range(N):
				distance = (points[i][0] - points[v][0]) ** 2 + (points[i][1] - points[v][1]) ** 2
				if i != v and not visited[i] and distance >= C:
					hq.heappush(heap, (distance, i))
	return sum_w if False not in visited else -1

print(prim(0))
```
- pypy3 통과
## References
https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html
# # 바이러스
# import sys

# def dfs(g, r):
# 	global cnt
# 	visited[r] = True
# 	for c in g[r]:
# 		if not visited[c]:
# 			cnt += 1
# 			dfs(g, c)


# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# visited = [False] * n

# graph = [[] for _ in range(n)]

# for _ in range(m):
# 	i, j = map(int, sys.stdin.readline().split())
# 	graph[i- 1].append(j - 1)
# 	graph[j - 1].append(i - 1)

# cnt = 0
# dfs(graph, 0)
# print(cnt)

from collections import deque
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
visited = [False] * (N + 1)
q = deque([1])
visited[1] = True
while q:
    curr = q.popleft()
    for com in graph[curr]:
        if not visited[com]:
            q.append(com)
            visited[com] = True
            answer += 1


print(answer)
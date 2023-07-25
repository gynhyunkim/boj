from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def BFS(v):
        visited = [False] * (n + 1)
        q = deque([v])
        cnt = 1
        while q:
            curr = q.popleft()
            for next in graph[curr]:
                if not visited[next]:
                    q.append(next)
                    visited[curr] = True
                    cnt += 1
        return cnt
    
    answer = n
    for i,v in wires:
        graph[i].remove(v)
        graph[v].remove(i)          
        answer = min(abs(n - BFS(i) * 2), answer) 
        graph[i].append(v)
        graph[v].append(i)
    
    return answer


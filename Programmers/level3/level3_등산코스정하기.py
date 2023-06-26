from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    INF = float('inf')
    graph = defaultdict(list)
    heap = []
    inten_info = [INF] * (n + 1)
    summits = set(summits)
    
    for g in gates:
        heappush(heap, (0, g))
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    while heap:
        inten, path = heappop(heap)
        if path in summits or inten > inten_info[path]:
            continue
        for next_path, next_inten in graph[path]:
            intensity = max(inten, next_inten)
            if intensity < inten_info[next_path]:
                inten_info[next_path] = intensity
                heappush(heap, (intensity, next_path))
    answer = []
    for s in summits:
        answer.append([s, inten_info[s]])
    answer.sort(key = lambda x: (x[1], x[0]))
    return answer[0]


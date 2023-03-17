def solution(n, costs):
    def union(a, b):
        x = find(a)
        y = find(b)
        if x != y:
            bridge[x] = y
        
    def find(x):
        if bridge[x] == x:
            return x
        else:
            bridge[x] = find(bridge[x])
            return bridge[x]
        
    answer = 0
    bridge = [i for i in range(n)]
    costs.sort(key = lambda x:x[2])
    
    for cost in costs:
        if find(cost[0]) != find(cost[1]):
            union(cost[0], cost[1])
            answer += cost[2]
    
    return answer


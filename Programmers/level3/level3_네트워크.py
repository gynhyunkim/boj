from collections import deque
def solution(n, computers):
    answer = 0
    
    def BFS(q):
        while q:
            i = q.popleft()
            for j, com in enumerate(computers[i]):
                if com and computers[j][j]:
                    q.append(j)
                    computers[j][j] = 0
        
    for i in range(n):
        if computers[i][i]:
            q = deque()
            q.append(i)
            computers[i][i] = 0
            BFS(q)
            answer += 1
    return answer


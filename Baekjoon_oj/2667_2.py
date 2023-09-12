from sys import stdin

N = int(stdin.readline())
graph = [list(map(int, stdin.readline().strip('\n'))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
count = 0
def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 
    global count
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            DFS(x + dx[i], y + dy[i])

for i in range(N):
    for j in range(N):
        DFS(i, j)
        if count > 0:
            answer.append(count)
            count = 0
print(len(answer))
print(*answer, sep='\n')
    

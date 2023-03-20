from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 1))
    while q:
        y, x, distance = q.popleft()
        if y == n - 1 and x == m - 1:
            return distance
        if maps[y][x]:
            maps[y][x] = 0
            for i in range(4):
                if y + dy[i] < n and y + dy[i] >= 0 and x + dx[i] < m and x + dx[i] >= 0:
                    q.append([y + dy[i], x + dx[i], distance + 1])
    return -1 


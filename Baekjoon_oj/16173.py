# import sys

# sys.setrecursionlimit(10 ** 6)
# N = int(sys.stdin.readline())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp = [[-1] * N for _ in range(N)]
# def dfs(x, y):
#     if not 0 <= x < N or not 0 <= y < N:
#         return False
#     if x == N - 1 and y == N - 1:
#         return True
#     if dp[x][y] != -1:
#         return dp[x][y]
    
#     move = board[x][y]
#     dp[x][y] = (dfs(x + move, y) or dfs(x, y + move))
#     return dp[x][y]

# print("HaruHaru" if dfs(0, 0) else "Hing")

import sys
from collections import deque
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, 0]
dy = [0, 1]
def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited = [[False] * N for _ in range(N)]
    while q:
        x, y = q.popleft()
        if x == N - 1 and y == N - 1:
            return True
        move = board[x][y]
        for i in range(2):
            new_x, new_y = x + dx[i] * move, y + dy[i] * move
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
    return False

print("HaruHaru" if bfs(0, 0) else "Hing")
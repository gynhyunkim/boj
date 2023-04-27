from collections import deque

def dp(q):
    dt = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    
    x, y, path, cnt = q.popleft()
        if (x, y) == (r, c) and (k - cnt) % 2 == 1 or abs(x - r) + abs(y - c) > k:
            return "impossible"
        if (x, y) == (r, c) and k == cnt:
            return path
        for i in range(4):
            dx, dy, direction = dt[i]
            nx = x + dx
            ny = y + dy
            if nx > 0 and nx <= n and ny > 0 and ny <= m and abs(nx - r) + abs(ny - c) + cnt + 1 <= k:
                q.append((nx, ny, path + direction, cnt + 1))
                dp(q)
        

def solution(n, m, x, y, r, c, k):
    answer = ''
    q = deque([(x, y, "", 0)]) 
    
    dp(q)
                
    return answer
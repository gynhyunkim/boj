def solution(board, skill):
    n = len(board)
    m = len(board[0])
    prefix = [[0] * m for _ in range(n)]
    for stype, r1, c1, r2, c2, degree in skill:
        if stype == 1:
            degree = -degree
        prefix[r1][c1] += degree
        if c2 + 1 < m:
            prefix[r1][c2 + 1] += -degree
        if r2 + 1 < n:
            prefix[r2 + 1][c1] += -degree
        if r2 + 1 < n and c2 + 1 < m:    
            prefix[r2 + 1][c2 + 1] += degree
    
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j - 1]
    
    for i in range(1, n):
        for j in range(m):
            prefix[i][j] += prefix[i - 1][j]
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + prefix[i][j] > 0:
                cnt += 1
    return cnt


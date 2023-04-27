from collections import deque

def is_in_rect(rectangle, x, y):
        for x1, y1, x2, y2 in rectangle:
            if x1 < x and x < x2 and y1 < y and y < y2:
                return True
        return False
    
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    dt = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    max_x = 0
    max_y = 0
    
    rectangle = list(map(lambda x: list(map(lambda y: y*2, x)), rectangle))
    # 맵 생성을 위해서 모든 사각형을 담을 수 있는 최대 범위 구하기
    for x1, y1, x2, y2 in rectangle:
        max_x = max(x2, max_x)
        max_y = max(y2, max_y)
    # 맵 생성
    maps = [[0] * (max_x + 1) for i in range(max_y + 1)]
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                maps[i][j] = -1
    q = deque([(characterX * 2, characterY * 2, 0)])
    while q:
        x, y, length = q.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return length // 2
        for i in range(4):
            dx, dy = x + dt[i][0], y + dt[i][1]
            if dx <= max_x and dy <= max_y and maps[dy][dx] == -1 and not is_in_rect(rectangle, dx, dy):
                maps[dy][dx] = 1
                q.append((dx, dy, length + 1))

    return answer


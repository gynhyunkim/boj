import sys

N, M = map(int, sys.stdin.readline().split())
status = [0] + list(map(int, sys.stdin.readline().split()))

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        status[b] = c 
    elif a == 2:
        for i in range(b, c + 1):
            status[i] = 0 if status[i] else 1
    elif a == 3:
        for i in range(b, c + 1):
            status[i] = 0
    elif a == 4:
        for i in range(b, c + 1):
            status[i] = 1
print(*status[1:])
from sys import stdin
from collections import deque

INF = float('inf')

def dijkstra():
    time = [INF] * (n + 1)
    time[c] = 0
    count, end_time = 0, 0

    q = deque([[c, 0]])
    while q:
        curr_computer, curr_time = q.popleft()
        if curr_time < time[curr_computer]:
            continue

        for next_computer, next_time in connect[curr_computer]:
            if curr_time + next_time < time[next_computer]:
                time[next_computer] = curr_time + next_time
                q.append([next_computer, curr_time + next_time])
    for t in time:
        if t < INF:
            count += 1
            if t > end_time:
                end_time = t
    print(count, " ", end_time)
                

t = int(stdin.readline())
for _ in range(t):
    n, d, c = map(int, stdin.readline().split())
    connect = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, stdin.readline().split())
        connect[b].append([a, s])
    dijkstra()

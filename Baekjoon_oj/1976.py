from sys import stdin
from collections import deque

N = int(stdin.readline())
M = int(stdin.readline())

connect = [list(map(int, stdin.readline().split())) for _ in range(N)]
plan = list(map(int, stdin.readline().split()))

course = []
q = deque([plan[0] - 1])
while q:
    curr = q.popleft()
    course.append(curr + 1)
    for i in range(N):
        if connect[curr][i] == 1 and i + 1 not in course:
            q.append(i)
result = "YES"
for p in plan:
    if p not in course:
       result = "NO"
       break

print(result)


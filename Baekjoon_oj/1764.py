from sys import stdin

N, M = map(int, stdin.readline().split())
people = dict()
result = []
for _ in range(N):
    name = stdin.readline().rstrip()
    people[name] = 0
for _ in range(M):
    name = stdin.readline().rstrip()
    if name in people:
        result.append(name)
        
result.sort()
print(len(result))
print('\n'.join(result))

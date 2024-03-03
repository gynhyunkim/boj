import sys

N = int(sys.stdin.readline())
_min = [0, 0, 0]
_max = [0, 0, 0]

for _ in range(N):
    curr = list(map(int, sys.stdin.readline().split()))
    _min = [curr[0] + min(_min[:2]), curr[1] + min(_min), curr[2] + min(_min[1:3])]
    _max = [curr[0] + max(_max[:2]), curr[1] + max(_max), curr[2] + max(_max[1:3])]
print(max(_max), min(_min))

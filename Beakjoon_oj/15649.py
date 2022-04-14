import sys

n, m = map(int, sys.stdin.readline().split())
seq = []

def backtracking():
    if len(seq) == m:
        print(*seq)
    for i in range(1, n + 1):
        if i not in seq:
            seq.append(i)
            backtracking()
            seq.pop()

backtracking()
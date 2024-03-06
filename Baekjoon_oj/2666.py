import sys

n = int(sys.stdin.readline())
opened = list(map(int, sys.stdin.readline().split()))
seq_n = int(sys.stdin.readline())
seq = [int(sys.stdin.readline()) for _ in range(seq_n)]

dp = [[[-1] * (n + 1) for _ in range(n + 1)] for _ in range(seq_n)]

def solve(order, opened1, opened2):
    if order == seq_n:
        return 0
    if dp[order][opened1][opened2] > -1:
        return dp[order][opened1][opened2]
    
    opened1_cnt = solve(order + 1, seq[order], opened2) + abs(seq[order] - opened1)
    opened2_cnt = solve(order + 1, opened1, seq[order]) + abs(seq[order] - opened2)
    dp[order][opened1][opened2] = min(opened1_cnt, opened2_cnt)
    return dp[order][opened1][opened2]

print(solve(0, opened[0], opened[1]))

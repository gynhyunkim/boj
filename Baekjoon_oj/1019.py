from sys import stdin

N = int(stdin.readline())
result = [0] * 10
num = 1
def make_nine(N):
    while N % 10 != 9:
        for i in str(N):
            result[int(i)] += num
        N -= 1
    return N

while N > 0:
    N = make_nine(N)
    if N < 10:
        for i in range(N + 1):
            result[i] += num
    else:
        for i in range(10):
            result[i] += (N // 10 + 1) * num
    result[0] -= num
    num *= 10
    N //= 10
print(*result)


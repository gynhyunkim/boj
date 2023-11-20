from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort(reverse = True)
B.sort()

answer = 0
for i in range(N):
    answer += A[i] * B[i]
print(answer)


from sys import stdin
A, P = map(int, stdin.readline().split())
D = [0] * 250000
D[A] = 1

def DFS(A, cnt):
    num = 0
    for n in str(A):
        num += int(n) ** P
    if D[num] != 0:
        print(D[num] - 1)
        return
    else:
        cnt += 1
        D[num] = cnt
        DFS(num, cnt)

DFS(A, D[A])
# while True:
#     num = 0
#     index += 1
#     for n in str(D[index - 1]):
#         num += int(n) ** P

#     if num in D:
#         print(D.index(num) - 1)
#         break
#     else:
#         D[index] = num

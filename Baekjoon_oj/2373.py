from sys import stdin

N = int(stdin.readline())
fibo = [0, 1]
for i in range(2, 75):
    fibo.append(fibo[i - 2] + fibo[i - 1])
    if fibo[i] >= N:
        break

if N == fibo[-1]:
    print(-1)
else:
    for i in range(len(fibo) - 1, 2, -1):
        if fibo[i] > N:
            continue
        elif fibo[i] == N:
            break
        N -= fibo[i]
    print(N)g
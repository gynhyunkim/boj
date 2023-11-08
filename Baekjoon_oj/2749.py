from sys import stdin

N = int(stdin.readline())
mod = 1000000
p = mod//10 * 15;
fibo = [0, 1] + [0] * (p - 2);
for i in range(2, p):
    fibo[i] = fibo[i - 1] + fibo[i - 2];
    fibo[i] %= mod;
print(fibo[N % p])


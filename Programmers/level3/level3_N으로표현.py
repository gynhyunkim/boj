def calculate(A, B):
    result = set()
    for a in A:
        for b in B:
            result.add(a + b)
            result.add(a - b)
            result.add(a * b)
            if b != 0:
                result.add(a // b)
    return result

def solution(N, number):
    dp = dict()
    for i in range(1, 9):
        dp[i] = set([int(str(N) * i)])
        for j in range(1, i):
            dp[i].update(calculate(dp[j], dp[i - j]))
        if number in dp[i]:
            return i
    return -1


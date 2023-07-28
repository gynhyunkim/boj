import math
def solution(n, k):
    answer = []
    num = [x for x in range(1, n + 1)]
    for i in range(1, n + 1):
        i_fact = math.factorial(n - i)
        r = k // i_fact
        r = r - 1 if k % i_fact == 0 else r
        k %= i_fact
        answer.append(num[r])
        num.remove(num[r])
    return answer


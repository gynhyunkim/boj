from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    nums = dict()
    for i in range(1, len(numbers) + 1):
        nums.update(dict.fromkeys(list(map(int, map(''.join, permutations(numbers, i)))), 0))
    for num in nums.keys():
        answer = answer + 1 if is_prime(num) else answer    
    return answer
  

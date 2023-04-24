def binary(num, b_num):
    if num == 0:
        return
    binary(num // 2, b_num)
    b_num.append(num % 2)
    
def DFS(b_num):
    if not len(b_num):
        return 1
    root = len(b_num) // 2
    left = root // 2
    right = root + (root - left)
    if b_num[root] == 0 and (b_num[left] == 1 or b_num[right] == 1):
        return 0
    return DFS(b_num[:root]) and DFS(b_num[root + 1:])

def find_n(b_num):
    n = 2
    while len(b_num) > 2 ** n - 1:
        n += 1
    return n

def solution(numbers):
    answer = []
    for num in numbers:
        if num == 1:
            answer.append(1)
        else:
            b_num = []
            binary(num, b_num)
            n = find_n(b_num)
            b_num = [0 for i in range(2 ** n - 1 - len(b_num))] + b_num
            answer.append(DFS(b_num))
    return answer


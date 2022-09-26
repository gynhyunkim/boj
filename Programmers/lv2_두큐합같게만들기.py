def solution(queue1, queue2):
    answer = 0
    tq = queue1 + queue2
    target = sum(tq) // 2
    i = 0
    j = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    while i <= j and j < len(tq):
        if sum1 == target and sum2 == target:
            break 
        if sum1 > target:
            sum1 -= tq[i]
            sum2 += tq[i]
            i += 1
            answer += 1
        if sum2 > target:
            sum2 -= tq[j]
            sum1 += tq[j]
            j += 1
            answer += 1
    if j == len(tq) or i > j:
        return -1
    
    return answer

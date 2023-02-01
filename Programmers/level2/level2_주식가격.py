def solution(prices):
    answer = [0] * len(prices)
    stk = []
    for i in range(len(prices)):
        while stk and prices[stk[-1]] > prices[i]:
            idx = stk.pop()
            answer[idx] = i - idx
        stk.append(i)
    
    while stk:
        idx = stk.pop()
        answer[idx] = len(prices) - 1 - idx
    return answer

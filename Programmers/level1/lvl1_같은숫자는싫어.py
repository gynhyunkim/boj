def solution(arr):
    answer = []
    stk = []
    
    for a in arr:
        if not stk or stk[-1] != a:
            if stk:
                answer.append(stk.pop())
            stk.append(a)
    
    answer.append(stk.pop())
    return answer


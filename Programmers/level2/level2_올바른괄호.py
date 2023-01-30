def solution(s):
    stk = []
    for c in s:
        if c == '(':
            stk.append(c)
        else:
            if not stk or stk[-1] != '(':
                return False
            stk.pop()            
    return not stk

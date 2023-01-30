def solution(priorities, location):
    answer = 0
    while priorities:
        max_prior = max(priorities)
        if priorities[0] < max_prior:
            priorities.append(priorities.pop(0))
            location = len(priorities) - 1 if location == 0 else location - 1
        else:
            priorities.pop(0)
            answer += 1
            if location == 0:
                return answer
            location -= 1
    return answer


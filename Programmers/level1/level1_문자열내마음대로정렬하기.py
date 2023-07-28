def solution(strings, n):
    data = []
    for string in strings:
        data.append([string[n], string])
    data.sort()
    answer = [d[1] for d in data]
    return answer


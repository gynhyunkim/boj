def solution(sequence, k):
    answer = []
    length = len(sequence)
    n = sequence[0]
    idx = 0
    for i, v in enumerate(sequence):
        while n < k and idx <= length - 2:
            idx += 1
            n += sequence[idx]
        if n == k:
            answer.append([idx - i, [i, idx]])
        n -= v
    answer.sort()
    return answer[0][1]

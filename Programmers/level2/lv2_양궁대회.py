def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i:], r - 1):
                yield [arr[i]] + next
            

def solution(n, info):
    answer = [-1]
    max_gap = -1
    
    for combi in combinations(range(11), n):
        scores = [0] * 11;
        for c in combi:
            scores[10 - c] += 1
        apeach = 0
        lion = 0
        for i in range(11):
            if info[i] > 0 and info[i] >= scores[i]:
                apeach += 10 - i;
            elif scores[i] > 0 and info[i] < scores[i]:
                lion += 10 - i;
        if lion > apeach and max_gap < lion - apeach:
            max_gap = lion - apeach;
            answer = scores;
    return answer
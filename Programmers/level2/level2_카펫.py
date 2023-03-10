def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if brown == (width + height) * 2 + 4:
                return (sorted([width + 2, height + 2], reverse = True))


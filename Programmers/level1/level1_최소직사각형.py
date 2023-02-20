def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
        max_w = max(size[0], max_w)
        max_h = max(size[1], max_h)
    return max_w * max_h


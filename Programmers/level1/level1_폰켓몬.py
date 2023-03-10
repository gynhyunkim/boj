def solution(nums):
    N = len(nums) // 2
    items = dict()
    
    for n in nums:
        if n not in items:
            items[n] = 0
        items[n] += 1
    
    answer = N if N < len(items) else len(items)
    return answer

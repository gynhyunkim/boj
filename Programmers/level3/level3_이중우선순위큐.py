import heapq
def solution(operations):
    answer = [0, 0]
    min_heap = []
    max_heap = []
    
    for op in operations:
        op = op.split()
        if op[0] == 'I':
            heapq.heappush(min_heap, int(op[1]))
            heapq.heappush(max_heap, -int(op[1]))
        elif min_heap and op[1] == '-1':
            max_heap.remove(-heapq.heappop(min_heap))
        elif min_heap and op[1] == '1':
            min_heap.remove(-heapq.heappop(max_heap))
        
    if min_heap and max_heap:
        answer[0], answer[1] = -heapq.heappop(max_heap), heapq.heappop(min_heap)
    return answer


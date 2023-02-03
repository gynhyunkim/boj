import heapq
def solution(jobs):
    answer = 0
    time = 0
    length = len(jobs)
    jobs.sort()
    heap = []
    while jobs or heap:
        while jobs and jobs[0][0] <= time:
            heapq.heappush(heap, jobs.pop(0)[::-1])
        time = time if heap else jobs[0][0]
        if heap:
            process = heapq.heappop(heap)
            time += process[0]
            answer += time - process[1]
            
    return answer // length


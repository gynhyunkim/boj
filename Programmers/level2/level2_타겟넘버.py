answer = 0

def solution(numbers, target):
    def DFS(cnt, curr):
        global answer
        if curr == len(numbers):
            if cnt == target:
                answer += 1
            return 
        DFS(cnt + numbers[curr], curr + 1)
        DFS(cnt - numbers[curr], curr + 1)
        
    DFS(0, 0)
    return answer


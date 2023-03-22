from collections import deque

def solution(begin, target, words):
    visited = []
    def is_possible(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                cnt += 1
        return (cnt == len(word1) - 1)
    
    def BFS(q):
        while q:
            word, cnt = q.popleft()
            if word == target:
                return cnt
            for i, new_word in enumerate(words):
                if is_possible(word, new_word) and i not in visited:
                    q.append([new_word, cnt + 1])
                    visited.append(i)
                    
    answer = 0
    if target not in words:
        return answer
    q = deque()
    q.append([begin, 0])
    return BFS(q)


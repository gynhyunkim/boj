def solution(s):
    answer=s[int(len(s)/2)] if len(s)%2!=0 else s[int(len(s)/2-1):int(len(s)/2+1)]
    return answer

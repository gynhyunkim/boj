def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        result = ""
        cnt = 1
        tmp = s[:step]
        for i in range(step, len(s) + step, step):
            if tmp == s[i:i + step]:
                cnt += 1
            else:
                if cnt == 1:
                    result += tmp
                else:
                    result += str(cnt) + tmp
                tmp = s[i:i + step]
                cnt = 1
        answer = min(answer, len(result))
    return answer
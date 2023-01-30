def solution(record):
    answer = []
    user_info = dict()
    cmds = [list(r.split()) for r in record]
    
    for cmd in cmds:
        if cmd[0] == "Enter" or cmd[0] == "Change":
            user_info[cmd[1]] = cmd[2]
    
    for cmd in cmds:
        if cmd[0] == "Enter":
            answer.append(user_info[cmd[1]] + "님이 들어왔습니다.")
        elif cmd[0] == "Leave":
            answer.append(user_info[cmd[1]] + "님이 나갔습니다.")
            
    return answer
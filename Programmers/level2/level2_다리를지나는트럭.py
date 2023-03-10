def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        bridge.pop(0)
        answer += 1        
        if truck_weights:
            bridge.append(0 if sum(bridge) + truck_weights[0] > weight else truck_weights.pop(0))
    return answer


def solution(arr, divisor):
    answer = sorted([n for n in arr if n%divisor==0]) or [-1]
    return answer

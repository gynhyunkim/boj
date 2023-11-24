from math import gcd
def solution(w,h):
    answer = 1
    g = gcd(w, h)
    ww = w / g
    hh = h / g
    cut = ((ww * hh) - (ww - 1) * (hh - 1))
    answer = w * h - cut * g
    return answer
	
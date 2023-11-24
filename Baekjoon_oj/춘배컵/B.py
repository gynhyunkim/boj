from sys import stdin
# 무지개 만들기
# https://www.acmicpc.net/contest/problem/1151/2

UPPER_RAINBOW = "ROYGBIV"
LOWER_RAINBOW = "roygbiv"

def contains_rainbow(rainbow, str):
	for r in rainbow:
		tmp = str.find(r)
		if tmp == -1:
			return False
	return True

N = int(stdin.readline())
str = stdin.readline()
upper_case = contains_rainbow(UPPER_RAINBOW, str)
lower_case = contains_rainbow(LOWER_RAINBOW, str)

if upper_case and lower_case:
	print("YeS")
elif upper_case:
	print("YES")
elif lower_case:
	print("yes")
else:
	print("NO!")

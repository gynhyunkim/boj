from sys import stdin

# 감마선을 맞은 컴퓨터
# https://www.acmicpc.net/contest/problem/1151/1
SIZE = 15
classify = {'w' : "chunbae", 'b' : "nabi", 'g' : "yeongcheol"}
pictures = [stdin.readline().split() for _ in range(SIZE)]
answer = []
for pic in pictures:
	for classname in classify.keys():
		if not answer and classname in pic:
			answer.append(classify[classname])
	if answer:
		break

print(answer[-1])



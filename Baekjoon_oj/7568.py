n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
ranking = [1 for i in range(n)]

def comp(i, j):
	if info[i][0] > info[idx][0] and info[i][1] > info[idx][1]:
		return 1
	return 0

for idx in range(n):
	for i in range(n):
		if idx != i and comp(i, idx) == 1:
				ranking[idx] += 1

print(*ranking)
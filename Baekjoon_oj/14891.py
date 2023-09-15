from sys import stdin

status = [stdin.readline().strip('\n') for _ in range(4)]
K = int(stdin.readline())
infos = [list(map(int, stdin.readline().split())) for _ in range(K)]
LEFT = 6
RIGHT = 2

def rotate(n, d):
	global status
	rotated[n] = 1
	if n - 1 >= 0 and not rotated[n - 1] and status[n][LEFT] != status[n - 1][RIGHT]:
		rotate(n - 1, -d)
	if n + 1 < 4 and not rotated[n + 1] and status[n][RIGHT] != status[n + 1][LEFT]:
		rotate(n + 1, -d)
	if d == -1:
		status[n] = status[n][1:] + status[n][0]
	else:
		status[n] = status[n][7] + status[n][:7]

for n, d in infos:
	rotated = [0] * 4
	rotate(n - 1, d)

scores = [1, 2, 4, 8]
ans = 0
for i in range(4):
	if status[i][0] == '1':
		ans += scores[i]
print(ans)
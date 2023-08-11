from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

INF = float('inf')

N = int(stdin.readline())
W = int(stdin.readline())

cases = [[1, 1]] + [list(map(int, stdin.readline().split())) for _ in range(W)] + [(N, N)]

# dp = [[INF] * (W + 1) for _ in range(W + 1)]
# dp[0][1] = abs(cases[0][0] - 1) + abs(cases[0][1] - 1)
# dp[1][0] = abs(N - cases[0][0]) + abs(N - cases[0][1])

# for i in range(W):
# 	for j in range(W):
# 		if i == j:
# 			continue
# 		next = max(i, j) + 1
# 		dp[next][j] = min(dp[next][j], abs(cases[next][0] - cases[i][0]) + abs(cases[next][1] - cases[i][1]) + dp[i][j])
# 		dp[i][next] = min(dp[i][next], abs(cases[next][0] - cases[j][0]) + abs(cases[next][1] - cases[j][1]) + dp[i][j])

# answer = INF

# for i in range(W):
# 	answer = min(min(answer, dp[i][W]), dp[W][i])
# print(answer)

dp = [[-1] * (W + 1) for _ in range(W + 1)]

def find(dp, car1, car2):
	if dp[car1][car2] > -1:
		return dp[car1][car2]
	if car1 == W or car2 == W:
		return 0
	next = max(car1, car2) + 1
	car1_dis, car2_dis = 0, 0
	car1_dis = abs(1 - cases[next][0]) + abs(1 - cases[next][1])
	else:
		car1_dis = abs(cases[car1][0] - cases[next][0]) + abs(cases[car1][1] - cases[next][1])
	if car2 == 0:
		car2_dis = abs(N - cases[next][0]) + abs(N - cases[next][1])
	else:
		car2_dis = abs(cases[car2][0] - cases[next][0]) + abs(cases[car1][1] - cases[next][1])
	result1 = car1_dis + find(dp, next, car1)
	result2 = car2_dis + find(dp, next, car2)
	dp[car1][car2] = min(result1, result2)
	return dp[car1][car2]


# path = []
def tracking(dp, car1, car2):
	if car1 == W or car2 == W:
		return 0
	next = max(car1, car2) + 1
	car1_dis, car2_dis = 0, 0
	if car1 == 0:
		car1_dis = abs(1 - cases[next][0]) + abs(1 - cases[next][1])
	else:
		car1_dis = abs(cases[car1][0] - cases[next][0]) + abs(cases[car1][1] - cases[next][1])
	if car2 == 0:
		car2_dis = abs(N - cases[next][0]) + abs(N - cases[next][1])
	else:
		car2_dis = abs(cases[car2][0] - cases[next][0]) + abs(cases[car1][1] - cases[next][1])
	result1 = dp[next][car2] + car1_dis
	result2 = dp[car1][next] + car2_dis

	if result1 < result2:
		print("1")
		tracking(dp, next, car2)
	else:
		print("2")
		tracking(dp, car1, next)
print(find(dp, 0, 0))
tracking(dp, 0, 0)
# print(*path, sep = '\n')

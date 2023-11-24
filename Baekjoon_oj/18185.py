from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split())) + [0, 0]
answer = 0
for i in range(N):
	if A[i + 1] > A[i + 2]:
		min_A = min(A[i], A[i + 1] - A[i + 2])
		answer += min_A * 5
		A[i + 1] -= min_A
		A[i] -= min_A

		min_A = min(A[i], min(A[i + 1], A[i + 2]))
		answer += min_A * 7
		A[i + 2] -= min_A
		A[i + 1] -= min_A
		A[i] -= min_A
	else:
		min_A = min(A[i], min(A[i + 1], A[i + 2]))
		answer += min_A * 7
		A[i + 2] -= min_A
		A[i + 1] -= min_A
		A[i] -= min_A

		min_A = min(A[i], A[i + 1])
		answer += min_A * 5
		A[i + 1] -= min_A
		A[i] -= min_A
	answer += 3 * A[i]
	
print(answer)

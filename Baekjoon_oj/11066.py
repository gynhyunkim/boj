from sys import stdin

T = int(stdin.readline())

for _ in range(T):
	K = int(stdin.readline())
	files = list(map(int, stdin.readline().split()))
	s = [0] * (K + 1)

	for i in range(1, K + 1):
		s[i] = s[i - 1] + files[i - 1]
	
	dp = [[0] * (K + 1) for _ in range(K + 1)]
	for i in range(2, K + 1):
		for j in range(1, K + 2 - i):
			dp[j][j + i - 1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1)]) + s[j + i - 1] - s[j - 1]

	print(dp[1][K])
	




	


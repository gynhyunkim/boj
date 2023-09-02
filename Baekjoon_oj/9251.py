from sys import stdin

str1 = " " + stdin.readline().strip('\n')
str2 = " " + stdin.readline().strip('\n')

len1 = len(str1)
len2 = len(str2)

dp = [[0] * (len2) for i in range(len1)]

for i in range(1, len1):
	for j in range(1, len2):
		if str1[i] == str2[j]:
			dp[i][j] = dp[i - 1][j - 1] + 1
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len1 - 1][len2 - 1])
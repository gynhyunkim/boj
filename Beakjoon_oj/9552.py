from sys import stdin

str1, str2 = " " + stdin.readline().strip('\n'), " " + stdin.readline().strip('\n')
len1 = len(str1) - 1
len2 = len(str2) - 1
lsc = [[0] * (len2 + 1) for _ in range(len1 + 1)]

#lcs 계산
for i in range(1, len1 + 1):
	for j in range(1, len2 + 1):
		if str1[i] == str2[j]:
			lsc[i][j] = lsc[i - 1][j - 1] + 1
		else:
			lsc[i][j] = max(lsc[i - 1][j], lsc[i][j - 1])

answer = []
i, j = len1, len2 
while i > 0 and j > 0 and lsc[i][j]:
	if lsc[i][j] == lsc[i - 1][j]:
		i = i - 1
	elif lsc[i][j] == lsc[i][j - 1]:
		j = j - 1
	else:
		answer.append(str1[i])
		i, j = i - 1, j - 1

answer.reverse()
print(len(answer))
if answer:
	print(*answer, sep = '')
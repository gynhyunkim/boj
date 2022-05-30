# 행렬제곱
import sys

def mul(m1, m2):
	result = [[0] * n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] += m1[i][k] * m2[k][j]
				result[i][j] %= 1000
	return result

def devide(basem, index, m):
	if index == 1:
		return m
	elif index % 2 == 0:
		m = devide(basem, index // 2, m)
		return mul(m, m)
	else:
		m = devide(basem, index - 1, m)
		return mul(basem, m)

n, index = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

matrix = devide(matrix, index, matrix)
for mat in matrix:
	for m in mat:
		print(m % 1000, end = ' ')
	print() 

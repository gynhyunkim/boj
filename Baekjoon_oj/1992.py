# 쿼드트리
import sys

n = int(sys.stdin.readline())
m = [sys.stdin.readline().strip() for _ in range(n)]

def quadtree(n, x, y):
	is_zero = True
	is_one = True
	for i in range(y, y + n):
		for j in range(x, x + n):
			if m[i][j] == '0':
				is_one = False
			else:
				is_zero = False
			if not is_one and not is_zero:
				break
		if not is_one and not is_zero:
			break
	
	if is_one:
		print(1, end='')
	elif is_zero:
		print(0, end='')
	else:
		print("(", end='')
		quadtree(n // 2, x, y)
		quadtree(n // 2, x + n // 2, y)
		quadtree(n // 2, x, y + n // 2)
		quadtree(n // 2, x + n // 2, y + n // 2)
		print(")", end='')

quadtree(n, 0, 0)
print("")

from sys import stdin

def find_parent(parent, x):
	result = [x]
	while parent[x]:
		result.append(parent[x])
		x = parent[x]
	return result

T = int(stdin.readline())

for _ in range(T):
	N = int(stdin.readline())
	parent = [0] * (N + 1)
	for _ in range(N - 1):
		A, B = map(int, stdin.readline().split())
		parent[B] = A
	x, y = map(int, stdin.readline().split())
	x_parent = find_parent(parent, x)
	y_parent = find_parent(parent, y)
	ans = x_parent[-1]
	while x_parent and y_parent and x_parent[-1] == y_parent[-1]:
		ans = x_parent.pop()
		y_parent.pop()
	print(ans)
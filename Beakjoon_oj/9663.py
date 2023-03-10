n = int(input())
count = 0
queen = [0 for i in range(n)]
visited = [0 for i in range(n)]

def is_promising(idx):
	for i in range(idx):
		if idx - i == abs(queen[idx] - queen[i]):
			return False
	return True

def backtracking(idx):
	global count
	if idx == n:
		count += 1
		return
	
	for i in range(n):
		if visited[i]:
			continue
		queen[idx] = i
		if is_promising(idx):
			visited[i] = 1
			backtracking(idx + 1)
			visited[i] = 0

backtracking(0)
print(count)
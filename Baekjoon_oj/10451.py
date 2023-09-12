from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

t = int(stdin.readline())

def dfs(v):
	visited[v] = True
	if not visited[arr[v]]:
		dfs(arr[v])

for _ in range(t):
	n = int(stdin.readline())
	arr = [0] + list(map(int, stdin.readline().split()))
	visited = [False] * (n + 1)
	answer = 0
	for i in range(1, n + 1):
		if not visited[i]:
			dfs(i)
			answer += 1
	print(answer)


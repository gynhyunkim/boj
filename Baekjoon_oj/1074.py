from sys import stdin, setrecursionlimit

N, r, c = map(int, stdin.readline().split())
visited = 0

while N != 0:
	N -= 1
	size = 2 ** N
	if r < size and c >= size:
		visited += size * size
		c -= size
	elif r >= size and c < size:
		visited += size * size * 2
		r -= size
	elif r >= size and c >= size:
		visited += size * size * 3
		r -= size
		c -= size

print(visited)

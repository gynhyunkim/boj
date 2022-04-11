import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline() for _ in range(n)]
words = list(set(words))
words.sort()
words.sort(key = len)

for word in words:
	print(word, end='')

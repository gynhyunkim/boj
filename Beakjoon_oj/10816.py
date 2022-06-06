# 숫자 카드2
import sys

n = int(sys.stdin.readline())
cards = sorted(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
count = map(int, sys.stdin.readline().split())

def binary(target, start, end):
	if start > end:
		return 0
	mid = (start + end) // 2
	if target == cards[mid]:
		return cards[start:end + 1].count(target)
	elif target < cards[mid]:
		return binary(target, start, mid - 1)
	else:
		return binary(target, mid + 1, end)

result = {}
for	c in cards:
	start = 0
	end = len(cards) - 1
	if c not in result:
		result[c] = binary(c, start, end)

print(' '.join(str(result[c]) if c in result else '0' for c in count))
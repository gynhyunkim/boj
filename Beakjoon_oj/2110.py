#공유기 설치
from sys import stdin

n, c = map(int, stdin.readline().split())
coord = [int(stdin.readline()) for _ in range(n)]
coord = sorted(coord)

start = 1
end = coord[-1] - coord[0]
result = 0
while (start <= end):
	mid = (start + end) // 2
	value = coord[0]
	count = 1
	tmp = float("INF")
	for i in range(1, n):
		if (coord[i] >= value + mid):
			tmp = min(coord[i] - value, tmp)
			value = coord[i]
			count += 1
	if count >= c:
		start = mid + 1
		result = max(result, tmp)
	else:
		end = mid - 1
print(result)

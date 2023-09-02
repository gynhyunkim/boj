# 통계학
import math
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

avg = sum(arr) / n
diff = avg - math.floor(avg)
print(math.floor(avg) if diff < 0.5 else math.floor(avg) + 1)
arr = sorted(arr)
print(arr[n // 2])
counting = {}
for num in arr:
	if num not in counting:
		counting[num] = 1
	else:
		counting[num] += 1
counting = sorted(counting.items(), key = lambda x: x[1], reverse = True)
print(counting[0][0] if n == 1 or counting[0][1] != counting[1][1] else counting[1][0])
print(arr[-1] - arr[0])
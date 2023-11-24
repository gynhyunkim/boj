from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())
sensor = list(map(int, stdin.readline().split()))
sensor.sort()
diff = [0] * (N - 1)
for i in range(N - 1):
	diff[i] = sensor[i + 1] - sensor[i]
diff.sort()
print(sum(diff[:N - K]))


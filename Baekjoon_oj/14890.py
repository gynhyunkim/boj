from sys import stdin

N, L = map(int, stdin.readline().split())
road_map = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = 0

def check_road(road):
	for i in range(1, N):
		if abs(road[i] - road[i - 1]) > 1:
			return False
		if road[i] < road[i - 1]:
			for k in range(L):
				if i + k >= N or used[i + k] or road[i] != road[i + k]:
					return False
				if road[i] == road[i + k]:
					used[i + k] = True
		elif road[i] > road[i - 1]:
			for k in range(L):
				if i - k - 1 < 0 or road[i - 1] != road[i - k - 1] or used[i - k - 1]:
					return False
				if road[i - 1] == road[i - k - 1]:
					used[i - k - 1] = True
	return True

			 
for i in range(N):
	used = [False] * N
	if check_road(road_map[i]):
		answer += 1
	used = [0] * N
	if check_road([road_map[j][i] for j in range(N)]):
		answer += 1

print(answer)
		
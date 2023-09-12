# + - * //
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))

max_calc = -1e9
min_calc = 1e9

def dfs(level, calc):
	global max_calc, min_calc, op
	if level == n:
		max_calc = max(calc, max_calc)
		min_calc = min(calc, min_calc)
		return
	if op[0] > 0:
		op[0] -= 1
		dfs(level + 1, calc + nums[level])
		op[0] += 1
	if op[1] > 0:
		op[1] -= 1
		dfs(level + 1, calc - nums[level])
		op[1] += 1
	if op[2] > 0:
		op[2] -= 1
		dfs(level + 1, calc * nums[level])
		op[2] += 1
	if op[3] > 0:
		op[3] -= 1
		dfs(level + 1, int(calc / nums[level]))
		op[3] += 1

dfs(1, nums[0])
print(max_calc)
print(min_calc)
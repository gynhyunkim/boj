# n = int(input())
# start = n - (9 * len(str(n))) if n > 9 else 1
# result =  0
# for i in range(start, n + 1):
# 	num = sum(map(int, str(i))) + i
# 	if num == n:
#  		result = i
# 		break
# print(result)
	
n = int(input())
result = 0
for i in range(1, n):
	num = sum(map(int, str(i))) + i
	if num == n:
		result = i
		break

print(result)
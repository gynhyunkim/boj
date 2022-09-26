def solution(s):
	answer = len(s)
	# 최대가 반절이니까 1/2 까지만 step으로 지정
	for step in range(1, len(s) // 2 + 1):
		result = ""
		cnt = 1
		# 맨처음 step 길이만큼 자른 문자열
		tmp = s[:step]
		# step 이후 문자열 step만큼 비교, 마지막 문자열까지 비교하기 위해서 + step 더하기
		for i in range(step, len(s) + step, step):	
			if tmp == s[i:i + step]:
				cnt += 1
			else:
				if cnt == 1:
					result += tmp
				else:
					result += str(cnt) + tmp
				tmp = s[i:i + step]
				cnt = 1
		answer = min(answer, len(result))
	return answer
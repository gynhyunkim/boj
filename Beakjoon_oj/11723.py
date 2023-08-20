from sys import stdin

M = int(stdin.readline())
S = []
for _ in range(M):
	cmd = stdin.readline().split()
	cmd, num = cmd[0], int(cmd[1]) if len(cmd) == 2 else 0 
	num = int(num)
	if (cmd == "add" and num not in S) or (cmd == "toggle" and num not in S):
		S.append(num)
	elif cmd == "check":
		print(1 if num in S else 0)
	elif (cmd == "remove" and num in S) or (cmd == "toggle" and num in S):
		S.remove(num)
	elif cmd == "all":
		S = [i for i in range(1, 21)]
	elif cmd == "empty":
		S = []


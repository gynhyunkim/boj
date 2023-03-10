n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards = sorted(cards)
closest = 0
pick = []

def pick_card(cur):
	if len(pick) == 3 :
		global closest
		count = sum(pick)
		if count <= m:
			closest = count if m - closest > m - count else closest
		return
	for i in range(cur, len(cards)):
		pick.append(cards[i])
		pick_card(i + 1)
		pick.pop()

pick_card(0)
print(closest)

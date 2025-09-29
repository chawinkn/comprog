card = input().split()
op = input().replace(' ', '')
n = len(card)

for i in op:
	if i not in ['C', 'S']:
		continue
	if i == 'C':
		temp = card[n//2:] + card[:n//2]
		card = temp
	else:
		temp = []
		for i in range(n//2):
			temp.append(card[i])
			temp.append(card[n//2+i])
		card = temp

print(*card)
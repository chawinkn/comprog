score = {'X': 0, 'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7}

p = {'1': 0, '2': 0}

while True:
	s = input()
	p[s[0]] += sum([score[i] for i in s[1:]])

	if s[1] == 'K':
		break

print(p['1'], p['2'])
if p['1'] == p['2']:
	print("Tie")
else:
	print(f"Player {1 + int(p['2'] > p['1'])} wins")
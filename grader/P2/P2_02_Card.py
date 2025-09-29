s = input()
card = [s[i:i+2] for i in range(0, len(s), 2)]
val = {
	'A': 1,
	'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
	'T': 10, 'J': 11, 'Q': 12, 'K': 13,
}
deck = {
	'C': 1, 'D': 2, 'H': 3, 'S': 4,
}

for i in range(len(card)-1):
	lv, ld = [i for i in card[i]]
	rv, rd = [i for i in card[i+1]]
	d = 0

	if lv != rv:
		d = val[lv]-val[rv]
	else:
		d = deck[ld]-deck[rd]

	print(f'{"+" if d > 0 else ""}{d}', end="")
file, year = input().split()

y = year[2:]
with open(file, "r") as f:
	mn, mx, s, n = 0, 0, 0, 0
	for i in f:
		id, score = i.strip().split()
		score = float(score)
		if id[:2] != y:
			continue
		if n == 0:
			mn, mx = score, score
		else:
			mn, mx = min(mn, score), max(mx, score)
		s += score
		n += 1
	if n > 0:
		print(mn, mx, s/n)
	else:
		print("No data")
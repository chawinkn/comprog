def missing_digits(t):
	a = [0]*10
	for i in t:
		if i.isdigit():
			a[int(i)] = 1
			
	missing = [i for i in range(10) if a[i] == 0]
	return missing

exec(input()) # DON'T remove this line
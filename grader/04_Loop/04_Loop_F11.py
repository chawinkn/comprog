def RLE(t):
	n = len(t)
	res, cnt = [], 0
	for i in range(n):
		cnt += 1
		if i == n-1 or t[i] != t[i+1]:
			res.append([t[i], cnt])
			cnt = 0

	return res

exec(input()) # DON'T remove this line
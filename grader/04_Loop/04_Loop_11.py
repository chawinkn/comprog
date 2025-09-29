t = input()

n = len(t)
res, cnt = [], 0
for i in range(n):
	cnt += 1
	if i == n-1 or t[i] != t[i+1]:
		res.append([t[i], cnt])
		cnt = 0

for c, cnt in res:
	print(c, cnt, end=" ")
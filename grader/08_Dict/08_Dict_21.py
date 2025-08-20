s = input().lower()

cnt = {}

for i in s:
	if i < 'a' or i > 'z':
		continue
	if i not in cnt:
		cnt[i] = 1
	else:
		cnt[i] += 1

arr = [[-cnt[i], i] for i in cnt]

for c, i in sorted(arr):
	print(i, "->", -c)
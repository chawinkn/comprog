s = input()
cnt = [0]*10
for i in s:
	if i.isdigit():
		cnt[int(i)] = 1

missing = [str(i) for i in range(10) if cnt[i] == 0]
print(",".join(missing) if len(missing) else None)
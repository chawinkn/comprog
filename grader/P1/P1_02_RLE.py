t = input()
if t == "str2RLE":
	s = input()
	n, cnt = len(s), 0
	for i in range(n):
		cnt += 1
		if i == n-1 or s[i] != s[i+1]:
			print(s[i], cnt, end=" ")
			cnt = 0
elif t == "RLE2str":
	s = input().split()
	n = len(s)
	print("".join([s[i]*int(s[i+1]) for i in range(0, n-1, 2)]))
else:
	print("Error")
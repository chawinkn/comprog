N = int(input())
v = []
for i in range(N):
	s = input().split()
	for i in range(1, len(s)):
		s[i] = float(s[i])
	v.append(s)
c = input().split()
if c[0] == "show":
	for i in v:
		print(*i)
elif c[0] == "get":
	t = c[1]
	for i in v:
		if i[0] == t:
			print(*i)
			break
	else:
		print(f"{t} not found")
elif c[0] == "avg":
	m = int(c[1])

	print(round(sum([i[m] for i in v])/N, 4))
elif c[0] == "max":
	m = int(c[1])
	mx = max([i[m] for i in v])
	ans = ""
	for i in v:
		if i[m] == mx and (ans == "" or i[0] < ans):
			ans = i[0]

	print(ans, mx)
else:
	m = int(c[1])
	tmp = [[i[m], i[0]] for i in v]
	tmp.sort()

	print(*[i[1] for i in tmp])
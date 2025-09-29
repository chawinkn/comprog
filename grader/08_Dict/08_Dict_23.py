nt = {}
tn = {}

n = int(input())
for i in range(n):
	first, sur, tel = input().split()
	name = first + " " + sur
	nt[name] = tel
	tn[tel] = name

m = int(input())
for i in range(m):
	s = input()
	print(s, "-->", end=" ")
	if s in nt:
		print(nt[s])
	elif s in tn:
		print(tn[s])
	else:
		print("Not found")
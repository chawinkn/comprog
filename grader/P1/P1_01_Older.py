month = [
	"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

s = input().split()
n1, m1, d1, y1 = s[0], month.index(s[1])+1, int(s[2][:-1]), int(s[3])
s = input().split()
n2, m2, d2, y2 = s[0], month.index(s[1])+1, int(s[2][:-1]), int(s[3])

if y1 < y2:
	print(n1)
elif y2 < y1:
	print(n2)
else:
	if m1 < m2:
		print(n1)
	elif m2 < m1:
		print(n2)
	else:
		if d1 < d2:
			print(n1)
		elif d2 < d1:
			print(n2)
		else:
			print(n1, n2)
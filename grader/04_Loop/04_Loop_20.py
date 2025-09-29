n = 1

x, y = [int(i) for i in input().split()]
mn1, mx1 = x, y
mn2, mx2 = y, x

while True:
	t = input()

	if t == "Zig-Zag":
		print(mn1, mx1)
		break
	elif t == "Zag-Zig":
		print(mn2, mx2)
		break

	x, y = [int(i) for i in t.split()]

	if n%2 == 1:
		x, y = y, x
	mn1, mx1 = min(mn1, x), max(mx1, y)
	mn2, mx2 = min(mn2, y), max(mx2, x)

	n += 1
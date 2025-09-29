from math import sqrt

c = input().strip()
if c == 'S':
	m = int(input().strip())
	q, r, t, k, n, x, i, p = 1, 0, 1, 1, 3, 3, 0, ""
	while i < m:
		if 4*q+r-t < n*t:
			p += str(n)
			i += 1
			a = 10*(r - n*t)
			n = 10*(3*q + r)//t - 10*n
			q *= 10
			r = a
		else:
			a = (2*q + r)*x
			b = (7*q*k + 2 + x*r)//(x*t)
			q *= k
			t *= x
			x += 2
			k += 1
			n = b
			r = a

	p = p[0] + "." + p[1:]
	print("pi =", p)
elif c == 'R':
	n = int(input().strip())
	s = 0
	for k in range(n+1):
		s += (-3)**(-k)/(2*k+1)
	p = sqrt(12)*s
	p = round(p, 12)

	print("pi =", p)

elif c == 'P':
	p = sqrt(7+sqrt(6+sqrt(5)))
	p = round(p, 6)

	print("pi =", p)
else:
	print("Invalid")
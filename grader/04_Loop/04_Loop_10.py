a = float(input())
aa = a

L, U = 0, 0
while aa > 0:
	aa /= 10
	U += 1
x = (L+U)/2

while abs(a-10**x) > 1e-10 * max(a, 10**x):
	if 10**x > a:
		U = x
	else:
		L = x
	x = (L+U)/2

print(round(x, 6))
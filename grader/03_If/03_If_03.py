a, b, c, d = [float(i) for i in input().split()]
s = a+b+c+d

if a >= b and a >= c and a >= d:
	s -= a
elif b >= a and b >= c and b >= d:
	s -= b
elif c >= a and c >= b and c >= d:
	s -= c
else:
	s -= d 

if a <= b and a <= c and a <= d:
	s -= a
elif b <= a and b <= c and b <= d:
	s -= b
elif c <= a and c <= b and c <= d:
	s -= c
else:
	s -= d 

print(round(s/2, 2))
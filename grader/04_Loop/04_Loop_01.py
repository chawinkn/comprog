n = 0
s = 0

# didnt know can do this in python
while (num := input()) != 'q':
	s += float(num)
	n += 1

if n:
	print(round(s/n, 2))
else:
	print("No Data")
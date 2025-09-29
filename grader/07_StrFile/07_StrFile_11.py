s = input()

if s[-1] in ['s', 'x'] or s[-2:] == "ch":
	print(s+'es')
elif s[-1] == 'y' and s[-2] not in ['a', 'e', 'i', 'o', 'u']:
	print(s[:-1]+'ies')
else:
	print(s+'s')
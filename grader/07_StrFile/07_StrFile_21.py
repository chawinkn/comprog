while (s := input()) != "end":
	for i in s:
		if i.isalpha():
			a = ['a', 'A'][i.isupper()]
			print(chr(ord(a)+(ord(i)-ord(a)+13)%26), end="")
		else:
			print(i, end="")
	print()
s = "".join(i if i.isalpha() or i.isdigit() or i == ' ' else ' ' for i in input().lower())
s = s.split()

print(s[0], end="")
for i in s[1:]:
	print(i[0].upper()+i[1:], end="")
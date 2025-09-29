t = input()
w = input()
s = ""

for i in w:
	# if i.isalpha():
	if i not in ['"', '(', ')', ',', '.', "'"]:
		s += i
	else:
		s += " "

print(sum([1 for i in s.split() if i == t]))
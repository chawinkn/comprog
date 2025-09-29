s = input()

for i in s:
	if i == '(':
		print('[', end="")
	elif i == '[':
		print('(', end="")
	elif i == ')':
		print(']', end="")
	elif i == ']':
		print(')', end="")
	else:
		print(i, end="")
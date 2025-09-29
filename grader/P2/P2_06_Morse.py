name = input()

def T2M(text, pattern):
	morse = ''
	for e in text:
		j = pattern.find('[' + e + ']')
		if j == -1:
			print("Invalid :", text)
			break
		j += 3
		k = pattern.find('[', j)
		morse += pattern[j:k] + ' '
	else:
		print(morse.strip())

def M2T(morse, pattern):
	text = ''
	for e in morse.split():
		j = pattern.find(']' + e + '[')
		if j == -1:
			print("Invalid :", morse)
			break
		j -= 1
		text += pattern[j]
	else:
		print(text.strip())

with open(name, "r") as f:
	t = f.readline().strip()
	pattern = f.readline().strip()

	if t == "T2M":
		while (s := f.readline().strip()):
			T2M(s, pattern)
	elif t == "M2T":
		while (s := f.readline().strip()):
			M2T(s, pattern)
	else:
		print("Invalid code")
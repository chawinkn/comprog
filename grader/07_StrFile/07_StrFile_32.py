def no_lowercase(t): # return True if no lowercase, otherwise return False
	for i in t:
		if i.islower():
			return False
	return True

def no_uppercase(t):
	for i in t:
		if i.isupper():
			return False
	return True

def no_number(t):
	for i in t:
		if i.isdigit():
			return False
		
	return True

def no_symbol(t):
	for i in t:
		if not i.isalpha() and not i.isdigit():
			return False
		
	return True

def character_repetition(t):
	for i in range(len(t)-3):
		if t[i:i+4].count(t[i]) == 4:
			return True
		
	return False
		
def number_sequence(t):
	t = t.lower()
	for i in range(len(t)-3):
		if not t[i:i+4].isdigit():
			continue

		asc, desc = 0, 0
		for j in range(i, i+3):
			asc += (int(t[j])+1)%10 == int(t[j+1])
			desc += (int(t[j])-1)%10 == int(t[j+1])
		if asc == 3 or desc == 3:
			return True
		
	return False

def letter_sequence(t):
	t = t.lower()
	for i in range(len(t)-3):
		if not t[i:i+4].isalpha():
			continue
		
		asc, desc = 0, 0
		for j in range(i, i+3):
			asc += ord('a')+(ord(t[j])-ord('a')+1)%26 == ord(t[j+1])
			desc += ord('a')+(ord(t[j])-ord('a')-1)%26 == ord(t[j+1])
		if asc == 3 or desc == 3:
			return True
		
	return False

def keyboard_pattern(t):
	pattern = ["!@#$%^&*()_+", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
	t = t.lower()
	for i in range(len(t)-3):
		s = t[i:i+4]
		for p in pattern:
			if s in p or s in p[::-1]:
				return True

	return False

#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
	errors.append("Less than 8 characters")
if no_lowercase(passw):
	errors.append("No lowercase letters")
if no_uppercase(passw):
	errors.append("No uppercase letters")
if no_number(passw):
	errors.append("No numbers")
if no_symbol(passw):
	errors.append("No symbols")
if character_repetition(passw):
	errors.append("Character repetition")
if number_sequence(passw):
	errors.append("Number sequence")
if letter_sequence(passw):
	errors.append("Letter sequence")
if keyboard_pattern(passw):
	errors.append("Keyboard pattern")

if len(errors) == 0:
	print("OK")
else:
	for e in errors:
		print(e)
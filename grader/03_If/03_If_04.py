n = input()

if len(n) == 10 and n[:2] in ["06", "08", "09"]:
	print("Mobile number")
else:
	print("Not a mobile number")
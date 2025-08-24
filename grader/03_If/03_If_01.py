s = input()

if s.isdigit() and len(s) == 2:
	if s == "01" or s == "02" or 20 <= int(s) <= 40 or s == "51" or s == "53" or s == "55" or s == "58":
		print("OK")
	else:
		print("Error")
else:
	print("Error")
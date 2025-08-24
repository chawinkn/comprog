def is_mobile_number(number):
	# number เป็นสตริงเก็บหมายเลข (ภายในสตริงมีแต่ตัวเลขแน่ ๆ)
	# คืน True ถ้า number เป็นหมายเลขโทรศัพท์ ถ้าไม่เป็น คืน False
	return len(number) == 10 and number[:2] in ["06", "08", "09"]


exec(input()) # DON'T remove this line
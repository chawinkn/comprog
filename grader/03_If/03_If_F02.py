def choose(stu1, stu2):
	# stu1 และ stu2 เป็นลิสต์ [ ID, GPAX, compprog, cal1, cal2 ]
	# ID เป็นสตริงเก็บเลขประจำตัว
	# GPAX เป็น float
	# comprog, cal1, cal2 เป็นสตริงเก็บเกรดของสำมวิชำ (เกรดเป็นแบบไม่มีประจุ A,B,C,D,F)
	# ฟังก์ชันนี้คืน
	# - ถ้ำไม่ผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ว่ำง
	# - ถ้ำผ่ำนเกณฑ์ข้อ 1 คนเดียว คืนลิสต์ที่เก็บเลขประจำตัวของคนที่ผ่ำนเกณฑ์ข้อ 1
	# - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ที่เก็บเลขประจำตัวของนิสิตที่มีข้อ 2 ที่ดีกว่ำ
	# - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ และมีข้อ 2 เท่ำกัน คืนลิสต์ที่เก็บเลขประจำตัวของนิสิตคนแรก ตำมด้วยของคนที่สอง
	grade1 = stu1[2] == "A" and stu1[3] <= "C" and stu1[4] <= "C"
	grade2 = stu2[2] == "A" and stu2[3] <= "C" and stu2[4] <= "C"

	if not grade1 and not grade2:
		return []

	if grade1 and grade2:
		# GPAX
		if stu1[1] == stu2[1]:
			# cal1
			if stu1[3] == stu2[3]:
				# cal2
				if stu1[4] == stu2[4]:
					return [stu1[0], stu2[0]]
				else:
					return [stu1[0]] if stu1[4] < stu2[4] else [stu2[0]]
			else:
				return [stu1[0]] if stu1[3] < stu2[3] else [stu2[0]]
		else:
			return [stu1[0]] if stu1[1] > stu2[1] else [stu2[0]]
		
	if grade1:
		return [stu1[0]]
	
	return [stu2[0]]


exec(input()) # DON'T remove this line
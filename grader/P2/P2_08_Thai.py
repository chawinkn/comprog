def to_Thai(N):
	# N เป็นจำนวนเต็มที่ค่ำมีตั้งแต่ 0 ถึง 9999
	# (ไม่ต้องตรวจว่ำอยู่ในช่วงนี้หรือไม่ ข้อมูลทดสอบอยู่ในช่วงนี้แน่ ๆ)
	# คืนสตริงคำอ่ำนไทยของ N แต่ละคำคั่นด้วยช่องว่ำงหนึ่งช่อง (ดูตัวอย่ำงข้ำงล่ำง)
	out = []
	n = N
	d = ["soon", "neung", "song", "sam", "si", "ha", "hok", "chet", "paet", "kao"]
	if N >= 1000: # จัดกำรหลักพัน
		out.append(d[N//1000])
		out.append("pun")
		N %= 1000
	if N >= 100: # จัดกำรหลักร้อย
		out.append(d[N//100])
		out.append("roi")
		N %= 100
	if N >= 10: # จัดกำรหลักสิบ
		if N//10 == 1:
			out.append("sip")
		elif N//10 == 2:
			out.append("yi sip")
		else:
			out.append(d[N//10])
			out.append("sip")

	if N != 10:
		if n%10 == 1 and n > 1:
			out.append("et")
		else:
			N %= 10
			if N == 0 and n > 0:
				pass
			else:
				out.append(d[N])

	return " ".join(out)

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
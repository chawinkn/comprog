def is_odd(n):
	# คืน (True/False) ว่า n เป็นจานวนคี่หรือไม่
	return n%2 != 0
	
def has_odds(x):
	# คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลบางตัวเป็นจานวนคี่
	for i in x:
		if is_odd(i):
			return True
	return False

def all_odds(x):
	# คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลทุกตัวเป็นจานวนคี่
	for i in x:
		if not is_odd(i):
			return False
	return True

def no_odds(x):
	# คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข้อมูลที่เป็นจานวนคี่เลย
	return not has_odds(x)

def get_odds(x):
	# คืนลิสต์ที่มีจานวนคี่ที่มีเก็บในลิสต์ x (ลาดับก่อนหลังให้เป็นไปตามลาดับเดียวกับใน x)
	# เช่น x = [1,2,3,5,0] จะได้ผลคือ [1,3,5]
	return [i for i in x if is_odd(i)]

def zip_odds(a, b):
	# คืนลิสต์ที่สร้างจากการนาจานวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
	# เช่น a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได้คือ
	# [1,19,5,11,7,17,9,3]
	a, b = get_odds(a), get_odds(b)
	res = []
	i, j = 0, 0
	n, m = len(a), len(b)
	while i < n and j < m:
		res.append(a[i])
		res.append(b[j])
		i += 1
		j += 1
	while i < n:
		res.append(a[i])
		i += 1
	while j < m:
		res.append(b[j])
		j += 1
	return res


exec(input().strip()) # ต้องมีคาสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
def reverse(d):
	# d เป็น dict ที่มี value ไม่ซ ้ำกัน
	# คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได้รับ
	return {d[i]: i for i in d}

def keys(d, v):
	# คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได้) ที่มีค่ำ value เท่ำกับ v
	return [i for i in d if d[i] == v]


exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
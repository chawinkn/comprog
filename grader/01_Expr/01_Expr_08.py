def sqrt_n_times(x, n):
	# คืนค่าที่เสมือนการนาค่าใน x มากดปุ่ม  เป็นจานวน n ครั้ง
	for i in range(n):
		x = x**(1/2)
	return x

def cube_root(y):
	# คืนค่าประมาณของรากที่สามของ y โดยใช้วิธีที่เสมือนการกดปุ่มด้วยสูตร
	#
	# ข้อแนะนา: เรียกใช้ฟังก์ชัน sqrt_n_times
	y = sqrt_n_times(y, 2)
	for i in range(1, 6):
		y *= sqrt_n_times(y, 2**i)
	return y

def main():
	q = float(input())
	print(cube_root(q))

exec(input()) # DON'T remove this line
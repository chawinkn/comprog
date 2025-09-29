q = list() # ลิสต์ q ใช้เก็บข้อมูลบัตรคิวที่เหมาะสม
n = int(input()) # อ่านจ านวนค าสั่ง
next = 0
time = 0
cnt = 0
call = []

for k in range(n):
	c = input().split() # อ่านข้อมูลค าสั่ง
	if c[0] == 'reset':
		next = int(c[1])
	elif c[0] == 'new':
		t = int(c[1])
		q.append([next, t])
		print("ticket", next)
		next += 1
	elif c[0] == 'next':
		call = q[0]
		q.pop(0)
		print("call", call[0])
	elif c[0] == 'order':
		t = int(c[1])
		dt = t-call[1]
		time += dt
		cnt += 1
		print("qtime", call[0], dt)
	elif c[0] == 'avg_qtime':
		print("avg_qtime", round(time/cnt, 4))
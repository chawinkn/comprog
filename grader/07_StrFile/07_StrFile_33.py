def read_next(f):
	while True:
		t = f.readline()
		if len(t) == 0: # ถ้าอ่านหมดแล้ว ออกจากวงวน
			break
		x = t.strip().split() # ลบ blank ซ้ายขวา
		if len(x) == 2: # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
			return x[0], x[1]
	return "", "" # แฟ้มหมดแล้ว คืนสตริงว่าง

n1, n2 = input().split()

with open(n1, "r") as f1, open(n2, "r") as f2:
	id1, g1 = read_next(f1)
	id2, g2 = read_next(f2)

	while id1 != '' and id2 != '':
		# print(id1, g1, id2, g2)
		if id1[-2:] < id2[-2:]:
			print(id1, g1)
			id1, g1 = read_next(f1)
		elif id2[-2:] < id1[-2:]:
			print(id2, g2)
			id2, g2 = read_next(f2)
		else:
			if id1 < id2:
				print(id1, g1)
				id1, g1 = read_next(f1)
			else:
				print(id2, g2)
				id2, g2 = read_next(f2)
	
	while id1 != '':
		print(id1, g1)

		id1, g1 = read_next(f1)

	while id2 != '':
		print(id2, g2)

		id2, g2 = read_next(f2)
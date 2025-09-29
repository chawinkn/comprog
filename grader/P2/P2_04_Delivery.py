order = []

while (s := input().split()) != ["END"]:
	id, t, d, m, y = s[0], s[1], int(s[2]), int(s[3]), int(s[4])
	day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if ((y-543)%4 == 0 and (y-543)%100 != 0) or (y-543)%400 == 0:
		day[1] = 29

	if y < 2558:
		print("Error:", id, t, d, m, y, "--> Invalid year")
		continue
	if not 1 <= m <= 12:
		print("Error:", id, t, d, m, y, "--> Invalid month")
		continue
	if not 1 <= d <= day[m-1]:
		print("Error:", id, t, d, m, y, "--> Invalid date")
		continue
	
	dt = {'E': 1, 'Q': 3, 'N': 7, 'F': 14}

	if t in dt:
		d += dt[t]
		if d > day[m-1]:
			d -= day[m-1]
			m += 1
		if m > 12:
			m -= 12
			y += 1

		order.append([y, m, d, id])
	else:
		print("Error:", id, t, d, m, y, "--> Invalid delivery type")
		continue

order.sort()

for y, m, d, id in order:
	print(f"{id}: delivered on {d}/{m}/{y}")
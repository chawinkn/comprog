def total(pocket):
	return sum([i*pocket[i] for i in pocket])

def take(pocket, money_in):
	for i in money_in:
		if i in pocket:
			pocket[i] += money_in[i]
		else:
			pocket[i] = money_in[i]

def pay(pocket, amt):
	key = sorted([i for i in pocket], reverse=True)
	p = {}
	for i in key:
		if amt < i:
			continue
		n = min(amt//i, pocket[i])
		p[i] = n
		amt -= i*n

	if amt > 0:
		return {}
	
	for i in p:
		pocket[i] -= p[i]

	return p
	
exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ
a = input()
b = input()

cnta, cntb = [0]*26, [0]*26

for c in a.lower():
	if not 'a' <= c <= 'z':
		continue
	
	cnta[ord(c)-ord('a')] += 1

for c in b.lower():
	if not 'a' <= c <= 'z':
		continue
	
	cntb[ord(c)-ord('a')] += 1

rema, remb = [], []

for i in range(26):
	if cnta[i] == cntb[i]:
		continue
	
	d = abs(cnta[i]-cntb[i])
	if cnta[i] > cntb[i]:
		rema.append([d, chr(ord('a')+i)])
	else:
		remb.append([d, chr(ord('a')+i)])

print(a)
if len(rema) > 0:
	for i, c in rema:
		print(f" - remove {i} {c}{"'s" if i > 1 else ""}")
else:
	print(" - None")

print(b)
if len(remb) > 0:
	for i, c in remb:
		print(f" - remove {i} {c}{"'s" if i > 1 else ""}")
else:
	print(" - None")
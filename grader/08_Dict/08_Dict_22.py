n = int(input())

ic = {}

for _ in range(n):
	name, p = input().split()
	ic[name] = float(p)

m = int(input())

s = {}

for _ in range(m):
	name, k = input().split()
	if name not in ic:
		continue
	if name not in s:
		s[name] = ic[name]*float(k)
	else:
		s[name] += ic[name]*float(k)

total = sum([s[i] for i in s])

if total == 0:
	print("No ice cream sales")
else:
	mx = max([s[i] for i in s])
	ans = [i for i in s if s[i] == mx]
	
	print("Total ice cream sales:", total)
	print("Top sales:", ", ".join(sorted(ans)))
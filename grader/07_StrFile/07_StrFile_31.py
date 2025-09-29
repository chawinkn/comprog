def solve(dna):
	d = {
		'A': 'T', 'T': 'A', 
		'G': 'C', 'C': 'G'
	}
	
	for i in dna:
		if i not in d:
			print("Invalid DNA")
			return
		
	t = input()

	if t == 'R':
		print("".join(reversed([d[i] for i in dna])))
	elif t == 'F':
		cnt = {i: 0 for i in d}
		for i in dna:
			cnt[i] += 1
		print(", ".join([f"{i}={cnt[i]}" for i in cnt]))
	else:
		p = input()
		cnt = 0
		for i in range(len(dna)-1):
			cnt += dna[i] == p[0] and dna[i+1] == p[1]
		print(cnt)

dna = input().strip().upper()
solve(dna)
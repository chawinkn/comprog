def solve(t, n, s):
	for i in range(n-1):
		if len(s[i]) != len(s[i+1]):
			print("Invalid size")
			return
	m = len(s[0])
	if t == "90":
		for j in range(m):
			for i in range(n-1, -1, -1):
				print(s[i][j], end="")
			print()
	elif t == "180":
		for i in range(n-1, -1, -1):
			print(s[i][::-1])
	else:
		for i in range(n):
			print(s[i][::-1])
		
t = input()
n = int(input())
s = [input() for _ in range(n)]
solve(t, n, s)
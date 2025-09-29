sol = input()
ans = input()

n, m = len(sol), len(ans)
if n == m:
	print(sum([1 for i in range(n) if sol[i] == ans[i]]))
else:
	print("Incomplete answer")
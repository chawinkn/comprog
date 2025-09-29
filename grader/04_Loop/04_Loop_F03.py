def grade_mcq(sol, ans):
	n, m = len(sol), len(ans)
	if n != m:
		return -1

	return sum([1 for i in range(n) if sol[i] == ans[i]])

exec(input()) # DON'T remove this line
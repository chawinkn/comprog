def convex_polygon_area(p):
	n, s = len(p), 0
	for i in range(n):
		s += p[i][0]*p[(i+1)%n][1] - p[(i+1)%n][0]*p[i][1]

	return 1/2 * abs(s)

def is_heterogram(s):
	mp = [0]*26
	for c in s.lower():
		if not 'a' <= c <= 'z':
			continue

		i = ord(c)-ord('a')
		if mp[i] == 1:
			return False
		mp[i] += 1

	return True

def replace_ignorecase(s, a, b):
	ans = ""
	sl, al = s.lower(), a.lower()
	i, n, m = 0, len(s), len(a)
	while i < n:
		if sl[i:i+m] == al:
			ans += b
			i += m
		else:
			ans += s[i]
			i += 1

	return ans

def top3(votes):
	lst = [[-votes[i], i] for i in votes]
	lst.sort()
	
	return [i[1] for i in lst[:3]]

# ต้องมีคำสั่งข้ำงล่ำงนี้ ตอนส่งให้ Grader ตรวจ
for k in range(2):
	exec(input().strip())
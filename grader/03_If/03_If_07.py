n = int(input())
s = ""

if 1e3 <= n < 1e6:
	n /= 1e3
	s = "K"
elif 1e6 <= n < 1e9:
	n /= 1e6
	s = "M"
elif n >= 1e9:
	n /= 1e9
	s = "B"

print(f"{round(n) if n >= 10 else round(n, 1)}{s}")
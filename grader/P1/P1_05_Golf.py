from math import floor

par = 0
stroke = 0
sum_ms = 0

for i in range(9):
	p, s, c = [int(i) for i in input().split()]
	par += p
	stroke += s
	if c == 1:
		sum_ms += min(p+2, s)

handicap = floor(0.8*(1.5*sum_ms - par))
score = stroke - handicap

print(stroke)
print(handicap)
print(score)
a = float(input())
b = float(input())
c = float(input())

def cal(a, b, c, n):
	return (-b + n*(b*b-4*a*c)**(1/2)) / (2*a)

print(round(cal(a, b, c, -1), 3), round(cal(a, b, c, 1), 3))
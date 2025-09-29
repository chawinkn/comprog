n = int(input())
lst = []

for i in range(n):
	x, y = [float(i) for i in input().split()]
	lst.append([(x**2+y**2)**(1/2), i, x, y])

lst.sort()

print(f"#{lst[2][1]+1}: ({lst[2][2]}, {lst[2][3]})")
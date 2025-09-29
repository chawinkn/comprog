n = int(input())
x, y = [0]*n, [0]*n

for i in range(n):
	x[i], y[i] = [int(i) for i in input().split()]

t = input()

if t == "Zag-Zig":
	x, y = y, x
	
mn = min([x[i] if i%2 == 0 else y[i] for i in range(n)])
mx = max([y[i] if i%2 == 0 else x[i] for i in range(n)])
print(mn, mx)
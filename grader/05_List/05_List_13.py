ans = []
n = 0

for i in range(int(input())):
	a = int(input())
	n += 1
	ans.insert(0, a) if n%2 == 0 else ans.append(a)

for i in input().split():
	a = int(i)
	n += 1
	ans.insert(0, a) if n%2 == 0 else ans.append(a)

while (a := int(input())) != -1:
	n += 1
	ans.insert(0, a) if n%2 == 0 else ans.append(a)

print(ans)
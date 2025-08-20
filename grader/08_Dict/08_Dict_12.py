first, nick = {}, {}

n = int(input())

for _ in range(n):
	f, ni = input().split()
	first[f] = ni
	nick[ni] = f

m = int(input())

for _ in range(m):
	s = input()
	if s in first:
		print(first[s])
	elif s in nick:
		print(nick[s])
	else:
		print("Not found")
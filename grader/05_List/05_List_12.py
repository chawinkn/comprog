n = int(input())
first_nick = [
	["Robert", "Bob"],
	["William", "Bill"],
	["James", "Jim"],
	["John", "Jack"],
	["Margaret", "Peggy"],
	["Edward", "Ed"],
	["Sarah", "Sally"],
	["Andrew", "Andy"],
	["Anthony", "Tony"],
	["Deborah", "Debbie"],
]
m = len(first_nick)

for i in range(n):
	name = input()
	found = False
	for j in range(m):
		first, nick = first_nick[j]
		if first == name:
			print(nick)
			found = True
		elif nick == name:
			print(first)
			found = True
		if found:
			break
		
	if not found:
		print("Not found")
a = input()
b = input()

cnt = [0]*26
for i in a:
	if i.isalpha():
		cnt[ord(i.lower())-ord('a')] += 1
for i in b:
	if i.isalpha():
		cnt[ord(i.lower())-ord('a')] -= 1

anagram = True
for i in cnt:
	if i != 0:
		anagram = False
	
print("YES" if anagram else "NO")
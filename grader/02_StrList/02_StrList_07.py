s = input()

a = int(s[3::7])
b = int(s[7::5])
c = a+b+10000

t = [(c//1000)%10, (c//100)%10, (c//10)%10]
d = sum(t)
e = d%10 # + 1
print(f"{"".join(map(str, t))}{chr(ord('A')+e)}")
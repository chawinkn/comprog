id = input()

check = (11 - sum([(13 - i) * int(id[i]) for i in range(12)]) % 11) % 10

print(id[0], id[1:5], id[5:10], id[10:], check)

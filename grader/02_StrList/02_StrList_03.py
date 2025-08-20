d, m, y = [int(i) for i in input().split("/")]

month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print(f"{month[m-1]} {d}, {y}")

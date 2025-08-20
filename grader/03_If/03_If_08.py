d = int(input())
m = int(input())
y = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y -= 543
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
	day[1] += 1
print(sum(day[:m-1])+d)
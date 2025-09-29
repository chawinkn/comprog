import math

bd, bm, by, d, m, y = [int(e) for e in input().split()]
by -= 543
y -= 543

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# มกราคม, กุมภาพันธ์, มีนาคม, เมษายน, พฤษภาคม, มิถุนายน, กรกฏาคม, สิงหาคม, กันยายน, ตุลาคม, พฤศจิกายน, ธันวาคม

if (by%4 == 0 and by%100 != 0) or by%400 == 0:
	day[1] = 29
t = sum(day[bm-1:])-bd

t += 365*(y-by-1)
day[1] = 28

if (y%4 == 0 and y%100 != 0) or y%400 == 0:
	day[1] = 29
t += sum(day[:m-1])+d

print(t, f"{math.sin(2*math.pi*t/23):.2f}", f"{math.sin(2*math.pi*t/28):.2f}", f"{math.sin(2*math.pi*t/33):.2f}")
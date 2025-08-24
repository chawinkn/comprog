stu1 = [i for i in input().split()]
stu2 = [i for i in input().split()]
stu1[1] = float(stu1[1])
stu2[1] = float(stu2[1])
grade1 = stu1[2] == "A" and stu1[3] <= "C" and stu1[4] <= "C"
grade2 = stu2[2] == "A" and stu2[3] <= "C" and stu2[4] <= "C"

if not grade1 and not grade2:
	print("None")
elif grade1 and grade2:
	# GPAX
	if stu1[1] == stu2[1]:
		# cal1
		if stu1[3] == stu2[3]:
			# cal2
			if stu1[4] == stu2[4]:
				print("Both")
			else:
				print(stu1[0] if stu1[4] < stu2[4] else stu2[0])
		else:
			print(stu1[0] if stu1[3] < stu2[3] else stu2[0])
	else:
		print(stu1[0] if stu1[1] > stu2[1] else stu2[0])
elif grade1:
	print(stu1[0])
else:
	print(stu2[0])
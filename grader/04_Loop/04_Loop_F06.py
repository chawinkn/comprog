def print_triangle(h):
	# for i in range(h):
	# 	for j in range(h-i-1):
	# 		print(".", end="")
	# 	for j in range(2*i+1):
	# 		if j == 0 or j == 2*i or i == h-1:
	# 			print("*", end="")
	# 		else:
	# 			print(".", end="")
	# 	print()
	
	print("."*(h-1) + "*")
	for i in range(1, h-1):
		print("."*(h-i-1) + "*" + "."*(2*i-1) + "*")
	print("*"*(2*(h-1)+1))

exec(input()) # DON'T remove this line
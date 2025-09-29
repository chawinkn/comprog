from math import gcd

a, b, c = [i for i in input().split(",")]

num = (int(a)*10**len(b) + int(b or 0))*10**len(c) + int(c) - (int(a)*10**len(b) + int(b or 0))
de = 10**len(b) * (10**len(c) - 1)
# print(num, de)

gay = gcd(num, de)
print(f"{num//gay} / {de//gay}")

"""
5,,123

1000x = 5123.123123         * 10^len(c)
	x =    5.123123123

999x = 5123-5
"""

"""
5,19,123

	x =    5.19123123123

	100x    =    519.123123123  * 10^len(b)
	100000x = 519123.123123     * 10^len(c)

999x = 5123-5
"""
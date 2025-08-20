import math

def cal(n, m):
    return math.sqrt(2 * math.pi) * n ** (n + 1 / 2) * math.e ** (-n + 1 / (12 * n + m))

n = int(input())

print(cal(n, 1))
print(cal(n, 0))

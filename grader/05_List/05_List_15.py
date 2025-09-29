a = [int(i) for i in input().split()]
a.sort()

n = len(a)
ans = [a[i] for i in range(n) if i == n-1 or a[i] != a[i+1]]

print(len(ans))
print(ans[:10])
h = [int(i) for i in input().split()]
print(sum([1 for i in range(1, len(h)-1) if h[i-1] < h[i] > h[i+1]]))
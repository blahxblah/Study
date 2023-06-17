n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    min_a = min(a)
    max_b = max(b)
    if min_a >= max_b:
        break
    else:
        a[a.index(min_a)], b[b.index(max_b)] = max_b, min_a
        
print(sum(a))
n, k = map(int, input().split())
matrix = [ 0 for i in range(n+1)]
ans = 0
for i in range(k):
    s, e = map(int, input().split())
    
    matrix[e] += 1
    if matrix[e] > 6:
        pass
    elif matrix[e] % 2 == 0:
        ans += 1
        
print(ans)
print(matrix)
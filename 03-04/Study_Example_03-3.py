n, m = map(int, input().split())

matrix = []
min_values = []
for i in range(n) :
    row = list(map(int, input().split()))
    matrix.append(row)
    
for j in range(len(matrix)) : 
    matrix[j].sort()
    min_values.append(matrix[j][0])

min_values.sort(reverse=True)

print(min_values[0])
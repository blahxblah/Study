n = int(input())

array = []

def setting(array):
    return array[1]

for _ in range(n):
    array.append(tuple(input().split()))

result = sorted(array, key=setting)

for i in range(len(result)):
    print(result[i][0], end=' ')
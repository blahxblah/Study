N = int(input())
array = map(int, input().split())

cnt = [0 for _ in range(1000000)]

for n in array:
    cnt[n] += 1
        
for i in range(1000000):
    if cnt[i] == 1:
        print(i)
        break
    
print(array)
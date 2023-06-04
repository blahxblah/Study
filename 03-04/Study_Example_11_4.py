n = int(input())
money = list(map(int, input().split()))

money.sort()

summax = sum(money)

sumlist = money

result = 0
sum_subset = []


for i in range(2**n) :
    subset = [money[j] for j in range(len(money)) if (i & (1 << j))]
    
    sumlist.append(sum(subset))
    
    sum_subset = sum(subset)
        
for i in range(summax) :
    if i in sumlist :
        continue
    else:
        result = i
        
print(result)
print(sumlist)
print(sum_subset)
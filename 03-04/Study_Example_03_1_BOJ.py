money = [500, 100, 50, 10, 5, 1]
cash = int(input())
count = 0
for i in range(len(money)):
    count = count + cash // money[i]
    cash = cash % money[i]

print(count)
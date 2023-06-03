moneytype = [500, 100, 50, 10, 5, 1]
price = int(input())
changes = 1000 - price
cal_changes = changes
count = 0
for i in range(len(moneytype)):
    count = count + cal_changes // moneytype[i]
    cal_changes = cal_changes % moneytype[i]

print(count)
